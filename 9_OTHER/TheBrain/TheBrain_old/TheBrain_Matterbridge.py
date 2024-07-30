import requests
import json
import sys

class FreeJerryBrain:
    def __init__(self, brain_list_url, matterbridge_config_path, discord_webhook_url):
        self.brain_list_url = brain_list_url
        self.matterbridge_config_path = matterbridge_config_path
        self.discord_webhook_url = discord_webhook_url
        self.brains = []

    def download_brains(self):
        """Download the list of brains from the given URL."""
        print("Downloading brains from URL...")
        response = requests.get(self.brain_list_url)
        if response.status_code == 200:
            self.brains = response.json()
            print(f"Successfully downloaded {len(self.brains)} brains.")
        else:
            raise Exception(f"Failed to download brains: {response.status_code}")

    def format_for_matterbridge(self):
        """Format the brains data for Matterbridge."""
        print("Formatting brains data for Matterbridge...")
        formatted_brains = []
        for brain in self.brains:
            formatted_brain = {
                "name": brain.get("name"),
                "description": brain.get("description"),
                "channels": brain.get("channels", []),
                "webhooks": brain.get("webhooks", [])
            }
            formatted_brains.append(formatted_brain)
        print("Formatting complete.")
        return formatted_brains

    def save_to_matterbridge_config(self, formatted_brains):
        """Save the formatted brains data to the Matterbridge configuration file."""
        print(f"Saving formatted brains data to {self.matterbridge_config_path}...")
        with open(self.matterbridge_config_path, 'w') as config_file:
            json.dump({"brains": formatted_brains}, config_file, indent=4)
        print("Data saved to Matterbridge configuration file.")

    def post_to_discord(self, brain):
        """Post the brain data to Discord."""
        print(f"Posting brain '{brain['name']}' to Discord...")
        payload = {
            "content": f"New brain added: {brain['name']}\nDescription: {brain['description']}"
        }
        response = requests.post(self.discord_webhook_url, json=payload)
        if response.status_code == 204:
            print(f"Successfully posted brain '{brain['name']}' to Discord.")
        else:
            print(f"Failed to post brain '{brain['name']}' to Discord: {response.status_code}")

    def run(self):
        """Run the full process of downloading, formatting, saving, and posting brains data."""
        try:
            self.download_brains()
            formatted_brains = self.format_for_matterbridge()
            self.save_to_matterbridge_config(formatted_brains)
            for brain in formatted_brains:
                self.post_to_discord(brain)
        except Exception as e:
            print(f"An error occurred: {e}", file=sys.stderr)

# Example usage
if __name__ == "__main__":
    brain_list_url = "https://example.com/api/brains"
    matterbridge_config_path = "matterbridge_config.json"
    discord_webhook_url = "https://discord.com/api/webhooks/your_webhook_id/your_webhook_token"
    free_jerry_brain = FreeJerryBrain(brain_list_url, matterbridge_config_path, discord_webhook_url)
    free_jerry_brain.run()
