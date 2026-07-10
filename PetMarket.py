
def main():
    while True:
        productos = {
        'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True,
        False],
        'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False,
        False],
        'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
        'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False,
        True],
        'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True,
        False],
        'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False,
        False]
        }

        stock = {
        'M001': [32990, 12],
        'M002': [9990, 0],
        'M003': [5490, 25],
        'M004': [7990, 5],
        'M005': [11990, 7],
        'M006': [24990, 3]
        }

        print("""\n========== MENÚ PRINCIPAL ==========
1. Unidades por categoría
2. Búsqueda de productos por rango de precio
3. Actualizar precio de producto
4. Agregar producto
5. Eliminar producto
6. Salir
=====================================""")

        opcion = leer_opcion()
        if opcion == 6:
            print("Programa finalizado.")
            break
        
        elif opcion == 1:
            categoria = input("Ingrese categoría a consultar: ")
            unidades_categoria(categoria, productos, stock)
        
        elif opcion == 2:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                busqueda_precio(p_min, p_max, productos, stock)
            except ValueError:
                print("Debe ingresar valores enteros.")

        elif opcion == 3:
            while True:
                codigo = input("Ingrese código del producto: ")
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio > 0:
                        if actualizar_precio(codigo, nuevo_precio, stock):
                            print("Precio actulalizado.")
                        else:
                            print("El código no existe.")
                    else:
                        print("El precio debe ser un numero entero mayor a cero.")
                except ValueError:
                    print("Debe ingresar un valor entero para el precio.")
                continuar = input("¿Desea actualizar otro precio (s/n)?: ").lower()
                if continuar != "s":
                    break
        elif opcion == 4:
            codigo = input("Ingrese código: ")
            nombre = input("Ingrese nombre: ")
            categoria = input("Ingrese categoria: ")
            marca = input("Ingrese marca: ")
            peso = float(input("Ingrese peso (kg): "))
            es_imp = input("¿Es importado? (s/n): ")
            es_cach = input("¿Es para cachorro? (s/n): ")
            precio = int(input("Ingrese precio: "))
            unidades = int(input("Ingrese unidades: "))
            if (validar_codigo(codigo) and validar_nombre(nombre) and validar_categoria(categoria) and validar_marca(marca) and validar_peso(peso) and validar_si_no(es_imp) and validar_si_no(es_cach) and validar_precio(precio) and validar_unidades(unidades)):
                if agregar_producto(codigo, nombre, categoria, marca, peso, es_imp, es_cach, precio, unidades):
                    print("Producto agrgado.")
            else:
                print("Datos invalidos o el codigo ya existe.")

def leer_opcion():
    while True:
        try:        
            opcion = int(input("Ingrese opción: "))
            print(" ")
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe ingresar una opción valida.")
        except ValueError:
            print("Debe ingresar una opción valida.")


def unidades_categoria(categoria, productos, stock):
    categoria = categoria.lower()
    total_unidades = 0

    for codigo, info in productos.items():
        categoria_producto = info[1].lower()

        if categoria_producto == categoria:
            if codigo in stock:
                unidades = stock[codigo][1]
                total_unidades += unidades
    print(f"\nEl total de unidades disponibles es: {total_unidades}")

def busqueda_precio(p_min, p_max, productos, stock):
    if p_min < 0 or p_max < 0 or p_min > p_max:
        print("Rango de precios inválido.")
        return 
    resultados = []
    for codigo, info in stock.items():
        precio = info[0] 
        unidades = info[1]

        if p_min <= precio <= p_max and unidades > 0:
            nombre = productos[codigo][0]
            resultados.append(f"{nombre}--{codigo}")
    
    if not resultados:
        print("No hay productos en ese rango de precios.")
    else:
        resultados.sort()
        print(f"Los productos encontrados son: {resultados}")

def buscar_codigo(codigo, stock):
    codigo = codigo.upper()
    return codigo in stock

def actualizar_precio(codigo, nuevo_precio, stock):
    if buscar_codigo(codigo, stock):
        stock[codigo.upper()][0] = nuevo_precio
        return True
    return False

def agregar_producto(codigo, nombre, categoria, marca, peso, es_imp, es_cach, precio, unidades, productos, stock):
    imp_bool = True if es_imp.lower() == "s" else False
    cach_bool = True if es_cach.lower() == "s" else False
    
    productos[codigo.upper()] = [nombre, categoria, marca, peso, imp_bool, cach_bool]
    stock[codigo.upper()] = [precio, unidades]
    return True

def validar_codigo(codigo, productos):
    return len(codigo.strip()) > 0 and codigo.upper() not in productos

def validar_nombre(nombre):
    return len(nombre.strip()) > 0

def validar_categoria(categoria):
    return len(categoria.strip()) > 0

def validar_marca(marca):
    return len(marca.strip()) > 0

def validar_peso(peso):
    return peso > 0

def validar_si_no(valor):
    return valor.lower() in ["s", "n"]

def validar_precio(precio):
    return isinstance(precio, int) and precio > 0

def validar_unidades(unidades):
    return isinstance(unidades, int) and unidades >= 0

main()