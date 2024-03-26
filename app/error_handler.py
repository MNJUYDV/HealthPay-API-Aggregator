from fastapi import HTTPException

def handle_api_errors(responses: list) -> None:
    if not responses:
        raise HTTPException(status_code=500, detail="Unable to fetch data from APIs")
    
    response_structures = [set(response.keys()) for response in responses]
    
    # Check if all response structures are the same
    if len(set(map(tuple, response_structures))) != 1:
        raise HTTPException(status_code=500, detail="Data coherence issue: Inconsistent JSON structures in API responses")

    # Validate data types for 'oop_max', 'remaining_oop_max', and 'copay'
    for response in responses:
        for field in ['oop_max', 'remaining_oop_max', 'copay']:
            if field in response and not isinstance(response[field], int):
                raise HTTPException(status_code=500, detail=f"Data type issue: Incorrect data type in API response")