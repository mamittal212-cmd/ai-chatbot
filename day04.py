from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation_history = [
    {"role": "system", "content": "you are a chill boy saying serious things in a fun way."}
]

print("Chatbot is ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        print("AI: peace out ✌️")
        break

    conversation_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history
    )

    ai_reply = response.choices[0].message.content
    
    conversation_history.append({"role": "assistant", "content": ai_reply})

    print(f"\nAI: {ai_reply}\n")
