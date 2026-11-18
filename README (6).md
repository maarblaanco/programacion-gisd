# Programación · GISD (ETSIT-UPM)

Proyectos de la asignatura **Programación** del primer curso del Grado en Ingeniería de Sistemas de Datos (ETSIT, Universidad Politécnica de Madrid). Los tres están hechos en Python, tienen tests automáticos con `unittest` y se ejecutan por consola.

| Carpeta | Qué es | Qué practica |
|---|---|---|
| [`01-utilidades`](./01-utilidades) | Funciones de utilidad (divisas, texto, temperaturas, lista de productos) y menú interactivo | Funciones, bucles, listas, cadenas, tests |
| [`02-lista-compra`](./02-lista-compra) | Gestor de lista de la compra, en una versión con funciones y otra con clases | Diccionarios, programación orientada a objetos, ordenación |
| [`03-asistente-habilidades`](./03-asistente-habilidades) | Asistente de consola con habilidades y menús intercambiables | Herencia, polimorfismo, diseño con clases |

## Cómo ejecutar un proyecto

Requiere Python 3.10 o superior. Cada proyecto se ejecuta desde su propia carpeta; el README de cada una explica cómo.

```bash
cd 01-utilidades
python utilidades.py
python -m unittest test
```

## Tecnologías

Python 3.12 · `unittest`
