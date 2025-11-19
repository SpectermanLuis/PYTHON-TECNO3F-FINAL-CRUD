####################  #####################################
# productos_dao.py #  #  Operaciones ABM tabla productos  #
####################  #####################################


from .coneciondb import Conneccion

# Crear tablas
def crear_tabla():
    conn = Conneccion()
    sql = '''
        CREATE TABLE IF NOT EXISTS Categorias(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Descripcion TEXT
        );

        CREATE TABLE IF NOT EXISTS Proveedores(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Contacto TEXT
        );

        CREATE TABLE IF NOT EXISTS UnidadesMedida(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Abreviatura TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS Productos(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Stock INTEGER NOT NULL,
            Categoria INTEGER,
            Proveedor INTEGER,
            Unidad INTEGER,
            FOREIGN KEY (Categoria) REFERENCES Categorias(ID),
            FOREIGN KEY (Proveedor) REFERENCES Proveedores(ID),
            FOREIGN KEY (Unidad) REFERENCES UnidadesMedida(ID)
        );
    '''
    try:
        conn.cursor.executescript(sql)

       # --- Carga inicial de algunos datos en tablas maestras ---
        # Categorías
        conn.cursor.execute("SELECT COUNT(*) FROM Categorias;")
        if conn.cursor.fetchone()[0] == 0:
            conn.cursor.executemany(
                "INSERT INTO Categorias (Nombre, Descripcion) VALUES (?, ?);",
                [
                    ("Electrónica", "Dispositivos electrónicos"),
                    ("Papelería", "Artículos de oficina"),
                    ("Alimentos", "Productos comestibles")
                ]
            )

        # Proveedores
        conn.cursor.execute("SELECT COUNT(*) FROM Proveedores;")
        if conn.cursor.fetchone()[0] == 0:
            conn.cursor.executemany(
                "INSERT INTO Proveedores (Nombre, Contacto) VALUES (?, ?);",
                [
                    ("Proveedor A", "contactoA@mail.com"),
                    ("Proveedor B", "contactoB@mail.com")
                ]
            )

        # Unidades de medida
        conn.cursor.execute("SELECT COUNT(*) FROM UnidadesMedida;")
        if conn.cursor.fetchone()[0] == 0:
            conn.cursor.executemany(
                "INSERT INTO UnidadesMedida (Nombre, Abreviatura) VALUES (?, ?);",
                [
                    ("Unidad", "Uni"),
                    ("Kilogramo", "Kg"),
                    ("Litro", "Lt")
                ]
            )

        conn.cerrar_con()
    except Exception as e:
        print("Error al crear tablas:", e)



class Producto:
    def __init__(self, nombre, stock, categoria, proveedor, unidad):
        self.nombre = nombre
        self.stock = stock
        self.categoria = categoria
        self.proveedor = proveedor
        self.unidad = unidad

    def __str__(self):
        return f'Producto[{self.nombre}, {self.stock}, {self.categoria}, {self.proveedor}, {self.unidad}]'


def guardar_producto(producto):
    conn = Conneccion()
    sql = f'''
        INSERT INTO Productos(Nombre, Stock, Categoria, Proveedor, Unidad)
        VALUES('{producto.nombre}', {producto.stock},
               {producto.categoria}, {producto.proveedor}, {producto.unidad});
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print("Error al guardar producto:", e)


def listar_productos():
    conn = Conneccion()
    sql = '''
        SELECT p.ID, p.Nombre, p.Stock,
               c.Nombre, pr.Nombre, u.Abreviatura
        FROM Productos AS p
        INNER JOIN Categorias AS c ON p.Categoria = c.ID
        INNER JOIN Proveedores AS pr ON p.Proveedor = pr.ID
        INNER JOIN UnidadesMedida AS u ON p.Unidad = u.ID;
    '''
    try:
        conn.cursor.execute(sql)
        productos = conn.cursor.fetchall()
        conn.cerrar_con()
        return productos
    except Exception as e:
        print("Error al listar productos:", e)
        return []


def editar_producto(producto, id):
    conn = Conneccion()
    sql = f'''
        UPDATE Productos
        SET Nombre = '{producto.nombre}',
            Stock = {producto.stock},
            Categoria = {producto.categoria},
            Proveedor = {producto.proveedor},
            Unidad = {producto.unidad}
        WHERE ID = {id};
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print("Error al editar producto:", e)


def borrar_producto(id):
    conn = Conneccion()
    sql = f'''
        DELETE FROM Productos
        WHERE ID = {id};
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print("Error al borrar producto:", e)



def listar_categorias():
    conn = Conneccion()
    sql = "SELECT ID, Nombre FROM Categorias;"
    conn.cursor.execute(sql)
    datos = conn.cursor.fetchall()
    conn.cerrar_con()
    return datos

def listar_proveedores():
    conn = Conneccion()
    sql = "SELECT ID, Nombre FROM Proveedores;"
    conn.cursor.execute(sql)
    datos = conn.cursor.fetchall()
    conn.cerrar_con()
    return datos

def listar_unidades():
    conn = Conneccion()
    sql = "SELECT ID, Nombre,Abreviatura FROM UnidadesMedida;"
    conn.cursor.execute(sql)
    datos = conn.cursor.fetchall()
    conn.cerrar_con()
    return datos
