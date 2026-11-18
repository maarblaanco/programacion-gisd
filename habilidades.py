import shlex

# 1. Clase habilidad 

class Habilidad:
    '''Abstracción del concepto de habilidad en un asistente.'''

    def __init__(self, nombre, descripcion=None):
        self.nombre = nombre
        # Si no nos dan descripción, usamos la documentación de la clase o método
        self.descripcion = descripcion or self.__doc__

    def invocar(self):
        """Invocar la habilidad. No acepta parámetros"""
        print(f'Se ha invocado la habilidad {self.nombre}')

    def ayuda(self):
        """Devolver la descripción de la habilidad"""
        texto = self.invocar.__doc__ or self.descripcion
        print(texto)

# 4. Habilidad de conversión de divisas

class Divisas(Habilidad):
    '''Conversión de divisas'''
    def __init__(self, *args, tasa=0.85, **kwargs):
        super().__init__(*args, **kwargs)  # Llamamos al constructor de Habilidad
        self.tasa = tasa  # Guardamos la tasa de conversión

    def invocar(self, cantidad):
        '''Convertir una cantidad la divisa original a la divisa objetivo'''
        resultado = round(float(cantidad) * self.tasa, 2)
        print(resultado)
        return resultado

# 5. Menú interactivo

class Menu:
    '''Menú interactivo de gestión de habilidades.'''

    def __init__(self, habilidades):
        # habilidades es una LISTA
        # self.habilidades es un diccionario de nombre -> habilidad
        self.habilidades = {}
        # Llenamos el diccionario con las habilidades proporcionadas
        for hab in habilidades:
            self.habilidades[hab.nombre] = hab  # Asignamos cada habilidad al diccionario usando su nombre como clave

    def ayuda(self, habilidad=None):
        '''
        Muestra ayuda del uso del menú. Si no se especifica una habilidad,
        se muestra la ayuda general. Esta ayuda general muestra la lista
        de habilidades, una por línea, y la descripción de cada habilidad.

        Si se especifica una habilidad, se muestra su ayuda específica.
        '''
        if not habilidad: # Si no se proporciona una habilidad específica
            print('Habilidades disponibles:')
            for hab in self.habilidades.values():  # Iteramos sobre las habilidades
                print(f'\t{hab.nombre}:\t{hab.descripcion}')  # Mostramos el nombre y la descripción de cada habilidad
            return # Salimos del método(None)
        
        # Si se proporciona una habilidad específica
        if habilidad not in self.habilidades: # Verificamos si la habilidad existe
            print(f'Habilidad no encontrada: {habilidad}') # Mensaje de error si no se encuentra
            return
        
        # Si la habilidad existe, mostramos su ayuda
        self.habilidades[habilidad].ayuda() # Llamamos al método ayuda de la habilidad específica

    def lanzar(self):
        '''Recibe instrucciones del usuario en bucle.'''
        while True:
            linea = input('> ')  # Pide al usuario que ingrese un comando
            if self.ejecutar(linea):  # Ejecutamos el comando ingresado
                break  # Si se recibe "salir", rompe el bucle

    def convertir_linea(self, linea):
        '''Convierte una línea del usuario en comando + argumentos'''
        comando, *args = shlex.split(linea)  # Se usa shlex para dividir la línea en comando y argumentos
        return comando, args

    def ejecutar(self, linea):
        '''
        Recibe una línea del usuario y ejecuta la acción requerida.

        Devuelve True cuando se desea parar la ejecución.
        '''
        # Convierte la línea de entrada en un comando y sus argumentos
        comando, args = self.convertir_linea(linea)

        # Verifica si el comando es "salir"
        if comando == "salir":
            print("Adiós")
            return True  # Indica que se desea parar la ejecución

        # Verifica si el comando es "ayuda"
        elif comando == "ayuda":
            self.ayuda(*args)  # Llama al método ayuda con los argumentos proporcionados

        # Verifica si el comando no está en las habilidades disponibles
        elif comando not in self.habilidades:
            print(f"La habilidad '{comando}' no existe")  # Mensaje de error para comando no reconocido

        # Si el comando es válido, invoca la habilidad correspondiente
        else:
            self.habilidades[comando].invocar(*args)  # Llama a la habilidad con los argumentos proporcionados

        return False  # Indica que la ejecución debe continuar

    def emular(self, linea):
        '''Ejecuta una línea, mostrando por pantalla el comando'''
        print('>', linea)  # Muestra el comando que se va a ejecutar
        self.ejecutar(linea) # Llama al método ejecutar con la línea proporcionada

