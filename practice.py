import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv(r"C:\Users\rajaa\Downloads\happy.csv")

st.title("In Search for Happiness")
xaxis=st.selectbox("Select the data for the X-axis", options=["GDP", "Happiness", "Generosity"], index=0)
yaxis=st.selectbox("Select the data for the Y-axis", options=["GDP", "Happiness", "Generosity"], index=0)

if xaxis == "GDP":
    xop=data['gdp']
elif xaxis == "Happiness":
    xop=data['happiness']
elif xaxis == "Generosity":
    xop=data['generosity']

if yaxis == "GDP":
    yop=data['gdp']
elif yaxis == "Happiness":
    yop=data['happiness']
elif yaxis == "Generosity":
    yop=data['generosity']

st.header(f"{xaxis} and {yaxis}")
figure= px.scatter(x=xop,y=yop )
st.plotly_chart(figure)