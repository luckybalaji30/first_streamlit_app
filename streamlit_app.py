import streamlit

import pandas

import requests

import snowflake.connector

from urllib.error import URLError

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

def get_fruityvice_data(this_fruit_choice):
  fruitvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
  fruitvice_normalized = pandas.json_normalize(fruitvice_response.json())
  return fruitvice_normalized
                                 
  
streamlit.header("Fruitvice Fruit Advice !")

try:
  
  #Get the choice from user
  fruit_choice=streamlit.text_input('What fruit would you like information about?', 'Kiwi')
  
  if not fruit_choice :
    streamlit.error('Please select a fruit to get information')
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    #streamlit.write('The user entered', fruit_choice)
    #fruitvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
    #streamlit.text(fruitvice_response.json()) #just writes data in the screen
    
    #take the json version of the response and normalize it
    #fruitvice_normalized = pandas.json_normalize(fruitvice_response.json())

    #output it the screen as a table
    #streamlit.dataframe(fruitvice_normalized)

except URLError as e:
    streamlit.error()
    
# second part 
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
    return my_cur.fetchall()
  
# add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
  
  
# third part
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('from streamlit')")
        return "Thanks for adding " + new_fruit
      
add_my_fruit = streamlit.text_input('What fruit would you like to add ?')
if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)

streamlit.stop()

# try to fetch some values from the configuration
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)

# try to fetch some values from the tables.
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_rows)

#add user's favourite into list
add_fruit_choice = streamlit.text_input('What fruit would like to add?')
streamlit.write('Thanks for adding fruit ', add_fruit_choice)
my_data_rows.append(add_fruit_choice)

streamlit.header("Aftering adding user fruit")
streamlit.dataframe(my_data_rows)

