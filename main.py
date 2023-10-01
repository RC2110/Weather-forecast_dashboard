import streamlit as st
import plotly.express as px

# st.set_page_config(layout="wide")
st.title("An interactive weather forecast app")
inpt = st.text_input(label="Place:", placeholder="Enter a place", help="Enter a place you would like to forecast")
days = st.slider(label="Select days", min_value=1, max_value=5, step=1)
options= st.selectbox(label='Choose temperature or day', placeholder="Enter a key", options=["Temperature", "Sky"])




st.write(f"{inpt}'s {options} for the next {days} days is ")

def get_graph(days):
    date=["29-10-2023", "30-10-2023", "31-10-2023" ]
    temperatures = [20, 25, 27]
    newtemp= [i * days for i in temperatures]
    figure = px.line(x=date, y= newtemp)
    st.plotly_chart(figure)

get_graph(days)




