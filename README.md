# Chatbot UI
#### Video Demo:
#### Description:

Chatbot UI is a web interface to interact with ChatGPT written in Python.

##### `.editorconfig`

This file sets the indentation rules for Visual Studio Code (or any other compatible editor) with [EditorConfig](https://editorconfig.org/).

##### `.env.example`

This file include the available API key that must be associated with a valid value to enable the provider. **Chatbot UI won't work without an API key**. It musts be renamed to `.env` before starting.

##### `app.py`

Symbolik link to `project.py` to allow the use of the `flask run` command.

##### `database.db`

SQLite database that stores the conversations (it will be created on the first run).

##### `project.py`

This file handles the interaction between humans and the chatbot. It includes third party libraries (such as [Flask](https://flask.palletsprojects.com/) and [Markdown](https://pypi.org/project/Markdown/)) to prompt the user for questions.

##### `requirements.txt`

This file list the project dependencies to install.

##### `test_project.py`

This file provide some unit tests to check some of the project functionalities via [pytest](https://pytest.org).

##### `static/css/style.css`

Style for the template file in CSS.

##### `static/img/openai.svg`

Avatar for the OpenAI assistant in SVG.

##### `templates/index.html`

Template for the web interface in HTML and Jinja.

#### Usage

Downloaded the sources, you need to install the dependencies by running:

```bash
$ pip install -r requirements.txt
```

Then, to run the app you must rename `.env.example` to `.env` and add your secret key.

```bash
GITHUB_TOKEN=
```

Finally, you can execute the binary.

```bash
$ python project.py
```

or

```bash
$ flask run
```

It has been tested with Python 3.9.6.
