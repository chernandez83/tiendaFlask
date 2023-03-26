from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from .models.ModeloLibro import ModeloLibro
from .models.ModeloUsuario import ModeloUsuario
from .models.ModeloCompra import ModeloCompra

from .models.entities.Usuario import Usuario
from .models.entities.Libro import Libro
from .models.entities.Compra import Compra

from .consts import *

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModeloUsuario.obtener_por_id(db, id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario(
            None, request.form['usuario'], request.form['password'], None)
        usuario_logueado = ModeloUsuario.login(db, usuario)
        if usuario_logueado is not None:
            login_user(usuario_logueado)
            flash(f'{usuario.usuario.upper()}, {MENSAJE_BIENVENIDA}')
            return redirect(url_for('index'))
        else:
            flash(LOGIN_INVALIDO, 'warning')
    return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT_EXITOSO, 'success')
    return redirect(url_for('login'))


@app.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        if current_user.tipousuario.id == 1:
            libros_vendidos = []
            data = {
                'titulo': 'Libros Vendidos',
                'libros_vendidos': libros_vendidos
            }
        else:
            compras = []
            data = {
                'titulo': 'Mis Compras',
                'compras': compras
            }
        return render_template('index.html', data=data)
    return redirect(url_for('login'))


@app.route('/libros')
@login_required
def libros():
    if current_user.tipousuario.id == 1:
        return redirect(url_for('index'))
    try:
        libros = ModeloLibro.listar_libros(db)
        data = {
            'titulo': 'Listado de Libros',
            'libros': libros
        }
        return render_template('listado_libros.html', data=data)
    except Exception as ex:
        #raise Exception(ex)
        return render_template('errores/error.html', mensaje=format(ex))


@app.route('/comprarLibro', methods=['POST'])
@login_required
def comprarLibro():
    data_request = request.get_json()
    # print(data_request)
    data = {}
    try:
        libro = Libro(data_request['isbn'], None, None, None, None)
        compra = Compra(None, libro, current_user)
        data['exito'] = ModeloCompra.registrar_compra(db, compra)
    except Exception as ex:
        data['mensaje'] = format(ex)
        data['exito'] = False
    return jsonify(data)


def error404(error):
    return render_template('errores/404.html')  # , 404


def pagina_no_autorizada(error):
    return redirect(url_for('login'))


def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(401, pagina_no_autorizada)
    app.register_error_handler(404, error404)
    return app
