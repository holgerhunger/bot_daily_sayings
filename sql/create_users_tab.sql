use daily_sayings_db;

DROP TABLE IF EXISTS users;

CREATE TABLE users(
    id int not null AUTO_INCREMENT,
    email varchar(256) not null unique,
    passwordhash varchar(256),
    name varchar(256),
    confirmed boolean,
    last_access date,
    weekdays varchar(16),
    PRIMARY KEY (id)
 );
