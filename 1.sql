SELECT student_id, AVG(grade) AS average_grade
FROM grades
GROUP BY student_id
ORDER BY average_grade DESC
LIMIT 5;

SELECT student_id, AVG(grade) AS average_grade
FROM grades
WHERE subject_id = 'desired_subject_id'
GROUP BY student_id
ORDER BY average_grade DESC
LIMIT 1;


SELECT group_id, AVG(grade) AS average_grade
FROM grades
WHERE subject_id = 'desired_subject_id'
GROUP BY group_id;


SELECT AVG(grade) AS average_grade
FROM grades;


SELECT subject_id
FROM subjects
WHERE teacher_id = 'desired_teacher_id';
