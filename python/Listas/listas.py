#Conjunto de variables almacenadas en un identificdor cuyos elementos estan enlazados por un apuntador
# aylis = {"apple", "banana"}
suma = 0
j = 1
numero = 100101010
numero = 5

listaNumeros = [10001,2020,323,3212,33]

print(9)
print(1)

calificacionesTallerPython = []
contador  = 0

while contador < 14 : 
    calificaciones = float(input(".    Ingresa la primera calificación: "))
    calificacionesTallerPython.append(calificaciones)
    contador+=1

print(calificacionesTallerPython)

for calificacion in calificacionesTallerPython :
    
    suma = suma + calificacion
    
promedio = suma /len(calificacionesTallerPython)
print(promedio)