import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv(r"C:\Users\manoj\Desktop\workspace\sikil\.env")
print(os.getenv("GROQ_API_KEY"))
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Sidebar
st.sidebar.title("⚙️ Settings")

personality = st.sidebar.selectbox(
    "Choose AI Personality",
    [
        "Chill boy saying serious things in a fun way",
        "Strict professor who only uses bullet points",
        "Startup founder obsessed with money and growth",
        "10 year old who somehow knows everything",
        "Custom..."
    ]
)

if personality == "Custom...":
    personality = st.sidebar.text_area("Write your own personality:", "You are a helpful assistant.")

if st.sidebar.button("🔄 Reset Chat"):
    st.session_state.messages = []
    st.rerun()

# Main chat
st.title("🤖 Chill AI Chatbot")
st.caption(f"Current vibe: {personality}")

if "messages" not in st.session_state:
    st.session_state.messages = []

system_prompt = {"role": "system", "content": personality}

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Say something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[system_prompt] + st.session_state.messages
    )

    ai_reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})

    with st.chat_message("assistant"):
        st.write(ai_reply)