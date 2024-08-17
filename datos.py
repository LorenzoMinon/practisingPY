import csv

# Leer un archivo CSV
with open('datos.csv', mode='r') as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        print(fila)  # Cada fila es una lista de valores


import csv

# Datos a escribir en el archivo CSV
datos = [
    ["Nombre", "Edad", "Ciudad"],
    ["Juan", 30, "Madrid"],
    ["Ana", 25, "Barcelona"],
    ["Luis", 35, "Valencia"]
]

# Escribir en un archivo CSV
with open('datos.csv', mode='w', newline='') as archivo:
    escritor_csv = csv.writer(archivo)
    escritor_csv.writerows(datos)


import json

# Leer un archivo JSON
with open('datos.json', mode='r') as archivo:
    datos = json.load(archivo)
    print(datos)  # Los datos se cargan como un diccionario de Python

