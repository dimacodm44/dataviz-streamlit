# importing libraries
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Displaying Text

st.text("Text")
st.write("Super Function")
st.header("Header")
st.subheader("sub-Header")
st.title("Title")
st.markdown("*** Markdown***")
st.code("print('Hello, word!'))", language='python')
st.latex(r''' e^{i\pi} + 1 = 0 ''')

# Displaying INTERACTIVE Widgets
btn = st.button("Submit")
if btn :
    st.info("Info")
option = st.radio("Select",['A','B','C'])
if option == 'A':
    st.warning("Warning! :/")
elif option == 'B':
    st.error("Error! :(")
elif option == 'C':
    st.success("Success :)")

chk = st.checkbox("I agree")
if chk :
    st.exception("Agreement")

option = st.selectbox("Select",['A','B','C'])
if option == 'A':
    st.warning("Warning! :/")
elif option == 'B':
    st.error("Error! :(")
elif option == 'C':
    st.success("Success :)")

age = st.slider("Select",0,100)

st.select_slider("Select",['A','B','C'])

st.text_input("Entrer a text")
st.text_area("Entrer a paragraph")

st.file_uploader("Upload")

st.camera_input("Take a photo")

st.date_input("Today")

st.time_input("Now")

st.number_input("Num")

st.multiselect("Select",['A','B','C'])
st.color_picker("Colors")

df = sns.load_dataset('taxis')
# st.write(df)
st.dataframe(df.head())
btn = st.button("Show Data")

if btn: 
  st.dataframe(df.sample(5))
st.table(df.head(2))

