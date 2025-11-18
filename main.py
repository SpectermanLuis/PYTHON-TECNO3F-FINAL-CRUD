import tkinter as tk
from vista.productos_frame import FrameProductos
from include.menu import barrita_menu
from modelo.productos_dao import crear_tabla   # importar la función

def main():
    ventana = tk.Tk()
    ventana.title('Sistema de Ferreteria')
    # ventana.iconbitmap('img/icono.ico')
    # ventana.resizable(0,0)
    ventana.geometry("900x600")


    logo = tk.PhotoImage(file="img/imagen_logo.png")

    # Mostrar imagen centrada
    label_logo = tk.Label(ventana, image=logo)
    label_logo.pack(expand=True)


    # Crear tablas automáticamente al inicio
    crear_tabla()

    # Menú
    barrita_menu(ventana)

    # Frame principal
    # app = FrameProductos(root=ventana)

    ventana.mainloop()

if __name__ == '__main__':
    main()
