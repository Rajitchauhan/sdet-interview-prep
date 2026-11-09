from gemini import password_check

def test_valid_password():
    result = password_check('rajit1234')
    assert result is True, "password is valid"

def test_invalid_password():
    result = password_check('raj234')
    assert result is False, "password is not valid"
    