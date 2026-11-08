"""DATA layer: test users. Password pehle environment variable se, nahi to sirf DEMO default."""
import os
from dataclasses import dataclass, field


@dataclass(frozen=True)
class User:
    username: str
    password: str = field(repr=False)   # repr/log/assert-diff me password nahi dikhega
    role: str = "customer"


def get_user(kind: str = "standard") -> User:
    users = {
        "standard": User("standard_user", os.environ.get("STANDARD_USER_PASSWORD", "secret_sauce")),
        "locked": User("locked_user", os.environ.get("LOCKED_USER_PASSWORD", "secret_sauce")),
    }
    try:
        return users[kind]
    except KeyError:
        raise ValueError(f"Unknown user kind {kind!r}. Valid: {sorted(users)}") from None
