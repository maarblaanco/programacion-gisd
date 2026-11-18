'''
Módulo de gestión la lista de la compra

Un producto es un diccionario con las siguientes claves:

* nombre, prioridad, precio, etiquetas, categoria, comprado

Por ejemplo:

producto = {
  "nombre": "Huevo",
  "precio": 12.50,
  "etiquetas": ("huevos fritos", "empanada"),
  "categoria": "Alimentación",
  "comprado": False
}

En la parte 4 de está práctica veremos cómo transformar esto en una estructura más elegante.
'''

productos: list[dict] = []

def insertar(nombre: str, precio: float | int, categoria: str, etiquetas: list[str]=[], prioridad: int=3):
    '''Añade un producto nuevo a la lista con los parámetros dados'''
    producto = {
        "nombre": nombre,
        "precio": precio,
        "categoria": categoria,
        "etiquetas": tuple(etiquetas),     # Convierte la lista de etiquetas a una tupla
        "prioridad": prioridad,
        "comprado": False
    }
    productos.append(producto)


def borrar(indice: int):
    '''Borra de la lista el producto que se encuentra en la posición indicada'''
    if 0 <= indice < len(productos):   
        productos.pop(indice)
    else:
        print("Índice fuera de rango. No se puede borrar.") 
    
def actualizar_precio(indice: int, precio: float):
    '''Actualiza el precio del producto con el índice dado'''
    if 0 <= indice < len(productos):
        productos[indice]["precio"] = precio   
    else:
        print("Índice fuera de rango o precio inválido.")
    
def cambiar_estado(indice: int):
    '''Cambia el estado del producto con el índice dado entre comprado o no'''
    if 0 <= indice < len(productos):
        productos[indice]["comprado"] = not productos[indice]["comprado"]
    else:
        print("Índice fuera de rango. No se puede cambiar el estado.")

def mostrar_productos(comprados: bool=True, etiquetas: list[str]=[], categorias: list[str]=[]):
    '''
    Muestra por pantalla todos los productos con su información. Si un producto ya ha sido comprado, se marca con una x al comienzo.
    La prioridad se indicará mediante el uso de asteriscos (*), es decir, un artículo con prioridad 5 se representará mediante cinco asteriscos (*****).
    Si comprados es False, no se muestran los productos ya comprados.
    Etiquetas es una tupla o lista con etiquetas o aclaraciones. Si está vacía, se muestran
    todos los productos. Si contiene alguna etiqueta, sólo se muestran los productos
    que tengan todas las etiquetas proporcionadas.
    Categorias es una lista con las categorías que se quieren obtener. Si está vacía, se muestran
    todos los productos. Si contiene alguna categoría, solo se muestran los productos cuya categoría
    esté contenida en la lista.
    Ejemplo en que sólo un producto ha sido comprado:
    >>> mostrar_productos()
    [x] Alimentación - Arroz integral - *** - 0.72 € - #risotto #arrozalacubana
    [ ] Alimentación - Huevos - * - 1.20 € - #arrozalacubana #tortilla 
    [ ] Cosméticos - Desmaquillante - ***** - 4.50 € - #fiesta #teatro

    >>> mostrar_productos(etiquetas=('arrozalacubana'))
    [x] Alimentación - Arroz integral - *** - 0.72 € - #risotto #arrozalacubana
    [ ] Alimentación - Huevos - * - 1.20 € - #arrozalacubana #tortilla
    '''
    
    for producto in productos:
        # Filtrar por estado, comprado o no
        if not comprados and producto["comprado"]:
            continue  # Si comprados es False y el producto ya ha sido comprado, se salta

        # Filtrar por etiquetas: comprobar que todas las etiquetas proporcionadas estén en las etiquetas del producto
        if etiquetas and not all(etiqueta in producto["etiquetas"] for etiqueta in etiquetas):
                continue  # Si falta alguna etiqueta, pasamos al siguiente producto

        # Comprobar si el producto pertenece a una categoría de las indicadas
        if categorias and producto["categoria"] not in categorias:
            continue
        
        # Determina el estado del producto: "[x]" si está comprado, "[ ]" si no lo está.
        if producto["comprado"]:
            estado = "[x]"  
        else:
            estado = "[ ]"  

        # Representa la prioridad del producto como una cadena de asteriscos (*), según su valor numérico.
        prioridad = "*" * producto['prioridad']

        # Convierte la lista de etiquetas en una cadena, donde cada etiqueta tiene el prefijo "#" y están separadas por espacios.
        etiquetas_str = " ".join(f"#{etiqueta}" for etiqueta in producto['etiquetas'])

        # Imprime la información del producto en un formato legible, mostrando su estado, categoría, nombre, prioridad, precio y etiquetas.
        print(f"{estado} {producto['categoria']} - {producto['nombre']} - {prioridad} - {producto['precio']} € - {etiquetas_str}")


