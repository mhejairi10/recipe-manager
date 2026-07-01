#adding cooked date
cooked = st.selectbox("Have you cooked it before?", ["Yes","No","I will Cook it Today"])
    if cooked == "Yes":
        cooked_date = st.date_input("enter date:")
    elif cooked == "No":
        cooked_date = None
    elif cooked == "I will Cook it Today":
        cooked_date = st.date_input("")
#updating cooking history
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




#functions for cooking history
def suggest_by_history():
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
    df = pd.read_csv(CSV_FILE)

    if df.empty:
        return None
    return df[["Recipe", "Cooked Date"]]

def update_cooked_date(recipe_name):
    #this function updates the oldest recipe by date with today's date if the user want to cook it todayf
    df = pd.read_csv(CSV_FILE)
    today = datetime.today().strftime("%Y-%m-%d")
    df.loc[df["Recipe"] == recipe_name, "Cooked Date"] = today
    df.to_csv(CSV_FILE, index=False)
