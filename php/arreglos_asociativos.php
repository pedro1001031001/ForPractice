<?php 
    $ciudad[0] = [
        "Nombre"=> "Valdivia",
        "Población"=> 100,
    ];

    $ciudad[1] = [
        "Nombre"=> "Puerto Varas",
        "Población"=> 25
    ];

?>
<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>prueba 4</title>
    </head>
    <body>
        <h1>Ciudades</h1>
        <hr>
        <?php 

            // for ($i = 1; $i <= 1, $i++) {
            //     echo "<h2> Nombre: " . $ciudad[$i]["Nombre"] . "</h2>";
            //     echo "<h2> Población: " . $ciudad[$i]["Población"] . "</h2>";
            //     echo "<hr>";
            // }

            foreach ($ciudad as $value) {
                echo "<h2> Nombre: " . $value["Nombre"] . "</h2>";
                 echo "<h2> Población: " . $value["Población"] . "</h2>";
                 echo "<hr>";
            }
        ?>
    </body>
</html>