-- cities by state
SELECT states.id AS state_id, states.name AS state_name, 
       cities.id AS city_id, cities.name AS city_name
FROM states
INNER JOIN cities ON cities.state_id = state_id;
ORDER BY cities.id ASC;