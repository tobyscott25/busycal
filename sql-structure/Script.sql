CREATE DATABASE users;

use users;

CREATE TABLE user_info (
	user_id int NOT NULL AUTO_INCREMENT,
	username varchar(255) NOT NULL,
	email varchar(255) NOT NULL,
	verified bool DEFAULT False,
	display_name varchar(255) NOT NULL,
	password varchar(255) NOT NULL,
	PRIMARY KEY (user_id)
);



