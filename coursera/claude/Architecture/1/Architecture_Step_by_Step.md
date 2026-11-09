# 🪜 Architecture: Step by Step (Beginner Path)

> Pehle ek baat: pichhli guide tumhare liye **bahut badi aur ek saath** thi. Wo meri galti thi. Tumne "kaise sikhun" poocha tha, aur maine "ye lo banaya hua" de diya.
> **Is baar tum khud banaoge.** 9 chhote steps. Har step me **sirf ek idea**.

---

# 📍 Pehle ye padho (2 minute)

## Kya padhna hai, kya nahi

| File | Abhi kya karo |
|---|---|
| **Ye file** | ✅ **Sirf ye follow karo.** Step 1 se Step 9, order me |
| Badi guide `Test_Automation_Architecture_Guide.md` | ❌ **Abhi mat padho.** Wo baad me **dictionary** ki tarah hai: kisi step me kuch samajh na aaye to us step ke saamne likha "optional reading" part dekho |

## Har step ka format (hamesha same)

| Icon | Matlab |
|---|---|
| 🤕 **Dikkat** | Pehle dikhega ki problem kya hai (tabhi solution samajh aata hai) |
| 💡 **Idea** | Solution ek-do line me |
| ⌨️ **Karo** | Kaunsi file banani/badalni hai, code type karo |
| ▶️ **Chalao** | Command aur **kya output aana chahiye** |
| 🔍 **Code samjho** | Har line ka matlab |
| 🧠 **Kyun?** | Ye tareeka kyun, doosra kyun nahi |
| ✅ **Samjha?** | 2 chhote sawaal (jawab click karke dekho) |
| ✍️ **Khud karo** | Ek chhota kaam, tum khud |
| 🛟 **Atak gaye?** | `solutions/step_NN` folder me us step ka sahi code (usme `pytest` chalane ke liye Terminal 1 me demo shop chalta rehna chahiye) |

## 3 levels (kya zaroori hai)

| Level | Steps | Matlab |
|---|---|---|
| 🟢 **Zaroori** | 1 se 6 | Pehle ye pakke karo. Isse tumhara code **saaf** ho jaayega |
| 🟡 **Jab ready ho** | 7, 8 | Flow aur API. Pehle 6 steps ke baad |
| 🔵 **Bonus** | 9 | Rules ko test se enforce karna |

## Poora naksha (ek nazar me)

| Step | 🤕 Dikkat | 💡 Solution | Naya folder/file |
|---|---|---|---|
| 0 | Dekho: messy code | (kuch nahi, bas dekho) | |
| 1 | URL 3 jagah likha hai | Config me ek jagah | `pytest.ini` |
| 2 | Login ke 4 lines har test me | Page Object | `pages/login_page.py` |
| 3 | Baaki pages ke locators tests me | Baaki Page Objects | `pages/...` |
| 4 | Har page me same code | `BasePage` | `core/base_page.py` |
| 5 | `"standard_user"`, `"Backpack"` bikhre | Data layer | `data/` |
| 6 | Login ki taiyari har test me | Fixture | `tests/conftest.py` |
| 7 | Same sequence kai tests me | Flow | `flows/` |
| 8 | UI login har test me | API layer + token | `api/` |
| 9 | Koi rule tod de to? | Architecture test | `tests/test_architecture.py` |

## Ye 5 shabd jaan lo

| Shabd | Matlab |
|---|---|
| **Layer** | Code ka ek hissa jiska ek kaam hai (jaise `pages/` = screens ka code) |
| **Refactor** | Code ka **kaam badle bina** uski shakal saaf karna. Test pehle bhi green, baad me bhi green |
| **Import** | Ek file me dusri file ka code use karna (`from pages.login_page import LoginPage`) |
| **Dependency** | "A ko B chahiye" (A ne B ko import kiya) |
| **Repeat / duplicate** | Same code kai jagah. Isi se saari dikkat shuru hoti hai |

> [!IMPORTANT]
> **Sabse zaroori rule is poore guide ka:** har step ke baad `pytest` **green** hona chahiye. Agar red hai to aage mat badho. Pehle wahi step theek karo (ya `solutions/step_NN` se compare karo).

---

# ⚙️ Step 0: Setup aur messy code dekhna

## Setup (ek baar)

Zip kholo. `start/` folder me jao. Wahi tumhara kaam ka folder hai.

```bash
cd start
python -m venv .venv
source .venv/bin/activate          # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

## Demo shop chalao (**Terminal 1**, band mat karna)

```bash
python app_under_test/server.py
```
Likha aayega: `ShopDemo chal raha hai: http://127.0.0.1:8000`

> Is app ka code padhna **zaroori nahi**. Ye sirf wo shop hai jise hum test karenge.

## Tests chalao (**Terminal 2**, wahi `start` folder)

```bash
pytest
```
**Aana chahiye:** `3 passed` (ek warning aa sakti hai: "Session-scoped fixtures... base_url". Wo plugin ki apni warning hai, ignore karo).

## Ab `tests/test_shop.py` dekho

**File: `tests/test_shop.py`**
```python
from playwright.sync_api import expect


def test_login_works(page):
    page.goto("http://127.0.0.1:8000")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="Products")).to_be_visible()


def test_add_to_cart_updates_badge(page):
    page.goto("http://127.0.0.1:8000")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="Products")).to_be_visible()
    page.get_by_test_id("product").filter(has_text="Backpack").get_by_role("button", name="Add to cart").click()
    expect(page.get_by_test_id("cart-count")).to_have_text("1")


def test_user_can_buy_backpack(page):
    page.goto("http://127.0.0.1:8000")
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

## 🔎 Isme kya dikkat hai? (abhi sirf dekho, theek kal karenge)

Ye code **chalta hai**, par ginti karo:

| Cheez | Kitni baar likhi hai |
|---|---|
| `"http://127.0.0.1:8000"` | **3 baar** |
| Login ki 4 lines (`fill`, `fill`, `click`, `expect`) | **3 baar** |
| `"standard_user"`, `"secret_sauce"` | **3 baar** |
| `page.get_by_...` (raw locators test ke andar) | **kai baar** |

**Kal ka din socho:** developer "Login" button ka naam "Sign in" kar de. Tumhe **har test** me jaake badalna padega. 50 tests = 50 jagah. Isi dard ko dur karne ke liye **architecture** hai.

> [!NOTE]
> Architecture ka matlab "bahut saari files" nahi. Matlab: **har cheez ka ek ghar**, taaki ek badlaav = ek jagah.

**Agle 9 steps me hum ek-ek dard dur karenge.**

---

# 🟢 Step 1: URL ek jagah

## 🤕 Dikkat
URL (`http://127.0.0.1:8000`) 3 tests me likha hai. Kal app `9000` port par chale, ya staging par chalana ho, to 3 (ya 300) jagah badlana padega.

