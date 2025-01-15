import os
import shutil
import pandas as pd
import streamlit as st
from PIL import Image
import login

archivo=__file__.split("\\")[-1]
login.generarLogin(archivo)
if 'usuario' in st.session_state:
# Contraseña de protección (puedes cambiarla por una más segura)
PASSWORD = "1234"

# Función para borrar archivo
def borrar_archivo(directorio, archivo_seleccionado):
    # Mostrar un formulario para ingresar la contraseña
    contrasena = st.text_input("Ingrese la contraseña para borrar el archivo:", type="password")

    # Mostrar la contraseña ingresada para depuración (solo para fines de prueba)
    st.write(f"Contraseña ingresada: {contrasena}")

    # Botón para borrar el archivo
    if st.button(f"🗑️ Borrar {archivo_seleccionado}"):
        # Verificar si la contraseña ingresada es correcta
        if contrasena == PASSWORD:
            st.write("Contraseña correcta, intentando borrar el archivo.")
            try:
                archivo_path = os.path.join(directorio, archivo_seleccionado)
                os.remove(archivo_path)
                st.success(f"Archivo '{archivo_seleccionado}' borrado con éxito.")
            except Exception as e:
                st.error(f"No se pudo borrar el archivo. Error: {e}")
        elif contrasena:  # Si la contraseña no es correcta y se ha ingresado algo
            st.write("Contraseña incorrecta. Intente nuevamente.")
            st.error("Contraseña incorrecta. Intente nuevamente.")
        else:
            st.warning("Por favor ingrese una contraseña para borrar el archivo.")

            
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
                
                # Crear un expander para cada archivo sin el argumento 'key'
                with st.expander(f"Archivo: {f}", expanded=False):
                    # Mostrar las opciones dentro del expander
                    st.write(f"**Ruta:** {ruta_completa}")
                    
                    # Botón de descarga
                    with open(ruta_completa, "rb") as file:
                        st.download_button(
                            label=f"Descargar {f}",
                            data=file,
                            file_name=f,
                            mime="application/octet-stream"
                        )
                    
                    # Opción para borrar el archivo
                    delete_button_key = f"{f}-delete"
                    if st.button(f"🗑️ Borrar {f}", key=delete_button_key):
                        borrar_archivo(root, f)

                    # Opción para renombrar el archivo
                    rename_input_key = f"{f}-rename"
                    nuevo_nombre = st.text_input(f"Renombrar {f} (dejar en blanco para no cambiar):", key=rename_input_key)
                    if nuevo_nombre and nuevo_nombre != f:
                        nuevo_ruta = os.path.join(root, nuevo_nombre)
                        try:
                            os.rename(ruta_completa, nuevo_ruta)  # Renombrar el archivo
                            st.success(f'Archivo renombrado a {nuevo_nombre}')
                        except Exception as e:
                            st.error(f"No se pudo renombrar el archivo. Error: {e}")
    else:
        st.warning(f"No existen archivos en {carpeta_destino}.")

# Función para mostrar el menú principal
def mostrar_menu_principal():
    # Aquí mostramos solo el contenido específico del Menú Principal
    st.title("Gestor de Documentos")
    st.image("LogoIngAmbUD.png", caption="Gestor de Documentos", use_container_width=True)
    st.write("""**Bienvenido al Gestor de Documentos**  
    Este es un sistema diseñado para facilitar el manejo de documentos. Permite subir, ver, descargar y organizar documentos relacionados con la normatividad, estadísticas y otros archivos importantes.
    
    Puedes cargar archivos y organizarlos en categorías específicas, tales como **Normatividad**, **Estadísticas** y **Documentos**.
    """)
    
# Función para mostrar la sección de Normatividad
def mostrar_normatividad():
    st.title("Normatividad")
    st.write("Aquí podrás ver los documentos relacionados con la normatividad.")
    subir_archivos('normatividad')  # Asegúrate de que la función esté definida antes de llamarla
    listar_archivos('normatividad')

# Función para mostrar la sección de Estadísticas
def mostrar_estadisticas():
    st.title("Estadísticas")
    st.write("Aquí podrás ver los documentos y gráficos relacionados con estadísticas.")
    subir_archivos('estadisticas')
    listar_archivos('estadisticas')

# Función para mostrar la sección de Documentos
def mostrar_documentos():
    st.title("Documentos")
    st.write("Aquí podrás ver los documentos subidos y gestionados.")
    subir_archivos('Documentos')
    listar_archivos('Documentos')

# Crear un directorio principal para almacenar los archivos subidos
directorio_principal = './EspacioColaborativo'
os.makedirs(directorio_principal, exist_ok=True)

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

# Llamar la función principal para ejecutar la app
if __name__ == "__main__":
    menu_principal()
