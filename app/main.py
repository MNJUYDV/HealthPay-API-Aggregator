from fastapi import FastAPI, HTTPException
from .api_handler import APIHandlerFactory
from .error_handler import handle_api_errors
from typing import List, Optional
from statistics import mode

app = FastAPI()

from statistics import mode

def coalesce_data(responses: List[Optional[dict]]) -> dict:
    if not responses:
        return {}

    oop_max_values = [response.get("oop_max") for response in responses if "oop_max" in response]
    remaining_oop_max_values = [response.get("remaining_oop_max") for response in responses if "remaining_oop_max" in response]
    copay_values = [response.get("copay") for response in responses if "copay" in response]

    # Calculate the mode of oop_max, remaining_oop_max, and copay values
    oop_max = mode(oop_max_values) if oop_max_values else None
    remaining_oop_max = mode(remaining_oop_max_values) if remaining_oop_max_values else None
    copay = mode(copay_values) if copay_values else None

    coalesced_data = {
        "oop_max": oop_max,
        "remaining_oop_max": remaining_oop_max,
        "copay": copay
    }
    return coalesced_data

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
