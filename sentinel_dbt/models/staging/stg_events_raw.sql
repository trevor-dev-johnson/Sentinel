{{ config(materialized='view') }}

SELECT
  id,
  incident_id,
  dispatcher_id,
  location_id,
  event_type,
  severity,
  status,
  timestamp
FROM public.events_raw
