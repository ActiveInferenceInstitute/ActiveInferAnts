import requests
import json
import random
import time

# TheBrain API configuration
API_KEY = "your_api_key_here"
BRAIN_ID = "your_brain_id_here"
BASE_URL = "https://api.thebrain.com/v1"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def create_thought(name, kind=1, label=None, source_thought_id=None, relation=None):
    url = f"{BASE_URL}/thoughts/{BRAIN_ID}"
    data = {
        "name": name,
        "kind": kind,
        "label": label,
        "sourceThoughtId": source_thought_id,
        "relation": relation,
        "acType": 0
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["id"]
    else:
        print(f"Error creating thought: {response.text}")
        return None

def create_link(thought_id_a, thought_id_b, relation=1):
    url = f"{BASE_URL}/links/{BRAIN_ID}"
    data = {
        "thoughtIdA": thought_id_a,
        "thoughtIdB": thought_id_b,
        "relation": relation,
        "meaning": 1,
        "direction": 1
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print(f"Error creating link: {response.text}")

class Ant:
    def __init__(self, name, colony_id):
        self.name = name
        self.thought_id = create_thought(name, label="Ant")
        create_link(colony_id, self.thought_id, relation=1)  # Child relation

    def move(self, location_id):
        create_link(self.thought_id, location_id, relation=3)  # Jump relation

class AntColony:
    def __init__(self, name, location_id):
        self.name = name
        self.thought_id = create_thought(name, label="Ant Colony")
        self.ants = []
        create_link(self.thought_id, location_id, relation=3)  # Jump relation

    def spawn_ant(self, ant_name):
        ant = Ant(ant_name, self.thought_id)
        self.ants.append(ant)
        return ant

class Location:
    def __init__(self, name):
        self.name = name
        self.thought_id = create_thought(name, label="Location")

def simulate_ant_colony(colony_name, num_ants, num_locations, num_steps):
    # Create locations
    locations = [Location(f"Location_{i}") for i in range(num_locations)]

    # Create ant colony
    colony = AntColony(colony_name, locations[0].thought_id)

    # Spawn ants
    for i in range(num_ants):
        colony.spawn_ant(f"Ant_{i}")

    # Simulation steps
    for step in range(num_steps):
        print(f"Step {step + 1}")
        for ant in colony.ants:
            new_location = random.choice(locations)
            ant.move(new_location.thought_id)
            print(f"{ant.name} moved to {new_location.name}")
        time.sleep(1)  # Pause for 1 second between steps

# Run the simulation
simulate_ant_colony("MyAntColony", num_ants=5, num_locations=3, num_steps=10)
