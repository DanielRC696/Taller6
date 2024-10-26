from utils.utils import cargar_inventario, guardar_inventario
# Añadir un nuevo producto al inventario
def añadir_producto():
    inventario = cargar_inventario()
    nombre = input("Ingrese el nombre del producto: ")

    if nombre in inventario:
        print("El producto ya existe en el inventario.")
        return

    try:
        cantidad = int(input("Ingrese la cantidad disponible: "))
        precio = float(input("Ingrese el precio unitario: "))
    except ValueError:
        print("Error: La cantidad y el precio deben ser numéricos.")
        return

    inventario[nombre] = {"cantidad": cantidad, "precio": precio}
    guardar_inventario(inventario)
    print(f"Producto {nombre} añadido con éxito.")

# Actualizar un producto existente
def actualizar_producto():
    inventario = cargar_inventario()
    nombre = input("Ingrese el nombre del producto a actualizar: ")

    if nombre not in inventario:
        print("El producto no existe en el inventario.")
        return

    try:
        cantidad = int(input(f"Ingrese la nueva cantidad para {nombre}: "))
        precio = float(input(f"Ingrese el nuevo precio para {nombre}: "))
    except ValueError:
        print("Error: La cantidad y el precio deben ser numéricos.")
        return

    inventario[nombre]["cantidad"] = cantidad
    inventario[nombre]["precio"] = precio
    guardar_inventario(inventario)
    print(f"Producto {nombre} actualizado con éxito.")

# Eliminar un producto del inventario
def eliminar_producto():
    inventario = cargar_inventario()
    nombre = input("Ingrese el nombre del producto a eliminar: ")

    if nombre not in inventario:
        print("El producto no existe en el inventario.")
        return

    try:
        del inventario[nombre]
        guardar_inventario(inventario)
        print(f"Producto {nombre} eliminado con éxito.")
    except Exception as e:
        print(f"Error al eliminar el producto: {e}")

# Mostrar todos los productos del inventario
def mostrar_inventario():
    inventario = cargar_inventario()

    if not inventario:
        print("El inventario está vacío.")
        return

    try:
        print("\n--- Inventario de Productos ---")
        for nombre, detalles in inventario.items():
            cantidad = detalles["cantidad"]
            precio = detalles["precio"]
            print(f"Producto: {nombre}, Cantidad: {cantidad}, Precio: {precio}")
    except Exception as e:
        print(f"Error al mostrar el inventario: {e}")
