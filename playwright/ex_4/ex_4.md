# Exercise 04 — Fixture-Based Authentication and Multi-Test Isolation

> **Difficulty:** 🟡 Medium  
> **Category:** UI Automation / Pytest Architecture  
> **Framework:** Pytest + Playwright  
> **Application:** SauceDemo  
> **Focus:** Fixtures, authentication setup, test isolation, fixture scope, reusable setup

---

## 🎯 Learning Objective

In this exercise, you will practice designing reusable authentication setup with Pytest fixtures.

The goal is to move from:

```text
Every test
    ↓
Open application
    ↓
Enter username
    ↓
Enter password
    ↓
Click Login
```

towards:

```text
Authentication Fixture
        ↓
Authenticated Test
        ↓
Business Validation
```

You must decide how much responsibility belongs in the fixture and how much belongs in the test.

---

# 🌐 Application

Use:

**https://www.saucedemo.com/**

The application provides the following standard test credentials:

```text
Username: standard_user
Password: secret_sauce
```

These credentials are documented in Sauce Labs' own SauceDemo examples.

---

# 🏢 Business Scenario

You are working on an e-commerce automation suite.

Several tests need an authenticated user.

For example:

```text
Test 1 → Verify inventory
Test 2 → Add product to cart
Test 3 → Verify product details
```

Currently, every test would need to repeat the login workflow.

Your task is to design a reusable Pytest fixture so that authenticated tests do not unnecessarily duplicate the login steps.

---

# 🧪 Required Tests

Create **three independent tests**.

## Test 1 — Verify Inventory

An authenticated user should be able to access the inventory page.

Verify:

- User is successfully logged in.
- Inventory page is displayed.
- At least one product is visible.

---

## Test 2 — Add Product to Cart

An authenticated user should be able to add a product to the cart.

Use:

```text
Sauce Labs Backpack
```

Verify:

- Product is visible.
- Product can be added to cart.
- Cart reflects the added product.

---

## Test 3 — Verify Product Details

An authenticated user should be able to open a product and view its details.

Use:

```text
Sauce Labs Backpack
```

Verify:

- Product details page opens.
- Product name is visible.
- Product description is visible.
- Product price is visible.

---

# 🔐 Authentication Requirement

All three tests require an authenticated user.

You must avoid duplicating this login workflow in every test:

```text
Open application
    ↓
Enter username
    ↓
Enter password
    ↓
Click Login
```

Instead, design a reusable Pytest fixture.

---

# 🧩 Fixture Requirement

Create an authentication fixture responsible for preparing the browser for an authenticated test.

The fixture should:

1. Open the application.
2. Perform login.
3. Verify that login was successful.
4. Provide the authenticated `page` to the test.

The test should then start from the authenticated state.

---

# ⚠️ Important Responsibility Boundary

Think carefully about what belongs inside the fixture.

The fixture is responsible for:

```text
Environment / authentication setup
```

The test is responsible for:

```text
Business behavior / business validation
```

For example:

```text
Fixture
    ↓
Login
    ↓
Authenticated state
    ↓
Test
    ↓
Add product
    ↓
Validate cart
```

Do not put the actual business scenario into the authentication fixture.

---

# 🧪 Test Isolation Requirement

The three tests must be independently executable.

For example:

```bash
pytest test_authenticated_user.py::test_inventory
```

should work without requiring another test to run first.

Likewise:

```bash
pytest test_authenticated_user.py::test_add_product_to_cart
```

must not depend on:

```text
test_inventory
```

having executed previously.

---

# 🚫 Do Not Do

Do not create this dependency:

```text
test_login
    ↓
test_inventory
    ↓
test_add_product
```

Pytest tests should not depend on another test having already executed.

Also avoid:

- `time.sleep()`
- `nth()` when a stable locator is available
- Copy-pasting the complete login workflow into all three tests
- Putting product/cart business logic inside the authentication fixture
- Using global mutable state to share login state between tests

---

# 🏗️ Architecture Decision

You must decide where the fixture should live.

Possible choices include:

```text
test file
conftest.py
```

Choose based on the scope of reuse.

The authentication fixture is currently needed by multiple tests.

Your decision will be reviewed.

You do **not** need to create a large framework structure for this exercise.

---

# 🔎 Locator Expectations

Use stable locators wherever practical.

The application exposes useful semantic/accessibility information.

Prefer meaningful locators over brittle selectors.

You should be able to explain why you selected your locators.

---

# 🧠 Engineering Questions

You do not need to answer these before starting.

Use them to guide your implementation:

### Authentication

Should login be repeated in every test?

### Fixture

What exactly should the authentication fixture provide to the test?

### Scope

Should this fixture use:

```text
function
class
module
session
```

?

Choose based on the actual requirement rather than choosing a scope simply because it is available.

### Isolation

If two tests modify the cart, could one test affect another?

### Responsibility

Should the fixture know anything about:

```text
Sauce Labs Backpack
Cart
Product price
Product details
```

?

Or should those remain inside the tests?

---

# 📦 Expected Project Structure

You may choose your own structure.

For example:

```text
playwright-sdet-practice/
│
├── exercises/
│   └── 04-authentication-fixture/
│       ├── README.md
│       └── test_authenticated_user.py
│
└── conftest.py
```

This is only an example.

**Do not copy this structure blindly.**

Your architectural decision is part of the exercise.

---

# 📋 Expected Submission

Submit:

## 1. Project Structure

Show the relevant folders and files.

## 2. Complete Code

Submit all files you created or modified for this exercise.

## 3. Fixture Decision

Explain:

- Where you placed the fixture.
- What fixture scope you selected.
- Why you selected that scope.

## 4. Design Notes

Briefly explain:

- What the fixture is responsible for.
- What the tests are responsible for.
- How you kept tests independent.

## 5. Problems / Doubts

Mention anything you were unsure about during implementation.

---

# 🔎 Review Criteria

Your implementation will be reviewed for:

### Playwright

- Locator quality
- Assertions
- Waiting strategy
- Browser/page usage

### Pytest

- Fixture design
- Fixture scope
- Fixture dependency
- Test independence
- `conftest.py` usage

### Architecture

- Responsibility boundaries
- Duplication
- Maintainability
- Appropriate abstraction

### Production Thinking

- Parallel safety
- Test isolation
- State leakage
- Authentication strategy
- Future scalability

---

# 🎤 Interview Relevance

**🟢 COMMON INTERVIEW**

This exercise covers:

- What is a Pytest fixture?
- Why use fixtures?
- Fixture scope
- `conftest.py`
- Fixture vs test responsibility
- Test independence
- Authentication setup
- Why tests should not depend on execution order

---

# 🏭 Production Relevance

**🔴 PRODUCTION**

Authentication setup is one of the most common reusable pieces in UI automation frameworks.

The important engineering problem is not merely:

> "How do I login?"

It is:

> "How do I make authentication reusable without creating state leakage, unnecessary duplication, or test dependencies?"

---

# ✅ Completion Criteria

The exercise is complete when:

- Three tests are implemented.
- All three can run independently.
- Login is not unnecessarily duplicated.
- Authentication is handled through a fixture.
- Fixture responsibility is limited to authentication/setup.
- Business validations remain inside tests.
- Appropriate fixture scope is selected and justified.
- No unnecessary waits are used.
- Locators are reasonably stable.
- Tests do not depend on execution order.