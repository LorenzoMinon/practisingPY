# El proyecto consistirá en:

# Generador de flujo de números: Generará números aleatorios en tiempo real.
# Decoradores: Aplicarán operaciones como filtrado (solo números pares), registro de tiempo, y acumulación de estadísticas.
# Acumulador: Mantendrá un estado interno para calcular el promedio de los últimos n números procesados.

import random

def generador_numeros(min_valor, max_valor):
    while True:
        yield random.randint(min_valor, max_valor)

# Ejemplo de uso
flujo = generador_numeros(1, 100)
for _ in range(5):
    print(next(flujo))

import time

# Decorador para filtrar solo números pares
def filtrar_pares(func):
    def envoltura(*args, **kwargs):
        numero = func(*args, **kwargs)
        if numero % 2 == 0:
            return numero
        return None
    return envoltura

# Decorador para registrar el tiempo de procesamiento
def registrar_tiempo(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        if resultado is not None:
            print(f"Procesado en {fin - inicio:.4f} segundos")
        return resultado
    return envoltura



def acumulador_promedio(n):
    acumulador = []
    while True:
        nuevo_valor = yield sum(acumulador[-n:]) / len(acumulador[-n:]) if acumulador else None
        acumulador.append(nuevo_valor)

# Ejemplo de uso
acumulador = acumulador_promedio(5)
next(acumulador)  # Inicializar el generador
print(acumulador.send(10))  # Salida: 10.0
print(acumulador.send(20))  # Salida: 15.0
print(acumulador.send(30))  # Salida: 20.0


@filtrar_pares
@registrar_tiempo
def generar_numero(flujo):
    return next(flujo)

# Generador de números aleatorios
flujo = generador_numeros(1, 100)

# Acumulador de promedio de los últimos 5 números
acumulador = acumulador_promedio(5)
next(acumulador)  # Inicializar el generador

# Proceso de flujo de datos
for _ in range(10):
    numero = generar_numero(flujo)
    if numero is not None:
        promedio = acumulador.send(numero)
        if promedio is not None:
            print(f"Número: {numero}, Promedio de los últimos 5: {promedio:.2f}")
