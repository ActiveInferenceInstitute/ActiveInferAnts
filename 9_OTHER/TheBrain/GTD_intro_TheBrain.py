import requests
import os
import json

# Set the API key
os.environ["API_KEY"] = ""

class TheBrainAPI:
    BASE_URL = "https://api.bra.in/"

    def __init__(self, api_key, brain_id):
        self.api_key = api_key
        self.brain_id = brain_id
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.data_folder = "Data"
        os.makedirs(self.data_folder, exist_ok=True)

    def get_brain_details(self):
        return self._make_request("GET", f"brains/{self.brain_id}", "brain_details.json")

    def get_thought_details(self, thought_id):
        return self._make_request("GET", f"thoughts/{self.brain_id}/{thought_id}", f"thought_details_{thought_id}.json")

    def get_thought_links(self, thought_id):
        return self._make_request("GET", f"thoughts/{self.brain_id}/{thought_id}/links", f"thought_links_{thought_id}.json")

    def _make_request(self, method, endpoint, filename, params=None, json=None):
        url = f"{self.BASE_URL}{endpoint}"
        print(f"{method} request to {url}")
        response = requests.request(method, url, headers=self.headers, params=params, json=json)
        return self._handle_response(response, filename)

    def _handle_response(self, response, filename):
        if response.status_code == 200:
            data = response.json()
            self.save_data(filename, data)
            return data
        else:
            raise Exception(f"Failed to fetch data: {response.status_code} {response.text}")

    def save_data(self, filename, data):
        filepath = os.path.join(self.data_folder, filename)
        print(f"Saving data to {filepath}")
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)

    def walk_and_download_thoughts(self):
        brain_details = self.get_brain_details()
        print("Brain Details:", brain_details)

        thought_ids = self._extract_thought_ids(brain_details)
        for thought_id in thought_ids:
            thought_details = self.get_thought_details(thought_id)
            print(f"Thought Details for {thought_id}:", thought_details)

            thought_links = self.get_thought_links(thought_id)
            print(f"Thought Links for {thought_id}:", thought_links)

    def _extract_thought_ids(self, brain_details):
        thought_ids = []
        if "thoughts" in brain_details:
            for thought in brain_details["thoughts"]:
                thought_ids.append(thought["id"])
        return thought_ids

    def download_all_nodes_and_links(self):
        brain_details = self.get_brain_details()
        print("Brain Details:", brain_details)

        home_thought_id = brain_details.get("homeThoughtId")
        if not home_thought_id:
            raise Exception("Home thought ID not found in brain details")

        all_thoughts = []
        all_links = []
        visited_thoughts = set()

        def download_thoughts_and_links(thought_id):
            if thought_id in visited_thoughts:
                return
            visited_thoughts.add(thought_id)

            thought_details = self.get_thought_details(thought_id)
            all_thoughts.append(thought_details)
            print(f"Thought Details for {thought_id}:", thought_details)

            thought_links = self.get_thought_links(thought_id)
            all_links.extend(thought_links)
            print(f"Thought Links for {thought_id}:", thought_links)

            for link in thought_links:
                linked_thought_id = link.get("id")
                if linked_thought_id:
                    download_thoughts_and_links(linked_thought_id)

        download_thoughts_and_links(home_thought_id)

        self.save_data("all_thoughts.json", all_thoughts)
        self.save_data("all_links.json", all_links)

# Example usage
if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    brain_id = "ebebdd7c-d69f-462d-845b-60a88a472240"

    brain_api = TheBrainAPI(api_key, brain_id)
    
    try:
        brain_api.download_all_nodes_and_links()
    except Exception as e:
        print(f"An error occurred: {str(e)}")