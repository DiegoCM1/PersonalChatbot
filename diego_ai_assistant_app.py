import streamlit as st
from openai import OpenAI  # New import style for >=1.0.0

st.set_page_config(page_title="Ask About Luis", layout="centered")

st.title("🧠 Ask Me About Luis")
st.write("This assistant can answer questions about Luis: his background, projects, skills, and more.")

# Set up OpenAI client for OpenRouter
client = OpenAI(
    api_key=st.secrets["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1"
)

question = st.text_input("Ask a question:")

if question:
    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct:free",  # Free OpenRouter-compatible model
        messages=[
            {"role": "system", "content": "You are an assistant that only answers questions about Luis. Luis is a bilingual full-stack developer and AI builder. He co-founded Verskod and COMS, won Meta's Llama Impact Grant with BluEye ($100K), and regularly attends hackathons and conferences like Talent Land. He trains MMA, builds AI tools, and wants to launch a startup."},
            {"role": "user", "content": question}
        ]
    )

    st.write("🤖", response.choices[0].message.content)
