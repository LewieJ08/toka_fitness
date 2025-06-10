-- USERS TABLE 

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
    email TEXT,
    role TEXT
);