from .productos_dao import listar_unidades
from .coneciondb import Conneccion

# Clase que representa una unidad de medida
class Unidad:
    def __init__(self, nombre, abreviatura):
        self.nombre = nombre
        self.abreviatura = abreviatura

    def __str__(self):
        return f'Unidad[{self.nombre} - {self.abreviatura}]'

def guardar_unidad(unidad):
    conn = Conneccion()
    sql = f"INSERT INTO UnidadesMedida (Nombre, Abreviatura) VALUES ('{unidad.nombre}', '{unidad.abreviatura}');"
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print("Error al guardar unidad:", e)

def editar_unidad(unidad, id_unidad):
    conn = Conneccion()
    sql = f"UPDATE UnidadesMedida SET Nombre = '{unidad.nombre}', Abreviatura = '{unidad.abreviatura}' WHERE ID = {id_unidad};"
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print("Error al editar unidad:", e)

def borrar_unidad(id_unidad):
    conn = Conneccion()
    sql = f"DELETE FROM UnidadesMedida WHERE ID = {id_unidad};"
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print("Error al borrar unidad:", e)


class UnidadManager:
    def __init__(self):
        self.unidades = []
        self.cargar_unidades()
    
    #def cargar_unidades(self):
    #    x = listar_unidades()
    #    self.unidades = [{'id': 0, 'Nombre': 'Seleccione Uno'}]
    #    for uni in x:
    #        self.unidades.append({'id': uni[0], 'Nombre': uni[1], 'Abreviatura':[2]})

    def cargar_unidades(self):
        x = listar_unidades()
        self.unidades = [{'id': 0, 'Nombre': 'Seleccione Uno', 'Abreviatura': ''}]
        for uni in x:
            self.unidades.append({
                'id': uni[0],
                'Nombre': uni[1],        # columna nombre
                'Abreviatura': uni[2]    # columna abreviatura
            })

    def get_nombres(self):
        return [uni['Nombre'] for uni in self.unidades]
    
    def get_id_por_indice(self, index):
        if 0 <= index < len(self.unidades):
            return self.unidades[index]['id']
        return None
    
    def get_id_por_nombre(self, nombre):
        for uni in self.unidades:
            if uni['Nombre'] == nombre:
                return uni['id']
        return None
    
    def get_indice_por_nombre(self, nombre):
        for i, uni in enumerate(self.unidades):
            if uni['Nombre'] == nombre:
                return i
        return 0


    def get_abreviaturas(self):
        return [uni['Abreviatura'] for uni in self.unidades]

    def get_id_por_abreviatura(self, abreviatura):
        for uni in self.unidades:
            if uni['Abreviatura'] == abreviatura:
                return uni['id']
        return None

    def get_indice_por_abreviatura(self, abreviatura):
        for i, uni in enumerate(self.unidades):
            if uni['Abreviatura'] == abreviatura:
                return i
        return 0
