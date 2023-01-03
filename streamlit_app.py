import streamlit

import pandas

streamlit.title("🥣 My parents new Healthy Diner")

streamlit.header('\N{flexed biceps} Breakfast of Champion Coders \N{flexed biceps}')

streamlit.header("🥗 Breakfast Menu")

streamlit.text("🐔 Omega 3 & Bluebery Oatmeal")

streamlit.text("🥑 Kakle, Spanish & Rocket Smoothie")

streamlit.text("🍞 Hard-Boiled Free-Range Egg")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")




# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
