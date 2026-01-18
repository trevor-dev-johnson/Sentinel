from ingest.generator import generate_event
from ingest.loader import load_events

def collect_events(n: int = 100):
  return [generate_event() for _ in range(n)]

if __name__ == "__main__":
  events = collect_events(100)
  load_events(events)