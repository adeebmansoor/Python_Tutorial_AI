# Python Practice AI

Python learning notebooks plus a Streamlit recipe generator powered by the
Google Gen AI SDK.

## Contents

- `1_Datatypes.ipynb` through `9_Exercise_3.ipynb`: Python fundamentals and
  practice exercises.
- `10_Call_LLM.ipynb`: a first call to Gemini and a recipe-generation function.
- `app.py`: a Streamlit app for generating recipes from ingredients, cuisine,
  dietary preference, servings, and cooking time.

## Run locally

1. Create and activate a virtual environment (optional but recommended):

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install the app dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and add your Gemini API key:

   ```text
   GEMINI_API_KEY=your_api_key
   ```

   The app also accepts `GOOGLE_API_KEY` as an environment variable.

4. Start the app:

   ```powershell
   streamlit run app.py
   ```

Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).
Never commit your `.env` file or share your API key.
