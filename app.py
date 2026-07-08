
# funciones de validacion que se utilizaarn 
def validar_codigo(codigo, productos): pass
def validar_nombre(nombre): pass
def validar_categoria(categoria): pass
def validar_precio(precio): pass
def validar_disponible(opcion): pass
def validar_stock(stock): pass
def validar_vendidos(vendidos): pass

# funciones logicas que se utilizaran para cada opciopn del menu
def buscar_codigo(codigo, productos): pass
def stock_categoria(categoria, productos, inventario): pass
def buscar_precio(precio_min, precio_max, productos, inventario): pass
def actualizar_precio(codigo, nuevo_precio, productos): pass
def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario): pass
def eliminar_producto(codigo, productos, inventario): pass
def mostrar_productos(productos, inventario): pass

# funcion del menu
def mostrar_menu(): pass
def leer_opcion(): pass
def ejecutar_programa():
    productos = {
        "P101": ["Cuaderno", "Papelería", 2490, True],
        "P102": ["Lápiz", "Papelería", 590, True]
    }
    inventario = {
        "P101": [30, 15],
        "P102": [120, 50]
    }
    # en esta parte debe ir el if para las opciones del menu

ejecutar_programa()
