# Exercise 05 — Product Sorting, Selection & Cart Validation

> **Difficulty:** Medium  
> **Estimated Time:** 60–90 minutes  
> **Application:** SauceDemo  
> **Goal:** Practice dropdown handling, locator strategy, assertions, and maintaining a clean test flow after authentication.

---

## 1. Objective

In this exercise, you will extend the authentication knowledge from Exercise 04 and practice a realistic e-commerce workflow.

You will automate a scenario where an authenticated user:

1. Logs in.
2. Changes product sorting.
3. Verifies that the sorting was applied.
4. Selects a specific product.
5. Adds the product to the cart.
6. Opens the cart.
7. Verifies that the correct product and price are present.

The main purpose is **not just to make the test pass**.

You should practice making deliberate decisions about:

- locator selection
- dropdown handling
- assertions
- test responsibility
- fixture reuse
- avoiding brittle selectors
- validating actual application state

---

# 2. Application

Use the real SauceDemo application:

`https://www.saucedemo.com/`

Use:

- **Username:** `standard_user`
- **Password:** `secret_sauce`

---

# 3. Requirements

## Authentication

Reuse the authentication approach from Exercise 04.

Create/use an authentication fixture that:

- opens SauceDemo
- logs in
- verifies successful authentication
- provides an authenticated `Page` to the test

Do **not** repeat the login steps directly inside the test.

---

# 4. Test Scenario

Create the following test:

### `test_sort_product_and_add_to_cart`

The test should perform this workflow:

```text
Login
  ↓
Inventory page
  ↓
Change product sorting
  ↓
Verify sorting
  ↓
Locate Sauce Labs Backpack
  ↓
Verify product information
  ↓
Add Backpack to cart
  ↓
Open Shopping Cart
  ↓
Verify Backpack exists in cart
  ↓
Verify price
```

---

# 5. Sorting Requirement

On the inventory page, locate the product sorting dropdown.

Change the sorting to:

> **Price (low to high)**

Use Playwright's appropriate dropdown API.

Do not click random coordinates or use keyboard hacks.

---

# 6. Sorting Verification

After selecting **Price (low to high)**, verify that the sorting was actually applied.

You should not merely perform:

```python
select_option(...)
```

and assume the application worked.

The test must contain an assertion proving that the expected sorting option is selected.

Think about which assertion would best validate the dropdown's state.

---

# 7. Product Requirement

After sorting:

Locate:

> **Sauce Labs Backpack**

Use a stable locator strategy.

You should preferably scope the product-related actions to the product's container/card rather than globally searching for generic elements such as:

```text
Add to cart
$29.99
```

---

# 8. Product Validation

Before adding the product to the cart, verify:

- Product name is visible.
- Product price is visible.

Expected price:

> `$29.99`

---

# 9. Add to Cart

Add **Sauce Labs Backpack** to the cart.

Avoid:

- `nth()` unless genuinely required
- `time.sleep()`
- coordinate-based clicking
- JavaScript click hacks

Prefer semantic and scoped locators.

---

# 10. Cart Validation

Open the Shopping Cart.

Verify:

- Sauce Labs Backpack is present.
- Price is `$29.99`.

The test should verify the **cart state**, not merely that clicking the button completed without an exception.

---

# 11. Important Locator Requirement

Do NOT solve the exercise by relying on fragile selectors such as:

```python
div:nth-child(3)
```

or:

```python
.inventory_item:nth-child(1)
```

or:

```python
button:nth-child(...)
```

You should make the locator communicate **which product** you are working with.

For example, the general strategy should be:

```text
Product container
      ↓
Sauce Labs Backpack
      ↓
Product-specific action
```

You are expected to decide the exact locator implementation.

---

# 12. Test Design Requirements

Your test should be:

- independent
- readable
- deterministic
- maintainable
- free from unnecessary waits

Do not create unnecessary POM classes for this exercise.

The exercise is still small enough that a test + fixture structure is sufficient.

---

# 13. Suggested Structure

You may use:

```text
playwright-sdet-practice/
└── exercises/
    └── 05-sorting-and-cart/
        ├── README.md
        └── test_sorting_and_cart.py
```

You are free to choose a different structure if you have a good reason.

---

# 14. What You Are Expected to Practice

This exercise is specifically testing your ability to use:

### Playwright

- `select_option()`
- locators
- locator chaining/scoping
- `filter()`
- `expect()`
- dropdown assertions
- product-specific actions
- cart validation

