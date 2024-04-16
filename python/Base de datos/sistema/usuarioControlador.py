import mysql.connector
from mysql.connector import Error

import usuarioModelo

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='bolice',
                                         user='root',
                                         password='')
    
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM usuario")
        record = cursor.fetchall()
        
        modeloUsuario = usuarioModelo.usuario
        
        for row in record :
            modeloUsuario['nombre'] = '@' + row[1]
            print(modeloUsuario['nombre'])
        
        print("You're connected to database: ")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")