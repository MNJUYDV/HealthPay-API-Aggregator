from typing import List, Optional
import requests
from app.config import API_URLS, MAX_RETRIES, DELAY_BETWEEN_RETRIES
from app.error_handler import handle_api_errors
from fastapi import HTTPException
import time

def call_api(member_id: int) -> List[Optional[dict]]:
    responses = []

    for url in API_URLS:
        retries = 0
        while retries < MAX_RETRIES:
            try:
                response = requests.get(f"{url}?member_id={member_id}")
                if response.status_code == 200:
                    responses.append(response.json())
                    break  # Exit the retry loop if request is successful
            except Exception as e:
                print(f"Error accessing {url}: {e}")
            retries += 1
            time.sleep(DELAY_BETWEEN_RETRIES)  # Wait for specified delay before retrying

    if responses:
        handle_api_errors(responses)

    return responses
