import psycopg2
from typing import Iterable

def load_events(events: Iterable[dict]):
    conn = psycopg2.connect(
        host="127.0.0.1",
        port=5432,
        dbname="sentinel",
        user="sentinel",
        password="sentinel",
    )

    with conn:
        with conn.cursor() as cur:
            for event in events:
                cur.execute(
                    """
                    INSERT INTO events_raw (
                        id,
                        incident_id,
                        dispatcher_id,
                        location_id,
                        event_type,
                        severity,
                        status,
                        timestamp
                    )
                    VALUES (
                        %(id)s,
                        %(incident_id)s,
                        %(dispatcher_id)s,
                        %(location_id)s,
                        %(event_type)s,
                        %(severity)s,
                        %(status)s,
                        %(timestamp)s
                    )
                    """,
                    {
                        **event,
                        "id": str(event["id"]),
                        "incident_id": str(event["incident_id"]),
                    },
                )

    conn.close()
