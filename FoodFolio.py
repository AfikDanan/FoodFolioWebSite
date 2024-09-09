import streamlit as st

tab1, tab2 ,tab3= st.tabs(["Privacy Policy","About", "How to use"])

with tab1:

    st.title("Privacy Policy")
    st.write("**Effective Date:** Sep 9th, 2024")

    st.subheader("Information We Do Not Collect")
    st.write(
        "Our app does not collect, store, or share any personal information or data, "
        "except in specific scenarios related to image processing."
    )

    st.subheader("Data Collected for Image Processing")
    st.write(
        "If you choose to add a recipe via an image, the image will be temporarily sent "
        "to a third-party server (AWS) and then to the Google Vision API for text extraction. "
        "This process is solely for extracting recipe information from the image. The image is "
        "not stored on our servers or shared with any other third parties beyond the stated purpose."
    )

    st.subheader("Local Data Storage")
    st.write(
        "All other data you create or manage within the app is stored locally on your device. "
        "No other data is sent to our servers, third-party servers, or external services."
    )

    st.subheader("Data Security")
    st.write(
        "We prioritize your privacy and the security of your data. For the image processing feature, "
        "we use secure transmission methods to send the image to AWS and the Google Vision API. Once "
        "processed, the image is not retained by us or any of the third-party services."
    )

    st.subheader("Data Retention")
    st.write(
        "Images sent for processing are not stored by us or retained longer than necessary for text extraction. "
        "We do not maintain copies of the images beyond this purpose."
    )

    st.subheader("Changes to This Privacy Policy")
    st.write(
        "We may update this Privacy Policy from time to time. Any changes will be reflected in the updated policy, "
        "which will be available within the app. We encourage you to review this policy periodically for any updates or changes."
    )

    st.subheader("Contact Us")
    st.write(
        "If you have any questions or concerns about this Privacy Policy, please contact us at mystorecom24@gmail.com."
    )

with tab2:
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
with tab3:
    # Tutorial Section
    st.header("How to Use the Application")
    st.subheader("Add a New Recipe")
    st.markdown("""
    1. From the Home screen, tap the "Add" icon.
    2. Select a method to add the recipe (by image, by URL, or manually).
    3. Enter the recipe details, including the title, ingredients, instructions, category, and image (optional).
    4. Tap "Save" to store the recipe in your local database.
    """)

    st.subheader("Plan Your Meals")
    st.markdown("""
    1. Access the "Meal Planner" section.
    2. Select recipes to add to your meal plan.
    3. Organize your meal plan by day.
    """)
    
    st.subheader("Generate a Grocery List")
    st.markdown("""
    1. Go to the "Grocery List" section.
    2. Tap "Generate List" to automatically create a grocery list based on your selected recipes or the entire meal plan.
    3. Review and adjust the list if needed, adding or removing items.
    4. Use the grocery list during shopping to ensure you have all the ingredients required.
    """)

    st.subheader("Manage Your Recipe Collection")
    st.markdown("""
    1. View all your stored recipes in the "All Recipes" section.
    2. Edit or delete recipes as needed.
    3. Export your recipe collection to share with others.
    """)


