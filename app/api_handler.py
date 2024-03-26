from abc import ABC, abstractmethod
from typing import List, Optional
import requests
from .config import API_URLS
from .error_handler import handle_api_errors

class APIHandler(ABC):
    @abstractmethod
    def call_api(self, member_id: int) -> List[Optional[dict]]:
        pass

class API1Handler(APIHandler):
    def call_api(self, member_id: int) -> List[Optional[dict]]:
        # Implement API 1 logic here
        response = requests.get(f"https://api1.com?member_id={member_id}")
        if response.status_code == 200:
            return [response.json()]
        else:
            return []

class API2Handler(APIHandler):
    def call_api(self, member_id: int) -> List[Optional[dict]]:
        # Implement API 2 logic here
        response = requests.get(f"https://api2.com?member_id={member_id}")
        if response.status_code == 200:
            return [response.json()]
        else:
            return []

class API3Handler(APIHandler):
    def call_api(self, member_id: int) -> List[Optional[dict]]:
        # Implement API 3 logic here
        response = requests.get(f"https://api3.com?member_id={member_id}")
        print("here response 3", response)
        if response.status_code == 200:
            return [response.json()]
        else:
            return []

class APIHandlerFactory:
    @staticmethod
    def create_api_handler(url: str) -> APIHandler:
        if url == "https://api1.com":
            return API1Handler()
        elif url == "https://api2.com":
            return API2Handler()
        elif url == "https://api3.com":
            return API3Handler()
        else:
            raise ValueError("Unsupported API URL")

    @staticmethod
    def call_apis(member_id: int) -> List[Optional[dict]]:
        responses = []
        for url in API_URLS:
            api_handler = APIHandlerFactory.create_api_handler(url)
            responses.extend(api_handler.call_api(member_id))
        print(responses)
        return responses