# 🧩 Page Object Model (POM): Basic se Advanced, Step by Step

**Python + pytest + Playwright | Hinglish | Interview aur Production dono ke liye**

> Is guide me tum **khud banaoge**, ek-ek chhote step me. Har step me: pehle **dikkat**, phir **idea**, phir **code**, phir **"kyun ye, aur doosra option kyun nahi"**.

---

# 📍 Pehle ye padho (2 minute)

## Kaise padhna hai (apna raasta chuno)

| Tum kaun ho | Raasta |
|---|---|
| 🐣 **Pehli baar sikh raha hu** | Step 1 se 15, **order me** |
| ⏰ **Interview 2-3 din me hai** | Steps **2, 3, 4, 5, 6, 7, 13, 15** (baaki baad me) |
| 🏭 **Production/job me confidence chahiye** | Steps **5 se 14**, phir 15 |

## 3 levels

| Level | Steps | Tum kya seekhoge |
|---|---|---|
| 🟢 **Basic** | 1 se 5 | Page Object kya hai, locators, assertions, agla page |
| 🟡 **Intermediate** | 6 se 9 | BasePage, components, tables, pytest fixtures |
| 🔴 **Advanced** | 10 se 15 | iframe/shadow/popup, anti-patterns, alternatives, production, interview |

## Har step ka format

| Icon | Matlab |
|---|---|
| ⚡ **TL;DR** | Poore step ka ek line me saar |
| 🤕 **Dikkat** | Problem kya hai |
| 💡 **Idea** | Solution |
| ⌨️ **Karo** | Code type karo |
| ▶️ **Chalao** | Command aur **kya aana chahiye** |
| 🔍 **Code samjho** | Line-by-line |
| 🧠 **Kyun? Aur alternatives?** | Humne ye kyun chuna, **doosre options kya the aur kyun nahi** |
| ✅ **Samjha?** | 2 sawaal |
| ✍️ **Khud karo** | Ek chhota kaam |
| 🎤 **Interview line** | Isko interview me kaise bolo |

## 📦 Zip me kya hai

```text
start/            ← yahin se shuru karo (demo shop + 4 messy tests)
solutions/step_NN ← us step ke baad ka poora code (atko tabhi dekho)
experiments/      ← Step 4 aur 5 ke experiments (khud chalake dekhne ke liye)
```
Step 1, 14, 15 me naya code nahi hai. Step 4 aur 5 ke **experiments** `experiments/` folder me hain (`test_expB.py`, `test_expC.py`).

## ✅ Kya maine real me chalaya

| Cheez | Status |
|---|---|
| Is guide ka **saara code** (11 snapshots) | **Real Chromium browser me chalaya**, har step green |
| Experiments (locator strategies, race, `all()`, violation messages) | **Chalake dekhe**, outputs guide me hain |
| Selenium Java ka PageFactory | Mujhe general knowledge se pata hai, **chalaya nahi** |
| Tumhari SauceDemo / Windows / Mac | **Nahi** (Linux par demo app) |

---

# ⚙️ Step 0: Setup (ek baar)

```bash
cd start
python -m venv .venv
source .venv/bin/activate          # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

**Terminal 1** (demo shop chalao, band mat karna):
```bash
python app_under_test/server.py
```
**Terminal 2** (tests):
```bash
pytest
```
**Aana chahiye:** `4 passed` (ek `base_url` warning aa sakti hai, ignore karo).

> Demo shop me login, products, cart, checkout hai. Aur `http://127.0.0.1:8000/playground.html` par advanced practice page (table, modal, iframe, popup). Inka code padhna zaroori nahi.

---

# 🟢 Step 1: POM kya hai aur kyun?

⚡ **TL;DR:** POM = UI ka **model** code me. Har page (ya UI ka hissa) ke liye ek class. Class me **locators + actions**. Tests sirf **business ki bhasha** me.

## 🤕 Dikkat: ye messy code dekho

`tests/test_shop.py` (abhi ka, bina POM ke):

**File: `tests/test_shop.py`**
```python
from playwright.sync_api import expect


def test_login_works(page):
    page.goto("/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="Products")).to_be_visible()


def test_wrong_password_shows_error(page):
    page.goto("/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("wrong-password")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("alert")).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(page):
    page.goto("/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="Products")).to_be_visible()
    page.get_by_test_id("product").filter(has_text="Backpack").get_by_role("button", name="Add to cart").click()
    expect(page.get_by_test_id("cart-count")).to_have_text("1")


def test_user_can_buy_backpack(page):
    page.goto("/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="Products")).to_be_visible()
    page.get_by_test_id("product").filter(has_text="Backpack").get_by_role("button", name="Add to cart").click()
    page.get_by_role("button", name="View Cart").click()
    expect(page.get_by_role("heading", name="Your Cart")).to_be_visible()
    page.get_by_role("button", name="Checkout").click()
    expect(page.get_by_role("heading", name="Thank you for your order!")).to_be_visible()
```

**Ginti karo:**
- Login ki 3 lines: **4 baar** (har test me).
- `get_by_placeholder("Username")`: **4 baar**.
- Kal developer "Login" button ka naam "Sign in" kar de to **4 jagah** badlo. 200 tests = 200 jagah.

## 💡 Idea
```text
Test (kya verify karna hai)
   │   sirf business ki bhasha:  login.login_as(...)
   ▼
Page Object (kaise karna hai)
   │   locators + actions:  fill, fill, click
   ▼
Browser page
```
**Page Object Model** ek **design pattern** hai: UI ke har hisse ke liye ek class, jisme us hisse ke locators aur actions hon. Tests us class se baat karte hain, browser se seedha nahi.

## 3 faide
| Faida | Matlab |
|---|---|
| 🧼 **Maintainable** | UI badla → **ek file** badli |
| 📖 **Readable** | Test padh ke kahani samajh aaye |
| ♻️ **Reusable** | Login ek baar likha, har jagah use |

## ❌ POM kya NAHI hai
- Koi **tool/library** nahi (Playwright me built-in nahi, ye ek tareeka hai).
- "Ek page = ek test" nahi.
- **Selenium ke PageFactory** jaisa kuch nahi (wo alag cheez hai, Step 13 me).

## ✅ Samjha?
<details>
<summary>1. POM ka sabse bada faida ek line me?</summary>

UI ka badlaav **ek jagah** fix hota hai, 200 tests me nahi.
</details>
<details>
<summary>2. Kya POM ek library hai jo install karte hain?</summary>

Nahi. Ye ek **design pattern** hai, hum khud classes likhte hain.
</details>

🎤 **Interview line:** *"POM is a design pattern where each page or UI component has a class that holds its locators and actions, so tests read like business steps and a UI change is fixed in one place."*

---

# 🟢 Step 2: Pehla Page Object (LoginPage)

⚡ **TL;DR:** Login screen ke locators aur actions ek class `LoginPage` me.

## 🤕 Dikkat
Login ki 3 lines har test me repeat hain.

## 💡 Idea
Ek class banao. `__init__` me **locators**, methods me **actions**.

## ⌨️ Karo

1. Folder `pages/` banao aur usme khali `__init__.py` (isse folder "package" banta hai, `from pages.login_page import ...` chalta hai).
2. `pages/login_page.py`:

**File: `pages/login_page.py`**
```python
from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def open(self):
        self.page.goto("/")

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
```

3. `tests/test_shop.py` poora replace:

**File: `tests/test_shop.py`**
```python
from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_login_works(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    expect(page.get_by_role("heading", name="Products")).to_be_visible()


def test_wrong_password_shows_error(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "wrong-password")
    expect(page.get_by_role("alert")).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    expect(page.get_by_role("heading", name="Products")).to_be_visible()
    page.get_by_test_id("product").filter(has_text="Backpack").get_by_role("button", name="Add to cart").click()
    expect(page.get_by_test_id("cart-count")).to_have_text("1")


def test_user_can_buy_backpack(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    expect(page.get_by_role("heading", name="Products")).to_be_visible()
    page.get_by_test_id("product").filter(has_text="Backpack").get_by_role("button", name="Add to cart").click()
    page.get_by_role("button", name="View Cart").click()
    expect(page.get_by_role("heading", name="Your Cart")).to_be_visible()
    page.get_by_role("button", name="Checkout").click()
    expect(page.get_by_role("heading", name="Thank you for your order!")).to_be_visible()
```

## ▶️ Chalao
```bash
pytest
```
**Aana chahiye:** `4 passed`

## 🔍 Code samjho
| Line | Matlab |
|---|---|
| `class LoginPage:` | Login screen ka Python representation |
| `def __init__(self, page: Page)` | Page Object ko Playwright ka `page` milta hai (jaise tab ka remote control) |
| `self.page = page` | Baad ke methods ke liye yaad rakho |
| `self.username = page.get_by_placeholder("Username")` | Username box ka **locator**. Ye element ko **abhi dhundta nahi**, sirf "kaise dhundna hai" yaad rakhta hai (Step 3 me) |
| `def open(self)` | `/` kholo (`base_url` pytest.ini se aata hai) |
| `def login(self, username, password)` | Teen kaam: fill, fill, click. **Business naam: `login`** |
| Test me `login.login("standard_user", "secret_sauce")` | Test ko ab "kaise" nahi pata, sirf "kya" |

## 🧠 Kyun class? Aur alternatives?

| Option | Kya hai | Kyun nahi chuna / kab theek |
|---|---|---|
| **A. Class (Page Object)** ✅ | Locators + actions ek class me | **Chuna.** Grouping, editor autocomplete (`login.` dabao to methods dikhte hain), state (`self.page`), aage composition possible |
| B. Helper functions | `def login(page, u, p)` | Chhote suite me theek (Step 13 me code). Par grouping/autocomplete nahi, locators function ke andar bikhre, composition mushkil |
| C. Locators ke strings constants me | `USERNAME = "#username"` | Sirf locator bachaye, **action** (kaam) nahi. Tests me phir bhi fill/click repeat. Aur string selectors (Step 3) |
| D. Sirf fixtures | login ka kaam fixture me | Setup ke liye achha (Step 9), par UI ka **model** nahi. Alag page par kya karna hai batata nahi |
| E. Record and playback script | Codegen se bani script | Quick demo ke liye theek. Maintainable nahi: har jagah raw locators, repeat |

> Koi ek hamesha "sahi" nahi. **Jab suite 10+ tests se badi ho aur UI badalta ho, tab class (A)** sabse kam dard deti hai.

## ✅ Samjha?
<details>
<summary>1. <code>__init__</code> me locators bante hain, par tab page khula hi nahi tha. Kaise chala?</summary>

Playwright locator **lazy** hota hai: element **action ke waqt** dhundha jaata hai, locator banate waqt nahi. (Step 3 me real proof.)
</details>
<details>
<summary>2. Test me <code>login.login(...)</code> kyun, <code>fill/click</code> kyun nahi?</summary>

Test ko "kya" chahiye, "kaise" nahi. "Kaise" badle (field order, button naam) to sirf page object badlega.
</details>

## ✍️ Khud karo
`test_login_works` me `LoginPage` use ho raha hai par `expect(page.get_by_role("heading", ...))` raw hai. Abhi chhod do (Step 5 me hata denge). Bas ek test aur likho: `locked_user` (password `secret_sauce`) se login, aur `page.get_by_role("alert")` par text `Sorry, this user has been locked out.` check karo.

<details>
<summary>✅ Jawab</summary>

