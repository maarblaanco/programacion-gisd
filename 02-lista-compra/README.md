# Lista de la compra en Python

Gestor de lista de la compra por consola, implementado de dos formas para comparar enfoques: con **funciones y diccionarios** y con **clases (programación orientada a objetos)**. Proyecto de la asignatura **Programación** (1.º, Grado en Ingeniería y Sistemas de Datos, ETSIT-UPM).

## Qué hace

Cada producto tiene nombre, precio, categoría, etiquetas, prioridad (de 1 a 5, mostrada con asteriscos) y estado (comprado o no). Se puede:

- Insertar y borrar productos.
- Actualizar el precio de un producto.
- Marcar o desmarcar un producto como comprado.
- Mostrar la lista, con filtros por estado, etiquetas y categorías.
- Ordenar la lista: primero los no comprados y, dentro de cada grupo, de mayor a menor prioridad (ordenación por inserción implementada a mano).

## Estructura

| Archivo | Contenido |
|---|---|
| `listadelacompra.py` | Versión con funciones y diccionarios, y menú interactivo |
| `listadelacompra_clases.py` | Versión con las clases `Producto` y `ListaCompra`, y menú interactivo |
| `test.py` / `test_clases.py` | Tests de cada versión |
| `pruebas.py` / `prueba_clases.py` | Scripts de demostración |

## Cómo ejecutarlo

Abre una terminal en esta carpeta. Requiere Python 3.10 o superior (usa `match`).

```bash
python listadelacompra.py          # versión con funciones
python listadelacompra_clases.py   # versión con clases
```

Ejemplo:

```
Introduce un comando: insertar Pan; 1.2; Comida; horneado; 2
Introduce un comando: mostrar
[ ] Comida - Pan - ** - 1.2 € - #horneado
Introduce un comando: salir
Adiós
```

Comandos: `mostrar`, `insertar <nombre>; <precio>; <categoría>; <etiquetas>; <prioridad>`, `borrar <índice>`, `precio <índice>; <precio>`, `comprado <índice>` y `salir`. Cualquier otro comando muestra la ayuda.

## Tests

```bash
python -m unittest test
python -m unittest test_clases
```

## Posibles mejoras

- Añadir el comando `ordenar` al menú (la función existe, pero el menú aún no la expone).
- Validar la entrada del menú para evitar excepciones con comandos incompletos.
- Guardar la lista en un archivo para que no se pierda al cerrar el programa.

## Tecnologías

Python 3.12 · `unittest`
