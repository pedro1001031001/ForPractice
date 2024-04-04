<?php 

    //  PDO admite otras bases de datos
    //  Se crea una variable que contenga la 

    $link = "mysql:host=localhost;dbname=colores";
    $usuario = "root";
    $pass = "mysql";

    try {

        $pdo = new PDO($link, $usuario, $pass);

        //echo"Conectado" . "<br>";

        // foreach($pdo ->query("SELECT * FROM `colores`") as $row){
        //     print_r($row);
        //     print("</br>");
        // }
        
    }catch(PDOException $e) {
        print "¡Error!: " . $e ->getMessage() . "</br>";
        die();
    }
?>