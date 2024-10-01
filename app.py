from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

history = []


@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html', history=history)


if __name__ == '__main__':
    app.run(debug=True)