```python
def test_locked_user_shows_error(page):
    login = LoginPage(page)
    login.open()
    login.login("locked_user", "secret_sauce")
    expect(page.get_by_role("alert")).to_have_text("Sorry, this user has been locked out.")
```
(Step 3 me `page.get_by_role("alert")` bhi page object me chala jaayega.)
</details>

🎤 **Interview line:** *"I picked a class over plain helper functions because it groups a page's locators and actions, gives autocomplete, and lets me compose pages and components later."*

🛟 Atak gaye? `solutions/step_02`

---

# 🟢 Step 3: Locators sahi tareeke se

⚡ **TL;DR:** Locators `Locator` objects ho (strings nahi), **user-facing** pehle (`role`, `label`), private rakho, sirf wahi public jo test ko `expect` ke liye chahiye.

## 🤕 Dikkat
Locator likhne ke kai tareeke hain. Kaunsa kab toot-ta hai?

## 💡 Experiment: ek hi button, 5 tareeke (real run)

| Tareeka | Code | Aaj kitne element mile | Kab toot-ta hai |
|---|---|---|---|
| 🥇 **Role + naam** | `get_by_role("button", name="Login")` | **1** | Button ka **text** badle |
| 🥈 **id (CSS)** | `locator("#login-btn")` | **1** | Developer `id` badle |
| 🥉 **CSS structure** | `locator("section#login-view > button")` | **1** | HTML ka **structure** badle |
| ⚠️ **Position** | `locator("button").first` | **1** | **Koi bhi** nayi button upar jod de |
| 🔴 **XPath (lamba)** | `xpath=//*[@id='login-view']/button` | **1** | Structure ya id badle |

**Aaj paanchon chalte hain**, par kal ka badlaav alag cheez todta hai. Isliye **user-facing (role/label/placeholder)** pehle: wo wahi cheez dekhte hain jo user dekhta hai.

**Practical ladder (upar se neeche try karo):** `get_by_role` → `get_by_label` → `get_by_placeholder` → `get_by_text` → `get_by_test_id` (developer ke saath contract) → CSS → XPath (aakhri).

## 🔬 Locator lazy hota hai (real proof)
```text
about:blank par locator bana, count = 0
site khulne ke baad wahi locator, count = 1
```
Matlab: locator "dhundhne ka tareeka" hai, element ka **snapshot nahi**. Isliye page khulne se pehle `__init__` me banana safe hai, aur DOM dobara draw ho to bhi wahi locator kaam karta hai.

## ⌨️ Karo
`pages/login_page.py` replace (ab private/public dono):

**File: `pages/login_page.py`**
```python
from playwright.sync_api import Locator, Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_button = page.get_by_role("button", name="Login")
        self.error: Locator = page.get_by_role("alert")

    def open(self):
        self.page.goto("/")

    def login(self, username: str, password: str):
        self._username.fill(username)
        self._password.fill(password)
        self._login_button.click()
```

`tests/test_shop.py` me `test_wrong_password_shows_error` ab `login.error` use karta hai:

**File: `tests/test_shop.py`** (sirf ye badlaav: `-` hatao, `+` jodo)
```diff
     login.login("standard_user", "wrong-password")
-    expect(page.get_by_role("alert")).to_have_text("Username and password do not match")
+    expect(login.error).to_have_text("Username and password do not match")
 
```

## ▶️ Chalao
`pytest` → **`4 passed`**

## 🔍 Code samjho
| Line | Matlab |
|---|---|
| `self._username = ...` | **Underscore = private** ("ye page ke andar ki cheez"). Test `login()` use kare, `_username.fill()` nahi |
| `self.error: Locator = page.get_by_role("alert")` | **Public**, kyunki test ko `expect(login.error)...` likhna hai |
| `: Locator` | Type hint: editor ko batata hai ye Locator hai (autocomplete) |

## 🧠 Kyun? Aur alternatives?

**Locator object ya string selector?**

| Option | Kaisa dikhta hai | Dikkat |
|---|---|---|
| String store karna | `self.username = "#username"` | Har use par `page.locator(self.username)` likhna, typo ka darr, user-facing options ka fayda nahi ❌ |
| **`Locator` object** ✅ | `page.get_by_placeholder("Username")` | Ek baar banao, har jagah wahi. Lazy, retry-safe, editor madad karta hai |

**Public ya private?**
- Test ko jo cheez **`expect` se verify** karni hai → public `Locator` (jaise `error`, `cart_badge`).
- Baaki sab → private. Isse test galti se `click()` jaise low-level kaam nahi karte.

**Public cheez text kyun nahi, `Locator` kyun?** Step 4 me real proof.

## ✅ Samjha?
<details>
<summary>1. "Position" wala locator (<code>button.first</code>) kyun khatarnak hai?</summary>

Kal koi nayi button upar aa gayi to **galat button** click hoga, aur test chup-chap galat cheez karega.
</details>
<details>
<summary>2. <code>get_by_test_id</code> kab use karein?</summary>

Jab role/label se element pakda na jaye ya text badalta rehta ho. Developer ke saath **contract** ho ki `data-testid` nahi badlega.
</details>

## ✍️ Khud karo
Browser me app kholo, Inspect karke Backpack ka "Add to cart" button dhundo. Us ke liye role-based aur CSS-based dono locator likho. Kaunsa chhota aur samajhne layak hai?

🎤 **Interview line:** *"I prefer user-facing locators like role and label, keep them as Locator objects inside the page class, and expose only the ones tests need to assert on."*

🛟 Atak gaye? `solutions/step_03`

---

# 🟢 Step 4: Assertions kahan likhein? (page me ya test me)

⚡ **TL;DR:** **Business assertion test me.** Page Object **Locator expose** kare, test `expect(...)` kare. (Page me sirf "page load hua" jaisa readiness wait.)

## 🤕 Dikkat
Do tareeke hain. Kaunsa behtar? (Is step me sirf sochna aur experiment dekhna hai, naya code nahi.)

| Tareeka | Code |
|---|---|
| **A.** Page me verify method | `login.verify_error("...")` → andar `assert self.error.inner_text() == msg` |
| **B.** Page Locator de, test `expect` kare | `expect(login.error).to_have_text("...")` |

## 🔬 Real experiment: login API **500ms slow** kar di

Test code (maine ye chalaya):

**File: `tests/test_expB.py`**
```python
import time
from playwright.sync_api import expect
from pages.login_page import LoginPage

def _slow_login(page):
    def handler(route):
        time.sleep(0.5)
        route.continue_()
    page.route("**/api/login", handler)

def test_plain_assert_on_inner_text(page):
    _slow_login(page)
    login = LoginPage(page).open()
    login.attempt_login("standard_user", "wrong-password")
    assert login.error.inner_text() == "Username and password do not match"

def test_expect_on_locator(page):
    _slow_login(page)
    login = LoginPage(page).open()
    login.attempt_login("standard_user", "wrong-password")
    expect(login.error).to_have_text("Username and password do not match")

def test_expect_wrong_text_message(page):
    login = LoginPage(page).open()
    login.attempt_login("standard_user", "wrong-password")
    expect(login.error).to_have_text("Kuch aur likha hai", timeout=1500)
```

**Result:**

| Test | Nateeja |
|---|---|
| `inner_text()` par plain `assert` | ❌ **FAIL:** `assert '' == 'Username and password do not match'` |
| `expect(login.error).to_have_text(...)` | ✅ **PASS** |

**Kyun?** `inner_text()` **ek baar padhta hai**, us waqt error abhi aaya hi nahi tha (khaali `''`). `expect` **intezaar karta hai** (retry) jab tak text mil jaye.

**Galat text par `expect` ka message** (kitna madad-gaar):
```text
AssertionError: Locator expected to have text 'Kuch aur likha hai'
Actual value: Username and password do not match
  - unexpected value ""
  - unexpected value "Username and password do not match"
```
Isme dikhta hai ki **kya mila aur kya expected tha**.

## 🧠 Kyun? Aur alternatives?
| Option | Dikkat |
|---|---|
| **A. Page me `verify_*` + plain `assert`** | Race condition (upar dekha). Ek page method ek hi expectation ke liye. Alag test alag cheez chahe to naya method ❌ |
| **A'. Page me `expect(...)` wale verify methods** | Race nahi. Par page ek hi expectation me **fas** jaata hai ("error aaya") aur test ki zimmedari (kya sahi hai) page me chali jaati hai |
| **B. Locator expose, test me `expect`** ✅ | Retry, saaf message, test **apni expectation** khud likhta hai |

**Rule (yaad rakho):**
- ✅ Page me: **readiness wait** (`wait_until_loaded`: "page taiyar hai"), actions, Locators expose karna, values **padhna** (jaise order id).
- ❌ Page me: "kya sahi hai" ka faisla (`assert`).

> Kuch teams page me `expect` wale methods rakhti hain. Wo galat nahi, par **ek convention chuno aur pura project same rakho**.

## ✍️ Khud karo (experiment chalao)
`experiments/test_expB.py` ko `solutions/step_06/tests/` me copy karo aur chalao:
```bash
pytest tests/test_expB.py
```
**Aana chahiye:** `2 failed, 1 passed` (ek race wala fail, ek jaan-boojh ke galat text wala fail, ek `expect` pass). Jab tum ye khud dekh lo, tab interview me ye example **sach me bol sakte ho**.

## ✅ Samjha?
<details>
<summary>1. <code>inner_text()</code> ke saath plain <code>assert</code> kab flaky hota hai?</summary>

Jab UI async update hota hai (API se text aata hai). `inner_text()` ek hi baar padhta hai.
</details>
<details>
<summary>2. Page me <code>wait_until_loaded</code> me <code>expect</code> hai. Ye rule ke khilaf nahi?</summary>

Nahi: wo **business check nahi**, **readiness** hai ("page taiyar"). Business check test me.
</details>

🎤 **Interview line:** *"I keep business assertions in tests and expose Locators from page objects, so I get Playwright's auto-retrying expect and clear failure messages instead of one-shot reads."*

---

# 🟢 Step 5: Agla page lautao (navigation)

⚡ **TL;DR:** Jo method **naye page par le jaata hai**, wo us **naye page ka object lautaye**. Jab nateeja do ho sakte hain (success/fail), **alag methods** rakho.

## 🤕 Dikkat
Abhi tests me inventory, cart, order-complete ke locators raw hain. Aur "login ke baad kya?" kaun batayega?

## 💡 Idea
- Har screen ka Page Object.
- `login_as(...)` **inventory page lautata hai**, `cart.checkout()` **order-complete page**.

## ⌨️ Karo
Naye 3 pages aur `LoginPage` ka naya version:

**File: `pages/login_page.py`**
```python
from playwright.sync_api import Locator, Page

from pages.inventory_page import InventoryPage


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_button = page.get_by_role("button", name="Login")
        self.error: Locator = page.get_by_role("alert")

    def open(self):
        self.page.goto("/")

    def attempt_login(self, username: str, password: str) -> "LoginPage":
        """Login try karo. Kya hoga pata nahi (success ya error), isliye wahi page lautao."""
        self._username.fill(username)
        self._password.fill(password)
        self._login_button.click()
        return self

    def login_as(self, username: str, password: str) -> InventoryPage:
        """Login jo SUCCESS hona chahiye. Agla page (inventory) lautao."""
        self.attempt_login(username, password)
        inventory = InventoryPage(self.page)
        inventory.wait_until_loaded()
        return inventory
```

