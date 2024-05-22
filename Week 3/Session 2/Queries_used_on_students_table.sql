INSERT INTO students (first_name , last_name , email) VALUES("x" , "x" , "x@gmail.com");

SELECT * FROM students;

UPDATE students SET email = "MikeDoe@gmail.com" WHERE id = 2;

DELETE FROM students WHERE id = 3;