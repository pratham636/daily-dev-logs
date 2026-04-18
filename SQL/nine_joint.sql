USE startersql;
SELECT * FROM users;
SELECT * FROM addresses;

-- SELECT users.name,users.gender,addresses.city,addresses.state,addresses.id as address_id
-- FROM users
-- INNER join addresses ON users.id = addresses.user_id;
SELECT users.name,users.gender,addresses.city,addresses.state,addresses.id as address_id
FROM users
left join addresses ON users.id = addresses.user_id;