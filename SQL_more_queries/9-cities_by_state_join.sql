-- cities by state
USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name
FROM cities
    JOIN states
        ON cities.id = state_id;