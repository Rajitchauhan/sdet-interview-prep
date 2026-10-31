# 🚀 Module 5 --- AI-Assisted Playwright Automation with GitHub Copilot & Playwright MCP

## Python + Pytest + Playwright Python \| Hinglish Mentor Study Guide

> **Source reviewed:** Uploaded `module_5.zip`. It contains six lesson
> transcripts in `.txt` and matching English `.vtt` subtitle files. The
> `.txt` and `.vtt` versions are duplicate lesson content, so they have
> been consolidated rather than repeated.
>
> **Course demonstration stack:** VS Code, GitHub Copilot, Playwright
> MCP, Playwright Test with TypeScript, a local pizza-store application
> on `localhost:3000`.
>
> **Your learning stack:** Python, Pytest, Playwright Python.
>
> **Important:** The course demonstrates the workflows in TypeScript.
> This guide preserves what the instructor demonstrates, then translates
> the underlying ideas into Python + Pytest + Playwright Python. The
> Python examples are mentor adaptations, not code copied from the
> course. The uploaded ZIP contains no Module 4 lesson files and no
> separate written PDF for this module.

------------------------------------------------------------------------

# 🗺️ Module overview

This module moves from using AI to discuss testing into using an AI
coding assistant inside an actual automation project.

  -----------------------------------------------------------------------
  Lesson                  Source lesson           Main skill
  ----------------------- ----------------------- -----------------------
  5.1                     Generate a testing      Let Copilot inspect an
                          strategy                application and draft
                                                  an E2E strategy

  5.2                     Generate tests          Build one test
                          iteratively             file/feature at a time
                                                  using the strategy

  5.3                     Review AI-generated     Use AI to critique
                          tests                   generated tests, then
                                                  validate them yourself

  5.4                     Fix failing tests       Give the failing test
                                                  and error as focused
                                                  context

  5.5                     Avoid brittle           Make tests resilient
                          hard-coded data         when backend-driven
                                                  content changes

  5.6                     Playwright MCP          Let Copilot interact
                                                  with a browser through
                                                  the Playwright MCP
                                                  server

  5.7                     Copilot coding          Inline suggestions,
                          assistance              selected-code context,
                                                  inline chat and
                                                  explain/review

  5.8                     Page Object Model with  Use official
                          AI                      documentation and
                                                  existing code context
                                                  to refactor into POM
  -----------------------------------------------------------------------

**Module's central idea:** AI can help you move faster through test
strategy, test generation, review, debugging and refactoring. It does
not remove the need for QA judgment, code review or test execution.

------------------------------------------------------------------------

# 🍕 Course application: Pizza Web Store

The instructor uses a pizza-store web application as the demonstration
target.

The lessons refer to these areas: - Menu and pizza items. - Cart
interactions. - Order placement. - Order lookup. - Theme toggle. -
Backend-driven menu content.

The demo app is started locally using `npm start` and runs at
`localhost:3000`. That is the course's demo setup; your own Python
project may use a different command and port.

## Why this sample application matters

It gives the AI assistant something concrete to inspect and test. The
assistant is not asked to invent a test suite for an unknown product. It
is given access to the running UI and/or project context.

------------------------------------------------------------------------

# 🎯 Lesson 5.1 --- Generate an E2E testing strategy with GitHub Copilot

## WHY --- Why create a strategy before asking AI to write tests?

Imagine opening a new repository and asking Copilot:

> Implement all end-to-end tests for this application.

This is too broad. The assistant may: - Miss important user journeys. -
Guess behaviour that is not visible. - Create too many tests at once. -
Use inconsistent structure. - Generate code that is difficult to review.

The course instead follows this sequence:

1.  Give the assistant access to the running application.
2.  Ask it to inspect the application.
3.  Request a testing strategy.
4.  Save the strategy in a Markdown file.
5.  Use that strategy as a reference for implementation.
6.  Generate tests in smaller pieces.

## WHAT --- What is an E2E testing strategy?

An E2E strategy describes which important user journeys should be tested
from the user's point of view.

For the pizza store, the course assistant suggests separate areas such
as: - Menu and cart interactions. - Order placement. - Order lookup. -
UI-related behaviour.

The exact test inventory should be confirmed against the actual
application and requirements.

## HOW --- Course workflow in VS Code

### Step 1 --- Open the test project

The instructor starts with a fresh test project. The assistant does not
automatically know the application behaviour.

### Step 2 --- Give it access to the application

In the course, Copilot uses its `fetch` tool to retrieve the local web
page at `localhost:3000`. The transcript also describes a manual
alternative: open the page source in a browser, copy it and paste it as
context if a fetch tool is unavailable.

