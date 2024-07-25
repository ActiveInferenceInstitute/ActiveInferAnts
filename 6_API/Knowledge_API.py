from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional
from sqlalchemy import create_engine, Column, Integer, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import requests
import json
import pymongo
from pymongo import MongoClient
import redis
from elasticsearch import Elasticsearch
from neo4j import GraphDatabase
from datetime import datetime
import logging
from functools import lru_cache

app = FastAPI(title="Knowledge API", description="API for managing knowledge across multiple databases", version="1.0.0")

# Configuration
class Config:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./knowledge.db"
    MONGODB_URL = "mongodb://localhost:27017/"
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    ELASTICSEARCH_URL = "http://localhost:9200"
    NEO4J_URL = "bolt://localhost:7687"
    NEO4J_USER = "neo4j"
    NEO4J_PASSWORD = "password"

config = Config()

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# SQLAlchemy setup
engine = create_engine(config.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class KnowledgeItem(Base):
    __tablename__ = "knowledge_items"
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True, unique=True)
    content = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# MongoDB setup
mongo_client = MongoClient(config.MONGODB_URL)
mongo_db = mongo_client["knowledge_db"]
mongo_collection = mongo_db["knowledge_items"]

# Redis setup
redis_client = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=0)

# Elasticsearch setup
es_client = Elasticsearch(config.ELASTICSEARCH_URL)

# Neo4j setup
neo4j_driver = GraphDatabase.driver(config.NEO4J_URL, auth=(config.NEO4J_USER, config.NEO4J_PASSWORD))

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class KnowledgeBase(BaseModel):
    source: str = Field(..., description="Unique identifier for the knowledge item")
    content: Dict[str, Any] = Field(..., description="Content of the knowledge item")

    class Config:
        schema_extra = {
            "example": {
                "source": "example_source",
                "content": {"key": "value"}
            }
        }