**File: `pages/inventory_page.py`**
```python
from playwright.sync_api import Page, expect

from pages.cart_page import CartPage


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self._heading = page.get_by_role("heading", name="Products")
        self.cart_badge = page.get_by_test_id("cart-count")
        self._cart_button = page.get_by_role("button", name="View Cart")
        self._cards = page.get_by_test_id("product")

    def wait_until_loaded(self):
        expect(self._heading).to_be_visible()

    def add_to_cart(self, product_name: str):
        self._cards.filter(has_text=product_name).get_by_role("button", name="Add to cart").click()

    def open_cart(self) -> CartPage:
        self._cart_button.click()
        cart = CartPage(self.page)
        cart.wait_until_loaded()
        return cart
```

**File: `pages/cart_page.py`**
```python
from playwright.sync_api import Page, expect

from pages.order_complete_page import OrderCompletePage


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self._heading = page.get_by_role("heading", name="Your Cart")
        self._checkout_button = page.get_by_role("button", name="Checkout")

    def wait_until_loaded(self):
        expect(self._heading).to_be_visible()

    def checkout(self) -> OrderCompletePage:
        self._checkout_button.click()
        done = OrderCompletePage(self.page)
        done.wait_until_loaded()
        return done
```

**File: `pages/order_complete_page.py`**
```python
from playwright.sync_api import Page, expect


class OrderCompletePage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Thank you for your order!")

    def wait_until_loaded(self):
        expect(self.heading).to_be_visible()
```

`tests/test_shop.py` replace:

**File: `tests/test_shop.py`**
```python
from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_login_works(page):
    login = LoginPage(page)
    login.open()
    inventory = login.login_as("standard_user", "secret_sauce")
    expect(inventory.cart_badge).to_have_text("0")


def test_wrong_password_shows_error(page):
    login = LoginPage(page)
    login.open()
    login.attempt_login("standard_user", "wrong-password")
    expect(login.error).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(page):
    login = LoginPage(page)
    login.open()
    inventory = login.login_as("standard_user", "secret_sauce")
    inventory.add_to_cart("Backpack")
    expect(inventory.cart_badge).to_have_text("1")


def test_user_can_buy_backpack(page):
    login = LoginPage(page)
    login.open()
    inventory = login.login_as("standard_user", "secret_sauce")
    inventory.add_to_cart("Backpack")
    cart = inventory.open_cart()
    done = cart.checkout()
    expect(done.heading).to_be_visible()
```

## ▶️ Chalao
`pytest` → **`4 passed`**

## 🔍 Code samjho
| Line | Matlab |
|---|---|
| `from pages.inventory_page import InventoryPage` (login me) | `LoginPage` ko pata hai ki login ke baad kaunsa page aata hai |
| `attempt_login(...) -> "LoginPage"` | Login **try** karo. **Kya hoga pata nahi** (success ya error), isliye wahi page lautao |
| `login_as(...) -> InventoryPage` | Login jo **success hona chahiye**. `inventory.wait_until_loaded()` phir agla page |
| `open_cart() -> CartPage`, `checkout() -> OrderCompletePage` | Har navigation agla page deta hai |
| Test: `inventory = login.login_as(...)` | Ab `inventory` ke methods autocomplete me dikhte hain |
| Test: `done = inventory.open_cart().checkout()` | Padhne me kahani: login → cart → checkout |

## 🔬 Do methods kyun? (real experiment)
Agar **galat password** ke saath `login_as` use karo to kya hota hai? Test (`experiments/test_expC.py`, `solutions/step_06/tests/` me copy karke chalao):

**File: `tests/test_expC.py`**
```python
from pages.login_page import LoginPage

def test_login_as_with_wrong_password(page):
    LoginPage(page).open().login_as("standard_user", "wrong-password")
```

**Real output:**
```text
AssertionError: Locator expected to be visible
Error: element(s) not found
  - waiting for get_by_role("heading", name="Products")
```
Ye message batata hai *"Products heading nahi mili"*, **asli wajah (galat password) nahi**. Isliye negative test me `attempt_login` (jo `LoginPage` lautata hai aur `login.error` check karne deta hai).

## 🧠 Kyun? Aur alternatives?
| Option | Dikkat / faida |
|---|---|
| Methods kuch na lautayein, test khud `InventoryPage(page)` banaye | Chalta hai, par test ko pata hona chahiye "kaunsa page aata hai". Page ka **flow** page object me nahi |
| **Methods agla page lautayein** ✅ | Flow code me likha hai, autocomplete, galat page par galat method call nahi hota |
| Ek hi `login()` jo kabhi bhi kuch lautaye | Return type confusing, success/failure mix ❌ |
| **Alag methods** (`login_as` aur `attempt_login`) ✅ | Har method ka ek hi nateeja, saaf type |
| Har method `self` lautaye (fluent chain) | Same-page actions me over-chaining padhne me bhari. Humne **sirf navigation** me page lautaya |

**Circular import dhyan:** `LoginPage` → `InventoryPage` → `CartPage` → `OrderCompletePage`. Har page sirf **aage wale** ko import karta hai. Agar `InventoryPage` bhi `LoginPage` ko import kare (logout ke liye) to circle ban jaayega (tab type-hint string me ya function ke andar import).

## ✅ Samjha?
<details>
<summary>1. <code>login_as</code> aur <code>attempt_login</code> alag kyun?</summary>

`login_as` success maanta hai aur `InventoryPage` deta hai. `attempt_login` nateeja khula chhodta hai (error check ke liye). Ek method ka ek hi nateeja = type saaf.
</details>
<details>
<summary>2. <code>add_to_cart</code> kuch lautata kyun nahi?</summary>

Wo **same page** par kaam hai, navigation nahi. Naya page nahi aaya, to kuch lautana nahi.
</details>

## ✍️ Khud karo
Ek test likho jo `login_as` se login karke `inventory.add_to_cart("Onesie")` kare aur `cart_badge` `"1"` check kare.

🎤 **Interview line:** *"Navigation methods return the next page object, and when an action can have two outcomes I use two methods, for example login_as for success and attempt_login for negative tests."*

🛟 Atak gaye? `solutions/step_05`

---

# 🟡 Step 6: BasePage (jo sab pages me same hai)

⚡ **TL;DR:** Jo cheez **sab pages me same** hai (open, load wait) wo `BasePage` me. Child sirf batata hai "mere page ke load hone ka matlab".

## 🤕 Dikkat
Step 5 ke pages dekho. Har page me ye repeat hai:
```python
def wait_until_loaded(self):
    expect(self._heading).to_be_visible()
```
4 pages = 4 baar. Aur `open()` sirf login me hai.

## 💡 Idea
Common cheez ek **base class** me. (Is design ko **Template Method** kehte hain: base class ek template deta hai, child ek tukda bharta hai.)

## ⌨️ Karo
Folder `core/` + khali `__init__.py`. Phir:

**File: `core/base_page.py`**
```python
from playwright.sync_api import Locator, Page, expect


class BasePage:
    path = "/"

    def __init__(self, page: Page):
        self.page = page

    @property
    def loaded_locator(self) -> Locator:
        raise NotImplementedError("Child page 'loaded_locator' define kare")

    def wait_until_loaded(self):
        expect(self.loaded_locator).to_be_visible()
        return self

    def open(self):
        self.page.goto(self.path)
        return self.wait_until_loaded()
```

`pages/login_page.py` (poora):

**File: `pages/login_page.py`**
```python
from playwright.sync_api import Locator, Page

from core.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    path = "/"

    def __init__(self, page: Page):
        super().__init__(page)
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_button = page.get_by_role("button", name="Login")
        self.error: Locator = page.get_by_role("alert")

    @property
    def loaded_locator(self) -> Locator:
        return self._login_button

    def attempt_login(self, username: str, password: str) -> "LoginPage":
        self._username.fill(username)
        self._password.fill(password)
        self._login_button.click()
        return self

    def login_as(self, username: str, password: str) -> InventoryPage:
        self.attempt_login(username, password)
        return InventoryPage(self.page).wait_until_loaded()
```

Baaki 3 pages me sirf ye badlaav:

**File: `pages/inventory_page.py`** (sirf ye badlaav: `-` hatao, `+` jodo)
```diff
-from playwright.sync_api import Page, expect
+from playwright.sync_api import Locator, Page
 
+from core.base_page import BasePage
 from pages.cart_page import CartPage
  ...
 
-class InventoryPage:
+class InventoryPage(BasePage):
+    path = "/"
+
     def __init__(self, page: Page):
-        self.page = page
+        super().__init__(page)
         self._heading = page.get_by_role("heading", name="Products")
  ...
 
-    def wait_until_loaded(self):
-        expect(self._heading).to_be_visible()
+    @property
+    def loaded_locator(self) -> Locator:
+        return self._heading
 
  ...
         self._cart_button.click()
-        cart = CartPage(self.page)
-        cart.wait_until_loaded()
-        return cart
+        return CartPage(self.page).wait_until_loaded()
```

**File: `pages/cart_page.py`** (sirf ye badlaav: `-` hatao, `+` jodo)
```diff
-from playwright.sync_api import Page, expect
+from playwright.sync_api import Locator, Page
 
+from core.base_page import BasePage
 from pages.order_complete_page import OrderCompletePage
  ...
 
-class CartPage:
+class CartPage(BasePage):
     def __init__(self, page: Page):
-        self.page = page
+        super().__init__(page)
         self._heading = page.get_by_role("heading", name="Your Cart")
  ...
 
-    def wait_until_loaded(self):
-        expect(self._heading).to_be_visible()
+    @property
+    def loaded_locator(self) -> Locator:
+        return self._heading
 
  ...
         self._checkout_button.click()
-        done = OrderCompletePage(self.page)
-        done.wait_until_loaded()
-        return done
+        return OrderCompletePage(self.page).wait_until_loaded()
```

**File: `pages/order_complete_page.py`** (sirf ye badlaav: `-` hatao, `+` jodo)
```diff
-from playwright.sync_api import Page, expect
+from playwright.sync_api import Locator, Page
+
+from core.base_page import BasePage
 
 
-class OrderCompletePage:
+class OrderCompletePage(BasePage):
     def __init__(self, page: Page):
-        self.page = page
+        super().__init__(page)
         self.heading = page.get_by_role("heading", name="Thank you for your order!")
 
-    def wait_until_loaded(self):
-        expect(self.heading).to_be_visible()
+    @property
+    def loaded_locator(self) -> Locator:
+        return self.heading
```

`tests/test_shop.py` replace:

**File: `tests/test_shop.py`**
```python
from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_login_works(page):
    inventory = LoginPage(page).open().login_as("standard_user", "secret_sauce")
    expect(inventory.cart_badge).to_have_text("0")


def test_wrong_password_shows_error(page):
    login = LoginPage(page).open()
    login.attempt_login("standard_user", "wrong-password")
    expect(login.error).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(page):
    inventory = LoginPage(page).open().login_as("standard_user", "secret_sauce")
    inventory.add_to_cart("Backpack")
    expect(inventory.cart_badge).to_have_text("1")


def test_user_can_buy_backpack(page):
    inventory = LoginPage(page).open().login_as("standard_user", "secret_sauce")
    inventory.add_to_cart("Backpack")
    done = inventory.open_cart().checkout()
    expect(done.heading).to_be_visible()
```

