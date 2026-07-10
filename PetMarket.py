
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

        print("""========== MENÚ PRINCIPAL ==========
        1. Unidades por categoría
        2. Búsqueda de productos por rango de precio
        3. Actualizar precio de producto
        4. Agregar producto
        5. Eliminar producto
        6. Salir
        =====================================""")


def leer_opcion():
    while True:
        try:        
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Error. Debe ingresar una opción valida.")
        except ValueError:
            print("Error. Debe ingresar una opción valida.")



