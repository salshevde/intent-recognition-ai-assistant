import pytest
import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8000/api/v1"

@pytest.fixture
def test_user():
    return {
        "username": "testuser",
        "password": "testpass123"
    }


def test_home():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_register_user(test_user):
    response = requests.post(f"{BASE_URL}/register", json=test_user)
    assert response.status_code == 200
    assert "username" in response.json()
    assert response.json()["username"] == test_user["username"]

def test_register_duplicate_user(test_user):
    # First registration
    requests.post(f"{BASE_URL}/register", json=test_user)
    # Attempt duplicate registration
    response = requests.post(f"{BASE_URL}/register", json=test_user)
    assert response.status_code == 422
    assert "error" in response.json()

# def test_login_success(test_user):
#     # Register first
#     requests.post(f"{BASE_URL}/register", json=test_user)
#     # Then login
#     response = requests.post(f"{BASE_URL}/login", json=test_user)
#     assert response.status_code == 200
#     assert "token" in response.json()

# def test_login_invalid_credentials():
#     invalid_user = {
#         "username": "wronguser",
#         "password": "wrongpass"
#     }
#     response = requests.post(f"{BASE_URL}/login", json=invalid_user)
#     assert response.status_code == 401
#     assert "error" in response.json()

# def test_process_input(auth_token):
#     headers = {"Authorization": f"Bearer {auth_token}"}
#     test_data = {
#         "text": "Hello, how are you?",
#         "username": "testuser"
#     }
#     response = requests.post(f"{BASE_URL}/process", json=test_data, headers=headers)
#     assert response.status_code == 200
#     assert "intent" in response.json()
#     assert "confidence" in response.json()
#     assert "response" in response.json()
#     assert "entities" in response.json()

# def test_process_input_anonymous():
#     test_data = {
#         "text": "Hello, how are you?"
#     }
#     response = requests.post(f"{BASE_URL}/process", json=test_data)
#     assert response.status_code == 200
#     assert response.json()["username"] == "anonymous"

# def test_get_chat_history(auth_token, test_user):
#     headers = {"Authorization": f"Bearer {auth_token}"}
#     # First make some chat entries
#     test_data = {
#         "text": "Test message",
#         "username": test_user["username"]
#     }
#     requests.post(f"{BASE_URL}/process", json=test_data, headers=headers)
    
#     # Then get chat history
#     response = requests.post(f"{BASE_URL}/chat/{test_user['username']}", headers=headers)
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)
#     assert len(response.json()) > 0
#     assert "username" in response.json()[0]
#     assert "input_text" in response.json()[0]
#     assert "response" in response.json()[0]
#     assert "timestamp" in response.json()[0]

# def test_get_chat_history_invalid_user(auth_token):
#     headers = {"Authorization": f"Bearer {auth_token}"}
#     response = requests.post(f"{BASE_URL}/chat/nonexistentuser", headers=headers)
#     assert response.status_code == 404
#     assert "error" in response.json()

# def test_process_input_invalid_token():
#     headers = {"Authorization": "Bearer invalid_token"}
#     test_data = {
#         "text": "Hello",
#         "username": "testuser"
#     }
#     response = requests.post(f"{BASE_URL}/process", json=test_data, headers=headers)
#     assert response.status_code == 401
#     assert "error" in response.json()

# def test_input_validation():
#     # Test missing required fields
#     response = requests.post(f"{BASE_URL}/process", json={})
#     assert response.status_code == 422
#     assert "error" in response.json()

#     # Test invalid data types
#     invalid_data = {
#         "text": 123,  # Should be string
#         "username": ["invalid"]  # Should be string
#     }
#     response = requests.post(f"{BASE_URL}/process", json=invalid_data)
#     assert response.status_code == 422
#     assert "error" in response.json()