**Important distinction:** Fetching a page's HTML/source is not always
the same as understanding the complete application. Dynamic behaviour,
authentication, network calls and state changes may require browser
interaction or additional documentation.

### Step 3 --- Ask for a strategy, not the entire implementation

Course-style prompt:

``` text
Using the fetch tool, inspect http://localhost:3000.

Suggest an end-to-end testing strategy for this website.

Identify the important user journeys and propose
separate test files for each area.

Do not implement the tests yet.
List assumptions and questions where behaviour is unclear.
```

### Step 4 --- Save the strategy to Markdown

The instructor asks Copilot to save the strategy response as a `.md`
file. This gives the project a persistent reference that can be reused
in later prompts.

Suggested file name:

``` text
docs/e2e-testing-strategy.md
```

### Step 5 --- Review before implementation

Check: - Are all critical user journeys represented? - Are the proposed
test files sensible? - Does the strategy contain invented
requirements? - Are high-risk flows prioritised? - Are assumptions
clearly identified?

## Python adaptation

For a Python project, you can keep the same strategy document and
implement it with Pytest and Playwright Python.

Example structure:

``` text
pizza_qa/
├── README.md
├── pytest.ini
├── requirements.txt
├── docs/
│   └── e2e-testing-strategy.md
├── conftest.py
├── pages/
├── tests/
│   ├── test_menu.py
│   ├── test_cart.py
│   ├── test_order_placement.py
│   └── test_order_lookup.py
└── test_data/
```

This is a suggested Python structure, not the TypeScript folder
structure shown in the source video.

### Python example --- strategy-driven test

``` python
def test_menu_displays_available_items(page):
    page.goto("http://localhost:8000")

    menu_items = page.locator("[data-testid='menu-item']")

    assert menu_items.count() > 0
    assert menu_items.first.is_visible()
```

The selector is illustrative. Use a stable locator supported by the
actual application. Prefer accessible roles/labels or dedicated test IDs
where appropriate.

### Common mistakes

-   Asking AI to build the entire framework in one prompt.
-   Treating page source as complete product requirements.
-   Accepting suggested flows without checking the real application.
-   Saving a strategy but never using it as an implementation reference.
-   Allowing the assistant to invent expected behaviour.

### Interview-ready explanation

> "I use AI to accelerate initial test strategy creation. I provide the
> running application or relevant documentation, ask it to identify key
> user journeys and save the reviewed strategy in the repository. Then I
> implement the suite incrementally. I verify each suggested scenario
> against requirements and actual application behaviour rather than
> treating the AI-generated strategy as authoritative."

------------------------------------------------------------------------

# 🧱 Lesson 5.2 --- Generate tests iteratively using the strategy

## WHY --- Why not generate every test in one request?

The course explicitly recommends breaking large implementation tasks
into smaller iterations.

A huge request can produce: - Inconsistent test design. -
Difficult-to-review code. - Missing setup or data dependencies. -
Unclear failures. - A large change that is hard to debug.

## WHAT --- Iterative implementation

The course has a reviewed test suite and asks Copilot to implement
additional test files, for example: - Order placement spec. - Order
lookup spec. - UI spec.

The assistant uses the existing project files as context so that it can
follow the style and patterns already present.

## HOW --- Source workflow

1.  Keep the reviewed testing strategy file open or add it to Copilot's
    context.
2.  Provide the application URL/context again when required.
3.  Ask it to implement one specific test file.
4.  Review the proposed code.
5.  Allow the assistant to run the test only after checking the proposed
    action.
6.  Inspect the execution result.
7.  Keep or revise the changes.
8.  Move to the next feature.

The instructor uses Copilot's fetch tool and permits it to run
commands/tests. Copilot then creates the requested order-placement test
file and runs it.

## Python version --- iterative prompt sequence

### Prompt 1: implement menu tests

``` text
Use docs/e2e-testing-strategy.md as the agreed test plan.

Implement only tests/test_menu.py.

Technology:
Python + Pytest + Playwright Python sync API.

Follow the existing project conventions.
Do not create unrelated files.
Do not invent expected behaviour.

Before editing, summarise the tests you plan to add.
```

### Prompt 2: review the proposed changes

``` text
Review the proposed tests/test_menu.py.

Check:
- Does each test map to the strategy?
- Are locators stable?
- Are assertions meaningful?
- Is test data independent?
- Is any expected behaviour invented?

List findings before changing code.
```

### Prompt 3: run the focused test

``` text
Run only the tests in tests/test_menu.py.

Analyse the output.
Separate actual failures from environment or setup issues.
Do not modify unrelated tests.
```

