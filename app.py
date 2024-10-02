from flask import Flask, request, redirect, jsonify, render_template
from dotenv import load_dotenv
from openai import OpenAI
import os
import sqlite3


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

load_dotenv()

# Store the chat session history in a list.
history = [{
  "role": "system",
  "content": "You are a helpful assistant."
}]

# Connect to an existing SQLite database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

#
@app.route('/', methods=['GET', 'POST'])
def index():
    global history
    read()

    if request.method == 'POST':
        message = request.form.get('message')

        if message:
            history.append({
                'role': 'user',
                'content': message
            })
            response()
            return redirect('/')

    write(history)
    return render_template('index.html', history=history)

# Get a response from ChatGPT, show it and save it to the chat session history.
def response():
    global history
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
        history.append({
            'role': 'assistant',
            'content': response.choices[0].message.content
        })
        return redirect('/')

# Read previous chat history sessions from the database.
def read():
    global history
    cursor.execute('SELECT id, role, content FROM history')
    cursor.fetchall()
    # TODO: @fedtti - Save data to the history.


# Write the latest chat history session to the database.
def write(history):
    cursor.execute('CREATE TABLE IF NOT EXIST history(id INT PRIMARY KEY AUTOINCREMENT, role TEXT, content TEXT)')

    if history:
        cursor.executemany('INSERT INTO history VALUES(?, ?, ?)', history)
        connection.commit()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
