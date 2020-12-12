DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS members;

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
    members_id SERIAL REFERENCES members(id),
    sessions_id SERIAL REFERENCES sessions(id)
);

