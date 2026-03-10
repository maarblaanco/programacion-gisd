from utilidades import *

# Pruebas básicas
print("=== PRUEBAS BÁSICAS ===")

# Conversión de euros a bitcoins
print("\nPrueba: Conversión de Euros a Bitcoins")
print(euros_a_bitcoins(44471.78))  # Esperado: 1.0
print(euros_a_bitcoins(100000))    # Esperado: ~2.25
print(euros_a_bitcoins(0))         # Esperado: 0.0

# Conversión de bitcoins a euros
print("\nPrueba: Conversión de Bitcoins a Euros")
print(bitcoins_a_euros(1))         # Esperado: 44471.78
print(bitcoins_a_euros(2.25))      # Esperado: ~100061.50
print(bitcoins_a_euros(0))         # Esperado: 0.0

# Contar vocales
print("\nPrueba: Contar Vocales")
print(contar_vocales("Hola Mundo"))  # Esperado: 4
print(contar_vocales("ÁÉÍÓÚáéíóú"))  # Esperado: 10
print(contar_vocales("xyz"))         # Esperado: 0

# Verificar palíndromo
print("\nPrueba: Verificar Palíndromo")
print(es_palindromo("Anita lava la tina"))   # Esperado: True
print(es_palindromo("A man a plan a canal Panama"))  # Esperado: True
print(es_palindromo("Hola Mundo"))          # Esperado: False

# Filtrar temperaturas
print("\nPrueba: Filtrar Temperaturas")
print(max_temperaturas([30, 35, 40], 33))  # Esperado: [35, 40]
print(max_temperaturas([10, 15, 20], 50))  # Esperado: []
print(max_temperaturas([-5, 0, 5], 0))     # Esperado: [5]

# Manejo de la lista de productos
print("\nPrueba: Manejo de Lista de Productos")

# Limpieza inicial
productos.clear()
print("Lista inicial:", productos)  # Esperado: []

# Insertar productos
insertar("Manzana")
insertar("Pera")
insertar("Plátano")
print("Después de insertar:", productos)  # Esperado: ["Manzana", "Pera", "Plátano"]

# Borrar productos
borrar(1)
print("Después de borrar índice 1:", productos)  # Esperado: ["Manzana", "Plátano"]

# Mostrar productos
print("Productos actuales:")
mostrar_productos()  # Esperado: 0: Manzana, 1: Plátano

# Número de productos
print("Cantidad de productos:", len(productos))  # Esperado: 2