### Prompt 4: continue with order placement

``` text
Now implement only tests/test_order_placement.py.

Use the same conventions as the reviewed menu tests.
Use the existing fixtures where appropriate.
Explain any new fixture or data dependency before adding it.
```

## Why existing tests are valuable context

The source says Copilot can inspect existing tests and follow their
style. This can improve consistency, but it can also reproduce a bad
pattern.

**Senior QA rule:** AI should follow an existing convention only after
you have reviewed that convention. Do not let a flawed test become the
template for 20 more flawed tests.

------------------------------------------------------------------------

# 🔍 Lesson 5.3 --- Review AI-generated tests

## WHY --- Green tests do not automatically mean good tests

The instructor says the first generated tests have room for improvement.
The lesson is to review them with both: - GitHub Copilot's help. - A
tester's own judgment.

A test can pass but still be weak because it: - Checks the wrong
thing. - Has no meaningful assertion. - Depends on brittle data. -
Repeats another test. - Tests implementation details rather than
user-visible behaviour. - Does not isolate its state.

## WHAT --- Two layers of review

  -----------------------------------------------------------------------
  Review layer                        Questions
  ----------------------------------- -----------------------------------
  AI-assisted review                  Can the assistant identify
                                      suspicious code, missing assertions
                                      or maintainability issues?

  Human QA review                     Does the test verify the correct
                                      requirement and meaningful user
                                      outcome?
  -----------------------------------------------------------------------

## HOW --- Review checklist

For each generated test, inspect:

### 1. Requirement alignment

-   Which requirement does this test verify?
-   Is the expected result documented?
-   Has AI invented a business rule?

### 2. Locator quality

-   Is the locator based on role, label, text or stable test ID?
-   Is it coupled to a fragile CSS structure?
-   Does it identify the intended element uniquely?

### 3. Assertion quality

-   Does the assertion verify the outcome?
-   Could the test pass even if the feature is broken?
-   Is the assertion checking a meaningful user-visible state?

### 4. Test independence

-   Does the test depend on another test running first?
-   Does it leave data/state behind?
-   Can it run independently and repeatedly?

### 5. Maintainability

-   Is data hard-coded unnecessarily?
-   Is business logic duplicated?
-   Would a page object or helper make sense?

## Python example --- weak vs stronger assertion

Weak:

``` python
def test_order_page_loads(page):
    page.goto("/orders")
    assert page.title() is not None
```

This may pass even if the order page is empty or broken.

Stronger, if the requirement says the order history heading must be
shown:

``` python
def test_order_history_heading_is_visible(page):
    page.goto("/orders")

    heading = page.get_by_role(
        "heading",
        name="Order History"
    )

    assert heading.is_visible()
```

The expected heading must match the actual product requirement.

## Copilot review prompt

``` text
Review the selected test as a senior QA engineer.

Do not immediately rewrite it.

First report:
1. Requirement being verified (if identifiable).
2. Weak or missing assertions.
3. Locator stability concerns.
4. Test isolation/data issues.
5. Duplicate or unnecessary logic.
6. Possible false-positive risks.

Separate confirmed problems from suggestions.
Then propose the smallest safe improvement.
```

## Important source lesson

The course shows selecting a test and asking Copilot to review it. The
selection becomes context. You should deliberately select the relevant
code rather than sending a large, unrelated workspace dump.

------------------------------------------------------------------------

# 🛠️ Lesson 5.4 --- Fix failing tests with focused context

## Source demonstration

The instructor selects a failing test, copies its error and asks GitHub
Copilot to fix it.

Copilot identifies a Unicode minus-sign issue in one failing test. The
instructor keeps the change and runs only that test. It passes. The
instructor then selects another failing test and asks for a related fix.

## WHY --- Why select only the failing test?

Focused context helps the assistant concentrate on: - The relevant
test. - Its failure message. - The immediate code involved.

It reduces noise compared with asking the assistant to inspect the
entire project without direction.

## HOW --- Safe debugging workflow

1.  Run the failing test yourself.
2.  Capture the complete error and traceback.
3.  Select the failing test and relevant helper/fixture.
4.  Add the error output to the prompt.
5.  Ask AI to explain the likely issue before changing code.
6.  Inspect the suggested diff.
7.  Run the single failing test.
8.  Run related tests.
9.  Run the relevant suite.
10. Check that the change did not weaken the assertion.

## Python prompt

