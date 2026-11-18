# Utilidades en Python

Colección de funciones de utilidad en Python con un menú interactivo por consola. Proyecto de la asignatura **Programación** (1.º, Grado en Ingeniería y Sistemas de Datos, ETSIT-UPM).

## Qué incluye

- **Conversión de divisas:** euros a bitcoins y bitcoins a euros (tasa fija de 44 471,78 € por bitcoin).
- **Texto:** contar vocales (con tildes) y detectar palíndromos.
- **Temperaturas:** filtrar las mediciones que superan un umbral.
- **Lista de productos:** insertar, borrar, mostrar y contar productos.
- **Menú interactivo** que une todas las funciones anteriores.

## Conceptos que practica

Funciones con anotaciones de tipo, bucles y condicionales, listas, manejo de cadenas, entrada por consola y pruebas automáticas con `unittest`.

## Cómo ejecutarlo

Abre una terminal en esta carpeta. Requiere Python 3.10 o superior.

```bash
python utilidades.py
```

Ejemplo de sesión:

```
-> convertir euros bitcoins 44471.78
1.0
-> contar hola mundo
4
-> salir
¡Adiós!
```

Comandos del menú:

| Comando | Qué hace |
|---|---|
| `convertir euros bitcoins <cantidad>` | Convierte euros a bitcoins |
| `convertir bitcoins euros <cantidad>` | Convierte bitcoins a euros |
| `contar <texto>` | Cuenta las vocales del texto |
| `temperaturas <t1,t2,...> <umbral>` | Muestra las temperaturas por encima del umbral |
| `productos` | Muestra la lista de productos |
| `productos nuevo <nombre>` | Añade un producto |
| `productos borrar <índice>` | Borra el producto en ese índice |
| `salir` | Termina el programa |

## Tests

```bash
python -m unittest test
```

Hay 10 tests. Dos de ellos (`cifrar` y `descifrar`) son opcionales y se omiten porque no los he implementado. `pruebas.py` es un script de demostración que muestra la salida de cada función.

## Posibles mejoras

- Validar la entrada del menú (ahora un comando mal escrito puede lanzar una excepción).
- Implementar el cifrado y descifrado opcionales.

## Tecnologías

Python 3.12 · `unittest`
