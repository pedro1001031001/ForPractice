num1 : float = 1
num2 : float = 2
suma : float

def sum(numx, numy) :
    suma = numx + numy;
    print(f"La suma de los valores de {numx} y {numy} es {suma}")

print("")
print("Este programa suma dos valores dados por esl usuario.")
print("")

num1 = float(input("1.    Introduce el primer valor:  "))
num2 = float(input("2.    Introduce el segundo valor: "))
print("")

sum(num1, num2)
print("Estoy sumando en una función.")
print("")