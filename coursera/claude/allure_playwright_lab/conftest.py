import functools
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import allure
import pytest

APP_DIR = Path(__file__).parent / "demo_app"


# ---------------------------------------------------------------
# PART 1: demo app ko local server par chalana (base_url fixture)
# ---------------------------------------------------------------
class _QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass  # console me server logs nahi chahiye


@pytest.fixture(scope="session")
def base_url():
    handler = functools.partial(_QuietHandler, directory=str(APP_DIR))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)  # port 0 = koi bhi free port
    threading.Thread(target=server.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{server.server_port}"
    server.shutdown()


# ---------------------------------------------------------------
# PART 2: har test ke dauran browser ki baatein jama karna
# ---------------------------------------------------------------
@pytest.fixture(autouse=True)
def _evidence(request):
    if "page" not in request.fixturenames:      # API-only test: browser mat kholo
        yield
        return

    page = request.getfixturevalue("page")
    request.node.page_for_report = page          # hook ko page chahiye

    console_logs, network_errors = [], []
    request.node.console_logs = console_logs
    request.node.network_errors = network_errors

    page.on("console", lambda m: console_logs.append(f"[{m.type}] {m.text}"))
    page.on("pageerror", lambda e: console_logs.append(f"[pageerror] {e}"))
    page.on("requestfailed", lambda r: network_errors.append(f"FAILED {r.method} {r.url}"))
    page.on(
        "response",
        lambda r: network_errors.append(f"{r.status} {r.request.method} {r.url}")
        if r.status >= 400
        else None,
    )
    yield


# ---------------------------------------------------------------
# PART 3: test fail ho to evidence Allure me attach karna
# ---------------------------------------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)   # setup/call/teardown ka result yaad rakho

    page = getattr(item, "page_for_report", None)
    if page is None:
        return

    # (A) setup ya call me fail hua: page abhi zinda hai
    if report.failed and report.when in ("setup", "call"):
        try:
            allure.attach(page.screenshot(full_page=True), name=f"screenshot-{report.when}",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(page.url, name="page-url",
                          attachment_type=allure.attachment_type.TEXT)
            allure.attach(page.content(), name="page-html",
                          attachment_type=allure.attachment_type.HTML)
            allure.attach("\n".join(item.console_logs) or "(no console output)",
                          name="browser-console", attachment_type=allure.attachment_type.TEXT)
            allure.attach("\n".join(item.network_errors) or "(no network errors)",
                          name="network-errors", attachment_type=allure.attachment_type.TEXT)
        except Exception as exc:
            print(f"[evidence] attach fail hua: {exc}")

    # (B) teardown ke baad: browser context band, video aur trace files final
    if report.when == "teardown":
        failed = any(
            getattr(item, f"rep_{phase}", None) is not None
            and getattr(item, f"rep_{phase}").failed
            for phase in ("setup", "call")
        )
        out_dir = item.funcargs.get("output_path")
        if failed and out_dir:
            for f in Path(out_dir).glob("*"):
                if f.suffix == ".webm":
                    allure.attach.file(str(f), name="video",
                                       attachment_type=allure.attachment_type.WEBM)
                elif f.name == "trace.zip":
                    allure.attach.file(str(f), name="playwright-trace.zip",
                                       attachment_type=allure.attachment_type.ZIP)
