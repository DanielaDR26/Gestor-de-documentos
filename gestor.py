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
def listar_archivos():
    st.subheader("Archivos en el directorio principal:")
    for root, dirs, files in os.walk(directorio_principal):
        nivel = root.replace(directorio_principal, '').count(os.sep)
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

# Función para mostrar normatividad
def normatividad():
    st.title("Normatividad")
    st.write("Aquí puedes subir y ver documentos relacionados con la normatividad.")
    # Llamar a la función de subir y listar archivos relacionados con normatividad
    subir_archivos()
    listar_archivos()

# Función para mostrar estadísticas
def estadisticas():
    st.title("Estadísticas")
    st.write("Aquí puedes visualizar las estadísticas.")
    # Podrías agregar gráficos, tablas u otros contenidos relacionados con estadísticas aquí
    st.write("Estadísticas relacionadas con los documentos o cualquier otra información relevante.")

# Función para mostrar documentos
def documentos():
    st.title("Documentos")
    st.write("Aquí puedes gestionar otros documentos que no están en la normatividad ni en las estadísticas.")
    # Llamar a la función de subir y listar archivos relacionados con documentos
    subir_archivos()
    listar_archivos()

# Menú de opciones con Streamlit
def menu_principal():
    st.title("Espacio Colaborativo")
    
    # Subpáginas usando radio
    opcion = st.radio("Seleccione una sección:", ["Normatividad", "Estadísticas", "Documentos"])
    
    if opcion == "Normatividad":
        normatividad()
    elif opcion == "Estadísticas":
        estadisticas()
    elif opcion == "Documentos":
        documentos()

# Ejecutar la aplicación Streamlit
if __name__ == "__main__":
    menu_principal()


