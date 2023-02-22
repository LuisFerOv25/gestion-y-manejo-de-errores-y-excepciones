from flask import Flask,abort
from flask import render_template
from flask import request,session
from auth import autenticar
from inicio import home
from datetime import date
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
from werkzeug.exceptions import HTTPException
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

app = Flask(__name__)
app.secret_key = '97110c78ae51a45af397be6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'

    


sentry_sdk.init(
    dsn="https://47b422c23c014fec8d53ccc9dc0e3e61@o4504709798952960.ingest.sentry.io/4504709801443328",
    integrations=[
        FlaskIntegration(),
    ],
    traces_sample_rate=1.0
)
@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0
    
@app.route('/generate-error')
def generate_error():
    # Intenta acceder a una variable que no existe
    variable_inexistente = variable_inexistente + 1
    return 'Este error es generado a propósito'    

app.register_blueprint(home)
app.register_blueprint(autenticar)

def registrer_error_handlers(app):
    @app.errorhandler(500)
    def internal_error(e):
        if isinstance(e, HTTPException):
            return render_template('500.html',e=e), 500
        return e

    @app.errorhandler(404)
    def page_not_found(e):
        if isinstance(e, HTTPException):
            return render_template('404.html',e=e), 404
        return e
    
    @app.errorhandler(400)
    def error_400_handler(e):
        if isinstance(e, HTTPException):
            return render_template('400.html',e=e), 400
        return e

    @app.errorhandler(401)
    def error_401_handler(e):
        if isinstance(e, HTTPException):
            return render_template('401.html',e=e), 401
        return e
    
@app.route('/500')
def error500():
    abort(500)
    
@app.route('/401')
def error401():
    abort(401)
    
@app.route('/400')
def error400():
    abort(400)
    


if __name__ == '__main__':
    registrer_error_handlers(app)
    app.run(debug=True, port=5000)
