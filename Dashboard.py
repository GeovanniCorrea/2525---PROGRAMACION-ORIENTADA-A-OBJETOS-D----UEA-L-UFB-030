import os
import subprocess  # ya está, pero asegúrate de que ambos estén al inicio

"""
Archivo: dashboard.py
Descripción: Script que permite visualizar y ejecutar el contenido de diferentes scripts organizados por unidades temáticas.
El usuario puede seleccionar una opción del menú para ver el código fuente de un archivo específico o ejecutarlo.
...
"""

def mostrar_codigo(ruta_script):
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
    return {k: v for k, v in opciones.items() if palabra_clave.lower() in v.lower()}

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'UNIDAD 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py',
        '2': 'UNIDAD 1/1.3. Algoritmos/1.3.1. Introduccion a Algoritmos.py',
        '3': 'UNIDAD 1/1.4. Variables/1.4.1. Tipos de Datos.py',
        '4': 'UNIDAD 2/1.1. Tipos de Datos e Identificadores/Semana 05.py',
        '5': 'UNIDAD 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/Semana 06.py',
        '6': 'UNIDAD 2/2.1. Constructores y Destructores.py',
    }

    nombres_opciones = {
        '1': 'Ejemplo Técnicas de Programación',
        '2': 'Introducción a Algoritmos',
        '3': 'Tipos de Datos',
        '4': 'Tipos de Datos e Identificadores',
        '5': 'Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo',
        '6': 'Constructores y Destructores'
    }

    while True:
        print("\n📘 Menu Principal - Dashboard")
        for unidad, keys in [('UNIDAD 1', ['1', '2', '3']), ('UNIDAD 2', ['4', '5', '6'])]:
            print(f"\n{unidad}:")
            for key in keys:
                print(f"{key} - {nombres_opciones[key]}")
        print("\n7 - Buscar script por palabra clave")
        print("0 - Salir")

        elec = input("\nElige una opción: ")
        if elec == '0':
            print("👋 Saliendo... ¡Hasta luego!")
            break
        elif elec == '7':
            clave = input("🔍 Palabra clave: ")
            res = buscar_scripts(clave, opciones)
            if res:
                print("🔍 Resultados:")
                for k, v in res.items():
                    print(f"{k} - {nombres_opciones.get(k, 'Sin nombre')} ({v})")
            else:
                print("⚠️ No se encontraron scripts.")
        elif elec in opciones:
            ruta = os.path.join(ruta_base, opciones[elec])
            accion = input("¿Ver código (v) o Ejecutar (e)? ").lower()
            if accion == 'v':
                mostrar_codigo(ruta)
            elif accion == 'e':
                ejecutar_script(ruta)
            else:
                print("⚠️ Opción no válida.")
        else:
            print("⚠️ Opción no válida.")

if __name__ == "__main__":
    mostrar_menu()
