# AFSW
Automation for Swarm

**backend**:

Followed script need to be placed in new/updated "init.cql" file

`"CREATE MATERIALIZED VIEW all_events AS SELECT * FROM events
 WHERE event_type IS NOT NULL AND target_entity_type IS NOT NULL AND target_entity_id IS NOT NULL AND user_id IS NOT NULL AND event_time IS NOT NULL
 PRIMARY KEY (user_id, event_type, target_entity_id, target_entity_type, event_time)
    WITH CLUSTERING ORDER BY (event_time desc);"`
    
 
