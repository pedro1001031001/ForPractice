cantidad : int = 0
precio : float = 0
pago : float = 0
descuento : float = 0

cantidad = float(input("1. Ingresa numero de piezas vendidas: "))
precio = float(input("2. Introduzca el precio de las amnzana: "))


pago = (precio * cantidad)


if cantidad >= 10 :
    descuento = pago * 0.1
    pago = pago - descuento
    print(f"Se pago {pago} a la cual ya se le aplico en descuento en monto de {descuento}")

if cantidad < 10 :
    print(f"Se pago  {pago}")

