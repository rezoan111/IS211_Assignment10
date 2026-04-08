-- Part I: Music database
-- This file creates tables for artists, albums, and songs.

CREATE TABLE artists (
    id INTEGER PRIMARY KEY ASC,
    name TEXT
);

CREATE TABLE albums (
    id INTEGER PRIMARY KEY ASC,
    name TEXT,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES artists(id)
);

CREATE TABLE songs (
    id INTEGER PRIMARY KEY ASC,
    name TEXT,
    album_id INTEGER,
    track_number INTEGER,
    length_seconds INTEGER,
    FOREIGN KEY (album_id) REFERENCES albums(id)
);
