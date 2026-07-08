
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
                
    print(f"\nEl stock total para la categoria '{categoria}' es: {total_stock}")

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
        print(f"Categoria: {datos[1]}")
        print(f"Precio: ${datos[2]}")
        print(f"Disponible: {datos[3]}")
        print(f"Stock: {stock}")
        print(f"Vendidos: {vendidos}")


# funcion del menu
def mostrar_menu():
    print("""\n
    ========== MENu PRINCIPAL ==========
    1. Stock por categoria
    2. Buscar productos por rango de precio
    3. Actualizar precio
    4. Agregar producto
    5. Eliminar producto
    6. Mostrar productos
    7. Salir
    ====================================""")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if 1 <= opcion <= 7:
                return opcion
            else:
                print("Debe seleccionar una opcion valida")
        except ValueError:
            print("Debe seleccionar una opcion valida")


def ejecutar_programa():
    productos = {
        "P101": ["Cuaderno", "Papeleria", 2490, True],
        "P102": ["Lapiz", "Papeleria", 590, True]
    }
    inventario = {
        "P101": [30, 15],
        "P102": [120, 50]
    }
    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            while True:
                cat = input("Ingrese categoria a consultar: ").strip()
                if validar_categoria(cat):
                    break
                print("La categoria no puede estar vacia.")
            stock_categoria(cat, productos, inventario)

        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    if p_min >= 0: break
                    print("El precio minimo debe ser mayor o igual a cero.")
                except ValueError:
                    print("Debe ingresar un numero entero valido.")
            while True:
                try:
                    p_max = int(input("Ingrese precio maximo: "))
                    if p_max >= 0: break
                    print("El precio maximo debe ser mayor o igual a cero.")
                except ValueError:
                    print("Debe ingresar un numero entero valido.")
            
            if p_min > p_max:
                print("El precio minimo no puede ser mayor que el precio maximo.")
            else:
                buscar_precio(p_min, p_max, productos, inventario)

        elif opcion == 3:
            continuar = "s"
            while continuar.lower() == "s":
                cod = input("Ingrese codigo del producto a actualizar: ").strip()
                if buscar_codigo(cod, productos):
                    while True:
                        try:
                            n_precio = int(input("Ingrese nuevo precio: "))
                            if validar_precio(n_precio): break
                            print("El precio debe ser un entero mayor que cero.")
                        except ValueError:
                            print("Debe ingresar un numero entero valido.")
                    
                    actualizar_precio(cod, n_precio, productos)
                    print("Precio actualizado exitosamente.")
                else:
                    print("Codigo inexistente")
                
                continuar = input("Desea actualizar otro precio? (s/n): ").strip()

        elif opcion == 4:
            while True:
                cod = input("Ingrese nuevo codigo de producto: ").strip()
                if validar_codigo(cod, productos): break
                print("Codigo invalido o ya existente.")

            while True:
                nom = input("Ingrese nombre del producto: ").strip()
                if validar_nombre(nom): break
                print("El nombre no puede estar vacio.")

            while True:
                cat = input("Ingrese categoria: ").strip()
                if validar_categoria(cat): break
                print("La categoria no puede estar vacia.")

            while True:
                try:
                    prec = int(input("Ingrese precio: "))
                    if validar_precio(prec): break
                    print("El precio debe ser mayor que cero.")
                except ValueError:
                    print("Debe ingresar un numero entero.")

            while True:
                disp = input("Esta disponible? (s/n): ").strip()
                if validar_disponible(disp): break
                print("Debe ingresar 's' o 'n'.")

            while True:
                try:
                    stk = int(input("Ingrese stock inicial: "))
                    if validar_stock(stk): break
                    print("El stock debe ser mayor o igual a cero.")
                except ValueError:
                    print("Debe ingresar un numero entero.")

            while True:
                try:
                    vend = int(input("Ingrese cantidad de vendidos: "))
                    if validar_vendidos(vend): break
                    print("Los productos vendidos deben ser mayores o iguales a cero.")
                except ValueError:
                    print("Debe ingresar un numero entero.")

            agregar_producto(cod, nom, cat, prec, disp, stk, vend, productos, inventario)
            print("Producto agregado con exito.")

        elif opcion == 5:
            cod = input("Ingrese el codigo del producto a eliminar: ").strip()
            if eliminar_producto(cod, productos, inventario):
                print("Producto eliminado exitosamente.")
            else:
                print("El codigo no existe.")

        elif opcion == 6:
            mostrar_productos(productos, inventario)

        elif opcion == 7:
            print("Programa finalizado.")
            break
ejecutar_programa()
