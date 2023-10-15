#Packages
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px
import time


#Load dataset
nutri_ori = pd.read_csv('Food_nutrition.csv').drop(columns=['index']).dropna()
nutri = nutri_ori[:1000]

# Rename columns for better readability
dict_column_renaming = {
  'index':'index',
  'NDB_No':'ID',
  'Shrt_Desc':'Description',
  'Water_(g)':'Water (g)',
  'Energ_Kcal':'Energy (kcal)',
  'Protein_(g)':'Protein (g)',
  'Lipid_Tot_(g)':'Total Lipid (g)',
  'Ash_(g)':'Ash (g)',
  'Carbohydrt_(g)':'Carbohydrate (g)',
  'Fiber_TD_(g)':'Total Fiber (g)',
  'Sugar_Tot_(g)':'Total Sugar (g)',
  'Calcium_(mg)':'Calcium (mg)',
  'Iron_(mg)':'Iron (mg)',
  'Magnesium_(mg)':'Magnesium (mg)',
  'Phosphorus_(mg)':'Phosphorus (mg)',
  'Potassium_(mg)':'Potassium (mg)',
  'Sodium_(mg)':'Sodium (mg)',
  'Zinc_(mg)':'Zinc (mg)',
  'Copper_mg)':'Copper (mg)',
  'Manganese_(mg)':'Manganese (mg)',
  'Selenium_(µg)':'Selenium (µg)',
  'Vit_C_(mg)':'Vitamin C (mg)',
  'Thiamin_(mg)':'Thiamin (mg)',
  'Riboflavin_(mg)':'Riboflavin (mg)',
  'Niacin_(mg)':'Niacin (mg)',
  'Panto_Acid_mg)':'Panto Acid (mg)',
  'Vit_B6_(mg)':'Vitamin B6 (mg)',
  'Folate_Tot_(µg)':'Total Folate (µg)',
  'Folic_Acid_(µg)':'Folic Acid (µg)',
  'Food_Folate_(µg)':'Food Folate (µg)',
  'Folate_DFE_(µg)':'Folate DFE (µg)',
  'Choline_Tot_ (mg)':'Total Choline (mg)',
  'Vit_B12_(µg)':'Vitamin B12 (µg)',
  'Vit_A_IU':'Vitamin A IU',
  'Vit_A_RAE':'Vitamin A RAE',
  'Retinol_(µg)':'Retinol (µg)',
  'Alpha_Carot_(µg)':'Alpha Carotene (µg)',
  'Beta_Carot_(µg)':'Bata Carotene (µg)',
  'Beta_Crypt_(µg)':'Beta Cryptoxanthin (µg)',
  'Lycopene_(µg)':'Lycopene (µg)',
  'Lut+Zea_ (µg)':'Lutein and Zeaxanthin (µg)',
  'Vit_E_(mg)':'Vitamin E (mg)',
  'Vit_D_µg':'Vitamin D (µg)',
  'Vit_D_IU':'Vitamin D IU',
  'Vit_K_(µg)':'Vitamin K (µg)',
  'FA_Sat_(g)':'Saturated Fat (g)',
  'FA_Mono_(g)':'Monounsaturated Fat (g)',
  'FA_Poly_(g)':'Polyunsaturated Fat (g)',
  'Cholestrl_(mg)':'Cholesterol (mg)',
  'GmWt_1':'Gram Weight 1',
  'GmWt_Desc1':'Gram Weight 1 Description',
  'GmWt_2':'Gram Weight 2',
  'GmWt_Desc2':'Gram Weight 2 Description',
  'Refuse_Pct':'Percent Refuse'
}

nutri = nutri.rename(columns=dict_column_renaming)


macronutrients = ['Water (g)', 'Protein (g)', 'Total Lipid (g)', 'Carbohydrate (g)', 'Total Fiber (g)', 'Ash (g)']
minerals = [
'Calcium (mg)', 'Iron (mg)', 'Magnesium (mg)',
       'Phosphorus (mg)', 'Potassium (mg)', 'Sodium (mg)', 'Zinc (mg)',
       'Copper (mg)', 'Manganese (mg)', 'Selenium (µg)',
       'Thiamin (mg)', 'Riboflavin (mg)', 'Niacin (mg)', 'Panto Acid (mg)',
       'Total Folate (µg)', 'Folic Acid (µg)',
       'Food Folate (µg)', 'Folate DFE (µg)', 'Total Choline (mg)',
       'Retinol (µg)',
       'Alpha Carotene (µg)', 'Bata Carotene (µg)', 'Beta Cryptoxanthin (µg)',
       'Lycopene (µg)', 'Lutein and Zeaxanthin (µg)'
]
vitamins = [col for col in nutri.columns if col.startswith('Vitamin')]

