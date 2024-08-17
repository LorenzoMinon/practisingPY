# Función lambda que suma dos números
suma = lambda a, b: a + b
print(suma(5, 3))  # Salida: 8

# Lista de diccionarios
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Juan", "edad": 20}
]

# Ordenar la lista por edad usando una función lambda
personas_ordenadas = sorted(personas, key=lambda x: x["edad"], reverse=True)
print(personas_ordenadas)
# Salida: [{'nombre': 'Juan', 'edad': 20}, {'nombre': 'Ana', 'edad': 25}, {'nombre': 'Luis', 'edad': 30}]


def decorador(func):
    def envoltura():
        print("Antes de ejecutar la función")
        func()
        print("Después de ejecutar la función")
    return envoltura

@decorador
def decir_hola():
    print("¡Hola!")

decir_hola()
# Salida:
# Antes de ejecutar la función
# ¡Hola!
# Después de ejecutar la función

import time

def medir_tiempo(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
        return resultado
    return envoltura

@medir_tiempo
def funcion_lenta():
    time.sleep(2)
    print("Función lenta ejecutada")

# Ejemplo de uso
funcion_lenta()
# Salida:
# Función lenta ejecutada
# Tiempo de ejecución: 2.0020 segundos


## Generadores

def contador(n):
    while n > 0:
        yield n
        n -= 1

# Ejemplo de uso
for numero in contador(5):
    print(numero)
# Salida:
# 5
# 4
# 3
# 2
# 1


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def generador_primos():
    numero = 2
    while True:
        if es_primo(numero):
            yield numero
        numero += 1

# Ejemplo de uso
primos = generador_primos()
for _ in range(10):
    print(next(primos))
# Salida (los primeros 10 números primos):
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29

