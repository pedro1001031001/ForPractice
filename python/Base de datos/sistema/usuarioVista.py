import usuarioControlador
import usuarioModelo

id : int = input("1.  Ingresa el usuario a buscar: ")
11
modeloUsuario = usuarioModelo.usuario
datos = usuarioControlador.ConsultarDatosUsuarios(id)

for row in datos :
    modeloUsuario['nombre'] = '@' + row[1]
    modeloUsuario['apellido_pat'] = row[2]
    modeloUsuario['apellido_mat'] = row[3]
    print(modeloUsuario['nombre'] + "   Apellidos:  " + modeloUsuario['apellido_pat'] + " " + modeloUsuario['apellido_mat'])
    

opcion = input("2.  ¿Quieres eliminar el usuario (SI)?")

if (opcion == "SI"):
    usuarioControlador.EliminarDatosUsuarios(id)
else :
    breakpoint
    
opicion = input("3. ¿Quieres agregar un usuario (SI)?")

if (opcion == "SI"):
    nombre = input("a.  Introdice el nombre del usuario:    ")
    apellido_pat = input("b.  Introdice el apellido paterno del usuario:    ")
    apellido_mat = input("c.  Introdice el apellido materno del usuario:    ")
    contrase_a = input("d.  Introdice el contraseña del usuario:    ")
    correo = input("e.  Introdice el correo del usuario:    ")
    telefono = input("f.  Introdice el teléfono del usuario:    ")
    usuarioControlador.AgrgarDatosUsuarios(nombre, apellido_pat, apellido_mat,)
else :
    breakpoint
