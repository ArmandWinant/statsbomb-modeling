# DROP TABLES

matches_table_drop = "DROP TABLE IF EXISTS matches;"
events_table_drop = "DROP TABLE IF EXISTS events;"
teams_table_drop = "DROP TABLE IF EXISTS teams;"
players_table_drop = "DROP TABLE IF EXISTS players;"
play_patterns_table_drop = "DROP TABLE IF EXISTS play_patterns;"

# CREATE TABLES
competitions_table_create = ("""
    CREATE TABLE IF NOT EXISTS competitions (
        id SMALLINT PRIMARY KEY,
        
    );
""")

matches_table_create = ("""
    CREATE TABLE IF NOT EXISTS matches (
        id INT PRIMARY KEY,
        date DATE,
        competition_id SMALLINT,
        season SMALLINT,
        home_team_id SMALLINT,
        away_team_id SMALLINT,
        home_goals SMALLINT,
        away_goals SMALLINT,
        last_updated TIMESTAMP
    );
""")

events_table_create = ("""
    CREATE TABLE IF NOT EXISTS events (
        id VARCHAR PRIMARY KEY,
        match_id INT,
        index SMALLINT,
        period SMALLINT,
        minute SMALLINT,
        seconds REAL,
        type VARCHAR,
        pattern_id SMALLINT,
        team_id SMALLINT,
        possession SMALLINT,
        player_id SMALLINT,
        possession_team_id SMALLINT,
        duration REAL,
        position VARCHAR,
        location_x REAL
        location_y REAL
    );
""")

teams_table_create = ("""
    CREATE TABLE IF NOT EXISTS teams (
        id SMALLINT PRIMARY KEY,
        name VARCHAR,
        team_gender CHAR(1)
    );
""")

players_table_create = ("""
    CREATE TABLE IF NOT EXISTS players (
        id SMALLINT PRIMARY KEY,
        name VARCHAR,
        team_id SMALLINT,
        position VARCHAR,
        jersey_number SMALLINT
    );
""")

# INSERT RECORDS

events_table_insert = ("""
    INSERT INTO events (
        id,
        index,
        time,
        type,
        pattern_id,
        team_id,
        possession,
        posession_team_id
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (id)
    DO NOTHING;
""")

players_table_insert = ("""
    INSERT INTO players (
        id,
        name,
        team_id,
        position,
        jersey_number
    )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (id)
    DO UPDATE
    SET
        name = EXCLUDED.name,
        team_id = EXCLUDED.team_id,
        position = EXCLUDED.position,
        jersey_number = EXCLUDED.jersey_number;
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]