-- A script that prepares a MYSQL server for the project
-- A database of name hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Created a user with password hbnb_dev_pwd in localhost
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all pviledges for the hbnb_dev on hbnb_dev_db.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grants SELECT privilege for hbnb_dev on performance_schema.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
