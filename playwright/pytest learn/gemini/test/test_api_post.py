import requests
import pytest

@pytest.fixture 
def user_payload():

    return {"name": "Rit Kumar", "job": "SDET Engineer"} 

def test_create_user(user_payload):
    url = "https://jsonplaceholder.typicode.com/users"

    responce = requests.post(url , json= user_payload)

    assert responce.status_code == 201 , "data/user profile created"

    data = responce.json()
    assert data['name'] == "Rit Kumar"