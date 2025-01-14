import os
import shutil
import pandas as pd
import streamlit as st
from PIL import Image

# Contraseña de protección (puedes cambiarla por una más segura)
PASSWORD = "miContraseñaSegura"

# Función para borrar archivo
def borrar_archivo(directorio, archivo_seleccionado):
    # Pedir al usuario que ingrese la contraseña
    contrasena = st.text_input("Ingrese la contraseña para borrar el archivo:", type="password")
    
    if contrasena == PASSWORD:
        # Borrar el archivo seleccionado
        try:
            os.remove(os.path.join(directorio, archivo_seleccionado))
            st.success(f"Archivo '{archivo_seleccionado}' borrado con éxito.")
        except Exception as e:
            st.error(f"No se pudo borrar el archivo. Error: {e}")
    else:
        if contrasena:
            st.error("Contraseña incorrecta. Intente nuevamente.")

# Función para listar archivos (Documentos)
def listar_archivos(carpeta_destino):
    ruta_carpeta = os.path.join(directorio_principal, carpeta_destino)
    
    if os.path.exists(ruta_carpeta):
        st.subheader(f"Archivos en {carpeta_destino}:")
        for root, dirs, files in os.walk(ruta_carpeta):
            nivel = root.replace(ruta_carpeta, '').count(os.sep)
            sangria = ' ' * 4 * (nivel)
            st.write(f'{sangria}{os.path.basename(root)}/')
            sub_sangria = ' ' * 4 * (nivel + 1)
            for f in files:
                ruta_completa = os.path.join(root, f)
                st.write(f'{sub_sangria}{f}')
                
                # Agregar botón para descarga
                with open(ruta_completa, "rb") as file:
                    btn = st.download_button(
                        label=f"Descargar {f}",
                        data=file,
                        file_name=f,
                        mime="application/octet-stream"
                    )
                
                # Agregar un ícono para borrar el archivo
                if st.button(f"🗑️ Borrar {f}", key=f"{root}-{f}"):
                    borrar_archivo(root, f)
    else:
        st.warning(f"No existen archivos en {carpeta_destino}.")

# Función para mostrar el menú principal
def menu_principal():
    # Opciones del menú en la barra lateral
    opcion = st.sidebar.radio("Seleccione una sección:", ["Menú Principal", "Normatividad", "Estadísticas", "Documentos"])
    
    # Mostrar contenido según la opción seleccionada
    if opcion == "Menú Principal":
        mostrar_menu_principal()  # Mostrar la sección principal
    elif opcion == "Normatividad":
        mostrar_normatividad()  # Mostrar la sección de Normatividad
    elif opcion == "Estadísticas":
        mostrar_estadisticas()  # Mostrar la sección de Estadísticas
    elif opcion == "Documentos":
        mostrar_documentos()  # Mostrar la sección de Documentos

# Función para mostrar la sección de Normatividad
def mostrar_normatividad():
    st.title("Normatividad")
    st.write("Aquí podrás ver los documentos relacionados con la normatividad.")
    # Agrega contenido específico para la sección de normatividad
    subir_archivos('normatividad')
    listar_archivos('normatividad')

# Función para mostrar la sección de Estadísticas
def mostrar_estadisticas():
    st.title("Estadísticas")
    st.write("Aquí podrás ver los documentos y gráficos relacionados con estadísticas.")
    # Agrega contenido específico para la sección de estadísticas
    subir_archivos('estadisticas')
    listar_archivos('estadisticas')

# Función para mostrar la sección de Documentos
def mostrar_documentos():
    st.title("Documentos")
    st.write("Aquí podrás ver los documentos subidos y gestionados.")
    # Agrega contenido específico para la sección de documentos
    subir_archivos('Documentos')
    listar_archivos('Documentos')

# Llamar la función principal para ejecutar la app
if __name__ == "__main__":
    menu_principal()

