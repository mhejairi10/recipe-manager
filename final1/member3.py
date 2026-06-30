import pandas as pd

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
    try:
        df = pd.read_csv('./data/recipe.csv')

        # normalize input
        ingredient = ingredient.lower()

        results = df[
            df["ingredients"].str.lower().str.contains(ingredient, na=False)
        ]

        if results.empty:
            print("No recipes found.")
        else:
            print(results)

    except Exception as e:
        print(f"Error reading file: {e}")