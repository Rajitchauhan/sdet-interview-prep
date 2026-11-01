# PROJECT 01 — RetailHub E-commerce SDET Automation
## Manual-first project: khud sochna, khud implement karna, khud debug karna (AI use nahi karna)

**Level target:** 2-year experience SDET / QA Automation Engineer  
**Primary stack:** Python, Pytest, Playwright (Python sync API), Requests, Git, GitHub Actions, Allure  
**Language:** Hinglish explanations; requirements and workplace artifacts realistic English  
**Learning mode:** Step-by-step. Is guide ko sequence mein follow karo. Pehle requirement samjho, phir test design, phir code. Direct final code copy-paste karke project complete mat samajhna.

> **Important honesty note:** Ye ek realistic training project aur simulated client engagement hai. Isse tumhe 2-year SDET role ke kaam ka practice milega, lekin sirf project complete karne se automatically 2 years ka employment experience claim nahi karna chahiye. Interview mein ise independently built end-to-end automation project ke roop mein explain karna.

---

# 0. Project ka overview

## 0.1 Client aur product

Tum ek mid-size online retail company **RetailHub** mein QA Automation Engineer join karte ho. Company web par electronics, home items aur accessories sell karti hai.

Company ke paas:
- Customer-facing web application
- Login / registration
- Product listing, search, filters, sorting
- Cart and checkout
- Order history
- Backend REST APIs
- QA environment
- GitHub-based development workflow

Development team har sprint mein features release karti hai. Manual regression mein bahut time lagta hai. Tumhara assignment hai reliable automation framework banana jo UI aur API dono ko cover kare.

## 0.2 Tumhara role kya hai?

Tum sirf scripts likhne wale tester nahi ho. Tum:
1. Product requirements read karoge.
2. Ambiguity identify karke questions raise karoge.
3. Acceptance criteria ko test scenarios mein convert karoge.
4. Risk-based test coverage decide karoge.
5. API aur UI tests automate karoge.
6. Test data aur environment manage karoge.
7. Failures debug karke root cause classify karoge.
8. Bugs ko reproducible evidence ke saath report karoge.
9. CI pipeline mein tests run karwaoge.
10. Reports aur quality risks stakeholders ko communicate karoge.

**Typical sprint workflow:** refinement → test analysis → test design → automation implementation → PR review → CI execution → defect triage → release sign-off.

## 0.3 Project deliverables

Project complete hone par repo mein ye deliverables honge:

- Requirement clarification log
- Test strategy and test plan
- Requirement Traceability Matrix (RTM)
- Manual test cases
- API test suite
- UI test suite
- Reusable Pytest fixtures
- Page Object Model
- Environment/configuration handling
- Logging and failure artifacts
- HTML/Allure reporting
- GitHub Actions CI workflow
- Bug reports
- README and execution guide
- Final QA summary / release recommendation

---

# 1. Environment and working agreement

## 1.1 Required tools

- Python 3.11+ recommended (stable release; beta interpreter use mat karna)
- VS Code
- Git
- Chrome or Chromium
- Playwright Python
- Pytest
- Requests
- `pytest-html` or Allure (we will start with HTML; Allure can be added later)
- GitHub account

Commands:

```bash
python --version
git --version
code --version
```

Create repository and environment:

```bash
mkdir retailhub-sdet
cd retailhub-sdet
git init
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install pytest playwright requests python-dotenv pytest-html
playwright install
```

Freeze dependencies:

```bash
pip freeze > requirements.txt
```

## 1.2 Proposed repository structure

Create this structure gradually; ek saath saari files mat banao.