class MenuComas(Menu):
    '''Menú en el que el comando y los argumentos se proporcionan separados por comas.'''

    def convertir_linea(self, linea):
        '''Convierte una línea del usuario en comando + argumentos, separando por comas.'''
        comando, *args = [arg.strip() for arg in linea.split(',')]  # Separa la línea por comas y elimina espacios
        return comando, args  # Devuelve el comando y los argumentos

class MenuPrompt(Menu):
    # El símbolo al inicio de cada línea es configurable
    def __init__(self, *args, prompt=">", **kwargs):
        super().__init__(*args, **kwargs)  # Llama al constructor de la clase base
        self.prompt = prompt  # Almacena el símbolo de prompt proporcionado

    def emular(self, linea):
        """Ejecuta una línea, mostrando por pantalla el comando"""
        print(self.prompt, linea)  # Muestra el prompt y la línea
        self.ejecutar(linea)  # Ejecuta la línea

    def lanzar(self):
        """Recibe instrucciones del usuario en bucle."""
        while True:
            line = input(self.prompt + " ")  # Muestra el prompt y espera la entrada del usuario
            if self.ejecutar(line):  # Ejecuta la línea ingresada
                break  # Si se recibe "salir", rompe el bucle

class MenuPreguntas(Menu):
    '''Menú en el que se pide primero el comando y luego los argumentos uno a uno.'''

    def lanzar(self):
        '''Recibe instrucciones del usuario en bucle.'''
        while True:
            comando = input('> ')
            # Si el comando existe (o es ayuda/salir), se piden los argumentos
            if comando not in self.habilidades and comando not in ("ayuda", "salir"):
                print(f"La habilidad '{comando}' no existe")
                continue

            # Recoger argumentos uno a uno hasta que uno esté en blanco
            args = []
            while True:
                arg = input(f'Argumento {len(args)}: ')
                if arg == "":
                    break
                args.append(arg)

            if comando == "salir":
                print("Adiós")
                break
            elif comando == "ayuda":
                self.ayuda(*args)
            else:
                self.habilidades[comando].invocar(*args)


# 7. Habilidades con subcomandos

class HabilidadSubcomandos(Habilidad):
    '''Un tipo de habilidad que permite invocar varios sub-comandos'''

    def subcomandos(self):
        '''
        Devuelve un diccionario de subcomandos a funciones.
        
        p.e.:
            {
            'insertar': self.insertar_producto,
            'borrar': self.borrar_producto,
            }
        '''
        return {}

    def invocar(self, subcomando, *args):
        '''Invoca un subcomando específico con sus argumentos.'''
        if subcomando in self.subcomandos():
            return self.subcomandos()[subcomando](*args)  # Llama al subcomando correspondiente
        else:
            print(f"Subcomando '{subcomando}' no encontrado.")  # Mensaje de error si el subcomando no existe

    def ayuda(self):
        # Muestra información sobre el comando y sus subcomandos
        print('Comando:\t', self.nombre)
        print('Descripción:\t', self.descripcion)
        print('Subcomandos:')
        for subcomando in self.subcomandos():
            # Muestra la ayuda de cada subcomando
            print(f'\t{subcomando}: {self.subcomandos()[subcomando].__doc__}')


# Lista de la compra con subcomandos (apartado 7)

