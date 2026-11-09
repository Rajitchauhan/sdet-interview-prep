import os
from dataclasses import dataclass, field


@dataclass(frozen=True)
class User:
    username: str
    password: str = field(repr=False)


def get_user(kind: str = "standard") -> User:
    users = {
        "standard": User("standard_user", os.environ.get("STANDARD_USER_PASSWORD", "secret_sauce")),
        "locked": User("locked_user", os.environ.get("LOCKED_USER_PASSWORD", "secret_sauce")),
    }
    return users[kind]
