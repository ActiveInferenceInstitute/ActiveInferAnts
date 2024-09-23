import requests
import random
import time
from typing import List, Dict, Optional, Tuple, Any
import numpy as np
from scipy.stats import entropy
import logging
from dataclasses import dataclass, field
from enum import Enum, auto
from abc import ABC, abstractmethod
import asyncio
import aiohttp
from tenacity import retry, stop_after_attempt, wait_exponential
import os
import argparse

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CodaAPIError(Exception):
    """Custom exception for Coda API errors."""
    pass

class CodaAPI:
    def __init__(self, api_token: str):
        """Initialize the CodaAPI client with the provided API token."""
        self.base_url = "https://coda.io/apis/v1"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
        self.session = aiohttp.ClientSession(headers=self.headers)
    
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def _make_request(self, method: str, endpoint: str, payload: Optional[Dict] = None, params: Optional[Dict] = None) -> Dict:
        url = f"{self.base_url}/{endpoint}"
        try:
            async with self.session.request(method, url, json=payload, params=params) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientResponseError as e:
            logger.error(f"API request failed: {e}")
            raise CodaAPIError(f"API request failed: {e}")

    async def create_doc(self, title: str, source_doc: Optional[str] = None, timezone: Optional[str] = None) -> Dict:
        """Create a new Coda document."""
        payload = {"title": title, "sourceDoc": source_doc, "timezone": timezone}
        return await self._make_request("POST", "docs", payload=payload)

    async def list_docs(self, is_owner: Optional[bool] = None, query: Optional[str] = None) -> Dict:
        params = {"isOwner": is_owner, "query": query}
        return await self._make_request("GET", "docs", params=params)

    async def get_doc(self, doc_id: str) -> Dict:
        return await self._make_request("GET", f"docs/{doc_id}")

    async def delete_doc(self, doc_id: str) -> Dict:
        return await self._make_request("DELETE", f"docs/{doc_id}")

    async def create_table(self, doc_id: str, table_name: str, columns: List[Dict]) -> Dict:
        payload = {"name": table_name, "columns": columns}
        return await self._make_request("POST", f"docs/{doc_id}/tables", payload=payload)

    async def add_row(self, doc_id: str, table_id: str, row_data: Dict) -> Dict:
        payload = {"rows": [row_data]}
        return await self._make_request("POST", f"docs/{doc_id}/tables/{table_id}/rows", payload=payload)

    async def get_rows(self, doc_id: str, table_id: str, query: Optional[str] = None) -> Dict:
        params = {"query": query}
        return await self._make_request("GET", f"docs/{doc_id}/tables/{table_id}/rows", params=params)

    async def update_row(self, doc_id: str, table_id: str, row_id: str, row_data: Dict) -> Dict:
        payload = {"row": row_data}
        return await self._make_request("PUT", f"docs/{doc_id}/tables/{table_id}/rows/{row_id}", payload=payload)

class AntSpecies(Enum):
    FIRE_ANT = auto()
    CARPENTER_ANT = auto()
    LEAFCUTTER_ANT = auto()
    ARMY_ANT = auto()
    BULLET_ANT = auto()

@dataclass
class AntAttributes:
    speed: float
    strength: float
    perception: float

class ActiveInferenceModel(ABC):
    @abstractmethod
    def perceive(self, observation: np.ndarray) -> None:
        pass

    @abstractmethod
    def act(self) -> np.ndarray:
        pass

    @abstractmethod
    def calculate_efe(self, action: np.ndarray) -> float:
        pass