``` text
Act as a Senior Python QA Automation Engineer.

The selected Pytest test is failing.
Use the supplied traceback and selected code.

First:
1. Explain the exact error.
2. Identify the line involved.
3. Separate facts from hypotheses.
4. Suggest the smallest possible fix.

Do not:
- Remove or weaken assertions just to make the test pass.
- Add arbitrary sleeps.
- Change unrelated tests.
- Invent application behaviour.

After suggesting the fix, tell me which tests to run to verify it.
```

## Python debugging commands

``` bash
# Run one test
pytest tests/test_menu.py::test_menu_displays_available_items -v

# Run one test file
pytest tests/test_menu.py -v

# Run tests matching a keyword
pytest -k "menu" -v

# Run the full suite
pytest -v
```

## Common AI-generated bad fixes

  -----------------------------------------------------------------------
  Bad suggestion                      Why it is dangerous
  ----------------------------------- -----------------------------------
  Delete the failing assertion        Hides the defect instead of fixing
                                      it

  Add `time.sleep(10)`                Slows tests and may still be flaky

  Use `force=True` everywhere         Bypasses actionability checks and
                                      may hide UI problems

  Catch every exception               Turns real failures into silent
                                      passes

  Hard-code a new expected value      May encode the wrong requirement
  without evidence                    
  -----------------------------------------------------------------------

**Rule:** Never accept a fix merely because the test becomes green.
Confirm that the test still checks the intended behaviour.

------------------------------------------------------------------------

# 🧩 Lesson 5.5 --- Remove brittle hard-coded backend data

## WHY --- Why did the instructor change the test?

The course test for the menu page contained hard-coded expected pizza
names.

The instructor points out: - Menu data comes from a backend. - The
business may update the menu. - A test that expects fixed names may fail
even when the UI is functioning correctly.

The instructor asks Copilot to remove hard-coded names and instead
verify that each menu item has a visible, non-empty heading.

This is a key maintainability lesson: test the stable contract that
matters, not incidental data that changes legitimately.

## WHAT --- Brittle vs resilient assertions

Brittle assertion:

``` typescript
expect(menuNames).toEqual([
  "Margherita",
  "Pepperoni",
  "Veggie"
]);
```

If the backend menu changes, the test fails.

More resilient intent:

> Verify that each displayed menu item has a visible, non-empty heading.

## Python + Playwright adaptation

Illustrative markup:

``` html
<article data-testid="menu-item">
  <h2 data-testid="menu-item-name">Margherita</h2>
</article>
```

Python test:

``` python
def test_each_menu_item_has_a_visible_name(page):
    page.goto("http://localhost:8000/menu")

    menu_items = page.get_by_test_id("menu-item")

    assert menu_items.count() > 0

    for item in menu_items.all():
        name = item.get_by_test_id("menu-item-name")

        assert name.is_visible()
        assert name.inner_text().strip() != ""
```

This verifies a stable structural/functional expectation without
hard-coding every menu name.

### But don't over-generalise!

The instructor's replacement assertion is appropriate only if the
requirement is that menu items display a non-empty heading.

If the requirement specifically says: - Margherita must always be
available, or - a particular product must be displayed to a specific
customer,

then you must verify that exact business rule.

**Better test-data strategy:** - Use controlled test data for
deterministic tests. - Use API/database setup where permitted to create
known state. - Use dynamic assertions when the requirement allows
variable content. - Avoid depending on uncontrolled production-like
data.

## Interview question

**How do you avoid brittle UI automation tests?**

> I avoid unnecessary hard-coded data and unstable selectors. I prefer
> semantic locators or stable test IDs, isolate test data, and verify
> the business requirement rather than incidental UI details. If content
> is backend-driven, I either control the test data or assert the stable
> contract that the requirement defines. I also review AI-generated
> tests for hidden assumptions.

------------------------------------------------------------------------

# 🌐 Lesson 5.6 --- Playwright MCP with GitHub Copilot

## WHY --- What problem does MCP solve in the course?

Before using Playwright MCP, the instructor uses Copilot's fetch tool to
understand the application. This involves multiple fetch/cURL
interactions.

The course introduces Playwright MCP as a more browser-oriented way for
Copilot to interact with the website using browser actions.

## WHAT --- Model Context Protocol (MCP)

In this course, MCP is used to extend the assistant's available tools.
Instead of only generating text, the assistant can invoke tools that
interact with a browser.

The instructor installs the Microsoft-published Playwright MCP server in
VS Code. Copilot then exposes Playwright MCP actions in its tool list.

**Conceptual distinction:** - Chat model: interprets the request and
decides what assistance to provide. - MCP server: exposes specific
tools/actions. - Browser: performs the actual navigation and
interaction. - User: reviews and approves tool execution where prompted.

