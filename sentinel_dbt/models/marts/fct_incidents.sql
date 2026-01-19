{{ config(materialized='table') }}

WITH incident_bounds AS (
  SELECT
    incident_id,
    MIN(timestamp) AS started_at,
    MAX(timestamp) FILTER (WHERE event_type = 'incident_closed') AS closed_at,
    MAX(severity) AS incident_severity,
    COUNT(*) AS event_count
  FROM {{ ref('stg_events_raw') }}
  GROUP BY incident_id
)

SELECT
  incident_id,
  incident_severity,
  event_count,
  started_at,
  closed_at,
  closed_at - started_at AS duration
FROM incident_bounds
WHERE closed_at IS NOT NULL