def menu():
    '''
    Menú interactivo para modificar la lista de la compra.
    Acciones:

    -  mostrar
    -  insertar <nombre>; <precio>; <categoria>; <etiquetas separadas por comas>; <prioridad>
    -  borrar <indice>
    -  precio <numero>; <precio>
    -  comprado <numero>
    -  ayuda
    -  salir

    Por ejemplo:
    Introduce un comando: mostrar
    Introduce un comando: insertar Garbanzos; 0.68; Alimentación; cocido, hummus; 3
    Introduce un comando: insertar Hierbabuena; 1.5; Alimentación; cocktails; 1
    Introduce un comando: borrar 0
    Introduce un comando: precio 1; 1.65
    Introduce un comando: comprado 1
    '''

    # Diccionario que mapea los comandos a sus funciones correspondientes
    comandos = {
        "mostrar": mostrar_productos,
        "insertar": insertar,
        "borrar": borrar,
        "precio": actualizar_precio,
        "comprado": cambiar_estado,
    }

    while True:  
        # Solicita al usuario que introduzca un comando y elimina espacios al principio y al final
        accion = input("Introduce un comando: ").strip()
        # Divide el comando en la acción (primer elemento) y los argumentos (resto)
        comando = accion.split(" ", 1)  
        orden = comando[0]  # La primera parte es el comando a ejecutar

        match orden:
            case "mostrar":
                # Llama a la función para mostrar productos
                if productos:
                    comandos[orden]()  # Llama a la función mostrar_productos
                else:
                    print("No hay productos")  # Mensaje si no hay productos
                
            case "insertar":
                # Divide los argumentos por el separador ';' y limpia los espacios
                args = [arg.strip() for arg in comando[1].split(";")]  
                # Asigna cada argumento a su variable correspondiente
                nombre = args[0]  # Nombre del producto
                precio = float(args[1])  # Precio del producto convertido a float
                categoria = args[2]  # Categoría del producto
                # Limpia las etiquetas, separándolas por comas y eliminando espacios
                etiquetas = [etiqueta.strip() for etiqueta in args[3].split(",")]  
                prioridad = int(args[4])  # Prioridad del producto convertida a int
                # Llama a la función para insertar el nuevo producto en la lista
                comandos[orden](nombre, precio, categoria, etiquetas, prioridad)

            case "borrar":
                # Convierte el argumento a un índice entero y llama a la función para borrar
                indice = int(comando[1].strip())  
                comandos[orden](indice)  # Llama a la función para borrar

            case "precio":
                # Divide los argumentos por el separador ';' y limpia los espacios
                args = [arg.strip() for arg in comando[1].split(";")]  
                # Asigna los argumentos a sus variables
                indice = int(args[0])  # Índice del producto a actualizar
                precio = float(args[1])  # Nuevo precio del producto
                # Llama a la función para actualizar el precio del producto
                comandos[orden](indice, precio)

            case "comprado":
                # Convierte el argumento a un índice entero y llama a la función para cambiar el estado
                indice = int(comando[1].strip())  
                comandos[orden](indice)  # Llama a la función para cambiar el estado

            case "salir":
                # Mensaje de despedida y termina el programa
                print("Adiós")  
                break  # Sale del bucle y termina el programa

            case _:
                print(menu.__doc__.strip())  # Si no existe ese comando muestra la documentación



def ordenar():
    '''
    Se ordena la lista de productos, poniendo aquellos no comprados al principio.
    Dentro de los no comprados y comprados, se ordenan de mayor a menor prioridad.
    '''
    for i in range(1, len(productos)):    # Comenzamos desde el segundo elemento
        producto_actual = productos[i]  # Producto a ordenar
        j = i - 1  # Se empieza a comparar con el producto anterior
        
        # Comparamos el producto actual con los anteriores para encontrar su posición
        while j >= 0 and (
            # Si el producto anterior está comprado y el actual no, o 
            (productos[j]["comprado"] and not producto_actual["comprado"]) or 
            # Si ambos productos tienen el mismo estado de compra, pero el producto anterior tiene menor prioridad 
            (productos[j]["comprado"] == producto_actual["comprado"] and productos[j]["prioridad"] < producto_actual["prioridad"]) 
        ):
            
            productos[j + 1] = productos[j]  # Mueve el producto en la posición j a la derecha
            j -= 1  # El índice j se reduce para seguir comparando con los productos anteriores
        
        productos[j + 1] = producto_actual  # Cuando se encuentra la posición correcta para el producto actual, lo colocamos en su lugar ordenado


if __name__ == '__main__':
    menu()
