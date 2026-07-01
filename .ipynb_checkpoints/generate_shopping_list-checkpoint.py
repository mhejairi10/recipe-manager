##function

def generate_shopping_list(selected_recipes):
    df = pd.read_csv("./data/recipe.csv")
    shopping_list = []

    for recipe in selected_recipes:
        row = df[df["recipe"] == recipe]
        ingredients = row["ingredients"].iloc[0].split(",")

        for item in ingredients:
            shopping_list.append(item.strip())

    return shopping_list

##streamlit
elif menu == "Generate Shopping List":
    df = pd.read_csv("./data/recipe.csv")

selected_recipes = st.multiselect("Choose recipes",list(df["recipe"]))

if st.button("Generate Shopping List"):
    shopping_list = rm.generate_shopping_list(selected_recipes)

    st.write("### Shopping List")

    for item in shopping_list:
        st.write("- " + item)