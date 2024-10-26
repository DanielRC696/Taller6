import json
import os

# Ruta del archivo JSON dentro de la carpeta data
RUTA_ARCHIVO = os.path.join('data', 'inventory.json')

# Cargar el inventario desde el archivo JSON
def cargar_inventario():
    try:
        if os.path.exists(RUTA_ARCHIVO):
            with open(RUTA_ARCHIVO, 'r') as archivo:
                return json.load(archivo)
        else:
            return {}  # Si el archivo no existe, retorna un diccionario vacío
    except json.JSONDecodeError:
        print("Error: El archivo de inventario está corrupto o no es un JSON válido.")
        return {}
    except Exception as e:
        print(f"Error al cargar el inventario: {e}")
        return {}

# Guardar el inventario en el archivo JSON
def guardar_inventario(inventario):
    try:
        os.makedirs(os.path.dirname(RUTA_ARCHIVO), exist_ok=True)  # Crear carpeta 'data' si no existe
        with open(RUTA_ARCHIVO, 'w') as archivo:
            json.dump(inventario, archivo, indent=4)
    except Exception as e:
        print(f"Error al guardar el inventario: {e}")
