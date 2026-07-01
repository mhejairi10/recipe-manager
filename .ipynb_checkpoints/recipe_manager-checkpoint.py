import pandas as pd
import os
import re

CSV_FILE = "data/recipe.csv"


def save_recipe(name, ingredients, time, instructions, difficulty, category, servings,rating):
    new_data = pd.DataFrame([{
        "Recipe": name,
        "Ingredients": ingredients,
        "Time": time,
        "Instructions": instructions,
        "Difficulty": difficulty,
        "Category": category,
        "Servings": servings,
        "Rating": rating
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