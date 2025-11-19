import tkinter as tk
from tkinter import ttk, messagebox

from modelo import proveedores_dao as proveedores

class FrameProveedores(tk.Toplevel):
    def __init__(self, root=None):
        super().__init__(root)
        self.title("ABM Proveedores")
        self.geometry("900x450")
        self.fondo = "#FBFCDD"
        self.config(bg=self.fondo)

        self.id_proveedor = None

        # Widgets internos
        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()

    def label_form(self):
        tk.Label(self, text="Nombre:", font=('Arial',12,'bold'),
                 bg=self.fondo, fg="#1931E8").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self, text="Contacto:", font=('Arial',12,'bold'),
                 bg=self.fondo, fg="#1931E8").grid(row=1, column=0, padx=10, pady=10)

    def input_form(self):
        self.nombre = tk.StringVar()
        self.contacto = tk.StringVar()

        self.entry_nombre = tk.Entry(self, textvariable=self.nombre, state='disabled', width=40)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.entry_contacto = tk.Entry(self, textvariable=self.contacto, state='disabled', width=40)
        self.entry_contacto.grid(row=1, column=1, padx=10, pady=10)

    def botones_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos,
                                  width=20, font=('Arial',12,'bold'),
                                  fg='#FFFFFF', bg='#1C500B')
        self.btn_alta.grid(row=2, column=0, padx=10, pady=10)

        self.btn_guardar = tk.Button(self, text='Guardar', command=self.guardar_campos,
                                     width=20, font=('Arial',12,'bold'),
                                     fg='#FFFFFF', bg='#0D2A83', state='disabled')
        self.btn_guardar.grid(row=2, column=1, padx=10, pady=10)

        self.btn_cancelar = tk.Button(self, text='Cancelar', command=self.bloquear_campos,
                                      width=20, font=('Arial',12,'bold'),
                                      fg='#FFFFFF', bg='#A90A0A', state='disabled')
        self.btn_cancelar.grid(row=2, column=2, padx=10, pady=10)

    def mostrar_tabla(self):
        self.lista_p = proveedores.listar_proveedores()
        self.lista_p.reverse()

        self.tabla = ttk.Treeview(self, columns=('Nombre','Contacto'))
        self.tabla.grid(row=3, column=0, columnspan=3, sticky='nse')

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Contacto')

        for p in self.lista_p:
            self.tabla.insert('',0,text=p[0], values=(p[1],p[2]))

        self.btn_editar = tk.Button(self, text='Editar', command=self.editar_registro,
                                    width=20, font=('Arial',12,'bold'),
                                    fg='#FFFFFF', bg='#1C500B')
        self.btn_editar.grid(row=4, column=0, padx=10, pady=10)

        self.btn_delete = tk.Button(self, text='Delete', command=self.borrar_registro,
                                    width=20, font=('Arial',12,'bold'),
                                    fg='#FFFFFF', bg='#A90A0A')
        self.btn_delete.grid(row=4, column=1, padx=10, pady=10)

    def guardar_campos(self):

        nombre = self.nombre.get().strip()   
        if not nombre:   # si está vacío
            messagebox.showwarning("Atención", "Debe ingresar un nombre válido",parent=self)
            return

        proveedor = proveedores.Proveedor(self.nombre.get(), self.contacto.get())

        try:
            if self.id_proveedor is None:
                proveedores.guardar_proveedor(proveedor)
            else:
                proveedores.editar_proveedor(proveedor, int(self.id_proveedor))
            self.mostrar_tabla()
            self.bloquear_campos()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {e}",parent=self)

    def editar_registro(self):
        try:
            self.id_proveedor = self.tabla.item(self.tabla.selection())['text']
            valores = self.tabla.item(self.tabla.selection())['values']
            self.habilitar_campos()
            self.nombre.set(valores[0])
            self.contacto.set(valores[1])
        except:
            messagebox.showwarning("Atención", "Seleccione un proveedor primero",parent=self)

    def borrar_registro(self):
        try:
            self.id_proveedor = self.tabla.item(self.tabla.selection())['text']
            response = messagebox.askyesno("Confirmar", "¿Desea borrar el proveedor?",parent=self)
            if response:
                proveedores.borrar_proveedor(int(self.id_proveedor))
            self.mostrar_tabla()
        except:
            messagebox.showwarning("Atención", "Seleccione un proveedor primero",parent=self)

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_contacto.config(state='normal')
        self.btn_guardar.config(state='normal')
        self.btn_cancelar.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_contacto.config(state='disabled')
        self.btn_guardar.config(state='disabled')
        self.btn_cancelar.config(state='disabled')
        self.btn_alta.config(state='normal')
        self.nombre.set('')
        self.contacto.set('')
        self.id_proveedor = None
