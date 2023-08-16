-- Displays the average temperature (in Fahrenheit)
-- by city arranged from largest to smallest temp.
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
