-- get all cities from DB
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id;
