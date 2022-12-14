SELECT * FROM dojos;
SELECT * FROM ninjas;

INSERT INTO dojos (name) VALUES ("Seattle"), ("Denver"), ("Los Angeles");

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Chuck", "Norris", 40, 83), ("Bruce", "Lee", 30, 83), ("Jackie", "Chan", 55, 83);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Jet", "Li", 22, 84), ("Ung", "Bok", 18, 84);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Arnold", "Schwarzenegger", 50, 85), ("Sylvester", "Stallone");

SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id;

DELETE FROM dojos WHERE id;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM dojos;  
DELETE FROM ninjas;

