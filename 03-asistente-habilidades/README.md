# Asistente de habilidades en Python

Pequeño asistente de consola cuyas funcionalidades ("habilidades") son clases que se registran en un menú. Está pensado para practicar **programación orientada a objetos**: herencia, sobrescritura de métodos y polimorfismo. Proyecto de la asignatura **Programación** (1.º, Grado en Ingeniería y Sistemas de Datos, ETSIT-UPM).

## Diseño

- `Habilidad`: clase base con un nombre, una descripción y los métodos `invocar` y `ayuda`.
- `Divisas`: conversión entre divisas con una tasa configurable.
- `HabilidadSubcomandos`: habilidad que ofrece varios subcomandos (`insertar`, `borrar`...).
- `ListaDeLaCompra` y `ListaCompraP2`: listas de la compra basadas en subcomandos (la segunda, con precio, categoría, etiquetas, prioridad y ordenación).
- `Contador` (vocales) y `DetectorPalindromos`: habilidades de texto.
- `Menu`: bucle interactivo que ejecuta habilidades y muestra ayuda. Tiene tres variantes por herencia:
  - `MenuComas`: comando y argumentos separados por comas.
  - `MenuPrompt`: símbolo de entrada configurable.
  - `MenuPreguntas`: pide el comando y después los argumentos uno a uno.

## Cómo ejecutarlo

Abre una terminal en esta carpeta. Requiere Python 3.10 o superior.

```bash
python habilidades.py
```

Ejemplo:

```
> ayuda
Habilidades disponibles:
	bitcoin2euro:	Conversión de bitcoins a euros
	euro2bitcoin:	Conversión de euros a bitcoins
	contador:	Contador de vocales en un texto.
	detector_palindromos:	Detector de palíndromos.
	listacomprap2:	Gestión avanzada de la lista de la compra.
> bitcoin2euro 1
49929.38
> contador murcielago
Número de vocales: 5
> listacomprap2 insertar Pan 1.2 Comida horneado 2
Producto "Pan" añadido a la lista.
> listacomprap2 mostrar
[ ] Comida - Pan - ** - 1.2 € - #horneado
> salir
Adiós
```

Para probar los otros menús:

```bash
python -c "from habilidades import ejecutar_menu_comas; ejecutar_menu_comas()"
python -c "from habilidades import ejecutar_menu_prompt; ejecutar_menu_prompt()"
python -c "from habilidades import ejecutar_menu_preguntas; ejecutar_menu_preguntas()"
```

## Tests

```bash
python -m unittest test
```

Los 8 tests comprueban las habilidades, los tres menús y los subcomandos.

## Posibles mejoras

- Gestionar los errores de entrada en las habilidades (argumentos que faltan o con formato incorrecto).
- Evitar el código repetido entre las funciones `ejecutar_menu_*`.

## Tecnologías

Python 3.12 · `unittest`