class ListaDeLaCompra(HabilidadSubcomandos):
    '''Gestión muy simple de lista de la compra'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.productos = []

    def subcomandos(self):
        return {
            'insertar': self.insertar,
            'borrar': self.borrar,
            'listar': self.listar,
            'cantidad': self.cantidad,
        }

    def insertar(self, producto):
        '''Insertar un producto nuevo'''
        self.productos.append(producto)

    def listar(self):
        '''Mostrar el listado de productos'''
        for ix, producto in enumerate(self.productos):
            print(f'{ix}: {producto}')

    def borrar(self, numero):
        '''Borrar un producto'''
        self.productos.pop(int(numero))

    def cantidad(self):
        '''Mostrar el número de productos en la lista'''
        print(len(self.productos))
        return len(self.productos)


# 8. Refactorizar el código

# Contador de vocales
class Contador(Habilidad):
    '''Contador de vocales en un texto.'''

    def invocar(self, texto: str):
        '''Devuelve el número de vocales en el texto dado.'''
        texto = texto.lower()
        vocales = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'u', 'ú']
        
        contador = 0
        for caracter in texto:
            if caracter in vocales:
                contador += 1
        
        print(f'Número de vocales: {contador}')
        return contador
    
# Palíndromos
class DetectorPalindromos(Habilidad):
    '''Detector de palíndromos.'''

    def invocar(self, texto: str):
        '''Detecta si un texto es palíndromo o no.'''
        texto = texto.replace(" ", "").lower()
        es_palindromo = texto == texto[::-1]
        if es_palindromo:
            print(f'El texto "{texto}" es un palíndromo.')
        else:
            print(f'El texto "{texto}" no es un palíndromo.')
        return es_palindromo
    
# Lista de la compra avanzada

class ListaCompraP2(HabilidadSubcomandos):
    '''Gestión avanzada de la lista de la compra.

    Acciones disponibles:
    - insertar <nombre> <precio> <categoria> <"etiquetas"(separadas por comas)> <prioridad>: Añade un nuevo producto a la lista. Ejemplo listacomprap2 insertar Manzana 1.5 Frutas "saludable,fresco" 2
    - borrar <índice>: Elimina un producto de la lista en la posición indicada.
    - mostrar: Muestra todos los productos en la lista.
    - listar: Muestra el listado de productos con su índice y nombre.
    - cantidad: Muestra cuántos productos hay en la lista.
    - actualizar_precio <índice> <nuevo_precio>: Actualiza el precio de un producto en la posición indicada.
    - cambiar_estado <índice>: Cambia el estado de un producto entre comprado y no comprado.
    - ordenar: Ordena la lista de productos.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.productos = []

    def subcomandos(self):
        return {
            'insertar': self.insertar,
            'borrar': self.borrar,
            'actualizar_precio': self.actualizar_precio,
            'cambiar_estado': self.cambiar_estado,
            'mostrar': self.mostrar_productos,
            'listar': self.listar,
            'ordenar': self.ordenar,
            'cantidad': self.cantidad,
        }

    def insertar(self, nombre: str, precio: float | int, categoria: str, etiquetas: str = "", prioridad: int = 3):
        '''Añade un producto nuevo a la lista.'''
        precio = float(precio)
       # Convertir la cadena de etiquetas en una lista
        etiquetas = [etiqueta.strip() for etiqueta in etiquetas.split(',')] if etiquetas else []
        prioridad = int(prioridad)  # Asegurarse de que prioridad sea un entero
        producto = {
            "nombre": nombre,
            "precio": precio,
            "categoria": categoria,
            "etiquetas": tuple(etiquetas),
            "prioridad": prioridad,
            "comprado": False
        }
        self.productos.append(producto)
        print(f'Producto "{nombre}" añadido a la lista.')

    def borrar(self, indice: str):
        '''Borra el producto en la posición indicada.'''
        if indice.isdigit():  # Verifica si el índice es un número entero positivo
            indice = int(indice)  # Convierte el índice a entero
            if 0 <= indice < len(self.productos):
                producto_borrado = self.productos.pop(indice)
                print(f'Producto "{producto_borrado["nombre"]}" borrado de la lista.')
            else:
                print("Índice fuera de rango. No se puede borrar.")
        else:
            print("El índice debe ser un número entero.")

    def actualizar_precio(self, indice: str, precio: str):
        '''Actualiza el precio del producto en la posición indicada.'''
        indice, precio = int(indice), float(precio)
        if 0 <= indice < len(self.productos):
            self.productos[indice]["precio"] = precio
            print(f'Precio del producto "{self.productos[indice]["nombre"]}" actualizado a {precio} €.')
        else:
            print("Índice fuera de rango.")

    def cambiar_estado(self, indice: str):
        '''Cambia el estado del producto entre comprado y no comprado.'''
        if indice.isdigit():  # Verifica si el índice es un número entero positivo
            indice = int(indice)  # Convierte el índice a entero
            if 0 <= indice < len(self.productos):
                self.productos[indice]["comprado"] = not self.productos[indice]["comprado"]
                estado = "comprado" if self.productos[indice]["comprado"] else "no comprado"
                print(f'Producto "{self.productos[indice]["nombre"]}" marcado como {estado}.')
            else:
                print("Índice fuera de rango.")
        else:
            print("El índice debe ser un número entero.")

    def mostrar_productos(self, comprados: bool = True, etiquetas: list[str] = [], categorias: list[str] = []):
        '''Muestra todos los productos con su información.'''
        if not self.productos:
            print("No hay productos en la lista.")
            return

        for producto in self.productos:
            # Filtrar por estado, comprado o no
            if not comprados and producto["comprado"]:
                continue

            # Filtrar por etiquetas
            if etiquetas and not all(etiqueta in producto["etiquetas"] for etiqueta in etiquetas):
                continue

            # Comprobar si el producto pertenece a una categoría de las indicadas
            if categorias and producto["categoria"] not in categorias:
                continue

            if producto["comprado"]:
                estado = "[x]"  
            else:
                estado = "[ ]"
            prioridad = "*" * producto["prioridad"]  # Asegúrate de que prioridad sea un entero
        
            # Mostrar correctamente las etiquetas
            etiquetas_str = " ".join(f"#{etiqueta}" for etiqueta in producto["etiquetas"]) if producto["etiquetas"] else ""

            # Imprime la información del producto
            print(f"{estado} {producto['categoria']} - {producto['nombre']} - {prioridad} - {producto['precio']} € - {etiquetas_str}")
    
    
    def listar(self):
        '''Mostrar el listado de productos con su índice y nombre.'''
        # Verifica si hay productos en la lista
        if not self.productos:
            print("No hay productos en la lista.")  # Mensaje si la lista está vacía
            return  # Sale del método si no hay productos
        
        print("Lista de productos:")  # Mensaje de encabezado para la lista
        # Itera sobre los productos en la lista con su índice
        for ix, producto in enumerate(self.productos):
            # Imprime el índice y el nombre del producto
            print(f'{ix}: {producto["nombre"]}')  # Muestra el índice y el nombre del producto

    def cantidad(self):
        '''Muestra la cantidad de productos en la lista.'''
        print(f"Hay {len(self.productos)} productos en la lista.")
        return len(self.productos)

    def ordenar(self):
        '''
        Se ordena la lista de productos, poniendo aquellos no comprados al principio.
        Dentro de los no comprados y comprados, se ordenan de mayor a menor prioridad.
        '''
        for i in range(1, len(self.productos)):    # Comenzamos desde el segundo elemento
            producto_actual = self.productos[i]  # Producto a ordenar
            j = i - 1  # Se empieza a comparar con el producto anterior
            
            # Comparamos el producto actual con los anteriores para encontrar su posición
            while j >= 0 and (
                # Si el producto anterior está comprado y el actual no, o 
                (self.productos[j]["comprado"] and not producto_actual["comprado"]) or 
                # Si ambos productos tienen el mismo estado de compra, pero el producto anterior tiene menor prioridad 
                (self.productos[j]["comprado"] == producto_actual["comprado"] and self.productos[j]["prioridad"] < producto_actual["prioridad"]) 
                ):
                
                self.productos[j + 1] = self.productos[j]  # Mueve el producto en la posición j a la derecha
                j -= 1  # El índice j se reduce para seguir comparando con los productos anteriores
            
            self.productos[j + 1] = producto_actual  # Cuando se encuentra la posición correcta para el producto actual, lo colocamos en su lugar ordenado 

        print("Lista de productos ordenada.")

    def ayuda(self):
        '''Muestra las acciones disponibles para esta habilidad.'''
        print(self.__doc__)  # Muestra la documentación de la clase
    

