from project import create_app
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


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
