CREATE KEYSPACE Datawatch WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 1 };
DESCRIBE keyspaces;
USE datawatch;

CREATE TABLE events
       (event_type varchar,
		event_time timestamp, 
		user_id varchar, 
		target_entity_id varchar,
		target_entity_type varchar,
		properties varchar,
		PRIMARY KEY ((event_type, target_entity_type, target_entity_id, user_id), event_time))
		WITH CLUSTERING ORDER BY (event_time DESC);

CREATE MATERIALIZED VIEW events_from_user AS SELECT * FROM events 
    WHERE event_type IS NOT NULL AND target_entity_type IS NOT NULL AND target_entity_id IS NOT NULL AND user_id IS NOT NULL AND event_time IS NOT NULL
    PRIMARY KEY ((user_id, event_type), target_entity_id, target_entity_type, event_time)
    WITH CLUSTERING ORDER BY (event_time desc);
	
CREATE MATERIALIZED VIEW events_by_item AS SELECT * FROM events 
    WHERE event_type IS NOT NULL AND target_entity_type IS NOT NULL AND target_entity_id IS NOT NULL AND user_id IS NOT NULL AND event_time IS NOT NULL 
    PRIMARY KEY ((event_type, target_entity_id), event_time, target_entity_type, user_id)
    WITH CLUSTERING ORDER BY (event_time desc);

CREATE MATERIALIZED VIEW all_events AS SELECT * FROM events
    WHERE event_type IS NOT NULL AND target_entity_type IS NOT NULL AND target_entity_id IS NOT NULL AND user_id IS NOT NULL AND event_time IS NOT NULL
    PRIMARY KEY (user_id, event_type, target_entity_id, target_entity_type, event_time)
    WITH CLUSTERING ORDER BY (event_time desc);

CREATE TABLE als_user_recommendations (user text,
		recommended_user text, 
		corr float,
		PRIMARY KEY (user, recommended_user));

CREATE TABLE als_item_recommendations (user_id text,
		item_id text, 
		rating float,
		PRIMARY KEY (user_id, item_id));
		
CREATE TABLE mba_recommendations (
	antecedent frozen<set<text>>,
	consequent frozen<set<text>>, 
	confidence float, 
	lift float,
	PRIMARY KEY (antecedent, consequent));
	
CREATE TABLE group_user_popularities (
	group varchar,
	rating int,
	user varchar,
	PRIMARY KEY (group, user));
		
CREATE TABLE userprofiles
       (user_id varchar,
		following set<text>,
		groups set<text>,
		PRIMARY KEY (user_id));
		
CREATE TABLE projects
       (project_id varchar,
		datasources set<text>,
		PRIMARY KEY (project_id));
		
CREATE TABLE item_ratings (
	user_id varchar,
	item_id varchar,
	rating double,
	PRIMARY KEY (user_id, item_id)
);

CREATE TABLE next_change_recommendations (
	antecedent frozen<list<text>>,
	consequent text,
	confidence float,
	PRIMARY KEY (antecedent, consequent));
