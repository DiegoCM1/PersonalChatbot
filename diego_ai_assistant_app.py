import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Ask Diego's Assistant", layout="centered")

# Styling (dark floating bubble theme)
st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
        max-width: 600px;
        margin: auto;
        font-family: 'Segoe UI', sans-serif;
    }
    h1 {
        text-align: center;
        color: #000;
    }
    .stTextInput>div>div>input {
        font-size: 16px;
        padding: 12px;
    }
    .stButton button {
        background-color: black;
        color: white;
        font-size: 16px;
        padding: 8px 16px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("### 👋 Ask Me About Diego")
st.write("I'm a personal assistant trained on Diego's career, projects, and passions. Ask me anything!")

client = OpenAI(
    api_key=st.secrets["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1"
)

question = st.text_input("Type your question here:")

if question:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct:free",
            messages=[
                {"role": "system", "content": "You only answer about Diego. Diego is a bilingual full-stack developer, co-founder of Verskod and COMS, won Meta’s Llama Grant ($100K), builds AI tools, attends hackathons, and trains MMA."},
                {"role": "user", "content": question}
            ]
        )
        st.success("Here's what I found:")
        st.markdown(f"**🤖 {response.choices[0].message.content}**")
