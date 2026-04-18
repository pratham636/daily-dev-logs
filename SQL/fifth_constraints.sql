USE startersql;
ALTER TABLE users ADD CONSTRAINT chk_dob CHECK (date_of_birth > '1920-01-01');
-- ALTER TABLE users ADD CONSTRAINT unique_date_of_birth UNIQUE (date_of_birth);
SELECT * FROM users;