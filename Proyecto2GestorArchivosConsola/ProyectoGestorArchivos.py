# https://github.com/Xhinen/Python/tree/main/Proyecto2GestorArchivosConsola
# Importamos los módulos que necesitaremos
import os
from datetime import datetime


# Creamos una función para mostrar el menú principal y la ruta de trabajo actual.

def mostrar_menu():

    print("\n=======================================")
    print("<------ GESTOR DE ARCHIVOS v1.0 ------>")
    print("=======================================")
    try:
        print(f"\nRuta Actual: {os.getcwd()}")
    except Exception as e:
        print(f"\nNo se pudo obtener la ruta actual: {e}")

    print("1. Listar contenido del directorio actual")
    print("2. Crear un nuevo directorio")
    print("3. Crear un archivo de texto")
    print("4. Escribir texto en un archivo existente (añadir)")
    print("5. Eliminar un archivo o directorio")
    print("6. Mostrar información del archivo/directorio")
    print("7. Salir")

def listar_contenido():
    
    # Con esta función vamos a listar el contenido del directorio actual, distinguiendo entre archivos y carpetas.
    
    try:
        print("\n========================================")
        print("<------ CONTENIDO DEL DIRECTORIO ------>")
        print("========================================")
        contenido = os.listdir(".")
        if not contenido:
            print("\nEl directorio está vacío.")
            return

        # Indicamos si es archivo o carpeta en el contenido del directorio que mostramos.
        for i in contenido:
            try:
                if os.path.isdir(i):
                    print(f"[CARPETA] {i}")
                else:
                    print(f"[ARCHIVO] {i}")
            except Exception:
                # Por si puede fallar por enlaces simbólicos rotos, etc.
                print(f"[DESCONOCIDO] {i}")

    except PermissionError:
        print("\nError: No tienes permisos para leer este directorio.")
    except Exception as e:
        print(f"\nError inesperado al listar contenido: {e}")

def crear_directorio():
    
    # Crea un nuevo directorio en la ruta actual. (Similar a ejercicio1.py y ejercicio2.py que hicimos en clase)
    
    print("\n================================")
    print("<------ CREAR DIRECTORIO ------>")
    print("================================")
    nombre_directorio = input("Introduce el nombre del nuevo directorio: ")
    if not nombre_directorio:
        print("\nError: El campo 'nombre' no puede estar vacío.")
        return

    try:
        os.mkdir(nombre_directorio)
        print(f"\nDirectorio '{nombre_directorio}' creado con éxito.")
    except FileExistsError:
        # Manejamos errores de nombre existente y permisos.
        print(f"\nError: El directorio '{nombre_directorio}' ya existe.")
    except PermissionError:
        print("\nError: No tienes permisos para crear un directorio aquí.")
    except Exception as e:
        print(f"\nError inesperado al crear directorio: {e}")

def crear_archivo():
    
    # Vamos crear un nuevo archivo de texto que nos permita escribir contenido en él.
    
    print("\n=============================")
    print("<------ CREAR ARCHIVO ------>")
    print("=============================")
    nombre_archivo = input("Introduce el nombre del nuevo archivo (ej. 'texto.txt'): ")
    if not nombre_archivo:
        print("\nError: El 'nombre' del archivo a crear no puede estar vacío.")
        return

    if os.path.exists(nombre_archivo):
        # Manejamos el error en el caso de que un archivo exista con el mismo nombre.
        print(f"\nError: El archivo con nombre '{nombre_archivo}' ya existe.")
        return

    try:
        # Escribir contenido en el archivo creado.
        contenido = input("Escribe el contenido inicial (deja en blanco si no quieres): ")
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(f"\nArchivo '{nombre_archivo}' creado con éxito.")
    except PermissionError:
        print("\nError: No tienes permisos para crear este archivo aquí.")
    except Exception as e:
        print(f"\nError inesperado al crear el archivo: {e}")

def escribir_en_archivo():
    
    # Añadimos texto a un archivo existente sin sobreescribir el contenido que ya tiene.
    
    print("\n===================================")
    print("<------ ESCRIBIR EN ARCHIVO ------>")
    print("===================================")
    nombre_archivo = input("Introduce el nombre del archivo al que quieres añadir texto: ")

    try:
        # Comprobamos que el archivo existe.
        if not os.path.exists(nombre_archivo):
            print(f"\nError: El archivo '{nombre_archivo}' no existe.")
            return

        # Comprobamos que es un archivo y no un carpeta.
        if os.path.isdir(nombre_archivo):
            print(f"\nError: '{nombre_archivo}' es un directorio, no es un archivo.")
            return

        # Añadimos contenido al archivo (append)
        contenido_archivo = input("Escribe el texto que quieres añadir (se añadirá al final): ")
        with open(nombre_archivo, 'a', encoding='utf-8') as f:
            f.write("\n" + contenido_archivo)
        print(f"\nTexto añadido a '{nombre_archivo}' con éxito.")

    except PermissionError:
        print(f"\nError: No tienes permisos para escribir en '{nombre_archivo}'.")
    except Exception as e:
        print(f"\nError inesperado al escribir en el archivo: {e}")

