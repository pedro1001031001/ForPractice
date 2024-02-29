#   Declaración de las variables
num1 : float
num2 : float

#   Descripción del programa
print("")
print("Este programa evalua dos valores numéricos para determinar cual de ellos es menor.")
print("")

#   Inicialización de las variables
num1 = input("1.    Introduce el primer valor numérico: ")
num2 = input("2.    Introduce el segundo númerico:  ")
print("")

#   Proceso y salida
if num1 > num2 :
    print( f"Entre {num1} y {num2}, el menor es {num2}.")
elif num1 < num2 :
    print(f"Entre {num1} y {num2}, el menor es {num1}.")
print("")