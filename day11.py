import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv(r"C:\Users\manoj\Desktop\workspace\sikil\.env")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Business info - this is what you'd change per client
BUSINESS_INFO = """
Business Name: Manoj's Coaching Center
Location: Hisar, Haryana
Timings: Mon-Sat, 9am to 7pm
Courses: Python, AI, Web Development
Fees: Python - 3000rs, AI - 5000rs, Web Dev - 4000rs
Contact: 9999999999
Special Offer: First class is free!
"""

st.title("Coaching Center Assistant")
st.caption("Ask me anything about our courses!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask about courses, fees, timings...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": f"""You are a helpful assistant for a business.
            Answer questions using ONLY the information below.
            If something is not mentioned, say 'Please call us for more details.'
            Be friendly, short and helpful.

            Business Info:
            {BUSINESS_INFO}
            """},
        ] + st.session_state.messages
    )

    ai_reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})

    with st.chat_message("assistant"):
        st.write(ai_reply)