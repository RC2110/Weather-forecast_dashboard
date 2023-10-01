import streamlit as st
import plotly.express as px
from functions import get_data

# st.set_page_config(layout="wide")
st.title("An interactive weather forecast app")
location = st.text_input(label="Place:", placeholder="Enter a place", help="Enter a place you would like to forecast")
days = st.slider(label="Select days", min_value=1, max_value=5, step=1)
options= st.selectbox(label='Choose temperature or day', placeholder="Enter a key", options=["Temperature", "Sky"])

try:
    if location:
        st.write(f"{location}'s {options} for the next {days} days is ")


        daysin3hr = int(days) * 9
        content = get_data(location, days, options)
        days= [i['dt_txt']for i in content['list']][0:daysin3hr]

        if options == "Temperature":
            temperatures = [i['main']['temp'] for i in content['list']][0:daysin3hr]
            temperatures= [i / 10 for i in temperatures]
            figure = px.line(x=days, y=temperatures)
            st.plotly_chart(figure)
        elif options == "Sky":
            temperatures = [i['weather'][0]['main']for i in content['list']][0:daysin3hr]
            img_url=[f"Images/{i.lower()}.png" for i in temperatures]
            st.image(img_url,width=150)


except KeyError:
    st.info("Make sure the location is spelled right!")






