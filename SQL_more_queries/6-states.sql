-- create databse and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
    PRIMARY KEY (id)
);