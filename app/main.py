from fastapi import FastAPI, HTTPException

from app.utils import coalesce_data
from .api_handler import APIHandlerFactory
from .error_handler import handle_api_errors
from typing import List, Optional
from statistics import mode

app = FastAPI()

from statistics import mode

@app.get("/healthcare/{member_id}")
async def get_healthcare_info(member_id: int) -> dict:
    try:
        responses = APIHandlerFactory.call_apis(member_id)
        healthcare_info = coalesce_data(responses)
        return healthcare_info
    except HTTPException as e:
        raise e 
    except Exception as e:
        print(f"Error processing request for member {member_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
