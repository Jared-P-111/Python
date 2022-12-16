SELECT * FROM users;
SELECT * FROM users WHERE email = "janneygirl4@gmail.com";

INSERT INTO users (first_name, last_name, email, password)
VALUES	("Jane", "Amsden", "janneygirl4@gmail.com", "password123"),
		("Emily", "Dixon", "emmydixion@yahoo.com", "1122332211"),
        ("Theodore", "Dostoevsky", "littletheo@outlook.com", "passMyWord");
        
SET SQL_SAFE_UPDATES = 0;

DELETE FROM users; 