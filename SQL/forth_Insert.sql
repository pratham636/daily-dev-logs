USE startersql;
-- SELECT name,gender,salary from users where date_of_birth<'1995-09-09';
-- SELECT * from users where id>10;
-- SELECT * from users WHERE date_of_birth is not NULL;
-- SELECT * from users WHERE date_of_birth BETWEEN '1990-09-09' AND '1999-09-09';
-- SELECT * from users WHERE gender in ('Male','Female')
-- SELECT * FROM users WHERE gender='female' AND salary>70000 ORDER BY date_of_birth DESC LIMIT 5;


-- UPDATE users SET salary = 45000 WHERE id=1;
-- SET SQL_SAFE_UPDATES=0;
-- UPDATE users SET salary=salary+10000 WHERE salary < 60000;
-- SET SQL_SAFE_UPDATES=1;
-- SET SQL_SAFE_UPDATES=0;
-- DELETE FROM users WHERE salary<65000;
-- SET SQL_SAFE_UPDATES=1;
-- DROP TABlE users;
SELECT * FROM users;