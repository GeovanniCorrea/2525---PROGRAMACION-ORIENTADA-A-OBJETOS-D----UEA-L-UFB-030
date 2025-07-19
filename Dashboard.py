import os
import subprocess

"""
Archivo: dashboard.py
Descripción: Script que permite visualizar y ejecutar el contenido de diferentes scripts organizados por unidades temáticas.
El usuario puede seleccionar una opción del menú para ver el código fuente de un archivo específico o ejecutarlo.

Cambios realizados:
- Se organizó el menú por unidades temáticas.
- Se agregaron rutas relativas a los archivos.
- Se implementaron funciones con manejo de errores.
- Se mejoró la interfaz del menú con nombres descriptivos.
- Se documentó el código con comentarios explicativos.
"""

def mostrar_codigo(ruta_script):
    """
    Abre y muestra el contenido del archivo Python especificado.
    Parámetros:
    ruta_script (str): Ruta absoluta del archivo a mostrar.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("❌ El archivo no se encontró.")
    except Exception as e:
        print(f"❌ Ocurrió un error al leer el archivo: {e}")

def ejecutar_script(ruta_script):
    """
    Ejecuta el script Python especificado.
    Parámetros:
    ruta_script (str): Ruta absoluta del archivo a ejecutar.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        print(f"\n▶️ Ejecutando {ruta_script}...\n")
        subprocess.run(['python', ruta_script_absoluta], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al ejecutar el script: {e}")
    except FileNotFoundError:
        print("❌ El archivo no se encontró.")
    except Exception as e:
        print(f"❌ Ocurrió un error al ejecutar el archivo: {e}")

def buscar_scripts(palabra_clave, opciones):
    """
    Busca scripts que contengan una palabra clave en su nombre o descripción.
    Parámetros:
    palabra_clave (str): Palabra clave para buscar.
    opciones (dict): Diccionario con las rutas relativas de los scripts.
    """
    resultados = {key: value for key, value in opciones.items() if palabra_clave.lower() in value.lower()}
    return resultados

def mostrar_menu():
    """
    Muestra el menú de opciones y permite al usuario elegir un archivo para ver su
