Bilkul bhai. 🔥 **Ye actually better rahega.** Aage se jab tum bolo “MD bana do”, main **direct copy-paste-ready Markdown text** dunga, jab tak tum specifically downloadable `.md` file na bolo.

Aur format **pichhli Python notes wali style** jaisa hi rakhenge — clean, premium, visual, emojis/callouts/code blocks/tables/collapsible sections etc.

Neeche **Exercise #3 ka complete copy-paste-ready `.md`** hai:

````md
# 🔥 Exercise #3 — API Setup + UI Validation

> **Difficulty:** 🟡 Medium  
> **Type:** API + UI Automation  
> **Tools:** Pytest + Playwright + `requests`  
> **Focus:** API setup, UI validation, test-data strategy, separation of responsibilities

---

## 🎯 Objective

A user should be able to view an order that already exists in the system.

Tumhe **API ka use test data/setup ke liye** karna hai aur **UI ka use actual user-facing behavior validate karne ke liye**.

### 🔄 Expected Flow

```text
API
 ↓
Create Order
 ↓
UI
 ↓
Login
 ↓
Open Orders
 ↓
Find Created Order
 ↓
Validate Order Details
````

---

# 🏢 Business Scenario

E-commerce application mein order manually UI se create karna possible hai.

Lekin automation suite mein har test ke liye UI se order create karna unnecessary time consume karta hai.

SDET ke taur par tum decide karte ho:

> 💡 **Order creation API ke through setup karenge, aur UI ke through order visibility/details validate karenge.**

### 🤔 Why API for Setup?

UI se order create karne mein multiple steps ho sakte hain:

```text
Login
 ↓
Product Search
 ↓
Add Product
 ↓
Cart
 ↓
Checkout
 ↓
Address
 ↓
Payment
 ↓
Place Order
```

Agar humein sirf **order visibility** test karni hai, toh ye unnecessary UI steps hain.

Instead:

```text
API → Create required test data
             ↓
UI  → Validate actual user-facing behavior
```

---

# 📋 Requirements

## 1️⃣ Create Test Order Through API

Test ke setup phase mein API request ke through ek new order create karo.

### 🧪 Test Data

```text
Customer: Rajit
Product: iPhone 15
Quantity: 2
Price per item: $799
```

API response se generated:

```text
order_id
```

capture karo.

---

## 2️⃣ Login Through UI

Application ko browser mein open karo.

Login karo using the application's valid test credentials.

Login successful hone ke baad dashboard/home page verify karo.

---

## 3️⃣ Navigate to Orders

UI ke through user's orders section open karo.

---

## 4️⃣ Find the Created Order

Orders page par multiple orders ho sakte hain.

Example:

```text
ORD-998
ORD-999
ORD-1000
ORD-1001
...
```

API se create kiya hua **dynamic `order_id`** use karke correct order identify karo.

> ⚠️ **Hard-coded order ID use nahi karna hai.**

---

## 5️⃣ Validate Order

UI par API se created order ke andar verify karo:

| Field       | Expected Value         |
| ----------- | ---------------------- |
| 🆔 Order ID | API-created `order_id` |
| 👤 Customer | `Rajit`                |
| 📱 Product  | `iPhone 15`            |
| 🔢 Quantity | `2`                    |
| 💵 Price    | `$799`                 |

---

# 6️⃣ Test Isolation

Test ko is assumption par depend nahi karna chahiye ki database mein pehle se koi specific order available hai.

Har test execution mein required order:

```text
API
 ↓
Create fresh order
 ↓
Capture order_id
 ↓
