
# db.py
fake_db = {}


def add_user(user_id: str, name: str):
    fake_db[user_id] = name


def get_user(user_id: str):
    return fake_db.get(user_id)