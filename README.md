# 🍽️ Recipe Manager

A Python-based Recipe Manager application that allows users to store, organize, search, and manage their favorite recipes. The application uses CSV files for persistent storage and provides an easy-to-use command-line interface for interacting with recipe data.

## 📖 Project Overview

The Recipe Manager was developed as part of a Python Fundamentals project. It demonstrates core Python programming concepts including:

- Functions
- File handling (CSV)
- Lists and dictionaries
- User input validation
- Modular programming
- Random selection
- Data persistence

## ✨ Features

### Core Features

- ➕ Add new recipes
- 🔍 Search recipes by ingredient
- 📋 View all recipes
- 🎲 Get a random recipe suggestion
- 💾 Automatically save recipes to a CSV file
- 📂 Load saved recipes when the application starts

### Recipe Information

Each recipe includes:

- Recipe Name
- Ingredients
- Preparation Time
- Cooking Instructions
- Difficulty Level

### Bonus Features

- 🍳 Categorize recipes (Breakfast, Lunch, Dinner, Dessert)
- ⭐ Rate recipes
- 📊 Sort recipes by rating
- 🛒 Generate shopping lists
- 👨‍🍳 Track cooking history
- 🍽️ Scale ingredient quantities based on the number of servings

---

## 🛠️ Technologies Used

- Python 3
- Pandas
- CSV
- Random Module
- OS Module

---

## 📂 Project Structure

```
Recipe_Manager/
│
├── data/
│   └── recipes.csv
│
├── app.py
├── recipe_manager.py
├── utils.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Recipe_Manager.git
```

### 2. Navigate to the project folder

```bash
cd Recipe_Manager
```

### 3. Install dependencies

```bash
pip install pandas
```

### 4. Run the application

```bash
python app.py
```

---

## 📋 Menu Options

```
Recipe Manager

1. Add Recipe
2. Search Recipe by Ingredient
3. View All Recipes
4. Random Recipe Suggestion
5. Exit
```

---

## 📁 Data Storage

All recipe information is stored in a CSV file, allowing data to persist between application sessions.

---

## 🎯 Learning Objectives

This project demonstrates:

- File handling using CSV
- Data management with Pandas
- Modular Python programming
- User interaction through a command-line interface
- Input validation
- Python functions and control structures

---

## 👥 Team Members

- Team Leader: *Your Name*
- Member 2
- Member 3
- Member 4

---

## 📄 License

This project was developed for educational purposes as part of a Python Fundamentals course.