## 💡 Idea
URL **ek jagah** (config file me). Tests me sirf `"/"` likhenge.

## ⌨️ Karo

**1) `pytest.ini` badlo** (ek line jodo):

**File: `pytest.ini`**
```ini
[pytest]
pythonpath = .
testpaths = tests
base_url = http://127.0.0.1:8000
```

**2) `tests/test_shop.py` me** har `page.goto("http://127.0.0.1:8000")` ko `page.goto("/")` karo. Poora badlaav:

**File: `tests/test_shop.py`** (sirf ye badlaav: `-` hatao, `+` jodo)
```diff
 def test_login_works(page):
-    page.goto("http://127.0.0.1:8000")
+    page.goto("/")
     page.get_by_placeholder("Username").fill("standard_user")
  ...
 def test_add_to_cart_updates_badge(page):
-    page.goto("http://127.0.0.1:8000")
+    page.goto("/")
     page.get_by_placeholder("Username").fill("standard_user")
  ...
 def test_user_can_buy_backpack(page):
-    page.goto("http://127.0.0.1:8000")
+    page.goto("/")
     page.get_by_placeholder("Username").fill("standard_user")
```

(Hint: editor me Find & Replace use karo: `"http://127.0.0.1:8000"` → `"/"`)

## ▶️ Chalao
```bash
pytest
```
**Aana chahiye:** `3 passed`

## 🔍 Code samjho
- `base_url = ...`: pytest-playwright ka setting. Isse Playwright ko **default website** pata chalti hai.
- `page.goto("/")`: Playwright `base_url` ke aage `/` jod deta hai, yaani `http://127.0.0.1:8000/`.
- Ab URL **sirf `pytest.ini` me** hai.

## 🧠 Kyun?
| Tareeka | Dikkat |
|---|---|
| URL har test me | Badalna = bahut jagah ❌ |
| **URL config me (humne chuna)** | Badalna = 1 jagah ✅. Command se bhi badal sakte ho: `pytest --base-url http://127.0.0.1:9000` |

Isko kehte hain **"config over code"**: jo cheez environment ke saath badalti hai wo code me nahi, config me.

## ✅ Samjha?
<details>
<summary>1. App 9000 port par chalne lage. Kitni files badlengi?</summary>

**Ek:** `pytest.ini`. (Ya koi file nahi, agar `pytest --base-url http://127.0.0.1:9000` chalao.)
</details>

<details>
<summary>2. <code>page.goto("/")</code> me poora URL kyun nahi?</summary>

Taaki test ko **pata hi na ho** ki kaunsa environment hai. Environment ka kaam config ka hai.
</details>

## ✍️ Khud karo
`pytest.ini` me port `8000` ki jagah `9000` likho aur `pytest` chalao. **Error padho** (kya likha hai?). Phir wapas `8000` karo.

<details>
<summary>💬 Kya dikhna chahiye</summary>

Error me `net::ERR_CONNECTION_REFUSED at http://127.0.0.1:9000/` aayega. Matlab: "us address par koi app nahi chal rahi". Ye error pehchanna seekho, ye bahut kaam aayega.
</details>

🛟 Atak gaye? `solutions/step_01`

---

# 🟢 Step 2: Login ka Page Object

## 🤕 Dikkat
Login ki 4 lines (`fill`, `fill`, `click`) **har test me** hain. "Login" button ka naam badla to har test toota.

## 💡 Idea
**Ek screen = ek class.** Login screen ki saari cheezein ek class `LoginPage` me. (Page Object tum jaante ho. Yahan dhyan do **folder aur public/private** par.)

## ⌨️ Karo

**1) Folder `pages/` banao** aur usme ek khali file `__init__.py` (isse folder "package" banta hai, `from pages... import` chalta hai).

**2) `pages/login_page.py`:**

**File: `pages/login_page.py`**
```python
from playwright.sync_api import Locator, Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_button = page.get_by_role("button", name="Login")
        self.error: Locator = page.get_by_role("alert")

    def open(self):
        self.page.goto("/")
        self.wait_until_loaded()

    def wait_until_loaded(self):
        expect(self._login_button).to_be_visible()

    def login(self, username: str, password: str):
        self._username.fill(username)
        self._password.fill(password)
        self._login_button.click()
```

**3) `tests/test_shop.py`** poora replace karo (ab login `LoginPage` se, aur ek naya test bhi):

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
    expect(login.error).to_have_text("Username and password do not match")


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
| `class LoginPage:` | Login screen ka representation |
| `def __init__(self, page)` | Page Object ko Playwright ka `page` milta hai |
| `self._username = page.get_by_placeholder("Username")` | Username box ka locator. **`_` se shuru = private** ("ye class ke andar ki cheez hai") |
| `self.error: Locator = page.get_by_role("alert")` | Error message ka locator. **Bina `_` = public**, kyunki test ko `expect(login.error)...` likhna hai |
| `def open(self)` | `/` kholo (`base_url` ke saath) aur login button dikhne tak **wait** |
| `def wait_until_loaded(self)` | Login button visible hone ka intezaar |
| `def login(self, username, password)` | Teen kaam: username bharo, password bharo, button dabao |

## 🧠 Kyun?
- **Locators page ke andar, tests ke bahar:** "Login" ka naam badla to sirf `login_page.py` badlega.
- **Private vs public:** jo cheez test ko **seedha check** karni hai (`error`) wo public. Baaki chhupi hui. Test ko `click()` nahi, `login()` bolna chahiye.
- **Public cheez `Locator` hai (text nahi):** `expect(login.error).to_have_text(...)` **retry** karta hai (thodi der wait). Agar page `get_error_text()` jaisa method deta jo text ek baar padh leta, to test flaky hota.

## ✅ Samjha?
<details>
<summary>1. "Login" button ka text "Sign in" ho gaya. Kitni files badlengi?</summary>

**Ek:** `pages/login_page.py` (`name="Login"` ek jagah). Tests nahi badlenge.
</details>

<details>
<summary>2. <code>_username</code> ke aage underscore kyun?</summary>

Convention: "ye private hai, bahar se mat chhuo". Test `login()` use kare, `_username.fill()` nahi. Ye rakhta hai ki locator ka detail page ke andar chhupa rahe.
</details>

## ✍️ Khud karo
Ek naya test likho: `test_locked_user_shows_error`. User `locked_user` (password `secret_sauce`) se login karo aur error `Sorry, this user has been locked out.` check karo.

<details>
<summary>💡 Hint</summary>

`test_wrong_password_shows_error` jaisa hi hai. Bas username aur expected message alag.
</details>

<details>
<summary>✅ Jawab</summary>

```python
def test_locked_user_shows_error(page):
    login = LoginPage(page)
    login.open()
    login.login("locked_user", "secret_sauce")
    expect(login.error).to_have_text("Sorry, this user has been locked out.")
```
</details>

