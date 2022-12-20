SELECT * FROM recipes;
SELECT * FROM users;

SELECT * FROM users WHERE email = "jaredpisell";
SELECT * FROM users WHERE email = "gofast@yahoo.com";


INSERT INTO recipes (posted_by_user_id, recipe_name, description, instructions, date_cooked, under_30_min) 
-- VALUES (%(posted_by_user_id)s, %(recipe_name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_30_min)s);
VALUES ("1", "Spaghetti", "Its Pasta bitch", "cook that shit up!","2022-12-05", True);

DELETE FROM users WHERE id;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM users; 