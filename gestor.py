# Función para mostrar la página principal del gestor
def menu_principal():
    st.title("Menú Principal")
    
    # Mostrar imagen
    st.image("ruta/a/tu/imagen.jpg", caption="Gestor de Documentos", use_column_width=True)  # Asegúrate de poner la ruta correcta de la imagen
    
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

