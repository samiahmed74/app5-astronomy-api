# get image of the day from Nasa open api and displaying it on a web
# browser using streamlit
import requests
import streamlit as st

api_key="7DZy9SawBdwKWZEVsngVPedIEZib827K2UPV8X1H"

url = "https://api.nasa.gov/planetary/apod"

params = {
    'api_key': api_key
}

# make request
response = requests.get(url, params=params)
data = response.json()

image_url = data['url']
image_title = data['title']
image_explanation = data['explanation']

image_response = requests.get(image_url)

# saving the image in file for reference
with open("image.jpg", "wb") as file:
    file.write(image_response.content)

# showing the image on streamlit
st.set_page_config(layout="wide")
st.header("NASA Image of the Day")
st.subheader(image_title)
st.image(image_response.content)
st.write(image_explanation)
st.write(image_url)

