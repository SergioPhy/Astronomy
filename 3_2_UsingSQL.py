#Abreviations and aliases for the table heads
#Write a query that returns the radius of each star and planet pair whose radii have a ratio greater than the Sun-to-Earth radius ratio. Order the results in 
#descending order based on the stellar radii. Use sun_radius and planet_radius as attribute aliases for the star and planet radii.

#For this problem you will have to join the two tables to find all planets belonging to a given star and use a condition to select those results which fulfill 
#the size requirement above.

SELECT s.radius AS sun_radius, p.radius AS planet_radius
FROM Star AS s, Planet AS p
WHERE s.kepler_id = p.kepler_id AND
      s.radius / p.radius > 1
ORDER BY s.radius DESC;

#-----------------------------------------------

#Write a query which counts the number of planets in each solar system where the corresponding stars are larger than our sun (i.e. their radius is larger than 1).

#Your query should return the star's radius and its number of planets, showing only rows where the number of planets is more than one. Sort the rows in descending
#order based on the star radii.

SELECT Star.radius, COUNT(Planet.koi_name)
FROM Star
JOIN Planet USING (kepler_id)
GROUP BY Star.kepler_id
HAVING COUNT(Planet.koi_name) > 1 AND Star.radius > 1
ORDER BY Star.radius DESC;

#-----------------------------------------------

#To practise your outer joins, write a query which returns the kepler_id, t_eff and radius for all stars in the Star table which haven't got a planet as join 
#partner. Order the resulting table based on the t_eff attribute in descending order.

SELECT Star.kepler_id, Star.t_eff, Star.radius
FROM Star
LEFT OUTER JOIN Planet USING (kepler_id)
WHERE Planet.koi_name IS NULL #Tal parece que koi_name nos dice cuando el planeta está junto a una estrella o no
ORDER BY Star.t_eff DESC;
