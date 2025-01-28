import shlex
import sys
import os

#   Declaración de variables
ejercicio : int = 0
opcion : int = 0

#       Bonos
seleccion : chr = 's'
InversionInicial : float = 10000
Tasa : float = 0.0978
Plazo : int = 365
ValorNominalCETE : float = 100

#       Posición en largo
CantidadAccionesLargo : int = 100
PrecioCompra : float = 50
PrecioVenta : float = 55
DividendosAccion : float = 2

#      Posición en corto
CantidadAccionesCorto : int = 200
PrecioVentaInicial : float = 80
PrecioRecompraFinal : float = 70

#       Funciones Bonos
PrecioCETE : float = 0
NumeroCETE : int = 0
MontoTotalVencimiento : float = 0
GananciaTotal : float = 0

#       Funciones Acciones
GananciaLargo : float = 0
GananciaCorto : float = 0


### Ejercicio 1 - Calculo del rendimiento de una inversión en CETES.
def CalculoPrecioAdquision(Tasa, Plazo, PrecioCETE):
    PrecioCETE = 100/(1+((Tasa * Plazo)/360))
    
    return PrecioCETE

def CalculoNumeroCetesComprar(NumeroCETE, InversionInicial, PrecioCETE):
    NumeroCETE = (InversionInicial/PrecioCETE)
    
    return NumeroCETE

def calculoMontoTotalVencimiento(NumeroCETE, ValorNominalCETE, MontoTotalVencimiento):
    MontoTotalVencimiento = NumeroCETE * ValorNominalCETE
    
    return MontoTotalVencimiento

def CalculoGananciaTotal(MontoTotalVencimiento, InversionInicial, GananciaTotal):
    GananciaTotal = MontoTotalVencimiento - InversionInicial
    
    return GananciaTotal

def menu_bonos(seleccion):
        
    seleccion = input(f"\n¿Deseas calcular el rendimiento de una inversión en CETES (s ó n)?    ")
    
    if seleccion == 's' or seleccion == 'S':
        bonos(InversionInicial, Tasa, Plazo, ValorNominalCETE, PrecioCETE, NumeroCETE, MontoTotalVencimiento, seleccion, GananciaTotal)
    else:
        menu_Ejercicios(ejercicio)

def bonos(InversionInicial, Tasa, Plazo, ValorNominalCETE, PrecioCETE, NumeroCETE, MontoTotalVencimiento, seleccion, GananciaTotal):
    os.system("cls")
    
    seleccion = input("Para el calculo del rendimiento de un bono, ¿deseas usar los valores establecidos (s ó n)?   ")
    
    if seleccion == 'S' or seleccion == 's':
        PrecioCETE = CalculoPrecioAdquision(Tasa, Plazo, PrecioCETE)
        NumeroCETE = CalculoNumeroCetesComprar(NumeroCETE, InversionInicial, PrecioCETE)
        MontoTotalVencimiento = calculoMontoTotalVencimiento(NumeroCETE, ValorNominalCETE, MontoTotalVencimiento)
        GananciaTotal = CalculoGananciaTotal(MontoTotalVencimiento, InversionInicial, GananciaTotal)
        
        print(f"\nEl precio de adquisición del CETE es de ",PrecioCETE)
        print(f"El número de CETES a comprar es de ",int(NumeroCETE))
        print(f"El monto total al vencimiento es de ",MontoTotalVencimiento)
        print(f"La ganancia total obtenida es de ",GananciaTotal)
    else:
        Tasa = float(input(f"1.   Introduce la tasa de retorno del CETE (en valor decimal):  "))
        Plazo = float(input(f"2.   Introduce el plazo de la inversión:  "))
        InversionInicial = float(input(f"3.   Introduce el monto de la inversión (ó capital):  "))
        
        PrecioCETE = CalculoPrecioAdquision(Tasa, Plazo, PrecioCETE)
        NumeroCETE = CalculoNumeroCetesComprar(NumeroCETE, InversionInicial, PrecioCETE)
        MontoTotalVencimiento = calculoMontoTotalVencimiento(NumeroCETE, ValorNominalCETE, MontoTotalVencimiento)
        GananciaTotal = CalculoGananciaTotal(MontoTotalVencimiento, InversionInicial, GananciaTotal)
        
        print(f"\nEl precio de adquisición del CETE es de ",PrecioCETE)
        print(f"El número de CETES a comprar es de ",int(NumeroCETE))
        print(f"El monto total al vencimiento es de ",MontoTotalVencimiento)
        print(f"La ganancia total obtenida es de ",GananciaTotal)
    
    menu_bonos(seleccion)

