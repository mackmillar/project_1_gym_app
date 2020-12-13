DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS sessions;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    date VARCHAR(255),
    description TEXT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id SERIAL REFERENCES members(id) ON DELETE CASCADE,
    session_id SERIAL REFERENCES sessions(id) ON DELETE CASCADE
);

