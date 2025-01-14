import os
import shutil
import pandas as pd
import streamlit as st
from PIL import Image

# Directorio principal
directorio_principal = './EspacioColaborativo'
os.makedirs(directorio_principal, exist_ok=True)

def mostrar_archivos(directorio):
    # Verificar si el directorio existe antes de intentar listar los archivos
    if not os.path.exists(directorio):
        st.warning(f"El directorio '{directorio}' no existe.")
        return
    
    # Obtener lista de archivos en el directorio
    archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]
    
    # Mostrar los archivos
    if archivos:
        archivo_seleccionado = st.selectbox("Seleccione un archivo para ver o descargar", archivos)
        # Botón para descargar el archivo seleccionado
        if st.button(f"Ver/Descargar {archivo_seleccionado}"):
            with open(os.path.join(directorio, archivo_seleccionado), "rb") as file:
                st.download_button(label="Descargar", data=file, file_name=archivo_seleccionado, mime="application/octet-stream")
    else:
        st.warning("No se encontraron archivos en este directorio.")

# Función para subir archivos (Documentos)
def subir_archivos(carpeta_destino):
    # Definir la carpeta donde se guardarán los archivos según la subpágina
    ruta_carpeta = os.path.join(directorio_principal, carpeta_destino)
    
    # Crear el directorio si no existe
    os.makedirs(ruta_carpeta, exist_ok=True)
    
    # Subir archivos
    archivos = st.file_uploader("Seleccione los archivos para subir", accept_multiple_files=True)
    
    if archivos:
        for archivo in archivos:
            # Guardar cada archivo en la carpeta especificada
            ruta_archivo = os.path.join(ruta_carpeta, archivo.name)
            with open(ruta_archivo, "wb") as f:
                f.write(archivo.getbuffer())
            st.success(f'Archivo {archivo.name} subido exitosamente a {ruta_carpeta}')
    else:
        st.warning("No se ha seleccionado ningún archivo para subir.")

# Función para borrar archivo
def borrar_archivo(directorio):
    # Pedir al usuario que ingrese la contraseña
    contrasena = st.text_input("Ingrese la contraseña para borrar el archivo:", type="password")
    
    if contrasena == "miContraseñaSegura":
        archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]
        if archivos:
            archivo_seleccionado = st.selectbox("Seleccione un archivo para borrar", archivos)
            if st.button(f"Borrar archivo: {archivo_seleccionado}"):
                try:
                    os.remove(os.path.join(directorio, archivo_seleccionado))
                    st.success(f"Archivo '{archivo_seleccionado}' borrado con éxito.")
                except Exception as e:
                    st.error(f"No se pudo borrar el archivo. Error: {e}")
        else:
            st.warning("No 
