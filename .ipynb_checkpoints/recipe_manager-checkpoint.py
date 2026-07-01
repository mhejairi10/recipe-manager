import pandas as pd
import os
import re
from datetime import datetime

CSV_FILE = "data/recipe.csv"


<<<<<<< Updated upstream
def save_recipe(name, ingredients, time, instructions, difficulty, category, servings,rating):
=======
def save_recipe(name, ingredients, time, instructions, difficulty, category, servings,rating,cooked_date):
    """
    Sava/Add recipe into recipe.csv file
    
    Args:
        save_recipe(name, ingredients, time, instructions, difficulty, category, servings,rating):
    
    Returns:
        Nothing
        
    Member: 
        Mohammed Hejairi
    """

>>>>>>> Stashed changes
    new_data = pd.DataFrame([{
        "Recipe": name,
        "Ingredients": ingredients,
        "Time": time,
        "Instructions": instructions,
        "Difficulty": difficulty,
        "Category": category,
        "Servings": servings,
        "Rating": rating,
        "Cooked Date" : cooked_date
    }])

    if os.path.exists(CSV_FILE):
        new_data.to_csv(CSV_FILE, mode="a", header=False, index=False)
    else:
        new_data.to_csv(CSV_FILE, index=False) #header=True as defult and mode ="r" as defult

def search(ingredient):
    """
    Search for all recipes that contain that ingredient
    
    Args:
        search (ingredient)
    
    Returns:
        Nothing
        
    Member: 
        Elias Abbas
    """

    # try read csv file
    try:
        #read file
        df = pd.read_csv(CSV_FILE)
        #result containt of all recipe that match the condition
        results = df[
            df["ingredients"].str.lower().str.contains(ingredient.lower())
        ]
        return results
    except FileNotFoundError:
        return pd.DataFrame()


def view_all() :
    df = pd.read_csv(CSV_FILE)

    if df.empty:
        return None
    return df[["recipe", "time"]]


def random_select():
    
    """
    chooses a random recipe

    Args:
       random_select()

    Returns:
        random recipe

    Member:
        Mohammed Hejairi
    """
    
    df = pd.read_csv(CSV_FILE)

    if df.empty:
        return None

    recipe = df.sample(n=1).reset_index(drop=True)
    return recipe



def isValidInputName(name):
    """
    Check whether the recipe name is valid.

    Args:
       random_select()

    Returns:
        random recipe

    Member:
        

    Rules:
    - Cannot be empty.
    - Can contain only letters and spaces.
    """
    
    #From the beginning to the end, allow only letters and spaces.
    #'r' raw string 
    #'^' begining 
    #'+' can write one or more characters that in [...]
    #'$' check character to the end
    pattern = r"^[A-Za-z ]+$"
    #using .strip() for remove space in beginning and ending "       " return false, without stripe return true
    return bool(re.fullmatch(pattern, name.strip()))
    
def isValidInputIngredient(ingredients):
    """
    Validate ingredients.

    Example of valid input:
        Cheese, Tomato, Olive Oil
    """
    #^[A-Za-z] Matches the first ingredient.
    #(,[A-Za-z ]+)* Repeat this entire group zero or more times.
    # $ to the end 
    pattern = r"^[A-Za-z ]+(,[A-Za-z ]+)*$"

    # withotu bool return "None" if not valid, for tranform it to false use bool()
    return bool(re.fullmatch(pattern, ingredients.strip()))



#functions for cooking history
def suggest_by_history():

    """
    suggests recipes by date
    
    Args:
        suggest_by_history()
    
    Returns:
        dataFrame content of Recipe and Cooked Date
        
    Member: 
        Ali Radhi
    """

    #this function suggest the oldest recipe by date to cook and replace the date with todays date
    df = pd.read_csv(CSV_FILE)
    uncooked_recipes = df[df["Cooked Date"].isna()]
    if uncooked_recipes.empty:
        oldest_suggest = df[["Recipe","Cooked Date"]].sort_values("Cooked Date").head(1)
        return oldest_suggest
    else:
        suggested_uncooked = df[df["Cooked Date"].isna()][["Recipe","Cooked Date"]].head(1)
        return suggested_uncooked

def view_cooking_history():
    #this function displays the recipe name and cooking date
    """
    displays all the recipes and the cooked date
    
    Args:
        view_cooking_history()
    
    Returns:
        dataFrame content of Recipe and Cooked Date
        
    Member: 
        Mohammed Hejairi
    """
    df = pd.read_csv(CSV_FILE)

    if df.empty:
        return None
    return df[["Recipe", "Cooked Date"]]

def update_cooked_date(recipe_name):
    """
    updateds the cooked date to today's date
    
    Args:
        update_cooked_date()
    
    Returns:
       nothing
        
    Member: 
        ALi Radhi and Mohammed Hejairi
    """
    #this function updates the oldest recipe by date with today's date if the user want to cook it today
    df = pd.read_csv(CSV_FILE)
    today = datetime.today().strftime("%Y-%m-%d")
    df.loc[df["Recipe"] == recipe_name, "Cooked Date"] = today
    df.to_csv(CSV_FILE, index=False)