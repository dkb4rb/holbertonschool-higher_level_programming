-- get data from cities that are equal to states data
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
	)
ORDER BY id;
