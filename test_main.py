from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"user_id": 1, "name": "User 1"}

def test_create_user():
    response = client.post("/users/", json={"name": "John"})
    assert response.status_code == 200
    assert response.json()["message"] == "User created"

