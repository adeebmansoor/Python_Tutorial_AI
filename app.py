import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError


MODEL_NAME = "gemini-3.8-flash"

load_dotenv()

st.set_page_config(
    page_title="Recipe Studio",
    page_icon="🍲",
    layout="centered",
)

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(ellipse at 10% 0%, #f4ead5 0, transparent 35%),
            #fbfaf7;
    }
    .main .block-container {
        max-width: 850px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }
    .eyebrow {
        color: #64806b;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="eyebrow">Your kitchen, your ingredients</div>', unsafe_allow_html=True)
st.title("Recipe Studio")
st.write("Tell us what you have. Get a simple recipe made for you.")

with st.form("recipe_form"):
    ingredients_text = st.text_area(
        "Ingredients",
        placeholder="For example: tomatoes, lentils, onion, cumin, salt",
        help="Separate ingredients with commas or put each one on a new line.",
        height=110,
    )

    cuisine_col, diet_col = st.columns(2)
    with cuisine_col:
        cuisine = st.selectbox(
            "Cuisine",
            ["Any", "Indian", "Italian", "Mexican", "Chinese", "Mediterranean", "Thai"],
        )
    with diet_col:
        diet = st.selectbox(
            "Diet",
            ["Any", "Vegetarian", "Vegan", "Jain", "Gluten-free", "Dairy-free"],
        )

    servings_col, time_col = st.columns(2)
    with servings_col:
        servings = st.number_input("Servings", min_value=1, max_value=12, value=2)
    with time_col:
        cooking_time = st.slider("Maximum cooking time", min_value=10, max_value=120, value=30, step=5)

    extra_notes = st.text_input(
        "Anything else to consider? (optional)",
        placeholder="e.g. mild spice, no oven, use up spinach",
        max_chars=250,
    )

    submitted = st.form_submit_button("Generate my recipe", type="primary", use_container_width=True)

if submitted:
    ingredients = [
        ingredient.strip()
        for ingredient in ingredients_text.replace("\n", ",").split(",")
        if ingredient.strip()
    ]

    if not ingredients:
        st.warning("Add at least one ingredient to get started.")
    else:
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            st.error(
                "Gemini API key not found. Add GEMINI_API_KEY=your_key to the project "
                ".env file, or set GEMINI_API_KEY in your environment."
            )
        else:
            prompt = f"""
Create one practical recipe using these ingredients: {", ".join(ingredients)}.
Cuisine: {cuisine}.
Diet: {diet}.
Servings: {servings}.
Maximum cooking time: {cooking_time} minutes.
Additional preferences: {extra_notes or "None"}.

Keep the recipe concise (no more than 100 words). Include a recipe title,
ingredient quantities, and clear numbered cooking steps. Respect the dietary
preference and time limit. Do not claim that a recipe is safe for an allergy
unless the ingredients and preparation are explicitly safe.
"""
            try:
                client = genai.Client(api_key=api_key)
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt,
                )
            except APIError as error:
                if error.code == 429:
                    st.warning(
                        "Gemini's request quota has been reached. Wait about a minute "
                        "and try again. If the problem continues, check your quota, "
                        "usage, and billing settings."
                    )
                    st.markdown(
                        "[Gemini API rate limits](https://ai.google.dev/gemini-api/docs/rate-limits) "
                        " · [Usage dashboard](https://ai.dev/rate-limit)"
                    )
                else:
                    st.error(
                        f"Gemini API error ({error.status}): {error.message}"
                    )
            else:
                if response.text and response.text.strip():
                    st.session_state["recipe"] = response.text.strip()
                else:
                    st.error("Gemini returned an empty recipe. Please try again.")

if "recipe" in st.session_state:
    st.markdown("---")
    st.subheader("Your recipe")
    with st.container(border=True):
        st.markdown(st.session_state["recipe"])
    st.download_button(
        "Download recipe",
        data=st.session_state["recipe"],
        file_name="my_recipe.md",
        mime="text/markdown",
    )
    st.caption(
        "Check ingredient labels and preparation for your own dietary or allergy needs."
    )
