# Exercise 02 — Login and Add Product to Cart

> **Difficulty:** 🟡 Medium  
> **Category:** UI Automation  
> **Framework:** Pytest + Playwright  
> **Focus:** Authentication, locators, assertions, locator scoping, end-to-end workflow

---

## 🎯 Learning Objective

In this exercise, you will automate a realistic e-commerce workflow where a user:

1. Logs into the application.
2. Searches for a product.
3. Identifies the correct product from multiple products.
4. Adds that specific product to the cart.
5. Opens the cart.
6. Verifies that the correct product was added.

The primary goal is **not simply to make the test pass**.

You should write the automation in a way that is:

- readable
- maintainable
- reliable
- resistant to common locator problems
- suitable for a real automation project

---

## 🏢 Business Scenario

You are working as an SDET on an e-commerce application.

A customer must be able to log in, search for a product, add the required product to the shopping cart, and verify the cart contents.

The application contains multiple products, and every product has its own `Add to Cart` button.

For example:

```text
iPhone 15
Samsung Galaxy S25
Google Pixel 10
OnePlus 13
MacBook Air
...
```

Each product has its own:

```text
Product Name
Price
Add to Cart
```

Your automation must ensure that the **correct product's button** is clicked.

---

# 🧪 Test Scenario

Automate the following user journey:

```text
Open Application
       ↓
Login
       ↓
Verify Successful Login
       ↓
Search for "iPhone 15"
       ↓
Identify "iPhone 15" Product
       ↓
Verify Product Name
       ↓
Verify Product Price
       ↓
Add "iPhone 15" to Cart
       ↓
Open Cart
       ↓
Verify "iPhone 15" exists in Cart
       ↓
Verify Cart Product Price
```

---

# 📋 Functional Requirements

## 1. Open Application

Open the e-commerce application using the Playwright `page` fixture.

The application URL will be provided by the test environment.

---

## 2. Login

Use the following credentials:

| Field | Value |
|---|---|
| Email | `testuser@example.com` |
| Password | `Test@123` |

The login page contains:

```html
<label>Email</label>
<input type="email" aria-label="Email">

<label>Password</label>
<input type="password" aria-label="Password">

<button>Login</button>
```

Perform the login operation.

---

## 3. Verify Successful Login

After successful login, the application displays:

```html
<h1>Dashboard</h1>
```

Verify that the dashboard is visible before continuing with the product workflow.

---

## 4. Search for Product

Use the application's search functionality.

Search for:

```text
iPhone 15
```

The search UI contains:

```html
<input placeholder="Search">
<button>Search</button>
```

Execute the search.

---

## 5. Identify the Product

The search results may contain multiple product cards.

The relevant product has the following structure:

```html
<div class="product-card">
    <h3 class="product-name">iPhone 15</h3>
    <span class="price">$799</span>
    <button>Add to Cart</button>
</div>
```

Identify the product card belonging specifically to:

```text
iPhone 15
```

---

## 6. Verify Product Details

Inside the identified product card, verify:

### Product Name

```text
iPhone 15
```

### Product Price

```text
$799
```

Both values must be validated using appropriate Playwright assertions.

---

## 7. Add Product to Cart

Click the:

```text
Add to Cart
```

button belonging specifically to the **iPhone 15 product card**.

### Important

Do not accidentally interact with another product's `Add to Cart` button.

The page may contain many buttons with the same accessible name.

Your locator strategy must therefore correctly scope the action to the selected product.

---

## 8. Open Shopping Cart

After adding the product, open the shopping cart.

The cart control is represented by:

```html
<a aria-label="Shopping Cart">
    <span class="cart-count">1</span>
</a>
```

Open the cart using an appropriate locator.

---

## 9. Verify Cart Contents

The cart contains items using the following structure:

```html
<div class="cart-item">
    <span class="product-name">iPhone 15</span>
    <span class="price">$799</span>
</div>
```

Verify that:

- `iPhone 15` is present.
- The displayed price is `$799`.

---

# 🧩 Technical Requirements

Your implementation must satisfy the following requirements.

### Playwright

