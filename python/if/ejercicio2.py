numCliente : int
numGanador : int = 1000

print("")
print("Este programa evalua el número de cliente para reconcoer a un ganador")
print("")

numCliente = int(input("1.  Introduce el número de cliente: "))
print("")

if numCliente == numGanador :
    print("¡Felicidades! Ganaste un premio")
else :
    print("¡Sigue participando!")
print("")