class personas :
    def __init__(self, nombre, apellidoPAt, apellidoMat, edad, carrera ) :
        self.nombre = nombre
        self.apellidoPAt = apellidoPAt
        self.apellidoMat = apellidoMat
        self.edad = edad
        self.carrera = carrera
    
    def __init__(self, nombre, apellidoPAt, edad, carrera ) :
        self.nombre = nombre
        self.apellidoPAt = apellidoPAt
        self.edad = edad
        self.carrera = carrera
        
octavio = personas("Octavio","", 20,"LTIN")
octavio.nombre = "Octavio"
print(f"El nombre es {octavio.nombre}")
octavio.apellidoPAt = "López"
print(f"El apellido es {octavio.apellidoPAt}")

#Yesenia = personas()
#Yesenia.nombre = "Yesenia"
#print(f"El nombre es {Yesenia.nombre}")