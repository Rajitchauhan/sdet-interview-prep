😂 Haan bhai, **ab 100% samajh gaya.**
Tumhe **Exercise #3 jo tumne upar paste ki thi**, usi ka `.md` chahiye — **Word/Python notes wali file ka nahi**.

Aur tumhara main point ye hai ki **Markdown code ko outer code block mein nahi daalna**, warna copy karne par nested ``` ki wajah se khichdi ban jaati hai.

Isliye main ab **direct Markdown content** de raha hoon. Is response ke **is section ko copy karke `.md` file mein paste** kar sakte ho:

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

---

## 🏢 Business Scenario

E-commerce application mein order manually UI se create karna possible hai.

Lekin automation suite mein har test ke liye UI se order create karna unnecessary time consume karta hai.

SDET ke taur par tum decide karte ho:

> 💡 **Order creation API ke through setup karenge, aur UI ke through order visibility/details validate karenge.**

### 🤔 Why API for Setup?

UI se order create karne mein multiple steps ho sakte hain:

**Login → Product Search → Add Product → Cart → Checkout → Address → Payment → Place Order**

Agar humein sirf **order visibility** test karni hai, toh ye unnecessary UI steps hain.

Instead:

**API → Create required test data → UI → Validate actual user-facing behavior**

---

# 📋 Requirements

## 1️⃣ Create Test Order Through API

Test ke setup phase mein API request ke through ek new order create karo.

### 🧪 Test Data

| Field          | Value       |
| -------------- | ----------- |
| Customer       | `Rajit`     |
| Product        | `iPhone 15` |
| Quantity       | `2`         |
| Price per item | `$799`      |

API response se generated:

`order_id`

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

* `ORD-998`
* `ORD-999`
* `ORD-1000`
* `ORD-1001`
* ...

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

## 6️⃣ Test Isolation

Test ko is assumption par depend nahi karna chahiye ki database mein pehle se koi specific order available hai.

Har test execution mein required order **API se create** hona chahiye.

Expected flow:

**API → Create fresh order → Capture `order_id` → UI validation**

### 🎯 Goal

Run #1 → Create Order A → Validate A
Run #2 → Create Order B → Validate B
Run #3 → Create Order C → Validate C

Existing database state par depend nahi kare.

---

# 🌐 Test Application / API

Is exercise ke liye **JSONPlaceholder** ko API backend aur **SauceDemo** ko UI application ki tarah combine mat karna — woh real integration nahi hoga.

Instead, is exercise ko apne practice project mein **mock/test API contract** ke against implement karo.

---

# 🔌 API Contract

## Create Order

**HTTP Method:** `POST`

**Endpoint:**

`/api/orders`

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

> ⚠️ **Important:** Ye API contract exercise ke liye provided contract hai. Agar tumhare local practice application/API mein endpoint ya response structure different hai, apne actual environment ke according adapt karna.

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

* `ORD-998`
* `ORD-999`
* `ORD-1000`
* `ORD-1001`
* ...

Tumhe **API se returned order ID** ke basis par correct order identify karna hai.

---

# 🔧 Technical Constraints

### ✅ Must Use

* Pytest
* Playwright
* Python `requests` for API setup

### 🚫 Rules

* ❌ Hard-coded order ID use mat karo.
* ❌ Existing database/order data par depend mat karo.
* ❌ `time.sleep()` use mat karo.
* ❌ `nth()` use mat karo just because convenient hai.
* ✅ Stable/scoped locators prefer karo.
* ✅ API response se generated `order_id` capture karo.
* ✅ UI validation API response ke data ke against karo.
* ✅ API interaction aur UI interaction ki responsibilities clearly separate rakho.
* ✅ Test ko deterministic rakhne ki koshish karo.

---

# 🏗️ Architecture Decision

Is exercise mein tumhe **khud architecture decide karna hai**.

Tum decide karo:

### 🌐 API Call

* API call test ke andar directly?
* Ya separate API client?

### 🧪 Test Data

* Dictionary?
* Dataclass?
* Fixture?
* Kuch aur?

### ⚙️ Setup

* Fixture?
* Test method?
* Separate helper?

### 🎭 UI

* Direct Playwright code?
* Page Object Model?

### 🧹 Cleanup

Socho:

**Create Order → Test Complete → Order ka kya hoga?**

Kya cleanup required hai?

Agar haan:

**POST → Create → UI Validate → DELETE → Cleanup**

Agar cleanup nahi karoge, toh reason justify karna.

> 🧠 **Kisi particular architecture ko blindly follow mat karo.**

Exercise ka important part hai:

> **Requirement dekh kar appropriate abstraction choose karna.**

---

# 🚫 Don't Do

* ❌ Hard-code `ORD-1001`
* ❌ UI se order create karke phir UI se same order validate karna
* ❌ Existing order assume karna
* ❌ API response ignore karna
* ❌ API setup aur UI validation ko unnecessarily mix karna
* ❌ `time.sleep()`
* ❌ `nth()` just because it is convenient

---

# 💡 Engineering Thinking

Implementation se pehle socho:

### 1️⃣ Test Data

**Test data API se create karne ka benefit kya hai?**

---

### 2️⃣ Dynamic ID

**`order_id` ko test ke different parts mein kaise pass karoge?**

Expected thinking:

API Response
↓
`order_id`
↓
Fixture / Test
↓
Orders Page
↓
Find Order

---

### 3️⃣ API Client

**API client ki zarurat hai ya direct request sufficient hai?**

Compare:

`requests.post(...)`

vs.

`order_api.create_order(...)`

Kaunsa abstraction **is exercise ke scale par justified** hai?

---

### 4️⃣ POM

**POM ki responsibility kya hogi?**

POM ko API call karni chahiye?

Ya POM ko sirf:

> 🎭 **UI interaction**

tak limited rehna chahiye?

---

### 5️⃣ Assertions

API response validation aur UI validation mein kya difference hai?

**API Assertion**

Backend ne correct data create kiya?

**UI Assertion**

User ko correct data visible ho raha hai?

---

### 6️⃣ Parallel Execution

Agar test parallel mein 5 times run ho:

* Test A → Order ?
* Test B → Order ?
* Test C → Order ?
* Test D → Order ?
* Test E → Order ?

Toh orders clash kaise avoid karoge?

---

### 7️⃣ Cleanup

Test fail hone par API-created order ka kya hoga?

---

> 💡 **Ye questions answer karke submit karna mandatory nahi hai.**
> Ye sirf implementation ke time tumhari engineering thinking guide karne ke liye hain.

---

# 📦 Submission

Git project mein exercise ko apni preferred structure ke according implement karo.

### Submit

**Exercise:** `#3`

**Project Structure:**

Project ka folder/file structure provide karo.

**Files:**

Changed files ki list provide karo.

**Code:**

Complete relevant code provide karo.

**Architecture:**

POM / Fixture / API Client etc.

**Reason:**

Short explanation ki architecture kyun choose kiya.

**Problems/Doubts:**

Implementation ke during jo problems ya doubts aaye.

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

**API → Prepare Test Data → UI → Perform User Action → UI Assertions**

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

🟢 **Good approach**
🟡 **Think about this**
🔴 **Change this**

Lekin bina zarurat tumhara **complete solution/code** nahi likhunga.

---

# 🏁 Final Challenge

Before submitting, make sure your test conceptually achieve karta hai:

**Create Order via API**
↓
**Capture dynamic `order_id`**
↓
**Login via UI**
↓
**Open Orders**
↓
**Find `order_id`**
↓
**Validate Order Details**

---

<div align="center">

# 🚀 Now Build Exercise #3

### Think → Design → Implement → Test → Submit

🔥 **SDET mindset > Just making the test pass**

</div>
