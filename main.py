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

print(image_title)
print(image_url)
print(image_explanation)

image_response = requests.get(image_url)

with open("image.jpg", "wb") as file:
    file.write(image_response.content)

