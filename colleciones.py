# Análisis de frecuencia de palabras en un archivo

from collections import Counter

def leer_archivo(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return archivo.read()

def contar_palabras(texto):
    palabras = texto.lower().split()
    return Counter(palabras)

def mostrar_frecuencia(frecuencias):
    for palabra, frecuencia in frecuencias.items():
        print(f"{palabra}: {frecuencia}")

# Ejemplo de uso
ruta_archivo = 'texto.txt'
texto = leer_archivo(ruta_archivo)
frecuencias = contar_palabras(texto)
mostrar_frecuencia(frecuencias)