class ActiveInferenceAnt(ActiveInferenceModel):
    def __init__(self, name: str, species: AntSpecies, position: np.ndarray):
        """Initialize an Active Inference Ant with given attributes."""
        self.name = name
        self.species = species
        self.position = position
        self.attributes = self._initialize_attributes()
        self.A_matrix = np.random.rand(3, 3)  # Sensory mapping
        self.B_matrix = np.random.rand(3, 3, 3)  # Transition probabilities
        self.C_matrix = np.random.rand(3)  # Preferred outcomes
        self.D_matrix = np.random.rand(3)  # Initial beliefs
        self.learning_rate = 0.01

    def _initialize_attributes(self) -> AntAttributes:
        base_attributes = {
            AntSpecies.FIRE_ANT: AntAttributes(speed=0.7, strength=0.6, perception=0.5),
            AntSpecies.CARPENTER_ANT: AntAttributes(speed=0.5, strength=0.8, perception=0.6),
            AntSpecies.LEAFCUTTER_ANT: AntAttributes(speed=0.6, strength=0.7, perception=0.7),
            AntSpecies.ARMY_ANT: AntAttributes(speed=0.8, strength=0.7, perception=0.6),
            AntSpecies.BULLET_ANT: AntAttributes(speed=0.6, strength=0.9, perception=0.5)
        }
        attributes = base_attributes[self.species]
        return AntAttributes(
            speed=np.clip(attributes.speed + random.uniform(-0.1, 0.1), 0, 1),
            strength=np.clip(attributes.strength + random.uniform(-0.1, 0.1), 0, 1),
            perception=np.clip(attributes.perception + random.uniform(-0.1, 0.1), 0, 1)
        )

    def perceive(self, observation: np.ndarray) -> None:
        """Update the ant's beliefs based on the observation."""
        prediction = np.dot(self.A_matrix, self.position)
        prediction_error = observation - prediction
        self.position -= self.attributes.perception * self.learning_rate * prediction_error
        self._update_matrices(observation, prediction_error)

    def _update_matrices(self, observation: np.ndarray, prediction_error: np.ndarray) -> None:
        self.A_matrix += self.learning_rate * np.outer(prediction_error, self.position)
        self.C_matrix += self.learning_rate * (observation - self.C_matrix)

    def act(self) -> np.ndarray:
        """Determine the next action based on expected free energy."""
        possible_actions = np.eye(3)
        efe_scores = [self.calculate_efe(action) for action in possible_actions]
        return possible_actions[np.argmin(efe_scores)]

    def calculate_efe(self, action: np.ndarray) -> float:
        """Calculate the expected free energy for a given action."""
        future_state = np.dot(self.B_matrix, action)
        expected_observation = np.dot(self.A_matrix, future_state)
        pragmatic_value = np.dot(self.C_matrix, expected_observation)
        epistemic_value = entropy(future_state)
        return -(self.attributes.strength * pragmatic_value + self.attributes.speed * epistemic_value)

@dataclass
class SimulationConfig:
    """Configuration for the ant simulation."""
    num_ants: int
    num_steps: int
    environment_size: Tuple[int, int] = (100, 100)
    pheromone_decay_rate: float = 0.95

class Environment:
    def __init__(self, config: SimulationConfig):
        self.size = config.environment_size
        self.pheromone_map = np.zeros(self.size)
        self.decay_rate = config.pheromone_decay_rate

    def update_pheromones(self, ant_positions: List[np.ndarray]):
        for position in ant_positions:
            x, y = position[:2].astype(int)
            self.pheromone_map[x, y] += 1
        self.pheromone_map *= self.decay_rate

    def get_local_pheromones(self, position: np.ndarray, radius: int = 3) -> np.ndarray:
        x, y = position[:2].astype(int)
        x_min, x_max = max(0, x - radius), min(self.size[0], x + radius + 1)
        y_min, y_max = max(0, y - radius), min(self.size[1], y + radius + 1)
        return self.pheromone_map[x_min:x_max, y_min:y_max]

