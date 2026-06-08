from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


user_question = input("Ask me anything: ")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "you are a chill boy saying serious things in a fun way."},
        {"role": "user", "content": user_question}
    ]
)

print("\nAI says:")
print(response.choices[0].message.content)
