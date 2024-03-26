from typing import List, Optional
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
