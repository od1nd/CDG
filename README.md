# CDG (Custo Dictionary Generator)

CDG (Custom Dictionary Generator) es una herramienta escrita en Python para generar diccionarios personalizados a partir de palabras específicas. Es ideal para preubas de pentesting y permite generar listas de palabras que se pueden utilizar para detectar y explotar vulnerabilidades en sistemas y aplicaciones.

## Características

- **Generación de Diccionarios:** Crea diccionarios personalizados a partir de una lista de palabras.

- **Permutaciones:** Calcula todas las permutaciones posibles de las palabras ingresadas

- **Salida en Archivo:** Guarda las permutaciones generadas en un archivo de texto.

## Requisitos
- Python 3.10 o superior

## Instalación

Clona el repositorio o descar el archivo ZIP y descomprimelo:

```
git clone https://github.com/od1nd/CDG

cd CDG

```

## Uso

Ejecuta el programa desde la línea de comandos con los argumentos necesarios:

```
python cdg.py -a palabra1 palabra2 palabra3 -o nombre_del_archivo.txt
```

## Argumentos

- *-a*, *--add*: Agrega palabras al diccionario (lista de palabras separadas por espacio.)
- *-o*, *--output*: Nombre del archivo de salida donde se guardarán las pemutaciones.

### Ejemplo

```
python cdg.py -a 1 2 3 4 5 -o diccionario.txt
```

## Funcionamiento Interno

1. **Permutations:** La función *permutations* calcula el número de permutaciones posibles de la lista de palabras.

2. **Output:** La función *output* guarda las palabras en el archivo especificado.

3. **Generate:** La función *generate* genera todas las permutaciones posibles y las guarda en el archivo de salida.

## Ejecución del Programa

Al ejecutar el program, este calculará el número de permutaciones, generará todas las permutaciones posibles y las guardará en el archivo específicado. También mostrará el tiempo de ejecución del proceso.

## Contribuciones

Las contribucioens son bienvenidas. Por favor, abre un issue o envía un pull request con tus sugerencias y mejoras.

## Fuentes

- [Algoritmo de Heap](https://es.wikipedia.org/wiki/Algoritmo_de_Heap)


