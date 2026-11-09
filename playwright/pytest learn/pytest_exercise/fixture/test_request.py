import pytest 

@pytest.fixture 
def info(request):
    print("this is test name : " ,request.node.name)

def test_login(info):
    pass

def test_profile(info):
    pass

def test_logout(info):
    pass

@pytest.fixture(params=['admin' , 'user','guest'])
def role(request):
    return request.param

def test_role(role):
    print(role)