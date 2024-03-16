import clearScreen

n : int = 0
i : int = 0

print()
print("Este programa solicita valores enteros entre 0 y 20, y cuenta las veces que se ha introducido un valor.")
print()

while n >= 20 & n <= 0 :
    n = int(input("1.   Introduce un número enteros menor a 10: "))
    i = i + 1
    
    print(f"Se ha introducido {i} valores.")


if n >= 0 & n <= 20: 
    clearScreen.borrarpantalla()        
    print(f"El número tecleado es {n}.")
    print()

