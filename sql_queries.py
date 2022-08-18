# DROP TABLES

events_table_drop = "DROP TABLE IF EXISTS events;"
matches_table_drop = "DROP TABLE IF EXISTS matches;"
players_table_drop = "DROP TABLE IF EXISTS players;"
teams_table_drop = "DROP TABLE IF EXISTS teams;"
competitions_table_drop = "DROP TABLE IF EXISTS competitions;"
related_events_table_drop = "DROP TABLE IF EXISTS related_events;"

# CREATE TABLES

events_table_create = ("""
    CREATE TABLE IF NOT EXISTS events (
        id SMALLINT PRIMARY KEY,
        index SMALLINT NOT NULL,
        type VARCHAR NOT NULL,
        event_time TIMESTAMP NOT NULL,
        period SMALLINT NOT NULL,
        location_x FLOAT,
        location_y FLOAT,
        position VARCHAR,
        possession_team SMALLINT,
        possession SMALLINT,
        match SMALLINT NOT NULL,
        player SMALLINT,
        duration FLOAT
    );
""")

matches_table_create = ("""
    CREATE TABLE IF NOT EXISTS matches (
        id SMALLINT PRIMARY KEY,
        stadium SMALLINT,
        match_date DATE,
        competition SMALLINT,
        home_team SMALLINT,
        away_team SMALLINT,
        home_score SMALLINT,
        away_score SMALLINT
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
        name VARCHAR,
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
        event_x SMALLINT,
        event_y SMALLINT,
        PRIMARY KEY(event_x, event_y);
    );
""")

# INSERT RECORDS

events_table_insert = ("""
    INSERT INTO events (
        id,
        index,
        type,
        event_time,
        period,
        location_x,
        location_y,
        position,
        possession_team,
        possession,
        match,
        player,
        duration) 
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (id)
    DO NOTHING;
""")

matches_table_insert = ("""
    INSERT INTO (
        id,
        stadium,
        match_date
        competition,
        home_team,
        away_team,
        home_score,
        away_score
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (id)
    DO NOTHING;
""")

players_table_insert = ("""
    INSERT INTO matches (
        id,
        stadium,
        match_date,
        competition,
        home_team,
        away_team,
        home_score,
        away_score
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT(id)
    DO NOTHING;
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
        name = EXCLUCED.name;
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

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [events_table_create, matches_table_create, players_table_create, teams_table_create,
                        competitions_table_create, related_events_table_create]
drop_table_queries = [events_table_drop, matches_table_drop, players_table_drop, teams_table_drop, competitions_table_drop,
                      related_events_table_drop]