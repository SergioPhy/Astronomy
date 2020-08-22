#Write an SQL query to find the radius and temperature of the stars in the Star table that are larger than our sun.

SELECT radius, t_eff FROM Star
WHERE radius > 1;

#Your task is to write a range query which returns the kepler_id and the t_eff attributes of all those stars in the 
#Star table whose temperature lies between 5000 and 6000 Kelvin (inclusive).

SELECT kepler_id, t_eff FROM Star
WHERE t_eff BETWEEN 5000 AND 6000