🛟 Atak gaye? `solutions/step_02` (📖 optional reading: badi guide ka Part 8)

---

# 🟢 Step 3: Baaki pages

## 🤕 Dikkat
Login to `LoginPage` me chala gaya. Par inventory (products), cart aur order-complete ke locators abhi bhi tests me hain (`page.get_by_test_id("product")...`).

## 💡 Idea
Wahi pattern: **har screen ka ek page class.** Ab 3 page aur banao.

## ⌨️ Karo

**`pages/inventory_page.py`:**

**File: `pages/inventory_page.py`**
```python
from playwright.sync_api import Page, expect


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

    def open_cart(self):
        self._cart_button.click()
```

**Ab `CartPage` aur `OrderCompletePage` khud banane ki koshish karo** (neeche hint). Phir solution se check karo.

<details>
<summary>💡 Hint</summary>

`InventoryPage` jaisa hi:
- `CartPage`: heading `"Your Cart"`, button `"Checkout"` (private), method `wait_until_loaded()` aur `checkout()`.
- `OrderCompletePage`: heading `"Thank you for your order!"` (**public**, kyunki test check karega), method `wait_until_loaded()`.
</details>

<details>
<summary>✅ Solution</summary>

**File: `pages/cart_page.py`**
```python
from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self._heading = page.get_by_role("heading", name="Your Cart")
        self._checkout_button = page.get_by_role("button", name="Checkout")

    def wait_until_loaded(self):
        expect(self._heading).to_be_visible()

    def checkout(self):
        self._checkout_button.click()
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
</details>

**`tests/test_shop.py`** poora replace:

**File: `tests/test_shop.py`**
```python
from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.order_complete_page import OrderCompletePage


def test_login_works(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    InventoryPage(page).wait_until_loaded()


def test_wrong_password_shows_error(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "wrong-password")
    expect(login.error).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.wait_until_loaded()
    inventory.add_to_cart("Backpack")
    expect(inventory.cart_badge).to_have_text("1")


def test_user_can_buy_backpack(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.wait_until_loaded()
    inventory.add_to_cart("Backpack")
    inventory.open_cart()
    cart = CartPage(page)
    cart.wait_until_loaded()
    cart.checkout()
    done = OrderCompletePage(page)
    expect(done.heading).to_be_visible()
```

## ▶️ Chalao
```bash
pytest
```
**Aana chahiye:** `4 passed`

## 🔍 Code samjho (naye hisse)
- `self.cart_badge = page.get_by_test_id("cart-count")`: cart ka number. **Public**, test `expect(inventory.cart_badge).to_have_text("1")` likhega.
- `self._cards.filter(has_text=product_name)`: saare product cards me se wo jisme ye naam hai. Phir **us card ke andar** ka "Add to cart" button. Isse "sahe product ka sahi button" milta hai.
- `def add_to_cart(self, product_name)`: test ko sirf product ka **naam** dena hai. Button, card, locator ka detail andar.
- `test_user_can_buy_backpack` ab **kahani** jaisa padhta hai: login, inventory, add, cart, checkout, order complete.

## 🧠 Kyun?
Test ab **kya** karna hai batata hai (`add_to_cart("Backpack")`), **kaise** nahi (button kahan hai). "Kaise" ek jagah (page) me hai.

## ✅ Samjha?
<details>
<summary>1. Test file me ab <code>get_by_</code> likha hai kahin?</summary>

**Nahi.** Saare locators `pages/` me. (Step 9 me hum is baat ko test se enforce karenge.)
</details>

<details>
<summary>2. Cart badge ka locator badla. Kahan fix?</summary>

`pages/inventory_page.py` me ek line.
</details>

🛟 Atak gaye? `solutions/step_03`

---

# 🟢 Step 4: BasePage (jo cheez har page me same hai)

## 🤕 Dikkat
Dekho `pages/` ko. **Har page me same cheez** hai:

```python
def wait_until_loaded(self):
    expect(self._heading).to_be_visible()
```
4 pages = 4 baar. Aur `open()` sirf `LoginPage` me hai.

## 💡 Idea
Jo cheez **sab pages me same** hai wo ek **`BasePage`** me. Har page us se **inherit** kare, aur sirf itna bataye: *"mere page ke load hone ka matlab kya hai"*.

## ⌨️ Karo

**1) Folder `core/` + khali `__init__.py`. Phir `core/base_page.py`:**

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

**2) `pages/login_page.py`** (poora):

**File: `pages/login_page.py`**
```python
from playwright.sync_api import Locator, Page

from core.base_page import BasePage


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

    def login(self, username: str, password: str):
        self._username.fill(username)
        self._password.fill(password)
        self._login_button.click()
```

**3) Baaki 3 pages me sirf ye badlaav** (`-` hatao, `+` jodo):

**File: `pages/inventory_page.py`** (sirf ye badlaav: `-` hatao, `+` jodo)
```diff
-from playwright.sync_api import Page, expect
+from playwright.sync_api import Locator, Page
+
+from core.base_page import BasePage
 
 
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
 
```

**File: `pages/cart_page.py`** (sirf ye badlaav: `-` hatao, `+` jodo)
```diff
-from playwright.sync_api import Page, expect
+from playwright.sync_api import Locator, Page
+
+from core.base_page import BasePage
 
 
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

**4) `tests/test_shop.py`** poora replace:

**File: `tests/test_shop.py`**
```python
from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.order_complete_page import OrderCompletePage


def test_login_works(page):
    login = LoginPage(page).open()
    login.login("standard_user", "secret_sauce")
    InventoryPage(page).wait_until_loaded()


def test_wrong_password_shows_error(page):
    login = LoginPage(page).open()
    login.login("standard_user", "wrong-password")
    expect(login.error).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(page):
    login = LoginPage(page).open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page).wait_until_loaded()
    inventory.add_to_cart("Backpack")
    expect(inventory.cart_badge).to_have_text("1")


def test_user_can_buy_backpack(page):
    login = LoginPage(page).open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page).wait_until_loaded()
    inventory.add_to_cart("Backpack")
    inventory.open_cart()
    CartPage(page).wait_until_loaded().checkout()
    done = OrderCompletePage(page)
    expect(done.heading).to_be_visible()
```

## ▶️ Chalao
```bash
pytest
```
**Aana chahiye:** `4 passed`

## 🔍 Code samjho (BasePage)

| Line | Matlab |
|---|---|
| `path = "/"` | Page ka URL path. Child chaahe to badal le |
| `@property def loaded_locator` + `raise NotImplementedError` | **Har child ko batana padega.** Nahi bataya to saaf error aayega. "Page load hua" ka matlab har page ke liye alag hai |
| `wait_until_loaded()` | `loaded_locator` dikhne tak wait. `return self` karta hai |
| `open()` | `goto(path)` phir `wait_until_loaded()`. **Har page ka `open()` ab ek jaisa** |
| `return self` | Isse chain likh sakte ho: `LoginPage(page).open().login(...)` |
| `class LoginPage(BasePage):` | `LoginPage` ko `BasePage` ka `open` aur `wait_until_loaded` mil gaya |
| `super().__init__(page)` | Parent ka `__init__` bhi chalao (taaki `self.page` set ho) |

## 🧠 Kyun?
- **Repeat kam:** "page load wait" ek jagah.
- **Galti kam:** naya page banate waqt "wait lagana bhool gaya" nahi hota (`open()` khud karta hai).
- **Template idea:** `BasePage` ek **template** hai, child sirf ek tukda (`loaded_locator`) bharta hai.

> [!WARNING]
> **`BasePage` me sirf wahi daalo jo SAB pages ko chahiye.** Agar `login()` ya `add_to_cart()` jaise methods BasePage me daaloge to wo ek bada kabaad (god class) ban jaayega aur ek badlaav sab ko hilayega. **Chhota rakho.**

## ✅ Samjha?
<details>
<summary>1. Naya page banaya par <code>loaded_locator</code> nahi likha. Kya hoga?</summary>

`open()` ya `wait_until_loaded()` par `NotImplementedError: Child page 'loaded_locator' define kare`. Ye jaan-boojh ke saaf error hai.
</details>

<details>
<summary>2. <code>wait_until_loaded</code> ko BasePage me kyun rakha, <code>add_to_cart</code> ko kyun nahi?</summary>

`wait_until_loaded` **sab pages** ko chahiye. `add_to_cart` sirf inventory page ka kaam hai.
</details>

## ✍️ Khud karo
Ek **khayali** page banao (bas test ke liye, baad me hata dena): `core` ki tarah `BasePage` se inherit karke `class ProfilePage(BasePage): pass`. Phir ek temporary test me `ProfilePage(page).open()` chalao. **Kya error aaya?** Aur kyun?

<details>
<summary>💬 Kya dikhna chahiye</summary>

`NotImplementedError: Child page 'loaded_locator' define kare`. Kyunki `ProfilePage` ne nahi bataya ki "mera page load hua" ka matlab kya. Ye **jaan-boojh ka saaf error** hai (chup-chap galat chalne se behtar).
</details>

🛟 Atak gaye? `solutions/step_04` (📖 optional: badi guide ka Part 7.3)

---

# 🟢 Step 5: Data layer

## 🤕 Dikkat
`"standard_user"`, `"secret_sauce"`, `"Backpack"` strings tests me bikhri hain. Product ka naam badla ya password badla to har jagah.

## 💡 Idea
**Data ek jagah** (`data/` folder). Tests us data ka **naam** use karein.

## ⌨️ Karo

**1) Folder `data/` + khali `__init__.py`.**

