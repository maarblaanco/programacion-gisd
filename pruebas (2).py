from listadelacompra import *


def pruebas():
    # Inicializar la lista de productos
    productos = []

    # Prueba 1: Insertar productos
    print("Prueba 1: Insertar productos")
    insertar("Huevo", 12.50, "Alimentación", ["huevos fritos", "empanada"], 3)
    insertar("Leche", 1.20, "Alimentación", ["lácteo"], 2)
    insertar("Pan", 0.80, "Alimentación", ["pan"], 5)
    
    # Mostrar productos después de la inserción
    mostrar_productos()
    print("\n")

    # Prueba 2: Borrar un producto
    print("Prueba 2: Borrar un producto")
    borrar(1)  # Borrar "Leche"
    mostrar_productos()
    print("\n")

    # Prueba 3: Actualizar precio
    print("Prueba 3: Actualizar precio")
    actualizar_precio(0, 15.00)  # Actualizar precio de "Huevo"
    mostrar_productos()
    print("\n")

    # Prueba 4: Cambiar estado de un producto
    print("Prueba 4: Cambiar estado de un producto")
    cambiar_estado(0)  # Cambiar estado de "Huevo" a comprado
    mostrar_productos()
    print("\n")

    # Prueba 5: Ordenar productos
    print("Prueba 6: Ordenar productos")
    insertar("Garbanzos", 0.68, "Alimentación", ["cocido", "hummus"], 3)
    insertar("Hierbabuena", 1.5, "Alimentación", ["cocktails"], 1)
    cambiar_estado(1)  # Cambiar estado de "Leche" a comprado
    ordenar()  # Ordenar productos
    mostrar_productos()
    print("\n")

# Llamar a la función de pruebas
if __name__ == '__main__':
    pruebas()