#Packages
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import time


#Load dataset
nutri_ori = pd.read_csv('Food_nutrition.csv').dropna()
nutri = nutri_ori[:1000]


macronutrients = ['Water_(g)', 'Protein_(g)', 'Lipid_Tot_(g)', 'Carbohydrt_(g)', 'Fiber_TD_(g)']
minerals = [
    'Calcium_(mg)', 'Iron_(mg)',
       'Magnesium_(mg)', 'Phosphorus_(mg)', 'Potassium_(mg)', 'Sodium_(mg)',
       'Zinc_(mg)', 'Copper_mg)', 'Manganese_(mg)', 'Selenium_(µg)',
        'Thiamin_(mg)', 'Riboflavin_(mg)', 'Niacin_(mg)',
       'Panto_Acid_mg)',  'Folate_Tot_(µg)', 'Folic_Acid_(µg)',
       'Food_Folate_(µg)', 'Folate_DFE_(µg)', 'Choline_Tot_ (mg)',
        'Retinol_(µg)',
       'Alpha_Carot_(µg)', 'Beta_Carot_(µg)', 'Beta_Crypt_(µg)',
       'Lycopene_(µg)', 'Lut+Zea_ (µg)', 
        'FA_Sat_(g)', 'FA_Mono_(g)', 'FA_Poly_(g)',
]
vitamins = [col for col in nutri.columns if col.startswith('Vit_')]

#Function

#User information
with st.expander("Click here to view your dataset infomation"):
    st.write("Data sample")
    st.write(nutri.head())
    st.write("Data summary")
    st.write(nutri.describe())

# Dataset selector
#dataset_option = st.selectbox('Select dataset:', ['Sample Dataset', 'Seaborn MPG'])


#y_var = st.selectbox('Select y-variable:', [col for col in nutri.columns if nutri[col].dtype != 'object'])
#selected_df = nutri[[x_var, y_var]].dropna()

#Visualization 
st.subheader("Nutrition Quick View")
tab1, tab2, tab3 = st.tabs(["Macronutrients, Calories and Cholesterol", "Essential Minerals", "Vital Vitamins"])
with tab1:
    x1_var = st.selectbox('Choose your Macronutrients:', macronutrients)
    y1_var = st.selectbox('Weight Control or Heart Heath Promotion?', ['Energ_Kcal', 'Cholestrl_(mg)'])
    fig1 = px.scatter(nutri, x=x1_var, y=y1_var, hover_data='Shrt_Desc', marginal_x="histogram", marginal_y="histogram")
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
with tab2:
    options2 = st.multiselect("Which Essential Minerals do you care about?", minerals)
    #st.pyplot(fig2, use_container_width=True)
with tab3:
    options3 = st.multiselect("Which Vital Vitamins do you care about?", vitamins)
    #st.pyplot(fig3, use_container_width=True)


