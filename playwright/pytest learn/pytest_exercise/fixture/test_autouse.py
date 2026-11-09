import pytest

@pytest.fixture(scope='module' ,  autouse=True)
def setup():
    print("AUTOUSE FIXTURE")

def test_1():
    pass

def test_2():
    pass

def test_3():
    pass

