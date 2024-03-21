SELECT DISTINCT *
FROM usuario
WHERE nombre LIKE "b%"

UPDATE usuario SET apellido_pat = "Diaz"
WHERE nombre = "Bruce"

DELETE frOM usuario WHERE nombre = "Barry"