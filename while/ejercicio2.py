n : int = 11
print()
print("Este programa solicita valores enteros menores a 10.")
print()

while n >=10 :
    n = int(input("1.   Introduce un número enteros menor a 10: "))
    print()

    if n < 10 : 
        print(f"El número tecleado {n} es menor a {10}.")
        print()

