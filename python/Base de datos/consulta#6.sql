SELECT ct.Name AS "Nombre del país", ct.Continent AS "Continente", cl.`Language`, cl.IsOfficial, cy.Name, cy.District
FROM country ct
LEFT JOIN countrylanguage cl ON ct.code = cl.CountryCode
LEFT JOIN city cy ON ct.Capital = cy.ID
WHERE ct.name = "mexico"