-- creates the database and table with constraints
-- creates the database and table with constraints
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id));
