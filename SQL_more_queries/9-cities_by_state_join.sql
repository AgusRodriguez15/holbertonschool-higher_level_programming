-- cities by state
SELECT cities, name, name 
FROM cities
JOIN states 
    ON cities.state_id = state.id
 ORDER BY cities.id;