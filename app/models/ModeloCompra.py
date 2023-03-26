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