**2) `data/users.py`:**

**File: `data/users.py`**
```python
import os
from dataclasses import dataclass, field


@dataclass(frozen=True)
class User:
    username: str
    password: str = field(repr=False)


def get_user(kind: str = "standard") -> User:
    users = {
        "standard": User("standard_user", os.environ.get("STANDARD_USER_PASSWORD", "secret_sauce")),
        "locked": User("locked_user", os.environ.get("LOCKED_USER_PASSWORD", "secret_sauce")),
    }
    return users[kind]
```

**3) `data/products.py`:**

**File: `data/products.py`**
```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    id: str
    name: str
    price: float


BACKPACK = Product("backpack", "Backpack", 29.99)
BIKE_LIGHT = Product("bike-light", "Bike Light", 9.99)
ONESIE = Product("onesie", "Onesie", 7.99)

ALL_PRODUCTS = (BACKPACK, BIKE_LIGHT, ONESIE)
```

**4) `tests/test_shop.py`** poora replace:

**File: `tests/test_shop.py`**
```python
from dataclasses import replace

from playwright.sync_api import expect

from data.products import BACKPACK
from data.users import get_user
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.order_complete_page import OrderCompletePage


def test_login_works(page):
    user = get_user("standard")
    login = LoginPage(page).open()
    login.login(user.username, user.password)
    InventoryPage(page).wait_until_loaded()


def test_wrong_password_shows_error(page):
    bad_user = replace(get_user("standard"), password="wrong-password")
    login = LoginPage(page).open()
    login.login(bad_user.username, bad_user.password)
    expect(login.error).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(page):
    user = get_user("standard")
    login = LoginPage(page).open()
    login.login(user.username, user.password)
    inventory = InventoryPage(page).wait_until_loaded()
    inventory.add_to_cart(BACKPACK.name)
    expect(inventory.cart_badge).to_have_text("1")


def test_user_can_buy_backpack(page):
    user = get_user("standard")
    login = LoginPage(page).open()
    login.login(user.username, user.password)
    inventory = InventoryPage(page).wait_until_loaded()
    inventory.add_to_cart(BACKPACK.name)
    inventory.open_cart()
    CartPage(page).wait_until_loaded().checkout()
    done = OrderCompletePage(page)
    expect(done.heading).to_be_visible()
```

## ▶️ Chalao
```bash
pytest
```
**Aana chahiye:** `4 passed`

## 🔍 Code samjho

| Line | Matlab |
|---|---|
| `@dataclass(frozen=True)` | Chhoti data class. `frozen=True` = **badal nahi sakte** (galti se test beech me user ka password na badal de) |
| `password: str = field(repr=False)` | `print(user)` ya error message me **password nahi dikhega** (security) |
| `os.environ.get("STANDARD_USER_PASSWORD", "secret_sauce")` | Pehle environment variable se, nahi to demo default. Asli password code me nahi rehta |
| `get_user("standard")` | Naam se user. Padhne me saaf |
| `BACKPACK = Product("backpack", "Backpack", 29.99)` | Product ek jagah. Test me `BACKPACK.name` |
| `ALL_PRODUCTS = (...)` | Saare products ki list (Step 7 me kaam aayegi) |
| `from dataclasses import replace` | **Copy with change.** `replace(get_user("standard"), password="wrong-password")` = standard user, par password alag |

## 🧠 Kyun?
- Product ka naam badla = **1 file**.
- Password code me nahi, **environment me**. Repo public ho jaye to bhi leak nahi.
- `frozen` + `repr=False`: chhote kadam jo bade bugs aur leaks rokte hain.

## ✅ Samjha?
<details>
<summary>1. Terminal me <code>python -c "from data.users import get_user; print(get_user('standard'))"</code> chalao. Password dikha?</summary>

Nahi: `User(username='standard_user')`. `repr=False` ki wajah se.
</details>

<details>
<summary>2. Backpack ka naam "Rucksack" ho gaya (app me bhi). Kitni files?</summary>

