cantidad : int = 0
precio : float = 0
pago : float = 0
descuento : float = 0
descuentoSecreto : float = 0

cantidad = float(input("1. Ingresa numero de piezas vendidas: "))
precio = float(input("2. Introduzca el precio de las amnzana: "))
print("")


pago = (precio * cantidad)


if cantidad == 18 :
    descuentoSecreto = pago * 0.15
    pago = pago - descuentoSecreto
    print(f"Se pago {pago}")
elif cantidad >= 10 and cantidad :
    descuento = pago * 0.1
    pago = pago - descuento
    print(f"Se pago {pago} a la cual ya se le aplico en descuento en monto de {descuento}.")
else :
    print(f"Se pago  {pago}")
    print("Gracias por su compra.")

