
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

main()