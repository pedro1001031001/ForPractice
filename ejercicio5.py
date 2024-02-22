#   Declaración de las variables
num1 : float
num2 : float
num3 : float

#   Descripción del programa
print("")
print("Este programa evalua 3 números y determina si con respecto a cada uno se tiene igualdad")
print("")

#   Inicialización de las variables
num1 = float(input("1.  Introduce el primer valor:  "))
num2 = float(input("2.  Introduce el segundo valor: "))
num3 = float(input("3.  Introduce el tercer valor:  "))
print("")

#   Proceso y salida de datos
if num1 == num2 == num3 :
    print(f"Entre los valores otorgados, {num1}, {num2} y {num3}, se tiene igualdad")
    print("")
else :
    print("No son iguales los valores otorgados.")
    if num1 == num2 :
        print("Solo son iguales el primer y segundo número.")
        print("")
    elif num1 == num3 :
        print("Solo son iguales el primer y tercer número.")
        print("")
    elif num2 == num3 :
        print("Solo son iguales el segundo y tercer valor.")
        print("")
        
