from flask import Blueprint, request, render_template, redirect
from flaskr.db import get_db
from openai import OpenAI
from dotenv import load_dotenv
import os
import markdown


bp = Blueprint('index', __name__, url_prefix='/')

@bp.after_request
def after_request(response):
  response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
  response.headers['Expires'] = 0
  response.headers['Pragma'] = 'no-cache'
  return response


completions = [{
  'role': 'system',
  'content': 'You are a helpful assistant'
}]

@bp.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    message = request.form.get('message')
    if message:
      data = {
        'role': 'user',
        'content': message
      }
      completions.append(data)
      write(data)
      get_completion()
      return redirect('/')
  else:
    read()

    return render_template('base.html', completions=completions)


db = get_db()

def read():
  if len(completions) <= 1:
    items = db.execute('SELECT id, role, content FROM completions').fetchall()

    for item in items:
      completions.append({
        'role': item[1],
        'content': item[2]
      })

  return 0


load_dotenv()

def get_completion():
  token = os.getenv('GITHUB_TOKEN')
  endpoint = 'https://models.inference.ai.azure.com'
  model_name = 'gpt-4o'
  client = OpenAI(
    base_url=endpoint,
    api_key=token
  )
  response = client.chat.completions.create(
    messages = completions,
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
  )

  if response:
    data = {
      'role': 'assistant',
      'content': markdown.markdown(response.choices[0].message.content)
    }
    completions.append(data)
    write(data)

  return redirect('/')


def write(data):
  if data:
    db.execute('INSERT INTO completions (role, content) VALUES (:role, :content)', data)
    db.commit()

    return 0
