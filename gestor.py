import os
import shutil
import pandas as pd
import streamlit as st
from PIL import Image

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
                
                # Agregar opción para renombrar
                nuevo_nombre = st.text_input(f"Renombrar {f} (dejar en blanco para no cambiar):", "")
                if nuevo_nombre and nuevo_nombre != f:
                    nuevo_ruta = os.path.join(root, nuevo_nombre)
                    os.rename(ruta_completa, nuevo_ruta)  # Renombrar archivo
                    st.success(f'Archivo renombrado a {nuevo_nombre}')
    else:
        st.warning(f"No existen archivos en {carpeta_destino}.")

# Función para mostrar normatividad
def normatividad():
    st.title("Normatividad")
    st.write("Aquí puedes subir y ver documentos relacionados con la normatividad.")
    # Llamar a la función de subir y listar archivos relacionados con normatividad
    subir_archivos('Normatividad')
    listar_archivos('Normatividad')

# Función para mostrar estadísticas
def estadisticas():
    st.title("Estadísticas")
    st.write("Aquí puedes visualizar las estadísticas de tus archivos CSV.")
    
    # Subir archivos CSV
    archivos_csv = st.file_uploader("Seleccione archivos CSV para ver estadísticas", type=["csv"], accept_multiple_files=True)
    
    if archivos_csv:
        for archivo in archivos_csv:
            # Leer archivo CSV con Pandas
            df = pd.read_csv(archivo)
            
            # Mostrar la tabla del CSV
            st.subheader(f"Datos de {archivo.name}")
            st.dataframe(df)
            
            # Mostrar estadísticas básicas
            st.subheader("Estadísticas básicas")
            st.write("Promedio de las columnas numéricas:")
            st.write(df.describe())
            
            st.write("Primeras filas del archivo:")
            st.write(df.head())

# Función para mostrar documentos
def documentos():
    st.title("Documentos")
    st.write("Aquí puedes gestionar otros documentos que no están en la normatividad ni en las estadísticas.")
    # Llamar a la función de subir y listar archivos relacionados con documentos
    subir_archivos('Documentos')
    listar_archivos('Documentos')

# Función para mostrar la página principal del gestor
def menu_principal():
    st.title("Menú Principal")
    
    # Mostrar imagen
    st.image("LogoIngAmbUD.png", caption="Gestor de Documentos", use_column_width=True)  # Asegúrate de poner la ruta correcta de la imagen
    
    # Descripción
    st.write("""
    **Bienvenido al Gestor de Documentos**  
    Este es un sistema diseñado para facilitar el manejo de documentos. Permite subir, ver, descargar y organizar documentos relacionados con la normatividad, estadísticas y otros archivos importantes.
    
    Puedes cargar archivos y organizarlos en categorías específicas, tales como **Normatividad**, **Estadísticas** y **Documentos**.
    """)
    
    # Opciones del menú
    opcion = st.sidebar.radio("Seleccione una sección:", ["Menú Principal", "Normatividad", "Estadísticas", "Documentos"])
    
    # Mostrar contenido según la opción seleccionada
    if opcion == "Menú Principal":
        pass  # Ya estamos en la página principal
    elif opcion == "Normatividad":
        normatividad()
    elif opcion == "Estadísticas":
        estadisticas()
    elif opcion == "Documentos":
        documentos()

# Ejecutar la aplicación Streamlit
if __name__ == "__main__":
    menu_principal()

