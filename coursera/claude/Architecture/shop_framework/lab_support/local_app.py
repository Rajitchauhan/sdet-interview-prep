"""LAB ONLY: demo app ko local start karta hai. Asli project me ye file nahi hogi (BASE_URL set hoga)."""
import os
import sys
import threading
from pathlib import Path


def pytest_configure(config):
    if os.environ.get("BASE_URL"):
        return   # tum kisi asli environment ko test kar rahe ho

    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app_under_test"))
    import server

    srv = server.create_server()          # port 0 = koi bhi free port
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    os.environ["BASE_URL"] = f"http://127.0.0.1:{srv.server_port}"
