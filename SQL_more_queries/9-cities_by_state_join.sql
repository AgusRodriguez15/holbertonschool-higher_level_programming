-- cities by state
SELECT states.name, cities.id, cities.name FROM cities
        INNER JOIN states ON cities.state_id = state.id
        ORDER BY cities.id;