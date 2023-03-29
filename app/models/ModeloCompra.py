from .entities.Compra import Compra
from .entities.Libro import Libro

class ModeloCompra:
    
    def __init__(self):
        pass
    
    @classmethod
    def registrar_compra(self, db, compra):
        try:
            cursor = db.connection.cursor()
            sql = (f'INSERT INTO compra (uuid, isbn, usuario_id) '
                   f'VALUES (uuid(), {compra.libro.isbn}, {compra.usuario.id})')
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def listar_compras_usuario(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = (f'SELECT C.fecha, C.isbn, L.titulo, L.precio ' 
                   f'FROM compra AS C '
                   f'JOIN libro AS L '
                   f'ON C.isbn = L.isbn '
                   f'WHERE C.usuario_id = {usuario.id}')
            cursor.execute(sql)
            data = cursor.fetchall()
            compras = []
            for row in data:
                libro = Libro(row[1], row[2], None, None, row[3])
                compra = Compra(None, libro, usuario, row[0])
                compras.append(compra)
            return compras
        except Exception as ex:
            raise Exception(ex)