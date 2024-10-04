from app import create_app, create
import sqlite3
import pytest


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'TEMPLATES_AUTO_RELOAD': True
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200


def test_index_post(client):
    response = client.post('/', headers={'Content-Type': 'application/x-www-form-urlencoded'}, data='message=')
    assert response.status_code == 200


def test_create():
    create()
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('PRAGMA table_info(history)')
    history = cursor.fetchone()
    assert history is not None
