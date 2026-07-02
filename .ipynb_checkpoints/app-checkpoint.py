# ============================================================
# app.py - Streamlit Application
#
# Group Members:
# - Elias Abbas
# - Ali Radhi
# - Mohammed Hejairi
# ============================================================


import streamlit as st
import pandas as pd
import recipe_manager as rm


#Put title for website
st.title("🍽️ Recipe Manager")
CSV_FILE = "data/recipe.csv"

#Create menu of options in sidder section
menu = st.sidebar.selectbox(
    "Choose an option", #Title/label for the menu
    [
        "Add New Recipe",
        "Search by Ingredient",
        "View All Recipes",
        "Random Recipe Suggestion",
        "Generate Shopping List",
        "Cooking History"
    ] #options
)

#Transform to Add New Recipe mode (in same page)
if menu == "Add New Recipe":
    st.header("Add New Recipe") #Write header for the group
    
    name = st.text_input("Recipe Name") #Add text area for name field
    ingredients = st.text_input("Ingredients separated by commas") #Add text area for ingredients field
    time = st.number_input("Preparation Time in Minutes", min_value=1) #Add number area for time field
    instructions = st.text_area("Cooking Instructions") #Add text area for instruntions field
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"]) #Add selected box for difficulty field
    category = st.selectbox("Category", ["Breakfast", "Lunch", "Dinner","Dessert"]) #Add selected box for difficulty field
    servings = st.number_input("Number of Servings", min_value=1)
    st.markdown("Rating")
    srating = st.feedback("stars") 
    if srating is not None:
        rating = srating + 1
    cooked = st.selectbox("Have you cooked it before?", ["Yes","No","I will Cook it Today"])
    if cooked == "Yes":
        cooked_date = st.date_input("enter date:")
    elif cooked == "No":
        cooked_date = None
    elif cooked == "I will Cook it Today":
        cooked_date = st.date_input("")


    #If clicked Add Recipe button then:
    if st.button("Add Recipe"):
        #If user does not write name or ingredients or instructions then:    
        if not name or not ingredients or not instructions:
            #show this warning message:
            st.warning("Please fill all required fields.")
        #else if user write invalid name and ingredient then:    
        elif not rm.isValidInputName(name) and not rm.isValidInputIngredient(ingredients):
            #show this warning message:
            st.warning("Recipe name must contain only letters and spaces and Ingredients must contain only letters separated by commas")
        #else if user write invalid ingredient then:    
        elif not rm.isValidInputName(name):
            #show this warning message:
            st.warning("Recipe name must contain only letters and spaces.")
        #else if user write invalid name then:    
        elif not rm.isValidInputIngredient(ingredients):
            #show this warning message:
            st.warning("Ingredients must contain only letters separated by commas.")
        else:
            #otherwise save/add recipe by calling save_recipe funtion
            rm.save_recipe(
                name,
                ingredients,
                time,
                instructions,
                difficulty,
                category,
                servings,
                rating,
                cooked_date
            )
            st.success("Recipe added successfully!")


elif menu == "Search by Ingredient":
    st.header("Search Recipes by Ingredient") #Write header for the group
    ingredient = st.text_input("Enter ingredient")  #Add text area for target ingredient field
    if st.button("Search"):
        #if user write invalid name
        if not rm.isValidInputName(ingredient):
            #show this warning message: 
            st.warning("Ingredients must contain only letters.")
        else:
             #call search() funtion and save return value in 'results' variable
            results = rm.search(ingredient)
            if not results.empty:
                #Show results as data frame form in the page
                st.dataframe(results,hide_index=True)
            else:
                st.warning("No recipes found.")

elif menu == "View All Recipes":
    st.header("All Recipes")
    results = rm.view_all()

    #if result is not None then:
    if  results is not None:
        #show the result as data frame in the page 
        st.dataframe(results, hide_index=True)
    else:
        #otherwise show this warning message:
        st.warning("Sorry, no recipes found.")


elif menu == "Random Recipe Suggestion":
    st.header("Random Recipe Suggestion")
    #call random
    results = rm.random_select()

    #if result is not None then:
    if results is not None:
        #show the result as data frame in the page 
        st.dataframe(results,hide_index=True)
    else:
        #otherwise show this warning message:
        st.warning("Sorry, no recipes found.")

elif menu == "Generate Shopping List":
    #read csv file
    df = pd.read_csv(CSV_FILE)

    #you can choice multi-options by using st.multiselect
    selected_recipes = st.multiselect("Choose recipes",list(df["Recipe"]))

    #if clicked Generate Shopping List then:
    if st.button("Generate Shopping List"):
        #call generate_shoping_list() funtion and save return value in shoping_list variable
        shopping_list = rm.generate_shopping_list(selected_recipes)

        #write Shopping List in the page 
        st.write("Shopping List")
        
        for i in shopping_list:
            #write require ingredients to selected recipes
            #'-' means write ingredients in Listed form 
            st.write("- " + i)


elif menu =="Cooking History":
    st.header("Cooking History")
    # call a function for the cooking history
    results = rm.view_cooking_history()
    st.dataframe(results, hide_index=True)

    st.header("Suggestion")
    #call a function for the suggestions
    suggest = rm.suggest_by_history()
    st.dataframe(suggest, hide_index=True)

    recipe_name = suggest["Recipe"].iloc[0]
    if st.button("I will cook this today"):
        #updates the cooked date
        rm.update_cooked_date(recipe_name)
        st.success("Cooking date updated!")
