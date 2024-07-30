import requests
import json
import os
from datetime import datetime
from typing import Dict, List, Any
import hashlib

class TheBrainActivityPubArchiver:
    def __init__(self, api_key: str, base_url: str = "https://api.bra.in/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def get_brains(self) -> List[Dict[str, Any]]:
        response = requests.get(f"{self.base_url}/brains", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_thoughts(self, brain_id: str) -> List[Dict[str, Any]]:
        response = requests.get(f"{self.base_url}/thoughts/{brain_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_links(self, brain_id: str) -> List[Dict[str, Any]]:
        response = requests.get(f"{self.base_url}/links/{brain_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def to_activity_pub_format(self, brain: Dict[str, Any], thoughts: List[Dict[str, Any]], links: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {
            "@context": "https://www.w3.org/ns/activitystreams",
            "type": "Collection",
            "id": f"urn:brain:{brain['id']}",
            "name": brain['name'],
            "totalItems": len(thoughts),
            "items": [
                {
                    "type": "Note",
                    "id": f"urn:thought:{thought['id']}",
                    "content": thought['name'],
                    "published": thought['creationDateTime'],
                    "updated": thought['modificationDateTime'],
                    "tag": [link for link in links if link['thoughtIdA'] == thought['id'] or link['thoughtIdB'] == thought['id']]
                } for thought in thoughts
            ]
        }

    def archive_brain(self, brain_id: str, output_dir: str):
        brain = next(brain for brain in self.get_brains() if brain['id'] == brain_id)
        thoughts = self.get_thoughts(brain_id)
        links = self.get_links(brain_id)

        activity_pub_data = self.to_activity_pub_format(brain, thoughts, links)

        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"{brain['name']}_{datetime.now().isoformat()}.json")

        with open(output_file, 'w') as f:
            json.dump(activity_pub_data, f, indent=2)

        return output_file

    def verify_integrity(self, brain_id: str, archive_file: str) -> bool:
        with open(archive_file, 'r') as f:
            archived_data = json.load(f)

        current_brain = next(brain for brain in self.get_brains() if brain['id'] == brain_id)
        current_thoughts = self.get_thoughts(brain_id)
        current_links = self.get_links(brain_id)

        current_data = self.to_activity_pub_format(current_brain, current_thoughts, current_links)

        return self.hash_dict(archived_data) == self.hash_dict(current_data)

    @staticmethod
    def hash_dict(d: Dict[str, Any]) -> str:
        return hashlib.sha256(json.dumps(d, sort_keys=True).encode()).hexdigest()

def archive_and_verify_brain(api_key: str, brain_id: str, output_dir: str):
    archiver = TheBrainActivityPubArchiver(api_key)
    
    print(f"Archiving brain {brain_id}...")
    archive_file = archiver.archive_brain(brain_id, output_dir)
    print(f"Brain archived to {archive_file}")

    print("Verifying integrity...")
    if archiver.verify_integrity(brain_id, archive_file):
        print("Integrity check passed. Archive is consistent with the current state of the brain.")
    else:
        print("Integrity check failed. Archive may be outdated or corrupted.")

if __name__ == "__main__":
    api_key = "your_api_key_here"
    brain_id = "your_brain_id_here"
    output_dir = "brain_archives"

    archive_and_verify_brain(api_key, brain_id, output_dir)
