import mysql.connector
from mysql.connector import Error
import usuarioModelo

def consultarDatosUsuarios():
    try:
        connection = mysql.connector.connect(host='148.202.39.38',
                                            database='bolicesupreme',
                                            user='test',
                                            password='test')
        if connection.is_connected():
            
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM usuario")
            record = cursor.fetchall()
            
            return record
        
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def ConsultarDatosUsuarios(id) :

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='bolice',
                                            user='root',
                                            password='')
        
        if connection.is_connected():
            
            n_id = id
            
            db_Info = connection.get_server_info()
            # print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM usuario WHERE id_usuario = {n_id}")
            record = cursor.fetchall()
            
            return record
            
            # print("You're connected to database: ")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            #   print("MySQL connection is closed")
            
        
# Rubber 

def EliminarDatosUsuarios(id) :

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='bolice',
                                            user='root',
                                            password='')
        
        if connection.is_connected():
            
            n_id = id
            
            db_Info = connection.get_server_info()
            # print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM usuario WHERE id_usuario = {n_id}")
            record = cursor.fetchall()
            print(f"Se a eliminado {cursor.rowcount}")
            connection.commit()
            
            # print("You're connected to database: ")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            #   print("MySQL connection is closed")

def AgrgarDatosUsuarios(id) :

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='bolice',
                                            user='root',
                                            password='')
        
        if connection.is_connected():
            
            db_Info = connection.get_server_info()
            # print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO usuario () values ()")
            record = cursor.fetchall()
            print(f"Se ingresado {cursor.rowcount}")
            connection.commit()
            
            # print("You're connected to database: ")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # 
        