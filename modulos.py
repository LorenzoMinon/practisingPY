# Suponiendo que tienes un archivo llamado "mi_modulo.py" con el siguiente contenido:

# mi_modulo.py
def saludar(nombre):
    return f"Hola, {nombre}!"

# En otro archivo, puedes importar y usar este módulo:
import mi_modulo

print(mi_modulo.saludar("Juan"))  # Salida: Hola, Juan!


# Importar elementos de un modulo

from mi_modulo import saludar

print(saludar("Ana"))  # Salida: Hola, Ana!

import mi_modulo as mod

print(mod.saludar("Luis"))  # Salida: Hola, Luis!

from mi_modulo import saludar as saludo

print(saludo("Maria"))  # Salida: Hola, Maria!


import math

print(math.sqrt(16))  # Salida: 4.0

import random

print(random.randint(1, 10))  # Salida: Un número aleatorio entre 1 y 10

import datetime

ahora = datetime.datetime.now()
print(ahora)  # Salida: Fecha y hora actual
