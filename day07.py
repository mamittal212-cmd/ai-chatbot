import os
from datetime import datetime
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
folder = r"C:\Users\manoj\Desktop\workspace\chats"
os.makedirs(folder, exist_ok=True)

def show_menu():
    print("\n" + "="*40)
    print("       🤖 CHILL AI CHATBOT")
    print("="*40)
    print("  1. Start new chat")
    print("  2. Read previous chats")
    print("  3. Exit")
    print("="*40)
    return input("Choose (1/2/3): ").strip()

def read_previous_chats():
    files = os.listdir(folder)
    if not files:
        print("\nNo previous chats found.")
        return
    print("\nYour previous chats:")
    for i, file in enumerate(files):
        print(f"  {i+1}. {file}")
    choice = input("\nEnter number to read (or Enter to go back): ")
    if choice.strip().isdigit():
        index = int(choice) - 1
        if 0 <= index < len(files):
            with open(os.path.join(folder, files[index]), "r", encoding="utf-8") as f:
                print("\n" + "="*40)
                print(f.read())
                print("="*40)

def start_chat():
    conversation_history = [
        {"role": "system", "content": "you are a chill boy saying serious things in a fun way."}
    ]
    log_filename = os.path.join(folder, f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    print(f"\nChat started! Type 'quit' to go back to menu.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("AI: peace out ✌️\n")
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

# Main loop
while True:
    choice = show_menu()
    if choice == "1":
        start_chat()
    elif choice == "2":
        read_previous_chats()
    elif choice == "3":
        print("\nAI: later! ✌️")
        break
    else:
        print("invalid choice, try again")
