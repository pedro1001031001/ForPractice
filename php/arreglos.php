<?php 

    $animales = ["Perro", "Gato", "Elefante"];
    //$animales = array();
?>

<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Prueba 2</title>
    </head>
    <body>
        <h1>
            Mi animal favorito es
            <?php
                echo $animales[1]?>
            <?php 

                $i = 0;
                while($i <= 2) {
                    echo "<h1>Mi animal favorito es ". $animales[$i] ."</h1>";
                    $i++;
                }

            ?>
        </h1>
    </body>
</html>