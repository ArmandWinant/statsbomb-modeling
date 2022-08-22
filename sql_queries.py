# DROP TABLES

events_table_drop = "DROP TABLE IF EXISTS events;"
matches_table_drop = "DROP TABLE IF EXISTS matches;"
players_table_drop = "DROP TABLE IF EXISTS players;"
teams_table_drop = "DROP TABLE IF EXISTS teams;"
competitions_table_drop = "DROP TABLE IF EXISTS competitions;"
related_events_table_drop = "DROP TABLE IF EXISTS related_events;"
referees_table_drop = "DROP TABLE IF EXISTS referees";

# CREATE TABLES

events_table_create = ("""
    CREATE TABLE IF NOT EXISTS events (
        id VARCHAR PRIMARY KEY,
        index SMALLINT NOT NULL,
        type VARCHAR NOT NULL,
        pattern VARCHAR NOT NULL,
        event_time TIME NOT NULL,
        period SMALLINT NOT NULL,
        location_x FLOAT,
        location_y FLOAT,
        possession_team SMALLINT NOT NULL,
        possession SMALLINT NOT NULL,
        match SMALLINT NOT NULL,
        player SMALLINT,
        team SMALLINT,
        duration FLOAT
    );
""")

matches_table_create = ("""
    CREATE TABLE IF NOT EXISTS matches (
        id SMALLINT PRIMARY KEY,
        match_date DATE,
        kick_off TIME,
        competition SMALLINT,
        season CHAR(9),
        match_week SMALLINT,
        competition_stage VARCHAR,
        stadium SMALLINT,
        home_team SMALLINT,
        away_team SMALLINT,
        home_score SMALLINT,
        away_score SMALLINT,
        match_status VARCHAR,
        last_updated TIMESTAMP
    );
""")

players_table_create = ("""
    CREATE TABLE IF NOT EXISTS players (
        id SMALLINT PRIMARY KEY,
        name VARCHAR,
        position VARCHAR,
        team SMALLINT
    );
""");

teams_table_create = ("""
    CREATE TABLE IF NOT EXISTS teams (
        id SMALLINT PRIMARY KEY,
        name VARCHAR NOT NULL,
        gender CHAR(1),
        country VARCHAR
    );
""")

competitions_table_create = ("""
    CREATE TABLE IF NOT EXISTS competitions (
        id SMALLINT PRIMARY KEY,
        name VARCHAR,
        season CHAR(7)
    );
""")

related_events_table_create = ("""
    CREATE TABLE IF NOT EXISTS related_events (
        event_x VARCHAR,
        event_y VARCHAR,
        PRIMARY KEY(event_x, event_y)
    );
""")

referees_table_create = ("""
    CREATE TABLE IF NOT EXISTS referees (
        id SMALLINT PRIMARY KEY,
        name VARCHAR,
        country SMALLINT
    );
""")

# INSERT RECORDS

events_table_insert = ("""
    INSERT INTO events (
        id,
        index,
        type,
        pattern,
        event_time,
        period,
        location_x,
        location_y,
        possession_team,
        possession,
        match,
        player,
        team,
        duration
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (id)
    DO NOTHING;
""")

matches_table_insert = ("""
    INSERT INTO matches (
        id,
        match_date,
        kick_off,
        competition,
        season,
        match_week,
        competition_stage,
        stadium,
        home_team,
        away_team,
        home_score,
        away_score,
        match_status,
        last_updated
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (id)
    DO UPDATE
    SET
        match_status = EXCLUDED.match_status,
        kick_off = EXCLUDED.kick_off,
        home_score = EXCLUDED.home_score,
        away_score = EXCLUDED.away_score,
        last_updated = EXCLUDED.last_updated;
""")

players_table_insert = ("""
    INSERT INTO players (
        id,
        name,
        position,
        team
    )
    VALUES (%s, %s, %s, %s)
    ON CONFLICT(id)
    DO UPDATE
    SET
        position = EXCLUDED.position,
        team = EXCLUDED.team;
""")

teams_table_insert = ("""
    INSERT INTO teams (
        id,
        name,
        gender,
        country
    )
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (id)
    DO UPDATE
    SET
        name = EXCLUDED.name;
""")

competitions_table_insert = ("""
    INSERT INTO competitions (
        id,
        name,
        season
    )
    VALUES (%s, %s, %s)
    ON CONFLICT (id)
    DO NOTHING;
""")

related_events_table_insert = ("""
    INSERT INTO related_events (
        event_x,
        event_y
    )
    VALUES (%s, %s);
""")

referees_table_insert = ("""
    INSERT INTO referees (
        id,
        name,
        country
    )
    VALUES (%s, %s, %s)
    ON CONFLICT (id)
    DO NOTHING;
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [events_table_create, matches_table_create, players_table_create, teams_table_create,
                        competitions_table_create, related_events_table_create, referees_table_create]
drop_table_queries = [events_table_drop, matches_table_drop, players_table_drop, teams_table_drop, competitions_table_drop,
                      related_events_table_drop, referees_table_drop]