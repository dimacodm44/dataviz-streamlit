# importing libraries
import streamlit as st
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.express as px

# loading Data
df = pd.read_excel('Financial.xlsx')
st.sidebar.header("Tableau de bord")
st.sidebar.image('sncf.jpg')
st.sidebar.write("Tableau de bord utilise dataset Financial")

# Filter
st.sidebar.write("")
st.sidebar.markdown("Réalisé par :raising_hand: Lead Dev Power BI [Dehaimani Mustapha](mustapha.dehaimani@sncf.fr)")

# body
st.metric("Max. Total Profit",df['Profit'].max())
st.metric("Max. Total Cogs",df['COGS'].max())

# création page
st.sidebar.title ("Sommaire")
pages = ["Page1","page2","page3"]
page = st.sidebar.radio("Aller vers la page :",pages)
if page == pages[0] :
    st.write("### Page1")
    st.write("Cette page explique la présentation générale du projet")
elif page == pages[1] :
    st.write("### Page2")
    st.write("Cette page2 explore le dataset du projet")
elif page == pages[2] :
    st.write("### Page3")
    st.write("Cette page3 concerne la visualisation des données")
    st.dataframe(df)
    
