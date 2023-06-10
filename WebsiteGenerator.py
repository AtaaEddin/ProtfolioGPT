from flask import Flask, render_template, request 
import openai
from contexts import INIT_COMMANDS

openai.api_key = open('Key.txt', "r").read().strip("\n")

def chat(inp):
    message_history = INIT_COMMANDS
    # Append the input message to the message history
    message_history.append({"role": "user", "content": f"{inp}"})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history)
    reply_content = completion.choices[0].message.content
    return reply_content 

# create a new flask app and set the secret key
app = Flask(__name__)
app.secret_key = "mysecretkey"


# Define the homepage route for the Flask app
@app.route('/', methods=['GET', 'POST'])
def home():
    # Page's title:
    title = "ProtfolioGPT"
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        text = chat(prompt)
        return render_template('rendered_website.html', text = text)
    return render_template('home.html', title=title) 

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5001)

