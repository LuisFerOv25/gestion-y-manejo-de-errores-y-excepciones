from flask import render_template,abort
from . import autenticar
from flask import Flask,request,url_for,redirect

from datetime import date
from datetime import datetime

from bd import *  #Importando conexion BD
from controller import *  #Importando mis Funciones

import re
from werkzeug.security import generate_password_hash, check_password_hash


# Rutas para login y recuperacion de cuenta
@autenticar.route('/login/')
def login():
    return render_template('login.html')

@autenticar.route('/registro/')
def registro():
    return render_template("registro.html")

@autenticar.route('/recuperar_correo/')
def recuperarc():
    return render_template("cuenta.html")

@autenticar.route('/verificar/')
def verificar():
    return render_template("cuenta2.html")

@autenticar.route('/validar/')
def validar():
    return render_template("cuenta3.html")




#Registrando una cuenta de Usuario
@autenticar.route('/registro-usuario', methods=['GET', 'POST'])
def registerUser():
    msg = ''
    conexion = obtener_conexion()
    if request.method == 'POST':
        tipo_user                   =2
        nombre                      = request.form['nombre']
        apellido                    = request.form['apellido']
        correo                       = request.form['correo']
        direccion                       = request.form['direccion']
        telefono                       = request.form['telefono']
        password                    = request.form['password']
        repite_password             = request.form['repite_password']
        genero                        = request.form['genero']
        create_at                   = date.today()
        #current_time = datetime.datetime.now()
        # Comprobando si ya existe la cuenta de Usuario con respecto al correo
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute('SELECT * FROM usuario WHERE correo = %s', (correo,))
        account = cursor.fetchone()
        cursor.close() #cerrrando conexion SQL
          
        if account:
            msg = 'Ya existe el Email!'
        elif password != repite_password:
            msg = 'Disculpa, las clave no coinciden!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', correo):
            msg = 'Disculpa, formato de Email incorrecto!'
        elif not nombre or not apellido or not correo or not direccion or not telefono or not genero or not password or not repite_password:
            abort(400)
            msg = 'El formulario no debe estar vacio!'
        else:
            # La cuenta no existe y los datos del formulario son v??lidos,
            password_encriptada = generate_password_hash(password, method='sha256')
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute('INSERT INTO usuario (tipo_user, nombre, apellido, correo,direccion,telefono, password,genero, create_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (tipo_user, nombre, apellido, correo,direccion,telefono, password_encriptada, genero, create_at))
            conexion.commit()
            cursor.close()
            msg = 'Cuenta creada correctamente!'

        return render_template('login.html', msjAlert = msg, typeAlert=1)
    return render_template('login.html', dataLogin = dataLoginSesion(), msjAlert = msg, typeAlert=0)

    
# Cerrar session del usuario
@autenticar.route('/logout')
def logout():
    msgClose = ''
    # Eliminar datos de sesi??n, esto cerrar?? la sesi??n del usuario
    session.pop('conectado', None)
    session.pop('id', None)
    session.pop('correo', None)
    msgClose ="La sesi??n fue cerrada correctamente"
    return render_template('./login.html', msjAlert = msgClose, typeAlert=1)



@autenticar.route('/dashboard', methods=['GET', 'POST'])
def loginUsser():
    conexion = obtener_conexion()
    if 'conectado' in session:
        return render_template('./home.html', dataLogin = dataLoginSesion())
        
    else:
        msg = ''
        if request.method == 'POST' and 'correo' in request.form and 'password' in request.form:
            correo      = str(request.form['correo'])
            password   = str(request.form['password'])
            auth = request.authorization
                  
                
            # Comprobando si existe una cuenta
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuario WHERE correo = %s", [correo])
            account = cursor.fetchone()

            if account:
                if check_password_hash(account['password'],password):
                    # Crear datos de sesi??n, para poder acceder a estos datos en otras rutas 
                    session['conectado']        = True
                    session['id']               = account['id']
                    session['tipo_user']        = account['tipo_user']
                    session['nombre']           = account['nombre']
                    session['apellido']         = account['apellido']
                    session['correo']           = account['correo']
                    session['direccion']        = account['direccion']
                    session['telefono']         = account['telefono']
                    session['genero']           = account['genero']
                    session['create_at']        = account['create_at']

                    msg = "Ha iniciado sesi??n correctamente."
                    render_template('./home.html', msjAlert = msg, typeAlert=1, dataLogin = dataLoginSesion()) 

                else:
                    msg = 'Datos incorrectos, por favor verfique!'
                    return render_template('login.html', msjAlert = msg, typeAlert=0)
            else:
                return abort(401),render_template('login.html', msjAlert = msg, typeAlert=0)
            
    return render_template('login.html', msjAlert = 'Debe iniciar sesi??n.', typeAlert=0)

