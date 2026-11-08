"""CORE layer: safe Allure step decorator."""
import functools

import allure


def step(title: str):
    """Allure step, jo function ke arguments report me NAHI daalta (password leak se bachav)."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with allure.step(title):
                return func(*args, **kwargs)

        return wrapper

    return decorator