## ▶️ Chalao
`pytest` → **`4 passed`**

## 🔍 Code samjho
| Line | Matlab |
|---|---|
| `path = "/"` | Page ka URL path. Child badal sakta hai (`path = "/playground.html"`) |
| `@property def loaded_locator(...)` + `raise NotImplementedError` | **Child ko batana padega.** Nahi bataya to saaf error. Har page ke liye "load hua" ka matlab alag hai |
| `wait_until_loaded()` | `loaded_locator` dikhne tak **wait** (retry), `return self` |
| `open()` | `goto(path)` phir `wait_until_loaded()` |
| `return self` | Chain: `LoginPage(page).open().login_as(...)` |
| `class LoginPage(BasePage)` | `BasePage` ka sab mil gaya |
| `super().__init__(page)` | Parent ka `__init__` bhi chalao |

## 🔬 Waiting ka rule (production ke liye bahut zaroori)
`wait_until_loaded` me `expect(...)`. **`time.sleep` nahi.**

| Tareeka | Kyun nahi |
|---|---|
| `time.sleep(2)` | Kabhi zyada (slow suite), kabhi kam (flaky) ❌ |
| `wait_for_timeout(2000)` | Wahi, sleep ka dusra naam ❌ |
| `wait_for_load_state("networkidle")` | Aajkal ke apps me hamesha idle nahi hota, aur "page load" ka sahi matlab nahi batata ❌ |
| **`expect(locator).to_be_visible()`** ✅ | **Condition** par wait. Jitni der chahiye utni hi |

## 🧠 Kyun? Aur alternatives?
| Option | Dikkat / faida |
|---|---|
| Koi base class nahi | Repeat (4x), "wait lagana bhool gaye" ki galti |
| **Chhota BasePage** ✅ | Repeat khatam, har `open()` ek jaisa |
| **Bada BasePage** (click, fill, type wrappers, 50 methods) | **God class** ❌. Ek change sab ko hilata hai. Playwright ka locator API pehle se achha hai, wrapper bekaar layer |
| Mixins / multiple inheritance | Chhote tukde (e.g. `WaitMixin`) theek, par ulajhna jaldi hota hai. Pehle composition (Step 7) |
| Utility functions | Common helpers ke liye theek, par "page ka template" nahi de sakte |

> [!WARNING]
> **BasePage me sirf wahi jo SAB pages ko chahiye.** `login()` ya `add_to_cart()` BasePage me daaloge to wo kabaad ka dher ban jaayega.

## ✅ Samjha?
<details>
<summary>1. Child ne <code>loaded_locator</code> nahi likha to?</summary>

`NotImplementedError: Child page 'loaded_locator' define kare`. Jaan-boojh ke saaf error.
</details>
<details>
<summary>2. <code>wait_until_loaded</code> me <code>sleep(2)</code> kyun nahi?</summary>

Slow ya fast machine par ek jaisa nahi. Condition par wait sahi, time par nahi.
</details>

## ✍️ Khud karo
Ek khayali `ProfilePage(BasePage): pass` banao aur temporary test me `ProfilePage(page).open()` chalao. Kya error aaya?

🎤 **Interview line:** *"I keep the base page tiny: path, open and a readiness wait using expect. Anything page-specific stays in the child, otherwise the base becomes a god class."*

🛟 Atak gaye? `solutions/step_06`

---

# 🟡 Step 7: Components (jab UI ka hissa repeat hota hai)

⚡ **TL;DR:** Jo hissa **repeat** hota hai (list ke items) ya **kai pages par** dikhta hai, uska alag class (**Component**). Component apne **root Locator** se banta hai, page se nahi.

## 🤕 Dikkat
`InventoryPage.add_to_cart(name)` product ke baare me **sab kuch** jaanta hai: naam, price, button. Kal price check, remove button, rating jodoge to `InventoryPage` phool jaayega.

## 💡 Idea
Ek **product card** = ek class `ProductCard`. Wo apne **root** (us card ka box) ke andar hi dhundhta hai.

## ⌨️ Karo
Folder `components/` + khali `__init__.py`:

**File: `components/product_card.py`**
```python
from playwright.sync_api import Locator


class ProductCard:
    """Ek product card. Page se nahi, apne 'root' locator se bana hai."""

    def __init__(self, root: Locator):
        self._root = root
        self.name: Locator = root.locator(".name")
        self.price: Locator = root.locator(".price")
        self.action_button: Locator = root.get_by_role("button")

    def add_to_cart(self):
        self._root.get_by_role("button", name="Add to cart").click()

    def remove_from_cart(self):
        self._root.get_by_role("button", name="Remove").click()
```

`pages/inventory_page.py` (diff):

**File: `pages/inventory_page.py`** (sirf ye badlaav: `-` hatao, `+` jodo)
```diff
 
+from components.product_card import ProductCard
 from core.base_page import BasePage
  ...
         self._cards = page.get_by_test_id("product")
+        self.names: Locator = self._cards.locator(".name")
 
  ...
 
-    def add_to_cart(self, product_name: str):
-        self._cards.filter(has_text=product_name).get_by_role("button", name="Add to cart").click()
+    def product(self, name: str) -> ProductCard:
+        return ProductCard(self._cards.filter(has_text=name))
 
```

`tests/test_shop.py` replace:

**File: `tests/test_shop.py`**
```python
from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_login_works(page):
    inventory = LoginPage(page).open().login_as("standard_user", "secret_sauce")
    expect(inventory.cart_badge).to_have_text("0")


def test_wrong_password_shows_error(page):
    login = LoginPage(page).open()
    login.attempt_login("standard_user", "wrong-password")
    expect(login.error).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(page):
    inventory = LoginPage(page).open().login_as("standard_user", "secret_sauce")
    inventory.product("Backpack").add_to_cart()
    expect(inventory.cart_badge).to_have_text("1")


def test_product_card_shows_price_and_toggles_button(page):
    inventory = LoginPage(page).open().login_as("standard_user", "secret_sauce")
    backpack = inventory.product("Backpack")
    expect(backpack.price).to_have_text("$29.99")
    expect(backpack.action_button).to_have_text("Add to cart")
    backpack.add_to_cart()
    expect(backpack.action_button).to_have_text("Remove")


def test_products_are_listed_alphabetically(page):
    inventory = LoginPage(page).open().login_as("standard_user", "secret_sauce")
    expect(inventory.names).to_have_text(["Backpack", "Bike Light", "Onesie"])


def test_user_can_buy_backpack(page):
    inventory = LoginPage(page).open().login_as("standard_user", "secret_sauce")
    inventory.product("Backpack").add_to_cart()
    done = inventory.open_cart().checkout()
    expect(done.heading).to_be_visible()
```

## ▶️ Chalao
`pytest` → **`6 passed`**

## 🔍 Code samjho
| Line | Matlab |
|---|---|
| `def __init__(self, root: Locator)` | Component ko **page nahi, apna root Locator** milta hai (ek card ka box) |
| `root.locator(".name")` | **Is card ke andar** ka naam. Doosre card ka nahi |
| `self.action_button = root.get_by_role("button")` | Is card ka button (public: test `to_have_text("Remove")` check kare) |
| `self._cards.filter(has_text=name)` | Saare cards me se wo jisme ye naam hai |
| `def product(self, name) -> ProductCard` | Page ek **card lautata hai**, kaam card karta hai |
| `inventory.product("Backpack").add_to_cart()` | Test padhne me saaf: "Backpack product ko cart me daalo" |
| `self.names = self._cards.locator(".name")` | **Saare** cards ke naam (public Locator), list assertion ke liye |
| `expect(inventory.names).to_have_text([...])` | **List assertion**: ginti + order + retry |

## 🔬 Ek jaal: `all()` wait nahi karta (real)
```text
all() turant: 0 | expect ke baad: 2
```
`locator.all()` jo us waqt page par hai wahi deta hai, **wait nahi karta**. Isliye pehle `expect(locator).to_have_count(n)` se intezaar, phir `all()`. Zyadatar kaam `filter`/`nth` aur `expect` se ho jaata hai, `all()` ki zaroorat kam padti hai.

## 🧠 Kyun? Aur alternatives?
| Option | Dikkat / faida |
|---|---|
| Page me `add_to_cart(name)`, `price_of(name)`, `is_added(name)`... | Page har product-baat ke methods se bhar jaata hai ❌ |
| **`ProductCard` component, root Locator se** ✅ | Chhota, reuse (Orders ki row bhi isi idea se, Step 8), page patla |
| Component page ko leke apna locator banaye (`page.locator(".card")`) | Kaun sa card? Sab matched, "strict mode" error ya galat card ❌. **Root se scope** karna zaroori |
| Har item ke liye alag page object | Item ka koi URL nahi, ye page nahi, component hai |

**Component kab banao?**
- 🔁 **Repeat hota hai** (list/table ka item).
- 🧱 **Kai pages par** hai (header, nav, footer).
- 📏 Page **bada** ho raha hai (200+ lines) aur ek hissa alag samajhne layak hai.
- ❌ Agar sirf ek jagah ek baar hai aur chhota hai, **abhi component mat banao** (YAGNI).

## ✅ Samjha?
<details>
<summary>1. Component ko <code>page</code> ki jagah <code>root</code> kyun?</summary>

Taaki sab kuch **us ek item ke andar** hi dhundhe. Page se banate to saare cards me se match hota.
</details>
<details>
<summary>2. Page <code>ProductCard</code> lautata hai, <code>add_to_cart</code> khud kyun nahi?</summary>

Page ko product ke detail ka pata nahi hona chahiye. "Ye card lo" page ka kaam, "card ke saath kya karna" card ka.
</details>

## ✍️ Khud karo
`test_remove_from_cart` likho: Backpack add karo, phir `remove_from_cart()` karo, aur `cart_badge` `"0"` ho.

<details>
<summary>✅ Jawab</summary>

```python
def test_remove_from_cart(page):
    inventory = LoginPage(page).open().login_as("standard_user", "secret_sauce")
    backpack = inventory.product("Backpack")
    backpack.add_to_cart()
    expect(inventory.cart_badge).to_have_text("1")
    backpack.remove_from_cart()
    expect(inventory.cart_badge).to_have_text("0")
```
</details>

🎤 **Interview line:** *"For repeated UI like list items I use a component built from a root locator, so every query is scoped to that item and the page object stays small."*

🛟 Atak gaye? `solutions/step_07`

---

# 🟡 Step 8: Tables aur modals

⚡ **TL;DR:** Table = `OrdersTable` (rows) + `OrderRow` (ek row). Row ko **uski ID se** dhundo (index ya adhoori text se nahi). Modal alag component.

## 🤕 Dikkat
Table me row kaise dhundhein jab data badalta rehta hai? Aur "1002 order cancel karo" kaise likhein?

Practice page: `http://127.0.0.1:8000/playground.html` (Orders table, Details button, Cancel button, modal).

## 🔬 Row dhundhne ke tareeke (real experiment)
| Tareeka | Result | Kyun |
|---|---|---|
| `rows.nth(1)` | Aaj 1002 mila | **Index par bharosa nahi**: order badla to galat row ❌ |
| `rows.filter(has_text="100")` | **4 rows** (sab) | Text **substring** match karta hai ❌ |
| `rows.filter(has_text="Pending")` | **2 rows** | Status par filter, ek row nahi |
| `rows.filter(has_text="1002")` | 1 row | Chalta hai, par "10020" hota to bhi match |
| ✅ `rows.filter(has=id_cell_exact("1002"))` | **1 row** | **ID wali cell ka exact match** |

