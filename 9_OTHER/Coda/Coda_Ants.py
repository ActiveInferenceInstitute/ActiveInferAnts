import requests
import random
import time
from typing import List, Dict, Optional, Tuple
import numpy as np
from scipy.stats import entropy
import logging
from dataclasses import dataclass
from enum import Enum, auto

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CodaAPI:
    def __init__(self, api_token: str):
        self.base_url = "https://coda.io/apis/v1"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }

    def _make_request(self, method: str, endpoint: str, payload: Optional[Dict] = None, params: Optional[Dict] = None) -> Dict:
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, json=payload, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise

    def create_doc(self, title: str, source_doc: Optional[str] = None, timezone: Optional[str] = None) -> Dict:
        payload = {"title": title, "sourceDoc": source_doc, "timezone": timezone}
        return self._make_request("POST", "docs", payload=payload)

    def list_docs(self, is_owner: Optional[bool] = None, query: Optional[str] = None) -> Dict:
        params = {"isOwner": is_owner, "query": query}
        return self._make_request("GET", "docs", params=params)

    def get_doc(self, doc_id: str) -> Dict:
        return self._make_request("GET", f"docs/{doc_id}")

    def delete_doc(self, doc_id: str) -> Dict:
        return self._make_request("DELETE", f"docs/{doc_id}")

    def create_table(self, doc_id: str, table_name: str, columns: List[Dict]) -> Dict:
        payload = {"name": table_name, "columns": columns}
        return self._make_request("POST", f"docs/{doc_id}/tables", payload=payload)

    def add_row(self, doc_id: str, table_id: str, row_data: Dict) -> Dict:
        payload = {"rows": [row_data]}
        return self._make_request("POST", f"docs/{doc_id}/tables/{table_id}/rows", payload=payload)

    def get_rows(self, doc_id: str, table_id: str, query: Optional[str] = None) -> Dict:
        params = {"query": query}
        return self._make_request("GET", f"docs/{doc_id}/tables/{table_id}/rows", params=params)

    def update_row(self, doc_id: str, table_id: str, row_id: str, row_data: Dict) -> Dict:
        payload = {"row": row_data}
        return self._make_request("PUT", f"docs/{doc_id}/tables/{table_id}/rows/{row_id}", payload=payload)

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

class ActiveInferenceAnt:
    def __init__(self, name: str, species: AntSpecies, position: np.ndarray):
        self.name = name
        self.species = species
        self.position = position
        self.attributes = self._initialize_attributes()
        self.A_matrix = np.random.rand(3, 3)  # Sensory mapping
        self.B_matrix = np.random.rand(3, 3, 3)  # Transition probabilities
        self.C_matrix = np.random.rand(3)  # Preferred outcomes
        self.D_matrix = np.random.rand(3)  # Initial beliefs

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
            speed=attributes.speed + random.uniform(-0.1, 0.1),
            strength=attributes.strength + random.uniform(-0.1, 0.1),
            perception=attributes.perception + random.uniform(-0.1, 0.1)
        )

    def perceive(self, observation: np.ndarray):
        prediction_error = observation - np.dot(self.A_matrix, self.position)
        self.position -= self.attributes.perception * 0.1 * prediction_error

    def act(self) -> np.ndarray:
        possible_actions = np.eye(3)
        efe_scores = [self.calculate_efe(action) for action in possible_actions]
        return possible_actions[np.argmin(efe_scores)]

    def calculate_efe(self, action: np.ndarray) -> float:
        future_state = np.dot(self.B_matrix, action)
        expected_observation = np.dot(self.A_matrix, future_state)
        pragmatic_value = np.dot(self.C_matrix, expected_observation)
        epistemic_value = entropy(future_state)
        return -(self.attributes.strength * pragmatic_value + self.attributes.speed * epistemic_value)

class AntSimulation:
    def __init__(self, coda_api: CodaAPI, doc_id: str, table_id: str):
        self.coda_api = coda_api
        self.doc_id = doc_id
        self.table_id = table_id
        self.ants: List[ActiveInferenceAnt] = []

    def create_ant(self, name: str, species: AntSpecies):
        position = np.random.rand(3)
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
        self.coda_api.add_row(self.doc_id, self.table_id, row_data)

    def simulate(self, num_steps: int):
        for step in range(num_steps):
            logger.info(f"Simulation step: {step + 1}/{num_steps}")
            for ant in self.ants:
                action = ant.act()
                observation = self._generate_observation(ant)
                ant.perceive(observation)
                
                self._update_coda_table(ant, action, observation)
            
            time.sleep(1)  # Simulate time delay between steps

    def _generate_observation(self, ant: ActiveInferenceAnt) -> np.ndarray:
        base_observation = np.random.rand(3)
        return base_observation * ant.attributes.perception

    def _update_coda_table(self, ant: ActiveInferenceAnt, action: np.ndarray, observation: np.ndarray):
        rows = self.coda_api.get_rows(self.doc_id, self.table_id, query=f'Name:"{ant.name}"')
        row_id = rows['items'][0]['id']
        row_data = {
            "cells": [
                {"column": "Position", "value": ant.position.tolist()},
                {"column": "Action", "value": action.tolist()},
                {"column": "Observation", "value": observation.tolist()}
            ]
        }
        self.coda_api.update_row(self.doc_id, self.table_id, row_id, row_data)

def run_simulation(api_token: str, num_ants: int = 5, num_steps: int = 10) -> Tuple[str, str]:
    coda_api = CodaAPI(api_token)

    # Create a new doc
    new_doc = coda_api.create_doc(title="Advanced Active Inference Ants Simulation")
    doc_id = new_doc['id']
    logger.info(f"Created doc: {new_doc['name']} (ID: {doc_id})")

    # Create a table for the simulation
    table = coda_api.create_table(doc_id, "Ant Simulation", [
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
    ant_simulation = AntSimulation(coda_api, doc_id, table_id)

    # Create ants
    for i in range(num_ants):
        species = random.choice(list(AntSpecies))
        ant_simulation.create_ant(f"Ant-{i+1}", species)
    logger.info(f"Created {num_ants} ants")

    # Run simulation
    ant_simulation.simulate(num_steps)
    logger.info(f"Completed simulation for {num_steps} steps")

    return doc_id, table_id

if __name__ == "__main__":
    api_token = "your_api_token_here"
    doc_id, table_id = run_simulation(api_token)

    # Get final state of the simulation
    coda_api = CodaAPI(api_token)
    final_state = coda_api.get_rows(doc_id, table_id)
    logger.info(f"Final state of simulation: {final_state}")

    # Optionally, delete the doc when done
    # deleted_doc = coda_api.delete_doc(doc_id)
    # logger.info(f"Deleted doc: {deleted_doc['name']} (ID: {deleted_doc['id']})")
