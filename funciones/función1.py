nombre : str = "Raul" #Contexto global: Todo es lo que se ejecuta

def saludo(): # Contexto logal 
    print(nombre)
    print("Buenos días")

saludo() 
saludo()
nombre = "Xotchil"
saludo()