## ⌨️ Karo

**File: `components/order_details_modal.py`**
```python
from playwright.sync_api import Locator, Page, expect


class OrderDetailsModal:
    def __init__(self, page: Page):
        self.root: Locator = page.get_by_role("dialog", name="Order details")
        self.title: Locator = self.root.get_by_role("heading")
        self._close_button = self.root.get_by_role("button", name="Close")

    def wait_until_open(self):
        expect(self.root).to_be_visible()
        return self

    def close(self):
        self._close_button.click()
```

**File: `components/orders_table.py`**
```python
from playwright.sync_api import Locator, Page

from components.order_details_modal import OrderDetailsModal


class OrderRow:
    def __init__(self, root: Locator, page: Page):
        self._page = page
        self.customer: Locator = root.get_by_test_id("customer")
        self.status: Locator = root.get_by_test_id("status")
        self.cancel_button: Locator = root.get_by_role("button", name="Cancel")
        self._details_button = root.get_by_role("button", name="Details")

    def cancel(self):
        self.cancel_button.click()

    def open_details(self) -> OrderDetailsModal:
        self._details_button.click()
        return OrderDetailsModal(self._page).wait_until_open()


class OrdersTable:
    def __init__(self, page: Page):
        self._page = page
        self.rows: Locator = page.get_by_test_id("order-row")

    def row_for(self, order_id: str) -> OrderRow:
        id_cell = self._page.get_by_test_id("order-id").get_by_text(order_id, exact=True)
        return OrderRow(self.rows.filter(has=id_cell), self._page)
```

**File: `pages/playground_page.py`**
```python
from playwright.sync_api import Locator, Page

from components.orders_table import OrdersTable
from core.base_page import BasePage


class PlaygroundPage(BasePage):
    path = "/playground.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self._heading = page.get_by_role("heading", name="Playground")
        self.orders = OrdersTable(page)

    @property
    def loaded_locator(self) -> Locator:
        return self._heading
```

**File: `tests/test_orders.py`**
```python
from playwright.sync_api import expect

from pages.playground_page import PlaygroundPage


def test_orders_table_shows_four_orders(page):
    playground = PlaygroundPage(page).open()
    expect(playground.orders.rows).to_have_count(4)


def test_pending_order_can_be_cancelled(page):
    playground = PlaygroundPage(page).open()
    row = playground.orders.row_for("1002")

    expect(row.status).to_have_text("Pending")
    row.cancel()

    expect(row.status).to_have_text("Cancelled")
    expect(row.cancel_button).to_have_count(0)


def test_order_details_modal_opens_and_closes(page):
    playground = PlaygroundPage(page).open()

    modal = playground.orders.row_for("1001").open_details()
    expect(modal.title).to_have_text("Order #1001")

    modal.close()
    expect(modal.root).to_be_hidden()
```

## ▶️ Chalao
`pytest` → **`9 passed`**

## 🔍 Code samjho
| Line | Matlab |
|---|---|
| `class OrderRow` | **Ek row**: customer, status, cancel button, details button |
| `root.get_by_test_id("status")` | Is row ke andar ka status |
| `self.cancel_button` (public) | Test `to_have_count(0)` se check kare ki cancel ke baad button gayab |
| `open_details() -> OrderDetailsModal` | Details click karo, **modal object** lautao (navigation jaisa idea) |
| `OrdersTable.row_for(order_id)` | `page.get_by_test_id("order-id").get_by_text(order_id, exact=True)`: **sirf ID wali cell**, exact |
| `self.rows.filter(has=id_cell)` | Wo row jiske andar ye cell hai |
| `page.get_by_role("dialog", name="Order details")` | Modal ka root (dialog ka accessible naam se) |
| `wait_until_open()` | Modal dikhne tak wait (readiness) |
| `PlaygroundPage` | Page = components ka jod (`self.orders = OrdersTable(page)`) |

**Test ka ek kamaal:** `test_pending_order_can_be_cancelled` me `row` ek baar bana, cancel ke baad table **dobara draw** hota hai (purani `<tr>` hat-ti hai), phir bhi `row.status` sahi chala. **Locator lazy hai**, har baar naye DOM me dhundhta hai.

## 🧠 Kyun? Aur alternatives?
| Option | Dikkat / faida |
|---|---|
| `nth(index)` | Data badla to galat row ❌ |
| Poori row ka `has_text` | Substring pitfall ❌ |
| **ID cell ka exact match** ✅ | Stable aur seedha business key (order id) |
| Table ko 2D list me padhna (`[[...]]`) | Dikhane ke liye theek, par **action** (cancel) ke liye nahi, aur retry nahi |
| Modal ke liye alag page object | Modal ka URL nahi, ye **component** hai |

## ✅ Samjha?
<details>
<summary>1. <code>has_text="100"</code> ne 4 rows kyun diye?</summary>

Kyunki "1001", "1002", "1003", "1004" sab me "100" hai. `has_text` **substring** hai.
</details>
<details>
<summary>2. Cancel ke baad <code>row</code> locator kaam kyun karta raha?</summary>

Locator ek **query** hai, element ka snapshot nahi. DOM badla to nayi query naye element par chalti hai.
</details>

## ✍️ Khud karo
Ek test likho: order `1004` ka status `"Shipped"` ho aur uske **Cancel button ki ginti 0** ho.

🎤 **Interview line:** *"For tables I model a row component and find rows by a business key like order id using an exact cell match, never by index or loose text, and I assert with count and text expects so they retry."*

🛟 Atak gaye? `solutions/step_08`

---

# 🟡 Step 9: POM + pytest fixtures

⚡ **TL;DR:** Common **starting state** (login page khuli, logged-in inventory) ko **fixtures** me. Fixture **Page Object lautata hai**, test me `LoginPage(page)` likhna nahi padta.

## 🤕 Dikkat
Har test me pehle `LoginPage(page).open().login_as(...)` repeat hai.

## ⌨️ Karo

**File: `tests/conftest.py`**
```python
import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.playground_page import PlaygroundPage

# Demo credentials. Asli project me password environment variable se lo.
STANDARD_USER = ("standard_user", "secret_sauce")


@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page).open()


@pytest.fixture
def inventory_page(login_page) -> InventoryPage:
    username, password = STANDARD_USER
    return login_page.login_as(username, password)


@pytest.fixture
def playground(page) -> PlaygroundPage:
    return PlaygroundPage(page).open()
```

`tests/test_shop.py` replace (ab fixtures se):

**File: `tests/test_shop.py`**
```python
from playwright.sync_api import expect


def test_login_works(inventory_page):
    expect(inventory_page.cart_badge).to_have_text("0")


def test_wrong_password_shows_error(login_page):
    login_page.attempt_login("standard_user", "wrong-password")
    expect(login_page.error).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(inventory_page):
    inventory_page.product("Backpack").add_to_cart()
    expect(inventory_page.cart_badge).to_have_text("1")


def test_product_card_shows_price_and_toggles_button(inventory_page):
    backpack = inventory_page.product("Backpack")
    expect(backpack.price).to_have_text("$29.99")
    expect(backpack.action_button).to_have_text("Add to cart")
    backpack.add_to_cart()
    expect(backpack.action_button).to_have_text("Remove")


def test_products_are_listed_alphabetically(inventory_page):
    expect(inventory_page.names).to_have_text(["Backpack", "Bike Light", "Onesie"])


def test_user_can_buy_backpack(inventory_page):
    inventory_page.product("Backpack").add_to_cart()
    done = inventory_page.open_cart().checkout()
    expect(done.heading).to_be_visible()
```

`tests/test_orders.py` replace:

**File: `tests/test_orders.py`**
```python
from playwright.sync_api import expect


def test_orders_table_shows_four_orders(playground):
    expect(playground.orders.rows).to_have_count(4)


def test_pending_order_can_be_cancelled(playground):
    row = playground.orders.row_for("1002")

    expect(row.status).to_have_text("Pending")
    row.cancel()

    expect(row.status).to_have_text("Cancelled")
    expect(row.cancel_button).to_have_count(0)


def test_order_details_modal_opens_and_closes(playground):
    modal = playground.orders.row_for("1001").open_details()
    expect(modal.title).to_have_text("Order #1001")

    modal.close()
    expect(modal.root).to_be_hidden()
```

## ▶️ Chalao
`pytest` → **`9 passed`**

## 🔍 Code samjho
| Line | Matlab |
|---|---|
| `tests/conftest.py` | Is naam ki file ke fixtures `tests/` ke tests ko **bina import** mil jaate hain |
| `def login_page(page)` | `page` pytest-playwright ka fixture. Ye **LoginPage object lautata hai** (khuli hui) |
| `def inventory_page(login_page)` | Fixture doosre fixture ko **naam se** maangta hai (chain) |
| `return login_page.login_as(username, password)` | Logged-in inventory page |
| `def playground(page)` | Playground page khuli hui |
| `STANDARD_USER = (...)` | Demo credentials. **Asli project me env variable** (password code me nahi) |
| `def test_login_works(inventory_page)` | Test sirf **apna kaam** likhta hai |

## 🧠 Kyun? Aur alternatives?
| Option | Dikkat / faida |
|---|---|
| Har test me page object khud banana | Chhote suite me theek. Repeat badhta hai |
| **Fixtures page objects lautayein** ✅ | Taiyari ek jagah, test chhota |
| Ek bada `app` fixture (Facade, Step 13) | Imports kam, par god-object ka khatra |
| **Module-level global page object** (`login_page = LoginPage(...)` file ke upar) | ❌ **Parallel/independent tests ke liye khatarnak**: sab tests ek hi state share karte hain |
| `scope="session"` page object | ❌ `page` har test ka naya hai; session scope me purana page chipak jaata hai |

**Rule:** page object **per test**, fixture scope **function** (default). Page Object me **koi class-level ya module-level mutable state nahi**.

**Fixture me kya nahi:** business assertions. (Sirf readiness wait ok.)

## ✅ Samjha?
<details>
<summary>1. Login ke tests me <code>inventory_page</code> fixture kyun nahi?</summary>

Wo login hi test kar rahe hain. Agar fixture pehle login kar de to test kuch test nahi karta. Isliye `login_page` fixture (khuli page) lete hain.
</details>
<details>
<summary>2. Page object fixture ko <code>session</code> scope karne se kya hoga?</summary>

Purana `page` (pehle test ka) chipak jaayega aur tests ek doosre ki state dekhenge. `page` function-scoped hai, to uska page object bhi.
</details>

🎤 **Interview line:** *"I expose starting states as function-scoped fixtures that return page objects, so tests stay short and independent, and page objects never hold shared module-level state."*

🛟 Atak gaye? `solutions/step_09`

---

# 🔴 Step 10: iframe aur Shadow DOM

⚡ **TL;DR:** iframe ke liye `frame_locator`. Open shadow DOM me Playwright locators **seedha ghus jaate hain**. Dono ko **component** banao, taaki test ko pata na ho ki wo iframe/shadow me hai.

## 🤕 Dikkat
Payment form ek **iframe** me hai. Rating widget **shadow DOM** me. Normal locator se mile nahi?

## ⌨️ Karo