MCP does not mean the model magically sees everything. It can only use
the tools and permissions actually made available.

## Course demo 1 --- Change the website theme

The instructor prompts Copilot to: 1. Use Playwright MCP. 2. Open
`localhost:3000`. 3. Find the theme toggle. 4. Click it. 5. Observe the
changed theme. 6. Save the interaction as a Playwright test.

The generated test records the browser interaction.

## Python equivalent --- what the test might look like

``` python
def test_user_can_toggle_theme(page):
    page.goto("http://localhost:8000")

    theme_button = page.get_by_role(
        "button",
        name="Toggle theme"
    )

    theme_button.click()

    # Example assertion: adapt to the real app's theme contract.
    assert page.locator("html").get_attribute("data-theme") == "dark"
```

The exact accessible name and theme attribute depend on the actual
application. Do not assume this markup exists.

## Course demo 2 --- Order lookup

The instructor asks Copilot, using Playwright MCP, to implement the
order lookup spec.

The assistant: 1. Opens the website. 2. Places an actual order to obtain
a valid order ID. 3. Uses the ID to test successful order lookup. 4.
Creates the test file. 5. Runs the test after user approval.

### Why is this more powerful than fetching HTML?

The order lookup flow requires stateful browser interaction: - Filling
forms. - Clicking controls. - Creating an order. - Reading the generated
order ID. - Searching for that order.

A static page fetch may not reveal all of these behaviours.

## Python-first approach

A Python test might separate order creation from lookup using an API
fixture or a UI flow, depending on what the test is intended to cover.

Example fixture concept:

``` python
import pytest

@pytest.fixture
def created_order(api_client):
    response = api_client.post(
        "/api/orders/",
        json={"items": [{"product_id": 1, "quantity": 1}]},
    )

    assert response.status_code == 201

    order_id = response.json()["id"]
    yield order_id

    # Cleanup only if the application provides a safe,
    # supported cleanup mechanism.
```

Then:

``` python
def test_user_can_lookup_existing_order(page, created_order):
    page.goto("http://localhost:8000/order-lookup")

    page.get_by_label("Order ID").fill(str(created_order))
    page.get_by_role("button", name="Find order").click()

    expect(page.get_by_text(str(created_order))).to_be_visible()
```

This is an illustrative pattern. Actual API payload, endpoint, fixture
and UI behaviour must be based on the application.

## MCP safety rules

Before allowing an assistant to use browser tools: - Confirm the target
environment is local/test, not production. - Review whether the action
creates, updates or deletes data. - Do not provide real credentials
unnecessarily. - Inspect generated files before keeping them. - Check
the test's assertions and cleanup. - Do not let a browser agent place
real orders or payments in a live environment.

## Interview answer

> "MCP allows an AI assistant to access tools exposed by an MCP server.
> In the course example, Playwright MCP exposes browser actions to
> GitHub Copilot. The assistant can navigate a website, interact with
> controls and help generate a Playwright test. I would still review the
> actions, generated code, test data and assertions, and I would
> restrict execution to a safe test environment."

------------------------------------------------------------------------

# 💻 Lesson 5.7 --- GitHub Copilot coding assistance

The source demonstrates four ways Copilot assists while coding.

## 1. Inline suggestions / shadow text

As the developer types, Copilot suggests code as faded or ghost text.
Pressing `Tab` accepts the suggestion. The instructor also shows that
inline suggestions can be disabled or configured in the VS Code status
bar/settings.

### Python example

You begin typing:

``` python
def test_login
```

Copilot may suggest a function body or completion. Review the suggestion
before accepting it.

**Do not accept code only because it looks plausible.**

## 2. Add selected code to chat

The source shows selecting a code block, right-clicking and choosing the
Copilot option to add the selection to chat.

This provides focused code context. You can ask: - Explain this code. -
Review this code. - Debug this code. - Suggest an improvement.

### Prompt

``` text
Explain the selected Python test line by line.

Then identify:
- What it verifies.
- What it does not verify.
- Any hidden assumptions.
- One possible improvement.
```

## 3. Inline chat

The source shows opening a smaller chat directly inside the code editor
after selecting code. This is useful for a focused edit or question
without switching to the full chat view.

Possible requests: - Optimise this function. - Fix this specific
issue. - Add a meaningful assertion. - Explain this locator.

## 4. Explain / Review actions

The instructor demonstrates using the selected code as context with
predefined explain/review actions.

### Python QA examples

``` text
Explain why this fixture uses function scope.
```

``` text
Review whether this Playwright locator is stable.
Do not rewrite it until you explain the risk.
```

