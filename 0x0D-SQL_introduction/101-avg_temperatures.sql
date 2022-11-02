-- displays the average temperature by city ordered by temperature
SELECT city, AVG(value) as avg_temp FROM tempreatures GROUP BY city ORDER BY avg_temp DESC;
