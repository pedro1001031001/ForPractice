/*
    Usa lo mismo que java
    Java virtual machine
    No interactua con java, usa su principio
    Es de código abierto
    Evoluciona java, es iteroperable con java, puede interatuarse con las librerias de java
    Potencia los productos de la empresa
    No se preocupa por la migración
    Es el lenguaje principal para desarrollar aplicaciones en android
    No han caido en los ,is,os errores que java
    Es multiplataforma y multiparadigmatico
    Se adapta a los diferentes entornos
    Usos:  aplicaciones nativas en android, para crear back-end.
    Todo lo que funciona con java funciona con kotlin.
    Da soporte para crear webs,para crear aplicaiones plataformas, alicaiones de escritorio, aplicaiones de data science, estan en una etapa inicial, no estan del todo preparado.
    Se puede usar una misma base de código para ios android, se hace en partes diferentes la parte visual
    Valida data
    En ios, genera un códio c que le permita enender, optimiza todo, se tiene todo compilado.
    Se piuede decidir en que momenot se puede usar la multiplataforma.
    Es orientado a objetos.

*/

fun main(){
    println("Hola, kotlin")

    //  Fundamentos
    //      Variables
    var myString = "Esto es una cadena de texto"
        //myString = "aqui cqmbia el valor de la cadena de texto"
        //  myString = 6 - error
    println(myString)

    var myString2 : String = "Esto es otra cadena de texto"

    println(myString2)

    var myInt = 7
    myInt = myInt + 4
    println(myInt)
    println(myInt - 1)
    println(myInt)

    var myInt2 : Int = 5
    println(myInt2)

    var myDouble = 6.5
    println(myDouble)

    myDouble = 6.0
    println(myDouble)

    var myDouble2 : Double = 6.5
    var myFloat : Float = 6.5f
    var myBool : Boolean = true
    println(myFloat)
    println(myDouble2)
    println(myBool)

    //      Constantes
        //val myConst = "Mi propiedad constante"

    //  Estructura de control
    myInt = 48
    myString = "Hola"

    if (myInt == 11 && myString == "Hola"){
        println("El vlaor es 11")
    } else if (myInt == 10){
        println("El vlaor es 10")
    }else {
        println("El valor es distinto de 11")
    }
}