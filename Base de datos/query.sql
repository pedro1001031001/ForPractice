SELECT country.Name, country.Continent, countrylanguage.`Language`, countrylanguage.IsOfficial, city.Name, city.District
FROM country
LEFT JOIN countrylanguage ON country.code = countrylanguage.CountryCode
LEFT JOIN city ON country.Capital = city.ID
WHERE country.name = "mexico"

/* llave primaria */
