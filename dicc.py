# Gestión de inventario

def agregar_producto(inventario, producto, cantidad):
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad

def mostrar_inventario(inventario):
    print("Inventario actual:")
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad}")

def vender_producto(inventario, producto, cantidad):
    if producto in inventario and inventario[producto] >= cantidad:
        inventario[producto] -= cantidad
        if inventario[producto] == 0:
            del inventario[producto]
        print(f"Se vendieron {cantidad} unidades de {producto}")
    else:
        print(f"No hay suficiente stock de {producto}")

# Ejemplo de uso
inventario = {}

agregar_producto(inventario, 'Manzanas', 50)
agregar_producto(inventario, 'Peras', 30)
agregar_producto(inventario, 'Manzanas', 20)
mostrar_inventario(inventario)

vender_producto(inventario, 'Manzanas', 60)
mostrar_inventario(inventario)

vender_producto(inventario, 'Peras', 15)
mostrar_inventario(inventario)
