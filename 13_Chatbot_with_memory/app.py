import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError


MODEL_NAME = "gemini-3.8-flash"

load_dotenv()

st.set_page_config(
    page_title="Chatbot with Memory",
    page_icon="💬",
    layout="centered",
)

st.title("Chatbot with Memory 💬")
st.write(
    "Chat with Gemini. This app sends the conversation so far with each message, "
    "so the assistant can refer back to what you discussed."
)

if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

with st.sidebar:
    st.subheader("Conversation")
    st.caption("Your chat history is kept for this browser session.")
    if st.button("Clear conversation", use_container_width=True):
        st.session_state["conversation"] = []

for message in st.session_state["conversation"]:
    role = "user" if message["role"] == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message["parts"][0]["text"])

user_message = st.chat_input("Send a message")

if user_message:
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error(
            "Gemini API key not found. Add GEMINI_API_KEY=your_key to the project "
            ".env file, or set GEMINI_API_KEY in your environment."
        )
    else:
        user_turn = {"role": "user", "parts": [{"text": user_message}]}
        pending_conversation = [*st.session_state["conversation"], user_turn]

        try:
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=pending_conversation,
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
                st.error(f"Gemini API error ({error.status}): {error.message}")
        else:
            reply = response.text
            if reply and reply.strip():
                st.session_state["conversation"] = [
                    *pending_conversation,
                    {"role": "model", "parts": [{"text": reply.strip()}]},
                ]
                st.rerun()
            else:
                st.error("Gemini returned an empty response. Please try again.")