``` text
Suggest a minimal refactor that preserves test behaviour.
```

## When to use which mode?

  -----------------------------------------------------------------------
  Mode                                Best use
  ----------------------------------- -----------------------------------
  Inline suggestion                   Completing repetitive code while
                                      typing

  Selected code + chat                Detailed review or explanation of a
                                      specific block

  Inline chat                         Small focused edit or question in
                                      the editor

  Explain/Review action               Quick understanding or review of
                                      selected code
  -----------------------------------------------------------------------

The exact menu labels and available features can change with Copilot and
VS Code versions.

------------------------------------------------------------------------

# 🏗️ Lesson 5.8 --- Use AI to implement Page Object Model

## WHY --- Why POM?

The source introduces Page Object Model as a design pattern that helps
make automation code easier to maintain.

Without POM, tests may contain repeated locators and page interaction
logic. If the UI changes, many tests may need edits.

POM groups page-specific locators and actions into page classes.

## WHAT --- Course workflow

The instructor: 1. Opens the official Playwright documentation page
about POM. 2. Copies its URL. 3. Uses Copilot's fetch tool to provide
the documentation as context. 4. Copies an existing test file as a
backup/new file. 5. Asks Copilot to implement POM for that file. 6.
Copilot creates a page object file in a `pages` folder. 7. The
instructor reviews the generated page object. 8. Runs the tests to
verify the refactor.

The source uses TypeScript files such as `menu.page.ts` and a `pages`
folder.

## Python + Playwright POM adaptation

### Suggested structure

``` text
tests/
    test_menu.py
pages/
    menu_page.py
conftest.py
```

### `pages/menu_page.py`

``` python
from playwright.sync_api import Page, Locator


class MenuPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_items: Locator = page.get_by_test_id("menu-item")

    def open(self):
        self.page.goto("http://localhost:8000/menu")

    def get_menu_item_count(self) -> int:
        return self.menu_items.count()

    def get_menu_item_names(self) -> list[str]:
        names = []

        for item in self.menu_items.all():
            heading = item.get_by_test_id("menu-item-name")
            names.append(heading.inner_text().strip())

        return names
```

### `tests/test_menu.py`

``` python
from pages.menu_page import MenuPage


def test_menu_contains_named_items(page):
    menu_page = MenuPage(page)

    menu_page.open()

    names = menu_page.get_menu_item_names()

    assert names
    assert all(name for name in names)
```

This example assumes the application uses the stated test IDs. Replace
them with locators supported by your real application.

## POM review checklist

-   [ ] Page class represents a meaningful page/component.
-   [ ] Locators are scoped correctly.
-   [ ] Page actions are reusable and readable.
-   [ ] Tests contain business assertions, not unnecessary
    implementation detail.
-   [ ] POM is not over-engineered.
-   [ ] Tests still pass after refactoring.
-   [ ] No expected behaviour was silently changed.

## AI prompt for POM refactoring

``` text
Act as a Senior Python Playwright Automation Engineer.

Use the selected Python test file and the supplied
official Playwright Python documentation.

Refactor this test into a simple Page Object Model.

Requirements:
- Use Python and Playwright sync API.
- Preserve existing test behaviour.
- Keep business assertions in the test where appropriate.
- Put page-specific locators and actions in the page class.
- Avoid unnecessary abstraction.
- Explain each created or modified file.
- Do not invent selectors or application behaviour.

First propose the refactor plan.
Wait for approval before making broad changes.
```

## Important distinction

POM is not a rule that every locator must be hidden in a page class.
Keep the design simple. A small test suite may not need many layers.
Introduce abstractions when they improve reuse, readability or
maintainability.

------------------------------------------------------------------------

# 🧠 Module-wide engineering lessons

## 1. AI-generated code must be reviewed

A generated test can be syntactically correct but logically wrong.
Review: - Requirement mapping. - Locator quality. - Assertions. - Data
setup. - Isolation. - Cleanup. - Failure behaviour.

## 2. Work incrementally

Use this cycle:

``` text
Understand requirement
        ↓
Create/review strategy
        ↓
Implement one small feature
        ↓
Review code
        ↓
Run focused test
        ↓
Run related tests
        ↓
Run full suite when appropriate
        ↓
Commit reviewed changes
```

## 3. Preserve useful project context

The course saves a strategy in Markdown and reuses existing tests as
examples. This is a simple form of persistent project context.

Useful context files: - `README.md` - `docs/e2e-testing-strategy.md` -
`docs/test-data-rules.md` - `pytest.ini` - `conftest.py` - Existing
reviewed page objects and tests

