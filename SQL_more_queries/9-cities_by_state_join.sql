-- cities by state
USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name
FROM cities
    JOIN states
        ON cities.state_id = state_id
ORDER BY cities.id