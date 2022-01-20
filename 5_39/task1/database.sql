DROP TABLE IF EXISTS phonebook;

CREATE TABLE phonebook(
id_client integer PRIMARY KEY,
client_name text NOT NULL,
phone_number integer NOT NULL UNIQUE,
email TEXT);

INSERT INTO phonebook (client_name, phone_number, email)
VALUES("Andrew", 23456789, "email@email.com");

INSERT INTO phonebook (client_name, phone_number, email)
VALUES("Sergey", 76543215, "email2@email.com");

INSERT INTO phonebook (client_name, phone_number, email)
VALUES("Alexey", 75543215, "email3@email.com");

INSERT INTO phonebook (client_name, phone_number, email)
VALUES("Andrew", 76573452, "email4@email.com");

UPDATE phonebook
SET client_name = 'Andrii'
WHERE client_name = 'Andrew';

DELETE FROM phonebook
WHERE phone_number = 76573452;
