import os
import shutil
import pandas as pd
import streamlit as st
from PIL import Image

import streamlit as st
import login

archivo=__file__.split("\\")[-1]
login.generarLogin(archivo)
if 'usuario' in st.session_state:
    st.header('Página :red[Compras]')

    


