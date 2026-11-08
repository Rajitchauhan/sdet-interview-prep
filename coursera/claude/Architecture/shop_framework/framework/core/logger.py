"""CORE layer: logging. Library code handler configure NAHI karta."""
import logging


def get_logger(name: str) -> logging.Logger:
    # Level aur format pytest.ini (log_level, log_format) se aate hain.
    return logging.getLogger(f"shopfw.{name}")
