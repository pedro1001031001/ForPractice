<?php 
    // echo "editar.php?id=1&color=success&descripcion=Este es un color verde.";
    // echo "<br>";

    //  El usuario debe enviar los datos atraves de la url

    $id = $_GET['id'];
    $color = $_GET["color"];
    $descripcion = $_GET["descripcion"];


    // echo $id;
    // echo "<br>";
    // echo $color;
    // echo "<br>";
    // echo $descripcion;

    include"conexion.php";

    $sql_editar = "UPDATE colores SET color=?, descripcion=? WHERE id_colores=?";
    $sentencia_editar = $pdo ->prepare($sql_editar);
    $sentencia_editar->execute(array($color, $descripcion, $id));


    //  Cierre de la conexión con la base de datos y sentencia
    $pdo = null;
    $sentencia_editar = null;
    
    header('location: index.php');
?>