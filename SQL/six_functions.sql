Use startersql;
-- SELECT COUNT(*) FROM users WHERE gender='Female';
-- SELECT gender, MIN(salary) AS min_salary, MAX(salary) AS max_salary FROM users GROUP BY gender;
-- SELECT * FROM users

-- SELECT SUM(salary) AS total_cub FROM users;
-- SELECT gender,AVG(salary) AS avg_sal FROM users GROUP BY gender;

-- SELECT name,length(name) AS name_len FROM users;
-- SELECT id,gender, LOWER(name) as lower,CONCAT(LOWER(name),"5678") AS user_name,month(date_of_birth) AS TIME, LENGTH(name) AS name_len FROM users;
-- SELECT name,DATEDIFF(CURDATE(), date_of_birth) AS days FROM users;


