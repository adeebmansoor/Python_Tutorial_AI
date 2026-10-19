<div align="center">

# 🐍 Python Tutorial AI

### From Python basics to building AI apps with Gemini, Streamlit & FastAPI

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Apps-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?logo=google&logoColor=white)](https://aistudio.google.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)

*A hands-on learning path: 23 modules of notebooks and exercises that take you from your first variable to calling LLMs, building chatbots and serving APIs.*

</div>

---

## 📑 Table of Contents

- [About](#-about)
- [Learning Path](#-learning-path)
- [Featured Apps](#-featured-apps)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Security Notes](#-security-notes)
- [Author](#-author)

---

## 📖 About

This repository is my personal Python learning journey, organised as a numbered, step-by-step curriculum. It starts with core language fundamentals and gradually moves into practical AI engineering: calling large language models, keeping conversation memory, getting structured output, handling files, consuming APIs, building a FastAPI backend and talking to databases.

Every concept is followed by a practice **Exercise** module so the ideas stick.

**What you'll find here**

- 📓 Jupyter notebooks that explain and demonstrate each topic
- 🧪 Exercise modules after each group of lessons
- 🤖 Two working **Streamlit** apps powered by the **Google Gen AI SDK** (Gemini)
- ⚡ A FastAPI module and a database interaction module for real-world backends

---

## 🗺️ Learning Path

### 🟢 Phase 1 — Python Fundamentals

| # | Module | Focus |
|---|--------|-------|
| 1 | `1_Datatypes` | Core data types |
| 2 | `2_For_Loop` | Loops and iteration |
| 3 | `3_Dictionary_&_Tuples` | Dictionaries and tuples |
| 4 | `4_Exercise_1` | 🧪 Practice |
| 5 | `5_Functions` | Writing reusable functions |
| 6 | `6_Args_&_Kargs` | `*args` and `**kwargs` |
| 7 | `7_Exercise_2` | 🧪 Practice |
| 8 | `8_Classes_&_Functions` | Object-oriented basics |
| 9 | `9_Exercise_3` | 🧪 Practice |

### 🟡 Phase 2 — Working with LLMs

| # | Module | Focus |
|---|--------|-------|
| 10 | `10_Call_LLM` | First Gemini call + recipe generator app |
| 11 | `11_Error_Handling` | Handling errors gracefully |
| 12 | `12_Exercise_4` | 🧪 Practice |
| 13 | `13_Chatbot_with_memory` | Chatbot that remembers the conversation |
| 14 | `14_Exercise_5` | 🧪 Practice |
| 15 | `15_Structured_Output` | Getting structured responses from the model |
| 16 | `16_Exercise_6` | 🧪 Practice |

### 🔴 Phase 3 — Files, APIs & Backends

| # | Module | Focus |
|---|--------|-------|
| 17 | `17_File_Handling` | Reading and writing files |
| 18 | `18_Exercise_7` | 🧪 Practice |
| 19 | `19_Calling_API` | Consuming external APIs |
| 20 | `20_Exercise_8` | 🧪 Practice |
| 21 | `21_FastAPI` | Building your own API |
| 22 | `22_Database_Interaction` | Working with databases |
| 23 | `23_Exercise_9` | 🧪 Practice |

---

## 🚀 Featured Apps

### 🍳 AI Recipe Generator — `10_Call_LLM/app.py`

A Streamlit app that creates recipes from what you have in your kitchen. Provide:

- 🥕 Ingredients
- 🌍 Cuisine
- 🥗 Dietary preference
- 👥 Servings
- ⏱️ Cooking time

…and Gemini cooks up a recipe for you. The matching notebook, `Call_LLM.ipynb`, walks through the first Gemini call and the recipe-generation function step by step.

### 💬 Chatbot with Memory — `13_Chatbot_with_memory/app.py`

A Streamlit chat app that sends the **full conversation history** with every message and keeps it for the browser session, so the bot stays in context. The companion notebook, `Chatbot_with_memory.ipynb`, shows how history is preserved between Gemini calls.

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.10 or newer
- A free Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)

### 1. Clone the repository

```bash
git clone https://github.com/adeebmansoor/Python_Tutorial_AI.git
cd Python_Tutorial_AI
```

### 2. Create a virtual environment *(recommended)*

**Windows (PowerShell)**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Add your API key

Copy `.env.example` to `.env` and add your key:

```env
GEMINI_API_KEY=your_api_key
```

> The apps also accept `GOOGLE_API_KEY` as an environment variable.

### 5. Run an app

From the project root:

```bash
# Recipe generator
streamlit run 10_Call_LLM/app.py

# Chatbot with memory
streamlit run 13_Chatbot_with_memory/app.py
```

> On Windows you can use backslashes too: `streamlit run 10_Call_LLM\app.py`

To explore the notebooks, open any module folder in VS Code or run `jupyter notebook`.

---

## 📂 Project Structure

```text
Python_Tutorial_AI/
├── 1_Datatypes/
├── 2_For_Loop/
├── 3_Dictionary_&_Tuples/
├── 4_Exercise_1/
├── 5_Functions/
├── 6_Args_&_Kargs/
├── 7_Exercise_2/
├── 8_Classes_&_Functions/
├── 9_Exercise_3/
├── 10_Call_LLM/                # Notebook + Streamlit recipe app
├── 11_Error_Handling/
├── 12_Exercise_4/
├── 13_Chatbot_with_memory/     # Notebook + Streamlit chat app
├── 14_Exercise_5/
├── 15_Structured_Output/
├── 16_Exercise_6/
├── 17_File_Handling/
├── 18_Exercise_7/
├── 19_Calling_API/
├── 20_Exercise_8/
├── 21_FastAPI/
├── 22_Database_Interaction/
├── 23_Exercise_9/
├── .env.example                # Template for your API key
├── requirements.txt
└── README.md
```

---

## 🔐 Security Notes

- Never commit your `.env` file. It is already covered by `.gitignore`, but double-check before pushing.
- Never share your API key publicly. If it ever leaks, revoke it in Google AI Studio and generate a new one.

---

## 👨‍💻 Author

**Adeeb Mansoor**

[![GitHub](https://img.shields.io/badge/GitHub-adeebmansoor-181717?logo=github&logoColor=white)](https://github.com/adeebmansoor/)

---

<div align="center">

⭐ If this repo helped you learn something, consider giving it a star!

</div>
