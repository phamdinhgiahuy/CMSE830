import pandas as pd
import streamlit as st
import time

#path = r'C:\Users\Admin\OneDrive - Michigan State University\Courses\CMSE 830\HW and Assignment\Dataset\Food_nutrition.csv'


col1, col2, col3 = st.columns([1, 2, 1])

col1.markdown(" ## Navigation: ")
col1.markdown(" ### Start Here! ")

file = col2.file_uploader("Upload your dataset here!")
if file is None:
    col2.markdown(" No files uploaded yet. ")
else:
    bar = col2.progress(0)
    for per in range(100):
        time.sleep(0.01)
        bar.progress(per+1)

    col2.success("Your dataset has been uploaded!")
    nutri = pd.read_csv(file)
    col3.metric(label="Data Rows Count", value = f'{nutri.shape[0]}')
    with st.expander("Click here to view your dataset infomation"):
        st.write("Data sample")
        st.write(nutri.head())
        st.write("Data summary")
        st.write(nutri.describe())
            