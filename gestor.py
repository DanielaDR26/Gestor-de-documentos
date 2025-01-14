import os
import shutil
import pandas as pd
import streamlit as st

# Crear un directorio principal para almacenar los archivos subidos
directorio_principal = './EspacioColaborativo'
os.makedirs(directorio_principal, exist_ok=True)

# Función para subir archivos (Documentos)
def subir_archivos(carpeta_destino):
    # Definir la carpeta donde se guardarán los archivos según la subpágina
    ruta_carpeta = os.path.join(directorio_principal, carpeta_destino)
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

# Función para listar archivos (Documentos)
def listar_archivos(carpeta_destino):
    ruta_carpeta = os.path.join(directorio_principal, carpeta_destino)
    
    if os.path.exists(ruta_carpeta):
       


