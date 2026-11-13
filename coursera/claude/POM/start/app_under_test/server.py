"""Chhota demo shop: static UI + JSON API. Ye FRAMEWORK ka hissa NAHI, ye 'application under test' hai."""
import json
import secrets
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

STATIC_DIR = Path(__file__).parent / "static"

PRODUCTS = [
    {"id": "backpack", "name": "Backpack", "price": 29.99},
    {"id": "bike-light", "name": "Bike Light", "price": 9.99},
    {"id": "onesie", "name": "Onesie", "price": 7.99},
]
USERS = {"standard_user": "secret_sauce", "locked_user": "secret_sauce"}
LOCKED = {"locked_user"}


class State:
    def __init__(self):
        self.lock = threading.Lock()
        self.tokens = {}      # token -> username
        self.carts = {}       # token -> [product ids]
        self.orders = []      # [{order_id, user, items}]
        self.next_order_id = 1001


class Handler(BaseHTTPRequestHandler):
    state = State()

    def log_message(self, *args):
        pass

    # ---------- helpers ----------
    def _send(self, status, payload=None, content_type="application/json"):
        body = b"" if payload is None else (
            payload if isinstance(payload, bytes) else json.dumps(payload).encode())
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _body(self):
        length = int(self.headers.get("Content-Length", 0))
        if not length:
            return {}
        try:
            return json.loads(self.rfile.read(length))
        except json.JSONDecodeError:
            return {}

    def _token(self):
        auth = self.headers.get("Authorization", "")
        token = auth.removeprefix("Bearer ").strip() if auth.startswith("Bearer ") else None
        return token if token in self.state.tokens else None

    def _cart_payload(self, token):
        items = self.state.carts.setdefault(token, [])
        return {"items": list(items), "count": len(items)}

    # ---------- routes ----------
    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/":
            path = "/index.html"
        if path.endswith(".html") and (STATIC_DIR / path.lstrip("/")).is_file():
            return self._send(200, (STATIC_DIR / path.lstrip("/")).read_bytes(), "text/html; charset=utf-8")
        if path == "/api/products":
            return self._send(200, PRODUCTS)
        token = self._token()
        if path == "/api/cart":
            return self._send(200, self._cart_payload(token)) if token else self._send(401, {"error": "Unauthorized"})
        if path == "/api/orders":
            if not token:
                return self._send(401, {"error": "Unauthorized"})
            user = self.state.tokens[token]
            return self._send(200, [o for o in self.state.orders if o["user"] == user])
        self._send(404, {"error": "Not found"})

    def do_POST(self):
        path = urlparse(self.path).path
        data = self._body()
        with self.state.lock:
            if path == "/api/login":
                user, pwd = data.get("username"), data.get("password")
                if user in LOCKED:
                    return self._send(423, {"error": "Sorry, this user has been locked out."})
                if USERS.get(user) != pwd or user is None:
                    return self._send(401, {"error": "Username and password do not match"})
                token = secrets.token_hex(8)
                self.state.tokens[token] = user
                self.state.carts[token] = []
                return self._send(200, {"token": token})
            token = self._token()
            if not token:
                return self._send(401, {"error": "Unauthorized"})
            if path == "/api/cart":
                pid = data.get("product_id")
                if pid not in {p["id"] for p in PRODUCTS}:
                    return self._send(404, {"error": "Unknown product"})
                cart = self.state.carts.setdefault(token, [])
                if pid not in cart:
                    cart.append(pid)
                return self._send(201, self._cart_payload(token))
            if path == "/api/checkout":
                cart = self.state.carts.setdefault(token, [])
                if not cart:
                    return self._send(400, {"error": "Cart is empty"})
                order = {"order_id": self.state.next_order_id,
                         "user": self.state.tokens[token], "items": list(cart)}
                self.state.next_order_id += 1
                self.state.orders.append(order)
                self.state.carts[token] = []
                return self._send(201, {"order_id": order["order_id"], "items": order["items"]})
        self._send(404, {"error": "Not found"})

    def do_DELETE(self):
        path = urlparse(self.path).path
        with self.state.lock:
            token = self._token()
            if not token:
                return self._send(401, {"error": "Unauthorized"})
            if path == "/api/cart":
                self.state.carts[token] = []
                return self._send(200, self._cart_payload(token))
            if path.startswith("/api/cart/"):
                pid = path.rsplit("/", 1)[-1]
                cart = self.state.carts.setdefault(token, [])
                if pid in cart:
                    cart.remove(pid)
                return self._send(200, self._cart_payload(token))
        self._send(404, {"error": "Not found"})


def create_server(host="127.0.0.1", port=0):
    return ThreadingHTTPServer((host, port), Handler)


if __name__ == "__main__":
    server = create_server(port=8000)
    print(f"ShopDemo chal raha hai: http://127.0.0.1:{server.server_port}")
    server.serve_forever()
