SELECT * FROM books;
SELECT * FROM users;
SELECT * FROM favorites;

-- INSERT INTO users (first_name, last_name)
-- VALUES	("Jane", "Amsden"),("Emily", "Dixon"),("Theodore", "Dostoevsky"),
-- 		("William", "Shapiro"),("Lao", "Xiu");
--         

-- INSERT INTO books (title, num_of_pages)
-- VALUES	("C Sharp", 200),("Java", 300),("Python", 100),
-- 		("PHP", 10),("Ruby", 2000);
--         
-- -- share id amoungst the user and the books
-- INSERT INTO favorites(user_id, book_id)
-- VALUES (1, 1), (1, 2);

-- INSERT INTO favorites(user_id, book_id)
-- VALUES (2, 1), (2, 2), (2, 3);

-- INSERT INTO favorites(user_id, book_id)
-- VALUES (3, 1), (3, 2), (3, 3), (3, 4);

-- INSERT INTO favorites(user_id, book_id)
-- VALUES (4, 1), (4, 2), (4, 3), (4, 4);

-- SELECT * FROM favorites WHERE book_id = 3;

-- DELETE FROM favorites WHERE id = 5;

-- SELECT * FROM favorites WHERE user_id = 3;

-- SELECT * FROM favorites WHERE book_id = 3;



-- INSERT INTO favorites(user_id, book_id)
-- VALUES (5, 2);

DELETE FROM favorites WHERE book_id = 3 LIMIT 1;