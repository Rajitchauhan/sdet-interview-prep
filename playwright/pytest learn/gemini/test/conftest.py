
import pytest 

@pytest.fixture
def base_url():
    return "[https://api.testing.com/v1](https://api.testing.com/v1)"


#ye test file mai hoga.

def test_endpoint_url(base_url):
    # result = base_url()  bcz ye automatcally callho jayega base_url 

    assert "testing.com" in base_url