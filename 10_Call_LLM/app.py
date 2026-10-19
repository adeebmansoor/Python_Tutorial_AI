import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError


MODEL_NAME = "gemini-3.8-flash"
DIETARY_PREFERENCES = [
    "No preference",
    "Vegetarian",
    "Vegan",
    "Pescatarian",
    "Jain",
    "Gluten-free",
    "Dairy-free",
]

load_dotenv()

st.set_page_config(
    page_title="Recipe Generator",
    page_icon="🍲",
    layout="centered",
)

st.title("Your next meal, made with what you have 🍲")
st.write(
    "Tell Gemini what is in your kitchen and get a recipe tailored to your "
    "cuisine, dietary needs, and schedule."
)

with st.sidebar:
    st.subheader("About")
    st.write("Recipes are generated with Gemini using the Google Gen AI SDK.")
    st.caption(
        "Set GEMINI_API_KEY in your .env file or environment to enable generation."
    )

with st.form("recipe_form"):
    ingredients_text = st.text_area(
        "Ingredients",
        placeholder="For example: tomatoes, lentils, onions, cumin, salt",
        help="Separate ingredients with commas or put each one on a new line.",
    )

    cuisine = st.text_input(
        "Cuisine",
        value="Any",
        placeholder="For example: Indian, Italian, Mexican",
    )

    dietary_preference = st.selectbox(
        "Dietary preference",
        DIETARY_PREFERENCES,
    )

    servings = st.number_input(
        "Servings",
        min_value=1,
        max_value=20,
        value=2,
        step=1,
    )

    max_cooking_minutes = st.number_input(
        "Maximum cooking time (minutes)",
        min_value=5,
        max_value=240,
        value=45,
        step=5,
    )

    submitted = st.form_submit_button(
        "Generate recipe",
        type="primary",
        use_container_width=True,
    )

if submitted:
    ingredients = list(
        dict.fromkeys(
            ingredient.strip()
            for ingredient in ingredients_text.replace("\n", ",").split(",")
            if ingredient.strip()
        )
    )

    if not ingredients:
        st.session_state.pop("recipe", None)
        st.error("Enter at least one ingredient to generate a recipe.")
    else:
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            st.session_state.pop("recipe", None)
            st.error(
                "Gemini API key not found. Add GEMINI_API_KEY=your_key to the "
                "project .env file, or set GEMINI_API_KEY in your environment."
            )
        else:
            prompt = f"""
Create one practical recipe using these available ingredients: {", ".join(ingredients)}.
Cuisine: {cuisine.strip() or "Any"}.
Dietary preference: {dietary_preference}.
Servings: {servings}.
Maximum cooking time: {max_cooking_minutes} minutes.

Use a clear title, list ingredients with quantities, and provide numbered,
easy-to-follow cooking steps. Include prep and cooking time. Keep the recipe
within the dietary preference and maximum time. If an essential ingredient is
not listed, mark it as optional rather than assuming it is available.
"""

            try:
                client = genai.Client(api_key=api_key)
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt,
                )
            except APIError as error:
                st.session_state.pop("recipe", None)
                if error.code == 429:
                    st.warning(
                        "Gemini's request quota has been reached. Wait about a "
                        "minute and try again. If the problem continues, check "
                        "your quota, usage, and billing settings."
                    )
                    st.markdown(
                        "[Gemini API rate limits](https://ai.google.dev/gemini-api/docs/rate-limits) "
                        " · [Usage dashboard](https://ai.dev/rate-limit)"
                    )
                else:
                    st.error(f"Gemini API error ({error.status}): {error.message}")
            else:
                recipe = response.text
                if recipe and recipe.strip():
                    st.session_state["recipe"] = recipe.strip()
                else:
                    st.session_state.pop("recipe", None)
                    st.error("Gemini returned an empty response. Please try again.")

if recipe := st.session_state.get("recipe"):
    st.divider()
    st.subheader("Your recipe")
    st.markdown(recipe)
    st.download_button(
        "Download recipe",
        data=recipe,
        file_name="gemini_recipe.md",
        mime="text/markdown",
    )
