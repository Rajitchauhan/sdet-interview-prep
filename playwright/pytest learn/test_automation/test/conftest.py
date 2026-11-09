import pytest
@pytest.fixture
def task():
    return   {
            "id": 1,
            "title": "SDET",
            "completed": False
        }

@pytest.fixture
def api_base_url():
    return "https://jsonplaceholder.typicode.com"
