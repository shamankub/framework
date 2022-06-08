
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS client;
CREATE TABLE client (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, name VARCHAR (32));

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
