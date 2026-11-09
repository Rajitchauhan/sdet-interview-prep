
# calculator.py

def get_number():
    return 10

def calculate():
    return get_number() * 2


# Patch get_number
# ↓
# make it return 5
# ↓
# call calculate()
# ↓
# assert result == 10

from unittest.mock import patch

def test_calc():
    with patch('calculator.get_number') as mock_get_number:
        mock_get_number.return_value = 5

        result = calculator.calculate()

        assert result == 10




# user_api.py

import requests

def get_user():
    response = requests.get("https://example.com/user")
    return response.json()


def test_api():
    with patch('user_api.get_user') as mock_get:
        mock_get.return_value.json.return_value =    {
    "id": 101,
    "name": "Rajit"
} 
        result = user_api.get_user()

        assert result['id'] == 101
        assert result['name'] == "Rajit"
        mock_get.assert_called_once()
# Test requirements:

# Don't hit real internet.
# Patch requests.get.
# Make fake response return:

# {
#     "id": 101,
#     "name": "Rajit"
# }

# Call actual get_user().
# Assert ID and name.
# Verify requests.get() was called exactly once.
# Verify it was called with the correct URL.


########### right code ###########################
def test_api():
    with patch("user_api.requests.get") as mock_get:

        mock_get.return_value.json.return_value = {
            "id": 101,
            "name": "Rajit"
        }

        result = user_api.get_user()

        assert result["id"] == 101
        assert result["name"] == "Rajit"

        mock_get.assert_called_once()
        mock_get.assert_called_once_with(
            "https://example.com/user"
        )