import streamlit as st
import plotly.express as px

# st.set_page_config(layout="wide")
st.title("An interactive weather forecast app")
location = st.text_input(label="Place:", placeholder="Enter a place", help="Enter a place you would like to forecast")
days = st.slider(label="Select days", min_value=1, max_value=5, step=1)
options= st.selectbox(label='Choose temperature or day', placeholder="Enter a key", options=["Temperature", "Sky"])


st.write(f"{inpt}'s {options} for the next {days} days is ")

temperatures = get_graph(location, days, options)
newtemp= [i * days for i in temperatures]
figure = px.line(x=date, y= newtemp)
st.plotly_chart(figure)

get_graph(days)