###   Ejercicio 2 - Inversiones en acciones (largo y corto).
def Largo(PrecioVenta, PrecioCompra, CantidadAccionesLargo, DividendosAccion, GananciaLargo):
    GananciaLargo = (PrecioVenta - PrecioCompra) * CantidadAccionesLargo + (DividendosAccion * CantidadAccionesLargo)
    
    return GananciaLargo

def Corto(PrecioVentaInicial, PrecioRecompraFinal, CantidadAccionesCorto, GananciaCorto):
    GananciaCorto = (PrecioVentaInicial - PrecioRecompraFinal) * CantidadAccionesCorto
    
    return GananciaCorto

def menu_acciones(seleccion):
    seleccion = input(f"\n¿Deseas calcular el rendimiento de una inversión en acciones (s ó n)? ")
    
    if seleccion == 's' or seleccion == 'S':
        acciones(PrecioVenta, PrecioCompra, CantidadAccionesLargo, DividendosAccion, GananciaLargo, PrecioVentaInicial, PrecioRecompraFinal, CantidadAccionesCorto, GananciaCorto)
    else:
        menu_Ejercicios(ejercicio)
        
def acciones(PrecioVenta, PrecioCompra, CantidadAccionesLargo, DividendosAccion, GananciaLargo, PrecioVentaInicial, PrecioRecompraFinal, CantidadAccionesCorto, GananciaCorto):
    os.system("cls")
    
    print(f"¿Que posición te gustaria evaluar?\n\n1.    Posición corta.\n2.    Posición larga.\n")
    opcion = int(input(f"Introduzca su elección:    "))
    
    if opcion == 1:
        
        seleccion = input("\nPara el calculo del rendimiento de una acción, ¿deseas usar los valores establecidos (s ó n)?   ")
        
        if seleccion == 'n' or seleccion == 'N':
            PrecioVentaInicial = float(input(f"\n1.    Indique el precio de venta inicial:  "))
            PrecioRecompraFinal = float(input(f"2.    Indique el precio de recompra:  "))
            CantidadAccionesCorto = int(input(f"3.    Indique la cantidad de acciones:    "))
            
        GananciaCorto = Corto(PrecioVentaInicial, PrecioRecompraFinal, CantidadAccionesCorto, GananciaCorto)
        
        print(f"\nGanancia a corto plazo: ", GananciaCorto)
        
    elif opcion == 2:
        
        seleccion = input("\nPara el calculo del rendimiento de una acción, ¿deseas usar los valores establecidos (s ó n)?   ")
        
        if seleccion == 'n' or seleccion == 'N':
            PrecioVenta = float(input(f"\n1.    Indique el precio de venta:  "))
            PrecioCompra = float(input(f"2.    Indique el precio de compra:  "))
            CantidadAccionesLargo = int(input(f"3.    Indique la cantidad de acciones:    "))
            DividendosAccion = float(input(f"4.    Indique el valor del dividendo persibido:    "))
            
        GananciaLargo = Largo(PrecioVenta, PrecioCompra, CantidadAccionesLargo, DividendosAccion, GananciaLargo)
        
        print(f"\nGanancia a largo plazo: ",GananciaLargo)    
    
    menu_acciones(seleccion)

def menu_Ejercicios(ejercicio):
    os.system("cls")
    
    print("Menú:\n\n1.    Calculo de rendimiento de los bonos.\n2.    Calculo del rendimiento en  la inversión de acciones.\n3.    Salir del programa.\n")
    ejercicio = int(input("Introduzca su elección:  "))
    
    if ejercicio == 1:
        bonos(InversionInicial, Tasa, Plazo, ValorNominalCETE, PrecioCETE, NumeroCETE, MontoTotalVencimiento, seleccion, GananciaTotal)
        
    elif ejercicio == 2:
        acciones(PrecioVenta, PrecioCompra, CantidadAccionesLargo, DividendosAccion, GananciaLargo, PrecioVentaInicial, PrecioRecompraFinal, CantidadAccionesCorto, GananciaCorto)
        
    else:
        quit()

### Función principal
def main():
    os.system("cls")
    
    menu_Ejercicios(ejercicio)

if __name__ == '__main__':
    sys.exit(main())