## 4. Don't confuse test passing with test quality

A test can pass while: - Checking the wrong element. - Skipping the
important business rule. - Using stale data. - Depending on another
test. - Having an assertion that is always true.

A green test is evidence that the current test passed under the current
conditions. It is not proof that the product is defect-free.

------------------------------------------------------------------------

# 🧪 Hands-on practice plan

## Exercise 1 --- Testing strategy

Use a demo web application you can safely access.

Deliverable: `docs/e2e-testing-strategy.md`

Include: - Critical user journeys. - Proposed test files. -
Positive/negative scenarios. - Test data needs. - Assumptions and
clarification questions. - High-risk areas.

## Exercise 2 --- Iterative test generation

Implement only one feature's tests first.

Deliverables: - One Pytest test file. - A short explanation of each
test. - Evidence of execution. - Review notes.

## Exercise 3 --- AI test review

Ask Copilot or another assistant to review your generated tests.

Deliverable: a review table:

  ----------------------------------------------------------------------------
  Finding           AI suggestion     Your decision          Reason
  ----------------- ----------------- ---------------------- -----------------
  Example           Replace fixed     Accept/Modify/Reject   Explain based on
                    menu names                               requirement

  ----------------------------------------------------------------------------

## Exercise 4 --- Failure debugging

Intentionally introduce a safe test error, such as an incorrect expected
text.

Deliverables: - Failing test output. - AI diagnosis. - Your own
diagnosis. - Minimal correction. - Focused rerun and related-suite
result.

Do not deliberately break a shared or production environment.

## Exercise 5 --- Dynamic data

Create a test where backend-driven menu data can change.

Decide whether to: - Control data through an API/fixture, or - Verify a
stable contract without hard-coding every product name.

Explain why your chosen strategy matches the requirement.

## Exercise 6 --- MCP browser interaction

If your environment and approved tooling support it: - Ask the assistant
to open a local test application. - Toggle a non-destructive UI
setting. - Inspect what action it performed. - Save a test draft. -
Review and execute the test yourself.

Do not use real payment or production data.

## Exercise 7 --- POM refactor

Refactor one small test file into: - One page object. - One test file. -
Existing fixtures where useful.

Run the tests before and after refactoring. Confirm the refactor did not
change intended behaviour.

------------------------------------------------------------------------

# 🎤 Interview questions from this module

## Q1. How do you use GitHub Copilot in automation testing?

> I use GitHub Copilot as a coding assistant to draft test code, explain
> selected code, review existing tests and help investigate failures. I
> provide focused context such as the relevant test, requirement and
> traceback. I review the proposed changes and execute the tests before
> accepting them. I do not rely on generated code without validating its
> assertions and behaviour.

## Q2. How would you generate an E2E testing strategy using AI?

> I first provide the assistant with the application context, such as a
> running test environment, requirements or relevant documentation. I
> ask it to identify important user journeys and propose a structured
> test strategy. I review the scenarios, assumptions and gaps, save the
> approved strategy in the repository and then implement one feature at
> a time.

## Q3. What is Playwright MCP?

> Playwright MCP is an MCP server that exposes browser automation tools
> to an AI assistant. In the course demonstration, GitHub Copilot uses
> those tools to navigate a website, interact with controls and help
> create Playwright tests. I would review tool actions, generated code
> and test results, and restrict it to a safe environment.

## Q4. How do you debug an AI-generated failing test?

> I reproduce the failure and collect the traceback. I provide the
> relevant test and error as focused context, ask the assistant to
> distinguish facts from possible causes, and review the proposed
> minimal fix. Then I run the individual test, related tests and the
> appropriate suite. I make sure the fix does not remove or weaken the
> intended assertion.

## Q5. Why avoid hard-coded backend data in UI tests?

> Backend-driven data may change legitimately. If a test expects a fixed
> list of product names without that being a requirement, it can fail
> even when the UI works correctly. I either control the test data for
> deterministic verification or assert the stable behaviour required by
> the specification. I do not remove exact assertions when the business
> requirement really requires those values.

## Q6. How can AI help implement POM?

> I provide the existing test code and the official framework
> documentation as context. I ask the assistant to propose a small
> refactor that moves page-specific locators and actions into page
> classes while preserving test behaviour. I review the generated
> abstractions and run the tests before accepting the changes.

## Q7. What are the risks of AI-generated automation?

> AI can invent requirements, create brittle locators, weaken assertions
> or introduce unnecessary abstractions. It may also make changes
> outside the requested scope. I reduce these risks by providing focused
> context, limiting the task, reviewing diffs, running tests and
> checking that the original business intent is preserved.

