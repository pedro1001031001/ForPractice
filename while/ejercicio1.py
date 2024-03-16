import clearScreen

#   Este programa se ejecuta hasta que se tecle o, usando números enteros

n : int = 1

print("Este programa soicita números positivos y termina de salicitarlo hasta que se teclee cero")

while n != 0 :
    n = int(input("1.   Introduce un número positivo:   "))
    
    if n == 0 :
        clearScreen.borrarpantalla()
    
    if n == 0 :
        print("Has decidido salir. Gracias por usar el programa.")    
