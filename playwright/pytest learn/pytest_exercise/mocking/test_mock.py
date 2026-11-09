from unittest.mock import Mock 
import pytest 

def test_calc():
    calc = Mock()
    calc.add.return_value = 5
    result =  calc.add(2 , 3)
    assert result == 5 

    calc.add.assert_called_once()
    calc.add.assert_called_once_with(2 ,3)

#side_effect for raises exceptions

def test_api():
    api = Mock()
    api.get_user.side_effect = RuntimeError("API Down")


###############################################
def send_notification(service):
    return service.send("Rajit")


def test_send_notification():
    api = Mock()
    api.send.return_value = "sent"

    api.send.assert_called_once()

    api.send.assert_called_once_with("Rajit")

########### right code ###############

def test_api():
    api = Mock()

    api.get_user.side_effect = RuntimeError("API Down")

    with pytest.raises(RuntimeError, match="API Down"):
        api.get_user()

def test_send_notification():
    api = Mock()
    api.send.return_value = "sent"
    result = send_notification(api)
    assert result == "sent"
    api.send.assert_called_once()
    api.send.assert_called_once_with("Rajit")