from starlette.testclient import TestClient

from main import app

client = TestClient(app)

def test_main_status_code():
    response = client.get('/')
    assert response.status_code == 200

def test_main_response_json():
    response = client.get('/')
    assert response.json() == {'hello': 'world'}

def test_list_todo_status_code():
    response = client.get('/list')
    assert response.status_code == 200

def test_list_todo_should_return_list():
    response = client.get('/list')
    assert type(response.json()) is list 