Test side par **ek**: `data/products.py`.
</details>

## ✍️ Khud karo
`data/users.py` me ek aur user type jodo (jaise `"problem"`: `"problem_user"`) aur dekho `get_user("problem")` chalta hai. Phir `get_user("abc")` karke error padho. Kya error aaya? (KeyError) Is par socho: error aur saaf kaise ho sakta hai? (Badi guide Part 6 me ek tareeka hai.)

🛟 Atak gaye? `solutions/step_05`

---

# 🟢 Step 6: Fixture (taiyari ek jagah)

## 🤕 Dikkat
Dekho tests: `test_add_to_cart_updates_badge` aur `test_user_can_buy_backpack` dono **pehle ye karte hain:** user lo → login page kholo → login karo → inventory ka intezaar. Ye "taiyari" repeat ho rahi hai.

## 💡 Idea
"Taiyari" ko **fixture** me daalo. Test sirf apna asli kaam likhe. (Fixture tum jaante ho. Yahan dhyan do: **fixtures ka kaam layers ko jodna hai** (wiring).)

## ⌨️ Karo

**1) `tests/conftest.py` (naya):**

**File: `tests/conftest.py`**
```python
import pytest

from data.users import User, get_user
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def user() -> User:
    return get_user("standard")


@pytest.fixture
def inventory_page(page, user) -> InventoryPage:
    LoginPage(page).open().login(user.username, user.password)
    return InventoryPage(page).wait_until_loaded()
```

**2) `tests/test_shop.py`** poora replace:

**File: `tests/test_shop.py`**
```python
from dataclasses import replace

from playwright.sync_api import expect

from data.products import BACKPACK
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.order_complete_page import OrderCompletePage


def test_login_works(page, user):
    login = LoginPage(page).open()
    login.login(user.username, user.password)
    InventoryPage(page).wait_until_loaded()


def test_wrong_password_shows_error(page, user):
    bad_user = replace(user, password="wrong-password")
    login = LoginPage(page).open()
    login.login(bad_user.username, bad_user.password)
    expect(login.error).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(inventory_page):
    inventory_page.add_to_cart(BACKPACK.name)
    expect(inventory_page.cart_badge).to_have_text("1")


def test_user_can_buy_backpack(page, inventory_page):
    inventory_page.add_to_cart(BACKPACK.name)
    inventory_page.open_cart()
    CartPage(page).wait_until_loaded().checkout()
    done = OrderCompletePage(page)
    expect(done.heading).to_be_visible()
```

## ▶️ Chalao
```bash
pytest
```
**Aana chahiye:** `4 passed`

## 🔍 Code samjho

| Line | Matlab |
|---|---|
| `tests/conftest.py` | Is naam ki file ke fixtures `tests/` ke **saare tests ko bina import kiye** milte hain |
| `def user()` | Fixture: standard user deta hai |
| `def inventory_page(page, user)` | Fixture ko `page` (pytest-playwright ka) aur `user` (hamara) chahiye. Pytest **argument ke naam se** dhundh ke deta hai |
| `LoginPage(page).open().login(...)` | Login karo (chain: open phir login) |
| `return InventoryPage(page).wait_until_loaded()` | Inventory ready page object lautao |
| `def test_add_to_cart_updates_badge(inventory_page)` | Test ko ab **login ki chinta nahi**. Seedha logged-in inventory page mila |

## 🧠 Kyun?
- Taiyari ek jagah. Login ka tareeka badla = **ek fixture** badlega.
- **Fixture ka kaam wiring hai:** `pages` ko `data` se jodna aur tests ko dena. Isme business assertions nahi (wo test ka kaam).
- Login ke **tests** (`test_login_works`, `test_wrong_password...`) fixture nahi use karte, kyunki unka maqsad hi login karna hai.

## ✅ Samjha?
<details>
<summary>1. <code>test_login_works</code> ne <code>inventory_page</code> fixture kyun nahi liya?</summary>

Wo **login hi test kar raha hai**. Agar fixture pehle login kar de to test kuch test hi nahi karta.
</details>

<details>
<summary>2. Fixture ke andar <code>expect(...)</code> jaisi business assertion kyun nahi?</summary>

Fixture taiyari karta hai. "Kya sahi hai" ka faisla test karta hai. (Sirf "page load hua" jaisa readiness wait theek hai: <code>wait_until_loaded</code>.)
</details>

## ✍️ Khud karo
Ek naya test likho `test_cart_badge_starts_at_zero(inventory_page)`: shuru me cart badge `"0"` hona chahiye.

<details>
<summary>✅ Jawab</summary>

```python
def test_cart_badge_starts_at_zero(inventory_page):
    expect(inventory_page.cart_badge).to_have_text("0")
```
</details>

## 🎉 Level 🟢 complete!
Tumne ye kiya: **config, pages, base class, data, fixture.** Ye architecture ka 80% hai. Ab agle 2 steps (🟡) tab karo jab upar wale pakke ho gaye.

🛟 Atak gaye? `solutions/step_06` (📖 optional: badi guide ka Part 11)

---

# 🟡 Step 7: Flow (jab sequence teesri baar repeat ho)

## 🤕 Dikkat
Maan lo ab 3 aur tests chahiye: "har product khareedna" aur "do products saath". Har test me ye block copy karna padega:

```python
inventory_page.add_to_cart(...)
inventory_page.add_to_cart(...)   # (do product hon to)
inventory_page.open_cart()
CartPage(page).wait_until_loaded().checkout()
done = OrderCompletePage(page).wait_until_loaded()
```
Wahi cheez fir se repeat.

## 💡 Idea
**Rule of three:** pehli baar likho, doosri baar copy chalega, **teesri baar repeat dikhe to ek jagah banao.** Ye jagah ka naam **Flow**: kai pages ko jodne wala business action ("khareedo").

## ⌨️ Karo

**1) Folder `flows/` + khali `__init__.py`. Phir `flows/shopping_flow.py`:**

**File: `flows/shopping_flow.py`**
```python
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.order_complete_page import OrderCompletePage


class ShoppingFlow:
    def __init__(self, page: Page):
        self._page = page

    def buy(self, inventory: InventoryPage, product_names: list[str]) -> OrderCompletePage:
        for name in product_names:
            inventory.add_to_cart(name)
        inventory.open_cart()
        CartPage(self._page).wait_until_loaded().checkout()
        return OrderCompletePage(self._page).wait_until_loaded()
```

**2) `tests/test_shop.py`** poora replace:

