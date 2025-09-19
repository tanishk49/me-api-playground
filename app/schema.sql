-- Profiles Table
CREATE TABLE profiles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    education VARCHAR(255),
    github VARCHAR(255)
);

-- Projects Table
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    skill VARCHAR(100) NOT NULL,
    profile_id INT NOT NULL REFERENCES profiles(id) ON DELETE CASCADE
);

-- Skills Table
CREATE TABLE skills (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    profile_id INT NOT NULL REFERENCES profiles(id) ON DELETE CASCADE
);
