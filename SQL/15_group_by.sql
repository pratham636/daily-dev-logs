USE startersql;
-- SELECT gender,AVG(salary) as 'Average Salary' FROM users GROUP BY gender;
SELECT gender,AVG(salary) as 'AVG' , COUNT(*) AS 'Count' FROM users GROUP BY gender HAVING AVG (salary) >61000;
SELECT referred_by_id, COUNT(*) AS total_referred
FROM users
WHERE referred_by_id IS NOT NULL
GROUP BY referred_by_id with rollup
HAVING COUNT(*) >1;