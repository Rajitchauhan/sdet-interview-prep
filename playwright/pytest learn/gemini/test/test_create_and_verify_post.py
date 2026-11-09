import pytest 
import requests

def test_create_and_verify_post():
    url  = "https://jsonplaceholder.typicode.com/posts"

    user_data = {"title": "SDET Mastery", "userId": 1}

    responce = requests.post(url , json=user_data)

    assert responce.status_code == 201 , "post created"

    id_data = responce.json()['id'] # capture id

    get_responce = requests.get(f"{url}/1")

    assert get_responce.status_code == 200 , "get the post data"

    data = get_responce.json()
    assert "title" in data  


