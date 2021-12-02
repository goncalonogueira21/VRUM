CREATE DATABASE user_authentication;

USE user_authentication;

CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT, 
    email VARCHAR(255) NOT NULL, 
    password_salt VARCHAR(255) NOT NULL, 
    password_hash VARCHAR(255) NOT NULL, 
    PRIMARY KEY (id), UNIQUE (email)
);