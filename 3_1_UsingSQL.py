#Write an SQL query to find the radius and temperature of the stars in the Star table that are larger than our sun.

SELECT radius, t_eff FROM Star
WHERE radius > 1;

#---------------

#Your task is to write a range query which returns the kepler_id and the t_eff attributes of all those stars in the 
#Star table whose temperature lies between 5000 and 6000 Kelvin (inclusive).

SELECT kepler_id, t_eff FROM Star
WHERE t_eff BETWEEN 5000 AND 6000

#---------------

#In this question you should write a query to find the kepler_name and radius of each planet in the Planet table which 
#is a confirmed exoplanet, meaning that their kepler_name is not NULL, or, equivalently, whose status is 'CONFIRMED'.

SELECT kepler_name, radius FROM Planet
WHERE radius BETWEEN 1 AND 3 AND kepler_name IS NOT NULL;

#OR

SELECT kepler_name, radius 
FROM Planet
WHERE
  radius BETWEEN 1 AND 3 AND
  kepler_name IS NOT NULL;
  
#---------------

#Let's analyse the size of the unconfirmed exoplanets.

#Your task is to write a query that calculates the:

#minimum radius;
#maximum radius;
#average radius; and
#standard deviation of the radii
#of unconfirmed planets (with a NULL value in kepler_name) in the Planet table.

SELECT MIN(radius), MAX(radius), AVG(radius), STDDEV(radius)
FROM Planet
WHERE
  kepler_name IS NULL;

#---------------  
#You need to find out how many planets in the Planet database are in a multi-planet system. Planets sharing the same star 
#will have the same kepler_id, but different koi_name values.

#Your query should return a table in which each row contains the kepler_id of the star and the number of planets orbiting 
#that star (i.e. that share this kepler_id).

#Limit your results to counts above one and order the rows in descending order based on the number of planets.
#OBS: Here, we are not taking account if the planets have the status of confirmed or not.

SELECT kepler_id, COUNT(koi_name)
From Planet
GROUP BY kepler_id
HAVING COUNT(koi_name) > 1
ORDER BY COUNT(koi_name) DESC
