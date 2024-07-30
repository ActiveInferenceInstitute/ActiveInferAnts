from fastapi import FastAPI, HTTPException, Depends, Query, BackgroundTasks
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
from typing import Dict, List, Any, Optional
from sqlalchemy import create_engine, Column, Integer, String, JSON, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import requests
import json
import pymongo
from pymongo import MongoClient, IndexModel
import redis
from elasticsearch import Elasticsearch
from neo4j import GraphDatabase
from datetime import datetime
import logging
from functools import lru_cache
import asyncio
from aiocache import cached, Cache
from aiocache.serializers import JsonSerializer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import JSONResponse as StarletteJSONResponse

app = FastAPI(
    title="Knowledge API",
    description="Advanced API for managing knowledge across multiple databases",
    version="2.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
class Config:
    SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/knowledge_db"
    MONGODB_URL = "mongodb://localhost:27017/"
    REDIS_URL = "redis://localhost:6379/0"
    ELASTICSEARCH_URL = "http://localhost:9200"
    NEO4J_URL = "bolt://localhost:7687"
    NEO4J_USER = "neo4j"
    NEO4J_PASSWORD = "password"
    LOG_LEVEL = logging.INFO
    CACHE_TTL = 300  # 5 minutes
    API_KEY = "your-secret-api-key"  # Add this for API key authentication

config = Config()

# Logging setup
logging.basicConfig(level=config.LOG_LEVEL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# SQLAlchemy setup
engine = create_engine(config.SQLALCHEMY_DATABASE_URL, pool_size=20, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class KnowledgeItem(Base):
    __tablename__ = "knowledge_items"
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True, unique=True)
    content = Column(JSON)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

Base.metadata.create_all(bind=engine)

# MongoDB setup
mongo_client = MongoClient(config.MONGODB_URL)
mongo_db = mongo_client["knowledge_db"]
mongo_collection = mongo_db["knowledge_items"]
mongo_collection.create_index([("source", pymongo.ASCENDING)], unique=True)

# Redis setup
redis_client = redis.from_url(config.REDIS_URL)

# Elasticsearch setup
es_client = Elasticsearch([config.ELASTICSEARCH_URL])

# Neo4j setup
neo4j_driver = GraphDatabase.driver(config.NEO4J_URL, auth=(config.NEO4J_USER, config.NEO4J_PASSWORD))

# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()

# API Key authentication
def api_key_auth(api_key: str = Query(..., description="API Key for authentication")):
    if api_key != config.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return api_key

class KnowledgeBase(BaseModel):
    source: str = Field(..., description="Unique identifier for the knowledge item")
    content: Dict[str, Any] = Field(..., description="Content of the knowledge item")

    @validator('source')
    def source_must_be_valid(cls, v):
        if not v.strip():
            raise ValueError('Source must not be empty')
        return v

    class Config:
        schema_extra = {
            "example": {
                "source": "example_source",
                "content": {"key": "value"}
            }
        }

@app.post("/api/knowledge/", response_model=Dict[str, str], status_code=201)
async def create_knowledge(
    knowledge: KnowledgeBase,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    api_key: str = Depends(api_key_auth)
):
    try:
        # SQLite
        db_item = KnowledgeItem(**knowledge.dict())
        db.add(db_item)
        await db.commit()
        await db.refresh(db_item)
        
        # Asynchronously update other databases
        background_tasks.add_task(update_other_databases, knowledge)
        
        logger.info(f"Knowledge created: {knowledge.source}")
        return JSONResponse(content={"message": "Knowledge created successfully", "id": db_item.id}, status_code=201)
    except Exception as e:
        logger.error(f"Error creating knowledge: {str(e)}")
        raise HTTPException(status_code=500, detail="Error creating knowledge")

async def update_other_databases(knowledge: KnowledgeBase):
    try:
        # MongoDB
        await asyncio.to_thread(mongo_collection.insert_one, knowledge.dict())
        
        # Redis
        await asyncio.to_thread(redis_client.set, f"knowledge:{knowledge.source}", json.dumps(knowledge.dict()))
        
        # Elasticsearch
        await asyncio.to_thread(es_client.index, index="knowledge", id=knowledge.source, body=knowledge.dict())
        
        # Neo4j
        async with neo4j_driver.session() as session:
            await session.run("CREATE (k:Knowledge {source: $source, content: $content})",
                              source=knowledge.source, content=json.dumps(knowledge.content))
    except Exception as e:
        logger.error(f"Error updating other databases: {str(e)}")

@app.get("/api/knowledge/{source}", response_model=Dict[str, Dict[str, Any]])
@cached(ttl=config.CACHE_TTL, cache=Cache.MEMORY, serializer=JsonSerializer())
async def read_knowledge(
    source: str,
    db: Session = Depends(get_db),
    api_key: str = Depends(api_key_auth)
):
    results = {}
    
    try:
        # SQLite
        db_item = await db.execute(KnowledgeItem.__table__.select().where(KnowledgeItem.source == source))
        db_item = db_item.first()
        if db_item:
            results["sqlite"] = db_item.content
        
        # Asynchronously fetch from other databases
        other_results = await asyncio.gather(
            fetch_from_mongodb(source),
            fetch_from_redis(source),
            fetch_from_elasticsearch(source),
            fetch_from_neo4j(source)
        )
        
        results.update(dict(filter(None, other_results)))
        
        if not results:
            raise HTTPException(status_code=404, detail="Knowledge not found")
        
        logger.info(f"Knowledge retrieved: {source}")
        return results
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error retrieving knowledge: {str(e)}")
        raise HTTPException(status_code=500, detail="Error retrieving knowledge")

async def fetch_from_mongodb(source):
    mongo_item = await asyncio.to_thread(mongo_collection.find_one, {"source": source})
    return ("mongodb", mongo_item["content"]) if mongo_item else None

async def fetch_from_redis(source):
    redis_item = await asyncio.to_thread(redis_client.get, f"knowledge:{source}")
    return ("redis", json.loads(redis_item)["content"]) if redis_item else None

async def fetch_from_elasticsearch(source):
    es_result = await asyncio.to_thread(es_client.get, index="knowledge", id=source, ignore=[404])
    return ("elasticsearch", es_result["_source"]["content"]) if es_result.get('found') else None

async def fetch_from_neo4j(source):
    async with neo4j_driver.session() as session:
        result = await session.run("MATCH (k:Knowledge {source: $source}) RETURN k.content", source=source)
        record = await result.single()
        return ("neo4j", json.loads(record["k.content"])) if record else None

@app.put("/api/knowledge/{source}", response_model=Dict[str, str])
async def update_knowledge(
    source: str,
    knowledge: KnowledgeBase,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    api_key: str = Depends(api_key_auth)
):
    try:
        # SQLite
        db_item = await db.execute(KnowledgeItem.__table__.select().where(KnowledgeItem.source == source))
        db_item = db_item.first()
        if db_item:
            await db.execute(KnowledgeItem.__table__.update().where(KnowledgeItem.source == source).values(content=knowledge.content, updated_at=func.now()))
            await db.commit()
        else:
            raise HTTPException(status_code=404, detail="Knowledge not found in SQLite")
        
        # Asynchronously update other databases
        background_tasks.add_task(update_other_databases_on_put, source, knowledge)
        
        logger.info(f"Knowledge updated: {source}")
        return {"message": "Knowledge updated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating knowledge: {str(e)}")
        raise HTTPException(status_code=500, detail="Error updating knowledge")

async def update_other_databases_on_put(source: str, knowledge: KnowledgeBase):
    try:
        # MongoDB
        await asyncio.to_thread(mongo_collection.update_one, {"source": source}, {"$set": knowledge.dict()})
        
        # Redis
        await asyncio.to_thread(redis_client.set, f"knowledge:{source}", json.dumps(knowledge.dict()))
        
        # Elasticsearch
        await asyncio.to_thread(es_client.update, index="knowledge", id=source, body={"doc": knowledge.dict()})
        
        # Neo4j
        async with neo4j_driver.session() as session:
            await session.run("MATCH (k:Knowledge {source: $source}) SET k.content = $content",
                              source=source, content=json.dumps(knowledge.content))
    except Exception as e:
        logger.error(f"Error updating other databases: {str(e)}")

@app.delete("/api/knowledge/{source}", response_model=Dict[str, str])
async def delete_knowledge(
    source: str,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    api_key: str = Depends(api_key_auth)
):
    try:
        # SQLite
        result = await db.execute(KnowledgeItem.__table__.delete().where(KnowledgeItem.source == source))
        await db.commit()
        
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Knowledge not found")
        
        # Asynchronously delete from other databases
        background_tasks.add_task(delete_from_other_databases, source)
        
        logger.info(f"Knowledge deleted: {source}")
        return {"message": "Knowledge deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting knowledge: {str(e)}")
        raise HTTPException(status_code=500, detail="Error deleting knowledge")

async def delete_from_other_databases(source: str):
    try:
        # MongoDB
        await asyncio.to_thread(mongo_collection.delete_one, {"source": source})
        
        # Redis
        await asyncio.to_thread(redis_client.delete, f"knowledge:{source}")
        
        # Elasticsearch
        await asyncio.to_thread(es_client.delete, index="knowledge", id=source, ignore=[404])
        
        # Neo4j
        async with neo4j_driver.session() as session:
            await session.run("MATCH (k:Knowledge {source: $source}) DELETE k", source=source)
    except Exception as e:
        logger.error(f"Error deleting from other databases: {str(e)}")

@app.get("/api/knowledge/", response_model=List[Dict[str, Any]])
async def list_knowledge(
    skip: int = Query(0, description="Number of items to skip"),
    limit: int = Query(10, description="Number of items to return"),
    db: Session = Depends(get_db),
    api_key: str = Depends(api_key_auth)
):
    try:
        query = KnowledgeItem.__table__.select().offset(skip).limit(limit)
        result = await db.execute(query)
        items = result.fetchall()
        return [{"source": item.source, "content": item.content, "created_at": item.created_at, "updated_at": item.updated_at} for item in items]
    except Exception as e:
        logger.error(f"Error listing knowledge: {str(e)}")
        raise HTTPException(status_code=500, detail="Error listing knowledge")

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up Knowledge API")
    # Perform any necessary startup tasks (e.g., ensuring indexes, checking connections)
    await check_database_connections()

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down Knowledge API")
    # Perform any necessary cleanup tasks
    await close_database_connections()

async def check_database_connections():
    try:
        # Check SQLite connection
        async with engine.connect() as conn:
            await conn.execute("SELECT 1")
        
        # Check MongoDB connection
        await asyncio.to_thread(mongo_client.server_info)
        
        # Check Redis connection
        await asyncio.to_thread(redis_client.ping)
        
        # Check Elasticsearch connection
        await asyncio.to_thread(es_client.ping)
        
        # Check Neo4j connection
        async with neo4j_driver.session() as session:
            await session.run("RETURN 1")
        
        logger.info("All database connections established successfully")
    except Exception as e:
        logger.error(f"Error checking database connections: {str(e)}")
        raise

async def close_database_connections():
    try:
        await engine.dispose()
        mongo_client.close()
        await asyncio.to_thread(redis_client.close)
        await asyncio.to_thread(es_client.close)
        await neo4j_driver.close()
        logger.info("All database connections closed successfully")
    except Exception as e:
        logger.error(f"Error closing database connections: {str(e)}")

# Custom exception handler
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return StarletteJSONResponse(
        status_code=exc.status_code,
        content={"message": str(exc.detail)}
    )

# Root redirect
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=4)
