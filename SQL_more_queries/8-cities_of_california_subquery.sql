-- cities of california
USE hbtn_0d_usa;
SELECT name
    FROM states
    WHERE name = California
    ORDER BY cities.id ASC;