EURO_BITCOIN_RATE = 44471.78

def sumar_numeros(num1, num2):
    '''Suma los dos numeros proporcionados.'''
    suma = num1 + num2
    return suma

def euros_a_bitcoins(euros: int | float) -> int | float:
  '''Convierte una cantidad de euros a bitcoins. 1 bitcoin = 44471.78 €'''
  bitcoins = round(euros / EURO_BITCOIN_RATE, 2)
  return bitcoins

def bitcoins_a_euros(bitcoins: int | float) -> int | float:
  '''Convierte una cantidad de bitcoins a euros. 1 bitcoin = 44471.78 €'''
  euros = round (bitcoins * EURO_BITCOIN_RATE, 2)
  return euros

def contar_vocales(texto: str) -> int:
  '''Devuelve el número de vocales que tiene el texto dado.'''
  texto = texto.lower()
  
  vocales = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'u', 'ú']

  contador = 0
  for caracter in texto:
    if caracter in vocales:
      contador +=1 
  return contador

def es_palindromo(texto: str) -> bool:
  '''Detecta si un texto es palíndromo o no'''
  texto = texto.replace(" ", "").lower()    # Reemplaza todos los espacios con una cadena vacía "", quitando los espacios
  return texto == texto[::-1]

def max_temperaturas(temperaturas: list[float], umbral: float) -> list[float]: 
   '''Detecta qué mediciones de temperatura han superado el umbral dado'''
   temperaturas_superiores = []
   for temp in temperaturas:
        if temp > umbral:
            temperaturas_superiores.append(temp)
   return temperaturas_superiores
   # return[temp for temp in temperaturas if temp> umbral]  (más eficiente)

productos: list[str] = []

def insertar(producto: str) -> None:
   '''Añade un producto a la lista'''
   productos.append(producto)
  
def borrar(numero: int) -> None:
  '''Borra el producto en el índice dado de lista de productos.'''
  del productos[numero]

def mostrar_productos() -> None:      
     '''Muestra la lista de productos con sus índices.'''
     if len(productos) == 0:
        print("No hay productos")
     else:
        for indice, producto in enumerate(productos):
            print(f"{indice}: {producto}")
     

def cantidad() -> int:
  '''Devuelve el número de productos.'''
  return (len(productos))

# Menú interactivo
'''Menú interactivo para realizar diversas operaciones:
covertir euros a bitcoins y viceversa, contar vocales en un texto, verificar si un texto es un palíndromo, 
 filtrar temperaturas mayores a un umbral, mostrar, añadir y borrar productos y opción para salir del menú.'''


def menu_interactivo():
    '''Menú interactivo para que el usuario ingrese los comandos'''
    print("Menú interactivo\n"
          "Opciones disponibles:\n"
          "convertir euros bitcoins <cantidad>\n"
          "convertir bitcoins euros <cantidad>\n"
          "contar <texto>\n"
          "temperaturas <varios números separados por comas> <umbral>\n"
          "productos\n"
          "productos nuevo <nombre>\n"
          "productos borrar <índice>\n"
          "salir")

    while True:
        comando = input("-> ").strip().lower()  # Captura el comando ingresado por el usuario
        
        if comando.startswith("convertir euros bitcoins"):
            partes = comando.split()  # Divide el comando en partes
            cantidad = float(partes[3])  # Obtiene la cantidad de euros
            print(euros_a_bitcoins(cantidad))  # Muestra la conversión a bitcoins

        elif comando.startswith("convertir bitcoins euros"):
            partes = comando.split()  # Divide el comando en partes
            cantidad = float(partes[3])  # Obtiene la cantidad de bitcoins
            print(bitcoins_a_euros(cantidad))  # Muestra la conversión a euros

        elif comando.startswith("contar"):
            partes = comando.split()  # Divide el comando en partes
            texto = " ".join(partes[1:])  # Une las partes restantes como texto
            print(contar_vocales(texto))  # Llama a la función y muestra el resultado

        elif comando.startswith("temperaturas"):
            partes = comando.split()  # Divide el comando en partes
            temperaturas = []
            for temp in partes[1].split(','):  # Convierte las temperaturas a una lista de floats
                temperaturas.append(float(temp))
            umbral = float(partes[2])  # Convierte el umbral a float
            print(max_temperaturas(temperaturas, umbral))  # Muestra las temperaturas superiores al umbral

        elif comando == "productos":
            mostrar_productos()  # Muestra la lista de productos

        elif comando.startswith("productos nuevo"):
            partes = comando.split()  # Divide el comando en partes
            nombre = ""
            for i in range(2, len(partes)):  # Une las partes restantes como nombre del producto
                nombre += partes[i] + " "
            nombre = nombre.strip()  # Elimina el espacio extra al final
            insertar(nombre)  # Añade el producto a la lista
            print(nombre)  # Muestra el nombre del producto añadido

        elif comando.startswith("productos borrar"):
            partes = comando.split()  # Divide el comando en partes
            indice = int(partes[2])  # Convierte el índice a entero
            borrar(indice)  # Borra el producto en el índice especificado
            

        elif comando == "salir":
            print("¡Adiós!")  # Mensaje de despedida
            break  # Sale del bucle

        else:
            print("Comando no reconocido.")  # Mensaje de error si el comando no es válido

# Este bloque asegura que el código solo se ejecute cuando el archivo se ejecute directamente
if __name__ == "__main__":
    menu_interactivo()
