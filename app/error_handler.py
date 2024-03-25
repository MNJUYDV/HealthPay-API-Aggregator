from fastapi import HTTPException

def handle_api_errors(responses: list) -> None:
    """
    Function to handle errors from API responses.
    """
    if not responses:
        raise HTTPException(status_code=500, detail="Unable to fetch data from APIs")