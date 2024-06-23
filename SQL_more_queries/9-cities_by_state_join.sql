-- cities by state
SELECT cities, name, name 
FROM cities
INNER JOIN states 
    ON cities.state_id = state.id
 ORDER BY cities.id;