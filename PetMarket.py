
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
        
        if opcion == 1:
            categoria = input("Ingrese categoría a consultar: ")
            unidades_categoria(categoria, productos, stock)

            
def leer_opcion():
    while True:
        try:        
            opcion = int(input("Ingrese opción: "))
            print(" ")
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Error. Debe ingresar una opción valida.")
        except ValueError:
            print("Error. Debe ingresar una opción valida.")


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


main()