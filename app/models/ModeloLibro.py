from .entities.Autor import Autor
from .entities.Libro import Libro


class ModeloLibro:

    def __init__(self):
        pass

    @classmethod
    def listar_libros(self, db):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT L.isbn, L.titulo, L.anoedicion, L.precio, A.apellidos, A.nombres
                     FROM libro AS L
                     JOIN autor AS A
                     ON L.autor_id = A.id
                     ORDER BY l.titulo ASC;
                    """
            cursor.execute(sql)
            data = cursor.fetchall()
            libros = []
            for row in data:
                aut = Autor(0, row[4], row[5])
                libro = Libro(row[0], row[1], aut, row[2], row[3])
                libros.append(libro)
            return libros
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def listar_libros_vendidos(self, db):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT C.isbn, L.titulo, L.precio, COUNT(C.isbn) AS unidades_vendidas
                     FROM compra AS C
                     JOIN libro AS L
                     ON C.isbn = L.isbn
                     GROUP BY C.isbn
                     ORDER BY unidades_vendidas DESC, L.titulo ASC;
                    """
            cursor.execute(sql)
            data = cursor.fetchall()
            libros = []
            for row in data:
                libro = Libro(row[0], row[1], None, None, row[2])
                libro.unidades_vendidas = int(row[3])
                libros.append(libro)
            return libros
        except Exception as ex:
            raise Exception(ex)
