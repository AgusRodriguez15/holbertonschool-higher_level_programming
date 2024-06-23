-- cities by state
SELECT states.id, states.name, cities.id, cities.name FROM cities
    INNER JOIN states ON cities.state_id = state_id
    ORDER BY cities.id ASC;