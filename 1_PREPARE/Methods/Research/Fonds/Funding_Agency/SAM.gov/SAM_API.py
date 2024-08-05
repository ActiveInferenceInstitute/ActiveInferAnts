import requests
import json
import os
from typing import Optional, Dict, Any

API_KEY = 'your_api_key_here'
BASE_URL = 'https://api.sam.gov/opportunities/v2/search'
OUTPUT_DIR = 'SAM_export'

def fetch_opportunities(api_key: str, params: Dict[str, Any]) -> Dict[str, Any]:
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def save_opportunities(data: Dict[str, Any], filename: str) -> None:
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def build_params(api_key: str, posted_from: str, posted_to: str, limit: int = 1000, offset: int = 0, **kwargs) -> Dict[str, Any]:
    params = {
        'api_key': api_key,
        'postedFrom': posted_from,
        'postedTo': posted_to,
        'limit': limit,
        'offset': offset
    }
    params.update(kwargs)
    return params

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    posted_from = '01/01/2020'
    posted_to = '12/31/2028'
    offset = 0
    limit = 1000
    total_records = 1  # Initialize to enter the loop
    
    while offset < total_records:
        params = build_params(API_KEY, posted_from, posted_to, limit, offset)
        data = fetch_opportunities(API_KEY, params)
        total_records = data.get('totalRecords', 0)
        filename = f"{OUTPUT_DIR}/sam_opportunities_{offset}.json"
        save_opportunities(data, filename)
        offset += limit

if __name__ == "__main__":
    main()
