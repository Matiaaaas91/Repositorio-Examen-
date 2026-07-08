
# funciones de validacion que se utilizaarn 
def validar_codigo(codigo, productos):
    codigo_limpio = codigo.strip().upper()
    if codigo_limpio == "":
        return False
    return codigo_limpio not in [k.upper() for k in productos.keys()]

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_categoria(categoria):
    return categoria.strip() != ""

def validar_precio(precio):
    return precio > 0

def validar_disponible(opcion):
    return opcion.strip().lower() in ['s', 'n']

def validar_stock(stock):
    return stock >= 0

def validar_vendidos(vendidos):
    return vendidos >= 0


# funciones logicas que se utilizaran para cada opciopn del menu
def buscar_codigo(codigo, productos):
    return codigo.strip().upper() in [k.upper() for k in productos.keys()]

def stock_categoria(categoria, productos, inventario):
    total_stock = 0
    cat_buscar = categoria.strip().lower()
    
    for cod, datos in productos.items():
        cat_producto = datos[1].lower()
        if cat_producto == cat_buscar:
            if cod in inventario:
                total_stock += inventario[cod][0] 
                
    print(f"\nEl stock total para la categoría '{categoria}' es: {total_stock}")

def buscar_precio(precio_min, precio_max, productos, inventario):
    resultados = []
    
    for cod, datos_inv in inventario.items():
        stock = datos_inv[0]
        if cod in productos:
            precio = productos[cod][2] 
            nombre = productos[cod][0] 
            
            if precio >= precio_min and precio <= precio_max and stock > 0:
                resultados.append(f"{nombre}--{cod}")
                
    resultados.sort() 
    
    if resultados:
        print("\nProductos encontrados:")
        for r in resultados:
            print(r)
    else:
        print("\nNo se encontraron productos en ese rango de precio con stock disponible.")

def actualizar_precio(codigo, nuevo_precio, productos):
    cod_upper = codigo.strip().upper()
    for real_key in productos.keys():
        if real_key.upper() == cod_upper:
            productos[real_key][2] = nuevo_precio 
            return True
    return False

def agregar_producto(codigo, nombre, categoria, precio, disponible, stock, vendidos, productos, inventario):
    cod_upper = codigo.strip().upper()
    
    if not validar_codigo(cod_upper, productos):
        return False
        
    bool_disponible = True if disponible.lower() == 's' else False
    
    productos[cod_upper] = [nombre.strip(), categoria.strip(), precio, bool_disponible]
    inventario[cod_upper] = [stock, vendidos]
    return True

def eliminar_producto(codigo, productos, inventario):
    cod_upper = codigo.strip().upper()
    llave_encontrada = None
    
    for real_key in productos.keys():
        if real_key.upper() == cod_upper:
            llave_encontrada = real_key
            break
            
    if llave_encontrada:
        del productos[llave_encontrada]
        if llave_encontrada in inventario:
            del inventario[llave_encontrada]
        return True
    return False

def mostrar_productos(productos, inventario):
    if not productos:
        print("\nNo hay productos registrados.")
        return
        
    for cod, datos in productos.items():
        stock = inventario[cod][0] if cod in inventario else 0
        vendidos = inventario[cod][1] if cod in inventario else 0
        print(f"\nCODIGO: {cod}")
        print(f"Nombre: {datos[0]}")
        print(f"Categoría: {datos[1]}")
        print(f"Precio: ${datos[2]}")
        print(f"Disponible: {datos[3]}")
        print(f"Stock: {stock}")
        print(f"Vendidos: {vendidos}")


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
