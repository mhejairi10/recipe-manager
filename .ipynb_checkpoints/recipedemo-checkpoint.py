import csv
import random
from datetime import datetime

RECIPE_FILE = "recipes.csv"
HISTORY_FILE = "cooking_history.csv"


def create_files():
    try:
        with open(RECIPE_FILE, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "name", "ingredients", "prep_time", "instructions",
                "difficulty", "category", "servings", "rating"
            ])
    except FileExistsError:
        pass

    try:
        with open(HISTORY_FILE, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["recipe_name", "date_cooked"])
    except FileExistsError:
        pass


def load_recipes():
    recipes = []

    with open(RECIPE_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            recipes.append(row)

    return recipes


def save_recipe(recipe):
    with open(RECIPE_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "name", "ingredients", "prep_time", "instructions",
            "difficulty", "category", "servings", "rating"
        ])

        writer.writerow(recipe)


def add_recipe():
    name = input("Recipe name: ")
    ingredients = input("Ingredients separated by commas: ")
    prep_time = input("Preparation time in minutes: ")
    instructions = input("Cooking instructions: ")
    difficulty = input("Difficulty level (Easy, Medium, Hard): ")
    category = input("Category (Breakfast, Lunch, Dinner, Dessert): ")
    servings = input("Number of servings: ")
    rating = input("Rating out of 5: ")

    recipe = {
        "name": name,
        "ingredients": ingredients,
        "prep_time": prep_time,
        "instructions": instructions,
        "difficulty": difficulty,
        "category": category,
        "servings": servings,
        "rating": rating
    }

    save_recipe(recipe)
    print("Recipe added successfully!")


def search_by_ingredient():
    recipes = load_recipes()
    ingredient = input("Enter ingredient to search for: ").lower()

    found = False

    for recipe in recipes:
        if ingredient in recipe["ingredients"].lower():
            print_recipe(recipe)
            found = True

    if not found:
        print("No recipes found with that ingredient.")


def view_all_recipes():
    recipes = load_recipes()

    if len(recipes) == 0:
        print("No recipes saved yet.")
        return

    recipes.sort(key=lambda x: float(x["rating"]), reverse=True)

    print("\nAll Recipes:")
    for recipe in recipes:
        print(f"{recipe['name']} - {recipe['prep_time']} minutes - Rating: {recipe['rating']}/5")


def random_recipe():
    recipes = load_recipes()

    if len(recipes) == 0:
        print("No recipes saved yet.")
        return

    recipe = random.choice(recipes)
    print_recipe(recipe)

    cooked = input("Did you cook this recipe? (yes/no): ").lower()

    if cooked == "yes":
        with open(HISTORY_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([recipe["name"], datetime.now().strftime("%Y-%m-%d")])

        print("Cooking history updated!")


def scale_ingredients():
    recipes = load_recipes()
    recipe_name = input("Enter recipe name: ").lower()

    for recipe in recipes:
        if recipe["name"].lower() == recipe_name:
            old_servings = int(recipe["servings"])
            new_servings = int(input("Desired number of servings: "))

            scale = new_servings / old_servings

            print("\nScaled Ingredients:")
            ingredients = recipe["ingredients"].split(",")

            for ingredient in ingredients:
                print(f"{ingredient.strip()} x {scale}")

            return

    print("Recipe not found.")


def shopping_list():
    recipes = load_recipes()
    selected = input("Enter recipe names separated by commas: ").lower().split(",")

    print("\nShopping List:")

    for recipe in recipes:
        if recipe["name"].lower() in [name.strip() for name in selected]:
            ingredients = recipe["ingredients"].split(",")

            for ingredient in ingredients:
                print(f"- {ingredient.strip()}")


def suggest_not_recently_cooked():
    recipes = load_recipes()
    cooked_recipes = []

    with open(HISTORY_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cooked_recipes.append(row["recipe_name"])

    not_recent = []

    for recipe in recipes:
        if recipe["name"] not in cooked_recipes:
            not_recent.append(recipe)

    if len(not_recent) == 0:
        print("You have cooked all recipes before.")
    else:
        recipe = random.choice(not_recent)
        print("Recipe you have not cooked recently:")
        print_recipe(recipe)


def print_recipe(recipe):
    print("\n-------------------------")
    print(f"Name: {recipe['name']}")
    print(f"Ingredients: {recipe['ingredients']}")
    print(f"Preparation Time: {recipe['prep_time']} minutes")
    print(f"Instructions: {recipe['instructions']}")
    print(f"Difficulty: {recipe['difficulty']}")
    print(f"Category: {recipe['category']}")
    print(f"Servings: {recipe['servings']}")
    print(f"Rating: {recipe['rating']}/5")
    print("-------------------------")


def menu():
    create_files()

    while True:
        print("\nRecipe Manager")
        print("1. Add a new recipe")
        print("2. Search for recipes by ingredient")
        print("3. View all recipes")
        print("4. View a random recipe suggestion")
        print("5. Scale ingredient quantities")
        print("6. Generate shopping list")
        print("7. Suggest recipe not cooked recently")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_recipe()
        elif choice == "2":
            search_by_ingredient()
        elif choice == "3":
            view_all_recipes()
        elif choice == "4":
            random_recipe()
        elif choice == "5":
            scale_ingredients()
        elif choice == "6":
            shopping_list()
        elif choice == "7":
            suggest_not_recently_cooked()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


menu()