import streamlit as st
import pandas as pd
import recipe_manager as rm


import recipe_manager as rm


#Put title for website
st.title("🍽️ Recipe Manager")

#Create menu of options 
menu = st.sidebar.selectbox(
    "Choose an option", #Title/label for the menu
    ["Add New Recipe", "Search by Ingredient", "View All Recipes"] #options
)

#Transform to Addd New Recipe mode (in same page)
if menu == "Add New Recipe":
    st.header("Add New Recipe") #Write header for the group

    name = st.text_input("Recipe Name") #Add text area for name field
    ingredients = st.text_input("Ingredients separated by commas") #Add text area for ingredients field
    time = st.number_input("Preparation Time in Minutes", min_value=1) #Add number area for time field
    instructions = st.text_area("Cooking Instructions") #Add text area for instruntions field
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"]) #Add selected box for difficulty field

    if st.button("Add Recipe") and name and ingredients and instructions:
        rm.save_recipe(name, ingredients, time, instructions, difficulty) #call the save_recipe
        st.success("Recipe added successfully!")
    else:
        st.warning("Please fill all required fields.") #if there is mission input(s) print the message


elif menu == "Search by Ingredient":
    st.header("Search Recipes by Ingredient") #Write header for the group
    ingredient = st.text_input("Enter ingredient")  #Add text area for target ingredient field
    results= ''
    if st.button("Search"):
        results = rm.search(ingredient) #call search()
        
        if not results.empty:
            st.dataframe(results)
        else:
            st.warning("No recipes found.")


elif menu == "View All Recipes":
    st.header("All Recipes")
    results = rm.view_all()

    if not (results is None):
        st.dataframe(results)
    else:
        st.warning("Sorry, no recipes found.")
