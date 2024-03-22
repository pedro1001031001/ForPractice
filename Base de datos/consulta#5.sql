/** Left join muestrame los datos que se tienen en una tabla y sei se tienen en otra muestralos
*/
SELECT country.Name, country.Continent, city.Name, city.District
FROM country
left JOIN city
ON country.Name = "Zimbawe"
