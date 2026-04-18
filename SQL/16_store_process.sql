USE startersql;
-- SELECT * FROM users;

-- DELIMITER $$
-- CREATE PROCEDURE add_users(
-- IN p_name VARCHAR(100),
-- IN p_email VARCHAR(100),
-- IN p_gender ENUM('Male','Female','Other'),
-- IN p_dob DATE,
-- IN p_salary INT
-- )
-- BEGIN
--  INSERT INTO users (name,email,gender,date_of_birth,salary)
--  VALUE (p_name,p_email,p_gender,p_dob,p_salary);
--  SELECT * FROM users;
--  END $$
--   DELIMITER ;
  
CALL add_users('Jone','john@harry.com','Other','1990-07-21',74000);