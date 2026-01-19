import uuid
import random
from datetime import datetime, timedelta, timezone

EVENT_TYPES = [
    "call_received",
    "unit_dispatched",
    "unit_arrived",
    "incident_closed",
]

_ACTIVE_INCIDENTS: dict[uuid.UUID, datetime] = {}

MAX_ACTIVE_INCIDENTS = 25


def _get_incident_id() -> uuid.UUID:
    if _ACTIVE_INCIDENTS and random.random() < 0.7:
        return random.choice(list(_ACTIVE_INCIDENTS.keys()))

    incident_id = uuid.uuid4()

    if len(_ACTIVE_INCIDENTS) < MAX_ACTIVE_INCIDENTS:
        _ACTIVE_INCIDENTS[incident_id] = (
            datetime.now(timezone.utc)
            - timedelta(minutes=random.randint(1, 60))
        )

    return incident_id


def generate_event():
    incident_id = _get_incident_id()
    current_time = _ACTIVE_INCIDENTS[incident_id]

    event_type = random.choice(EVENT_TYPES)

    event_time = current_time + timedelta(minutes=random.randint(1, 15))

    _ACTIVE_INCIDENTS[incident_id] = event_time

    status = (
        "closed"
        if event_type == "incident_closed"
        else random.choice(["open", "in_progress"])
    )

    if status == "closed":
        _ACTIVE_INCIDENTS.pop(incident_id, None)

    return {
        "id": uuid.uuid4(),
        "incident_id": incident_id,
        "dispatcher_id": random.randint(1, 20),
        "location_id": random.randint(1, 50),
        "event_type": event_type,
        "severity": random.randint(1, 5),
        "status": status,
        "timestamp": event_time,
    }
