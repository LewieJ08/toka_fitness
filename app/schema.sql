-- USERS TABLE 

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username TEXT,
    hashed_password TEXT,
    email TEXT,
    membership_type TEXT,
    role TEXT DEFAULT 'member'
);