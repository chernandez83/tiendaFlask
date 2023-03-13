#from flask_script import Manager
from flask.cli import FlaskGroup
from app import inicializar_app
from config import config

#app = inicializar_app()

#manager = Manager(app)

# if __name__ == '__main__':
#    manager.run()

configuracion = config['development']

app = inicializar_app(configuracion)

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()