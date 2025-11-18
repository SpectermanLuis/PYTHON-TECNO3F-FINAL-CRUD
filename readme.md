# Sistema de Gestión de Productos

Proyecto académico en Python con **Tkinter** y SQLite.  
Permite administrar productos y tablas maestras (categorías, proveedores y unidades de medida), además de realizar consultas específicas desde un menú principal.

---

## 📂 Estructura de directorios

```
├── modelo/ │ 
├── coneciondb.py # Clase Conneccion: maneja conexión y cursor a la base de datos SQLite 
│ 
├── productos_dao.py # CRUD y clase Producto 
│ 
├── categorias_dao.py # CRUD y clase Categoria 
│ 
├── proveedores_dao.py # CRUD y clase Proveedor 
│ 
└── unidades_dao.py # CRUD y clase Unidad 
│ 
├── vista/ 
│ 
├── menu.py # Menú principal con opciones Inicio, Tablas Maestras, Productos, Consultas, Otros 
│ 
├── productos_frame.py # Ventana ABM Productos (Tkinter Toplevel) 
│ 
├── categorias_frame.py # Ventana ABM Categorías 
│ 
├── proveedores_frame.py # Ventana ABM Proveedores 
│ 
└── unidades_frame.py # Ventana ABM Unidades de Medida 
│ 
└── consultas_frame.py # Ventanas de consultas (por categoría, proveedor, unidad, stock bajo) 
│ 
├── main.py # Punto de entrada: inicializa la aplicación y abre el menú principal 
└── README.md # Documentación del proyecto
```

---

## 📌 Descripción breve de cada archivo

### Carpeta `modelo/`
- **coneciondb.py** → Clase `Conneccion` para abrir/cerrar conexión a SQLite.  
- **productos_dao.py** → Clase `Producto` y funciones CRUD para la tabla `Productos`.  
- **categorias_dao.py** → Clase `Categoria` y funciones CRUD para la tabla `Categorias`.  
- **proveedores_dao.py** → Clase `Proveedor` y funciones CRUD para la tabla `Proveedores`.  
- **unidades_dao.py** → Clase `Unidad` y funciones CRUD para la tabla `UnidadesMedida`.  

### Carpeta `vista/`
- **menu.py** → Barra de menú principal con opciones para abrir los distintos frames.  
- **productos_frame.py** → Ventana ABM de productos (alta, baja, modificación, listado).  
- **categorias_frame.py** → Ventana ABM de categorías.  
- **proveedores_frame.py** → Ventana ABM de proveedores.  
- **unidades_frame.py** → Ventana ABM de unidades de medida.  
- **consultas_frame.py** → Ventanas de consultas: por categoría, proveedor, unidad y stock bajo.  

### Raíz
- **main.py** → Archivo principal que arranca la aplicación y carga el menú.  
- **README.md** → Este documento con la estructura y explicación del proyecto.  

---

## 🚀 Cómo ejecutar
1. Clonar o descargar el proyecto.  
2. Ejecutar `main.py` con Python 3:  
   ```bash
   python main.py