**File: `tests/test_shop.py`**
```python
from dataclasses import replace

import pytest
from playwright.sync_api import expect

from data.products import ALL_PRODUCTS, BACKPACK, ONESIE
from flows.shopping_flow import ShoppingFlow
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_login_works(page, user):
    login = LoginPage(page).open()
    login.login(user.username, user.password)
    InventoryPage(page).wait_until_loaded()


def test_wrong_password_shows_error(page, user):
    bad_user = replace(user, password="wrong-password")
    login = LoginPage(page).open()
    login.login(bad_user.username, bad_user.password)
    expect(login.error).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(inventory_page):
    inventory_page.add_to_cart(BACKPACK.name)
    expect(inventory_page.cart_badge).to_have_text("1")


@pytest.mark.parametrize("product", ALL_PRODUCTS, ids=lambda p: p.id)
def test_user_can_buy_each_product(page, inventory_page, product):
    done = ShoppingFlow(page).buy(inventory_page, [product.name])
    expect(done.heading).to_be_visible()


def test_user_can_buy_two_products(page, inventory_page):
    done = ShoppingFlow(page).buy(inventory_page, [BACKPACK.name, ONESIE.name])
    expect(done.heading).to_be_visible()
```

## ▶️ Chalao
```bash
pytest
```
**Aana chahiye:** `7 passed` (parametrize se ek test 3 baar chala)

## 🔍 Code samjho

| Line | Matlab |
|---|---|
| `class ShoppingFlow` | Khareedne ka kaam |
| `def buy(self, inventory, product_names)` | Naye products ki list lo aur khareed lo |
| `for name in product_names: inventory.add_to_cart(name)` | Har naam ke liye add |
| `CartPage(...).wait_until_loaded().checkout()` | Cart khulne ka wait, phir checkout |
| `return OrderCompletePage(...).wait_until_loaded()` | Agla page lautao, taaki test `done.heading` check kar sake |
| `@pytest.mark.parametrize("product", ALL_PRODUCTS, ids=lambda p: p.id)` | **Ek test, 3 baar** (har product ke liye). `ids=` se test ka naam readable (`...[backpack]`) |
| **`buy()` me koi `expect` nahi** | Flow sirf **karta** hai. "Kya sahi hai" test ka kaam |

## 🧠 Kyun?
| Tareeka | Dikkat |
|---|---|
| Har test me copy | Badlaav = bahut jagah ❌ |
| Page me `buy()` daalna | InventoryPage ko cart aur order ka pata ho gaya (page phool gaya) ❌ |
| **Alag Flow class (humne chuna)** | Pages chhote, "khareedna" ek jagah ✅ |

> [!WARNING]
> **Flow tab banao jab repeat dikhe, pehle se nahi.** Agar sirf ek test "buy" karta, to flow ki zaroorat nahi thi. Flow me `if/else` aane lage to ruk jao: wo ab test logic ban raha hai.

## ✅ Samjha?
<details>
<summary>1. Flow me <code>expect(...)</code> kyun nahi?</summary>

Alag tests alag cheez verify karna chahenge. Flow sirf kaam karta hai, verify test karta hai.
</details>

<details>
<summary>2. Naya product "Water Bottle" app me aaya. <code>data/products.py</code> me kya karoge aur test ka kya hoga?</summary>

`ALL_PRODUCTS` me jodo. `test_user_can_buy_each_product` **apne aap** uske liye bhi chalega.
</details>

## ✍️ Khud karo
Ek test likho jo **Bike Light** aur **Onesie** dono khareede (`BIKE_LIGHT`, `ONESIE` data se).

<details>
<summary>✅ Jawab</summary>

```python
from data.products import BIKE_LIGHT, ONESIE

def test_user_can_buy_bike_light_and_onesie(page, inventory_page):
    done = ShoppingFlow(page).buy(inventory_page, [BIKE_LIGHT.name, ONESIE.name])
    expect(done.heading).to_be_visible()
```
(`BIKE_LIGHT`, `ONESIE` ko import karna mat bhoolna.)
</details>

🛟 Atak gaye? `solutions/step_07` (📖 optional: badi guide ka Part 9)

---

# 🟡 Step 8: API layer (UI se login ki jagah token)

## 🤕 Dikkat
`inventory_page` fixture **UI se login** karta hai (type, click). Ye:
1. **Slow** hai (har test me).
2. **Fragile** hai: login screen ki ek problem se **saare** tests fail.
3. Test me "cart me pehle se 1 item" jaisi **taiyari** UI se karna mushkil hai.

## 💡 Idea
Backend ke **API** se login karo, token lo, browser ko de do. UI test seedha logged-in shuru ho. Aur API se data bhi taiyar karo.

```text
Fixture ──► API se login ──► token ─┬──► browser ko token do  (UI test logged-in shuru)
                                    └──► API client ko token do (cart me item daalna, cleanup)
```

> [!NOTE]
> **Honest baat:** mere local test me fark chhota dikha: ek test ka setup+run **~0.77 sec (UI login)** se **~0.59 sec (API token)**. Kyunki demo app local aur tez hai. **Asli, door ke server par fark bahut bada hota hai.** Aur bada faida **speed nahi, control** hai (API se data banana).

## ⌨️ Karo

**1) Folder `api/` + khali `__init__.py`. Teen files:**

**File: `api/base_client.py`**
```python
import requests


class BaseApiClient:
    def __init__(self, base_url: str, token: str | None = None, timeout: float = 10):
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout
        self._session = requests.Session()
        if token:
            self._session.headers["Authorization"] = f"Bearer {token}"

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        kwargs.setdefault("timeout", self._timeout)
        return self._session.request(method, f"{self._base_url}{path}", **kwargs)

    def close(self):
        self._session.close()
```

**File: `api/auth_api.py`**
```python
import requests

from api.base_client import BaseApiClient
from data.users import User


class AuthApi(BaseApiClient):
    def login(self, username: str, password: str) -> requests.Response:
        return self.request("POST", "/api/login", json={"username": username, "password": password})

    def get_token(self, user: User) -> str:
        response = self.login(user.username, user.password)
        response.raise_for_status()
        return response.json()["token"]
```

**File: `api/shop_api.py`**
```python
import requests

from api.base_client import BaseApiClient


class ShopApi(BaseApiClient):
    def get_cart(self) -> requests.Response:
        return self.request("GET", "/api/cart")

    def add_to_cart(self, product_id: str) -> requests.Response:
        return self.request("POST", "/api/cart", json={"product_id": product_id})

    def clear_cart(self) -> requests.Response:
        return self.request("DELETE", "/api/cart")

    def checkout(self) -> requests.Response:
        return self.request("POST", "/api/checkout")
```

**2) `tests/conftest.py`** poora replace:

