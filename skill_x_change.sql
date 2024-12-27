CREATE DATABASE skillx_db;

USE skillx_db;

INSERT INTO users(id, username, email, password_hash, rating)
VALUES(1, 'tc', 'tc@gmail.com', 'abcde', 1);
SELECT * FROM users;
CREATE TABLE users (
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(50) NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE,
password_hash VARCHAR(100) NOT NULL,
rating FLOAT DEFAULT 0,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE skills (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
description TEXT
);

CREATE TABLE user_skills (
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT NOT NULL,
skill_id INT NOT NULL,
proficiency_level VARCHAR(50),
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (skill_id) REFERENCES skills(id)
);

CREATE TABLE listings (
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT NOT NULL,
skill_id INT NOT NULL,
title VARCHAR(255) NOT NULL,
description TEXT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (skill_id) REFERENCES skills(id)
);

CREATE TABLE transactions (
id INT AUTO_INCREMENT PRIMARY KEY,
listing_id INT NOT NULL,
requester_id INT NOT NULL,
status ENUM('pending', 'completed', 'cancelled'),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
completed_at TIMESTAMP,
FOREIGN KEY (listing_id) REFERENCES listings(id),
FOREIGN KEY (requester_id) REFERENCES users(id)
);


CREATE TABLE reviews (
id INT AUTO_INCREMENT PRIMARY KEY,
reviewer_id INT NOT NULL,
reviewee_id INT NOT NULL,
transaction_id INT NOT NULL,
rating INT CHECK (rating >= 1 AND rating <= 5),
comment TEXT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (reviewer_id) REFERENCES users(id),
FOREIGN KEY (reviewee_id) REFERENCES users(id),
FOREIGN KEY (transaction_id) REFERENCES transactions(id)
);

