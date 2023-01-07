import streamlit

import pandas

import requests

streamlit.title("🥣 My parents new Healthy Diner")

streamlit.header('\N{flexed biceps} Breakfast of Champion Coders \N{flexed biceps}')

streamlit.header("🥗 Breakfast Menu")

streamlit.text("🐔 Omega 3 & Bluebery Oatmeal")

streamlit.text("🥑 Kakle, Spanish & Rocket Smoothie")

streamlit.text("🍞 Hard-Boiled Free-Range Egg")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Apple'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruitvice Fruit Advice")
#new Section to display fruitvice api response
fruitvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruitvice_response.json()) #just writes data in the screen

#take the json version of the response and normalize it
fruitvice_normalized = pandas.json_normalize(fruitvice_response.json())

#output it the screen as a table
streamlit.dataframe(fruitvice_normalized)



