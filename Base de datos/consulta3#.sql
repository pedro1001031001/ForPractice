SELECT country.Name, country.Continent, city.Name, city.District
FROM country
INNER JOIN city
ON country.Capital = city.ID

/**
	on es donde
*/
