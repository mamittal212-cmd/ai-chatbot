import os
from datetime import datetime
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

folder = r"C:\Users\manoj\Desktop\workspace\chats"
os.makedirs(folder, exist_ok=True)

# Show previous chats
def show_previous_chats():
    files = os.listdir(folder)
    if not files:
        print("No previous chats found.\n")
        return
    print("Your previous chats:")
    for i, file in enumerate(files):
        print(f"  {i+1}. {file}")
    choice = input("\nEnter number to read a chat (or press Enter to skip): ")
    if choice.strip().isdigit():
        index = int(choice) - 1
        if 0 <= index < len(files):
            with open(os.path.join(folder, files[index]), "r", encoding="utf-8") as f:
                print("\n" + "="*40)
                print(f.read())
                print("="*40 + "\n")

show_previous_chats()

# Start new chat
conversation_history = [
    {"role": "system", "content": "you are a chill boy saying serious things in a fun way."}
]

log_filename = os.path.join(folder, f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
print(f"New chat started! Saving to: {log_filename}\n")

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

    with open(log_filename, "a", encoding="utf-8") as f:
        f.write(f"You: {user_input}\n")
        f.write(f"AI: {ai_reply}\n")
        f.write("-" * 40 + "\n")
