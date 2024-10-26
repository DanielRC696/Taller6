from inventario.operaciones import añadir_producto, actualizar_producto, eliminar_producto, mostrar_inventario


# Función principal que ejecuta el menú
def menu_principal():
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        try:
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                añadir_producto()
            elif opcion == '2':
                actualizar_producto()
            elif opcion == '3':
                eliminar_producto()
            elif opcion == '4':
                mostrar_inventario()
            elif opcion == '5':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")


# Ejecutar el menú principal
if __name__ == "__main__":
    menu_principal()
