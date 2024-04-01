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
    myInt = 11
    myString = "PedroDev"

    if (myInt == 10 && myString == "Hola"){
        println("El valor es 10")
    } else if (myInt == 11 || myString == "Hola"){
        println("El valor es 11")
    }else {
        println("El valor ni es 10 ni 11.")
    }

    //  Estructuras
    var myList = mutableListOf<String>("Pedro", "Aguilar", "Rodríguez")
    println(myList[1])
    myList.add("Pedro")
    println(myList)

    //      sets
    var mySet = setOf("Pedro", "Aguilar","Rodríguez","Pedro")
    println(mySet)

    //      Mapas
    //  Estructura que permite diferentes tipos
    var myMap = mutableMapOf("Pedro" to 36, "Aguilar" to 31, "Rodríguez" to 81)
    myMap["Damian"] = 80
    println(myMap["Pedro"])

    //  Bucles
    for (value in myList){
        println(value)
    }

    for (value in mySet){
        println(value)
    }

    for (value in myMap){
        println(value)
    }

    var myCounter = 0
    
    while(myCounter < myList.count()){
        println(myList[myCounter])
        myCounter ++
        myFunction()
    }

    //  opcionales
    var myOpcional : String? = null
    myOpcional = "Mi cadena de texto opcional"
    println(myOpcional)

    //  Funciones
    myFunction()

    //  Clases
    var MyClass = MyClass("Pedro",21)
    println(MyClass.age)
    MyClass.myFunction()

    //  Interpolación de datos
    println("Este es el valor de la variable myInt: $myInt")
}

//  Funciones
    fun myFunction(){
        println("Esto es una función")
    }

//  Clases 
class MyClass (val name : String, val age : Int){

    fun myFunction(){
        println("Esto es una función en una clase.")
    }

}