**File: `components/payment_frame.py`**
```python
from playwright.sync_api import Locator, Page


class PaymentFrame:
    """Page ke andar ek iframe ka form."""

    def __init__(self, page: Page):
        frame = page.frame_locator("iframe[title='Payment']")
        self._card_number = frame.get_by_label("Card number")
        self._pay_button = frame.get_by_role("button", name="Pay now")
        self.message: Locator = frame.locator("#msg")

    def pay(self, card_number: str):
        self._card_number.fill(card_number)
        self._pay_button.click()
```

**File: `components/rating_widget.py`**
```python
from playwright.sync_api import Locator, Page


class RatingWidget:
    """Custom element <rating-widget> (open shadow DOM ke andar)."""

    def __init__(self, page: Page):
        self._root = page.locator("rating-widget")
        self.value: Locator = self._root.get_by_text("Rating:")

    def rate(self, stars: int):
        self._root.get_by_role("button", name=f"Rate {stars}").click()
```

`pages/playground_page.py` (diff):

**File: `pages/playground_page.py`** (sirf ye badlaav: `-` hatao, `+` jodo)
```diff
 from components.orders_table import OrdersTable
+from components.payment_frame import PaymentFrame
+from components.rating_widget import RatingWidget
 from core.base_page import BasePage
  ...
         self.orders = OrdersTable(page)
+        self.payment = PaymentFrame(page)
+        self.rating = RatingWidget(page)
 
```

**File: `tests/test_playground_widgets.py`**
```python
from playwright.sync_api import expect


def test_payment_form_inside_iframe(playground):
    playground.payment.pay("4242424242424242")
    expect(playground.payment.message).to_have_text("Payment accepted")


def test_rating_widget_inside_shadow_dom(playground):
    playground.rating.rate(4)
    expect(playground.rating.value).to_have_text("Rating: 4")
```

## ▶️ Chalao
`pytest` → **`11 passed`**

## 🔍 Code samjho
| Line | Matlab |
|---|---|
| `page.frame_locator("iframe[title='Payment']")` | iframe ke andar ka locator-scope. **Lazy aur auto-wait** (iframe load hone tak) |
| `frame.get_by_label("Card number")` | iframe ke **andar** ka field |
| `page.locator("rating-widget")` | Custom element (shadow root wala) |
| `self._root.get_by_role("button", name=f"Rate {stars}")` | **Shadow DOM ke andar** ka button, bina kuch khaas kiye (Playwright open shadow root me ghus jaata hai) |
| `PaymentFrame.pay(card)` | Test ko iframe ka pata hi nahi: sirf "pay karo" |

## 🧠 Kyun? Aur alternatives?
| Option | Dikkat / faida |
|---|---|
| `page.frame(name=...)` / `page.frames` (frame object lena) | Frame ke load hone ka khud khayal rakhna padta hai ❌ |
| **`frame_locator`** ✅ | Locator ki tarah lazy aur auto-wait |
| Shadow DOM ke liye JavaScript (`evaluate`) | Zaroorat nahi, locators already pierce karte hain ❌ |
| Page me raw `frame_locator` bikhra | Component me chhupao: iframe badla to ek file |

> Playwright **open** shadow DOM me ghus jaata hai. **Closed** shadow root ke andar locators nahi pahunch sakte (developer se open karwao ya test hook maango). *(Ye Playwright ke documented behaviour ke mutabiq hai; maine closed shadow root chalake nahi dekha.)*

## ✅ Samjha?
<details>
<summary>1. Test me <code>frame_locator</code> kyun nahi likha?</summary>

Test ko implementation ka pata nahi hona chahiye. Kal iframe hata kar normal form aaya to sirf `PaymentFrame` badlega.
</details>
<details>
<summary>2. Shadow DOM ke button ke liye alag code kyun nahi likha?</summary>

Playwright ke locators open shadow root ke andar seedha dhundh lete hain.
</details>

## ✍️ Khud karo
`RatingWidget` me ek test likho jo 2 star select kare aur `"Rating: 2"` check kare.

🎤 **Interview line:** *"I wrap iframes and shadow DOM widgets in components using frame_locator and normal locators, so the test never knows about those details."*

🛟 Atak gaye? `solutions/step_10`

---

# 🔴 Step 11: Naya tab (popup) aur browser dialog

⚡ **TL;DR:** Naya tab → `expect_popup`, aur **naye tab ka page object lautao**. Dialog (`confirm`) → handler **click se pehle** lagao.

## ⌨️ Karo

**File: `pages/help_page.py`**
```python
from playwright.sync_api import Locator, Page

from core.base_page import BasePage


class HelpPage(BasePage):
    path = "/help.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self._heading = page.get_by_role("heading", name="Help Center")

    @property
    def loaded_locator(self) -> Locator:
        return self._heading
```

`pages/playground_page.py` (diff):

**File: `pages/playground_page.py`** (sirf ye badlaav: `-` hatao, `+` jodo)
```diff
 from core.base_page import BasePage
+from pages.help_page import HelpPage
 
  ...
         self._heading = page.get_by_role("heading", name="Playground")
+        self._open_help_button = page.get_by_role("button", name="Open help (new tab)")
+        self._delete_account_button = page.get_by_role("button", name="Delete account")
+        self.account_status: Locator = page.get_by_test_id("account-status")
         self.orders = OrdersTable(page)
  ...
         return self._heading
+
+    def open_help(self) -> HelpPage:
+        """Naya tab khulta hai. Us naye tab ka page object lautao."""
+        with self.page.expect_popup() as popup_info:
+            self._open_help_button.click()
+        return HelpPage(popup_info.value).wait_until_loaded()
+
+    def delete_account(self, confirm: bool = True):
+        """Browser ka confirm() dialog aata hai. Dialog ko accept ya dismiss karo."""
+        self.page.once("dialog", lambda dialog: dialog.accept() if confirm else dialog.dismiss())
+        self._delete_account_button.click()
```

**File: `tests/test_playground_widgets.py`**
```python
from playwright.sync_api import expect


def test_payment_form_inside_iframe(playground):
    playground.payment.pay("4242424242424242")
    expect(playground.payment.message).to_have_text("Payment accepted")


def test_rating_widget_inside_shadow_dom(playground):
    playground.rating.rate(4)
    expect(playground.rating.value).to_have_text("Rating: 4")


def test_help_opens_in_new_tab(playground):
    help_page = playground.open_help()
    expect(help_page.loaded_locator).to_be_visible()
    assert help_page.page is not playground.page      # alag tab


def test_delete_account_confirmed(playground):
    playground.delete_account(confirm=True)
    expect(playground.account_status).to_have_text("Account deleted")


def test_delete_account_cancelled(playground):
    playground.delete_account(confirm=False)
    expect(playground.account_status).to_have_text("")
```

## ▶️ Chalao
`pytest` → **`14 passed`**

## 🔍 Code samjho
| Line | Matlab |
|---|---|
| `with self.page.expect_popup() as popup_info:` | "Is block me naya tab khulega, uska intezaar karo" |
| `self._open_help_button.click()` | Click **with ke andar**, taaki popup miss na ho |
| `HelpPage(popup_info.value)` | Naye tab ka `page` ek **naya Page Object** deta hai (alag `page`!) |
| `assert help_page.page is not playground.page` | Alag tab hai (test me ye plain check theek hai) |
| `self.page.once("dialog", lambda dialog: ...)` | **Ek baar** ke liye dialog handler |
| `dialog.accept() if confirm else dialog.dismiss()` | OK ya Cancel |
| `delete_account(confirm=True)` | Parameter se **dono outcome** test ho sakte hain |

## 🔬 Handler pehle kyun? (real)
Agar dialog ka handler **na** lagao aur click karo, to Playwright dialog ko **chup-chap dismiss** kar deta hai. Maine dekha: status `''` raha (account delete nahi hua). Isliye handler **click se pehle**.

## 🧠 Kyun? Aur alternatives?
| Option | Dikkat / faida |
|---|---|
| `time.sleep` ke baad `context.pages[-1]` | Race, galat tab ❌ |
| **`expect_popup`** ✅ | Popup aate hi mil jaata hai |
| Naye tab ko wahi page object se control | Naye tab ka alag `page` hai, alag page object chahiye |
| Dialog handler test me bikhra | Page object method me: `delete_account(confirm=...)` |

## ✅ Samjha?
<details>
<summary>1. Popup ka <code>page</code> alag kyun hai?</summary>

Naya tab = naya `page` object. Isliye `HelpPage` ko `popup_info.value` do, `self.page` nahi.
</details>
<details>
<summary>2. <code>page.once("dialog", ...)</code> click ke baad likhte to?</summary>

Dialog tab tak dismiss ho chuka hota. Handler **pehle** lagana zaroori.
</details>

🎤 **Interview line:** *"For new tabs I wrap the click in expect_popup and return a page object bound to the popup page, and for dialogs I register the handler before the click inside a method like delete_account(confirm)."*

🛟 Atak gaye? `solutions/step_11`

---

# 🔴 Step 12: Anti-patterns aur rules ko test se enforce karo

⚡ **TL;DR:** POM ke 10 aam bigaad. Aur 4 rules jo **test se** pakde ja sakte hain.

## 🟥 Anti-pattern gallery (click karke dekho)

<details>
<summary><b>1. God Page (ek class me poori app)</b></summary>

`AppPage` me login, cart, orders, payment sab, 800 lines. **Fix:** ek screen = ek class, repeat hissa = component.
</details>

<details>
<summary><b>2. Generic wrappers: <code>click(selector)</code>, <code>fill(selector, text)</code></b></summary>

```diff
- def click(self, selector): self.page.click(selector)      # BasePage me
- self.click("#login-btn")
+ self._login_button.click()                                 # Locator seedha
```
**Dikkat:** string selectors wapas aa gaye, Playwright ka achha API chhup gaya, ek faltu layer. **Fix:** Locator objects.
</details>

<details>
<summary><b>3. Page me <code>assert</code></b></summary>

Step 4. Race, ek expectation me fas gaya. **Fix:** test me `expect`.
</details>

<details>
<summary><b>4. Sleeps</b></summary>

`time.sleep(2)`. **Fix:** `expect` / readiness.
</details>

<details>
<summary><b>5. Test me raw locators</b></summary>

```diff
- page.get_by_role("button", name="Login").click()     # test me
+ login.attempt_login(user, pwd)                         # page object se
```
</details>

<details>
<summary><b>6. Global / shared state</b></summary>

Module ke upar `login_page = LoginPage(some_page)`. **Parallel me tests ek doosre ko todte hain.** **Fix:** per-test fixture.
</details>

<details>
<summary><b>7. Page Object me test data / credentials</b></summary>

`LoginPage.login_as_admin()` jisme password hard-coded. **Fix:** data alag, page object ko argument do.
</details>

<details>
<summary><b>8. Page Object me HTTP / API calls</b></summary>

Page ka kaam UI. **Fix:** API ke liye alag layer (pichhli architecture guide).
</details>

<details>
<summary><b>9. Locator ki jagah text return karna</b></summary>

`def get_error(self) -> str` → test `assert login.get_error() == ...`. Race (Step 4). **Fix:** `Locator` return/expose.
</details>

<details>
<summary><b>10. Har chhoti cheez ke liye Page Object</b></summary>

Ek button ke liye class. **Fix:** component tab jab repeat/bada ho (YAGNI).
</details>

## ⌨️ Karo: rules ko test bana do

