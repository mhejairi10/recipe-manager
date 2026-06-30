import adding_recipe as add_recipe
import pandas as pd
import os 
import random as randint

def random_select():
    df = pd.read_csv("./data/recipe.csv")

    recipe = df.sample()
    print(recipe)
    