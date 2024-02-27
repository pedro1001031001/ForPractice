num1 : float = 1
num2 : float = 2
mul : float

print("")
print("Este programa multiplica dos valores, entre si, dados por esl usuario.")
print("")

num1 = float(input("1.    Introduce el primer valor:  "))
num2 = float(input("2.    Introduce el segundo valor: "))
print("")

def mult(numx, numy) :
    total = numx * numy
    print(f"La multiplicación de los valores  {numx} y {numy} es {total}")
    return total

total = mult(num1, num2)
print(total)
print("Estoy multiplicando en una función.")
print("")
