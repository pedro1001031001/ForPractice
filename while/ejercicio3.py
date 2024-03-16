import clearScreen

n : int = 0
 
print()
print("Este programa solicita valores enteros entre 0 y 20.")
print()

while n >= 20 & n <= 0 :
    n = int(input("1.   Introduce un número enteros menor a 10: "))


if n >= 0 & n <= 20: 
    clearScreen.borrarpantalla()        
    print(f"El número tecleado es {n}.")
    print()

