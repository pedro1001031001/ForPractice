import funciones.funcionesManzanas.m_Descuento as m_Descuento
import clearScreen

cantidad : int = 1
precio : float = 0
pago : float = 0
descuento : float = 0
descuentoSecreto : float = 0
opcion = 1

print("")
print("Este programa determina el monto a cobrar por x cantidad de frutas vendidas a un precio dado.")
print("")


    
while cantidad != 0 :
    
    cantidad = float(input("1. Ingresa numero de piezas vendidas: "))
    
    if cantidad == 0 :
        clearScreen.borrarpantalla()
        break
    
    precio = float(input("2. Introduzca el precio de las : "))
    print("")
    
    pago = (precio * cantidad)
    descuento = m_Descuento.descuento(pago, cantidad)
    Pago = pago - descuento
    
    print(f"Se pago  {pago}")
    cantidad = int(input("¿quieres salir (introduce un 0):    "))


print("¡Adios!")
clearScreen.borrarpantalla()



