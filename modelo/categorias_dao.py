#####################  #####################################
# categorias_dao.py #  #  Operaciones ABM tabla categorias #
#####################  #####################################

from .coneciondb import Conneccion

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f'Categoria[{self.nombre}]'


# Funciones CRUD
def listar_categorias():
    conn = Conneccion()
    sql = "SELECT ID, Nombre FROM Categorias;"
    try:
        conn.cursor.execute(sql)
        categorias = conn.cursor.fetchall()
        conn.cerrar_con()
        return categorias
    except Exception as e:
        print("Error al listar categorías:", e)
        return []

def guardar_categoria(categoria):
    conn = Conneccion()
    sql = f"INSERT INTO Categorias (Nombre) VALUES ('{categoria.nombre}');"
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print("Error al guardar categoría:", e)

def editar_categoria(categoria, id_categoria):
    conn = Conneccion()
    sql = f"UPDATE Categorias SET Nombre = '{categoria.nombre}' WHERE ID = {id_categoria};"
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print("Error al editar categoría:", e)

def borrar_categoria(id_categoria):
    conn = Conneccion()
    sql = f"DELETE FROM Categorias WHERE ID = {id_categoria};"
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print("Error al borrar categoría:", e)


# Manager para combos y listas
class CategoriaManager:
    def __init__(self):
        self.categorias = []
        self.cargar_categorias()

    def cargar_categorias(self):
        x = listar_categorias()
        self.categorias = [{'id': 0, 'Nombre': 'Seleccione Uno'}]
        for cat in x:
            self.categorias.append({'id': cat[0], 'Nombre': cat[1]})

    def get_nombres(self):
        return [cat['Nombre'] for cat in self.categorias]

    def get_id_por_indice(self, index):
        if 0 <= index < len(self.categorias):
            return self.categorias[index]['id']
        return None

    def get_id_por_nombre(self, nombre):
        for cat in self.categorias:
            if cat['Nombre'] == nombre:
                return cat['id']
        return None

    def get_indice_por_nombre(self, nombre):
        for i, cat in enumerate(self.categorias):
            if cat['Nombre'] == nombre:
                return i
        return 0
