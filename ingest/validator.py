VALID_EVENT_TYPES = {
    "call_received",
    "unit_dispatched",
    "unit_arrived",
    "incident_closed",
}

VALID_STATUSES = {"open", "in_progress", "closed"}

def validate_event(event: dict) -> bool:
    if event["severity"] not in range(1, 6):
        return False

    if event["event_type"] not in VALID_EVENT_TYPES:
        return False

    if event["status"] not in VALID_STATUSES:
        return False

    return True
