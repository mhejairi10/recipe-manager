import streamlit as st
import pandas as pd
import recipe_manager as rm


#Put title for website
st.title("🍽️ Recipe Manager")

#Create menu of options in sidder section
menu = st.sidebar.selectbox(
    "Choose an option", #Title/label for the menu
    [
        "Add New Recipe",
        "Search by Ingredient",
        "View All Recipes",
        "Random Recipe Suggestion",
        "Cooking History"
    ] #options
)

#Transform to Addd New Recipe mode (in same page)
if menu == "Add New Recipe":
    st.header("Add New Recipe") #Write header for the group

    name = st.text_input("Recipe Name") #Add text area for name field
    ingredients = st.text_input("Ingredients separated by commas") #Add text area for ingredients field
    time = st.number_input("Preparation Time in Minutes", min_value=1) #Add number area for time field
    instructions = st.text_area("Cooking Instructions") #Add text area for instruntions field
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"]) #Add selected box for difficulty field
    category = st.selectbox("Category", ["Breakfast", "Lunch", "Dinner","Dessert"]) #Add selected box for difficulty field
    servings = st.number_input("Number of Servings", min_value=1)
    rating = st.slider("Rating", 1, 5, 3) 
    cooked = st.selectbox("Have you cooked it before?", ["Yes","No","I will Cook it Today"])
    if cooked == "Yes":
        cooked_date = st.date_input("enter date:")
    elif cooked == "No":
        cooked_date = None
    elif cooked == "I will Cook it Today":
        cooked_date = st.date_input("")
        
    
    if st.button("Add Recipe"):
        if not name or not ingredients or not instructions:
            st.warning("Please fill all required fields.")
        elif not rm.isValidInputName(name) and not rm.isValidInputIngredient(ingredients):
            st.warning("Recipe name must contain only letters and spaces and Ingredients must contain only letters separated by commas")
        elif not rm.isValidInputName(name):
            st.warning("Recipe name must contain only letters and spaces.")

        elif not rm.isValidInputIngredient(ingredients):
            st.warning("Ingredients must contain only letters separated by commas.")
        else:
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
    results= ''
    if st.button("Search"):
        if not rm.isValidInputName(ingredient):
            st.warning("Ingredients must contain only letters.")
        else:
            results = rm.search(ingredient) #call search()
            if not results.empty:
                st.dataframe(results,hide_index=True)
            else:
                st.warning("No recipes found.")

        


elif menu == "View All Recipes":
    st.header("All Recipes")
    results = rm.view_all()

    if not (results is None):
        st.dataframe(results,hide_index=True)
    else:
        st.warning("Sorry, no recipes found.")


elif menu == "Random Recipe Suggestion":
    st.header("Random Recipe Suggestion")
    results = rm.random_select()

    if results is not None:
        st.dataframe(results,hide_index=True)
    else:
        st.warning("Sorry, no recipes found.")

elif menu == "Generate Shopping List":
    df = pd.read_csv("./data/recipe.csv")

    selected_recipes = st.multiselect("Choose recipes",list(df["recipe"]))

    if st.button("Generate Shopping List"):
        shopping_list = rm.generate_shopping_list(selected_recipes)

    st.write("### Shopping List")

    for item in shopping_list:
        st.write("- " + item)
 
elif menu =="Cooking History":
    st.header("Cooking History")

    results = rm.view_cooking_history()
    st.dataframe(results, hide_index=True)

    st.header("Suggestion")

    suggest = rm.suggest_by_history()
    st.dataframe(suggest, hide_index=True)

    recipe_name = suggest["Recipe"].iloc[0]
    if st.button("I will cook this today"):
        rm.update_cooked_date(recipe_name)
        st.success("Cooking date updated!")

        