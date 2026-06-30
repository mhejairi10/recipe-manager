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

    # try read csv file
    try:
        #read file
        df = pd.read_csv('recipe.csv')
        #result containt of all recipe that match the condition
        results = df[
            df["ingredients"].str.lower().str.contains(ingredient)
        ]
        
        if not results.empty:
            print(results)
        else:
            print("No recipes found.")
            
    except :
        print('cannot read the file')