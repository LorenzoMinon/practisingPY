#Decoradores avanzados 

# **¿Qué son *args y kwargs?

# *args: Permite pasar un número variable de argumentos posicionales a una función. Estos argumentos se empaquetan en una tupla dentro de la función.
# **kwargs: Permite pasar un número variable de argumentos de palabras clave (nombre=valor) a una función.
#  Estos argumentos se empaquetan en un diccionario dentro de la función.

def decorador_1(func):
    def envoltura_1(*args, **kwargs):
        print("Ejecutando decorador_1")
        return func(*args, **kwargs)
    return envoltura_1

def decorador_2(func):
    def envoltura_2(*args, **kwargs):
        print("Ejecutando decorador_2")
        return func(*args, **kwargs)
    return envoltura_2

@decorador_1
@decorador_2
def mi_funcion():
    print("Función original ejecutada")

# Ejemplo de uso
mi_funcion()
# Salida:
# Ejecutando decorador_1
# Ejecutando decorador_2
# Función original ejecutada


#Con argumentos: 
def repetir_veces(n):
    def decorador(func):
        def envoltura(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return envoltura
    return decorador

@repetir_veces(3)
def saludar():
    print("¡Hola!")

# Ejemplo de uso
saludar()
# Salida:
# ¡Hola!
# ¡Hola!
# ¡Hola!


#Generadores avanzados

def generador_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Ejemplo de uso
fibonacci = generador_fibonacci()
for _ in range(10):
    print(next(fibonacci))
# Salida (los primeros 10 números de Fibonacci):
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
