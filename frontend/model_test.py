import ollama

user_input = input("/...")

messages=[
    {"role":"user",
     "content":user_input}
]
response = ollama.chat(
                    model="gemma3b",
                    messages=messages,
                )

print(response["message"]["content"])