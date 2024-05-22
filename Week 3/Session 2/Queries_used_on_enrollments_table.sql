INSERT INTO enrollments (students_id , courses_id , grades) VALUES(4 , 2 , 20);

SELECT 
students.id, students.first_name, students.last_name , 
courses.id , courses.name, courses.description
FROM students 
LEFT JOIN enrollments ON students.id = enrollments.students_id
LEFT JOIN courses ON courses.id = enrollments.courses_id;