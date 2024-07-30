import requests
import json
from typing import Dict, List, Optional

class TheBrainGTD:
    def __init__(self, api_key: str, base_url: str = "https://api.thebrain.com/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def create_thought(self, name: str, type_id: str, parent_id: Optional[str] = None) -> Dict:
        data = {
            "name": name,
            "typeId": type_id,
            "parentId": parent_id
        }
        return self._make_request("POST", "thoughts", data)

    def update_thought(self, thought_id: str, name: Optional[str] = None, type_id: Optional[str] = None) -> Dict:
        data = {}
        if name:
            data["name"] = name
        if type_id:
            data["typeId"] = type_id
        return self._make_request("PATCH", f"thoughts/{thought_id}", data)

    def delete_thought(self, thought_id: str) -> Dict:
        return self._make_request("DELETE", f"thoughts/{thought_id}")

    def get_thought(self, thought_id: str) -> Dict:
        return self._make_request("GET", f"thoughts/{thought_id}")

    def search_thoughts(self, query: str) -> List[Dict]:
        return self._make_request("GET", f"thoughts/search?q={query}")

    def create_link(self, thought_id: str, target_id: str, relationship: str) -> Dict:
        data = {
            "thoughtId": thought_id,
            "targetId": target_id,
            "relationship": relationship
        }
        return self._make_request("POST", "links", data)

    def delete_link(self, link_id: str) -> Dict:
        return self._make_request("DELETE", f"links/{link_id}")

class GTDManager:
    def __init__(self, brain: TheBrainGTD):
        self.brain = brain
        self.gtd_types = {
            "inbox": "GTD_Inbox",
            "next_action": "GTD_NextAction",
            "project": "GTD_Project",
            "waiting_for": "GTD_WaitingFor",
            "someday_maybe": "GTD_SomedayMaybe",
            "reference": "GTD_Reference"
        }

    def add_to_inbox(self, item: str) -> Dict:
        return self.brain.create_thought(item, self.gtd_types["inbox"])

    def create_next_action(self, action: str, project_id: Optional[str] = None) -> Dict:
        thought = self.brain.create_thought(action, self.gtd_types["next_action"])
        if project_id:
            self.brain.create_link(thought["id"], project_id, "belongs_to")
        return thought

    def create_project(self, project: str) -> Dict:
        return self.brain.create_thought(project, self.gtd_types["project"])

    def add_waiting_for(self, item: str, project_id: Optional[str] = None) -> Dict:
        thought = self.brain.create_thought(item, self.gtd_types["waiting_for"])
        if project_id:
            self.brain.create_link(thought["id"], project_id, "belongs_to")
        return thought

    def add_someday_maybe(self, item: str) -> Dict:
        return self.brain.create_thought(item, self.gtd_types["someday_maybe"])

    def add_reference(self, item: str) -> Dict:
        return self.brain.create_thought(item, self.gtd_types["reference"])

    def complete_action(self, action_id: str) -> None:
        self.brain.delete_thought(action_id)

    def move_to_next_actions(self, thought_id: str) -> Dict:
        return self.brain.update_thought(thought_id, type_id=self.gtd_types["next_action"])

    def get_all_next_actions(self) -> List[Dict]:
        return self.brain.search_thoughts(f"typeId:{self.gtd_types['next_action']}")

    def get_all_projects(self) -> List[Dict]:
        return self.brain.search_thoughts(f"typeId:{self.gtd_types['project']}")

    def get_project_next_actions(self, project_id: str) -> List[Dict]:
        project = self.brain.get_thought(project_id)
        return [child for child in project.get("children", []) if child["typeId"] == self.gtd_types["next_action"]]

# Usage example:
if __name__ == "__main__":
    api_key = "your_api_key_here"
    brain = TheBrainGTD(api_key)
    gtd = GTDManager(brain)

    # Add items to inbox
    inbox_item = gtd.add_to_inbox("Buy groceries")
    print(f"Added to inbox: {inbox_item['name']}")

    # Create a project
    project = gtd.create_project("Home renovation")
    print(f"Created project: {project['name']}")

    # Create next actions
    action1 = gtd.create_next_action("Call contractor", project["id"])
    action2 = gtd.create_next_action("Research paint colors", project["id"])
    print(f"Created next actions: {action1['name']}, {action2['name']}")

    # Add waiting for item
    waiting = gtd.add_waiting_for("Contractor estimate", project["id"])
    print(f"Added waiting for: {waiting['name']}")

    # Add someday/maybe item
    someday = gtd.add_someday_maybe("Learn to play guitar")
    print(f"Added someday/maybe: {someday['name']}")

    # Add reference item
    reference = gtd.add_reference("Home renovation inspiration photos")
    print(f"Added reference: {reference['name']}")

    # Get all next actions
    next_actions = gtd.get_all_next_actions()
    print("All next actions:", [action["name"] for action in next_actions])

    # Get all projects
    projects = gtd.get_all_projects()
    print("All projects:", [proj["name"] for proj in projects])

    # Get next actions for a specific project
    project_actions = gtd.get_project_next_actions(project["id"])
    print(f"Next actions for {project['name']}:", [action["name"] for action in project_actions])

    # Complete an action
    gtd.complete_action(action1["id"])
    print(f"Completed action: {action1['name']}")

    # Move inbox item to next actions
    moved_action = gtd.move_to_next_actions(inbox_item["id"])
    print(f"Moved to next actions: {moved_action['name']}")