fat = [col for col in nutri.columns if col.find('Fat') != -1]

#Function

#User information
with st.expander("Click here to view your dataset infomation"):
    st.write("Data sample")
    st.write(nutri.head())
    st.write("Data summary")
    st.write(nutri.describe())


st.subheader("Nutrition Quick View and Breakdown")
tab1, tab2, tab3= st.tabs(["Macronutrients, Calories and Cholesterol",
                                   "Not All Fat is Bad", "Minerals and Vitamins"])
with tab1:
    x1_var = st.selectbox('Choose your Macronutrients:', macronutrients)
    y1_var = st.selectbox('Weight Control or Heart Heath Promotion?', ['Energy (kcal)', 'Cholesterol (mg)'])
    fig1 = px.scatter(nutri, x=x1_var, y=y1_var, hover_data=['Description', 'Gram Weight 1', 
                                                             'Gram Weight 1 Description', 'Percent Refuse'], 
                      marginal_x="histogram", marginal_y="histogram")
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
with tab2:
    options2 = st.multiselect("Which Fat do you care about?", fat)
    #Proceed when user select sth
    if options2 != []:
        #st.write('You have choosen: ',options4)
        fat = ['Description', 'Total Lipid (g)'] + options2
        fat_df = nutri[fat]

        #Melt the fat type columns in the dataframe for histogram count 
        fat_df_hist = fat_df.melt(id_vars=['Description', 'Total Lipid (g)'], value_vars=options2,
                        var_name='Fat Type', value_name='Weight')
        
        #Add a percent fat column
        fat_df_hist['Percentage'] = fat_df_hist['Weight']/fat_df_hist['Total Lipid (g)']
        
        # Create distplot with custom bin_size
        fig2 = px.histogram(fat_df_hist, x='Percentage', color='Fat Type', marginal="rug", 
                            title='Histogram of Fat Breakdown', opacity=0.75,
                            hover_data=fat_df_hist.columns, nbins=50)

        st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    else:
        st.write('Nothing have been selected!')
with tab3:
    min_on = st.toggle('Show me the Essential Minerals!')

    if min_on:
        options3 = st.multiselect("Which Essential Minerals do you care about?", minerals)
        #Proceed when user select sth
        if options3 != []:
            #st.write('You have choosen: ',options4)
            mineral = ['Description', 'Gram Weight 1'] + options3
            mineral_df = nutri[mineral]

            #Melt the fat type columns in the dataframe for histogram count 
            mineral_df_hist = mineral_df.melt(id_vars=['Description', 'Gram Weight 1'], value_vars=options3,
                            var_name='Mineral Type', value_name='Weight')
            
            #Add a percent (mg) or (µg) tag:
            mineral_df_hist['Measured in'] = mineral_df_hist['Mineral Type'].str[-3:-1]
            
            # Create distplot with custom bin_size
            fig3 = px.box(mineral_df_hist, x='Mineral Type', y='Weight', color='Measured in',
                                title='Minerals Distribution', facet_col='Measured in',
                                hover_data=mineral_df_hist.columns)

            st.plotly_chart(fig3, theme="streamlit", use_container_width=True)
        else:
            st.write('Nothing have been selected!')
        #st.pyplot(fig2, use_container_width=True)

    vit_on = st.toggle('Show me the Vital Vitamins!')
    if vit_on:
        options4 = st.multiselect("Which Vital Vitamins do you care about?", vitamins)
        #Proceed when user select sth
        if options4 != []:
            #st.write('You have choosen: ',options4)
            vit = ['Description', 'Gram Weight 1'] + options4
            vit_df = nutri[vit]

            #Melt the fat type columns in the dataframe for histogram count 
            vit_df_hist = vit_df.melt(id_vars=['Description', 'Gram Weight 1'], value_vars=options4,
                            var_name='Vitamin Type', value_name='Weight')
            
            #Add a percent (mg) or (µg) tag:
            vit_df_hist['Measured in'] = vit_df_hist['Vitamin Type'].str[-3:-1]
            
            # Create distplot with custom bin_size
            fig4 = px.box(vit_df_hist, x='Vitamin Type', y='Weight', color='Measured in',
                                title='Vitamins Distribution', facet_col='Measured in',
                                hover_data=vit_df_hist.columns)

            st.plotly_chart(fig4, theme="streamlit", use_container_width=True)
        else:
            st.write('Nothing have been selected!')
        #st.pyplot(fig2, use_container_width=True)   