```text
retailhub-sdet/
├── .github/
│   └── workflows/
│       └── tests.yml
├── config/
│   └── settings.py
├── data/
│   └── test_users.json
├── logs/
├── reports/
├── src/
│   ├── api/
│   │   └── clients.py
│   ├── pages/
│   │   ├── login_page.py
│   │   ├── products_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   └── utils/
│       └── logger.py
├── tests/
│   ├── api/
│   │   ├── test_products_api.py
│   │   └── test_auth_api.py
│   └── ui/
│       ├── test_login.py
│       ├── test_products.py
│       └── test_checkout.py
├── conftest.py
├── pytest.ini
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 1.3 Initial files

`.gitignore`:

```gitignore
.venv/
__pycache__/
.pytest_cache/
.env
allure-results/
reports/
logs/*.log
test-results/
playwright-report/
```

`.env.example`:

```env
BASE_URL=https://practicesoftwaretesting.com
API_BASE_URL=https://api.practicesoftwaretesting.com
HEADLESS=true
TIMEOUT_MS=10000
```

Copy `.env.example` to `.env`. Real secrets kabhi Git mein commit nahi karne.

`config/settings.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://practicesoftwaretesting.com")
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.practicesoftwaretesting.com")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
TIMEOUT_MS = int(os.getenv("TIMEOUT_MS", "10000"))
```

`pytest.ini`:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -ra
markers =
    smoke: critical happy-path tests
    regression: broader regression coverage
    api: API tests
    ui: browser UI tests
    negative: invalid-input and error-path tests
```

**Check:** `pytest --collect-only -q` abhi zero tests dikhaye to normal hai; abhi tests create nahi kiye.

---

# 2. Requirement Engineering — pehle requirement padhna seekho

## 2.1 Client requirement (realistic English)

**Feature ID:** RH-AUTH-001  
**Title:** Customer Login

**Business requirement:**  
Registered customers must be able to sign in using their email address and password. The application must prevent unauthenticated users from accessing account-specific pages.

**Acceptance criteria:**
- AC1: A registered active customer can log in with valid credentials.
- AC2: An invalid password must not create an authenticated session.
- AC3: An unknown email must not create an authenticated session.
- AC4: Email and password fields are mandatory.
- AC5: Password must be masked by default.
- AC6: Successful login must take the customer to an authenticated landing page.
- AC7: A customer must be able to log out.
- AC8: After logout, accessing an account-only page must require authentication.

## 2.2 Requirement ko kaise read karna hai?

Har requirement ko 5 questions se parse karo:

1. **Actor:** Kaun action kar raha hai? Registered customer.
2. **Precondition:** Action se pehle kya true hona chahiye? Account active hona chahiye.
3. **Action:** User kya karega? Email/password enter karke sign in.
4. **Expected result:** System kya karega? Session create aur authenticated page show.
5. **Negative/security behavior:** Invalid login ya logout ke baad kya nahi hona chahiye? Authenticated access nahi.

## 2.3 Ambiguity log — developer/product owner se kya poochoge?

| ID | Question | Why it matters |
|---|---|---|
| Q1 | Login email case-sensitive hai ya case-insensitive? | Input normalization |
| Q2 | Invalid login par exact error message kya hoga? | Assertion contract |
| Q3 | Account lockout policy hai? Kitne failed attempts? | Security and negative tests |
| Q4 | Session expiry kitni der mein hoti hai? | Session test |
| Q5 | Logout ke baad browser Back se protected content accessible hona chahiye? | Cache/session behavior |

**Workplace habit:** Requirement unclear ho to expected behavior invent mat karo. Question raise karo aur answer document karo.

## 2.4 Test scenarios

| Scenario ID | Scenario | Type | Priority |
|---|---|---|---|
| AUTH-01 | Valid active user login | Positive | P0 |
| AUTH-02 | Wrong password | Negative | P0 |
| AUTH-03 | Unknown email | Negative | P1 |
| AUTH-04 | Empty email | Validation | P1 |
| AUTH-05 | Empty password | Validation | P1 |
| AUTH-06 | Both fields empty | Validation | P1 |
| AUTH-07 | Password masked | UI/security | P2 |
| AUTH-08 | Logout | Positive | P0 |
| AUTH-09 | Protected page after logout | Security | P0 |
| AUTH-10 | Email with leading/trailing spaces | Boundary | P2 |

P0 = release-blocking critical path; P1 = important; P2 = lower risk / usability.

## 2.5 Detailed test case example

**TC ID:** AUTH-01  
**Title:** Login succeeds with valid active customer  
**Precondition:** Active user exists in QA environment.  
**Test data:** QA-provided account; password stored in environment secret, not in source code.

Steps:
1. Open application login page.
2. Enter registered email.
3. Enter correct password.
4. Click Sign in.
5. Wait for authenticated landing page.
6. Verify account-specific navigation is visible.

Expected:
- User is authenticated.
- Login page is no longer the current page.
- Account-specific navigation is visible.
- No error message is displayed.

## 2.6 RTM (Requirement Traceability Matrix)

| Requirement | Test scenarios |
|---|---|
| AC1 | AUTH-01 |
| AC2 | AUTH-02 |
| AC3 | AUTH-03 |
| AC4 | AUTH-04, AUTH-05, AUTH-06 |
| AC5 | AUTH-07 |
| AC6 | AUTH-01 |
| AC7 | AUTH-08 |
| AC8 | AUTH-09 |

**Exercise 1:** Product listing requirement ke liye 8 scenarios banao: listing, search, category, sorting, empty result, product detail, unavailable product, price display. Pehle khud likho, phir guide ke solution se compare karo.

---

# 3. Test Strategy — hum kya automate karenge aur kyun?

## 3.1 Scope

**In scope:**
- Authentication UI and API behavior
- Product listing/search/sort
- Cart operations
- Checkout happy path and validations
- Order history
- API status, schema/basic contract, negative cases
- Browser compatibility smoke (Chromium first)
- CI execution and failure artifacts

**Out of scope for this training release:**
- Real payment processing
- Penetration testing
- Load testing at production scale
- Real customer data
- Actual financial transactions

## 3.2 Test pyramid

- API tests: broad business/API checks; fast and stable.
- UI tests: critical end-to-end customer journeys only.
- Manual exploratory testing: new/unclear workflows and usability.

Rule: UI test ko API test se replace mat karo jab user journey itself important ho. Aur simple validation ko unnecessarily full browser journey mat banao.

## 3.3 Risk-based priorities

Highest risk:
1. Login/authentication
2. Cart total and price calculations
3. Checkout/order creation
4. Order visibility and ownership
5. Product availability

Lower risk:
- Static labels
- Decorative layout
- Non-critical text formatting

## 3.4 Definition of Done for an automated test

A test is done only when:
- It maps to a requirement/scenario.
- It has clear arrange/act/assert structure.
- It uses reliable locators.
- It does not depend on another test's execution.
- It cleans up data it creates, where applicable.
- It produces useful failure evidence.
- It passes repeatedly in a clean run.
- It has been reviewed and committed.

---

# 4. API testing — first executable tests

## 4.1 API testing ka purpose

UI ke peeche API data provide karti hai. API tests se backend contract aur business response quickly validate hota hai. Is training project mein public practice API use ki ja rahi hai; public demo environments reset/change ho sakte hain. Agar service unavailable ho, failure ko application defect assume mat karna — environment/service health verify karo.

Base URL: `https://api.practicesoftwaretesting.com`

Before automation:
1. API documentation/current environment verify karo.
2. Browser/Postman/curl se endpoint manually call karo.
3. Status code, headers, JSON shape, data types inspect karo.
4. Expected behavior document karo.
5. Phir automated assertion likho.

## 4.2 First API smoke test

`tests/api/test_products_api.py`:

```python
import requests

BASE_URL = "https://api.practicesoftwaretesting.com"

def test_products_endpoint_returns_success():
    response = requests.get(
        f"{BASE_URL}/products",
        timeout=15,
    )

    assert response.status_code == 200
    assert "application/json" in response.headers.get("Content-Type", "")
```

Run:

```bash
pytest tests/api/test_products_api.py -v
```

Line-by-line:
- `requests.get`: HTTP GET request.
- `timeout=15`: request forever hang nahi karegi.
- `status_code`: HTTP-level result.
- `Content-Type`: response format contract.

Do not assert a hardcoded product count on a changing public demo dataset.

## 4.3 Inspect response before writing detailed assertions

Temporary diagnostic test:

```python
def test_inspect_products_response():
    response = requests.get(f"{BASE_URL}/products", timeout=15)
    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Body preview:", response.text[:500])

    assert response.ok
```

`pytest -s -v` se print output dekho. Inspection complete hone ke baad noisy diagnostic test remove ya convert karo.

## 4.4 Validate JSON structure safely

```python
def test_products_response_has_expected_structure():
    response = requests.get(f"{BASE_URL}/products", timeout=15)
    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, dict)
    assert "data" in payload
    assert isinstance(payload["data"], list)

    if payload["data"]:
        first_product = payload["data"][0]
        assert isinstance(first_product, dict)
        assert "id" in first_product
        assert "name" in first_product
```

Note: Exact field names API version/documentation se verify karo. Agar current contract different ho, test ko documented contract ke hisaab se adjust karo; blind copy mat karo.

## 4.5 API negative tests

Negative test ka goal server ko todna nahi; invalid input par documented safe response verify karna hai.

```python
def test_unknown_endpoint_returns_not_found():
    response = requests.get(
        f"{BASE_URL}/endpoint-that-does-not-exist",
        timeout=15,
    )
    assert response.status_code == 404
```

**Important:** Public service may route unknown paths differently. Expected status API contract se confirm karo.

## 4.6 Reusable API client

`src/api/clients.py`:

```python
import requests

class ApiClient:
    def __init__(self, base_url: str, timeout: int = 15):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def get(self, path: str, **kwargs):
        return self.session.get(
            f"{self.base_url}/{path.lstrip('/')}",
            timeout=self.timeout,
            **kwargs,
        )

    def post(self, path: str, **kwargs):
        return self.session.post(
            f"{self.base_url}/{path.lstrip('/')}",
            timeout=self.timeout,
            **kwargs,
        )
```

Why session? Connection reuse and common session configuration. Auth headers can later be attached to the session. Do not log passwords/tokens.

## 4.7 API debugging checklist

When API test fails:
1. Kya DNS/network reachable hai?
2. Correct base URL/environment?
3. Request method and path?
4. Query params/body correct?
5. Auth token/header present and valid?
6. Status code?
7. Content-Type?
8. Response body/error details?
9. Timeout or server error?
10. Is this product bug, test bug, data issue, or environment issue?

---

# 5. Pytest framework foundation

## 5.1 Fixtures

`conftest.py`:

```python
import pytest
import requests

API_BASE_URL = "https://api.practicesoftwaretesting.com"

@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    yield session
    session.close()

@pytest.fixture
def api_base_url():
    return API_BASE_URL
```

Test:

```python
def test_products_api(api_session, api_base_url):
    response = api_session.get(
        f"{api_base_url}/products",
        timeout=15,
    )
    assert response.status_code == 200
```

Explain:
- `scope="session"`: one session for the entire pytest run.
- `yield`: test(s) ko resource dena; yield ke baad cleanup.
- Function fixture `api_base_url`: simple value per test.
- Shared session ko mutate karte waqt state leakage avoid karo.

## 5.2 Parametrization

```python
import pytest

@pytest.mark.parametrize(
    "path, expected_status",
    [
        ("/products", 200),
        ("/unknown-training-path", 404),
    ],
)
def test_endpoint_status(api_session, api_base_url, path, expected_status):
    response = api_session.get(f"{api_base_url}{path}", timeout=15)
    assert response.status_code == expected_status
```

Use parametrization when same test logic applies to multiple independent data rows. Do not combine unrelated workflows into one giant parameterized test.

## 5.3 Markers

```python
import pytest

@pytest.mark.smoke
@pytest.mark.api
def test_products_api_smoke(api_session, api_base_url):
    response = api_session.get(f"{api_base_url}/products", timeout=15)
    assert response.status_code == 200
```

Run:
```bash
pytest -m smoke -v
pytest -m "api and not negative" -v
```

## 5.4 Debugging failed tests

Commands:
```bash
pytest -v
pytest -s -v
pytest -x -v
pytest --lf -v
pytest --ff -v
pytest -k "products" -v
pytest --tb=short
pytest --tb=long
pytest --pdb
```

Meaning:
- `-v`: test names and outcomes.
- `-s`: show print output.
- `-x`: stop after first failure.
- `--lf`: last failed tests.
- `--ff`: failed tests first.
- `-k`: select by test name expression.
- `--tb`: traceback detail.
- `--pdb`: enter debugger on failure.

---

# 6. UI automation with Playwright

## 6.1 Install and verify

```bash
pip install pytest-playwright
playwright install
```

Use the Playwright Python sync API for this project. Avoid mixing sync and async APIs in the same test suite.

## 6.2 Browser fixture

Extend `conftest.py`:

```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(10_000)
        yield page
        context.close()
        browser.close()
```

This explicit fixture teaches browser lifecycle. Later, compare it with the official `pytest-playwright` fixtures (`page`, `browser`, `context`) and standardize on one approach. Do not define a custom fixture named `page` if the plugin's fixture is also being used without understanding fixture overriding.

## 6.3 First UI smoke test

`tests/ui/test_home.py`:

```python
from config.settings import BASE_URL

def test_home_page_opens(page):
    response = page.goto(BASE_URL)
    assert response is not None
    assert response.status < 400
    assert page.title()
```

Run:
```bash
pytest tests/ui/test_home.py -v
```

## 6.4 Locator strategy

Priority:
1. `get_by_role()`
2. `get_by_label()`
3. `get_by_placeholder()`
4. `get_by_text()` for meaningful visible text
5. CSS locator when semantic locator unavailable
6. XPath only when necessary

Examples (actual accessible names must be inspected in the target app):

```python
page.get_by_role("link", name="Home")
page.get_by_role("button", name="Sign in")
page.get_by_label("Email")
page.get_by_placeholder("Search")
```

Do not guess names. Inspect the live page with Playwright Inspector or DevTools and verify the accessible role/name.

## 6.5 Login page object — pattern

`src/pages/login_page.py`:

```python
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email = page.get_by_label("Email")
        self.password = page.get_by_label("Password")
        self.submit_button = page.get_by_role("button", name="Login")

    def open(self, base_url: str):
        self.page.goto(f"{base_url}/auth/login")

    def login(self, email: str, password: str):
        self.email.fill(email)
        self.password.fill(password)
        self.submit_button.click()

    def expect_login_form_visible(self):
        expect(self.email).to_be_visible()
        expect(self.password).to_be_visible()
```

This is a teaching pattern. Confirm the target app's actual route, accessible labels, and button name before using it. If the app uses a different route/name, update the page object based on evidence.

## 6.6 UI test structure

```python
from config.settings import BASE_URL
from src.pages.login_page import LoginPage

def test_login_form_is_available(page):
    login_page = LoginPage(page)
    login_page.open(BASE_URL)
    login_page.expect_login_form_visible()
```

Do not put every assertion inside the Page Object. Page Object should model page behavior; test should express business expectation.

## 6.7 Playwright debugging methods

```python
page.pause()
```
Pause execution and inspect the page in Inspector.

```python
locator = page.get_by_role("button", name="Login")
print("Matches:", locator.count())
locator.highlight()
```

- `count()` checks how many elements match.
- `highlight()` visually highlights a locator during debugging.
- `is_visible()` / `is_enabled()` are useful diagnostic checks, not substitutes for web-first assertions in normal tests.
- Prefer `expect(locator).to_be_visible()` for auto-retrying assertions.

## 6.8 Common Playwright failure investigation

**Timeout waiting for locator**
1. Confirm correct URL/page.
2. Inspect accessible role/name.
3. Check whether element exists (`count()`).
4. Check visibility/overlay/disabled state.
5. Inspect console and network.
6. Check if app is still loading or backend request failed.
7. Fix locator or product issue based on evidence.

**Strict mode violation**
- Locator matched more than one element.
- Narrow it with a parent/container, `filter(has_text=...)`, or a more specific accessible name.
- Do not blindly add `.first` / `.nth()` to silence the error.

**Element not actionable**
- It may be hidden, disabled, moving, covered, or detached.
- Investigate the actual cause; do not default to `force=True`.

---

# 7. Cart and checkout test design

The public training application may change its checkout workflow. First explore it manually and document the current behavior. Do not invent a successful checkout if the environment does not support it.

## 7.1 Business scenarios

| ID | Scenario | Priority |
|---|---|---|
| CART-01 | Add one available product to cart | P0 |
| CART-02 | Cart displays selected product | P0 |
| CART-03 | Quantity update recalculates subtotal | P1 |
| CART-04 | Remove product empties cart | P1 |
| CART-05 | Cart total equals sum of line totals | P0 |
| CHECKOUT-01 | Required fields validation | P0 |
| CHECKOUT-02 | Valid checkout creates order | P0 |
| CHECKOUT-03 | Order appears in order history | P0 |
| CHECKOUT-04 | User cannot view another user's order | P0 |

## 7.2 Cart total calculation test logic

If cart contains line items with `unit_price` and `quantity`:

```python
def calculate_expected_total(items):
    return sum(
        item["unit_price"] * item["quantity"]
        for item in items
    )
```

Use Decimal for currency in Python when values are under your control:

```python
from decimal import Decimal

def calculate_total(items):
    total = Decimal("0.00")
    for item in items:
        total += Decimal(str(item["unit_price"])) * item["quantity"]
    return total
```

Why not float? Binary floating-point can produce precision artifacts. Compare currency using documented rounding rules.

## 7.3 Data setup and cleanup

Prefer API setup for data-heavy UI tests when the application exposes supported APIs. Then use UI to validate the user journey. Cleanup must be safe and scoped to test-created data only.

Never delete shared environment data or use real customer records.

---

# 8. Failure evidence, logs, and reports

## 8.1 Basic logging

`src/utils/logger.py`:

```python
import logging
from pathlib import Path

Path("logs").mkdir(exist_ok=True)

def get_logger(name: str):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler("logs/automation.log", encoding="utf-8")
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )
        )
        logger.addHandler(handler)
    return logger
```

Use:
```python
from src.utils.logger import get_logger

logger = get_logger(__name__)

def test_example():
    logger.info("Starting example test")
    assert 2 + 2 == 4
```

Do not log passwords, access tokens, session cookies, or personal data.

## 8.2 Screenshot on failure (pytest hook)

Add to `conftest.py` only when using the custom `page` fixture above:

```python
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            path = f"reports/{item.name}.png"
            page.screenshot(path=path, full_page=True)
            print(f"Screenshot saved: {path}")
```

Create reports folder:
```bash
mkdir reports
```

For production use, improve filenames with unique IDs and sanitize test names. Handle screenshot errors so artifact capture does not hide the original test failure.

## 8.3 HTML report

```bash
pytest --html=reports/report.html --self-contained-html
```

Report must answer:
- What ran?
- What passed/failed/skipped?
- Which requirement is covered?
- What failed and where?
- What evidence is attached?
- Is failure product, automation, data, or environment?

---

# 9. Defect reporting — industry-style

## Example bug report

**Bug ID:** RH-DEF-014  
**Title:** Cart subtotal is not recalculated after quantity update  
**Environment:** QA / Chromium / build 1.8.2  
**Severity:** Major (proposed; confirm business impact)  
**Priority:** P1 (proposed)

**Precondition:** One product is available and added to cart.

**Steps to reproduce:**
1. Open product listing.
2. Add a product priced at 20.00.
3. Open cart.
4. Change quantity from 1 to 2.
5. Observe line subtotal and cart total.

**Expected:** Subtotal becomes 40.00 (subject to documented tax/discount rules).  
**Actual:** Subtotal remains 20.00.  
**Evidence:** Screenshot, trace, timestamp, test data ID, network response.  
**Reproducibility:** 5/5 attempts.  
**Impact:** Customer may pay an incorrect amount or see inconsistent pricing.

Do not call every failure a bug. Triage:
- Product defect
- Automation defect
- Test data defect
- Environment/infrastructure issue
- Requirement ambiguity

---

# 10. Git workflow and pull request

Suggested branch:
```bash
git checkout -b feature/retailhub-login-tests
```

Commit:
```bash
git add .
git commit -m "Add login UI smoke coverage"
```

Before PR:
```bash
pytest -m smoke -v
git status
git diff --check
```

PR description template:

```text
## What changed?
Added login smoke automation.

## Requirement coverage
RH-AUTH-001 / AUTH-01

## Validation
- [ ] Tests pass locally
- [ ] No secrets committed
- [ ] Failure artifacts reviewed
- [ ] No unrelated changes

## Risks / notes
Document environment dependency or known limitations.
```

---

# 11. GitHub Actions CI

`.github/workflows/tests.yml`:

```yaml
name: RetailHub Automation

on:
  push:
    branches: [main]
  pull_request:
  workflow_dispatch:

jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          playwright install --with-deps chromium

      - name: Run smoke tests
        env:
          BASE_URL: ${{ vars.BASE_URL }}
          API_BASE_URL: ${{ vars.API_BASE_URL }}
        run: |
          pytest -m smoke -v --junitxml=reports/junit.xml

      - name: Upload test report
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: junit-report
          path: reports/
```

**CI debugging sequence:**
1. Read first failing step, not just final red status.
2. Check Python version and dependency install.
3. Check browser install.
4. Check environment variables/secrets.
5. Check whether public demo environment is reachable.
6. Download artifacts.
7. Reproduce locally with same Python/dependency versions.
8. Classify failure before changing code.

Never put secrets in workflow YAML. Store sensitive values in GitHub Secrets; non-sensitive URLs can be repository variables.

---

# 12. Release QA summary

Use this format at the end of a run:

```text
Product: RetailHub
Build:
Environment:
Execution date:

Total:
Passed:
Failed:
Skipped:

P0 requirements covered:
Open critical defects:
Known environment issues:

Release recommendation:
- GO
- GO WITH RISKS
- NO-GO

Reason:
Evidence:
Owner / next action:
```

Release recommendation must be based on risk and evidence, not only pass percentage.

---

# 13. Final project acceptance checklist

## Requirements and test design
- [ ] I can explain the feature in my own words.
- [ ] I can identify actors, preconditions, actions, expected outcomes.
- [ ] I raised requirement questions instead of guessing.
- [ ] Every critical acceptance criterion maps to tests.

## Automation
- [ ] API smoke tests execute.
- [ ] UI smoke tests execute.
- [ ] Fixtures manage setup/cleanup.
- [ ] Tests are independent.
- [ ] Locators are stable and semantic.
- [ ] Assertions verify business outcomes.
- [ ] Test data is controlled.

## Debugging and reporting
- [ ] I can reproduce failures.
- [ ] I can inspect traceback, browser, console, and network.
- [ ] I can distinguish product/test/data/environment failures.
- [ ] I attach useful evidence.
- [ ] I add regression coverage after a fix.

## Engineering workflow
- [ ] Project is committed to Git.
- [ ] README explains setup and execution.
- [ ] CI runs smoke tests.
- [ ] Reports/artifacts are retained.
- [ ] No credentials or personal data are committed.

## Interview readiness
You should be able to explain:
1. Why API and UI tests are split.
2. Why fixtures are used.
3. How you prevent test dependency.
4. How you select stable locators.
5. How you debug a Playwright timeout.
6. How you investigate a flaky test.
7. How you decide whether a failure is product or automation.
8. How CI artifacts help debugging.
9. How requirements map to tests.
10. What risks remain at release time.

---

# 14. Suggested execution plan

| Stage | Work | Evidence of completion |
|---|---|---|
| 1 | Understand product and requirements | Clarification log |
| 2 | Test scenarios and RTM | Test design document |
| 3 | Environment and repo | Clean setup on your machine |
| 4 | API smoke and contract tests | Passing API suite |
| 5 | Pytest fixtures/markers | Reusable test structure |
| 6 | UI smoke and page objects | Passing UI suite |
| 7 | Cart/checkout scenarios | Critical journey coverage |
| 8 | Debugging and artifacts | Reproducible failure evidence |
| 9 | Reporting and bug lifecycle | HTML report + bug report |
| 10 | Git and CI | Green CI run + artifact |
| 11 | Final review | QA summary and demo |

**Do not mark a stage complete just because code exists. Run it, inspect its result, understand it, and explain it without reading the file.**

---

# 15. What to do when the public practice environment differs

This project uses a public training application as the practice AUT. Public demo sites can change routes, accessible names, data, or availability. Therefore:
- Treat current UI and API documentation as the source of truth.
- Explore the live application before writing selectors.
- Keep environment-specific routes and selectors in one place.
- Do not weaken assertions simply to make a test green.
- Record environment drift as a test-environment issue.
- If the public service is unavailable, pause execution and report the blocker rather than claiming the suite passed.

**Project 01 completion means you can independently take a requirement, design coverage, implement and debug a maintainable UI/API automation suite, run it in CI, and communicate release risk.**
