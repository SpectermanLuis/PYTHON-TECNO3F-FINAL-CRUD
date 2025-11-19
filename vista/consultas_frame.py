######################  #################################
# consultas_frame.py #  #  Operaciones Consultas Varias #
######################  #################################

import tkinter as tk
from tkinter import ttk,messagebox
import modelo.productos_dao as dao
import modelo.categorias_dao as categorias
import modelo.proveedores_dao as proveedores
import modelo.unidades_dao as unidades

# -------------------
# Consulta por Categoría
# -------------------
class ConsultaPorCategoria(tk.Toplevel):
    def __init__(self, root=None):
        super().__init__(root)
        self.title("Consulta: Productos por Categoría")
        self.geometry("800x420")

        self.cat_manager = categorias.CategoriaManager()
        tk.Label(self, text="Categoría:").pack(pady=5)
        self.combo = ttk.Combobox(self, state="readonly", values=self.cat_manager.get_nombres())
        self.combo.current(0)
        self.combo.pack(pady=5)

        tk.Button(self, text="Consultar", command=self.mostrar_tabla).pack(pady=5)

        self.tabla = ttk.Treeview(self, columns=("Nombre","Stock","Proveedor","Unidad"), show="headings")
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)
        for col in ("Nombre","Stock","Proveedor","Unidad"):
            self.tabla.heading(col, text=col)

    def mostrar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        categoria_id = self.cat_manager.get_id_por_indice(self.combo.current())

        # messagebox.showinfo("Debug", f"Valor en categoria_id: {categoria_id}")  

        if categoria_id == 0:
            messagebox.showwarning("Atención", "Debe seleccionar una categoría válida",parent=self)
        else:   
            productos = listar_productos_por_categoria(categoria_id)
            for p in productos:
                self.tabla.insert("", tk.END, values=(p[1], p[2], p[3], p[4]))

def listar_productos_por_categoria(categoria_id):
    conn = dao.Conneccion()
    sql = f'''
        SELECT p.ID, p.Nombre, p.Stock, pr.Nombre, u.Abreviatura
        FROM Productos AS p
        INNER JOIN Proveedores AS pr ON p.Proveedor = pr.ID
        INNER JOIN UnidadesMedida AS u ON p.Unidad = u.ID
        WHERE p.Categoria = {categoria_id};
    '''
    conn.cursor.execute(sql)
    datos = conn.cursor.fetchall()
    conn.cerrar_con()
    return datos

# -------------------
# Consulta por Proveedor
# -------------------
class ConsultaPorProveedor(tk.Toplevel):
    def __init__(self, root=None):
        super().__init__(root)
        self.title("Consulta: Productos por Proveedor")
        self.geometry("800x420")

        self.prov_manager = proveedores.ProveedorManager()
        tk.Label(self, text="Proveedor:").pack(pady=5)
        self.combo = ttk.Combobox(self, state="readonly", values=self.prov_manager.get_nombres())
        self.combo.current(0)
        self.combo.pack(pady=5)

        tk.Button(self, text="Consultar", command=self.mostrar_tabla).pack(pady=5)

        self.tabla = ttk.Treeview(self, columns=("Nombre","Stock","Categoría","Unidad"), show="headings")
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)
        for col in ("Nombre","Stock","Categoría","Unidad"):
            self.tabla.heading(col, text=col)

    def mostrar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        proveedor_id = self.prov_manager.get_id_por_indice(self.combo.current())
        
        if proveedor_id == 0:
            messagebox.showwarning("Atención", "Debe seleccionar un proveedor válido",parent=self)
        else:        
            productos = listar_productos_por_proveedor(proveedor_id)
            for p in productos:
                self.tabla.insert("", tk.END, values=(p[1], p[2], p[3], p[4]))

def listar_productos_por_proveedor(proveedor_id):
    conn = dao.Conneccion()
    sql = f'''
        SELECT p.ID, p.Nombre,p.Stock, c.Nombre, u.Abreviatura
        FROM Productos AS p
        INNER JOIN Categorias AS c ON p.Categoria = c.ID
        INNER JOIN UnidadesMedida AS u ON p.Unidad = u.ID
        WHERE p.Proveedor = {proveedor_id};
    '''
    conn.cursor.execute(sql)
    datos = conn.cursor.fetchall()
    conn.cerrar_con()
    return datos

# -------------------
# Consulta de Stock Bajo
# -------------------
class ConsultaStockBajo(tk.Toplevel):
    def __init__(self, root=None):
        super().__init__(root)
        self.title("Consulta: Productos con Stock Bajo")
        self.geometry("640x420")

        tk.Label(self, text="Stock menor a:").pack(pady=5)
        self.umbral = tk.StringVar()
        self.entry_umbral = tk.Entry(self, textvariable=self.umbral)
        self.entry_umbral.pack(pady=5)

        tk.Button(self, text="Consultar", command=self.mostrar_tabla).pack(pady=5)

        self.tabla = ttk.Treeview(self, columns=("Nombre","Stock","Categoría","Proveedor","Unidad"), show="headings")
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)
        for col in ("Nombre","Stock","Categoría","Proveedor","Unidad"):
            self.tabla.heading(col, text=col)

    def mostrar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        try:
            limite = int(self.umbral.get())
        except:
            limite = 0
        productos = listar_productos_stock_bajo(limite)
        for p in productos:
            self.tabla.insert("", tk.END, values=(p[1], p[2], p[3], p[4], p[5]))

def listar_productos_stock_bajo(limite):
    conn = dao.Conneccion()
    sql = f'''
        SELECT p.ID, p.Nombre, p.Stock, c.Nombre, pr.Nombre, u.Abreviatura
        FROM Productos AS p
        INNER JOIN Categorias AS c ON p.Categoria = c.ID
        INNER JOIN Proveedores AS pr ON p.Proveedor = pr.ID
        INNER JOIN UnidadesMedida AS u ON p.Unidad = u.ID
        WHERE p.Stock < {limite};
    '''
    conn.cursor.execute(sql)
    datos = conn.cursor.fetchall()
    conn.cerrar_con()
    return datos