def eliminar_elemento():
    
    # Elimina un archivo o un directorio (solo si está vacío). (ejercicio3.py del 29 de octubre)

    print("\n==========================================")
    print("<------ ELIMINAR ARCHIVO O CARPETA ------>")
    print("==========================================")
    archivo_nombre = input("Introduce el nombre del archivo o directorio a eliminar: ")

    try:
        # Comprobamos si el archivo existe.
        if not os.path.exists(archivo_nombre):
            print(f"Error: '{archivo_nombre}' no existe.")
            return

        if os.path.isdir(archivo_nombre):
            # Si es un directorio usaremos "rmdir".
            os.rmdir(archivo_nombre)
            print(f"Directorio '{archivo_nombre}' eliminado con éxito.")
        else:
            # Si es un archivo usaremos "remove".
            os.remove(archivo_nombre)
            print(f"Archivo '{archivo_nombre}' eliminado con éxito.")

    except PermissionError:
        print(f"Error: No tienes permisos para eliminar '{archivo_nombre}'.")
    except OSError as e:
        # OSError se lanzará si el directorio no está vacío.
        print(f"Error: No se pudo eliminar '{archivo_nombre}'. ¿Quizás el directorio no está vacío? ({e})")
    except Exception as e:
        print(f"Error inesperado al eliminar: {e}")

def mostrar_informacion():
    
    # Muestra el tipo (archivo/carpeta), tamaño y fecha de última modificación.
    
    print("\n===================================")
    print("<------ MOSTRAR INFORMACIÓN ------>")
    print("===================================")
    nombre = input("Introduce el nombre del archivo o directorio: ")

    try:
        # Comprobamos si existe.
        if not os.path.exists(nombre):
            print(f"Error: '{nombre}' no existe.")
            return

        # Obtenemos estadísticas del archivo/directorio.
        stat = os.stat(nombre)

        # Mostramos el tipo de archivo.
        tipo = "Carpeta" if os.path.isdir(nombre) else "Archivo"

        # Mostramos el tamaño.
        tamaño = stat.st_size # Esto es para mostrarlo en bytes.

        # Mostramos la fecha de modificación.
        mod_time_stamp = stat.st_mtime
        mod_fecha = datetime.fromtimestamp(mod_time_stamp).strftime('%Y-%m-%d %H:%M:%S')

        print(f"\n--- Información de '{nombre}' ---")
        print(f"  Tipo: {tipo}")
        print(f"  Tamaño: {tamaño} bytes")
        print(f"  Última modificación: {mod_fecha}")

    except PermissionError:
        print(f"Error: No tienes permisos para ver la información de '{nombre}'.")
    except Exception as e:
        print(f"Error inesperado al obtener información: {e}")

def main():
    
    # Bucle while del programa principal, lo he cogido del ejercicio1.py del tema UT4 Funciones y Módulos (12 de junio)
    
    elegir_opcion = 0
    while elegir_opcion != 7:
        mostrar_menu()

        try:
            opcion = input("Escoge una opción (1-7): ")
            # Evitamos errores si en el input no se introduce nada.
            if not opcion:
                continue
            elegir_opcion = int(opcion)
        except ValueError:
            # Gestionamos errores de entrada que no sean números.
            print("\nError: Debes introducir un número del 1 al 7.")
            continue

        if elegir_opcion == 1:
            listar_contenido()
        elif elegir_opcion == 2:
            crear_directorio()
        elif elegir_opcion == 3:
            crear_archivo()
        elif elegir_opcion == 4:
            escribir_en_archivo()
        elif elegir_opcion == 5:
            eliminar_elemento()
        elif elegir_opcion == 6:
            mostrar_informacion()
        elif elegir_opcion == 7:
            print("\nSaliendo del gestor de archivos. ¡Hasta luego Lucas!")
        else:
            # Gestionamos errores de opciones no válidas.
            print("\nOpción no válida. Por favor, introduce un número del 1 al 7.")

if __name__ == '__main__':
    main()