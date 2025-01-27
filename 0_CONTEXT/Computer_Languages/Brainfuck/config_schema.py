"""
Configuration schema and validation for Brainfuck Active Inference.
"""
from pydantic import BaseModel, Field
from typing import Dict, Optional

class SimulationConfig(BaseModel):
    """Configuration schema for active inference simulation."""
    initial_values: Dict[str, int] = Field(
        default_factory=lambda: {
            "sensory_input": 10,
            "prediction": 10,
            "learning_rate": 3,
            "precision": 5,
            "temporal_integration": 1,
            "exploration_factor": 2,
            "model_complexity": 3,
            "goal_directed_behavior": 4,
            "uncertainty": 2
        }
    )
    max_iterations: int = Field(default=1000, gt=0)
    visualization_enabled: bool = Field(default=True)
    output_directory: Optional[str] = Field(default="./output")
    logging_level: str = Field(default="INFO")
    
    class Config:
        extra = "forbid" 