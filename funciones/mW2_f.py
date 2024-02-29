def descuento(pago, cantidad) :
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