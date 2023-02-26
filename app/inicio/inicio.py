from flask import render_template
from . import home


@home.route('/')
def index():
    return render_template("homePrevio.html")

# Medicamentos cliente
@home.route('/medicamentoscliente/')
def medicamentoscliente():
    return render_template("medicamentos.html")

# Cuidado personal
@home.route('/cuidadopersonalclient/')
def cuidadopersonalclient():
    return render_template("cuidadopersonalclient.html")

# Dermacosmeticos
@home.route('/dermacosmetica/')
def dermacosmetica():
    return render_template("dermacosmetica.html")

# Nutricionales
@home.route('/nutricionales/')
def nutricionales():
    return render_template("nutricionales.html")

# Bebe
@home.route('/bebe/')
def bebe():
    return render_template("bebe.html")

# Comprar producto
@home.route('/comprarproducto/')
def comprarproducto():
    return render_template("comprarproducto.html")

# Home User
@home.route('/homeuser/')
def homeuser():
    return render_template("home.html")

# Subir archivo
@home.route('/subir')
def subir():
    return render_template("archivo.html")