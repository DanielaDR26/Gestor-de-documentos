import os
import shutil
import pandas as pd
import streamlit as st
from PIL import Image

def mostrar_archivos(directorio):
    # Verificar si el directorio existe antes de intentar listar los archivos
    if not os.path.exists(directorio):
        st.warning(f"El directorio '{directorio}' no existe.")
        return
    
    # Obtener lista de archivos en el directorio
    archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]
    
    # Buscador por nombre de archivo
    busqueda = st.text_input("Buscar documento por nombre:")
    
    # Filtrar archivos por nombre
    if busqueda:
        archivos = [archivo for archivo in archivos if busqueda.lower() in archivo.lower()]
    
    # Mostrar los archivos filtrados
    if archivos:
        archivo_seleccionado = st.selectbox("Seleccione un archivo para ver o descargar", archivos)
        # Botón para descargar el archivo seleccionado
        if st.button(f"Ver/Descargar {archivo_seleccionado}"):
            with open(os.path.join(directorio, archivo_seleccionado), "rb") as file:
                st.download_button(label="Descargar", data=file, file_name=archivo_seleccionado, mime="application/octet-stream")
    else:
        st.warning("No se encontraron archivos que coincidan con la búsqueda.")

# Contraseña de protección (puedes cambiarla por una más segura)
PASSWORD = "miContraseñaSegura"

# Función para borrar archivo
def borrar_archivo(directorio):
    # Verificar si el directorio existe antes de intentar borrar archivos
    if not os.path.exists(directorio):
        st.warning(f"El directorio '{directorio}' no existe.")
        return
    
    # Pedir al usuario que ingrese la contraseña
    contrasena = st.text_input("Ingrese la contraseña para borrar el archivo:", type="password")
    
    if contrasena == PASSWORD:
        # Mostrar los archivos disponibles para borrar
        archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]  # Obtén todos los archivos en el directorio
        if archivos:
            archivo_seleccionado = st.selectbox("Seleccione un archivo para borrar", archivos)
            
            # Botón para borrar el archivo seleccionado
            if st.button(f"Borrar archivo: {archivo_seleccionado}"):
                try:
                    os.remove(os.path.join(directorio, archivo_seleccionado))
                    st.success(f"Archivo '{archivo_seleccionado}' borrado con éxito.")
                except Exception as e:
                    st.error(f"No se pudo borrar el archivo. Error: {e}")
        else:
            st.warning("No hay archivos disponibles para borrar.")
    else:
        if contrasena:
            st.error("Contraseña incorrecta. Intente nuevamente.")

# Crear un directorio principal para almacenar los archivos subidos
directorio_principal = './EspacioColaborativo'
# Crear el directorio principal si no existe
os.makedirs(directorio_principal, exist_ok=True)

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

# Función para listar archivos (Documentos)
def listar_archivos(carpeta_destino):
    ruta_carpeta = os.path.join(directorio_principal, carpeta_destino)
    
    # Verificar si el directorio existe antes de intentar listar los archivos
    if not os.path.exists(ruta_carpeta):
        st.warning(f"El directorio '{ruta_carpeta}' no existe.")
        return
    
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

# Función para mostrar el contenido de la página principal
def mostrar_menu_principal():
    st.title("Gestor de Documentos")
    st.image("LogoIngAmbUD.png", caption="Gestor de Documentos", use_container_width=True)
    st.write("""
    **Bienvenido al Gestor de Documentos**  
    Este es un sistema diseñado para facilitar el manejo de documentos. Permite subir, ver, descargar y organizar documentos relacionados con la normatividad, estadísticas y otros archivos importantes.
    
    Puedes cargar archivos y organizarlos en categorías específicas, tales como **Normatividad**, **Estadísticas** y **Documentos**.
    """)

# Función para mostrar la sección de Normatividad
def mostrar_normatividad():
    st.title("Normatividad")
    st.write("Aquí podrás ver los documentos relacionados con la normatividad.")
    # Agrega contenido específico para la sección de normatividad
    subir_archivos('normatividad')
    listar_archivos('normatividad')
    borrar_archivo("normatividad")
    mostrar_archivos("normatividad")

# Función para mostrar la sección de Estadísticas
def mostrar_estadisticas():
    st.title("Estadísticas")
    st.write("Aquí podrás ver los documentos y gráficos relacionados con estadísticas.")
    # Agrega contenido específico para la sección de estadísticas
    subir_archivos('estadisticas')
    listar_archivos('estadisticas')
    borrar_archivo("estadisticas")

# Función para mostrar la sección de Documentos
def mostrar_documentos():
    st.title("Documentos")
    st.write("Aquí podrás ver los documentos subidos y gestionados.")
    # Agrega contenido específico para la sección de documentos
    subir_archivos('Documentos')
    listar_archivos('Documentos')
    borrar_archivo('Documentos')

# Llamar la función principal para ejecutar la app
if __name__ == "__main__":
    menu_principal()

