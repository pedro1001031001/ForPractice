<?php 

    $animales = ["Perro", "Gato", "Elefante", 11, true, false];
    //$animales = array();
?>

<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Prueba 3</title>
    </head>
    <body>
        <h1>
            Mi animal favorito es
            <?php
                echo $animales[1]?>
            <?php 
                /*
                for($i = 0; $i <= 2; $i++) {
                    echo "<h1>Mi animal favorito es ". $animales[$i] ."</h1>";
                }
                */

                foreach ($animales as $animal) {
                    echo "<h1>Mi animal favorito es ". $animal ."</h1>";
                }

            ?>
        </h1>
    </body>
</html>