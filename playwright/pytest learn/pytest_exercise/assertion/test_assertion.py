import pytest 

@pytest.fixture
def user(request):
    print(request.node.name)
    user = {
    "id": 101,
    "name": "Rajit",
    "role": "tester",
    "active": True,
    "skills": ["Python", "Pytest", "API"]
}
    return user 

def test_user(user):
    assert user['id'] == 101
    assert user['name'] == "Rajit"
    assert user['active'] == True 
    assert "Pytest" in user['skills']
    assert "Java" not in user['skills']
    assert  len(user['skills']) == 3 
    assert 'email' not in user.keys()

@pytest.fixture
def user_res():
    response_data = {
    "id": 101,
    "title": "Learn Pytest",
    "completed": False,
    "tags": ["python", "testing", "automation"]
}
    return response_data

def test_user_res(user_res):
    assert 'id' in user_res.keys()
    # assert type(user_res['id']) == int 
    assert isinstance(user_res["id"], int)
    assert user_res['id'] == 101 
    assert 'title' in user_res.keys() 
    assert user_res["title"] != "" 
    assert type(user_res['completed']) == bool
    assert 'testing' in user_res['tags']
    assert 'java' not in user_res['tags']
    assert len(user_res['tags']) == 3


    