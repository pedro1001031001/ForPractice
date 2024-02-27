#   Declaración de las variables
año : int

#   Descripción de las variables
print("")
print("Este programa determina si el año es bisiesto con respecto a los días")
print("")

#   Inicialización de las variables
año = int(input("1. Introduzca: "))
print("")

#   Proceso y salida de los datos
if año % 4 == 0 :
    print("Es bisiesto")
elif año % 4 and año % 100 != 0 :
    print("")
elif año % 100 != 0 :
    print("No es bisiesto")
