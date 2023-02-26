from flask import Flask,abort
from flask import render_template
from auth import autenticar
from inicio import home

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

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404
error_codes = [
    400, 401, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
    416, 417, 418, 422, 428, 429, 431, 451, 500, 501, 502, 503, 504, 505
]
for code in error_codes:
    @app.errorhandler(code)
    def client_error(error):
        return render_template('error.html', error=error), error.code


    


@app.route('/400')
def error400():
    abort(400)
    
@app.route('/401')
def error401():
    abort(401)
 
@app.route('/403')
def error403():
    abort(403)  
    
@app.route('/428')
def error428():
    abort(428)  
                
@app.route('/500')
def error500():
    abort(500)
    

if __name__ == '__main__':
  
    app.run(debug=True, port=5100)
