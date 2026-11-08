"""CONFIG layer: environment ke hisaab se saari settings ek hi jagah."""
import os
from dataclasses import dataclass
from functools import lru_cache

# Har environment ka default URL (ye placeholders hain, apni asli URLs yahan likho)
ENVIRONMENTS = {
    "local": {"base_url": "http://127.0.0.1:8000"},
    "qa": {"base_url": "https://qa.shop.example.com"},
    "staging": {"base_url": "https://staging.shop.example.com"},
}


@dataclass(frozen=True)
class Settings:
    env: str
    base_url: str
    api_url: str
    ui_timeout_ms: int
    api_timeout_s: float


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    env = os.environ.get("TEST_ENV", "local")
    if env not in ENVIRONMENTS:
        raise ValueError(f"Unknown TEST_ENV={env!r}. Valid: {sorted(ENVIRONMENTS)}")

    base_url = os.environ.get("BASE_URL", ENVIRONMENTS[env]["base_url"]).rstrip("/")
    return Settings(
        env=env,
        base_url=base_url,
        api_url=os.environ.get("API_URL", base_url).rstrip("/"),
        ui_timeout_ms=int(os.environ.get("UI_TIMEOUT_MS", "5000")),
        api_timeout_s=float(os.environ.get("API_TIMEOUT_S", "10")),
    )
