import pandas as pd
import os
import re

CSV_FILE = "data/recipe.csv"


def save_recipe(name, ingredients, time, instructions, difficulty, category, servings,rating):
    """
    Sava/Add recipe into recipe.csv file
    
    Args:
        save_recipe(name, ingredients, time, instructions, difficulty, category, servings,rating):
    
    Returns:
        Nothing
        
    Member: 
        Mohammed Hejairi
    """

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
            df["Ingredients"].str.lower().str.contains(ingredient.lower())
        ]
        return results
    except FileNotFoundError:
        return pd.DataFrame()


def view_all():
    """
    view_all into recipe(s) that in recipe.csv
    
    Args:
        view_all():
    
    Returns:
        dataFrame content of Recipe and Time
        
    Member: 
        Ali Radhi
    """

    df = pd.read_csv(CSV_FILE)

    if df.empty:
        return None
    return df[["Recipe", "Time"]]


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
    #sample take 1 sample dataset as defult
    recipe = df.sample()
    return recipe

def generate_shopping_list(selected_recipes):
    """
    Generate shoping list content of require ingredient(s) for selected recipe(s)

    Args:
       generate_shopping_list(selected_recipes)

    Returns:
        shoping_list content of require ingredient(s) for selected recipe(s)

    Member:
        Mohammed Hejairi
    """

    df = pd.read_csv(CSV_FILE)
    shopping_list = []

    for recipe in selected_recipes:
        row = df[df["Recipe"] == recipe]
        #Assume we have two Recipe: Pizza we will have error
        ingredients = row["Ingredients"].iloc[0].split(",")

        for item in ingredients:
            shopping_list.append(item.strip())

    return shopping_list
    


def isValidInputName(name):
    """
    Check whether the recipe name is valid.

    Args:
       isValidInputName(name)

    Returns:
        True if name is valid, otherwise False

    Member:
        Elias Abbas
        
        

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
    
    Check whether the recipe Ingredient is valid.

    Args:
       isValidInputIngredient(ingredients)

    Returns:
        True if Ingredient is valid, otherwise False

    Member:
        Elias Abbas

    Example of valid input:
        Cheese, Tomato, Olive Oil
    """
    #^[A-Za-z] Matches the first ingredient.
    #(,[A-Za-z ]+)* Repeat this entire group zero or more times.
    # $ to the end 
    pattern = r"^[A-Za-z ]+(,[A-Za-z ]+)*$"

    # withotu bool return "None" if not valid, for tranform it to false use bool()
    return bool(re.fullmatch(pattern, ingredients.strip()))