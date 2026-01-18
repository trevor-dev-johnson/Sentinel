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

def generate_event():
    return {
        "id": uuid.uuid4(),
        "incident_id": uuid.uuid4(),
        "dispatcher_id": random.randint(1, 20),
        "location_id": random.randint(1, 50),
        "event_type": random.choice(EVENT_TYPES),
        "severity": random.randint(1, 5),
        "status": random.choice(STATUSES),
        "timestamp": datetime.now(timezone.utc)
        - timedelta(seconds=random.randint(0, 3600)),
    }
