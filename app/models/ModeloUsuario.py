from .entities.Usuario import Usuario
from .entities.TipoUsuario import TipoUsuario


class ModeloUsuario:

    def __init__(self):
        pass

    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = f'SELECT * FROM usuario WHERE usuario = "{usuario.usuario}"'
            cursor.execute(sql)
            data = cursor.fetchone()
            # print(data)
            if data is not None and Usuario.verificar_password(data[2], usuario.password):
                return Usuario(data[0], data[1], None, data[3])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def obtener_por_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = (f'SELECT U.id, U.usuario, T.id, T.nombre '
                   f'FROM usuario AS U '
                   f'JOIN tipousuario AS T '
                   f'ON U.tipousuario_id = T.id '
                   f'WHERE U.id = {id}')
            cursor.execute(sql)
            data = cursor.fetchone()
            tipo_usuario = TipoUsuario(data[2], data[3])
            usuario_logueado = Usuario(data[0], data[1], None, tipo_usuario)
            return usuario_logueado
        except Exception as ex:
            raise Exception(ex)
