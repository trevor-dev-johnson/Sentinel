WITH incident_bounds AS (
  SELECT
    incident_id,
    MIN(timestamp) AS started_at,
    MAX(timestamp) FILTER (WHERE event_type = 'incident_closed') AS closed_at
  FROM events_raw
  GROUP BY incident_id
),
durations AS (
  SELECT
    incident_id,
    closed_at - started_at AS duration
  FROM incident_bounds
  WHERE closed_at IS NOT NULL
)

SELECT
  COUNT(*) AS closed_incidents,
  AVG(duration) AS avg_duration,
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY duration) AS p50_duration,
  PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY duration) AS p90_duration
FROM durations;
