import pandas as pd
import os

def write_data_to_csv(data, filename):
  
    df2 = pd.DataFrame(data)  
    # Check if the file already exists on your system using os.path.exists
    file_exists = os.path.exists(filename)
        
    if file_exists:
        # Append data: 'a' mode, turn off headers so columns aren't duplicated in mid-file
        df2.to_csv(filename,mode="a",header = False,index = False)
        print("Recipe added successfully!\n")

        
    else:
        # Create new file: 'w' mode (default), write the header columns
        df2.to_csv(filename,mode="w",header=True,index=False)
        print("Recipe added successfully!\n")

        
def new_recipe():
    name = input("Enter the name of the recipe: ")
    ingredients = input("Enter the list of  ingredients in the recipe, list in commas seperatly e.g. (potato,cheese,olive oil):")
    time = int(input("Enter the number of minutes to prepare it: "))
    cooking = input("Explain the cooking instructions: ")
    level = input("how Difficuilt it is?(Easy, Medium, Hard): ")

    dict1 = [{ "recipe" : name, "ingredients" : ingredients, "time" : time, "instructions" : cooking, "difficuilty" : level}]
    df = pd.DataFrame(dict1)

    write_data_to_csv(df, "./data/recipe.csv")