# Pruebas consola


def ejecutar_menu():
    '''Función para ejecutar el menú interactivo con todas las habilidades.'''
    habilidades = [
        Divisas('bitcoin2euro', tasa=49929.38, descripcion='Conversión de bitcoins a euros'),
        Divisas('euro2bitcoin', tasa=1/49929.38, descripcion='Conversión de euros a bitcoins'),
        Contador('contador', 'Contador de vocales en un texto.'),
        DetectorPalindromos('detector_palindromos', 'Detector de palíndromos.'),
        ListaCompraP2('listacomprap2', 'Gestión avanzada de la lista de la compra.')
    ]
    m = Menu(habilidades)
    m.lanzar()  # Inicia el menú interactivo

# Menú comas
def ejecutar_menu_comas():
    '''Función para ejecutar el menú interactivo con todas las habilidades.'''
    habilidades = [
        Divisas('bitcoin2euro', tasa=49929.38, descripcion='Conversión de bitcoins a euros'),
        Divisas('euro2bitcoin', tasa=1/49929.38, descripcion='Conversión de euros a bitcoins'),
        Contador('contador', 'Contador de vocales en un texto.'),
        DetectorPalindromos('detector_palindromos', 'Detector de palíndromos.'),
        ListaCompraP2('listacomprap2', 'Gestión avanzada de la lista de la compra.')
    ]
    menu = MenuComas(habilidades)  # Crea una instancia del menú con habilidades
    menu.lanzar()


