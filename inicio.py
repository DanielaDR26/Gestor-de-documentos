import streamlit as st
import login1 as login

def main():
    # Your main application logic here
    st.title("Gestor de Documentos")
    login.generarLogin("inicio.py")  # Call the login function

if __name__ == "__main__":
    main()
