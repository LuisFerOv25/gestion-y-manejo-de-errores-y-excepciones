
import mysql.connector

def obtener_conexion():
    mydb = mysql.connector.connect(
        host ="localhost",
        user ="root",
        password ="",
        db = "db_farmaclick"
        )
    return mydb