UI validation
```

hona chahiye.

### 🎯 Goal

Test:

```text
Run #1 → Create Order A → Validate A
Run #2 → Create Order B → Validate B
Run #3 → Create Order C → Validate C
```

Existing database state par depend nahi kare.

---

# 🌐 Test Application / API

Is exercise ke liye **JSONPlaceholder** ko API backend aur **SauceDemo** ko UI application ki tarah combine mat karna.

❌ Woh real integration nahi hoga.

Instead, is exercise ko apne practice project mein **mock/test API contract** ke against implement karo.

---

# 🔌 API Contract

## Create Order

```http
POST /api/orders
```

### 📤 Request

```json
{
  "customer": "Rajit",
  "product": "iPhone 15",
  "quantity": 2,
  "price": 799
}
```

### 📥 Response

```json
{
  "order_id": "ORD-1001",
  "customer": "Rajit",
  "product": "iPhone 15",
  "quantity": 2,
  "price": 799
}
```

> ⚠️ **Important**
>
> Ye API contract exercise ke liye provided contract hai.
>
> Agar tumhare local practice application/API mein endpoint ya response structure different hai, apne actual environment ke according adapt karna.

---

# 🧩 UI Information

Orders page ka relevant structure:

```html
<div class="order-card">
    <span class="order-id">ORD-1001</span>
    <span class="customer">Rajit</span>
    <span class="product">iPhone 15</span>
    <span class="quantity">2</span>
    <span class="price">$799</span>
</div>
```

Multiple order cards ho sakte hain:

```text
ORD-998
ORD-999
ORD-1000
ORD-1001
...
```

Tumhe **API se returned order ID** ke basis par correct order identify karna hai.

---

# 🔧 Technical Constraints

### ✅ Must Use

* Pytest
* Playwright
* Python `requests` for API setup

### 🚫 Rules

* Hard-coded order ID use mat karo.
* Existing database/order data par depend mat karo.
* `time.sleep()` use mat karo.
* `nth()` avoid karo.
* Stable/scoped locators prefer karo.
* API response se generated `order_id` capture karo.
* UI validation API response ke data ke against karo.
* API interaction aur UI interaction ki responsibilities clearly separate rakho.
* Test ko deterministic rakhne ki koshish karo.

---

# 🏗️ Architecture Decision

Is exercise mein tumhe **khud architecture decide karna hai.**

Main tumhe koi fixed structure nahi de raha.

Tum decide karo:

### ❓ API Call

```text
Test ke andar direct request?
```

ya

```text
Separate API Client?
```

---

### ❓ Test Data

```text
Dictionary?
```

ya

```text
Dataclass?
```

ya

```text
Fixture?
```

---

### ❓ Setup

```text
Fixture?
```

ya

```text
Test method?
```

---

### ❓ UI

```text
Direct Playwright code?
```

ya

```text
Page Object Model?
```

---

### ❓ Cleanup

Socho:

```text
Order create hua
       ↓
Test complete
       ↓
Order ka kya hoga?
```

Kya cleanup required hai?

Agar haan:

```text
POST → Create
 ↓
UI → Validate
 ↓
DELETE → Cleanup
```

Agar cleanup nahi karoge, toh reason justify karna.

---

# 🧠 Important Engineering Principle

> **Kisi particular architecture ko blindly follow mat karo.**

Exercise ka important part hai:

> ## 🎯 Requirement dekh kar appropriate abstraction choose karna.

Main review mein sirf ye nahi dekhunga ki:

```text
❌ Test pass ho raha hai ya nahi
```

Main ye bhi dekhunga:

```text
✅ Why did you choose this architecture?
✅ Is the abstraction useful?
✅ Is anything unnecessarily complex?
```

---

# 🚫 Don't Do

```text
❌ Hard-code ORD-1001

❌ UI se order create karke
   phir UI se same order validate karna

❌ Existing order assume karna

❌ API response ignore karna

❌ API setup aur UI validation ko
   unnecessarily mix karna

❌ time.sleep()

❌ nth() just because it is convenient
```

---

# 💡 Engineering Thinking

Implementation se pehle in questions par socho.

### 1️⃣ Test Data

> Test data API se create karne ka benefit kya hai?

---

### 2️⃣ Dynamic ID

> `order_id` ko test ke different parts mein kaise pass karoge?

Example:

```text
API Response
     ↓
 order_id
     ↓
Fixture / Test
     ↓
Orders Page
     ↓
Find Order
```

---

### 3️⃣ API Client

> API client ki zarurat hai ya direct request sufficient hai?

Socho:

```python
requests.post(...)
```

vs.

```python
order_api.create_order(...)
```

Kaunsa abstraction **is exercise ke scale par justified** hai?

---

### 4️⃣ POM

> POM ka responsibility kya hoga?

POM ko:

```text
API call
```

karni chahiye?

Ya:

```text
UI interaction
```

tak limited rehna chahiye?

---

### 5️⃣ Assertions

API response validation aur UI validation mein kya difference hai?

```text
API Assertion
      ↓
