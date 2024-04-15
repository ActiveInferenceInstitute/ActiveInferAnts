from fastapi import FastAPI, BackgroundTasks, HTTPException, Query, Depends
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, Dict, List, Union, Any
from sqlalchemy.orm import Session
from ActiveInferAnts.core import AdvancedInferenceEngine, FederatedLearningEngine, SimulationEngine, EngineStatus
from ActiveInferAnts.security import SecureComputeSession, Authentication, Authorization, get_current_active_user
from ActiveInferAnts.utils import DataValidator, SimulationDataProcessor, create_session
from ActiveInferAnts.models import User

app = FastAPI(title="MetaInformAnt API", version="2.1", description="Enhanced API for decentralized, federated, and secure computation with the MetaInformAnt package")

class AdvancedInferenceRequest(BaseModel):
    data: Dict[str, List[float]] = Field(..., example={"feature1": [0.1, 0.2], "feature2": [0.3, 0.4]})
    inference_type: Optional[str] = Field(default="default", description="Type of inference to perform")
    simulation_steps: Optional[int] = Field(default=100, gt=0, description="Number of simulation steps")
    agent_params: Optional[Dict[str, Any]] = None
    niche_params: Optional[Dict[str, Any]] = None
    secure_compute: Optional[bool] = Field(default=False, description="Flag to enable secure computation")
    callback_url: Optional[HttpUrl] = None

class FederatedLearningRequest(BaseModel):
    data: Dict[str, List[float]] = Field(..., example={"feature1": [0.1, 0.2], "feature2": [0.3, 0.4]})
    learning_rate: Optional[float] = Field(default=0.01, gt=0, description="Learning rate for the federated learning model")
    epochs: Optional[int] = Field(default=10, gt=0, description="Number of epochs for the federated learning")
    secure_compute: Optional[bool] = Field(default=False, description="Flag to enable secure computation")
    callback_url: Optional[HttpUrl] = None

class InferenceResponse(BaseModel):
    result: Union[Dict[str, float], str]
    data: dict
    inference_type: Optional[str] = "default"
    simulation_steps: Optional[int] = 100
    agent_params: Optional[dict] = None
    niche_params: Optional[dict] = None
    callback_url: Optional[HttpUrl] = None

class ErrorResponse(BaseModel):
    error: Optional[str] = None

@app.post("/advanced_infer/", response_model=InferenceResponse)
async def perform_advanced_inference(request: AdvancedInferenceRequest, background_tasks: BackgroundTasks, current_user: User = Depends(get_current_active_user)):
    try:
        inference_engine = AdvancedInferenceEngine(SecureComputeSession(), request.callback_url) if request.secure_compute else AdvancedInferenceEngine(callback_url=request.callback_url)
        
        background_tasks.add_task(inference_engine.process_advanced, request.data, request.inference_type, request.simulation_steps, request.agent_params, request.niche_params)
        return {"result": "Advanced inference task started successfully", "data": request.data, "inference_type": request.inference_type, "simulation_steps": request.simulation_steps, "callback_url": request.callback_url}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Value Error: {str(ve)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected Error: {str(e)}")

@app.post("/federated_learn/", response_model=InferenceResponse)
async def perform_federated_learning(request: FederatedLearningRequest, background_tasks: BackgroundTasks, current_user: User = Depends(get_current_active_user)):
    try:
        learning_engine = FederatedLearningEngine(SecureComputeSession(), request.callback_url) if request.secure_compute else FederatedLearningEngine(callback_url=request.callback_url)
        
        background_tasks.add_task(learning_engine.process_learning, request.data, request.learning_rate, request.epochs)
        return {"result": "Federated learning task initiated successfully", "data": request.data, "learning_rate": request.learning_rate, "epochs": request.epochs, "callback_url": request.callback_url}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Value Error: {str(ve)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected Error: {str(e)}")

@app.get("/detailed_status/", response_model=Dict[str, Union[str, Dict[str, str]]])
async def check_detailed_status(simulation_id: Optional[str] = Query(None, description="Simulation ID to fetch detailed status for"), db: Session = Depends(create_session)):
    # Enhanced logic for querying the AdvancedInferenceEngine's or FederatedLearningEngine's current state with database support
    if simulation_id:
        engine_status = SimulationEngine.get_status(simulation_id, db)
        return {"status": engine_status, "simulation_id": simulation_id}
    else:
        engine_status = {"AdvancedInferenceEngine": AdvancedInferenceEngine.get_status(db), "FederatedLearningEngine": FederatedLearningEngine.get_status(db)}
        return {"status": engine_status}
