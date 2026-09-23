# Exercise 06 — Final Hard Integration Project
## Playwright + Pytest | Production-Style E-Commerce Workflow

> **Difficulty:** 🔴 Hard  
> **Estimated time:** 2–4 hours  
> **Application:** SauceDemo — https://www.saucedemo.com/  
> **Goal:** Combine the Playwright + Pytest concepts learned so far into one realistic, maintainable automation workflow.

---

## 🎯 Objective

This is the **final integration exercise** of the current Playwright practice track.

This is NOT about writing the maximum number of tests.

The challenge is to design a small but production-style automation solution where you decide:

- What belongs in a test?
- What belongs in a fixture?
- What should be reusable?
- Where should setup live?
- How should test data flow between layers?
- How do you keep tests independent?
- How do you validate UI behavior reliably?
- How would this framework behave when tests run independently or in parallel?

You are expected to make architectural decisions yourself.

---

## 🌐 Application

Use the real SauceDemo application:

`https://www.saucedemo.com/`

Standard user:

- Username: `standard_user`
- Password: `secret_sauce`

Do NOT use `example.com` or imaginary APIs.

---

# 🧠 Concepts Being Revised

This exercise intentionally combines:

### Playwright
- Page / Browser Context
- Semantic locators
- CSS selectors
- Locator scoping
- `filter()`
- Locator chaining
- `expect()`
- URL assertions
- `select_option()`
- Product cards
- Cart
- Product details
- Auto-waiting
- Test isolation

### Pytest
- Fixtures
- Fixture dependency
- `conftest.py`
- Fixture scope
- Assertions
- Parametrization
- Independent tests

### Automation Architecture
- Test responsibility
- Fixture responsibility
- Reusable UI logic
- Page Object / component decisions
- Test data
- Maintainability
- Debugging
- Failure investigation
- Parallel-safety thinking

---

# 🏗️ Project Requirement

Create a small automation project with a structure similar to:

```text
exercise_06/
│
├── tests/
│   └── test_checkout_workflow.py
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── conftest.py
├── pytest.ini
└── README.md
```

### Important

This structure is a **starting suggestion**, not a blind rule.

If you believe a different structure is better, use it.

You must be able to explain **why** you chose your structure.

Do NOT create unnecessary classes/files just to make the project look large.

---

# 🔐 Requirement 1 — Authentication

Create a reusable authenticated-page setup.

It must:

1. Open SauceDemo.
2. Login using `standard_user`.
3. Verify successful authentication.
4. Make the authenticated page available to tests.

Rules:

- Do not repeat login code in every test.
- Do not make one test depend on another test's login.
- Authentication setup belongs in the appropriate fixture/layer.

---

# 🛒 Requirement 2 — Product Selection

Create an independent workflow that:

1. Starts from an authenticated state.
2. Verifies the inventory page.
3. Locates **Sauce Labs Backpack**.
4. Verifies:
   - Product name
   - Price: `$29.99`
5. Adds the product to cart.

Use proper locator scoping.

Do NOT use `nth()` unless you can justify a genuine requirement.

---

# 🔽 Requirement 3 — Sorting Verification

Before selecting the product, apply:

**Price (low to high)**

Verify TWO things:

### A. Dropdown state

Verify that the expected sorting option is selected.

### B. Actual UI order

Collect the displayed product prices and verify that they are actually in ascending **numeric** order.

Do NOT verify sorting only by checking the dropdown value.

---

# 🛍️ Requirement 4 — Cart Validation

After adding the Backpack:

1. Open Shopping Cart.
2. Verify the correct product exists.
3. Verify the correct price exists.
4. Verify that the cart contains the expected product.

Do not rely only on a global text assertion if the page contains repeated product-related information.

Use appropriate locator scoping.

---

# 🧾 Requirement 5 — Checkout Workflow

Continue the workflow from the cart.

Use:

```text
First Name: Rajit
Last Name: Chauhan
Postal Code: 282001
```

Verify each important stage:

```text
Cart
 ↓
Checkout
 ↓
Customer Information
 ↓
Overview
 ↓
Finish
 ↓
Order Completion
```

The final state must be explicitly verified.

Do NOT simply click through the workflow without assertions.

---

# 🧪 Requirement 6 — Independent Tests

Your suite must contain **independent tests**.

A test must NOT assume another test has already:

- logged in
- added a product
- opened the cart
- completed checkout

For example:

```text
test_inventory
test_product_sorting
test_add_backpack_to_cart
test_checkout_backpack
```

Each test must establish the state it requires through fixtures/setup/workflow.

Do NOT create test-to-test dependencies.

---

# 🔄 Requirement 7 — Parametrization

Use `pytest.mark.parametrize` where it genuinely improves the test.

Create a small validation that checks multiple product-related data points.

For example, you may validate multiple products or multiple expected values.

Do not use parametrization merely because the exercise says so.

Use it where it makes the test:

- less repetitive
- easier to maintain
- clearer

You must be able to explain why parametrization is useful there.

---

# 🧩 Requirement 8 — Reusable Design

Make a conscious decision about where UI logic belongs.

Possible layers:

```text
Test
 ↓
Page Object / Component
 ↓
Playwright
```

and:

