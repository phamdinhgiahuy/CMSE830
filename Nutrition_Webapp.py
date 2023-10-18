#Packages
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px
from PIL import Image
import altair as alt


#Load dataset
nutri_ori = pd.read_csv('Food_nutrition.csv').drop(columns=['index']).dropna()
nutri = nutri_ori#[:1000]

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
#Section 1: Quick View and Breakdown
st.header("🍴Exploring Food Nutritional Content for a Healthier Lifestyle ")

with st.expander("Start Here"):
    st.write("""🔬Understanding the nutritional content of the food we 
             consume on a daily basis is essential for making informed dietary decisions. 
             The goal of this project is to create a web application that leverages a dataset called
               "The Nutritional Content of Food" to help all of us make healthier dietary choices by 
               providing easy access to essential nutritional information. """)
    image = Image.open('brain-with-fruits-concept.webp')
    st.image(image)
    st.write("""🏋️‍♂️You may think "Hey, I am not a gym rat and I would rather 
             die a couple of years earlier and savor my favorite dishes than survive on 
             the miserable combination of veggies and chicken breast." Completely understandable! 
             But this project intends to equip you with an informative and user-friendly tool to make 
             healthier food decisions and you will soon learn that there are several options from decent 
             to good to superb that you can choose from""")
    
    st.write("""There are 2 main Sections in this first stage of the Poject (⚒️Construction in progress!): 
             Section 1 is "Nutrition Quick View and Breakdown" and we will explore fundamentals elements of food nutrition.
             Section 2 is "The Real Bad Guys" and we will find out the real sneaky culprit 🕵️ that may potential undermine our 
             healthy dietary goal!""") 
    st.write("""But first, let's get you gear up by peaking at the dataset and see what it has to offer.""")

    st.write("Data Sample")         
    st.write(nutri.head(10))
    st.write("Data summary")
    st.write(nutri.describe())


#Food lookup:


#Section 1: Quick View and Breakdown

st.subheader("Section 1: Nutrition Quick View and Breakdown")
#tab1, tab2, tab3= st.tabs(["Do you really know your food?", "Macronutrients, Calories and Cholesterol",
#                                   "Minerals and Vitamins"])
tab2, tab3= st.tabs(["Macronutrients vs Calories",
                                   "Minerals and Vitamins"])
with tab2:
    st.write("""🍞 Macronutrients are nutrients that we need in large amounts. 
              """) 
    
    st.write("""We have all heard of it, the idea of 'a calorie in and a calorie out' when it comes to weight loss.
             But losing weight is not as simple as elementary math, where each certain amount of calories you cut, you'll lose a pound.
             Let's take a quick glance at the relationship between calories and other macronutrients.""")
    x1_var = st.selectbox('Choose your Macronutrients:', macronutrients)
    #y1_var = st.selectbox('Weight Control or Heart Heath Promotion?', ['Energy (kcal)', 'Cholesterol (mg)'])
    fig1 = px.scatter(nutri, x=x1_var, y='Energy (kcal)', hover_data=['Description', 'Gram Weight 1', 
                                                             'Gram Weight 1 Description', 'Percent Refuse'], 
                      marginal_x="histogram", marginal_y="histogram")
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
    st.write("""Did you catch any striking relationship that you have not already known? I guess not!
             The macronutrients—carbohydrate, protein, and fat—are the only nutrients that provide energy to the body, so their relationship
             with calories should be linear but the others not so much. And we do need all of these macronutrients to function well as a human beings.
             The world of nutritions does not revolve around "Calories Count". Not all calories are created equal and we have to consider several 
             other factors of our body and diets like gut microbiome, metabolism and the type of food. 👉 Let's head over to the next tab to 
             celebrate food quality and diversity 🙌.""")    
