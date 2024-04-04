<?php 

    function loremBy(){
        return "Lorem ipsum dolor sit, amet consectetur adipisicing elit.
        Neque libero vero corrupti omnis? Beatae magnam maiores veritatis doloremque harum! Quas repudiandae, est incidunt cumque asperiores rerum natus doloribus labore sit.
        Lorem ipsum dolor sit amet consectetur adipisicing elit.
        Debitis voluptatum ducimus quidem obcaecati veniam assumenda, excepturi exercitationem ut ad atque alias consequuntur dolor, saepe quis maxime repudiandae non, libero doloremque.";
    }

    function promedio($n1, $n2){
        return ($n1 + $n2) /2;
    }
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <section>
            <p>
                <?php echo loremBy();?>
                <?php echo loremBy();?>
                <?php echo loremBy();?>
                <br>
                <?php echo promedio(10, 10)?>
            </p>
        </section>
        <footer>
            <h1>Todos los derechos reservados - <?php echo date("Y")?></h1>
        </footer>
    </body>
</html>