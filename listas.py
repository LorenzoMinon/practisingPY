# Crear una lista
frutas = ["manzana", "banana", "cereza"]

# Acceder a elementos
print(frutas[0])  # Salida: manzana

# Modificar elementos
frutas[1] = "pera"
print(frutas)  # Salida: ["manzana", "pera", "cereza"]

# Añadir elementos
frutas.append("naranja")
print(frutas)  # Salida: ["manzana", "pera", "cereza", "naranja"]

# Eliminar elementos
frutas.remove("pera")
print(frutas)  # Salida: ["manzana", "cereza", "naranja"]

# Longitud de la lista
cantidad_frutas = len(frutas)  # Salida: 3

print (f"Longitud total, es decir cantidad de frutas = {cantidad_frutas}")


# Gestión de lista de tareas

tareas = []

def agregar_tarea(tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

def eliminar_tarea(tarea):
    if tarea in tareas:
        tareas.remove(tarea)
        print(f"Tarea '{tarea}' eliminada.")
    else:
        print(f"Tarea '{tarea}' no encontrada.")

def mostrar_tareas():
    if tareas:
        print("Tareas pendientes:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas pendientes.")

# Ejemplo de uso
agregar_tarea("Estudiar Python")
agregar_tarea("Hacer ejercicio")
mostrar_tareas()

eliminar_tarea("Estudiar Python")
mostrar_tareas()

print(len(tareas))
