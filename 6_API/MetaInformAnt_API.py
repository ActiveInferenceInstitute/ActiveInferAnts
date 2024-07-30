from fastapi import FastAPI, BackgroundTasks, HTTPException, Query, Depends
from pydantic import BaseModel, Field, HttpUrl, validator
from typing import Optional, Dict, List, Union, Any
from sqlalchemy.orm import Session
from ActiveInferAnts.core import AdvancedInferenceEngine, FederatedLearningEngine, SimulationEngine, EngineStatus
from ActiveInferAnts.security import SecureComputeSession, Authentication, Authorization, get_current_active_user
from ActiveInferAnts.utils import DataValidator, SimulationDataProcessor, create_session
from ActiveInferAnts.models import User
from ActiveInferAnts.logging import setup_logger
from ActiveInferAnts.config import Settings

app = FastAPI(
    title="MetaInformAnt API",
    version="1.0.0",
    description="Advanced API for decentralized, federated, and secure computation with the MetaInformAnt package",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

logger = setup_logger(__name__)
settings = Settings()

class AdvancedInferenceRequest(BaseModel):
    data: Dict[str, List[float]] = Field(..., example={"feature1": [0.1, 0.2], "feature2": [0.3, 0.4]})
    inference_type: Optional[str] = Field(default="default", description="Type of inference to perform")
    simulation_steps: Optional[int] = Field(default=100, gt=0, description="Number of simulation steps")
    agent_params: Optional[Dict[str, Any]] = Field(default=None, description="Parameters for agent configuration")
    niche_params: Optional[Dict[str, Any]] = Field(default=None, description="Parameters for niche configuration")
    secure_compute: Optional[bool] = Field(default=False, description="Flag to enable secure computation")
    callback_url: Optional[HttpUrl] = Field(default=None, description="URL for callback notifications")

    @validator('data')
    def validate_data(cls, v):
        if not v:
            raise ValueError("Data cannot be empty")
        return v

class FederatedLearningRequest(BaseModel):
    data: Dict[str, List[float]] = Field(..., example={"feature1": [0.1, 0.2], "feature2": [0.3, 0.4]})
    learning_rate: Optional[float] = Field(default=0.01, gt=0, le=1, description="Learning rate for the federated learning model")
    epochs: Optional[int] = Field(default=10, gt=0, description="Number of epochs for the federated learning")
    secure_compute: Optional[bool] = Field(default=False, description="Flag to enable secure computation")
    callback_url: Optional[HttpUrl] = Field(default=None, description="URL for callback notifications")

    @validator('data')
    def validate_data(cls, v):
        if not v:
            raise ValueError("Data cannot be empty")
        return v

class InferenceResponse(BaseModel):
    task_id: str
    status: str
    result: Optional[Union[Dict[str, float], str]] = None
    data: Dict[str, List[float]]
    inference_type: Optional[str] = "default"
    simulation_steps: Optional[int] = 100
    agent_params: Optional[Dict[str, Any]] = None
    niche_params: Optional[Dict[str, Any]] = None
    callback_url: Optional[HttpUrl] = None

class ErrorResponse(BaseModel):
    error: str
    details: Optional[Dict[str, Any]] = None

@app.post("/api/v1/advanced_infer/", response_model=InferenceResponse, responses={400: {"model": ErrorResponse}, 500: {"model": ErrorResponse}})
async def perform_advanced_inference(
    request: AdvancedInferenceRequest,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_active_user)
):
    try:
        DataValidator.validate_inference_data(request.data)
        
        inference_engine = AdvancedInferenceEngine(
            SecureComputeSession() if request.secure_compute else None,
            request.callback_url
        )
        
        task_id = await inference_engine.initialize_task()
        
        background_tasks.add_task(
            inference_engine.process_advanced,
            task_id,
            request.data,
            request.inference_type,
            request.simulation_steps,
            request.agent_params,
            request.niche_params
        )
        
        logger.info(f"Advanced inference task {task_id} started for user {current_user.username}")
        
        return InferenceResponse(
            task_id=task_id,
            status="PROCESSING",
            data=request.data,
            inference_type=request.inference_type,
            simulation_steps=request.simulation_steps,
            agent_params=request.agent_params,
            niche_params=request.niche_params,
            callback_url=request.callback_url
        )
    except ValueError as ve:
        logger.error(f"Value Error in advanced inference: {str(ve)}")
        raise HTTPException(status_code=400, detail={"error": "Invalid input", "details": str(ve)})
    except Exception as e:
        logger.exception(f"Unexpected error in advanced inference: {str(e)}")
        raise HTTPException(status_code=500, detail={"error": "Internal server error", "details": str(e)})

@app.post("/api/v1/federated_learn/", response_model=InferenceResponse, responses={400: {"model": ErrorResponse}, 500: {"model": ErrorResponse}})
async def perform_federated_learning(
    request: FederatedLearningRequest,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_active_user)
):
    try:
        DataValidator.validate_learning_data(request.data)
        
        learning_engine = FederatedLearningEngine(
            SecureComputeSession() if request.secure_compute else None,
            request.callback_url
        )
        
        task_id = await learning_engine.initialize_task()
        
        background_tasks.add_task(
            learning_engine.process_learning,
            task_id,
            request.data,
            request.learning_rate,
            request.epochs
        )
        
        logger.info(f"Federated learning task {task_id} initiated for user {current_user.username}")
        
        return InferenceResponse(
            task_id=task_id,
            status="PROCESSING",
            data=request.data,
            inference_type="federated_learning",
            simulation_steps=request.epochs,
            agent_params={"learning_rate": request.learning_rate},
            callback_url=request.callback_url
        )
    except ValueError as ve:
        logger.error(f"Value Error in federated learning: {str(ve)}")
        raise HTTPException(status_code=400, detail={"error": "Invalid input", "details": str(ve)})
    except Exception as e:
        logger.exception(f"Unexpected error in federated learning: {str(e)}")
        raise HTTPException(status_code=500, detail={"error": "Internal server error", "details": str(e)})

@app.get("/api/v1/status/", response_model=Dict[str, Union[str, Dict[str, str]]])
async def check_detailed_status(
    simulation_id: Optional[str] = Query(None, description="Simulation ID to fetch detailed status for"),
    db: Session = Depends(create_session),
    current_user: User = Depends(get_current_active_user)
):
    try:
        if simulation_id:
            engine_status = await SimulationEngine.get_status(simulation_id, db)
            if not engine_status:
                raise HTTPException(status_code=404, detail={"error": "Simulation not found"})
            return {"status": engine_status, "simulation_id": simulation_id}
        else:
            engine_status = {
                "AdvancedInferenceEngine": await AdvancedInferenceEngine.get_status(db),
                "FederatedLearningEngine": await FederatedLearningEngine.get_status(db)
            }
            return {"status": engine_status}
    except Exception as e:
        logger.exception(f"Error fetching status: {str(e)}")
        raise HTTPException(status_code=500, detail={"error": "Internal server error", "details": str(e)})

@app.get("/api/v1/health")
async def health_check():
    return {"status": "healthy", "version": app.version}
