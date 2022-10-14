import streamlit as st
import pandas as pd


uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")

if uploaded_file is not None:
    df = pd.read_csv(
        uploaded_file
    )
    
