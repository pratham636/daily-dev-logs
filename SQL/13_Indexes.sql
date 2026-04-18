USE startersql;
-- CREATE INDEX idx_email ON users(name);
DROP INDEX date_of_birth ON users;
SHOW INDEXES FROM users;

select * from users;
SELECT * FROM users WHERE gender='Female' and salary>70000;