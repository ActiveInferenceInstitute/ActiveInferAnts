import requests
from typing import Dict, Any, List

class TheBrainAPI:
    """
    A class to interact with TheBrain API and perform various operations.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.thebrain.com"):
        """
        Initializes the TheBrainAPI instance.

        Parameters:
        - api_key (str): The API key for authenticating with TheBrain API.
        - base_url (str): The base URL for TheBrain API. Default is "https://api.thebrain.com".
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        print(f"Initialized TheBrainAPI with base URL: {self.base_url}")

    def _make_request(self, method: str, endpoint: str, **kwargs) -> Any:
        """
        Makes an HTTP request to the specified endpoint.

        Parameters:
        - method (str): The HTTP method (GET, POST, PUT, DELETE).
        - endpoint (str): The API endpoint to call.
        - kwargs: Additional arguments to pass to the requests method.

        Returns:
        - Any: The response from the API.
        """
        url = f"{self.base_url}{endpoint}"
        print(f"Making {method} request to {url} with params: {kwargs.get('params', {})}")
        response = requests.request(method, url, headers=self.headers, **kwargs)
        response.raise_for_status()
        print(f"Received response with status code: {response.status_code}")
        return response.json() if response.content else None

    def get_brain_info(self, brain_id: str) -> Dict[str, Any]:
        """
        Retrieves information about a specific brain.

        Parameters:
        - brain_id (str): The ID of the brain to retrieve information for.

        Returns:
        - Dict[str, Any]: A dictionary containing brain information.
        """
        print(f"Retrieving information for brain ID: {brain_id}")
        return self._make_request("GET", f"/brains/{brain_id}")

    def list_thoughts(self, brain_id: str) -> List[Dict[str, Any]]:
        """
        Lists all thoughts in a specific brain.

        Parameters:
        - brain_id (str): The ID of the brain to list thoughts for.

        Returns:
        - List[Dict[str, Any]]: A list of dictionaries, each containing thought information.
        """
        print(f"Listing thoughts for brain ID: {brain_id}")
        return self._make_request("GET", f"/brains/{brain_id}/thoughts")

    def get_thought(self, brain_id: str, thought_id: str) -> Dict[str, Any]:
        """
        Retrieves information about a specific thought.

        Parameters:
        - brain_id (str): The ID of the brain containing the thought.
        - thought_id (str): The ID of the thought to retrieve information for.

        Returns:
        - Dict[str, Any]: A dictionary containing thought information.
        """
        print(f"Retrieving information for thought ID: {thought_id} in brain ID: {brain_id}")
        return self._make_request("GET", f"/brains/{brain_id}/thoughts/{thought_id}")

    def create_thought(self, brain_id: str, thought_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new thought in a specific brain.

        Parameters:
        - brain_id (str): The ID of the brain to create the thought in.
        - thought_data (Dict[str, Any]): A dictionary containing the thought data.

        Returns:
        - Dict[str, Any]: A dictionary containing the created thought information.
        """
        print(f"Creating thought in brain ID: {brain_id}")
        return self._make_request("POST", f"/brains/{brain_id}/thoughts", json=thought_data)

    def update_thought(self, brain_id: str, thought_id: str, thought_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates an existing thought in a specific brain.

        Parameters:
        - brain_id (str): The ID of the brain containing the thought.
        - thought_id (str): The ID of the thought to update.
        - thought_data (Dict[str, Any]): A dictionary containing the updated thought data.

        Returns:
        - Dict[str, Any]: A dictionary containing the updated thought information.
        """
        print(f"Updating thought ID: {thought_id} in brain ID: {brain_id}")
        return self._make_request("PUT", f"/brains/{brain_id}/thoughts/{thought_id}", json=thought_data)

    def delete_thought(self, brain_id: str, thought_id: str) -> None:
        """
        Deletes a thought from a specific brain.

        Parameters:
        - brain_id (str): The ID of the brain containing the thought.
        - thought_id (str): The ID of the thought to delete.

        Returns:
        - None
        """
        print(f"Deleting thought ID: {thought_id} from brain ID: {brain_id}")
        self._make_request("DELETE", f"/brains/{brain_id}/thoughts/{thought_id}")

    def list_links(self, brain_id: str) -> List[Dict[str, Any]]:
        """
        Lists all links in a specific brain.

        Parameters:
        - brain_id (str): The ID of the brain to list links for.

        Returns:
        - List[Dict[str, Any]]: A list of dictionaries, each containing link information.
        """
        print(f"Listing links for brain ID: {brain_id}")
        return self._make_request("GET", f"/brains/{brain_id}/links")

    def get_link(self, brain_id: str, link_id: str) -> Dict[str, Any]:
        """
        Retrieves information about a specific link.

        Parameters:
        - brain_id (str): The ID of the brain containing the link.
        - link_id (str): The ID of the link to retrieve information for.

        Returns:
        - Dict[str, Any]: A dictionary containing link information.
        """
        print(f"Retrieving information for link ID: {link_id} in brain ID: {brain_id}")
        return self._make_request("GET", f"/brains/{brain_id}/links/{link_id}")

    def create_link(self, brain_id: str, link_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new link in a specific brain.

        Parameters:
        - brain_id (str): The ID of the brain to create the link in.
        - link_data (Dict[str, Any]): A dictionary containing the link data.

        Returns:
        - Dict[str, Any]: A dictionary containing the created link information.
        """
        print(f"Creating link in brain ID: {brain_id}")
        return self._make_request("POST", f"/brains/{brain_id}/links", json=link_data)

    def update_link(self, brain_id: str, link_id: str, link_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates an existing link in a specific brain.

        Parameters:
        - brain_id (str): The ID of the brain containing the link.
        - link_id (str): The ID of the link to update.
        - link_data (Dict[str, Any]): A dictionary containing the updated link data.

        Returns:
        - Dict[str, Any]: A dictionary containing the updated link information.
        """
        print(f"Updating link ID: {link_id} in brain ID: {brain_id}")
        return self._make_request("PUT", f"/brains/{brain_id}/links/{link_id}", json=link_data)

    def delete_link(self, brain_id: str, link_id: str) -> None:
        """
        Deletes a link from a specific brain.

        Parameters:
        - brain_id (str): The ID of the brain containing the link.
        - link_id (str): The ID of the link to delete.

        Returns:
        - None
        """
        print(f"Deleting link ID: {link_id} from brain ID: {brain_id}")
        self._make_request("DELETE", f"/brains/{brain_id}/links/{link_id}")

    def get_attachment_metadata(self, brain_id: str, attachment_id: str) -> Dict[str, Any]:
        """
        Retrieves metadata for a specific attachment.

        Parameters:
        - brain_id (str): The ID of the brain containing the attachment.
        - attachment_id (str): The ID of the attachment to retrieve metadata for.

        Returns:
        - Dict[str, Any]: A dictionary containing attachment metadata.
        """
        print(f"Retrieving metadata for attachment ID: {attachment_id} in brain ID: {brain_id}")
        return self._make_request("GET", f"/attachments/{brain_id}/{attachment_id}/metadata")

    def get_attachment_file_content(self, brain_id: str, attachment_id: str) -> bytes:
        """
        Retrieves the binary data for a specific attachment.

        Parameters:
        - brain_id (str): The ID of the brain containing the attachment.
        - attachment_id (str): The ID of the attachment to retrieve file content for.

        Returns:
        - bytes: The binary data of the attachment.
        """
        print(f"Retrieving file content for attachment ID: {attachment_id} in brain ID: {brain_id}")
        return self._make_request("GET", f"/attachments/{brain_id}/{attachment_id}/file-content", stream=True).content

    def search_accessible(self, query_text: str, max_results: int = 30, only_search_thought_names: bool = False) -> List[Dict[str, Any]]:
        """
        Searches across all accessible brains for the given query text.

        Parameters:
        - query_text (str): The string to search for.
        - max_results (int): The maximum number of search results to return. Default is 30.
        - only_search_thought_names (bool): Whether to only search in thought names. Default is False.

        Returns:
        - List[Dict[str, Any]]: A list of dictionaries containing search results.
        """
        print(f"Searching for '{query_text}' with max results {max_results} and only_search_thought_names={only_search_thought_names}")
        params = {
            "queryText": query_text,
            "maxResults": max_results,
            "onlySearchThoughtNames": only_search_thought_names
        }
        return self._make_request("GET", "/search/accessible", params=params)