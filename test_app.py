import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"TaskManager API" in response.data

def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200