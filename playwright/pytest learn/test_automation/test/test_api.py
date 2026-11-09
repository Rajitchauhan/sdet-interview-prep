import requests , pytest

@pytest.mark.smoke
def test_get_api(api_base_url):
    responce = requests.get(f"{api_base_url}/posts")

    assert responce.status_code == 200

    data = responce.json()

    # print(data)

    # assert type(data) is list
    assert isinstance(data , list)

    assert len(data) > 0

    assert 'id' in data[0] and 'title' in data[0] 

    # assert type(data[0]['id']) is int
    assert isinstance(data[0]['id'] , int) 

@pytest.mark.regression
def test_invalid_endpoint_returns_404(api_base_url):
    responce = requests.get(f'{api_base_url}/this-endpoint-does-not-exist')

    assert responce.status_code == 404


def test_post_api(api_base_url):
    payload = {
    "title": "Learn Pytest",
    "body": "API automation",
    "userId": 1
}

    responce = requests.post(f"{api_base_url}/posts" , json=payload)

    assert responce.status_code == 201

    # print(responce.json())

    data = responce.json()

    # assert isinstance(data , JSON)
    assert 'id' in data

    assert data['title'] == "Learn Pytest"

    assert data['body'] == "API automation"
    assert data["userId"] == 1



def test_get_users(api_base_url):
    response = requests.get(f'{api_base_url}/users')

    assert response.status_code == 200

    data = response.json()

    assert 'id' in data[0]
    # assert isinstance(data[0]['id']  , int)
    assert type(data[0]['id']) is int  
    assert 'name' in data[0] 
    assert 'email' in data[0]




def test_get_user(api_base_url):
    response = requests.get(f'{api_base_url}/users/1')

    assert response.status_code == 200

    data = response.json()
    # print(data)
    assert data['id'] == 1  
    assert 'name' in data 
    assert 'email' in data


@pytest.mark.parametrize('ids' , [1,2,3,5,10])
def test_get_user_by_id(api_base_url,ids):
    response = requests.get(f'{api_base_url}/users/{ids}')
    
    assert response.status_code == 200

    data = response.json()
    # print(data)

@pytest.mark.regression
def test_get_non_existing_user(api_base_url):
    response = requests.get(f'{api_base_url}/users/999999')

    assert response.status_code == 404 

@pytest.mark.smoke
def test_create_user(api_base_url):
    payload = {
    "name": "Rajit",
    "username": "rajit",
    "email": "rajit@example.com"
}
    response = requests.post(f'{api_base_url}/users' , json=payload)

    assert response.status_code == 201
    data = response.json()

    assert 'id' in data
    assert data['name'] == payload['name']
    assert data['username'] == payload['username']
    assert data['email'] == payload['email']
    # print(data)
# name == payload["name"]
# username == payload["username"]
# email == payload["email"]

    
    
