import openai

openai.api_key = "your-api-key-here"

conversation_history = [
    {"role": "system", "content": "You are a friendly and intelligent assistant. Always be polite and helpful."},
]

def chat_with_gpt(user_input):
    """
    Function to interact with OpenAI's GPT model.
    """
   
    conversation_history.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        max_tokens=150,
        temperature=0.7,
    )

    bot_response = response.choices[0].message["content"]
    conversation_history.append({"role": "assistant", "content": bot_response})

    return bot_response

print("Welcome to the Intelligent Chatbot! I'm here to help you.")
user_name = input("Bot: What's your name? ")
print(f"Bot: Nice to meet you, {user_name}! How can I assist you today?")

while True:
    user_input = input(f"{user_name}: ")
    if user_input.lower() in ["exit", "bye", "goodbye"]:
        print(f"Bot: Goodbye, {user_name}! Have a great day!")
        break
    try:
        response = chat_with_gpt(user_input)
        print(f"Bot: {response}")
    except Exception as e:
        print(f"Bot: Sorry, {user_name}, I encountered an error. Please try again later.")