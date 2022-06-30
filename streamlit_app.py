import streamlit
import pandas

import requests

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")


streamlit.title("My Parents new Healthy Diner")

streamlit.header('Breakfast Favourites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket smoothie')
streamlit.text('🐔 Hard-Boiled Free range Egg')
streamlit.text('🥑🍞 Avocado Toast')

# Display the table on the page.
streamlit.title("Smoothie Bar")
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.header("Fruityvice Fruit Advice!")
streamlit.dataframe(my_fruit_list)
streamlit.text(fruityvice_response)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