with tab3:
    st.write("""Vitamins and minerals are micronutrients required by the body to carry out a range of normal functions. 
             However, these micronutrients are not produced in our bodies and must be derived from the food we eat.
             A good strategy should involve opting for food variety, let's see the top micronutrients dense food that you can
             consider adding to your diet.🥗🪙""") 
    min_on = st.toggle('I want the Essential Minerals!',value=True)
    if min_on:
        min_sel = st.selectbox("Which Essential Minerals do you care about?", minerals)

        min_num = st.number_input("Show me the top:", min_value=0, step=1, value=10)

        st.write('Top ', min_num, 'Food with the highest amount of ', min_sel, ':')
        #Proceed when user select sth
        if min_sel:
            #mineral_df = nutri[min_sel]       

            min_rank = alt.Chart(nutri).mark_bar().encode(
                x=alt.X('Description:N', sort='-y'),
                y=min_sel+':Q'
            ).transform_window(
                rank='rank(min_sel)',
                sort=[alt.SortField(min_sel, order='descending')]
            ).transform_filter(
                (alt.datum.rank < min_num)
            ).interactive()
            st.altair_chart(min_rank, use_container_width=True)
        else:
            st.write('Nothing have been selected!')



    vit_on = st.toggle('I want the Vital Vitamins!',value=True)
    if vit_on:
        vit_sel = st.selectbox("Which Vital Vitamins do you care about?", vitamins)
        vit_num = st.number_input("Show me the top: ", min_value=0, step=1, value=10)

        st.write('Top ', vit_num, 'Food with the highest amount of ', vit_sel, ':')
        #Proceed when user select sth
        if vit_sel:
            #mineral_df = nutri[min_sel]       

            vit_rank = alt.Chart(nutri).mark_bar().encode(
                x=alt.X('Description:N', sort='-y'),
                y=vit_sel+':Q'
            ).transform_window(
                rank='rank(min_sel)',
                sort=[alt.SortField(vit_sel, order='descending')]
            ).transform_filter(
                (alt.datum.rank < vit_num)
            ).interactive()
            st.altair_chart(vit_rank, use_container_width=True)
        else:
            st.write('Nothing have been selected!')

    both_on = st.toggle('I need both!')
    st.write("""Pick each side of the Macronutrients and pan over the scatter range to see what is some of the sample food types
             that satisfy your specification. 🔍""")  
    if both_on:
        vit_pick = st.selectbox('Choose your Macronutrients:', vitamins)
        min_pick = st.selectbox('Choose your Macronutrients:', minerals)

        brush = alt.selection_interval()

        points = alt.Chart(nutri).mark_point().encode(
            x= vit_pick +':Q',
            y= min_pick +':Q'
        ).add_params(
            brush
        )

        vit_pick = alt.Chart(nutri).mark_bar().encode(
            x=alt.X('Description:N', sort='-y'),
            y=vit_pick+':Q'
        ).transform_filter(
            (brush) 
        ).transform_window(
            rank='rank(vit_pick)',
            sort=[alt.SortField(vit_pick, order='descending')]
        ).transform_sample(10)

        min_pick = alt.Chart(nutri).mark_bar().encode(
            x=alt.X('Description:N', sort='-y'),
            y=min_pick+':Q'
        ).transform_filter(
            (brush) 
        ).transform_window(
            rank='rank(min_pick)',
            sort=[alt.SortField(min_pick, order='descending')]
        ).transform_sample(10)

        fig5 = points & (vit_pick | min_pick)
        st.altair_chart(fig5, use_container_width=True)

#Section 2: The Bad Guys

st.subheader("Section 2: The Real Bad Guys?")
tab4, tab5= st.tabs(["Not All Fat is Bad","Sweet sweet life!"])
with tab4:
    st.write("""The most horrendous type of Fat there are is trans fats. 
             Trans fats have no known health benefits and that there is no safe level of consumption.
             Luckily, these criminals have been officially banned in the United States""")
    st.write("""Saturated fats have been the most mixed! A diet rich in saturated fats can drive up total cholesterol, 
             and tip the balance toward more harmful LDL cholesterol but there is no solid proof or clear
             link between saturated fat and heart disease. Still, limiting saturated fat is recommended.""") 
    st.write("""And then, we have our good fellows: monounsaturated and polyunsaturated fats coming
              mainly from vegetables, nuts, seeds, and fish. Apart form a wide range of health benefits, these kind guys also help to
             reduce harmful LDL cholesterol and improve the cholesterol profile. So, you may want more of these!""") 
                
    st.write("""First, let's take a look at the Density Distrubution for these type of fats.""")
    fat_col = fat + ['Description', 'Total Lipid (g)', 'Carbohydrate (g)', 'Cholesterol (mg)']
    fat_per_col = [i.strip('(g)') + ' Percetage' for i in fat]
    fat_df = nutri[fat_col]
    for i in range(len(fat_per_col)):
        fat_df[fat_per_col[i]] = 100*fat_df[fat[i]]/fat_df['Total Lipid (g)']

    fat_chart = alt.Chart(fat_df).transform_fold(
        fat_per_col,
        as_ = ['Fat_type', 'value']
    ).transform_density(
        density='value',
        bandwidth=0.3,
        groupby=['Fat_type'],
        extent= [0, 100],
        counts = True,
        steps=200
    ).mark_area().encode(
        alt.X('value:Q'),
        alt.Y('density:Q').stack('zero'),
        alt.Color('Fat_type:N')
    ).interactive()
    st.altair_chart(fat_chart, use_container_width=True)

    st.write("""Now, head over to this Fat percentage of each type versus Cholesterol. Remember that you want more of
             the green guys, so hover over the green datapoints with high Percentage to see who these guys really are.""")
    options2 = st.multiselect("Which Type of Fat do you care about?", fat, default=fat)
    #Proceed when user select sth
    if options2 != []:

        #Melt the fat type columns in the dataframe for histogram count 
        fat_df_melt = fat_df.melt(id_vars=['Description', 'Total Lipid (g)', 
                                           'Carbohydrate (g)', 'Cholesterol (mg)'], value_vars=options2,
                        var_name='Fat Type', value_name='Weight (g)')
        
        #Add a percent fat column
        fat_df_melt['Percentage'] = fat_df_melt['Weight (g)']/fat_df_melt['Total Lipid (g)']
        
        # Create distplot with custom bin_size
        points = alt.Chart(fat_df_melt).mark_point().encode(
            x='Percentage:Q',
            y=alt.Y('Cholesterol (mg):Q').title('Cholesterol'),
            color=alt.Color('Fat Type:N'),
            tooltip=['Description', 'Total Lipid (g)', 'Carbohydrate (g)', 'Cholesterol (mg)', 'Weight (g)']
        ).interactive()
        st.altair_chart(points, use_container_width=True)

