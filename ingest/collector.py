from ingest.generator import generate_event
from ingest.loader import load_events
from ingest.validator import validate_event

def collect_events(n: int = 100):
    events = []

    for _ in range(n):
        event = generate_event()
        if validate_event(event):
            events.append(event)

    return events

if __name__ == "__main__":
    events = collect_events(100)
    load_events(events)
