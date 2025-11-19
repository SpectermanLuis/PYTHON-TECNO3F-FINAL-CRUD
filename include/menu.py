############  ###################################
#  menu.py #  #  menu de opciones del sistema   #
############  ###################################

import tkinter as tk
from tkinter import ttk, messagebox
from modelo.productos_dao    import crear_tabla
from vista.productos_frame   import FrameProductos
from vista.proveedores_frame import FrameProveedores
from vista.unidades_frame    import FrameUnidades
from vista.categorias_frame  import FrameCategorias

from vista.consultas_frame import (
    ConsultaPorCategoria,
    ConsultaPorProveedor,
    ConsultaStockBajo
)

def barrita_menu(root):
    barra = tk.Menu(root)
    root.config(menu=barra)

    # Menús principales
    m_inicio = tk.Menu(barra, tearoff=0)
    m_maestras = tk.Menu(barra, tearoff=0)
    m_productos = tk.Menu(barra, tearoff=0)
    m_consultas = tk.Menu(barra, tearoff=0)
    m_otros = tk.Menu(barra, tearoff=0)

    barra.add_cascade(label="Salir", menu=m_inicio)
    barra.add_cascade(label="Tablas Maestras", menu=m_maestras)
    barra.add_cascade(label="Productos", menu=m_productos)
    barra.add_cascade(label="Consultas", menu=m_consultas)
    barra.add_cascade(label="Otros", menu=m_otros)

    # Inicio
    # m_inicio.add_command(label="Conectar DB", command=crear_tabla)
    m_inicio.add_command(label="Salir", command=root.destroy)

    # Tablas Maestras 
    m_maestras.add_command(label="ABM Categorías" , command=lambda: FrameCategorias(root))
    m_maestras.add_command(label="ABM Proveedores", command=lambda: FrameProveedores(root) ) 
    m_maestras.add_command(label="ABM Unidades de Medida", command=lambda: FrameUnidades(root))

    # Productos
    m_productos.add_command(label="ABM Productos", command=lambda: FrameProductos(root))

    # Consultas
    m_consultas.add_command(label="Por Categoría", command=lambda: ConsultaPorCategoria(root))
    m_consultas.add_command(label="Por Proveedor", command=lambda: ConsultaPorProveedor(root))
    m_consultas.add_command(label="Stock Bajo", command=lambda: ConsultaStockBajo(root))

    # Otros
    m_otros.add_command(label="Acerca de…", command=lambda: mostrar_acerca_de())
    m_otros.add_command(label="Ayuda")

def mostrar_acerca_de():
    messagebox.showinfo(
        "Acerca de",
        "Trabajo Práctico de Python\n"
        "Realizado por: Luis Omar Specterman\n"
        "Versión: 1.0\n"
        "PYTHON INTERMEDIO\n"
        "TECNO 3F\n"        
        "Año: 2025"
    )