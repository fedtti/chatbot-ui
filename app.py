from flask import Flask, request, redirect,render_template
from dotenv import load_dotenv
from openai import OpenAI
import os
import sqlite3
import json


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

load_dotenv()

# Connect to an existing SQLite database
connection = sqlite3.connect('database.db', check_same_thread=False)
cursor = connection.cursor()

history = [{
    'role': 'system',
    'content': 'You are a helpful assistant'
}]


#
@app.route('/', methods=['GET', 'POST'])
def index():
    global history
    read()

    if request.method == 'POST':
        message = request.form.get('message')

        if message:
            data = {
                'role': 'user',
                'content': message
            }
            history.append(data)
            write(data)
            response()
            return redirect('/')

    return render_template('index.html', history=history)

# Get a response from ChatGPT, show it and save it to the chat session history.
def response():
    token = os.getenv('GITHUB_TOKEN')
    endpoint = 'https://models.inference.ai.azure.com'
    model_name = 'gpt-4o'

    client = OpenAI(
        base_url=endpoint,
        api_key=token
    )

    response = client.chat.completions.create(
        messages = history,
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        model=model_name
    )

    if response:
        data = {
            'role': 'assistant',
            'content': response.choices[0].message.content
        }
        history.append(data)
        write(data)
        return redirect('/')


# Write the latest chat history session to the database.
def write(message):
    if message:
        cursor.execute('INSERT INTO history(role, content) VALUES(:role, :content)', message)
        connection.commit()


# Read previous chat history sessions from the database.
def read():
    global history
    cursor.execute('SELECT id, role, content FROM history')
    items = cursor.fetchall()

    for item in items:
        history.append({
            'role': item[1],
            'content': item[2]
        })


if __name__ == '__main__':
    app.run(debug=True)
