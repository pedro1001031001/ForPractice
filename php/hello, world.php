<?php
    /*  Fundamentos.
        paradigma: Orientado a objetos
        interpretado.
        Tipado dinámico o débil.
        Todas las variables se definene situando un signo de dólar antes.
        Soporta: operadores, estructuras de control, funciones, estructuras, clases.
        Se ejecuta del lado del servidor.
        Permite interartuar con request de forma más sencilla a través de la red.
        Hace: get, post que interactue con una API. Lo hace de forma nativa.
        Lenguaje que interartua con las bases de datos.
    */

    //  Hola munda
    echo "hola, PHP.\n";

    //  Variables
    $my_string = "Esto es una cadena de texto";
    $my_string = "Aquí cambio el valor de la cadena de texto";

    echo $my_string . "\n";

    echo gettype($my_string) . "\n";

    $my_string = 6;
    echo $my_string . "\n";

    echo gettype($my_string) . "\n";

    $my_int = 7;
    $my_int = $my_int + 4;
    echo $my_int . "\n";
    echo $my_int - 1 . "\n";
    echo $my_int . "\n";
    echo gettype($my_int) . "\n";

    $my_double = 6.5;
    echo gettype($my_double) . "\n";
    echo $my_double + $my_int . "\n";
    //echo $my_int + $my_double + $my_string . "\n";

    $my_bool = true;
    echo $my_bool . "\n";
    $my_bool = false;
    echo $my_bool . "\n";
    echo gettype($my_bool) . "\n";

    echo "El valor de mi integer es $my_int y el de mi boolean es $my_bool.\n";

    //  Constantes
    const MY_CONSTANT = "El valor de la constante";
    echo MY_CONSTANT . "\n";

    //  Listas
    $my_array = [$my_string, $my_int, $my_double];
    echo gettype($my_array) . "\n";
    echo $my_array[0] . "\n";
    echo $my_array[2] . "\n";
    array_push($my_array, $my_bool);
    print_r($my_array);

    //  Diccionario
    $my_dic = array("string" =>  $my_string, "int" => $my_int, "bool" => $my_bool);
    echo gettype($my_dic) . "\n";
    print_r($my_dic);
    echo $my_dic["int"] . "\n";

    //  Set > No repiten valores
    array_push($my_array, "Pedro");
    array_push($my_array, "Pedro");
    print_r($my_array) . "\n";
    print_r(array_unique($my_array)) . "\n";

    //  Ciclos de control
    for ($index = 0; $index <= 10; $index++){
        echo $index . "\n";
    }

    foreach($my_array as $my_item){
        echo $my_item . "\n";
    }

    $index = 0;
    while($index <= sizeof($my_array) - 1){
        echo $my_array[$index] . "\n";
        $index++;
    }


    $my_int = 13; 
    $my_string = "Hola";
    
    if($my_int == 11 && $my_string == "Hola"){
        echo "El valor es 11 \n";
    } elseif($my_int == 12 || $my_string == "Hola"){
        echo "El valor es 12 \n";
    }else{
        echo "El valor no es 11 \n";
    }

    function print_number(){
        echo "10" . "\n";
    }

    print_number();
?>