**File: `tests/test_page_object_rules.py`**
```python
import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PO_FOLDERS = ["pages", "components", "core"]


def _po_files():
    for folder in PO_FOLDERS:
        yield from (ROOT / folder).glob("*.py")


def test_page_objects_have_no_assert_statements():
    offenders = []
    for path in _po_files():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Assert):
                offenders.append(f"{path.name}:{node.lineno}")
    assert not offenders, f"Page Object me assert mat likho (test me likho): {offenders}"


def test_page_objects_have_no_fixed_sleeps():
    offenders = [
        path.name for path in _po_files()
        if "time.sleep" in path.read_text(encoding="utf-8")
        or "wait_for_timeout" in path.read_text(encoding="utf-8")
    ]
    assert not offenders, f"Sleep mat use karo, expect/auto-wait use karo: {offenders}"


def test_page_objects_do_not_import_requests():
    offenders = [
        path.name for path in _po_files()
        if re.search(r"^\s*(import|from)\s+requests", path.read_text(encoding="utf-8"), re.M)
    ]
    assert not offenders, f"Page Object HTTP nahi karta: {offenders}"


def test_tests_do_not_use_raw_locators():
    pattern = re.compile(r"\.(locator|get_by_\w+)\(")
    offenders = []
    for path in (ROOT / "tests").glob("test_*.py"):
        if path.name == "test_page_object_rules.py":
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if pattern.search(line):
                offenders.append(f"{path.name}:{number}: {line.strip()}")
    assert not offenders, "Tests me raw locator mila:\n" + "\n".join(offenders)
```

## ▶️ Chalao
`pytest` → **`18 passed`** (4 naye rules tests)

## 🔬 Violation daal ke dekho (real)
| Maine kya kiya | Test ka message |
|---|---|
| `cart_page.py` me `assert True` | `Page Object me assert mat likho (test me likho): ['cart_page.py:19']` |
| `product_card.py` me `time.sleep` | `Sleep mat use karo, expect/auto-wait use karo: ['product_card.py']` |
| `login_page.py` me `import requests` | `Page Object HTTP nahi karta: ['login_page.py']` |
| `tests/test_shop.py` me raw `get_by_role` | `Tests me raw locator mila: test_shop.py:37: page.get_by_role("button", name="Login").click()` |

Chaaron me test **red** hua, galti hatane par green.

## 🔍 Code samjho
| Line | Matlab |
|---|---|
| `ast.parse(...)` + `ast.walk(tree)` | Python file ko **chalaye bina** padhna (syntax tree) |
| `isinstance(node, ast.Assert)` | Har `assert` statement dhundho |
| `"time.sleep" in text` | Seedha text check (sleeps ke liye kaafi) |
| `re.compile(r"\.(locator\|get_by_\w+)\(")` | `.locator(` ya `.get_by_xxx(` pattern |
| `PO_FOLDERS = ["pages", "components", "core"]` | Page Object wale folders |

## 🧠 Kyun?
| Option | Dikkat |
|---|---|
| Rule README me | Koi padhta nahi ❌ |
| Code review par bharosa | Insaan thak jaata hai ❌ |
| **Rule ek test** ✅ | Apne aap, har run, red = turant pata |

🎤 **Interview line:** *"I enforce page object rules with tests: no asserts, no sleeps, no HTTP in pages, and no raw locators in tests, so the structure can't quietly rot."*

🛟 Atak gaye? `solutions/step_12`

---

# 🔴 Step 13: Alternatives (POM ke alawa kya hai?)

⚡ **TL;DR:** POM sabse common hai, par **hamesha sabse behtar nahi**. Jaano baaki kya hain aur kab kaunsa.

## Tulna (ek table me)

| Pattern | Idea | Kab achha | Dikkat |
|---|---|---|---|
| **POM** ✅ | Page = class (locators + actions) | Zyadatar UI suites, team me | Bade page me phool sakta hai |
| **Functional helpers** | Plain functions `login(page, ...)` | Bahut chhota suite, quick scripts | Grouping nahi, state nahi |
| **App facade** | Ek `app` object jisse saare pages milte hain | Kam imports, discoverable | God-object ban sakta hai |
| **Screenplay** | Actor + Tasks + Questions | Bade teams, BDD, business-language | Zyada code, seekhna bhari |
| **App actions / API-first** | Setup API se, UI sirf jaha zaroori | Speed + stability (zaroor mix karo) | UI model nahi deta |
| **Selenium PageFactory (Java)** | `@FindBy` se locators auto-init | Selenium (Java) me | Playwright me **zaroorat nahi**: locators pehle se lazy |
| **Record and playback** | Codegen se script | Demo/quick check | Maintainable nahi |

## 🔬 Code: teen alternatives (real chalaye)

**1) Functional helpers:**

**File: `alternatives/functional_helpers.py`**
```python
from playwright.sync_api import Locator, Page, expect


def login(page: Page, username: str, password: str) -> None:
    page.goto("/")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="Products")).to_be_visible()


def add_to_cart(page: Page, product_name: str) -> None:
    card = page.get_by_test_id("product").filter(has_text=product_name)
    card.get_by_role("button", name="Add to cart").click()


def cart_badge(page: Page) -> Locator:
    return page.get_by_test_id("cart-count")
```

**2) Screenplay-lite:**

**File: `alternatives/screenplay.py`**
```python
from playwright.sync_api import Locator, Page


class Actor:
    """Screenplay-lite: Actor TASKS karta hai aur QUESTIONS puchta hai."""

    def __init__(self, name: str, page: Page):
        self.name = name
        self.page = page

    def attempts_to(self, *tasks) -> None:
        for task in tasks:
            task.perform_as(self)

    def sees(self, question) -> Locator:
        return question.answered_by(self)


class Login:
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password

    def perform_as(self, actor: Actor) -> None:
        page = actor.page
        page.goto("/")
        page.get_by_placeholder("Username").fill(self._username)
        page.get_by_placeholder("Password").fill(self._password)
        page.get_by_role("button", name="Login").click()


class AddToCart:
    def __init__(self, product_name: str):
        self._product_name = product_name

    def perform_as(self, actor: Actor) -> None:
        card = actor.page.get_by_test_id("product").filter(has_text=self._product_name)
        card.get_by_role("button", name="Add to cart").click()


class CartBadge:
    def answered_by(self, actor: Actor) -> Locator:
        return actor.page.get_by_test_id("cart-count")
```

**3) App facade:**

**File: `alternatives/app.py`**
```python
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class ShopApp:
    """Facade: ek object se saare pages. Pages wahi, bas milne ka tareeka alag."""

    def __init__(self, page: Page):
        self._page = page

    @property
    def login(self) -> LoginPage:
        return LoginPage(self._page)

    @property
    def inventory(self) -> InventoryPage:
        return InventoryPage(self._page)

    @property
    def cart(self) -> CartPage:
        return CartPage(self._page)
```

**Teeno ke tests:**

**File: `tests/test_alternatives.py`**
```python
import pytest
from playwright.sync_api import expect

from alternatives.app import ShopApp
from alternatives.functional_helpers import add_to_cart, cart_badge, login
from alternatives.screenplay import Actor, AddToCart, CartBadge, Login


def test_alt_plain_functions(page):
    login(page, "standard_user", "secret_sauce")
    add_to_cart(page, "Backpack")
    expect(cart_badge(page)).to_have_text("1")


def test_alt_screenplay_lite(page):
    asha = Actor("Asha", page)
    asha.attempts_to(Login("standard_user", "secret_sauce"), AddToCart("Backpack"))
    expect(asha.sees(CartBadge())).to_have_text("1")


@pytest.fixture
def app(page) -> ShopApp:
    return ShopApp(page)


def test_alt_app_facade(app):
    inventory = app.login.open().login_as("standard_user", "secret_sauce")
    inventory.product("Backpack").add_to_cart()
    expect(inventory.cart_badge).to_have_text("1")
```

`pytest` → **`21 passed`**

## 🧠 Humne POM kyun chuna?
| Sawaal | Jawab |
|---|---|
| Functional helpers? | Suite badhne par ye bikhre modules ban jaate hain, composition (component) mushkil |
| Screenplay? | Zyada boilerplate. Chhoti team ke liye mehnga. Idea accha hai (tasks/questions), par pehle POM pakka karo |
| App facade? | **POM ke upar** laga sakte ho (Step 9 ka variation). Alternative nahi, organize karne ka tareeka |
| PageFactory? | Playwright me locators already lazy, zaroorat nahi |

> [!IMPORTANT]
> **Interview me ye mat bolo "POM hi sahi hai".** Bolo: *"POM mera default hai kyunki ..., par chhote suite me functional helpers ya API-first setup bhi sahi ho sakte hain."* Ye **senior soch** dikhata hai.

## ✅ Samjha?
<details>
<summary>1. App facade POM ka alternative hai ya uske upar ki parat?</summary>

Upar ki parat. Pages wahi (POM), bas unhe ek `app` object se access karte hain.
</details>
<details>
<summary>2. Playwright me PageFactory kyun nahi chahiye?</summary>

Locators already lazy hain (Step 3), to "element ko pehle se init karna" jaisa kuch nahi karna.
</details>

🎤 **Interview line:** *"POM is my default for UI suites; for tiny suites plain helpers are fine, and I combine it with API-first setup so UI tests only exercise what the UI owns."*

🛟 Atak gaye? `solutions/step_13`

---

# 🔴 Step 14: Production me confidence

⚡ **TL;DR:** Code likhna ek cheez, team me **saalon tak chalana** doosri. Ye step checklists ka hai.

## 1) Folder aur naam (convention)
```text
core/          BasePage (chhota)
components/    repeat/shared hisse (ProductCard, OrdersTable, Header)
pages/         ek screen = ek class (LoginPage, InventoryPage)
tests/         sirf scenarios + conftest.py (fixtures)
```
| Convention | Kyun |
|---|---|
| Class naam `XxxPage` / noun (`ProductCard`) | Pehchaan aasan |
| Methods **verbs** (`login_as`, `cancel`) | Business action |
| Public Locators **nouns** (`error`, `cart_badge`) | `expect(page.error)` padhne me saaf |
| Private `_x` | Detail chhupi |
| **Absolute imports** (`from pages.login_page import ...`) | Grep karne layak, move karna aasan |

## 2) Developers ke saath locator contract
- `data-testid` **stable** rakhein (design change se na badle).
- Role/label/accessibility sahi ho (isse tests **aur** accessibility dono).
- Text-based locators (i18n, A/B copy) toot-te hain: multi-language app me `test_id`/role.

## 3) Parallel aur isolation
- Page object **per test**, fixtures **function scope**.
- Class-level / module-level **mutable state nahi**.
- Har test ka apna data (pichhli guide: per-test token).

## 4) Debuggability
- Failure par screenshot/trace/logs (pichhli Allure guide).
- Page Object methods ke **steps** (Allure me), par **password argument wale decorators nahi** (leak).
- Methods ke naam business jaise, taaki report padhne layak.

## 5) Pull request review checklist (copy karke use karo)
- [ ] Naya test me **raw locator nahi**.
- [ ] Page Object me **assert / sleep / HTTP nahi**.
- [ ] Naya method **business naam** ka hai.
- [ ] Locator **user-facing** pehle (role/label/test-id).
- [ ] Navigation method **agla page lautata** hai.
- [ ] Do outcome wale kaam ke **alag methods** hain.
- [ ] Component sirf tab jab repeat/bada.
- [ ] BasePage me **naya method nahi** (ya kaaran likha hai).
- [ ] Test **independent** (apna data/state).
- [ ] Rules tests green.

