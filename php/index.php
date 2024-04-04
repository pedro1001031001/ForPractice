<?php 
    include("conexion.php");

    //  echo"Desde archivo index.<br>";

    //  leer
    $sql_leer ="SELECT * FROM colores";
    $gsent = $pdo -> prepare($sql_leer);
    $gsent -> execute();
    $resultado = $gsent -> fetchAll();

    // var_dump($resultado);

    //  Agregar
    if($_POST){
        $color = $_POST['color'];
        $descripcion = $_POST['descripcion'];

        $sql_agregar ='INSERT INTO colores(color, descripcion) VALUES (?,?)';
        $sentencia_agregar = $pdo -> prepare($sql_agregar);
        $sentencia_agregar -> execute(array($color,$descripcion));

        //  Cierre de conexión de base de datos y sentencias
        //  Se hace cada que se ha una conexion
        $sentencia_agregar = null;
        $pdo = null;
        header('location: index.php');
    }

    //  Editar
    if($_GET){
        $id = $_GET['id'];
        $sql_unico ="SELECT * FROM colores WHERE id_colores = ?";
        $gsent_unico = $pdo -> prepare($sql_unico);
        $gsent_unico -> execute(array($id));
        $resultado_unico = $gsent_unico -> fetch();
        //var_dump($resultado_unico);
    }

?>
<!doctype html>

<html lang="es">

  <head>

    <meta charset="utf-8">

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Bootstrap demo</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
        crossorigin="anonymous"
    >

    <script src="https://kit.fontawesome.com/1dda4f402c.js" crossorigin="anonymous"></script>

  </head>

  <body>
    <div class="container mt-5">
        <div class="row">

            <div class="col-md-6">

                <?php foreach($resultado as $row): ?>

                    <div
                        class="alert
                        alert-<?php echo $row["color"]?>
                        text-uppercase"role="alert">
                        <?php echo $row["color"]?>
                        -
                        <?php echo $row["descripcion"]?>

                        <a href="index.php?id=<?php echo $row['id_colores']?>"
                        class="float-right">
                            <i class="fa-solid fa-pen-to-square"></i>
                        </a>

                        <a href="eliminar.php?id=<?php echo $row['id_colores']?>" class="float-right ml-3">
                            <i class="fa-regular fa-trash-can"></i>
                        </a>

                    </div>

                <?php endforeach; ?>

            </div>

            <div class="col-md-6">
                <?php if(!$_GET): ?>
                    <form method="POST">
                        <h3>Agregar elementos</h3>
                        <input type="text" class="form-control" name="color">
                        <input type="text" class="form-control" name="descripcion">
                        <button class="btn btn-primary mt-3">Agregar</button>
                    </form>
                <?php endif ?>

                <?php if($_GET): ?>
                    <form method="GET" action="editar.php">
                        <h3>Editar elementos</h3>
                        <input
                            type="text"
                            class="form-control"
                            name="color"
                            value="<?php echo $resultado_unico["color"]?>"
                        >

                        <input
                            type="text"
                            class="form-control"
                            name="descripcion"
                            value="<?php echo $resultado_unico["descripcion"]?>"
                            >
                        
                        <input
                            type="hidden"
                            name="id"
                            value="<?php echo $resultado_unico["id_colores"]?>"
                        >

                        <button class="btn btn-primary mt-3">Modificar</button>
                    </form>
                <?php endif ?>
            </div>

        </div>
        
    </div>

    <script
        src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous">
    </script>

    <script
        src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"
        integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r"
        crossorigin="anonymous">
    </script>

    <script
        src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"
        integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy"
        crossorigin="anonymous">
    </script>

  </body>

</html>

<?php 
    //  Cierre de conexión de la base de datos y sentencia
    $pdo = null;
    $gsent = null;
?>