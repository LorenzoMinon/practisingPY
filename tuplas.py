# Crear una tupla
coordenadas = (10.5, 20.3)

# Acceder a elementos
print(coordenadas)  # Salida: 10.5

# Intentar modificar una tupla (esto causará un error)
# coordenadas[0] = 15.0  # Error: las tuplas no permiten la asignación de elementos

# Tuplas de coordenadas geográficas

lugar = ("Eiffel Tower", 48.8584, 2.2945)

def mostrar_coordenadas(lugar):
    nombre, latitud, longitud = lugar
    print(f"Lugar: {nombre}")
    print(f"Latitud: {latitud}")
    print(f"Longitud: {longitud}")

# Ejemplo de uso
mostrar_coordenadas(lugar)



# Crear un diccionario
contacto = {
    "nombre": "Juan",
    "telefono": "123456789",
    "email": "juan@example.com"
}

# Acceder a un valor
print(contacto["nombre"])  # Salida: Juan

# Modificar un valor
contacto["telefono"] = "987654321"
print(contacto["telefono"])  # Salida: 987654321

# Añadir un nuevo par clave-valor
contacto["direccion"] = "Calle Falsa 123"
print(contacto)  # Salida: {..., "direccion": "Calle Falsa 123"}

# Eliminar un par clave-valor
del contacto["email"]
print(contacto)  # Salida: {..., "direccion": "Calle Falsa 123"}


# Sistema de gestión de contactos

contactos = {}

def agregar_contacto(nombre, telefono, email):
    contactos[nombre] = {
        "telefono": telefono,
        "email": email
    }
    print(f"Contacto '{nombre}' agregado.")

def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print(f"Contacto '{nombre}' no encontrado.")

def mostrar_contactos():
    if contactos:
        print("Lista de contactos:")
        for nombre, info in contactos.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info['telefono']}")
            print(f"Email: {info['email']}\n")
    else:
        print("No hay contactos.")

# Ejemplo de uso
agregar_contacto("Ana", "123456789", "ana@example.com")
agregar_contacto("Luis", "987654321", "luis@example.com")
mostrar_contactos()

# eliminar_contacto("Ana")
mostrar_contactos()


# Crear un set
frutas = {"manzana", "banana", "cereza"}

# Añadir un elemento
frutas.add("naranja")
print(frutas)  # Salida: {"manzana", "banana", "cereza", "naranja"}

# Intentar añadir un duplicado (no se añadirá)
frutas.add("manzana")
print(frutas)  # Salida: {"manzana", "banana", "cereza", "naranja"}

# Eliminar un elemento
frutas.remove("banana")
print(frutas)  # Salida: {"manzana", "cereza", "naranja"}

# Intersección de dos listas

def interseccion(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    return list(set1.intersection(set2))

# Ejemplo de uso
lista1 = ["manzana", "pera", "naranja"]
lista2 = ["banana", "naranja", "pera"]

resultado = interseccion(lista1, lista2)
print("Elementos comunes:", resultado)  # Salida: ["pera", "naranja"]