with tab5:
    st.write("""Now, this is the hard part. Everybody loves sugar, it's the chemical of happiness. But we all
             know too well that its sweetness comes at a cost, a probably detrimental effect to several aspects of our health and longevity.
             Yet again, not all sugars are created equally, there's not much that we can go wrong with the natural, complex carbohydrates 
             in whole food. However, the simple one, especially those added to your food just for the sake of tatse and shelf-life, these should be avoided.""")
    
    st.write("We added labels that include colour coding allow you to see at a glance if the food has a high, medium or low amount of sugars:")

    st.write("      red = high (more than 22.5g of sugar per 100g or more than 27g per portion)")

    st.write("      amber = medium (more than 5g but less than or equal to 22.5g of sugar per 100g)")
    
    st.write("      green = low (less than or equal to 5g of sugar per 100g)")
    st.write("""With that, watch out the the sugar dense food but low in fiber, this should be the sign that the sugar comes
             mainly from processing origin. Pan over the region you think is dangerous and should be avoived, the top food with highest
             percentage of sugar but lowest amount of fiber should pop up. Let's see who these bad guys are:🦹""")
    sugar_col = macronutrients + ['Description', 'Total Sugar (g)']
    sugar_df = nutri[sugar_col]

    sugar_df['Sugar Percentage (%)'] = (sugar_df['Total Sugar (g)'])/(sugar_df['Water (g)'] + sugar_df['Protein (g)'] +
                                                                sugar_df['Total Lipid (g)'] + sugar_df['Carbohydrate (g)'] +
                                                                sugar_df['Total Fiber (g)'] + sugar_df['Ash (g)'])*100
    #defining function filter 
    def su_label(x):
        if x <= 5:
            return 'low'
        if (x > 5 and x <= 22.5):
            return 'medium'
        if x > 22.5:
            return 'high'
    #applying the filter function to 'Salary' column 
    sugar_df['Sugar Label'] = sugar_df['Sugar Percentage (%)'].apply(su_label)

    #color mapping
    dom = ['high', 'medium', 'low']
    colo = ['red', 'orange', 'green']

    # Brush for selection
    brush = alt.selection_interval()
    points = alt.Chart(sugar_df).mark_point().encode(
        x='Total Fiber (g):Q',
        y='Sugar Percentage (%):Q',
        color=alt.Color('Sugar Label').scale(domain=dom, range=colo).legend(orient="left"),
        tooltip=['Description', 'Total Sugar (g)', 'Total Fiber (g)', 'Carbohydrate (g)']
        #color=alt.Color('Sugar Label').legend(orient="left")
        ).add_params(brush)

    # Base chart for data tables
    ranked_text = alt.Chart(sugar_df).mark_text(align='right').encode(
        y=alt.Y('row_number:O', axis=None)
    ).transform_filter(
        brush
    ).transform_window(
        row_number='row_number()',
        sort=[alt.SortField('Total Fiber (g)', order='ascending')]
    ).transform_filter(
        alt.datum.row_number < 15
    )

    # Data Tables
    food = ranked_text.encode(text='Description:N').properties(
        title=alt.Title(text='Description', align='right')
    )
    tsu = ranked_text.encode(text='Total Sugar (g):N').properties(
        title=alt.Title(text='Total Sugar (g)', align='right')
    )
    tfu = ranked_text.encode(text='Total Fiber (g):N').properties(
        title=alt.Title(text='Total Fiber (g)', align='left')
    )
    text = alt.hconcat(food, tsu, tfu) # Combine data tables

    # Build chart
    sug_chart = alt.vconcat(
        points,
        text
    ).resolve_legend(
        color="independent"
    ).configure_view(
        stroke=None
    )

    st.altair_chart(sug_chart, use_container_width=True)


    # else:
    #     st.write('Nothing have been selected!')
    
