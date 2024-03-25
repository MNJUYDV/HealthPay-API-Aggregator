# main.py

from fastapi import FastAPI, HTTPException
from app.api_handler import call_api
from app.error_handler import handle_api_errors
from typing import List, Optional
from statistics import mode

app = FastAPI()

def coalesce_data(responses: List[Optional[dict]]) -> dict:
    """
    Coalesce the data from multiple API responses.
    """
    if not responses:
        return {}  # Return empty dictionary if no responses

    # Aggregate oop_max, remaining_oop_max, copay using mode
    oop_max_values = [response.get("oop_max") for response in responses if "oop_max" in response]
    remaining_oop_max_values = [response.get("remaining_oop_max") for response in responses if "remaining_oop_max" in response]
    copay_values = [response.get("copay") for response in responses if "copay" in response]

    coalesced_data = {
        "oop_max": mode(oop_max_values) if oop_max_values else None,
        "remaining_oop_max": mode(remaining_oop_max_values) if remaining_oop_max_values else None,
        "copay": mode(copay_values) if copay_values else None
    }

    return coalesced_data

@app.get("/healthcare/{member_id}")
async def get_healthcare_info(member_id: int) -> dict:
    """
    Endpoint to fetch healthcare information for a member.
    """
    try:
        responses = call_api(member_id)
        healthcare_info = coalesce_data(responses)
        return healthcare_info
    except Exception as e:
        # Log the error or handle it as needed
        print(f"Error processing request for member {member_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
