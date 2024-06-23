-- cities by state
SELECT states.id, states.name, cities.id, cities.name FROM states
INNER JOIN cities ON cities.state_id = state_id;