Use Playwright for browser automation and assertions.

### Pytest

The scenario must be implemented as a Pytest test.

### Locators

Prefer stable and meaningful locators.

Consider semantic locators and scoped locators where appropriate.

### Assertions

Use Playwright's assertion mechanism to validate expected application behavior.

### Waiting

Rely on Playwright's built-in waiting behavior where appropriate.

Do **not** use:

```python
time.sleep()
```

as a synchronization strategy.

### Locator Scoping

When interacting with the product, ensure that the action is scoped to the **iPhone 15 product card**.

### `nth()`

Avoid positional locators such as:

```python
nth()
```

unless there is a genuine requirement that cannot reasonably be solved using a more stable locator.

---

# 🏗️ Architecture Requirement

For this exercise, **POM is not mandatory**.

You must make the architecture decision yourself.

You may implement the scenario:

- directly inside the test, or
- using a small POM structure.

Do not introduce unnecessary abstractions merely to make the project look like a framework.

Your implementation should be appropriate for the size and complexity of the exercise.

Your architectural decision will be reviewed separately.

---

# 🚫 Restrictions

Do not:

- use `time.sleep()`
- use unnecessary explicit waits
- use fragile positional selectors unnecessarily
- click a generic `Add to Cart` button without correctly identifying the product
- skip meaningful assertions
- create unnecessary utility functions
- create unnecessary POM classes
- duplicate the same locator/action without a reason

---

# 💡 Engineering Considerations

While implementing the exercise, think about the following:

> What makes a locator stable?

> How can you ensure that the correct product is selected when several products have identical buttons?

> Which parts of the workflow represent actual business validations?

> When is POM useful, and when would it be unnecessary?

> Which assertions would provide meaningful failure information?

These are **thinking points**, not implementation instructions.

You are expected to make the final implementation decisions yourself.

---

# 📦 Expected Submission

Create the automation inside your Playwright practice project.

Submit:

### 1. Project Structure

Show the relevant folder/file structure.

Example:

```text
exercises/
└── 02-login-cart/
    ├── README.md
    └── test_login_cart.py
```

Your actual structure may be different.

### 2. Implementation

Submit the complete code you wrote.

### 3. Architecture Decision

State whether you used POM.

If yes, briefly explain why.

If no, briefly explain why.

### 4. Problems / Doubts

Mention anything you were unsure about while implementing the test.

---

# 🔎 Evaluation Criteria

Your implementation will be reviewed for:

| Area | Evaluation |
|---|---|
| Functional correctness | Required workflow works correctly |
| Locator strategy | Stable and meaningful locators |
| Locator scoping | Correct product targeted |
| Assertions | Business behavior properly validated |
| Waiting strategy | No unnecessary synchronization |
| Test design | Clear and focused test |
| POM decision | Appropriate abstraction level |
| Readability | Code is easy to understand |
| Maintainability | Changes can be made safely |
| Flakiness | Avoids common flaky patterns |
| Production suitability | Reasonable real-world approach |

---

# 🎤 Interview Relevance

**🟢 COMMON INTERVIEW**

This exercise covers concepts commonly discussed in SDET/automation interviews:

- Stable locators
- Semantic locators
- Locator chaining/scoping
- Assertions
- Auto-waiting
- Page Object Model
- Test maintainability
- End-to-end test design

---

# 🏭 Production Relevance

**🟡 PRACTICAL QA**

This exercise represents a simplified version of a common real-world workflow.

In production automation, similar patterns are used when testing:

- e-commerce applications
- order management systems
- booking applications
- CRM systems
- SaaS applications

The important engineering problem is not only performing the action, but ensuring that the automation interacts with and validates the **correct business entity**.

---

# ✅ Completion Criteria

The exercise is considered complete when:

- Login workflow is automated.
- Successful login is validated.
- Product search is automated.
- Correct product is identified.
- Product details are validated.
- Correct product is added to cart.
- Cart is opened.
- Correct cart item is validated.
- Price is validated.
- No unnecessary sleeps or fragile positional interactions are used.
- Code is readable and maintainable.