import streamlit as st

tab1, tab2 = st.tabs(["About", "How to use"])


with tab1:
    st.header("About the Application")
    # Introduction
    st.title("Welcome to Our Recipe Management Application")
    st.subheader("Your Ultimate Solution for Organizing and Managing Recipes")

    st.markdown("""
    Our recipe management application helps you efficiently organize and manage your recipes. Whether you are a home cook, a professional chef, or just someone who enjoys cooking, this app provides the tools you need to store, categorize, and access your favorite recipes.
    """)

    # Key Features
    st.header("Key Features")
    st.markdown("""
    - **Streamlined Recipe Capture**: Quickly add recipes by capturing them through an image, URL, or manual entry.
    - **Meal Planning**: Plan meals by selecting recipes and organizing them into a weekly plan.
    - **Shopping List Generation**: Automatically generate shopping lists based on your selected recipes or the weekly plan.
    - **Categorization**: Categorize recipes for easy searching.
    - **Recipe Storage**: Easily store and access your recipes in a well-organized format.
    - **Integration with Local Database**: Save your data securely on your device.
    """)
    
        # Conclusion
    st.header("Get Started Now!")
    st.markdown("""
    Explore the app and make your cooking experience more enjoyable and organized. Whether you're looking for new recipes or managing your weekly meal plan, our app has got you covered!
    #### [QR Code to App Store Link]
    #### [QR Code to play Store Link]
    """)
    st.link_button("Github", 'https://github.com/TopazAakal/FoodFolioApp')
with tab2:
    # Tutorial Section
    st.header("How to Use the Application")
    st.subheader("Step 1: Add a New Recipe")
    st.markdown("""
    1. From the Home screen, tap the "Add" icon.
    2. Select a method to add the recipe (by image, by URL, or manually).
    3. Enter the recipe details, including the title, ingredients, instructions, category, and image (optional).
    4. Tap "Save" to store the recipe in your local database.
    """)

    st.subheader("Step 2: Search and Filter Recipes")
    st.markdown("""
    1. Go to the "Search Recipes" section.
    2. Use the search bar to find recipes by name or ingredient.
    3. Apply filters to narrow down your results by category, cooking time, or other criteria.
    """)

    st.subheader("Step 3: Plan Your Meals")
    st.markdown("""
    1. Access the "Meal Planner" section.
    2. Select recipes to add to your meal plan.
    3. Organize your meal plan by day, week, or month.
    4. Click "Generate Shopping List" to create a list of ingredients for the selected recipes.
    """)

    st.subheader("Step 4: Manage Your Recipe Collection")
    st.markdown("""
    1. View all your stored recipes in the "Recipe Collection" section.
    2. Edit or delete recipes as needed.
    3. Export your recipe collection to share with others.
    """)


