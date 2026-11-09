import pytest


@pytest.fixture
def manager_db():
    fake_db.clear()
    yeild
    fake_db.clear()
    print("\nDB cleaned after test")

def test_add_and_get_user(manager_db):
    add_user("u1", "Rit Kumar")
    name = get_user("u1")
    assert name == "Rit Kumar"

    

