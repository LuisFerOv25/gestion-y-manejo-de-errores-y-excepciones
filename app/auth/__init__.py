from flask import Blueprint

autenticar = Blueprint('autenticar', __name__, template_folder="templates", static_folder='static')
from . import auth
