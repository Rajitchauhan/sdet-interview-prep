# 🎯 Playwright Python --- Production Framework Architecture & Design

### The Final Playwright Learning Module \| Hinglish Mentor Notes

> **Mission:** Sirf tests likhna nahi --- ek aisa automation framework
> design karna jo readable, maintainable, reusable, debuggable aur team
> ke saath scale kar sake.
>
> **Learning style:** WHY → WHAT → HOW → code → line-by-line →
> real-world scenario → common mistakes → interview answers → exercise.

![Playwright](https://img.shields.io/badge/Playwright-Python-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Test%20Runner-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Architecture](https://img.shields.io/badge/Focus-Framework%20Architecture-7C3AED?style=for-the-badge)

------------------------------------------------------------------------

## 📍 0. Where are we in the roadmap?

Playwright ke major-topic roadmap mein hum 19/21 areas cover kar chuke
hain. CI/CD (topic 20) abhi in-progress hai aur is guide ka focus topic
21 --- **Production Framework** --- hai.

**Important distinction:** topic coverage ka matlab mastery ya
job-readiness guarantee nahi. Is module ka goal hai previously learned
concepts ko ek coherent framework mein integrate karna.

### Is module ke end tak tum kya kar paoge?

-   Framework ki folder structure ko reason ke saath design karna.
-   Test, Page Object, Fixture, API Client, Utility aur Config ki
    responsibilities separate rakhna.
-   Test setup/teardown aur test data lifecycle manage karna.
-   UI + API workflows ko cleanly combine karna.
-   Environment configuration, secrets aur parallel execution ko dhyan
    mein rakhna.
-   Failure evidence, logs aur reports collect karna.
-   Framework ko maintainable banane ke liye trade-offs explain karna.

------------------------------------------------------------------------

# 1. WHY --- Framework ki zaroorat kyun hoti hai?

Imagine karo ek e-commerce application hai. Tumhare paas 150 automated
tests hain.

Agar har test mein: - browser setup repeat hota hai, - login steps
repeat hote hain, - selectors hardcode hote hain, - API requests har
jagah copy-paste hoti hain, - test data manually create hota hai, -
cleanup bhool jaate ho,

to framework maintain karna mushkil ho jayega.

### Without framework vs with framework

  Without a thoughtful framework   With a thoughtful framework
  -------------------------------- ----------------------------------
  Repeated setup code              Shared fixtures
  UI selectors har test mein       Page Objects / component objects
  API calls scattered              API Client layer
  Hardcoded URLs                   Central configuration
  Test data mixed with logic       Dedicated test data/factories
  Random debugging                 Logs + screenshots + trace
  Hidden dependencies              Clear dependency flow

> **Framework ka matlab folders ki quantity nahi. Framework = clear
> responsibilities + predictable lifecycle + reusable components +
> reliable execution.**

## Framework ke design goals

1.  **Maintainability:** change ek jagah ho to unnecessary files edit na
    karni padein.
2.  **Readability:** naya team member test padh kar intent samajh sake.
3.  **Reliability:** tests independent hon, random failures kam hon.
4.  **Reusability:** repeated infrastructure logic reuse ho, business
    behavior hide na ho.
5.  **Debuggability:** failure ka reason aur evidence mil sake.
6.  **Scalability:** tests aur team badhne par structure manageable
    rahe.
7.  **Security:** credentials, tokens aur customer data leak na hon.

------------------------------------------------------------------------

# 2. WHAT --- Framework ke main building blocks

Sabse pehle responsibilities samjho. Ye module ka most important concept
hai.

``` mermaid
flowchart TD
    A["🧪 TESTS<br/>WHAT should be verified?"] --> B["🧩 FIXTURES<br/>Setup, dependencies, lifecycle"]
    A --> C["📄 PAGE OBJECTS<br/>How to interact with UI"]
    A --> D["🔌 API CLIENTS<br/>How to call backend APIs"]
    C --> E["🎭 PLAYWRIGHT<br/>Browser, Context, Page"]
    D --> F["🌐 API"]
    B --> E
    B --> D
    C --> G["🧰 COMPONENT OBJECTS<br/>Reusable UI components"]
    A --> H["📊 ASSERTIONS<br/>Expected business outcome"]
    I["⚙️ CONFIG"] --> B
    I --> C
    I --> D
    J["🗃️ TEST DATA"] --> A
    J --> D
    K["🪵 LOGGING / REPORTING"] --> A
```

## 2.1 Test layer --- WHAT to verify?

Test file business scenario aur expected result describe karta hai.

``` python
def test_customer_can_add_product_to_cart(
    page,
    inventory_page,
    cart_page,
):
    inventory_page.open()
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()

    assert cart_page.has_product("Sauce Labs Backpack")
```

**Responsibility:** - scenario define karna; - action sequence
coordinate karna; - expected outcome assert karna.

**Test mein kya avoid karna hai?** - long CSS/XPath selectors; -
repeated login/setup implementation; - raw HTTP request details; -
unrelated low-level browser configuration.

> Rule of thumb: test ko business story ki tarah padhna chahiye.

## 2.2 Page Object Model --- HOW to interact with a page?

POM ek design pattern hai. Page Object page ke locators aur
page-specific actions encapsulate karta hai.

``` python
from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_label("Username")
        self.password = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def open(self):
        self.page.goto("/login")

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def expect_login_error(self, message: str):
        expect(self.page.get_by_role("alert")).to_contain_text(message)
```

### Line-by-line thinking

-   `Page` type hint: batata hai ki constructor Playwright `Page` expect
    karta hai.
-   `self.page`: current browser tab ka reference.
-   `get_by_label()` / `get_by_role()`: semantic, user-facing locators.
-   `open()`: page navigation behavior.
-   `login()`: login page ka interaction.
-   `expect_login_error()`: page-specific UI expectation encapsulate
    karta hai.

### Assertions POM mein ya test mein?

Practical rule: - **Business outcome assertion** test mein rakho. -
**Reusable page-specific state/expectation** POM method mein rakh sakte
ho. - Dono approaches valid ho sakti hain; consistency aur readability
decide karegi.

Example: "Order successfully placed" business assertion test mein.
"Login error banner visible" reusable page-specific assertion POM mein
ho sakta hai.

### POM mistakes

-   ❌ One giant `BasePage` with every method.
-   ❌ POM mein API setup, database cleanup aur business test
    orchestration.
-   ❌ Har tiny locator ke liye unnecessary abstraction.
-   ❌ Test ka expected business result page class ke andar chhupa dena.
-   ❌ Unstable `nth()` selectors ko default banana.

## 2.3 Component Objects --- reusable UI parts

Navbar, sidebar, product card, date picker jaise components multiple
pages par reuse ho sakte hain.

``` python
class ProductCard:
    def __init__(self, card_locator):
        self.card = card_locator

    def add_to_cart(self):
        self.card.get_by_role(
            "button", name="Add to cart"
        ).click()
```

Page Object component ko compose kar sakta hai:

``` python
class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    def product(self, product_name: str) -> ProductCard:
        card = self.page.locator(".product-card").filter(
            has_text=product_name
        )
        return ProductCard(card)
```

Usage:

``` python
inventory_page.product("Sauce Labs Backpack").add_to_cart()
```

**Kab use karein?** Jab component ka behavior meaningful ho aur multiple
places par reuse ho. Har `div` ko class mat banao.

## 2.4 Fixtures --- setup, dependency aur lifecycle

Fixture test ko required object/resource provide karta hai. Fixture
inheritance nahi hai; ye dependency injection ka simple pattern hai.

``` python
import pytest
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    return LoginPage(page)
```

Test:

``` python
def test_login_page_opens(login_page):
    login_page.open()
```

Pytest fixture dependency chain:

``` mermaid
flowchart TD
    A["Test requests login_page"] --> B["Pytest runs login_page fixture"]
    B --> C["Fixture requests page"]
    C --> D["Playwright plugin creates Page"]
    D --> E["LoginPage(page) returned"]
    E --> F["Test executes"]
    F --> G["Fixture teardown, if defined"]
```

### `yield` --- setup and teardown

``` python
@pytest.fixture
def logged_in_page(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret")

    yield page

    # Teardown: runs after the test using this fixture
    # Add cleanup only if this fixture owns the resource.
```

-   `yield` se pehle: setup.
-   `yield` ke baad: teardown.
-   Fixture teardown test completion par run hota hai, including normal
    test failure.
-   Teardown ko safe, focused aur idempotent rakhna chahiye.

### Fixture scope

  Scope        Lifetime
  ------------ -----------------------
  `function`   Har test function
  `class`      Test class
  `module`     Python module
  `package`    Package
  `session`    Entire pytest session

**Caution:** shared mutable state aur shared browser/page resources
parallel tests mein race conditions create kar sakte hain. Scope sirf
performance ke liye badhana safe nahi.

### Fixture design rules

-   Fixture ka purpose clear ho.
-   Fixture wohi resource own kare jiska cleanup uski responsibility
    hai.
-   Fixture dependency explicit rakho.
-   `autouse=True` sirf truly universal setup ke liye.
-   Test ke business steps ko hidden autouse fixture mein mat chhupao.
-   Fixture names readable rakho: `authenticated_page`, `api_client`,
    `created_order`.

## 2.5 API Client --- API operations ko isolate karna

`requests` tum jaante ho. Use framework mein ek client class ke through
organize kar sakte ho.

``` python
import requests


class OrdersAPI:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}"
        })

    def create_order(self, payload: dict):
        response = self.session.post(
            f"{self.base_url}/orders",
            json=payload,
            timeout=15,
        )
        response.raise_for_status()
        return response.json()

    def get_order(self, order_id: str):
        response = self.session.get(
            f"{self.base_url}/orders/{order_id}",
            timeout=15,
        )
        response.raise_for_status()
        return response.json()
```

**Why?** - base URL/header logic centralize; - repeated request code
reduce; - API methods reusable; - tests business intent par focus kar
sakein.

**Important:** API client ko test assertions ka dumping ground mat
banao. HTTP operations aur response parsing client ki responsibility;
business expectation test ki responsibility.

### `requests` vs Playwright APIRequestContext

-   `requests`: Python HTTP library; tumhare existing API tests aur API
    client ke liye bilkul valid.
-   `playwright.request` / `APIRequestContext`: Playwright ka API
    testing capability; Playwright context ke saath cookie sharing aur
    browser-related workflows mein useful ho sakta hai.
-   Dono mein se ek ko universally best mat samjho. Project needs,
    authentication model aur team conventions ke basis par choose karo.

## 2.6 Utilities --- generic helpers

Utility ka kaam generic reusable support logic hai, business workflow
own karna nahi.

Examples: - random email generate karna; - date formatting; - file
reading; - safe JSON loading.

``` python
from uuid import uuid4


def unique_email():
    return f"qa-{uuid4().hex[:10]}@example.test"
```

**Bad utility smell:** `utils.py` mein 50 unrelated methods. Related
helpers ko meaningful modules mein divide karo.

## 2.7 Configuration --- environment-specific values

Dev, staging, production mein URLs aur settings change ho sakti hain.

``` python
import os


BASE_URL = os.getenv(
    "BASE_URL",
    "https://staging.example.com"
)

ENVIRONMENT = os.getenv("ENVIRONMENT", "staging")
```

Set environment variable:

``` bash
# Windows PowerShell
$env:BASE_URL="https://staging.example.com"

# macOS/Linux
export BASE_URL="https://staging.example.com"
```

**Secrets:** password, API token, private key source code mein hardcode
mat karo. GitHub Actions secrets ya approved secret manager use karo.
`.gitignore` secret ko magically secure nahi karta; woh sirf selected
files ko Git tracking se exclude karta hai.

## 2.8 Test Data --- test logic se separate

Test data ke common forms:

1.  Static test data: fixed known values.
2.  Parametrized data: multiple scenarios.
3.  Generated data: unique email/order identifier.
4.  API-created data: test se pehle backend resource create.
5.  Environment/config data: URL, credentials, feature flags.

``` python
import pytest


@pytest.mark.parametrize(
    "username, password, expected_message",
    [
        ("locked_user", "secret", "locked out"),
        ("invalid_user", "wrong", "invalid"),
    ],
    ids=["locked-account", "invalid-credentials"],
)
def test_invalid_login(
    login_page, username, password, expected_message
):
    login_page.open()
    login_page.login(username, password)
    login_page.expect_login_error(expected_message)
```

**Golden rule:** test data ko selectors ya POM methods ke andar hardcode
mat karo. Data aur interaction responsibilities alag rakho.

------------------------------------------------------------------------

# 3. HOW --- End-to-end architecture flow

Ab dekho ek test ka execution kaise flow karta hai:

``` mermaid
sequenceDiagram
    autonumber
    participant T as Test
    participant F as Pytest Fixture
    participant C as Config
    participant API as API Client
    participant P as Page Object
    participant B as Browser/Page

    T->>F: Request authenticated_page
    F->>C: Read environment settings
    F->>B: Get isolated Page
    F->>P: Create Page Object
    T->>API: Create test data (if needed)
    API-->>T: Return resource ID
    T->>P: Perform UI action
    P->>B: Locator action
    B-->>P: Browser result
    T->>T: Assert business outcome
    T->>API: Cleanup test data (if appropriate)
```

### Real-world example: Order flow

1.  API se unique order/product data create karo (agar API setup
    supported ho).
2.  UI browser page open karo.
3.  User login kare.
4.  Product cart mein add karo.
5.  Checkout complete karo.
6.  UI par confirmation assert karo.
7.  API se order status verify karna optional hai, agar requirement ke
    liye meaningful ho.
8.  Test-created data cleanup karo, agar cleanup supported ho.

**Important:** UI test ka purpose UI workflow verify karna hai. Har step
ko API se replace kar doge to UI coverage hi nahi bachegi.

------------------------------------------------------------------------

# 4. Suggested project structure

Ye ek sensible starting structure hai --- universal mandatory structure
nahi. Project size ke hisaab se simplify ya expand kar sakte ho.

``` text
playwright-framework/
│
├── tests/
│   ├── ui/
│   │   ├── test_login.py
│   │   └── test_checkout.py
│   ├── api/
│   │   └── test_orders_api.py
│   └── conftest.py
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
│
├── components/
│   └── product_card.py
│
├── api_clients/
│   └── orders_api.py
│
├── test_data/
│   └── users.py
│
├── config/
│   └── settings.py
│
├── utils/
│   └── data_generator.py
│
├── reports/
│
├── .github/
│   └── workflows/
│       └── playwright.yml
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Folder responsibilities

  Folder/file            Responsibility
  ---------------------- -------------------------------------------------
  `tests/`               Test scenarios and assertions
  `pages/`               Page-specific locators and actions
  `components/`          Reusable UI component behavior
  `api_clients/`         HTTP/API operations
  `test_data/`           Static or scenario-specific data
  `config/`              Environment and runtime settings
  `utils/`               Generic helper functions
  `conftest.py`          Shared pytest fixtures/hooks
  `pytest.ini`           Pytest configuration and markers
  `.github/workflows/`   CI workflow definitions
  `reports/`             Generated report output; usually ignored by Git

### `conftest.py` hierarchy

``` text
project/
├── conftest.py             # shared project fixtures
└── tests/
    ├── conftest.py         # fixtures for tests subtree
    ├── ui/
    │   └── test_login.py
    └── api/
        └── test_orders.py
```

Pytest nearer `conftest.py` files ko relevant test subtree mein discover
karta hai. Fixtures ko duplicate karne ke bajaye correct scope/location
choose karo.

------------------------------------------------------------------------

# 5. Example: A small connected framework slice

Ab ek mini example se responsibilities connect karte hain.

## `pages/login_page.py`

``` python
from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_label("Username")
        self.password = page.get_by_label("Password")
        self.submit_button = page.get_by_role(
            "button", name="Login"
        )

    def open(self, base_url: str):
        self.page.goto(f"{base_url}/login")

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.submit_button.click()
```

## `config/settings.py`

``` python
import os


class Settings:
    BASE_URL = os.getenv(
        "BASE_URL",
        "https://staging.example.com"
    )
```

## `conftest.py`

``` python
import pytest

from config.settings import Settings
from pages.login_page import LoginPage


@pytest.fixture
def app_settings():
    return Settings


@pytest.fixture
def login_page(page):
    return LoginPage(page)
```

## `tests/ui/test_login.py`

``` python
from playwright.sync_api import expect


def test_login_page_is_open(login_page, app_settings):
    login_page.open(app_settings.BASE_URL)

    expect(
        login_page.page.get_by_role("heading", name="Login")
    ).to_be_visible()
```

### Is example mein responsibility kaise divide hui?

-   `test_login.py`: scenario + assertion.
-   `login_page.py`: page locators + UI interaction.
-   `conftest.py`: object creation / dependency.
-   `settings.py`: environment configuration.
-   Playwright `page` fixture: browser page lifecycle plugin manage
    karta hai.

> Note: ye teaching slice hai, complete production framework nahi.
> Actual application ke locator labels, URL, auth aur test data
> requirements ke hisaab se change honge.

------------------------------------------------------------------------

# 6. Reliability --- production framework ke non-negotiables

## 6.1 Test independence

Ek test dusre test ke execution order par depend nahi hona chahiye.

Bad: - Test A user create kare. - Test B assume kare Test A pehle run
hua. - Test B standalone run ho to fail.

Better: - Test B apna required data fixture/API se create kare. - Test
complete hone par owned data cleanup kare.

## 6.2 Isolation

-   Har test ko appropriate isolated browser context/page do.
-   Shared mutable state avoid karo.
-   Unique test data generate karo.
-   Parallel execution mein same user/cart/order reuse karne se bachho.

## 6.3 Waits and assertions

-   Playwright locator actions aur web-first assertions ka auto-wait use
    karo.
-   `time.sleep()` default solution nahi.
-   Arbitrary large timeouts se slow/flaky test mask ho sakta hai.
-   `force=True` ko routine fix mat banao.
-   Assertion actual requirement ko verify kare.

## 6.4 Retries

Retry temporary infrastructure issues ke evidence gather karne mein help
kar sakta hai, lekin root cause fix nahi karta. Side-effecting workflows
mein retry duplicate orders/payments create kar sakta hai. Retry policy
thoughtfully design karo.

## 6.5 Parallel safety

-   Worker ke hisaab se unique resources.
-   Test-level isolation.
-   Shared account/data conflicts avoid.
-   External rate limits aur environment capacity consider.
-   Parallel workers badhane se hamesha speed improve nahi hoti.

## 6.6 Logging and evidence

Useful evidence: - failed test ka screenshot; - Playwright trace; -
browser console errors (where useful); - request/response diagnostics
(sensitive data redact karke); - structured test logs; - JUnit/Allure
report.

**Security rule:** password, bearer token, cookies, private customer
data logs/reports mein expose mat karo.

## 6.7 CI readiness

Framework ko local aur CI dono mein predictable chalna chahiye: -
dependencies pinned/managed; - browser installation documented; - base
URL environment se; - secrets CI secret store se; - report output
consistent; - exit code test result reflect kare; - CI failure par
useful evidence upload ho.

CI workflow ka dedicated learning Git + GitHub + CI/CD track mein
rahega; yahan architecture mein uski integration point samajhna enough
hai.

------------------------------------------------------------------------

# 7. Common architecture mistakes --- strict mentor review

  ------------------------------------------------------------------------
  Smell                   Why it is risky         Better direction
  ----------------------- ----------------------- ------------------------
  One giant `BasePage`    Every page becomes      Small focused
                          coupled                 page/component classes

  All logic in            Hidden setup and hard   Fixtures only for
  `conftest.py`           debugging               lifecycle/dependencies

  API calls inside POM    UI and backend          API Client layer
                          responsibilities mixed  

  Assertions hidden       Test intent becomes     Business assertions in
  everywhere              unclear                 tests

  Hardcoded credentials   Security risk           Environment/secrets

  One shared account for  State collision         Isolated/unique data
  parallel tests                                  

  `time.sleep()`          Slow and flaky          Auto-wait + web-first
                                                  assertion

  Catch all exceptions    Real failures hidden    Fail clearly; handle
  and continue                                    only expected cases

  Huge generic utilities  Unclear ownership       Domain-focused helper
  module                                          modules

  Abstract every one-line More indirection than   Abstract repeated
  action                  value                   meaningful behavior

  Tests depend on         Unreliable suite        Independent setup and
  execution order                                 cleanup
  ------------------------------------------------------------------------

### Strict review labels

When you submit your exercise, review will use:

-   🟢 **GOOD** --- sound and maintainable.
-   🔴 **WRONG** --- incorrect behavior/API/design.
-   🟠 **RISK** --- works now but may be flaky or unsafe.
-   🔵 **IMPROVEMENT** --- readability/maintainability opportunity.
-   ⭐ **PRODUCTION VERSION** --- stronger implementation and why.

------------------------------------------------------------------------

# 8. Interview preparation

## Q1. What is an automation framework?

**Simple answer:**

An automation framework is a structured set of tools, reusable
components, coding standards and execution practices used to build, run
and maintain automated tests.

**Stronger answer:**

An automation framework provides a consistent architecture for test
automation. It separates test scenarios from UI interaction, setup and
teardown, API operations, test data, configuration and reporting. In a
Python Playwright framework, Pytest manages test execution and fixtures,
Page Objects encapsulate UI behavior, API clients handle backend
operations, and configuration utilities support different environments.
A good framework focuses on maintainability, reliability, reusability,
isolation and debuggability rather than simply reducing code.

**Keywords:** maintainability, separation of concerns, fixtures, POM,
isolation, reporting.

## Q2. What is the difference between POM and fixtures?

**Simple answer:**

POM organizes page locators and UI actions. Fixtures manage test
dependencies, setup and teardown.

**Stronger answer:**

Page Object Model is a design pattern that encapsulates page-specific UI
behavior, while Pytest fixtures are a test lifecycle and
dependency-injection mechanism. A fixture can create a Page Object and
provide it to a test. They solve different problems and work together;
one does not replace the other.

**Keywords:** design pattern, lifecycle, dependency injection, UI
abstraction.

## Q3. Why should API logic not be placed inside Page Objects?

**Answer:**

Page Objects should represent UI pages and their interactions. API
operations belong in a separate API client layer. Keeping them separate
reduces coupling, makes each component easier to test and allows API
setup or cleanup to be reused independently.

## Q4. How do you make Playwright tests parallel-safe?

**Answer:**

I design tests to be independent, use isolated browser contexts,
generate unique test data, avoid shared mutable state and ensure cleanup
is safe. I also consider external service limits and application
capacity before increasing worker count.

## Q5. What makes a framework production-ready?

**Answer:**

A production-ready framework has clear separation of responsibilities,
stable locators, independent tests, environment-based configuration,
secure secret handling, reusable fixtures and clients, useful logs and
failure evidence, controlled parallel execution and reliable CI
integration. It should also be easy for another engineer to understand
and extend.

------------------------------------------------------------------------

# 9. 🧠 Architecture decision checklist

Before adding a new class/file, ask:

1.  What exact responsibility does this component own?
2.  Does this responsibility already exist somewhere?
3.  Is the abstraction genuinely reusable or just extra indirection?
4.  Is the dependency explicit?
5.  Can this component be tested or debugged independently?
6.  Does it make tests easier to read?
7.  Does it introduce shared state or parallel risk?
8.  Are secrets or sensitive data exposed?
9.  Is cleanup responsibility clear?
10. Would a teammate understand where to make a change?

> **Golden principle:** Good architecture is not the architecture with
> the most folders or classes. It is the simplest design that keeps
> responsibilities clear as the project grows.

------------------------------------------------------------------------

# 10. 🏋️ Your final architecture exercise

`<badge color="success">`{=html}Independent design
challenge`</badge>`{=html} `<badge color="warning">`{=html}Do not look
for a ready-made solution`</badge>`{=html}

## Scenario: E-commerce application

Tumhe ek e-commerce web application ke liye Python + Pytest + Playwright
automation framework design karna hai.

### Application capabilities

**Customer** - Login / logout - Product listing - Search product - Sort
by price - Add/remove cart item - Checkout - View order confirmation

**Manager** - Login - Add product - Update product - Delete product -
View orders

**Backend API** - Create user - Create product - Create order - Get
order details - Delete test-created resources

### Requirements

1.  UI tests and API tests both supported.
2.  Different environments: staging and QA.
3.  Credentials must not be hardcoded.
4.  Page Objects must be used.
5.  Shared UI components should be reusable where meaningful.
6.  Fixtures should manage setup and teardown.
7.  API setup and cleanup should be possible.
8.  Tests should support parallel execution.
9.  Failure evidence and reports should be collectable.
10. A new team member should understand the project structure.

## Your tasks

### Task A --- Folder architecture

Project ki complete folder structure design karo. Har folder/file ka
purpose ek line mein likho.

### Task B --- Responsibility mapping

In responsibilities ko correct layer mein place karo:

-   Login locators
-   Login interaction
-   Create test user through API
-   Base URL configuration
-   Generate unique email
-   Browser page lifecycle
-   Verify order confirmation
-   Delete test-created order
-   Allure attachment
-   Product card behavior

### Task C --- Execution flow

Ek checkout test ka flow draw/write karo:

``` text
Test starts
   ↓
   ?
   ↓
   ?
   ↓
   ?
   ↓
Business assertion
   ↓
Cleanup
```

### Task D --- Design decisions

In questions ka reasoning do:

1.  API Client ko POM ke andar kyun nahi rakhenge?
2.  Fixture aur POM mein kya difference hai?
3.  Har test ke liye new browser context kyun useful hai?
4.  Unique test data parallel execution mein kaise help karta hai?
5.  Kya har reusable function ko utility banana chahiye?

### Task E --- Code design

Abhi full implementation mat likhna. Sirf in classes/functions ka
proposed interface likho:

-   `LoginPage`
-   `InventoryPage`
-   `OrdersAPI`
-   `authenticated_page` fixture
-   `unique_email()` utility

------------------------------------------------------------------------

## 🧪 Self-assessment rubric

Exercise submit karne par main is rubric se review karunga:

  Evaluation area                         Weight
  ------------------------------------ ---------
  Separation of responsibilities              25
  Folder structure and clarity                15
  Fixture and lifecycle design                20
  API/UI integration                          15
  Test isolation and parallel safety          15
  Maintainability and reasoning               10
  **Total**                              **100**

**Target:** 80+ = good foundation; 90+ = strong design reasoning. Score
sirf submitted work ke basis par hoga.

------------------------------------------------------------------------

# 11. Revision map --- what to revisit when confused

  If you are confused about...   Revisit
  ------------------------------ -----------------------------------
  `page` object creation         Browser / Context / Page
  Fixture dependency             Pytest fixtures and `conftest.py`
  Page class responsibilities    POM
  Repeated UI sections           Component Objects
  API setup/cleanup              API + UI integration
  Multiple test inputs           Parametrization / test data
  Environment URL                Configuration
  Random test failures           Flaky tests / debugging
  Parallel conflicts             Isolation / xdist
  CI report/evidence             Logging / reporting / CI-CD

------------------------------------------------------------------------

# 🏁 Final takeaway

Framework design ka real test ye nahi ki tum 15 folders bana sakte ho.

Real test ye hai:

-   Test padhte hi business intent samajh aaye.
-   POM padhte hi UI interaction samajh aaye.
-   Fixture padhte hi setup/lifecycle samajh aaye.
-   API Client padhte hi backend operation samajh aaye.
-   Config padhte hi environment behavior samajh aaye.
-   Failure aane par evidence se root cause investigate kar sako.

**Ab tumhara next milestone:** Exercise ke through architecture design
karna, phir us design ko actual code mein implement karna.

> 🥷 Mentor rule: Pehle tum design submit karoge. Main review aur hints
> dunga. Full solution tumhare attempt se pehle nahi dunga.
