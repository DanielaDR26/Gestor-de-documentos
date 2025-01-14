import os
import shutil
import streamlit as st

# Crear un directorio principal para almacenar los archivos subidos
directorio_principal = './EspacioColaborativo'
os.makedirs(directorio_principal, exist_ok=True)

# Función para subir archivos (Documentos)
def subir_archivos():
    nombre_carpeta = st.text_input('Ingrese el nombre de la carpeta donde desea guardar los archivos (se creará si no existe):')
    
    if nombre_carpeta:
        ruta_carpeta = os.path.join(directorio_principal, nombre_carpeta)
        os.makedirs(ruta_carpeta, exist_ok=True)
        
        # Subir archivos
        archivos = st.file

