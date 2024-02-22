num1 : float
num2 : float

print("")
print("Este programa evalua dos valores numéricos para determinar cual de ellos es menor.")

num1 = input("1.    Introduce el primer valor numérico: ")
num2 = input("2.    Introduce el segundo númerico:  ")
print("")


if num1 > num2 :
    print( f"Entre {num1} y {num2}, el menor es {num2}.")
elif num1 < num2 :
    print(f"Entre {num1} y {num2}, el menor es {num1}.")
elif num1 == num2 :
    print(f"Los valores introducidos, {num1} y {num2}, son iguales")
print("")