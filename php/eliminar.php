<?php 
    include_once "conexion.php";

    $id = $_GET["id"];
    $sql_eliminar ="DELETE FROM colores WHERE id_colores = ?";
    $sentencia_eliminr = $pdo->prepare($sql_eliminar);
    $sentencia_eliminar = $sentencia_eliminr->execute(array($id));

    //  Cierre de la base de datos y sentencia
    $sentencia_eliminar = null;
    $pdo = null;

    header("location:index.php");
?>