## 6) Page Object bada ho gaya? (200+ lines)
1. Repeat hissa pehchano (list item, form section).
2. **Component** me nikaalo.
3. Page me composition (`self.orders = OrdersTable(page)`).
4. Tests green rakho har step me.

## 7) Purani messy suite ko POM me kaise laayein (safe plan)
1. Pehle tests **green** karo.
2. Ek **page** (login) ka Page Object banao, sirf us page ke tests badlo.
3. Har step ke baad `pytest`.
4. Phir agla page. **Ek saath sab nahi.**
5. Repeat dikhe to base/component.
6. Rules tests lagao.
7. Purane raw-locator tests tab tak chalte rahein jab tak naye ban na jayein.

## 8) Health ke sawaal (kya POM achha chal raha hai?)
| Sawaal | Achha jawab |
|---|---|
| Ek locator badla to kitni files badli? | **1** |
| Naya test likhna kitna mushkil? | Pehle se bane pieces jodna |
| Naya banda 30 min me samajh jaaye? | Haan (folder naam + rules test) |
| Flaky kyun ho rahe hain? | Sleeps nahi, expect, independence |

> [!NOTE]
> **Honest limit:** ye checklists general industry practice par based hain. Maine inhe kisi real team project par nahi chalaya. Tumhari company ke apne conventions ho sakte hain; wahan ka rule pehle.

🎤 **Interview line:** *"In production I rely on stable test ids agreed with developers, function-scoped page objects for parallel safety, and automated rules so the structure stays consistent as the team grows."*

---

# 🎤 Step 15: Interview crack

## A) POM ko 60 second me kaise samjhao (yaad karne layak)

> *"Page Object Model is a design pattern where each page, or reusable part of a page, has a class. The class owns the locators and the actions, and tests only call business-level methods. That means when the UI changes I fix one place instead of every test. In my framework pages extend a small base class, repeated UI like list items are components built from a root locator, navigation methods return the next page, and assertions stay in tests using Playwright's auto-retrying expect. I enforce those rules with tests, and I combine POM with API-based setup so UI tests stay fast and independent."*

## B) Sawaal (click karke jawab dekho; **pehle khud bolo**)

> [!IMPORTANT]
> Jahan jawab me **"in my experiment"** jaisa likha hai, wo **tabhi bolo jab tumne khud wo experiment chalaya ho** (Step 4, 5, 8 ke `experiments/` ya steps). Nahi chalaya to bolo: *"I read that ..."* ya wo example mat do. Interview me jhooth pakda jaata hai.

### 🟢 Basic

<details>
<summary><b>Q1. What is POM and why use it?</b></summary>

- *Simple:* A class per page holding locators and actions, so tests don't repeat UI details.
- *Strong:* "POM separates what a test verifies from how the UI is driven. Locators and interactions live in page classes, so a UI change is fixed once and tests read like business steps."
- *Keywords:* design pattern, maintainability, reuse, readability.
</details>

<details>
<summary><b>Q2. Benefits and drawbacks?</b></summary>

- *Strong:* "Benefits: one place per UI change, readable tests, reuse. Drawbacks: extra classes, risk of god pages and base classes, and the abstraction can hide Playwright's features if over-wrapped. I keep pages thin and use components."
- *Keywords:* god class, over-abstraction, YAGNI.
</details>

<details>
<summary><b>Q3. Where do locators live, and should they be public?</b></summary>

- *Strong:* "Inside the page object, as Locator objects. Private by default; I expose only those a test must assert on, so tests call methods instead of clicking raw elements."
- *Keywords:* Locator, lazy, private vs public.
</details>

<details>
<summary><b>Q4. Should page objects contain assertions?</b></summary>

- *Strong:* "I keep business assertions in tests. Pages expose Locators so tests use `expect` which retries. A page may have a readiness wait like `wait_until_loaded`. In an experiment with a slow login response, a one-shot `inner_text()` assertion failed while `expect` passed."
- *Keywords:* auto-retry, readiness vs business assertion.
</details>

<details>
<summary><b>Q5. What should a page method return?</b></summary>

- *Strong:* "A navigation method returns the next page object. A same-page action returns nothing. If an action can lead to two outcomes, I make two methods, like `login_as` for success and `attempt_login` for negative tests."
- *Keywords:* navigation, return type clarity.
</details>

<details>
<summary><b>Q6. What goes in a BasePage?</b></summary>

- *Strong:* "Only what every page needs: path, open and a readiness wait via an abstract `loaded_locator`. Not business actions, not click/fill wrappers, otherwise it becomes a god class."
- *Keywords:* template method, small base.
</details>

<details>
<summary><b>Q7. POM vs Selenium's PageFactory?</b></summary>

- *Strong:* "PageFactory is a Selenium (Java) mechanism to initialise annotated elements; POM is the pattern. In Playwright locators are already lazy, so I don't need a factory. I haven't used PageFactory myself."
- *Keywords:* lazy locators, pattern vs mechanism.
- ⚠️ Sirf wahi bolo jo sach ho (tumne use nahi kiya to "use nahi kiya" bolo).
</details>

### 🟡 Intermediate

<details>
<summary><b>Q8. How do you model lists and tables?</b></summary>

- *Strong:* "A component built from a root Locator, like `ProductCard` or `OrderRow`. I find a row by a business key with an exact cell match, not by index or loose text, because `has_text="100"` matched all four of my rows."
- *Keywords:* root locator scoping, exact match, not nth.
</details>

<details>
<summary><b>Q9. Component vs Page?</b></summary>

- *Strong:* "A page is a screen. A component is a reusable or repeated part like a header, a card or a table row. I create components when something repeats, appears on several pages, or a page gets too big."
- *Keywords:* composition, reuse.
</details>

<details>
<summary><b>Q10. How do you use POM with pytest fixtures?</b></summary>

- *Strong:* "Function-scoped fixtures return page objects for common starting states, such as a logged-in inventory page. The page object stays free of shared state, so tests are independent and parallel-safe."
- *Keywords:* function scope, conftest, isolation.
</details>

<details>
<summary><b>Q11. How do you handle waits in POM?</b></summary>

- *Strong:* "No sleeps. Playwright auto-waits for actions; for page readiness I use `expect(loaded_locator).to_be_visible()`; for async data I assert with `expect`, which retries."
- *Keywords:* auto-wait, expect, no `wait_for_timeout`.
</details>

<details>
<summary><b>Q12. Dynamic elements?</b></summary>

- *Strong:* "Locators are lazy queries, so re-rendered DOM is fine. I scope to a stable parent and filter by business data. After cancelling an order the table re-rendered and the same row locator still worked."
- *Keywords:* lazy locator, filter, stable key.
</details>

<details>
<summary><b>Q13. How do you avoid logging in through the UI in every test?</b></summary>

- *Strong:* "A fixture gets a token through the API and injects it into the browser before the page loads. UI login is tested only in login tests. Each test gets its own token for isolation."
- *Keywords:* API-first setup, token, hybrid.
</details>

<details>
<summary><b>Q14. How do you structure a large suite?</b></summary>

- *Strong:* "`core` for a tiny base, `components` for reusable parts, `pages` for screens, `tests` for scenarios and fixtures, plus config and data layers. Absolute imports, verb methods, and rule tests to keep it consistent."
- *Keywords:* layers, conventions.
</details>

### 🔴 Advanced

<details>
<summary><b>Q15. Inheritance vs composition in POM?</b></summary>

- *Strong:* "Inheritance only for a tiny shared template (open and readiness). Reuse comes from composition: pages hold components. Deep inheritance trees make one base-class change ripple across everything."
- *Keywords:* has-a vs is-a, god base.
</details>

<details>
<summary><b>Q16. iframes, shadow DOM, popups, dialogs?</b></summary>

- *Strong:* "I wrap them in components or page methods. `frame_locator` for iframes, normal locators pierce open shadow roots, `expect_popup` returns a page object bound to the new tab, and dialog handlers are registered before the click because unhandled dialogs are auto-dismissed."
- *Keywords:* encapsulation, expect_popup, handler before click.
</details>

<details>
<summary><b>Q17. When would you not use POM? Alternatives?</b></summary>

- *Strong:* "For tiny suites plain helper functions are enough; Screenplay suits large teams that want business-language tasks; API-first setup removes UI from setup altogether. I use POM as the default and mix API setup."
- *Keywords:* helpers, Screenplay, app actions, trade-offs.
</details>

<details>
<summary><b>Q18. How do you keep the framework from rotting?</b></summary>

- *Strong:* "Automated rules tests: no asserts, sleeps or HTTP in page objects, no raw locators in tests; plus a PR checklist. A violation turns the build red."
- *Keywords:* fitness tests, `ast`, CI gate.
</details>

<details>
<summary><b>Q19. Parallel safety?</b></summary>

- *Strong:* "Page objects are created per test, hold no module-level state, fixtures are function-scoped, and each test owns its data. Shared tokens made an order-dependent test fail in my experiment."
- *Keywords:* isolation, no shared state.
</details>

<details>
<summary><b>Q20. How would you migrate a legacy suite to POM?</b></summary>

- *Strong:* "Make tests green first. Introduce one page object at a time, converting only that page's tests, run after every step, then extract a base and components when repetition appears, and add rules tests last."
- *Keywords:* incremental, green at each step, strangler approach.
</details>

## C) Coding sawaal (interview me live likhne ke liye)

| Sawaal | Kya likhna hai | Tumhare paas jawab |
|---|---|---|
| "Login page ka POM likho" | class, private locators, `open`, `login`, public `error` | **Step 3** |
| "Dynamic rows wali table ka POM" | `OrderRow` + `OrdersTable.row_for(id)` | **Step 8** |
| "Ek button naya tab kholta hai" | `expect_popup`, return naye tab ka page object | **Step 11** |
| "iframe ke andar form" | `frame_locator`, component | **Step 10** |

## D) Interview me ye galtiyan mat karo

- ❌ "POM hi sabse sahi hai": **trade-offs** batao.
- ❌ Page me `assert` ko theek bolna bina reason: Step 4 ka experiment batao.
- ❌ Jo use nahi kiya (PageFactory, Screenplay) usse "use kiya hai" bolna.
- ❌ "Maine framework banaya" jab sirf copy kiya: **kya khud seekha** batao (Step ke experiments).
- ✅ **Real example do:** "mere experiment me `has_text='100'` ne 4 rows di".

## E) Confidence checklist

- [ ] Mai POM 60 second me explain kar sakta hu.
- [ ] Mai batata hu assertion test me kyun.
- [ ] Mai `login_as` aur `attempt_login` ka fark bata sakta hu.
- [ ] Mai BasePage me kya nahi jaata bata sakta hu.
- [ ] Mai component kab banate hain bata sakta hu.
- [ ] Mai table row kaise dhundhte hain (aur nth kyun nahi) bata sakta hu.
- [ ] Mai iframe/shadow/popup/dialog handle kar sakta hu.
- [ ] Mai 3 alternatives aur unke trade-offs bata sakta hu.
- [ ] Mai PR checklist se kisi ka POM review kar sakta hu.

> 🎯 Agla kadam: **Step 2 se Step 9 apne `ex_6` par lagao** (ek-ek, har step ke baad `pytest`), phir code bhejo. Strict review milega.
