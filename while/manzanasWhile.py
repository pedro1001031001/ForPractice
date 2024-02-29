cantidad : int = 1
precio : float = 0
pago : float = 0
descuento : float = 0
descuentoSecreto : float = 0
opcion = 1

print("")
print("Este programa determina el monto a cobrar por x cantidad de manzanas vendidas a un precio dado.")
print("")


cantidad = float(input("1. Ingresa numero de piezas vendidas: "))
    
while cantidad != 0 :
    precio = float(input("2. Introduzca el precio de las amnzana: "))
    print("")
    pago = (precio * cantidad)
    
    if cantidad == 18 :
        descuentoSecreto = pago * 0.15
        pago = pago - descuentoSecreto
        print(f"Se pago {pago}")
        print("")
    elif cantidad >= 10 and cantidad :
        descuento = pago * 0.1
        pago = pago - descuento
        print(f"Se pago {pago} a la cual ya se le aplico en descuento en monto de {descuento}.")
        print("")
    else :
        print(f"Se pago  {pago}")
        print("Gracias por su compra.")
        print("")
    
    opcion = int(input("¿quieres salir (introduce un 1):    "))




print("¡Adios!")



