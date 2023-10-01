API_KEY = "7d4e609402d852e10c27dc30644567eb"
import requests
import streamlit as st
def get_data(place, days=None, kind=None):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    temperatures = [i['main']['temp'] for i in content['list']]
    return content, temperatures

if __name__ == "__main__":
    print(get_data("Madurai"))
