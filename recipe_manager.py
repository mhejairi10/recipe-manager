import pandas as pd
import os

CSV_FILE = "data/recipe.csv"
# def new_recipe():
#     name = input("Enter the name of the recipe: ")
#     ingredients = input("Enter the list of  ingredients in the recipe, list in commas seperatly e.g. (potato,cheese,olive oil):")
#     time = int(input("Enter the number of minutes to prepare it: "))
#     cooking = input("Explain the cooking instructions: ")
#     level = input("how Difficuilt it is?(Easy, Medium, Hard): ")

#     dict1 = [{ "recipe" : name, "ingredients" : ingredients, "time" : time, "instructions" : cooking, "difficuilty" : level}]
#     df = pd.DataFrame(dict1)

#     write_data_to_csv(df, "./data/recipe.csv")


def save_recipe(name, ingredients, time, instructions, difficulty):
    new_data = pd.DataFrame([{
        "recipe": name,
        "ingredients": ingredients,
        "time": time,
        "instructions": instructions,
        "difficulty": difficulty
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
            df["ingredients"].str.lower().str.contains(ingredient)
        ]
        return results
    except FileNotFoundError:
        return pd.DataFrame()


def view_all() :
    df = pd.read_csv(CSV_FILE)

    if df.empty:
        return None
    return df[["recipe", "time"]]
    


# def view_all() :
#     """
#     prints all recepies name and their preparation time, returns  Created By Ali Mohammed Radhi
#     """
#     import pandas as pd
#     df = pd.read_csv('./recipe.csv')
#     if df.empty:
#       print("Sorry, no previous recepies")
#         # choice = input("Would you like to add a recipe now? (yes/no): ")

    
#     else:     
#         filtered = df[['recipe', 'time']]
#         print(filtered)
