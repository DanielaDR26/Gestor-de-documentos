import os
import shutil

# Crear un directorio principal para almacenar los archivos subidos
directorio_principal = './EspacioColaborativo'
os.makedirs(directorio_principal, exist_ok=True)

def subir_archivos():
    """Función para subir archivos y guardarlos en una carpeta especificada."""
    # Permitir al usuario elegir una carpeta
    nombre_carpeta = input('Ingrese el nombre de la carpeta donde desea guardar los archivos (se creará si no existe): ')
    ruta_carpeta = os.path.join(directorio_principal, nombre_carpeta)
    os.makedirs(ruta_carpeta, exist_ok=True)

    print("Por favor, mueva o copie los archivos que desea subir en la carpeta del directorio actual.")
    archivos = input('Ingrese los nombres de los archivos separados por comas (ejemplo: archivo1.txt, archivo2.csv): ').split(',')

    # Mover archivos a la carpeta especificada
    for nombre_archivo in archivos:
        nombre_archivo = nombre_archivo.strip()  # Eliminar espacios extra
        if os.path.exists(nombre_archivo):
            shutil.move(nombre_archivo, ruta_carpeta)
            print(f'Archivo {nombre_archivo} subido a {ruta_carpeta}')
        else:
            print(f'Archivo {nombre_archivo} no encontrado.')

    print(f"Todos los archivos se han subido exitosamente a la carpeta '{nombre_carpeta}'.")

def listar_archivos():
    """Función para listar todos los archivos en el directorio principal y sus subcarpetas."""
    for root, dirs, files in os.walk(directorio_principal):
        nivel = root.replace(directorio_principal, '').count(os.sep)
        sangria = ' ' * 4 * (nivel)
        print(f'{sangria}{os.path.basename(root)}/')
        sub_sangria = ' ' * 4 * (nivel + 1)
        for f in files:
            print(f'{sub_sangria}{f}')

# Menú principal
def menu_principal():
    while True:
        print("\nMenú del Espacio Colaborativo:")
        print("1. Subir Archivos")
        print("2. Listar Archivos")
        print("3. Salir")
        opcion = input("Ingrese su opción: ")
        
        if opcion == '1':
            subir_archivos()
        elif opcion == '2':
            listar_archivos()
        elif opcion == '3':
            print("Saliendo... ¡Adiós!")
            break
        else:
            print("Opción inválida. Por favor ingrese 1, 2 o 3.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu_principal()