```text
Fixture
 ↓
Setup / Lifecycle
```

### Responsibility model

**Test:**
```text
WHAT should be verified?
```

**Page Object / Component:**
```text
HOW do I interact with the UI?
```

**Fixture:**
```text
HOW do I prepare the environment?
```

You may introduce Page Objects because this workflow is now large enough to justify reusable UI behavior.

But avoid abstractions that provide no real benefit.

---

# 🧹 Requirement 9 — Code Quality

Avoid:

- `time.sleep()`
- hardcoded arbitrary waits
- unnecessary `nth()`
- coordinate-based clicks
- JavaScript click hacks
- duplicated login code
- duplicated product-locator logic
- test-to-test dependencies
- unnecessary global mutable state
- giant test functions containing every implementation detail

Use Playwright's built-in waiting and assertion mechanisms.

---

# 🐛 Requirement 10 — Failure Investigation

Add enough structure so that when a test fails, it is reasonably easy to understand:

- Which test failed?
- At which workflow step?
- What UI element was involved?
- What value was expected?
- What value was actually observed?

You do NOT need to build a full enterprise logging framework.

Think practically.

---

# ⚙️ Requirement 11 — Production Thinking

While implementing, ask:

### Test design
> If this test fails, what exactly does the failure tell me?

### Fixture design
> Is this setup really fixture responsibility?

### Page Object design
> Is this UI interaction reused enough to justify abstraction?

### Locator design
> Will this locator survive a small UI change?

### Isolation
> Can this test run alone?

### Parallel execution
> Would another test changing the cart cause this test to fail?

### Maintainability
> If the login UI changes tomorrow, how many files must I modify?

---

# 🚫 Important Constraints

Do NOT:

- copy the entire previous exercise without thinking
- create unnecessary architecture
- create POM classes only because "production frameworks use POM"
- put business assertions randomly inside fixtures
- make fixtures responsible for the entire test
- use one test's result as another test's setup
- use `sleep()`
- use fragile dynamic locators
- hide important test logic inside giant helper functions

---

# ⭐ Bonus — Optional Challenge

If the core exercise works correctly, think about:

### Authentication optimization

How could you avoid performing UI login before every test?

Think about:

```text
storage_state
```

You do NOT have to implement this if you are not confident.

The purpose is to think about the trade-off between:

```text
simple fixture-based login
```

and:

```text
reusable authenticated state
```

---

# 📋 Definition of Done

- [ ] Authentication is reusable.
- [ ] Inventory is independently validated.
- [ ] Product sorting is applied.
- [ ] Dropdown sorting state is verified.
- [ ] Actual numeric product ordering is verified.
- [ ] Backpack is located using proper scoping.
- [ ] Backpack name and price are verified.
- [ ] Product is added to cart.
- [ ] Cart contents are verified.
- [ ] Checkout workflow is automated.
- [ ] Final order completion is verified.
- [ ] Tests are independent.
- [ ] Parametrization is used meaningfully.
- [ ] UI logic is appropriately organized.
- [ ] Fixtures have clear responsibility.
- [ ] No unnecessary `sleep()` / fragile waits.
- [ ] No unnecessary `nth()`.
- [ ] No test-to-test dependency.
- [ ] Project structure is maintainable.
- [ ] You can explain your architectural decisions.

---

# 📝 Submission Format

When you finish, DO NOT send only one code file.

Send:

## 1. Project structure

```text
exercise_06/
├── ...
```

## 2. `conftest.py`

Complete code.

## 3. Page Object / Component files

Complete relevant code.

## 4. Test files

Complete relevant code.

## 5. `pytest.ini`

If used.

## 6. Architecture explanation

Briefly explain:

- Why you chose this fixture structure.
- Why you chose this POM/component structure.
- Where test data lives.
- Why you used parametrization where you did.
- How tests remain independent.
- What would happen if tests ran in parallel.

## 7. Doubts

Write any doubts you encountered during implementation.

---

# 🧑‍🏫 Mentor Review Rules

After submission, the review will include:

### Overall verdict

Whether the implementation is actually production-oriented.

### Requirement-by-requirement review

Each requirement will be checked against the actual implementation.

### "Tumne ye kiya hai" vs "Ye karna chahiye tha"

For every meaningful issue:

```text
Tumne:
...

Ye karna chahiye tha:
...
```

### Code-level mistakes

Exact problems and why they matter.

### Corrected suggestions

When something is wrong, the correct approach/snippet will be shown.

### Architecture review

- Test responsibility
- Fixture responsibility
- POM/component responsibility
- Data flow
- Isolation
- Maintainability

### Strengths

What you are doing well.

### Weaknesses

Repeated mistakes and areas that still require work.

### Production assessment

How close your implementation is to real-world SDET automation practices.

### Final exercise status

```text
✅ Complete
🟡 Complete with improvements
❌ Not complete
```

---

# 🏁 Final Goal

The objective is NOT:

> "Write Playwright code that passes."

The objective is:

> **Design an automation solution that another SDET can understand, maintain, debug, extend, and safely execute independently.**

Take your time.

Do not look for the perfect architecture before starting.

Start with the requirements, make reasonable decisions, implement, run the tests, observe failures, and improve the design where necessary.

**That process itself is part of the exercise.**
