-- create user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
SET PASSWORD FOR 'user_0d_1'@'localhost' = PASSWORD('user_0d_1_pwd');
GRANT ALL PRIVILEGES ON hbtn_0c_0.* TO 'user_0d_1_'@'localhost';