**File: `tests/conftest.py`**
```python
import json

import pytest

from api.auth_api import AuthApi
from api.shop_api import ShopApi
from data.users import User, get_user
from pages.inventory_page import InventoryPage


@pytest.fixture
def user() -> User:
    return get_user("standard")


@pytest.fixture
def api_token(base_url, user) -> str:
    client = AuthApi(base_url)
    try:
        return client.get_token(user)
    finally:
        client.close()


@pytest.fixture
def shop_api(base_url, api_token):
    client = ShopApi(base_url, token=api_token)
    yield client
    client.clear_cart()
    client.close()


@pytest.fixture
def authenticated_page(page, api_token):
    page.add_init_script(f"window.localStorage.setItem('token', {json.dumps(api_token)});")
    return page


@pytest.fixture
def inventory_page(authenticated_page) -> InventoryPage:
    return InventoryPage(authenticated_page).open()
```

**3) Do naye test files:**

**File: `tests/test_api_cart.py`**
```python
from data.products import BACKPACK


def test_add_product_to_cart(shop_api):
    response = shop_api.add_to_cart(BACKPACK.id)

    assert response.status_code == 201
    assert response.json() == {"items": [BACKPACK.id], "count": 1}


def test_unknown_product_is_rejected(shop_api):
    assert shop_api.add_to_cart("does-not-exist").status_code == 404


def test_checkout_with_empty_cart_is_rejected(shop_api):
    assert shop_api.checkout().status_code == 400
```

**File: `tests/test_hybrid.py`**
```python
from playwright.sync_api import expect

from data.products import BACKPACK
from pages.inventory_page import InventoryPage


def test_item_added_by_api_is_visible_in_ui(authenticated_page, shop_api):
    shop_api.add_to_cart(BACKPACK.id)                      # setup: API se

    inventory = InventoryPage(authenticated_page).open()   # verify: UI se
    expect(inventory.cart_badge).to_have_text("1")
```

(`tests/test_shop.py` **wahi rahega**: uska `inventory_page` ab naye fixture se aayega.)

## ▶️ Chalao
```bash
pytest
```
**Aana chahiye:** `11 passed`

## 🔍 Code samjho

### API files
| Line | Matlab |
|---|---|
| `class BaseApiClient` | Har API client ka base |
| `requests.Session()` | Ek session: headers aur connection reuse |
| `self._session.headers["Authorization"] = f"Bearer {token}"` | Token **ek baar**, har request me apne aap jaata hai |
| `kwargs.setdefault("timeout", self._timeout)` | **Timeout hamesha.** Bina timeout request atak sakti hai |
| `return self._session.request(...)` | **Raw response lautao** (raise nahi). Test decide kare ki 404/400 expected hai ya error |
| `class AuthApi(BaseApiClient)`, `login(...)` | `POST /api/login` |
| `get_token(user)` + `raise_for_status()` | Token lo. Login fail to **exception** (taiyari fail = saaf signal) |
| `class ShopApi`, `add_to_cart`, `clear_cart`, `checkout` | Har method = ek endpoint. Business naam (URL andar chhupa) |

### conftest.py
| Line | Matlab |
|---|---|
| `api_token(base_url, user)` | `base_url` pytest-playwright ka fixture (jo `pytest.ini` se aata hai). Login karo, token do, client band karo (`finally`) |
| **Har test ka apna token** | Token = alag session = **alag cart**. Tests ek doosre se **independent** |
| `shop_api(base_url, api_token)` + `yield` + `client.clear_cart()` | Test ke **baad cleanup** (`yield` ke baad ka code) |
| `authenticated_page(page, api_token)` | `page.add_init_script(...localStorage.setItem('token', ...))`: **page khulne se pehle** browser me token daal do. App token dekh ke seedha inventory dikhati hai |
| `json.dumps(api_token)` | Token ko safe JavaScript string banata hai |
| `inventory_page(authenticated_page)` | Ab **UI login nahi**, token se seedha inventory |

### hybrid test
`shop_api.add_to_cart(...)` (API se **setup**) → `InventoryPage(...).open()` → `expect(badge)...` (UI se **verify**). Dono ne **ek hi token** use kiya, isliye jo API me bana wo UI me dikha.

## 🧠 Kyun?
| Sawaal | Jawab |
|---|---|
| API alag layer kyun? | URL, token, timeout har test me copy na ho. Endpoint badla = ek file |
| Client raw response kyun lautata hai? | Negative tests (404, 400) ko status code chahiye |
| Har test ka alag token kyun? | **Isolation.** Shared token par ek test cart me item chhodta to doosra "cart khaali" expect karke fail (maine ye real me dekha) |
| `requests` kyun? | Simple, browser se independent (API test bina browser ke chalte hain) |

> [!WARNING]
> `add_init_script` **har page load par** token set karta hai. Agar kisi test me **logout** karke login screen dekhna hai to is fixture ki jagah normal `page` use karo.

## ✅ Samjha?
<details>
<summary>1. <code>shop_api</code> me <code>clear_cart</code> <code>yield</code> ke baad kyun?</summary>

`yield` ke baad ka code **test ke baad** chalta hai (teardown), chaahe test pass ho ya fail. Cleanup test ke andar likhte to test fail hone par skip ho jaata.
</details>

<details>
<summary>2. API aur UI dono ko <b>ek hi token</b> kyun dena zaroori hai?</summary>

Taaki API me jo cart bana wahi UI me dikhe. Alag tokens = alag users = alag carts.
</details>

## ✍️ Khud karo
`tests/test_api_cart.py` me ek test jodo: naye user ka cart shuru me khaali hona chahiye (`shop_api.get_cart().json()["count"] == 0`).

<details>
<summary>✅ Jawab</summary>

```python
def test_cart_starts_empty(shop_api):
    assert shop_api.get_cart().json()["count"] == 0
```
</details>

🛟 Atak gaye? `solutions/step_08` (📖 optional: badi guide ka Part 10 aur 11)

---

# 🔵 Step 9: Rules ko test se enforce karo

## 🤕 Dikkat
Hum ne rule banaye: "tests me raw locator nahi", "pages me `requests` nahi". Par kal koi naya banda (ya tum khud, jaldi me) in rules ko **tod dega**. Koi rokega nahi.

## 💡 Idea
Rules ko **test** bana do. Rule toota to test red.

## ⌨️ Karo
**`tests/test_architecture.py`:**

**File: `tests/test_architecture.py`**
```python
import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _imported_modules(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module.split(".")[0])
    return names


def test_pages_do_not_import_requests_or_api():
    for path in (ROOT / "pages").glob("*.py"):
        bad = _imported_modules(path) & {"requests", "api"}
        assert not bad, f"{path.name} ne ye import kiya (pages me mana hai): {bad}"


def test_tests_do_not_use_raw_locators():
    pattern = re.compile(r"\.(locator|get_by_\w+)\(")
    offenders = []
    for path in (ROOT / "tests").glob("test_*.py"):
        if path.name == "test_architecture.py":
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if pattern.search(line):
                offenders.append(f"{path.name}:{number}: {line.strip()}")
    assert not offenders, "Tests me raw locator mila:\n" + "\n".join(offenders)
```

