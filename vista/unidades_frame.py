#####################  #########################################
# unidades_frame.py #  # Operaciones Frame Unidades de Medida  #
#####################  #########################################

import tkinter as tk
from tkinter import ttk, messagebox

from modelo import unidades_dao as unidades

class FrameUnidades(tk.Toplevel):
    def __init__(self, root=None):
        super().__init__(root)
        self.title("ABM Unidades de Medida")
        self.geometry("900x450")
        self.fondo = "#FBFCDD"
        self.config(bg=self.fondo)

        self.id_unidad = None

        
        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()

    def label_form(self):
        tk.Label(
            self, text="Nombre:", font=('Arial', 12, 'bold'),
            bg=self.fondo, fg="#1931E8"
        ).grid(row=0, column=0, padx=10, pady=10)

        tk.Label(
            self, text="Abreviatura:", font=('Arial', 12, 'bold'),
            bg=self.fondo, fg="#1931E8"
        ).grid(row=1, column=0, padx=10, pady=10)

    def input_form(self):
        self.nombre = tk.StringVar()
        self.abreviatura = tk.StringVar()

        self.entry_nombre = tk.Entry(self, textvariable=self.nombre, state='disabled', width=40)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.entry_abreviatura = tk.Entry(self, textvariable=self.abreviatura, state='disabled', width=20)
        self.entry_abreviatura.grid(row=1, column=1, padx=10, pady=10)

    def botones_principales(self):
        self.btn_alta = tk.Button(
            self, text='Nuevo', command=self.habilitar_campos,
            width=20, font=('Arial', 12, 'bold'),
            fg='#FFFFFF', bg='#1C500B'
        )
        self.btn_alta.grid(row=2, column=0, padx=10, pady=10)

        self.btn_guardar = tk.Button(
            self, text='Guardar', command=self.guardar_campos,
            width=20, font=('Arial', 12, 'bold'),
            fg='#FFFFFF', bg='#0D2A83', state='disabled'
        )
        self.btn_guardar.grid(row=2, column=1, padx=10, pady=10)

        self.btn_cancelar = tk.Button(
            self, text='Cancelar', command=self.bloquear_campos,
            width=20, font=('Arial', 12, 'bold'),
            fg='#FFFFFF', bg='#A90A0A', state='disabled'
        )
        self.btn_cancelar.grid(row=2, column=2, padx=10, pady=10)

    def mostrar_tabla(self):
        # Obtener y ordenar (invirtiendo) la lista
        self.lista_u = unidades.listar_unidades()
        self.lista_u.reverse()

        # Crear/recrear la tabla
        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Abreviatura'))
        self.tabla.grid(row=3, column=0, columnspan=3, sticky='nse')

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Abreviatura')

        # Limpiar filas previas y cargar nuevas
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for u in self.lista_u:
            self.tabla.insert('', 0, text=u[0], values=(u[1], u[2]))

        # Botones debajo de la tabla
        self.btn_editar = tk.Button(
            self, text='Editar', command=self.editar_registro,
            width=20, font=('Arial', 12, 'bold'),
            fg='#FFFFFF', bg='#1C500B'
        )
        self.btn_editar.grid(row=4, column=0, padx=10, pady=10)

        self.btn_delete = tk.Button(
            self, text='Delete', command=self.borrar_registro,
            width=20, font=('Arial', 12, 'bold'),
            fg='#FFFFFF', bg='#A90A0A'
        )
        self.btn_delete.grid(row=4, column=1, padx=10, pady=10)

    def guardar_campos(self):
        # Validaciones simples
        nombre = self.nombre.get().strip()
        abrev = self.abreviatura.get().strip()

        if not nombre:
            messagebox.showwarning("Atención", "El campo Nombre es obligatorio",parent=self)
            return
        if not abrev:
            messagebox.showwarning("Atención", "El campo Abreviatura es obligatorio",parent=self)
            return

        unidad = unidades.Unidad(nombre, abrev)

        try:
            if self.id_unidad is None:
                unidades.guardar_unidad(unidad)
            else:
                unidades.editar_unidad(unidad, int(self.id_unidad))
            self.mostrar_tabla()
            self.bloquear_campos()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {e}",parent=self)

    def editar_registro(self):
        try:
            seleccion = self.tabla.selection()
            if not seleccion:
                raise ValueError("Sin selección")
            self.id_unidad = self.tabla.item(seleccion)['text']
            valores = self.tabla.item(seleccion)['values']
            self.habilitar_campos()
            self.nombre.set(valores[0])
            self.abreviatura.set(valores[1])
        except:
            messagebox.showwarning("Atención", "Seleccione una unidad primero",
    parent=self)

    def borrar_registro(self):
        try:
            seleccion = self.tabla.selection()
            if not seleccion:
                raise ValueError("Sin selección")
            self.id_unidad = self.tabla.item(seleccion)['text']
            response = messagebox.askyesno("Confirmar", "¿Desea borrar la unidad de medida?", parent=self)
            if response:
                unidades.borrar_unidad(int(self.id_unidad))
            self.mostrar_tabla()
        except:
            messagebox.showwarning("Atención", "Seleccione una unidad primero",
    parent=self)

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_abreviatura.config(state='normal')
        self.btn_guardar.config(state='normal')
        self.btn_cancelar.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_abreviatura.config(state='disabled')
        self.btn_guardar.config(state='disabled')
        self.btn_cancelar.config(state='disabled')
        self.btn_alta.config(state='normal')
        self.nombre.set('')
        self.abreviatura.set('')
        self.id_unidad = None
