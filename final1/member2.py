def view_all() :
    """
    prints all recepies name and their preparation time, returns  Created By Ali Mohammed Radhi
    """
    import pandas as pd
    df = pd.read_csv('./data/recipe.csv')
    if df.empty:
      print("Sorry, no previous recepies")
      choice = input("Would you like to add a recipe now? (yes/no): ")

    
    else:     
        filtered = df[['Recipe_Name', 'Prep_Time_Min']]
        print(filtered)