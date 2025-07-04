import streamlit as st
import google.generativeai as genai

# Set your Gemini API key directly
GEMINI_API_KEY = "" #Paste the api key given in the document(just below the githublink).
genai.configure(api_key=GEMINI_API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI setup
st.set_page_config(page_title="AI Code Explainer", layout="centered")
st.title("🤖 AI Code Explainer (Gemini 1.5 Flash)")

st.write("Paste a code snippet (Python or JavaScript) and get a plain English explanation powered by Gemini 1.5 Flash.")

# Language selection
language = st.selectbox("Select Code Language", ["Autodetect","Python", "JavaScript","C","kotlin","Java"])

# Code input area
code_input = st.text_area("Paste your code here:", height=250)

# Explain button
if st.button("🧠 Explain Code"):
    if not code_input.strip():
        st.warning("Please enter some code to explain.")
    else:
        with st.spinner("Explaining the code using Gemini..."):
            prompt = f"Explain the following {language} code in simple, beginner-friendly English:\n\n{code_input}"
            try:
                response = model.generate_content(prompt)
                st.subheader("📘 Explanation")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