## ▶️ Chalao
```bash
pytest
```
**Aana chahiye:** `13 passed` (2 naye architecture tests)

## 🔍 Code samjho

| Line | Matlab |
|---|---|
| `ROOT = Path(__file__).resolve().parents[1]` | Ye file `tests/` me hai. `parents[1]` = project ka root |
| `ast.parse(...)` | Python file ko **code chalaye bina** padhna (syntax tree) |
| `isinstance(node, ast.Import)` / `ast.ImportFrom` | `import x` aur `from x import y` wali lines dhundho |
| `_imported_modules(path) & {"requests", "api"}` | File ke imports aur "mana wale" naamon ka **common** (set intersection) |
| `assert not bad, f"..."` | Kuch common mila to test fail aur message |
| `re.compile(r"\.(locator\|get_by_\w+)\(")` | Pattern: `.locator(` ya `.get_by_xxx(` |
| `if path.name == "test_architecture.py": continue` | Is file me khud ye pattern likha hai, isko skip |

## 🔬 Violation daal ke dekho (real run)
**1) `pages/login_page.py` me sabse upar `import requests` likh do:**
```text
AssertionError: login_page.py ne ye import kiya (pages me mana hai): {'requests'}
```
**2) `tests/test_shop.py` me raw locator likh do** (`page.get_by_role("button", name="Login").click()`):
```text
AssertionError: Tests me raw locator mila:
  test_shop.py:42: page.get_by_role("button", name="Login").click()
```
Dono me test **red** hua. Galti hatane par wapas green.

## 🧠 Kyun?
| Tareeka | Dikkat |
|---|---|
| Rule sirf README me | Koi padhta nahi ❌ |
| Code review par bharosa | Insaan thak jaata hai ❌ |
| **Rule ek test** (humne chuna) | apne aap chalta hai, rule toota to turant red ✅ |

## ✍️ Khud karo
Ek aur rule jodo: **tests me `time.sleep` nahi.** (Hint: `test_tests_do_not_use_raw_locators` jaisa hi, bas pattern `time.sleep` text ka.)

<details>
<summary>✅ Jawab</summary>

```python
def test_tests_do_not_sleep():
    offenders = []
    for path in (ROOT / "tests").glob("test_*.py"):
        if path.name == "test_architecture.py":
            continue
        if "time.sleep" in path.read_text(encoding="utf-8"):
            offenders.append(path.name)
    assert not offenders, f"time.sleep mat use karo: {offenders}"
```
</details>

🛟 Atak gaye? `solutions/step_09` (📖 optional: badi guide ka Part 14)

---

# 🏁 Step 10: Tumne kya banaya (review)

## Final folder
```text
start/
├── app_under_test/           ← demo shop (tumhara nahi)
├── core/base_page.py         ← Step 4
├── data/                     ← Step 5   (users.py, products.py)
├── pages/                    ← Step 2-4 (login, inventory, cart, order_complete)
├── flows/shopping_flow.py    ← Step 7
├── api/                      ← Step 8   (base_client, auth_api, shop_api)
├── tests/
│   ├── conftest.py           ← Step 6, 8  (fixtures)
│   ├── test_shop.py
│   ├── test_api_cart.py
│   ├── test_hybrid.py
│   └── test_architecture.py  ← Step 9
├── pytest.ini                ← Step 1 (config)
└── requirements.txt
```

## Har folder kyun? (ek line me)

| Folder | Kaam | Badlaav kab? |
|---|---|---|
| `pytest.ini` | URL, settings | Environment badle |
| `pages/` | Screens ke locators/actions | UI badle |
| `core/` | Sab pages ka common | Kabhi-kabhi |
| `data/` | Users, products | Data badle |
| `flows/` | Kai pages ka business action | Business flow badle |
| `api/` | Backend se baat | API badle |
| `tests/conftest.py` | Layers ko tests se jodna | Setup badle |
| `tests/test_*.py` | **Kya verify karna hai** | Requirement badle |

> [!IMPORTANT]
> **Yahi asli idea hai:** har cheez **alag wajah se badalti hai**, isliye har cheez ka alag ghar. Ek badlaav = ek jagah.

## Ek rule yaad rakho: "arrows neeche"
Upar wali cheez neeche wali ko use kar sakti hai, ulta nahi:

`tests → fixtures/flows → pages → core` aur `tests/fixtures → api, data`
**`pages` kabhi `tests` ya `api` ko import nahi karta.** (Step 9 isi ko check karta hai.)

## ✅ Apni jaanch

- [ ] Mai bata sakta hu ki URL badalne ke liye kitni jagah badalni padegi (1).
- [ ] Mai bata sakta hu ki locator badalne par kaunsi file badlegi (page).
- [ ] Mai `BasePage` me kya jaata hai aur kya nahi, bata sakta hu.
- [ ] Mai fixture aur flow ka fark bata sakta hu.
- [ ] Mai samajhta hu ki har test ka apna token kyun.
- [ ] Mai ek rule ko test se enforce kar sakta hu.

## 🧭 Ab apne `ex_6` par lagao (5 chhote kaam)

Pehle `ex_6` ko green karo (goto, DoD pura). Phir **ek-ek**, har kaam ke baad `pytest`:

1. **Config:** URL `pytest.ini` ke `base_url` me (Step 1).
2. **BasePage:** `open()` + `loaded_locator` (Step 4).
3. **Data:** users/products ko `data/` me (Step 5).
4. **Fixture:** login ki taiyari `conftest.py` me, **ek hi baar** (Step 6). (Tumhare `ex_6` me ye fixture 3 jagah copy tha.)
5. **Rules:** `test_architecture.py` (Step 9).

> SauceDemo ek frontend demo hai. Mujhe nahi pata (maine check nahi kiya) ki uske paas test-friendly API hai ya nahi. **Agar nahi hai to Step 7-8 (Flow aur API) abhi skip karo.** Wo practice is guide ke demo shop par ho chuki.

Code bhejoge to strict review milega (GOOD / WRONG / RISK / IMPROVEMENT).

## 📖 Badi guide kab kholni hai?

| Jab ye samajh na aaye | Badi guide ka part |
|---|---|
| Config / environments | Part 5 |
| Data layer | Part 6 |
| BasePage, steps | Part 7 |
| Pages vs components | Part 8 |
| Flows | Part 9 |
| API layer | Part 10 |
| Fixtures aur scopes | Part 11 |
| Architecture tests | Part 14 |
| "Ye code kahan jaayega?" | Part 15 |
| Interview ke sawaal | Part 17 |

**Components, evidence plugin, Allure** is path me jaan-boojh ke nahi aaye. Wo "aage" ki cheezein hain. Jab upar ke 6 steps pakke ho jayein tab.
