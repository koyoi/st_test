
# https://qiita.com/tamura__246/items/366b5581c03dd74f4508#%E5%BF%9C%E7%94%A8%E7%B7%A8--%E3%83%87%E3%83%BC%E3%82%BF%E5%88%86%E6%9E%90web%E3%82%A2%E3%83%97%E3%83%AA%E3%81%AE%E9%96%8B%E7%99%BA

import streamlit as st
import pandas as pd

st.set_page_config(page_title="メインページ", page_icon='icon.png')
st.title("Multiple OSS Access Log Analyzer")

uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")

if uploaded_file is not None:
    df = pd.read_csv(
        uploaded_file
    )
    
    st.markdown('### アクセスログ（先頭5件）')
    st.write(df.head(5))