### Pytest

- fixtures
- fixture dependency
- test isolation

### Test Design

- separating setup from business validation
- choosing stable locators
- validating application state
- avoiding unnecessary implementation details

---

# 15. Common Mistakes to Avoid

### Mistake 1 — Selecting an option without verifying it

Bad:

```python
page.locator("select").select_option("lohi")
```

and then immediately continuing without an assertion.

---

### Mistake 2 — Global Add to Cart locator

Avoid blindly doing:

```python
page.get_by_role("button", name="Add to cart").click()
```

when multiple products have the same button.

First identify the correct product.

---

### Mistake 3 — Using `nth()` just to make the test work

Avoid:

```python
page.get_by_role("button", name="Add to cart").nth(0).click()
```

The first product today may not remain the first product tomorrow.

---

### Mistake 4 — Validating only the inventory page

The important business result is:

```text
Product selected
      ↓
Added to cart
      ↓
Correct product exists in cart
```

So validate the final cart state.

---

### Mistake 5 — `time.sleep()`

Do not use:

```python
time.sleep(2)
```

Playwright's auto-waiting and assertions should handle synchronization.

---

# 16. Engineering Thinking

Before coding, think about these questions.

These are **thinking prompts**, not questions you need to submit separately.

### A. Dropdown

How would you know whether this is a native `<select>` element or a custom dropdown?

### B. Locator

Why is product-card scoping safer than a global `Add to cart` locator?

### C. Assertion

What is the difference between:

```python
select_option()
```

and verifying that the selected option is actually active?

### D. Test Responsibility

Why should this test validate the final cart state instead of stopping immediately after clicking Add to Cart?

### E. Maintainability

If Sauce Labs Backpack moves from the first product to the fifth product, should your test break?

If yes, ask yourself why.

---

# 17. Production Perspective

Imagine this is a real e-commerce application.

A tester reports:

> "The sorting dropdown accepts the selection, but the product list does not actually change."

A weak automation test may pass because it only performs:

```text
select option
```

A stronger automation test verifies the resulting application state.

This exercise is therefore teaching an important principle:

> **An automation test should validate behavior, not merely execute actions.**

---

# 18. Interview Connection

You should be able to explain these concepts after completing the exercise:

### `select_option()`

What is it used for?

When is it appropriate?

What would you do if the dropdown is not a native `<select>`?

### Locator scoping

Why should repeated elements such as "Add to cart" be scoped to a product container?

### Assertions

Why do we verify the selected sorting option after selecting it?

### Test independence

Why should this test not depend on another test having already added a product?

---

# 19. Definition of Done

Exercise 05 is complete when:

- [ ] Authentication is handled through a fixture.
- [ ] Login success is verified.
- [ ] Inventory page is reached.
- [ ] Product sorting is changed to Price (low to high).
- [ ] Sorting selection is verified.
- [ ] Sauce Labs Backpack is located using a stable strategy.
- [ ] Product name is verified.
- [ ] Product price is verified.
- [ ] Backpack is added to the cart.
- [ ] Shopping Cart is opened.
- [ ] Backpack is verified in the cart.
- [ ] Cart price is verified.
- [ ] No `time.sleep()` is used.
- [ ] No unnecessary `nth()` is used.
- [ ] No test depends on another test.
- [ ] Locators are readable and maintainable.

---

# 20. Submission Format

When you finish, submit:

### 1. Project structure

```text
exercises/
└── 05-sorting-and-cart/
    ├── README.md
    └── test_sorting_and_cart.py
```

### 2. Complete relevant code

Paste the complete test file.

### 3. Your design decisions

Briefly explain:

- Why you chose your dropdown locator.
- Why you chose your product locator.
- How you verified sorting.
- How you verified the cart.
- Any part where you were unsure.

### 4. Problems/Doubts

If something confused you while implementing the exercise, write it down.

---

# Mentor Rule

**Do not look for a ready-made solution before attempting the exercise.**

The objective is not to memorize Playwright syntax.

The objective is to develop the ability to look at a real application and decide:

```text
What do I need to verify?
        ↓
What state should the application be in?
        ↓
Which locator represents that state?
        ↓
What assertion proves it?
        ↓
How do I keep the test maintainable?
```

After your submission, the review will include:

- Overall verdict
- What you did vs what should have been done
- Exact mistakes
- Corrected code/suggestions
- Strengths
- Weaknesses/repeated mistakes
- Production-level assessment
- Exercise status
