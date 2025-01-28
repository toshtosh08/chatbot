from flask import Flask, request, render_template
import openai

app = Flask(__name__)

openai.api_key = "your-api-key-here"

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = chat_with_gpt(user_input)
        return render_template("index.html", user_input=user_input, bot_response=bot_response)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)