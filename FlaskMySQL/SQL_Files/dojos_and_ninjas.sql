SELECT * FROM dojos;
SELECT * FROM ninjas;

INSERT INTO dojos (name) VALUES ("Seattle"), ("Denver"), ("Los Angeles");
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Jared", "Pisell", 22, 64);


SET SQL_SAFE_UPDATES = 0;

DELETE FROM dojos;  
DELETE FROM ninjas;