# api_handler.py
from typing import List, Optional
import requests
from app.config import API_URLS
from app.error_handler import handle_api_errors
from fastapi import HTTPException

def call_api(member_id: int) -> List[Optional[dict]]:
    """
    Function to call the APIs and fetch data.
    """
    responses = []
    for url in API_URLS:
        try:
            response = requests.get(f"{url}?member_id={member_id}")
            if response.status_code == 200:
                responses.append(response.json())
        except Exception as e:
            print(f"Error accessing {url}: {e}")
    if responses:  # Only call handle_api_errors if there are valid responses
        handle_api_errors(responses)
    return responses
