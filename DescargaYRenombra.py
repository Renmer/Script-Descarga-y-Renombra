import os
import pyodbc
import webbrowser
import time

#----Datos de la conexion a la base de datos SQLSERVER------
server = 'nombre del servidor'
database = 'nombre de la base de datos'
#conexion para la base de datos que corre en local
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')

#----Ejecucion de la consulta y generacion de documentos--------------
cursor = cnxn.cursor()
query = "introduce aqui la query"
cursor.execute(query)

row = cursor.fetchone()

while row:
    print("{:<40} {:<20} {:<50} {:<20}".format(row[0],row[4],row[6],row[3]))
    webbrowser.open("ingresa la ruta web de donde se descargara el archivo")
    time.sleep(1.2)
    archivo = 'ruta y nombre del archivo descargado'
    nombre_nuevo = "ruta y nombre nuevo del archivo nuevo"
    row = cursor.fetchone()
    try:
        time.sleep(0.3)
        os.rename(archivo,nombre_nuevo)
    except FileExistsError:
        time.sleep(0.3)
        os.remove(archivo)
webbrowser.open("http://localhost/Mensaje/alert.html")#se ejecuta cuando termine el proceso