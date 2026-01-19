import uuid
import random
from datetime import datetime, timedelta, timezone

EVENT_TYPES = [
    "call_received",
    "unit_dispatched",
    "unit_arrived",
    "incident_closed",
]

STATUSES = ["open", "in_progress", "closed"]

_ACTIVE_INCIDENTS: list[uuid.UUID] = []

MAX_ACTIVE_INCIDENTS = 25

def _get_incident_id() -> uuid.UUID:
  if _ACTIVE_INCIDENTS and random.random() < 0.7:
    return random.choice(_ACTIVE_INCIDENTS)
  
  incident_id = uuid.uuid4()
  
  if len(_ACTIVE_INCIDENTS) < MAX_ACTIVE_INCIDENTS:
    _ACTIVE_INCIDENTS.append(incident_id)
    
  return incident_id

def generate_event():
    incident_id = _get_incident_id()

    event_type = random.choice(EVENT_TYPES)
    status = (
        "closed"
        if event_type == "incident_closed"
        else random.choice(["open", "in_progress"])
    )

    if status == "closed" and incident_id in _ACTIVE_INCIDENTS:
        _ACTIVE_INCIDENTS.remove(incident_id)

    return {
        "id": uuid.uuid4(),
        "incident_id": incident_id,
        "dispatcher_id": random.randint(1, 20),
        "location_id": random.randint(1, 50),
        "event_type": event_type,
        "severity": random.randint(1, 5),
        "status": status,
        "timestamp": datetime.now(timezone.utc)
        - timedelta(seconds=random.randint(0, 3600)),
    }
