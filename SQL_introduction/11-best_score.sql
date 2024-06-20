-- list all the records >= 10
SELECT score, name FROM second_table GROUP BY score ORDER BY >=10 DESC;