class AntSimulation:
    def __init__(self, coda_api: CodaAPI, doc_id: str, table_id: str, config: SimulationConfig):
        self.coda_api = coda_api
        self.doc_id = doc_id
        self.table_id = table_id
        self.config = config
        self.ants: List[ActiveInferenceAnt] = []
        self.environment = Environment(config)

    async def create_ant(self, name: str, species: AntSpecies):
        position = np.random.rand(3) * self.config.environment_size[0]
        ant = ActiveInferenceAnt(name, species, position)
        self.ants.append(ant)
        row_data = {
            "cells": [
                {"column": "Name", "value": name},
                {"column": "Species", "value": species.name},
                {"column": "Position", "value": position.tolist()},
                {"column": "Speed", "value": ant.attributes.speed},
                {"column": "Strength", "value": ant.attributes.strength},
                {"column": "Perception", "value": ant.attributes.perception},
                {"column": "Action", "value": ""},
                {"column": "Observation", "value": ""}
            ]
        }
        await self.coda_api.add_row(self.doc_id, self.table_id, row_data)

    async def simulate(self):
        for step in range(self.config.num_steps):
            logger.info(f"Simulation step: {step + 1}/{self.config.num_steps}")
            ant_positions = []
            update_tasks = []
            
            for ant in self.ants:
                action = ant.act()
                observation = self._generate_observation(ant)
                ant.perceive(observation)
                ant_positions.append(ant.position)
                
                update_tasks.append(self._update_coda_table(ant, action, observation))
            
            self.environment.update_pheromones(ant_positions)
            await asyncio.gather(*update_tasks)
            
            await asyncio.sleep(1)  # Simulate time delay between steps

    def _generate_observation(self, ant: ActiveInferenceAnt) -> np.ndarray:
        local_pheromones = self.environment.get_local_pheromones(ant.position)
        base_observation = np.random.rand(3) + np.mean(local_pheromones)
        return base_observation * ant.attributes.perception

    async def _update_coda_table(self, ant: ActiveInferenceAnt, action: np.ndarray, observation: np.ndarray):
        rows = await self.coda_api.get_rows(self.doc_id, self.table_id, query=f'Name:"{ant.name}"')
        row_id = rows['items'][0]['id']
        row_data = {
            "cells": [
                {"column": "Position", "value": ant.position.tolist()},
                {"column": "Action", "value": action.tolist()},
                {"column": "Observation", "value": observation.tolist()}
            ]
        }
        await self.coda_api.update_row(self.doc_id, self.table_id, row_id, row_data)

async def run_simulation(api_token: str, config: SimulationConfig) -> Tuple[str, str]:
    async with CodaAPI(api_token) as coda_api:
        # Create a new doc
        new_doc = await coda_api.create_doc(title="Advanced Active Inference Ants Simulation")
        doc_id = new_doc['id']
        logger.info(f"Created doc: {new_doc['name']} (ID: {doc_id})")

        # Create a table for the simulation
        table = await coda_api.create_table(doc_id, "Ant Simulation", [
            {"name": "Name", "type": "text"},
            {"name": "Species", "type": "text"},
            {"name": "Position", "type": "array"},
            {"name": "Speed", "type": "number"},
            {"name": "Strength", "type": "number"},
            {"name": "Perception", "type": "number"},
            {"name": "Action", "type": "array"},
            {"name": "Observation", "type": "array"}
        ])
        table_id = table['id']
        logger.info(f"Created table: {table['name']} (ID: {table_id})")

        # Initialize the ant simulation
        ant_simulation = AntSimulation(coda_api, doc_id, table_id, config)

        # Create ants
        create_tasks = []
        for i in range(config.num_ants):
            species = random.choice(list(AntSpecies))
            create_tasks.append(ant_simulation.create_ant(f"Ant-{i+1}", species))
        await asyncio.gather(*create_tasks)
        logger.info(f"Created {config.num_ants} ants")

        # Run simulation
        await ant_simulation.simulate()
        logger.info(f"Completed simulation for {config.num_steps} steps")

        return doc_id, table_id

def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Run Active Inference Ants Simulation.")
    parser.add_argument('--api_token', type=str, help='Coda API token', default=os.getenv('CODA_API_TOKEN'))
    parser.add_argument('--num_ants', type=int, help='Number of ants in the simulation', default=10)
    parser.add_argument('--num_steps', type=int, help='Number of simulation steps', default=20)
    return parser.parse_args()

async def main():
    args = parse_arguments()
    if not args.api_token:
        logger.error("API token must be provided via --api_token or CODA_API_TOKEN environment variable.")
        return
    
    config = SimulationConfig(num_ants=args.num_ants, num_steps=args.num_steps)
    doc_id, table_id = await run_simulation(args.api_token, config)

    # Get final state of the simulation
    async with CodaAPI(args.api_token) as coda_api:
        final_state = await coda_api.get_rows(doc_id, table_id)
        logger.info(f"Final state of simulation: {final_state}")

        # Optionally, delete the doc when done
        # deleted_doc = await coda_api.delete_doc(doc_id)
        # logger.info(f"Deleted doc: {deleted_doc['name']} (ID: {deleted_doc['id']})")

if __name__ == "__main__":
    asyncio.run(main())