Did backend create correct data?

UI Assertion
      ↓
Does user see correct data?
```

---

### 6️⃣ Parallel Execution

Agar test parallel mein 5 times run ho:

```text
Test A → Order ?
Test B → Order ?
Test C → Order ?
Test D → Order ?
Test E → Order ?
```

Toh orders clash kaise avoid karoge?

---

### 7️⃣ Cleanup

Test fail hone par:

```text
API-created order
```

ka kya hoga?

---

> 🧠 **Ye questions answer karke submit karna mandatory nahi hai.**
>
> Ye sirf implementation ke time tumhari engineering thinking guide karne ke liye hain.

---

# 📦 Submission

Git project mein exercise ko apni preferred structure ke according implement karo.

Submit:

```text
Exercise: #3

Project Structure:
<folder/file structure>

Files:
<files changed>

Code:
<complete relevant code>

Architecture:
<POM / Fixture / API Client etc.>

Reason:
<short explanation>

Problems/Doubts:
<anything you faced>
```

---

# 🔎 Review Focus

Main specially review karunga:

### 🏗️ Architecture

* API/UI separation
* Fixture responsibility
* POM responsibility
* API client responsibility
* Whether abstraction is justified
* Whether solution is over-engineered

### 🧪 Test Design

* Test-data isolation
* Dynamic order ID handling
* Deterministic execution
* Parallel safety
* Cleanup strategy

### 🎭 Playwright

* Locator strategy
* Scoped locators
* Avoiding unnecessary `nth()`
* Proper assertions
* Waiting strategy

### 🌐 API

* Correct request construction
* Response handling
* Status-code validation
* Response data extraction
* Error handling

---

# 🎤 Interview Relevance

## 🟡 PRACTICAL QA

### Topics Covered

* API + UI automation
* Test data creation through API
* API vs UI responsibility
* Dynamic test data
* Fixtures
* POM
* End-to-end validation
* Test isolation
* Cleanup

---

# 🏭 Production Relevance

## 🔴 PRODUCTION

Real automation frameworks mein API ko test-data setup ke liye use karna aur UI ko business/user-facing behavior validate karne ke liye use karna ek important pattern hai.

Typical flow:

```text
API
 ↓
Prepare Test Data
 ↓
UI
 ↓
Perform User Action
 ↓
UI Assertions
```

Isse UI test ko unnecessary setup steps perform nahi karne padte.

---

# ⚠️ One Important Note

Is exercise ka **API contract intentionally provided hai**, lekin actual executable backend tumhe apne practice environment mein available/implement karna padega.

Agar tumhare paas suitable API environment nahi hai:

> **Code likhne se pehle mujhe bata dena.**

Main task ko real executable practice environment ke according adjust kar dunga.

---

# 🧑‍💻 Exercise Rules

## 🚫 No Solution

**Abhi solution nahi milega.**

Tumhe khud implementation karna hai.

---

## 🧠 Ask When Stuck

Agar implementation ke beech mein doubt aaye, pehle apna **thought/process** batao.

Example:

> "Main fixture use karne ka soch raha hoon because..."

Main mentor ki tarah bataunga:

```text
🟢 Good approach
🟡 Think about this
🔴 Change this
```

Lekin main bina zarurat tumhara **complete solution/code** nahi likhunga.

---

# 🏁 Final Challenge

Before submitting, make sure your test can conceptually achieve:

```text
          ┌──────────────────┐
          │   Create Order   │
          │      via API     │
          └────────┬─────────┘
                   │
                   ▼
             order_id
                   │
                   ▼
          ┌──────────────────┐
          │    Login via UI  │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │   Open Orders    │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ Find order_id    │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ Validate Details │
          └──────────────────┘
```

---

<div align="center">

# 🚀 Now Build Exercise #3

### Think → Design → Implement → Test → Submit

🔥 **SDET mindset > Just making the test pass**

</div>
```

**Aage se exactly isi style mein** exercise/notes ka Markdown text de dunga — tum bas **copy → `.md` file → paste** kar dena.
