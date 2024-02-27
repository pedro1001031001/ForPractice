num1 : float = 1
num2 : float = 2
mul : float

def mult(numx, numy) :
    total = numx * numy
    print(f"La multiplicación de los valores  {numx} y {numy} es {total}")
    return total

print("")
print("Este programa multiplica dos valores, entre si, dados por esl usuario.")
print("")

num1 = float(input("1.    Introduce el primer valor:  "))
num2 = float(input("2.    Introduce el segundo valor: "))
print("")

resultado = mult(num1, num2)
print(resultado)
print("Estoy multiplicando en una función.")
print("")

