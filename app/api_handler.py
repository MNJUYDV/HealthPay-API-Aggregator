from abc import ABC, abstractmethod
from typing import List, Optional
import requests
from .config import API_URLS

class APIHandler(ABC):
    @abstractmethod
    def call_api(self, member_id: int) -> List[Optional[dict]]:
        pass

class APIHandlerFactory:
    @staticmethod
    def create_api_handler(url: str) -> 'APIHandler':
        if url == API_URLS[0]:
            return API1Handler()
        elif url == API_URLS[1]:
            return API2Handler()
        elif url == API_URLS[2]:
            return API3Handler()
        else:
            raise ValueError("Unsupported API URL")

    @staticmethod
    def call_apis(member_id: int, max_retries: int = 3) -> List[Optional[dict]]:
        responses = []
        for url in API_URLS:
            retries = 0
            while retries < max_retries:
                api_handler = APIHandlerFactory.create_api_handler(url)
                try:
                    api_response = api_handler.call_api(member_id)
                    if api_response:
                        responses.extend(api_response)
                        break  # Break out of retry loop if successful response received
                except Exception as e:
                    print(f"Error calling API {url}: {e}")
                retries += 1
        return responses

class API1Handler(APIHandler):
    def call_api(self, member_id: int) -> List[Optional[dict]]:
        response = requests.get(f"{API_URLS[0]}?member_id={member_id}")
        if response.status_code == 200:
            return [response.json()]
        else:
            return []

class API2Handler(APIHandler):
    def call_api(self, member_id: int) -> List[Optional[dict]]:
        response = requests.get(f"{API_URLS[1]}?member_id={member_id}")
        if response.status_code == 200:
            return [response.json()]
        else:
            return []

class API3Handler(APIHandler):
    def call_api(self, member_id: int) -> List[Optional[dict]]:
        response = requests.get(f"{API_URLS[2]}?member_id={member_id}")
        if response.status_code == 200:
            return [response.json()]
        else:
            return []
