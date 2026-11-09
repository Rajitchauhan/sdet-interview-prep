import pytest 
import requests 

def test_get_user_details():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)

    assert response.status_code == 200  , "expected 200"

    data = response.json()

    assert data['id'] == 1

    assert "email" in data

