import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv(r"C:\Users\manoj\Desktop\workspace\sikil\.env")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# =============================================
# EDIT THIS SECTION PER CLIENT - THAT'S IT
# =============================================
BUSINESS_NAME = "Manoj's Coaching Center"
BUSINESS_TAGLINE = "Learn Python, AI & Web Dev from scratch"
BUSINESS_COLOR = "#6C63FF"
BUSINESS_INFO = """
Location: Panipat, Haryana
Timings: Mon-Sat, 9am to 7pm
Courses: Python, AI, Web Development
Fees: Python - 3000rs, AI - 5000rs, Web Dev - 4000rs
Contact: 9999999999
Special Offer: First class is free!
Trainer: Manoj Mittal, CSE student with AI expertise
"""
# =============================================

# Page config
st.set_page_config(
    page_title=BUSINESS_NAME,
    page_icon="🤖",
    layout="centered"
)

# Header
st.markdown(f"""
    <div style='text-align: center; padding: 1rem;'>
        <h1 style='color: {BUSINESS_COLOR};'>🤖 {BUSINESS_NAME}</h1>
        <p style='color: gray;'>{BUSINESS_TAGLINE}</p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# Suggested questions
st.markdown("**Quick questions:**")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("💰 Fees?"):
        st.session_state.quick = "What are the fees for all courses?"
with col2:
    if st.button("⏰ Timings?"):
        st.session_state.quick = "What are the timings?"
with col3:
    if st.button("🎁 Any offers?"):
        st.session_state.quick = "Any special offers or free trials?"

st.divider()

# Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Handle quick question buttons
user_input = st.chat_input("Ask me anything...")
if "quick" in st.session_state:
    user_input = st.session_state.quick
    del st.session_state.quick

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": f"""You are a friendly assistant for {BUSINESS_NAME}.
            Answer using ONLY the info below. Keep answers short and friendly.
            If not mentioned, say 'Please call us for more details.'
            Business Info: {BUSINESS_INFO}"""},
        ] + st.session_state.messages
    )

    ai_reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})

    with st.chat_message("assistant"):
        st.write(ai_reply)