import streamlit as st
import pandas as pd

st.title("Моё первое Streamlit-приложение")
st.write("Привет! Это тестовый проект.")

if st.button("Показать данные"):
    df = pd.DataFrame({
        "Число": [1, 2, 3, 4],
        "Квадрат": [1, 4, 9, 16]
    })
    st.write(df)
    st.line_chart(df.set_index("Число"))