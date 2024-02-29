import os

def borrarpantalla() :
    if os.name == "posix" : 
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")