------------------------------------------------------------------------

# 🧠 If you get stuck while using AI

Use this debugging prompt sequence:

### 1. Explain first

``` text
Do not change the code yet.
Explain what this test currently does and what it is intended to verify.
```

### 2. Diagnose

``` text
Analyse the error and separate confirmed facts from possible causes.
```

### 3. Propose a minimal fix

``` text
Suggest the smallest safe fix. Do not weaken assertions.
```

### 4. Verify

``` text
Tell me which focused tests and related tests should be run to validate this change.
```

### 5. Challenge the result

``` text
Could this change make the test pass while hiding a real application defect?
Explain any false-positive risk.
```

This sequence is often safer than asking "fix everything".

------------------------------------------------------------------------

# 📊 Module 5 progress tracker

  -----------------------------------------------------------------------
  Topic                   Status                  Evidence needed
  ----------------------- ----------------------- -----------------------
  5.1 AI testing strategy ⬜ Not started          Reviewed strategy
                                                  Markdown file

  5.2 Iterative test      ⬜ Not started          One reviewed Python
  generation                                      test file

  5.3 AI-assisted test    ⬜ Not started          Review findings and
  review                                          accept/reject decisions

  5.4 Fix failing tests   ⬜ Not started          Failure diagnosis and
                                                  verified fix

  5.5 Dynamic backend     ⬜ Not started          Resilient test with
  data                                            justified assertions

  5.6 Playwright MCP      ⬜ Not started          Safe browser
                                                  interaction and
                                                  reviewed test draft

  5.7 Copilot coding      ⬜ Not started          Explain/review/inline
  assistance                                      suggestion practice

  5.8 POM with AI         ⬜ Not started          Python page object
                                                  refactor with passing
                                                  tests
  -----------------------------------------------------------------------

## Mastery levels

-   **L1 --- Awareness:** Explain what the tool or technique does.
-   **L2 --- Guided:** Perform the workflow with step-by-step help.
-   **L3 --- Independent:** Use it, review output and debug issues
    independently.
-   **L4 --- Interview-ready:** Explain decisions, trade-offs, risks and
    real examples.

------------------------------------------------------------------------

# 📌 Source coverage and limitations

## Explicitly demonstrated in the uploaded Module 5 transcripts

-   Asking GitHub Copilot to inspect a local website through a fetch
    tool.
-   Generating an E2E testing strategy and saving it as Markdown.
-   Reusing the strategy as context for incremental test generation.
-   Generating additional test files for order placement and order
    lookup.
-   Reviewing generated tests with Copilot and with a tester's judgment.
-   Selecting failing tests and supplying error messages to help
    diagnose/fix them.
-   Identifying brittle hard-coded menu names when data is
    backend-driven.
-   Using Playwright MCP from VS Code with GitHub Copilot.
-   Browser navigation, theme toggling, order placement and order lookup
    through MCP.
-   Saving browser interactions as a Playwright test.
-   Copilot inline/shadow text suggestions and accepting them with Tab.
-   Adding selected code to chat, using inline chat, Explain and Review.
-   Using official Playwright documentation as context for POM
    generation.
-   Creating a page object file and running tests after refactoring.

## Not fully covered by the uploaded source

-   A complete Python implementation of these workflows.
-   Full GitHub Copilot setup instructions for every operating
    system/account.
-   Complete current configuration reference for every Copilot MCP
    option.
-   A full Python Playwright MCP project setup.
-   Full security/permission policy for every MCP environment.
-   A complete production-grade Python framework.

The Python examples and review checklists in this guide are mentor
adaptations designed to transfer the source concepts to your stack. They
are not presented as verbatim course demonstrations.

------------------------------------------------------------------------

# 🏁 Final mentor standard

You have understood Module 5 when you can independently:

1.  Give an AI assistant enough application context to propose an E2E
    strategy.
2.  Save and review that strategy.
3.  Generate one feature's Python tests incrementally.
4.  Review AI-generated tests for false positives and brittle
    assumptions.
5.  Diagnose a failure without blindly accepting an AI fix.
6.  Decide when data should be controlled versus dynamically asserted.
7.  Explain how MCP lets an assistant use browser tools.
8.  Use coding-assistant features with selected code as context.
9.  Refactor a small Python test into POM without changing its intended
    behaviour.
10. Defend the safety and quality checks you performed.

**Remember:** The goal is not to become someone who asks AI to write
tests. The goal is to become a QA Automation Engineer who knows how to
direct AI, inspect its work, catch its mistakes and take responsibility
for the quality of the automation.
