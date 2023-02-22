
from bd import *
from flask import session


def insertar_usuario(tipo_user,nombre, apellido, direccion,correo,telefono,genero):
    conexion = obtener_conexion()
    
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario(tipo_user,nombre, apellido,correo,direccion,telefono,genero) VALUES (%s, %s, %s,%s, %s, %s, %s)",
                       (tipo_user,nombre, apellido,correo,direccion,telefono,genero))
    conexion.commit()
    conexion.close()

def usuario_admin():
    conexion = obtener_conexion()
    usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM usuario where tipo_user = 1")
        usuarios = cursor.fetchall()
    conexion.close()
    return usuarios


def eliminar_usuario(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuario WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()    
    




def obtener_usuario_por_id(id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id,nombre,apellido,correo, direccion,telefono,genero FROM usuario WHERE id = %s", (id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego

def actualizar_producto(nombre, descripcion,cantidad, precio,fecha_vencimiento,id_producto ):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET nombre = %s, descripcion = %s,cantidad = %s, precio = %s,fecha_vencimiento = %s WHERE id_producto = %s",
                       (nombre,descripcion,cantidad,precio,fecha_vencimiento,id_producto ))
    conexion.commit()
    conexion.close()
    
#FUNCIONES PARA CREDENCIALES DE ACCESO

def dataLoginSesion():
    inforLogin = {
        "id"                  :session['id'],
        "tipoLogin"           :session['tipo_user'],
        "nombre"              :session['nombre'],
        "apellido"            :session['apellido'],
        "emailLogin"          :session['correo'],
        "direccion"           :session['direccion'],
        "telefono"            :session['telefono'],
        "genero"              :session['genero'],
        "create_at"           :session['create_at']
    }
    return inforLogin

