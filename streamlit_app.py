import streamlit as st
import pandas as pd


uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")

if uploaded_file is not None:
    df = pd.read_csv(
        uploaded_file
    )
    
    st.markdown('### アクセスログ（先頭5件）')
    st.write(df.head(5))
