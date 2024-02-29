def descuento(pago, cantidad) :
    if cantidad == 18 :
        descuento = pago * 0.15
        print(f"Se le aplico en descuento en monto de {descuentoSecreto}.")
        print("")
    elif cantidad >= 10 and cantidad :
        descuento = pago * 0.1
        print(f"Se le aplico en descuento en monto de {descuento}.")
        print("")
    else :
        print("Gracias por su compra.")
        print("")
    
    return descuento