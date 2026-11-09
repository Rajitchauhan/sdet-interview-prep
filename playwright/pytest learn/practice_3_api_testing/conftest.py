import pytest 

@pytest.fixture
def api_base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def sample_payload():
    return {
    "title": "SDET Automation Guide",
    "body": "Pytest with Requests",
    "userId": 1,
}
