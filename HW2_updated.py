import seaborn as sns
import plotly.express as px
import streamlit as st

df_iris = sns.load_dataset('iris')
st.subheader("Dimension of three Iris species")
fig1 = px.scatter_3d(
    df_iris,
    x="sepal_width",
    y="sepal_length",
    z="species",
    color="species",
    symbol="species",
)
fig2 = px.scatter_3d(
    df_iris,
    x="petal_width",
    y="petal_length",
    z="species",
    color="species",
    symbol="species",
)

tab1, tab2 = st.tabs(["Sepal Size", "Petal Size"])
with tab1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)