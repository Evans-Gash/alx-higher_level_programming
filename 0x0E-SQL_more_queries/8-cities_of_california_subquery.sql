--Shows all the cities of Carlifornia
-- Results are ordered by smallest to largest cities.id.
SELECT id, name FROM cities WHERE state_id = 1 ORDER BY cities.id ASC;
