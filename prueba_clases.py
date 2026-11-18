from listadelacompra_clases import *

def prueba_lista_compra():
    # Crea una instancia de ListaCompra
    lista_compra = ListaCompra()

    # Inserta algunos productos en la lista de compra
    lista_compra.insertar("Garbanzos", 0.68, "Alimentación", ["cocido", "hummus"], 3)
    lista_compra.insertar("Hierbabuena", 1.5, "Alimentación", ["cocktails"], 1)
    lista_compra.insertar("Leche", 0.89, "Alimentación", ["lácteo"], 2)
    lista_compra.insertar("Pan", 1.0, "Alimentación", ["horneado"], 2)

    # Muestra los productos en la lista de compra
    print("Lista de productos después de insertar:")
    lista_compra.mostrar_productos()

    # Actualiza el precio de un producto
    lista_compra.actualizar_precio(1, 1.65)  # Cambia el precio de "Hierbabuena"
    print("\nLista de productos después de actualizar el precio de 'Hierbabuena':")
    lista_compra.mostrar_productos()

    # Cambia el estado de compra de un producto
    lista_compra.cambiar_estado(0)  # Marca "Garbanzos" como comprado
    print("\nLista de productos después de marcar 'Garbanzos' como comprado:")
    lista_compra.mostrar_productos()

    # Borra un producto de la lista
    lista_compra.borrar(2)  # Borra "Leche"
    print("\nLista de productos después de borrar 'Leche':")
    lista_compra.mostrar_productos()

    # Ordena la lista de productos
    lista_compra.ordenar()
    print("\nLista de productos después de ordenar:")
    lista_compra.mostrar_productos()

# Llama a la función de prueba
if __name__ == '__main__':
    prueba_lista_compra()