def ejecutar_menu_prompt():
    '''Función para ejecutar el menú interactivo con todas las habilidades.'''
    habilidades = [
        Divisas('bitcoin2euro', tasa=49929.38, descripcion='Conversión de bitcoins a euros'),
        Divisas('euro2bitcoin', tasa=1/49929.38, descripcion='Conversión de euros a bitcoins'),
        Contador('contador', 'Contador de vocales en un texto.'),
        DetectorPalindromos('detector_palindromos', 'Detector de palíndromos.'),
        ListaCompraP2('listacomprap2', 'Gestión avanzada de la lista de la compra.')
    ]
    menu = MenuPrompt(habilidades, prompt='$$')  # Crea una instancia del menú con un prompt personalizado
    menu.lanzar()  # Lanza el menú para que el usuario interactúe

def ejecutar_menu_preguntas():
    '''Función para ejecutar el menú interactivo con todas las habilidades.'''
    habilidades = [
        Divisas('bitcoin2euro', tasa=49929.38, descripcion='Conversión de bitcoins a euros'),
        Divisas('euro2bitcoin', tasa=1/49929.38, descripcion='Conversión de euros a bitcoins'),
        Contador('contador', 'Contador de vocales en un texto.'),
        DetectorPalindromos('detector_palindromos', 'Detector de palíndromos.'),
        ListaCompraP2('listacomprap2', 'Gestión avanzada de la lista de la compra.')
    ]
    menu = MenuPreguntas(habilidades)  # Crea una instancia del menú de preguntas
    menu.lanzar()  # Lanza el menú para que el usuario interactúe

if __name__ == '__main__':
   
    ejecutar_menu()
    #ejecutar_menu_comas()
    #ejecutar_menu_prompt()
    #ejecutar_menu_preguntas()

