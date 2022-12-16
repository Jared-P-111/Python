SELECT * FROM dojos;
SELECT * FROM ninjas;

INSERT INTO dojos (name) VALUES ("Seattle"), ("Denver"), ("Los Angeles");

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Chuck", "Norris", 40, 87), ("Bruce", "Lee", 30, 87), ("Jackie", "Chan", 55, 87);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Jet", "Li", 22, 88), ("Ung", "Bok", 18, 88);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Arnold", "Schwarzenegger", 50, 89), ("Sylvester", "Stallone", 44, 89);

SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = 87;

SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id;

DELETE FROM dojos WHERE id;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM dojos;  
DELETE FROM ninjas;

