import uuid
from datetime import datetime, timezone
import psycopg2
from psycopg2.extras import register_uuid

register_uuid()

def insert_one_event():
    print("Connecting to Postgres...")
    conn = psycopg2.connect(
        host="127.0.0.1",
        port=5432,
        dbname="sentinel",
        user="sentinel",
        password="sentinel",
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS events_raw (
            id UUID PRIMARY KEY,
            incident_id UUID,
            dispatcher_id INTEGER,
            location_id INTEGER,
            event_type TEXT,
            severity INTEGER,
            status TEXT,
            timestamp TIMESTAMPTZ
        );
    """)

    print("Executing INSERT...")
    cur.execute(
        """
        INSERT INTO events_raw (
            id, incident_id, dispatcher_id, location_id, 
            event_type, severity, status, timestamp
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            uuid.uuid4(),
            uuid.uuid4(),
            1,
            1,
            "call_received",
            3,
            "open",
            datetime.now(timezone.utc),
        ),
    )

    conn.commit()
    print("DONE.")
    cur.close()
    conn.close()

if __name__ == "__main__":
    insert_one_event()