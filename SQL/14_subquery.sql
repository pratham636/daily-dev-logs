USE startersql;
-- SELECT AVG(salary) FROM users;
-- SELECT * FROM users WHERE salary> (SELECT AVG(salary) FROM users);

SELECT id,name,referred_by_id,salary FROM users WHERE referred_by_id IN (SELECT id FROM users WHERE salary< (SELECT AVG(salary) FROM users));