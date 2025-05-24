import streamlit as st
import openai

st.set_page_config(page_title="Ask About Luis", layout="centered")
st.title("🧠 Ask Me About Luis")
st.write("This assistant can answer questions about Luis: his background, projects, skills, and more.")

openai.api_key = st.secrets["OPENAI_API_KEY"]

question = st.text_input("Ask a question:")

if question:
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant that answers only about Luis. "
                    "Luis is a bilingual full-stack developer and AI builder. "
                    "He co-founded Verskod and COMS, won Meta's Llama Impact Grant with BluEye ($100K), "
                    "and regularly attends hackathons and conferences like Talent Land. "
                    "He trains MMA, builds AI tools, and wants to launch a startup."
                )
            },
            {"role": "user", "content": question}
        ]
    )
    st.write("🤖", response.choices[0].message.content)
