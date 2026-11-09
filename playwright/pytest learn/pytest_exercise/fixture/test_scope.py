import pytest 

@pytest.fixture
def counter():
    return "Fixture executed"
    # print("Fixture executed")

def test_one(counter):
    print(counter)

def test_two(counter):
    print(counter)
    

def test_three(counter):
    print(counter)

@pytest.fixture(scope='session')
def data_list():
    return []

def test_1(data_list):
    print(data_list)
    print('adding Rajit into list')
    data_list.append('Rajit')

def test_2(data_list):
    print(data_list)
    assert 'Rajit' in data_list