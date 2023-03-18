from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

from .models.ModeloLibro import ModeloLibro

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    print(request.method)
    print(request.form['usuario'])
    for key, value in request.form.items():
        print(f'{key}: {value}')
    """
    if request.method == 'POST':
        #for key, value in request.form.items():
        #    print(f'{key}: {value}')
        if request.form.get('usuario') == 'admin' and request.form.get('password') == '123456':
            return redirect(url_for('index'))
    return render_template('auth/login.html')

@app.route('/libros')
def libros():
    try:
        libros = ModeloLibro.listar_libros(db)
        data = {
            'libros': libros
        }
        return render_template('listado_libros.html', data=data)
    except Exception as ex:
        raise Exception(ex)

def error404(error):
    return render_template('errores/404.html'), 404


def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, error404)
    return app
