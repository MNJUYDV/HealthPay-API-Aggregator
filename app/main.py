from fastapi import FastAPI, HTTPException
import sys
import os
sys.path.append(os.path.dirname(__file__))
from utils import coalesce_data
from api_handler import APIHandlerFactory

app = FastAPI()

@app.get("/healthcare/{member_id}")
async def get_healthcare_info(member_id: int) -> dict:
    try:
        responses = APIHandlerFactory.call_apis(member_id)
        healthcare_info = coalesce_data(responses)
        #Can be replaced with loggers
        print("Success Check")
        return healthcare_info
    except HTTPException as e:
        raise e 
    except Exception as e:
        print(f"Exception Check .. Error processing request for member {member_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
