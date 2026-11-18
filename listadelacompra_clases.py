class Producto:
    def __init__(self, nombre: str, precio: float | int, categoria: str, etiquetas: list[str] = [], prioridad: int = 3):
        # Inicializa un nuevo producto con sus atributos
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.etiquetas = tuple(etiquetas)  # Convertimos la lista de etiquetas a una tupla
        self.prioridad = prioridad
        self.comprado = False  # Inicializamos como no comprado


class ListaCompra:
    def __init__(self):
        # Inicializa la lista de productos
        self.productos = []  # Inicializa la lista de productos

    def insertar(self, nombre: str, precio: float | int, categoria: str, etiquetas: list[str] = [], prioridad: int = 3):
        # Crea un nuevo producto y lo añade a la lista
        producto = Producto(nombre, precio, categoria, etiquetas, prioridad)
        self.productos.append(producto)  # Añade el nuevo producto a la lista

    def borrar(self, indice: int):
        if 0 <= indice < len(self.productos):
            self.productos.pop(indice)  # Borra el producto en la posición indicada
        else:
            print("Índice fuera de rango. No se puede borrar.")

    def actualizar_precio(self, indice: int, precio: float):
        if 0 <= indice < len(self.productos):
            self.productos[indice].precio = precio  # Actualiza el precio del producto
        else:
            print("Índice fuera de rango o precio inválido.")

    def cambiar_estado(self, indice: int):
        if 0 <= indice < len(self.productos):
            self.productos[indice].comprado = not self.productos[indice].comprado  # Cambia el estado del producto
        else:
            print("Índice fuera de rango. No se puede cambiar el estado.")

    def mostrar_productos(self, comprados: bool = True, etiquetas: list[str] = [], categorias: list[str] = []):
        for producto in self.productos:
            # Filtrar por estado, comprado o no
            if not comprados and producto.comprado:
                continue  # # Salta si el producto ya ha sido comprado

            # Filtrar por etiquetas
            if etiquetas and not all(etiqueta in producto.etiquetas for etiqueta in etiquetas):
                continue  # Salta si falta alguna etiqueta

            # Comprobar si el producto pertenece a una categoría de las indicadas
            if categorias and producto.categoria not in categorias:
                continue  # Salta si la categoría no está en las indicadas

            # Determina el estado del producto
            if producto.comprado:
                estado = "[x]" 
            else:
                estado = "[ ]"
            prioridad = "*" * producto.prioridad
            etiquetas_str = " ".join(f"#{etiqueta}" for etiqueta in producto.etiquetas)

            # Imprime la información del producto
            print(f"{estado} {producto.categoria} - {producto.nombre} - {prioridad} - {producto.precio} € - {etiquetas_str}")

    def ordenar(self):
        for i in range(1, len(self.productos)):  # Comenzamos desde el segundo elemento
            producto_actual = self.productos[i]  # Producto a ordenar
            j = i - 1  # Se empieza a comparar con el producto anterior
            
            # Comparamos el producto actual con los anteriores para encontrar su posición
            while j >= 0 and (
                # Si el producto anterior está comprado y el actual no, o 
                (self.productos[j].comprado and not producto_actual.comprado) or 
                # Si ambos productos tienen el mismo estado de compra, pero el producto anterior tiene menor prioridad 
                (self.productos[j].comprado == producto_actual.comprado and self.productos[j].prioridad < producto_actual.prioridad) 
            ):
                self.productos[j + 1] = self.productos[j]  # Mueve el producto en la posición j a la derecha
                j -= 1  # El índice j se reduce para seguir comparando con los productos anteriores
            
            self.productos[j + 1] = producto_actual  # Cuando se encuentra la posición correcta para el producto actual, lo colocamos en su lugar ordenado.


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

    lista_compra = ListaCompra()  # Crea una instancia de ListaCompra

    while True:
        accion = input("Introduce un comando: ").strip()
        comando = accion.split(" ", 1)
        orden = comando[0]

        match orden:
            case "mostrar":
                if lista_compra.productos:
                    lista_compra.mostrar_productos()
                else:
                    print("No hay productos")

            case "insertar":
                args = [arg.strip() for arg in comando[1].split(";")]
                nombre = args[0]
                precio = float(args[1])
                categoria = args[2]
                etiquetas = [etiqueta.strip() for etiqueta in args[3].split(",")]
                prioridad = int(args[4])
                # Inserta el nuevo producto en la lista
                lista_compra.insertar(nombre, precio, categoria, etiquetas, prioridad)

            case "borrar":
                indice = int(comando[1].strip())
                lista_compra.borrar(indice)

            case "precio":
                args = [arg.strip() for arg in comando[1].split(";")]
                indice = int(args[0])
                precio = float(args[1])
                lista_compra.actualizar_precio(indice, precio)

            case "comprado":
                indice = int(comando[1].strip())
                lista_compra.cambiar_estado(indice)

            case "ordenar":
                lista_compra.ordenar()  

            case "salir":
                print("Adiós")
                break

            case _:
                print(menu.__doc__)  # Imprime la documentación del menú
                

if __name__ == '__main__':
    menu()