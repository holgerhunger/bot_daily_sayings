use daily_sayings_db;

DROP TABLE IF EXISTS secret_keys;

CREATE TABLE secret_keys(
    id int not null AUTO_INCREMENT,
    name varchar(64) not null unique,
    value varchar(256),
    PRIMARY KEY (id)
);
