import pytest 

@pytest.fixture
def databse():
    print("database connected")

    print("database running")
    yield
    print("database cloased")

def test_db(databse):
    assert 2 == 2

@pytest.fixture
def config():
    return "www.google.com/"

@pytest.fixture
def api_config(config):
    return {'url' : config ,'name':'RK' , 'age':26}

def test_api(api_config):
    assert api_config['name'] == 'RK'
    assert api_config['url'] == "www.google.com/"
   