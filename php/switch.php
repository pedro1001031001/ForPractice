<?php 
    $eleccion = "helado";

    switch( $eleccion ) {
        case'helado':
            echo"El valor del helado es de $ 1,000.00";
            break;
        case 'pizza':
            echo "El valor de la pizza es de 5,000.00";
            break;
        case 'torta':
            echo "El valor de la torta es de $ 10,000.00";
            break;
        default:
            echo "Opción no valida";
            break;
    } //    El switch siempres se usa con comillas simples
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Prueba 6</title>
    </head>
    <body>
        <h1>Ingresa una opción: </h1>
        <hr>
        <h2>1)  Pizza</h2>
        <h2>2)  Helado</h2>
        <h2>3)  Torta</h2>
    </body>
</html>