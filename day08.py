import streamlit as st
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("🤖 Chill AI Chatbot")
st.caption("serious things said in a fun way")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "you are a chill boy saying serious things in a fun way."}
    ]

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# Chat input
user_input = st.chat_input("Say something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )

    ai_reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})

    with st.chat_message("assistant"):
        st.write(ai_reply)
