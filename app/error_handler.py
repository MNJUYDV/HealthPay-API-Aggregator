from fastapi import HTTPException

def validate_response_data(responses: list) -> None:
    for response in responses:
        for field in ['oop_max', 'remaining_oop_max', 'copay']:
            if field in response and not isinstance(response[field], int):
                raise HTTPException(status_code=500, detail=f"Data type issue: Incorrect data type in API response")

def ensure_coherent_response_structures(responses: list) -> None:
    response_structures = [set(response.keys()) for response in responses]
    
    if len(set(map(tuple, response_structures))) != 1:
        raise HTTPException(status_code=500, detail="Data coherence issue: Inconsistent JSON structures in API responses")

def handle_api_errors(responses: list) -> None:
    if not responses:
        raise HTTPException(status_code=500, detail="Unable to fetch data from APIs")

    validate_response_data(responses)
    ensure_coherent_response_structures(responses)
