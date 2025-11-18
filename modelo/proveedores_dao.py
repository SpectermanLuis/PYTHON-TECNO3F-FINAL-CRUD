from .productos_dao import listar_proveedores
from .coneciondb import Conneccion

# Clase que representa un proveedor
class Proveedor:
    def __init__(self, nombre, contacto):
        self.nombre = nombre
        self.contacto = contacto

    def __str__(self):
        return f'Proveedor[{self.nombre} - {self.contacto}]'


# Funciones CRUD
def listar_proveedores():
    conn = Conneccion()
    sql = "SELECT ID, Nombre, Contacto FROM Proveedores;"
    try:
        conn.cursor.execute(sql)
        proveedores = conn.cursor.fetchall()
        conn.cerrar_con()
        return proveedores
    except Exception as e:
        print("Error al listar proveedores:", e)
        return []

def guardar_proveedor(proveedor):
    conn = Conneccion()
    sql = f"INSERT INTO Proveedores (Nombre, Contacto) VALUES ('{proveedor.nombre}', '{proveedor.contacto}');"
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print("Error al guardar proveedor:", e)

def editar_proveedor(proveedor, id_proveedor):
    conn = Conneccion()
    sql = f"UPDATE Proveedores SET Nombre = '{proveedor.nombre}', Contacto = '{proveedor.contacto}' WHERE ID = {id_proveedor};"
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print("Error al editar proveedor:", e)

def borrar_proveedor(id_proveedor):
    conn = Conneccion()
    sql = f"DELETE FROM Proveedores WHERE ID = {id_proveedor};"
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print("Error al borrar proveedor:", e)


class ProveedorManager:
    def __init__(self):
        self.proveedores = []
        self.cargar_proveedores()
    
    def cargar_proveedores(self):
        x = listar_proveedores()
        self.proveedores = [{'id': 0, 'Nombre': 'Seleccione Uno'}]
        for prov in x:
            self.proveedores.append({'id': prov[0], 'Nombre': prov[1]})
    
    def get_nombres(self):
        return [prov['Nombre'] for prov in self.proveedores]
    
    def get_id_por_indice(self, index):
        if 0 <= index < len(self.proveedores):
            return self.proveedores[index]['id']
        return None
    
    def get_id_por_nombre(self, nombre):
        for prov in self.proveedores:
            if prov['Nombre'] == nombre:
                return prov['id']
        return None
    
    def get_indice_por_nombre(self, nombre):
        for i, prov in enumerate(self.proveedores):
            if prov['Nombre'] == nombre:
                return i
        return 0
