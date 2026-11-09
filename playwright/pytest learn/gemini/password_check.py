# auth.py
def check_password_length(password: str) -> bool:
    # Minimum 8 characters hone chahiye
    return len(password) >= 8