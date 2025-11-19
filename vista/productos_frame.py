import tkinter as tk
from tkinter import ttk, messagebox

#import modelo.productos_dao as productos
#import modelo.categorias_dao as categorias
#import modelo.proveedores_dao as proveedores
#import modelo.unidades_dao as unidades

from modelo import productos_dao as productos
from modelo import categorias_dao as categorias
from modelo import proveedores_dao as proveedores
from modelo import unidades_dao as unidades

#class FrameProductos(tk.Frame):
class FrameProductos(tk.Toplevel):    
    def __init__(self, root=None):
        super().__init__(root, width=900, height=600)
        self.root = root
       # self.pack()
        self.id_producto = None
        self.fondo = "#FBFCDD"
        self.config(bg=self.fondo)

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()

    def label_form(self):
        tk.Label(self, text="Nombre:", font=('Arial',12,'bold'),
                 bg=self.fondo, fg="#1931E8").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self, text="Stock:", font=('Arial',12,'bold'),
                 bg=self.fondo, fg="#1931E8").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self, text="Categoría:", font=('Arial',12,'bold'),
                 bg=self.fondo, fg="#1931E8").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self, text="Proveedor:", font=('Arial',12,'bold'),
                 bg=self.fondo, fg="#1931E8").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(self, text="Unidad:", font=('Arial',12,'bold'),
                 bg=self.fondo, fg="#1931E8").grid(row=4, column=0, padx=10, pady=10)

    def input_form(self):

        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre, state='disabled', width=50)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.stock  = tk.StringVar()
        self.entry_stock = tk.Entry(self, textvariable=self.stock, state='disabled', width=50)
        self.entry_stock.grid(row=1, column=1, padx=10, pady=10)

        # Combos
        self.categoria_manager = categorias.CategoriaManager()
        self.entry_categoria = ttk.Combobox(self, state="readonly")    
        self.entry_categoria.config(width=25, state='disabled')
        self.entry_categoria['values'] = self.categoria_manager.get_nombres()
        self.entry_categoria.current(0)

        def on_categoria_selected(event):
            selected_index = self.entry_categoria.current()
            genero_id = self.categoria_manager.get_id_por_indice(selected_index)
            return genero_id

        self.entry_categoria.bind("<<ComboboxSelected>>", on_categoria_selected)
        self.entry_categoria.grid(row= 2, column=1,padx=10,pady=10)

       # Combos
        self.proveedor_manager = proveedores.ProveedorManager()
        self.entry_proveedor = ttk.Combobox(self, state="readonly")    
        self.entry_proveedor.config(width=25, state='disabled')
        self.entry_proveedor['values'] = self.proveedor_manager.get_nombres()
        self.entry_proveedor.current(0)

        def on_proveedor_selected(event):
            selected_index = self.entry_proveedor.current()
            genero_id = self.proveedor_manager.get_id_por_indice(selected_index)
            return genero_id

        self.entry_proveedor.bind("<<ComboboxSelected>>", on_proveedor_selected)
        self.entry_proveedor.grid(row= 3, column=1,padx=10,pady=10)


       # Combos
        self.unidad_manager = unidades.UnidadManager()
        self.entry_unidad = ttk.Combobox(self, state="readonly")    
        self.entry_unidad.config(width=25, state='disabled')
        self.entry_unidad['values'] = self.unidad_manager.get_nombres()
        self.entry_unidad.current(0)

        def on_unidad_selected(event):
            selected_index = self.entry_unidad.current()
            genero_id = self.unidad_manager.get_id_por_indice(selected_index)
            return genero_id

        self.entry_unidad.bind("<<ComboboxSelected>>", on_unidad_selected)
        self.entry_unidad.grid(row= 4, column=1,padx=10,pady=10)


    def botones_principales(self):    
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos)    
        self.btn_alta.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')    
        self.btn_alta.grid(row= 6, column=0,padx=10,pady=10)   

        self.btn_guardar = tk.Button(self, text='Guardar', command=self.guardar_campos)    
        self.btn_guardar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#0D2A83',cursor='hand2',activebackground='#7594F5',activeforeground='#000000', state='disabled')    
        self.btn_guardar.grid(row= 6, column=1,padx=10,pady=10) 

        self.btn_cancelar = tk.Button(self, text='Cancelar', command=self.bloquear_campos)    
        self.btn_cancelar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000', state='disabled')    
        self.btn_cancelar.grid(row= 6, column=2,padx=10,pady=10)


    def mostrar_tabla(self):
        self.lista_p = productos.listar_productos()
        self.lista_p.reverse()

        self.tabla = ttk.Treeview(self, columns=('Nombre','Stock','Categoria','Proveedor','Unidad'))
        self.tabla.grid(row=7, column=0, columnspan=4, sticky='nse')


        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=7, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Stock')
        self.tabla.heading('#3', text='Categoría')
        self.tabla.heading('#4', text='Proveedor')
        self.tabla.heading('#5', text='Unidad')

        for p in self.lista_p:
            self.tabla.insert('',0,text=p[0],
                              values=(p[1],p[2],p[3],p[4],p[5]))

        self.btn_editar = tk.Button(self, text='Editar', command= self.editar_registro)    
        self.btn_editar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')    
        self.btn_editar.grid(row= 8, column=0,padx=10,pady=10)    
        
        self.btn_delete = tk.Button(self, text='Delete', command= self.borrar_registro)    
        self.btn_delete.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')    
        self.btn_delete.grid(row= 8, column=1,padx=10,pady=10)


    def borrar_registro(self):
        try:
            self.id_producto = self.tabla.item(self.tabla.selection())['text']
            response = messagebox.askyesno("Confirmar", "¿Desea borrar el producto?",parent=self)
            
            if response:
                productos.borrar_producto(int(self.id_producto))
            else:
                messagebox.showinfo("Aviso", "No se borró ningún producto",parent=self)
            
            self.id_producto = None
            self.mostrar_tabla()
        except:
            messagebox.showwarning("Atención", "Seleccione un producto primero",parent=self)

    def guardar_campos(self):

        nombre = self.nombre.get().strip()   

        if not nombre:   # si está vacío
            messagebox.showwarning("Atención", "Debe ingresar un nombre válido",parent=self)
            return

        try:
            stock_valor = int(self.stock.get())
        except ValueError:
            messagebox.showerror("Error", "El campo Stock debe ser un número entero",parent=self)
            return  # salir sin guardar

        if self.entry_categoria.current() == 0:
            messagebox.showwarning("Atención", "Debe seleccionar una categoría válida",parent=self)
            return

        if self.entry_proveedor.current() == 0:
            messagebox.showwarning("Atención", "Debe seleccionar un proveedor válido",parent=self)
            return

        if self.entry_unidad.current() == 0:
            messagebox.showwarning("Atención", "Debe seleccionar una unidad válida",parent=self)
            return

        producto = productos.Producto(
            self.nombre.get(),
            int(self.stock.get()),
            self.categoria_manager.get_id_por_indice(self.entry_categoria.current()),
            self.proveedor_manager.get_id_por_indice(self.entry_proveedor.current()),
            self.unidad_manager.get_id_por_indice(self.entry_unidad.current())
        )

        try:
            if self.id_producto is None:
                productos.guardar_producto(producto)
            else:
                productos.editar_producto(producto, int(self.id_producto))

            self.mostrar_tabla()
            self.bloquear_campos()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {e}",parent=self)

    def editar_registro(self):
        try:
            self.id_producto = self.tabla.item(self.tabla.selection())['text']
            valores = self.tabla.item(self.tabla.selection())['values']

            self.habilitar_campos()
            self.nombre.set(valores[0])
            self.stock.set(valores[1])

            indice_cat = self.categoria_manager.get_indice_por_nombre(valores[2])
            self.entry_categoria.current(indice_cat)

            indice_prov = self.proveedor_manager.get_indice_por_nombre(valores[3])
            self.entry_proveedor.current(indice_prov)

            # messagebox.showinfo("Debug", f"Valor en valores[4]: {valores[4]}") 
            indice_uni = self.unidad_manager.get_indice_por_abreviatura(valores[4])
            self.entry_unidad.current(indice_uni)

            try:
                # messagebox.showinfo("Debug", f"Valor en valores[4]: {valores[4]}") 
                indice_uni = self.unidad_manager.get_indice_por_abreviatura(valores[4])
                self.entry_unidad.current(indice_uni)
            except Exception as e:
                print("Error en get_indice_por_abreviatura:", e)
                messagebox.showerror("Error", f"Ocurrió un error: {e}",parent=self)
        
        except:
            messagebox.showwarning("Atención", "Seleccione un producto primero",parent=self)

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_stock.config(state='normal')
        self.entry_categoria.config(state='readonly')
        self.entry_proveedor.config(state='readonly')
        self.entry_unidad.config(state='readonly')
        self.btn_guardar.config(state='normal')
        self.btn_cancelar.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_stock.config(state='disabled')
        self.entry_categoria.config(state='disabled')
        self.entry_proveedor.config(state='disabled')
        self.entry_unidad.config(state='disabled')
        self.btn_guardar.config(state='disabled')
        self.btn_cancelar.config(state='disabled')
        self.btn_alta.config(state='normal')
        self.nombre.set('')
        self.stock.set('')
        self.entry_categoria.current(0)
        self.entry_proveedor.current(0)
        self.entry_unidad.current(0)
        self.id_producto = None
