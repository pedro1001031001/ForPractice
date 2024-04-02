/*
    
    Fue concebido para la web.
    Se programa con html y css
    Si senecesitaba algo más }
    Funciona en el explorador de web
    Es el lenguaje de la web
    Entiende todos los exploradores web
    Java es diferente de JavaScript
    Java era la palabra de moda
    Es interpretado.
    Se basa en la sintaxis de Java
    ECMAScript. Es la especificación.
    Se emplea para el desarrollo front-end.
    JavaScript se puede ejecutar en el servidor.
    Se emplea frameworks
    Se puede emplear para hacer para aplicaiones de escritorio y moviles con herramientas especificas
    MongoDB esta montado sobre el lenguaje
    Imperativo
    Basado en prototipos
    Lenguaje de tipado fácil
    el Backend 
*/

console.log("Hola, JavaScript")

//  Variables

var myString = "Esto es una cadena de texto" // Var es global
console.log(myString)

let myString2 = "Esta es una cadena de texto" //  Scoup, donde se habre llave y donde se cierra
myString = "Aquí cambia el valor de la cadena de texto"
console.log(typeof myString2)

myString2 = 6
console.log(myString2)
console.log(typeof myString2)

let myNumber = 7
myNumber = myNumber + 4
console.log(myNumber)
console.log(myNumber - 1)
console.log(myString + " " + myNumber)

let myNumber2 = 6.5
console.log(myNumber2)
console.log(typeof myNumber2)

let myBool = false
myBool = true
console.log(myBool)
console.log(typeof myBool)

myBool = null
console.log(myBool + myNumber2)

myBool = undefined
console.log(myBool)

let myUndefined
console.log(myUndefined)

//  Constantes
const MY_CONST = "Mi propiedad constante"
    //  MY_CONST = "Otro valor" <-- Error
console.log(MY_CONST)

//myNumber = 10
myString = "Hola"

//  Estructura de control
if (myNumber == 10 && myString == "Hola"){

    console.log("El valor es 10")

} else if (myNumber == 11 || myString == "Hola") {

    console.log("El valor es 11")

}else {

    console.log("El valor no es 10")

}

myBool = null

if (myBool){
    console.log("Null")
}

//  Funciones
function myFunction(){
    //console.log("Mi funcion")
    return "Mi función"
}

console.log(myFunction())

//  Listas
let myList = ["Pedro", "Aguilar", "31","Rodriguez"]
console.log(myList)
console.log(myList[0])

//  Set
let mySet = new Set(["Pedro", "Aguilar", "31","Rodriguez"])
mySet.add("Pedro")
console.log(mySet)

//  Mapa
let myMap = new Map([["pedro", 23], ["Aguilar", 10], ["Rodríguez", 21]])
myMap.set("Damian", 20)
console.log(myMap)
console.log(myMap.get("Pedro"))

//  Bucles
for (const value of myList){
    
    console.log(value)

}

let myCounter = 0

while (myCounter < myList.length){
    console.log(myList[myCounter])
    myCounter++
}

//  Clases
class MyClass{
    constructor(name, age){
        this.name = name
        this.age = age
    }
}

let myClass = new MyClass("pedro", 21)
console.log(myClass)
console.log(myClass.name)

//  Enum
const MyEnum ={
    DART: "dart",
    PYTHON: "python",
    SWIFT: "swift",
    JAVA: "java",
    KOTLIN : "kotlin",
    JAVASCRIPT : "javascript"
}

const myEnum = MyEnum.JAVASCRIPT
console.log(myEnum)