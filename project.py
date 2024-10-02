from flask import Flask, request, redirect, render_template
from dotenv import load_dotenv
from openai import OpenAI
import os
import sqlite3


history = [{
    'role': 'system',
    'content': 'You are a helpful assistant'
}]


def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    @app.after_request
    def after_request(response):
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Expires'] = 0
        response.headers['Pragma'] = 'no-cache'
        return response

    @app.route('/', methods=['GET', 'POST'])
    def index():
        global history

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
        else:
            read()

        return render_template('index.html', history=history)

    return app


def main():
    app = create_app()
    app.run(debug=True)


load_dotenv()


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


# Connect to an existing SQLite database or create a new one.
with sqlite3.connect('database.db', check_same_thread=False) as connection:
    cursor = connection.cursor()


# Create a table if it does not exist yet in the existing database.
def create():
    cursor.execute('CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY AUTOINCREMENT, role TEXT, content TEXT)')
    return 0


# Write the latest chat history session to the database.
def write(message):
    create()

    if message:
        cursor.execute('INSERT INTO history(role, content) VALUES(:role, :content)', message)
        connection.commit()

    return 0


# Read previous chat history sessions from the database (if any).
def read():
    global history
    create()
    cursor.execute('SELECT id, role, content FROM history')
    items = cursor.fetchall()

    for item in items:
        history.append({
            'role': item[1],
            'content': item[2]
        })
    return 0


if __name__ == '__main__':
    main()
