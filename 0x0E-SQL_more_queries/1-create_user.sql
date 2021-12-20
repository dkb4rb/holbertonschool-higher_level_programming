-- Create New user in sql for all database permissions
-- in Mysql
CREATE USER
	IF NOT EXISTS user_0d_1@localhost
	IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
	ON *.*
	TO user_0d_1@localhost;
FLUSH PRIVILEGES;
