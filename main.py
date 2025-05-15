import streamlit as st
st.set_page_config(page_title="Fraud Detection System", page_icon="💳")

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'ui')))
import ui  

if __name__ == "__main__":
    ui.render()