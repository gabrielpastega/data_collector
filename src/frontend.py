from typing import Any
import streamlit as st

class ExcelValidatorUI:

    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title="Validador de schema Excel"
        )
    
    def display_header(self):
        st.title("Validador de schema Excel")

    def upload_file(self):
        return st.file_uploader("Carregue seu arquivo Excel aqui", type=["xlsx"])