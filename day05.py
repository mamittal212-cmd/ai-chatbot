from groq import Groq
from datetime import datetime
import os
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation_history = [
    {"role": "system", "content": "you are a chill boy saying serious things in a fun way."}
]

# Create a log file with today's date and time


folder = r"C:\Users\manoj\Desktop\workspace\chats"
os.makedirs(folder, exist_ok=True)
log_filename = os.path.join(folder, f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

print(f"Chatbot ready! Saving to: {log_filename}")
print("Type 'quit' to exit.\n")

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

    # Save to file after every message
    with open(log_filename, "a", encoding="utf-8") as f:
        f.write(f"You: {user_input}\n")
        f.write(f"AI: {ai_reply}\n")
        f.write("-" * 40 + "\n")