@app.post("/knowledge/", response_model=Dict[str, str], status_code=201)
async def create_knowledge(knowledge: KnowledgeBase, db: Session = Depends(get_db)):
    try:
        # SQLite
        db_item = KnowledgeItem(**knowledge.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        
        # MongoDB
        mongo_collection.insert_one(knowledge.dict())
        
        # Redis
        redis_client.set(f"knowledge:{knowledge.source}", json.dumps(knowledge.dict()))
        
        # Elasticsearch
        es_client.index(index="knowledge", id=knowledge.source, body=knowledge.dict())
        
        # Neo4j
        with neo4j_driver.session() as session:
            session.run("CREATE (k:Knowledge {source: $source, content: $content})",
                        source=knowledge.source, content=json.dumps(knowledge.content))
        
        logger.info(f"Knowledge created: {knowledge.source}")
        return {"message": "Knowledge created in all databases"}
    except Exception as e:
        logger.error(f"Error creating knowledge: {str(e)}")
        raise HTTPException(status_code=500, detail="Error creating knowledge")

@app.get("/knowledge/{source}", response_model=Dict[str, Dict[str, Any]])
async def read_knowledge(source: str, db: Session = Depends(get_db)):
    results = {}
    
    try:
        # SQLite
        db_item = db.query(KnowledgeItem).filter(KnowledgeItem.source == source).first()
        if db_item:
            results["sqlite"] = db_item.content
        
        # MongoDB
        mongo_item = mongo_collection.find_one({"source": source})
        if mongo_item:
            results["mongodb"] = mongo_item["content"]
        
        # Redis
        redis_item = redis_client.get(f"knowledge:{source}")
        if redis_item:
            results["redis"] = json.loads(redis_item)["content"]
        
        # Elasticsearch
        es_result = es_client.get(index="knowledge", id=source, ignore=[404])
        if es_result.get('found'):
            results["elasticsearch"] = es_result["_source"]["content"]
        
        # Neo4j
        with neo4j_driver.session() as session:
            neo4j_result = session.run("MATCH (k:Knowledge {source: $source}) RETURN k.content", source=source)
            record = neo4j_result.single()
            if record:
                results["neo4j"] = json.loads(record["k.content"])
        
        if not results:
            raise HTTPException(status_code=404, detail="Knowledge not found")
        
        logger.info(f"Knowledge retrieved: {source}")
        return results
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error retrieving knowledge: {str(e)}")
        raise HTTPException(status_code=500, detail="Error retrieving knowledge")

@app.put("/knowledge/{source}", response_model=Dict[str, str])
async def update_knowledge(source: str, knowledge: KnowledgeBase, db: Session = Depends(get_db)):
    try:
        # SQLite
        db_item = db.query(KnowledgeItem).filter(KnowledgeItem.source == source).first()
        if db_item:
            db_item.content = knowledge.content
            db_item.updated_at = datetime.utcnow()
            db.commit()
        else:
            raise HTTPException(status_code=404, detail="Knowledge not found in SQLite")
        
        # MongoDB
        result = mongo_collection.update_one({"source": source}, {"$set": knowledge.dict()})
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Knowledge not found in MongoDB")
        
        # Redis
        if not redis_client.exists(f"knowledge:{source}"):
            raise HTTPException(status_code=404, detail="Knowledge not found in Redis")
        redis_client.set(f"knowledge:{source}", json.dumps(knowledge.dict()))
        
        # Elasticsearch
        if not es_client.exists(index="knowledge", id=source):
            raise HTTPException(status_code=404, detail="Knowledge not found in Elasticsearch")
        es_client.update(index="knowledge", id=source, body={"doc": knowledge.dict()})
        
        # Neo4j
        with neo4j_driver.session() as session:
            result = session.run("MATCH (k:Knowledge {source: $source}) SET k.content = $content RETURN k",
                                 source=source, content=json.dumps(knowledge.content))
            if not result.single():
                raise HTTPException(status_code=404, detail="Knowledge not found in Neo4j")
        
        logger.info(f"Knowledge updated: {source}")
        return {"message": "Knowledge updated in all databases"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating knowledge: {str(e)}")
        raise HTTPException(status_code=500, detail="Error updating knowledge")

@app.delete("/knowledge/{source}", response_model=Dict[str, str])
async def delete_knowledge(source: str, db: Session = Depends(get_db)):
    try:
        # SQLite
        db_item = db.query(KnowledgeItem).filter(KnowledgeItem.source == source).first()
        if db_item:
            db.delete(db_item)
            db.commit()
        
        # MongoDB
        mongo_collection.delete_one({"source": source})
        
        # Redis
        redis_client.delete(f"knowledge:{source}")
        
        # Elasticsearch
        es_client.delete(index="knowledge", id=source, ignore=[404])
        
        # Neo4j
        with neo4j_driver.session() as session:
            session.run("MATCH (k:Knowledge {source: $source}) DELETE k", source=source)
        
        logger.info(f"Knowledge deleted: {source}")
        return {"message": "Knowledge deleted from all databases"}
    except Exception as e:
        logger.error(f"Error deleting knowledge: {str(e)}")
        raise HTTPException(status_code=500, detail="Error deleting knowledge")

@app.get("/knowledge/", response_model=List[Dict[str, Any]])
async def list_knowledge(
    skip: int = Query(0, description="Number of items to skip"),
    limit: int = Query(10, description="Number of items to return"),
    db: Session = Depends(get_db)
):
    try:
        db_items = db.query(KnowledgeItem).offset(skip).limit(limit).all()
        return [{"source": item.source, "content": item.content, "created_at": item.created_at, "updated_at": item.updated_at} for item in db_items]
    except Exception as e:
        logger.error(f"Error listing knowledge: {str(e)}")
        raise HTTPException(status_code=500, detail="Error listing knowledge")

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up Knowledge API")
    # Perform any necessary startup tasks (e.g., ensuring indexes, checking connections)

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down Knowledge API")
    # Perform any necessary cleanup tasks

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
