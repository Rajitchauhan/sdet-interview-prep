# 🤖 Module 6 --- Claude Code for AI-Assisted Playwright Automation

## Python + Pytest + Playwright Python \| Hinglish Mentor Study Guide

> **Source reviewed:** Uploaded `module_6.zip`. It contains nine `.txt`
> subtitle/transcript files and nine matching `.vtt` subtitle files.
> Repeated lessons were consolidated so the same content is not
> duplicated.
>
> **Course demonstration stack:** Claude Code, VS Code, terminal,
> Playwright Test with TypeScript, a local pizza-store web application
> and Git.
>
> **Your implementation stack:** Python + Pytest + Playwright Python.
>
> **Source boundary:** This guide follows the workflows actually
> demonstrated in the supplied transcripts. Python code and
> Python-specific Claude instructions are mentor adaptations. The ZIP
> does not contain a complete Python-specific Claude Code tutorial or a
> full standalone Claude Code reference manual.

------------------------------------------------------------------------

# 🧭 Module 6 learning map

  -----------------------------------------------------------------------
  Lesson                  Topic                   Practical outcome
  ----------------------- ----------------------- -----------------------
  6.1                     Claude Code basics      Understand terminal and
                                                  VS Code workflows

  6.2                     Initialise a Playwright Use Claude Code to help
                          project                 set up a project and
                                                  understand command
                                                  permissions

  6.3                     Generate a testing      Inspect a running
                          strategy                application and save a
                                                  test plan

  6.4                     Generate tests          Implement one
                          incrementally           feature/test file at a
                                                  time

  6.5                     Review and improve      Identify hard-coded
                          generated tests         data and improve test
                                                  resilience

  6.6                     `CLAUDE.md` and memory  Give Claude persistent
                                                  project instructions

  6.7                     Complete remaining      Generate a larger
                          tests                   batch, run the suite
                                                  and diagnose failures

  6.8                     Model selection and     Match model
                          multiple sessions       capability/cost to task
                                                  complexity

  6.9                     Insights and usage      Reflect on how you use
                          review                  Claude Code
  -----------------------------------------------------------------------

**Central principle:** Claude Code can inspect project context, propose
edits, run commands and help debug. You remain responsible for reviewing
its changes and proving that the tests verify the correct requirements.

------------------------------------------------------------------------

# 🍕 Course demo application

The instructor uses a simple pizza-store website as the practice
application.

The lessons use the running website to: - Understand the application's
functionality. - Propose an end-to-end testing strategy. - Identify test
files and user journeys. - Generate a Page Object Model and test
files. - Execute tests. - Find and improve brittle assertions. -
Complete the remaining test suite.

The course application runs at `localhost:3000` in the demonstration.
That port and setup belong to the course environment; your own Python
application may use a different URL.

------------------------------------------------------------------------

# 🧠 Lesson 6.1 --- Claude Code: basic ways to work

## WHY --- Why use Claude Code?

A normal chat assistant mainly responds with text. Claude Code is
presented in this course as a coding assistant that can work with a
project workspace and, when permitted, use terminal commands and edit
project files.

For QA automation, that can help with: - Understanding existing test
code. - Creating a test strategy document. - Generating test files. -
Reviewing code. - Running tests. - Analysing failures. - Refactoring
tests into a maintainable structure.

## WHAT --- Two ways shown in the course

### 1. Terminal

The instructor opens a terminal inside the project workspace and starts
Claude Code by typing:

``` bash
claude
```

Once the session starts, slash commands can be used to access available
commands and descriptions.

### 2. VS Code extension

The instructor also demonstrates starting a Claude Code session from the
VS Code extension.

The editor remains available, so selected/open files can be used as
context. For example, opening `menu.spec.ts` and asking "Explain this
code" gives Claude a clear reference for what "this code" means.

## HOW --- What is the practical difference?

  -----------------------------------------------------------------------
  Terminal workflow                   VS Code workflow
  ----------------------------------- -----------------------------------
  Convenient for project-wide tasks   Convenient when inspecting or
  and terminal commands               selecting code

  Can initialise a project and        Can use open files and editor
  execute commands                    context

  Useful for longer-running tasks     Useful for focused code
                                      explanations and edits
  -----------------------------------------------------------------------

You do not need to use only one. The course uses both.

## Python example

Your project might look like:

``` text
python_qa_project/
├── README.md
├── requirements.txt
├── pytest.ini
├── conftest.py
├── pages/
├── tests/
└── docs/
```

From the project root, you can start Claude Code in the terminal if it
is installed and configured:

``` bash
claude
```

Then ask it to explain the project structure:

``` text
Inspect this Python QA automation project.

Explain:
1. Main folders and files.
2. Pytest configuration.
3. Fixtures and their scope.
4. How Playwright pages are created.
5. How tests are discovered.

Do not edit any files.
If something cannot be established from the project, say so.
```

### Common mistakes

-   Starting the assistant from the wrong directory.
-   Assuming it understands files that are not in its available context.
-   Asking it to edit before understanding the existing project.
-   Accepting a command without reading what it will do.

### Interview-ready explanation

> "Claude Code can be used from the terminal or a supported IDE
> integration. In a QA project, I can use it to inspect the repository,
> explain tests, propose changes and run commands when permission is
> granted. I review the proposed actions and code rather than treating
> the assistant as an unrestricted autonomous developer."

------------------------------------------------------------------------

# 🏗️ Lesson 6.2 --- Initialise a Playwright project with Claude Code

## Source demonstration

The instructor starts inside an empty folder and asks Claude how to
initialise a Playwright project. The course uses the TypeScript
Playwright setup command:

``` bash
npm init playwright@latest
```

The instructor then starts Claude Code in the terminal and asks it to
initialise the project. Claude proposes the command, the user approves
it, and the project files are created.

The instructor also demonstrates that, because the project is inside a
Git repository, Claude can be asked to add, commit and push the new
files.

## WHY --- Why is this useful?

It demonstrates a tool-assisted setup workflow: 1. Ask Claude what setup
is needed. 2. Let it propose the command. 3. Review the command. 4.
Approve execution. 5. Inspect the generated files. 6. Verify the project
works.

The important skill is not memorising the command. It is understanding
and reviewing the actions the assistant proposes.

## Python + Playwright setup

For your Python stack, the setup is different. The TypeScript command
above is not the command for creating a Python Playwright project.

A simple Python setup:

``` bash
# Create and activate a virtual environment
python -m venv .venv

# Windows PowerShell activation
.venv\Scripts\Activate.ps1

# Install dependencies
pip install pytest pytest-playwright

# Install Playwright browser binaries
playwright install
```

If you prefer to install Playwright directly:

``` bash
pip install pytest playwright
playwright install
```

The first approach uses the Pytest Playwright plugin. The second
installs the Playwright Python library; you may still use
`sync_playwright()` directly.

## Claude Code prompt for your Python project

``` text
Help me initialise a Python UI automation project.

Technology:
- Python
- Pytest
- Playwright Python sync API

Before running any command:
1. Explain what it does.
2. Tell me which files it will create or change.
3. Identify any destructive or environment-changing effect.
4. Wait for my approval.

Do not initialise a TypeScript or JavaScript project.
```

## Command permission: understand before approving

The course demonstrates that terminal commands may be allowed: - One
time only. - With a broader remembered permission for matching commands,
depending on the tool's permission interface.

**Mentor rule:** Start with the narrowest permission that lets you
complete the task. Do not grant broad command approval just to save a
click.

Before approving, check: - Is the command being run in the correct
folder? - Does it install or remove packages? - Does it modify files? -
Does it access the network? - Does it commit or push code? - Could it
affect production or shared data?

## Git operations shown in the source

The instructor asks Claude to commit and push the newly generated files.
Claude stages, commits and pushes the project changes.

For your own work, inspect the Git changes before committing:

``` bash
git status
git diff
git diff --staged
```

Then, when you are satisfied:

``` bash
git add .
git commit -m "Initialize Python Playwright project"
git push
```

Do not let AI push unreviewed code to a shared branch automatically.

------------------------------------------------------------------------

# 🧭 Lesson 6.3 --- Generate a testing strategy with Claude Code

## WHY --- Why start with a strategy?

The instructor does not immediately ask Claude to implement every test.

Instead, the assistant is asked to inspect the running pizza
application, understand its functionality, propose a testing plan and
save that plan to a file.

This is important because the assistant may otherwise follow the default
generated example test or choose a structure that does not match your
preferences.

## WHAT --- Testing strategy

A testing strategy is a documented approach describing: - What important
functionality should be tested. - Which user journeys matter. - What
kinds of checks are appropriate. - How tests should be organised. - What
assumptions or questions remain.

The course's strategy also suggests a file plan and a Page Object Model
structure.

## HOW --- Exact course workflow

1.  Open the Playwright project.
2.  Ensure the application is running.
3.  Start Claude Code in VS Code or the terminal.
4.  Ask it to visit the application and identify functionality.
5.  Ask for a testing plan.
6.  Explicitly say not to create tests yet.
7.  Review the plan.
8.  Ask for a file plan if one is missing.
9.  Ask Claude to add the file plan to the existing document.

The course transcript describes Claude making requests to understand the
website, including page fetches, scripts and API requests. The
instructor approves those requests.

## Course-style prompt

``` text
This project will hold tests for our application.

Go to the running website and understand its functionality.
Propose a testing plan and save it to a Markdown file.

Do not create any tests yet.

Include:
- Main features and user journeys.
- Suggested test coverage.
- A proposed test-file structure.
- Page Object Model considerations.
- Assumptions and questions.
```

## Python adaptation

Save the reviewed strategy at:

``` text
docs/testing-strategy.md
```

Example proposed structure:

``` text
python_qa_project/
├── docs/
│   └── testing-strategy.md
├── pages/
│   ├── menu_page.py
│   └── order_page.py
├── tests/
│   ├── test_menu.py
│   └── test_order.py
├── conftest.py
└── pytest.ini
```

This is a mentor-proposed Python structure. It is not the exact
TypeScript structure shown in the video.

### Strategy review checklist

-   [ ] Does the plan reflect the real application?
-   [ ] Are the important user journeys included?
-   [ ] Are assumptions separated from confirmed behaviour?
-   [ ] Does it suggest sensible test-file boundaries?
-   [ ] Is POM appropriate for the project size?
-   [ ] Does it avoid creating tests before the plan is approved?

### Common mistakes

-   Asking for tests and a strategy in the same large request.
-   Forgetting to state that tests must not be created yet.
-   Assuming the assistant has understood every backend rule from the
    UI.
-   Accepting a proposed test plan without review.
-   Forgetting to save the agreed plan for later sessions.

------------------------------------------------------------------------

# 🧪 Lesson 6.4 --- Generate tests incrementally

## WHY --- Why start with one test file?

The instructor explicitly avoids asking Claude to implement the entire
strategy immediately.

Instead: 1. Remove the generated example test that may bias the
assistant toward an unwanted style. 2. Start a new Claude session. 3.
Add the testing plan as context. 4. Ask for one basic test file, such as
`menu.spec.ts`. 5. Let Claude propose the POM and test file. 6. Review
the changes. 7. Run the tests.

This keeps the first implementation small enough to review.

## Course TypeScript example

The instructor asks Claude to implement the menu tests described in the
strategy. Claude creates: - A POM directory. - A `pizzaPage.ts` page
object. - A `menu.spec.ts` test file.

The user approves the edits and allows the tests to run.

## Python adaptation --- prompt

``` text
Use docs/testing-strategy.md as the approved plan.

Implement only tests/test_menu.py.

Technology:
Python + Pytest + Playwright Python sync API.

Use the existing project conventions.
If a page object is required, create only the smallest useful page object.
Do not implement other features yet.

Before editing:
1. Explain the tests you plan to add.
2. Identify the required locators.
3. List any assumptions.
```

### Example Python POM

``` python
from playwright.sync_api import Page


class PizzaMenuPage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_items = page.get_by_test_id("menu-item")

    def open(self):
        self.page.goto("http://localhost:8000/menu")

    def get_menu_item_names(self) -> list[str]:
        names = []

        for item in self.menu_items.all():
            name = item.get_by_test_id("menu-item-name")
            names.append(name.inner_text().strip())

        return names
```

### Example test

``` python
from pages.pizza_menu_page import PizzaMenuPage


def test_menu_contains_named_items(page):
    menu = PizzaMenuPage(page)
    menu.open()

    names = menu.get_menu_item_names()

    assert names
    assert all(names)
```

**Assumption:** The application exposes `data-testid="menu-item"` and
`data-testid="menu-item-name"`. Replace these with selectors that
actually exist. Never ask AI to invent selectors.

## Review after generation

The instructor manually inspects what Claude created. You must do the
same.

Review: - Does the POM contain sensible page-level locators/actions? -
Does the test verify the correct requirement? - Are assertions
meaningful? - Does the test depend on hard-coded data? - Did Claude add
unrelated files? - Does the code match Python project conventions?

------------------------------------------------------------------------

# 🔍 Lesson 6.5 --- Improve hard-coded expected data

## Source problem

The first generated menu test contains hard-coded expected menu items.

The instructor identifies a risk: - Menu content is controlled by the
backend. - If the backend menu changes, the test may fail even if the
page works correctly.

The instructor asks Claude to update the test so it no longer uses
hard-coded menu names.

Claude adds a `getMenuItems` method that reads menu item names from the
DOM. The test then uses the observed menu items rather than a fixed
list.

The instructor approves the changes, reruns the test and confirms it
passes.

## WHY --- Why can hard-coded values be a problem?

A test becomes brittle when it asserts values that are not part of the
stable requirement.

For example, if the menu is intentionally updated from: - Margherita -
Pepperoni - Veggie

to: - Margherita - Pepperoni - Four Cheese

a test expecting the old exact list may fail even though the menu is
behaving correctly.

## Python adaptation

``` python
def test_each_menu_item_has_a_name(page):
    page.goto("http://localhost:8000/menu")

    items = page.get_by_test_id("menu-item")

    assert items.count() > 0

    for item in items.all():
        name = item.get_by_test_id("menu-item-name")

        assert name.is_visible()
        assert name.inner_text().strip() != ""
```

This checks the stable contract that each displayed menu item has a
visible name.

## Important nuance --- dynamic assertion is not always correct

Do not remove expected values blindly.

If the requirement explicitly states that a specific product must be
displayed, then the test should verify that exact product.

Choose based on the requirement:

  -----------------------------------------------------------------------
  Requirement                         Better test approach
  ----------------------------------- -----------------------------------
  Menu may change; each item must     Assert non-empty visible names
  display a name                      

  A specific featured product must    Assert that product is present
  appear                              

  Test must verify a known menu       Seed/control test data and assert
  configuration                       the known values

  API response and UI must agree      Compare the UI with a controlled
                                      API response
  -----------------------------------------------------------------------

## Claude prompt

``` text
The menu names are hard-coded in this test.
The menu is backend-driven and can change.

Review the requirement and update the test to avoid
unnecessary hard-coded menu names.

Do not remove assertions that verify actual business rules.
Explain:
1. What is brittle.
2. Which behaviour must still be verified.
3. What code you want to change.
4. How the revised test avoids false positives.
```

### Interview answer

> "I avoid hard-coding dynamic backend content unless the exact value is
> part of the requirement. I either control the test data or verify a
> stable contract, such as each menu item having a visible name. I do
> not remove exact assertions when the business requirement explicitly
> requires those values."

------------------------------------------------------------------------

# 🧠 Lesson 6.6 --- Claude memory and `CLAUDE.md`

## WHY --- Why does a project need persistent instructions?

Without persistent project instructions, you may have to repeat: - Which
programming language the project uses. - Which test framework is used. -
Which API style is preferred. - How locators should be written. - Which
commands run the tests. - What coding conventions the project follows.

The course introduces `CLAUDE.md` as a way to give Claude persistent
project context.

## WHAT --- Two memory mechanisms described in the course

### 1. Auto memory

The transcript describes Claude automatically taking notes based on
interactions, corrections and preferences.

### 2. `CLAUDE.md`

A project instruction file containing information and instructions that
should be available in future Claude sessions.

The course describes several possible instruction locations: - A
user-level instruction file that can affect interactions across
projects. - A project-level `CLAUDE.md` shared with the team. - Personal
project instructions in a `.claude` directory, typically kept out of Git
if they are personal.

Exact file discovery and precedence can depend on the current Claude
Code version and configuration. Verify current official documentation
when setting up your environment.

## HOW --- Generate the file using the course workflow

The instructor: 1. Reaches a point where the project implementation is
satisfactory. 2. Invokes the initialization command shown in the
transcript as `.init`. 3. Claude analyses the project. 4. Claude
proposes a `CLAUDE.md` file. 5. The user reviews and allows the file to
be written. 6. The instructor notices that coding conventions are
missing. 7. The instructor asks Claude to inspect the TypeScript files
and add coding standards. 8. The file is updated with framework
conventions and locator preferences.

**Command note:** The transcript's speech-to-text writes the command as
`.init`. Claude Code command spelling can change or be rendered
imperfectly in subtitles; check the command palette/help or current
official Claude Code documentation before executing it. Do not blindly
copy a transcription error.

## Python-first `CLAUDE.md` starter

The following is a mentor-created template for your Python QA project:

``` markdown
# Project Instructions for Claude

## Project Overview
This repository contains UI and API automation tests.

## Technology Stack
- Python
- Pytest
- Playwright Python
- Requests for API tests

## Python Standards
- Use readable, type-aware Python where useful.
- Follow PEP 8 conventions.
- Prefer small functions with clear responsibilities.
- Avoid unnecessary abstraction.

## Pytest Standards
- Test files must use the test_ prefix.
- Test functions must use the test_ prefix.
- Use fixtures for shared setup and teardown.
- Keep tests independent.
- Use parametrization when it improves clarity.
- Do not hide failures with broad exception handling.

## Playwright Standards
- Use Playwright Python sync API unless the project specifies otherwise.
- Prefer get_by_role, get_by_label and get_by_test_id where appropriate.
- Avoid brittle XPath and positional selectors unless justified.
- Do not use force=True by default.
- Do not add arbitrary time.sleep calls.
- Use web-first assertions where appropriate.

## Test Quality
- Assert business outcomes.
- Do not weaken assertions just to make tests pass.
- Avoid hard-coded dynamic data unless required.
- Do not invent application requirements.
- Separate facts from hypotheses during debugging.

## Safety
- Never expose secrets or credentials.
- Do not run destructive actions against production.
- Explain commands that change files or environments.
- Ask before committing or pushing changes.

## Common Commands
- Run suite: pytest -v
- Run one file: pytest tests/test_example.py -v
```

Adapt this file to the actual repository. Do not keep rules that
contradict your team's approved standards.

## What should go into `CLAUDE.md`?

Good persistent instructions: - Project architecture. - Language and
framework. - Naming conventions. - Locator conventions. - Test execution
commands. - Code quality rules. - Safety constraints.

Avoid: - A huge copy of all documentation. - Temporary debugging
notes. - Secrets or passwords. - Unverified assumptions. - Instructions
that are no longer true.

## `CLAUDE.md` maintenance rule

Update it when you discover a reusable convention. Do not update it
after every temporary issue.

------------------------------------------------------------------------

# 🧪 Lesson 6.7 --- Generate the remaining tests and fix failures

## Source demonstration

Once the testing plan and `CLAUDE.md` exist, the instructor asks Claude
to implement the remaining tests.

The assistant: 1. Uses the testing plan as context. 2. Creates seven
remaining specification files. 3. Lists which test cases each file
covers. 4. The instructor runs the entire suite through the Playwright
VS Code extension. 5. The notification tests fail. 6. The instructor
asks Claude to run the notification tests and fix the errors. 7. Claude
identifies an assertion problem and changes the assertion based on the
application's CSS. 8. Claude reruns the test and reports that it passes.
9. The instructor runs the tests independently to verify the result.

## WHY --- Why is this a bigger task?

The course has already established: - A strategy. - A project
structure. - A first test implementation. - Persistent instructions.

That gives Claude more context for completing the remaining tests.

## HOW --- Safe workflow

The source uses a larger prompt to implement the remaining tests and
allows the assistant to perform several edits. This can save time, but
it increases the amount of code that must be reviewed.

Recommended sequence:

1.  Confirm the testing strategy is approved.
2.  Confirm `CLAUDE.md` contains correct instructions.
3.  Ask for a list of remaining test files and scenarios.
4.  Review that list.
5.  Ask Claude to implement the remaining tests.
6.  Inspect the file changes.
7.  Run the full test suite.
8.  Group failures by cause.
9.  Fix one failing area at a time.
10. Rerun focused tests and then the suite.

## Python prompt --- remaining tests

``` text
Use the approved docs/testing-strategy.md
and the project's CLAUDE.md instructions.

Implement the remaining Python Pytest tests.

Before editing:
1. List the files you intend to create or modify.
2. Map each test file to the strategy.
3. Identify shared fixtures and data dependencies.
4. Identify any unclear requirements.

Do not modify unrelated files.
Do not invent expected behaviour.
```

## Python prompt --- notification test failure

``` text
Run only the notification-related tests.

Analyse the failures and report:
1. Exact failing test.
2. Assertion that failed.
3. Expected vs actual result.
4. Evidence from the traceback or application.
5. Possible causes, labelled as hypotheses.

Then propose the smallest safe fix.
Do not weaken or remove the business assertion.
Run the focused tests after the change.
```

## Python commands

``` bash
# Run one failing test
pytest tests/test_notifications.py -v

# Run notification-related tests by keyword
pytest -k "notification" -v

# Run full suite
pytest -v
```

## Important warning --- CSS assertion from the course

The transcript says Claude fixed an assertion by checking CSS directly
in the application.

That may be appropriate if the requirement is about a CSS-driven visual
state. But do not assume CSS inspection is always the best assertion.

Prefer checking user-visible behaviour when possible: - Is the
notification visible? - Does it contain the expected message? - Does it
appear after the correct action? - Does it disappear or update as
required?

Use CSS property assertions when the requirement genuinely concerns
styling or visual state.

## Why run tests yourself after Claude says they pass?

Because the assistant's report is not independent proof. You should: -
Inspect the generated test. - Run the test in your own environment. -
Review the final output. - Confirm that no assertion was weakened. -
Check related tests for regressions.

------------------------------------------------------------------------

# ⚖️ Lesson 6.8 --- Claude model selection and multiple sessions

## Source demonstration

The instructor shows a model-selection command using `/model`.

The transcript describes three model choices: - A default middle-ground
model, called "Sonnet" in the transcript. - "Opus" as the more capable
option for difficult tasks, with higher usage. - A lightweight model
transcribed as "HYCU" in the subtitles, intended for quick tasks and
lower usage.

The "HYCU" spelling may be a speech-recognition error. The source does
not provide enough reliable evidence to correct the model name here.
Check the current Claude Code model selector for exact available names.

## WHY --- Why select a model based on task?

Not every task needs the most capable or expensive model.

  -----------------------------------------------------------------------
  Task type                           Model-selection principle
  ----------------------------------- -----------------------------------
  Quick explanation or small edit     Use an efficient model if it
                                      handles the task well

  Normal test generation or code      Use a balanced model
  review                              

  Complex debugging or architecture   Consider a more capable model if
  reasoning                           needed
  -----------------------------------------------------------------------

Actual model availability, names, context limits and usage costs change
over time. Check the current product interface and plan details.

## Multiple terminal sessions

The instructor demonstrates running Claude in more than one terminal: -
One session can handle a long-running task. - Another session can be
used for day-to-day questions or separate work.

### Mentor caution

Parallel sessions can be useful, but do not let two sessions edit the
same files at the same time. That can create conflicting changes.

Safer options: - Give each session a separate task and separate files. -
Ask one session to analyse while another makes no edits. - Review
`git diff` before combining changes. - Use separate branches or
worktrees for larger independent changes.

------------------------------------------------------------------------

# 📈 Lesson 6.9 --- Claude Code Insights

## Source demonstration

The instructor shows an `/insights` command. It generates an HTML report
about personal Claude Code usage, including: - Usage statistics. -
Patterns in how the assistant is used. - Areas where usage appears
appropriate. - Suggestions for improving usage.

The instructor opens the generated `report.html` file and notes that
much of the report is personal.

## Why is this useful?

It encourages reflection: - Are prompts clear? - Are you asking AI to do
too much at once? - Are you reviewing its output? - Are you repeatedly
correcting the same issue? - Are you using an unnecessarily capable
model for simple tasks?

Exact command availability and report content can change. Check the
current Claude Code command list before relying on this feature.

## Personal AI usage review

After a work session, ask yourself:

-   Did I provide enough context?
-   Did I split large work into smaller tasks?
-   Did I review all changes?
-   Did I run the tests independently?
-   Did I accept a fix without understanding it?
-   Did I use more context or model capability than necessary?

------------------------------------------------------------------------

# 🐍 Python + Playwright: complete practical workflow

This combines the module's techniques into a Python-first workflow.

## Suggested repository

``` text
pizza_qa_python/
├── README.md
├── CLAUDE.md
├── requirements.txt
├── pytest.ini
├── conftest.py
├── docs/
│   └── testing-strategy.md
├── pages/
│   ├── __init__.py
│   └── pizza_menu_page.py
├── tests/
│   ├── test_menu.py
│   ├── test_cart.py
│   ├── test_order.py
│   └── test_notifications.py
└── test_data/
```

## End-to-end workflow

``` text
Start Claude Code
        ↓
Understand existing project
        ↓
Inspect running application
        ↓
Draft testing strategy
        ↓
Review and save strategy
        ↓
Create/update CLAUDE.md
        ↓
Implement one test file
        ↓
Review POM and test code
        ↓
Run focused test
        ↓
Fix verified issues
        ↓
Implement remaining tests
        ↓
Run full suite
        ↓
Review Git diff
        ↓
Commit reviewed changes
```

## Reusable master prompt for your Python QA project

``` text
Act as a Senior Python QA Automation Engineer.

Project stack:
- Python
- Pytest
- Playwright Python sync API

Before making changes:
1. Inspect the relevant project files.
2. Read CLAUDE.md and the approved testing strategy.
3. Explain the task and proposed files.
4. Identify missing requirements or assumptions.

Implementation rules:
- Work incrementally.
- Use stable semantic locators where possible.
- Keep tests independent.
- Use fixtures for setup and teardown.
- Keep assertions meaningful.
- Do not add arbitrary sleeps.
- Do not weaken assertions to make tests pass.
- Do not invent application behaviour.
- Do not modify unrelated files.

Safety:
- Explain terminal commands before execution.
- Do not access production systems.
- Do not expose credentials or secrets.
- Ask before committing or pushing.

After implementation:
1. Summarise files changed.
2. Explain key design decisions.
3. Show test commands executed.
4. Report actual test results.
5. List remaining risks or assumptions.
```

------------------------------------------------------------------------

# 🧪 Practical assignments

## Exercise 1 --- Start Claude Code in your Python project

**Task** - Open your Python Playwright project. - Start Claude Code in
terminal or supported VS Code integration. - Ask it to explain the
project structure. - Do not allow edits.

**Deliverable** - Project explanation. - List of configuration files. -
One question about a file you did not understand.

## Exercise 2 --- Generate a testing strategy

**Task** - Use a local demo application. - Ask Claude to inspect its
functionality. - Ask for a strategy only. - Save it as
`docs/testing-strategy.md`.

**Deliverable** - Features. - User journeys. - Proposed test files. -
Assumptions. - Clarification questions.

## Exercise 3 --- Implement one feature

**Task** - Use the approved plan. - Ask Claude to implement only menu
tests. - Use Python + Pytest + Playwright. - Review all generated code.

**Deliverable** - One test file. - Optional POM file. - Test execution
evidence. - Your review comments.

## Exercise 4 --- Fix hard-coded test data

**Task** - Identify a dynamic field in the test. - Decide whether to
control test data or verify a stable contract. - Ask Claude for a
minimal change.

**Deliverable** - Before/after code. - Reason for the chosen
assertion. - Evidence that the test still checks the requirement.

## Exercise 5 --- Create `CLAUDE.md`

**Task** - Ask Claude to inspect the project. - Draft persistent project
instructions. - Add Python, Pytest and Playwright conventions. - Review
every rule.

**Deliverable** - `CLAUDE.md`. - A list of rules you accepted, modified
or rejected.

## Exercise 6 --- Generate remaining tests

**Task** - Ask Claude to implement remaining test files from the
strategy. - Review the proposed file list first. - Run the full suite.

**Deliverable** - Test files. - Test results. - Failure analysis if
applicable.

## Exercise 7 --- Debug a failing test

**Task** - Introduce a safe, intentional assertion mismatch in a local
test. - Give Claude the traceback and selected test. - Ask for diagnosis
before a fix. - Review the diff. - Rerun focused and related tests.

**Deliverable** - Failure evidence. - Diagnosis. - Fix. - Verification
evidence.

## Exercise 8 --- Model and session discipline

**Task** - Use a lightweight/efficient model for a simple explanation if
available. - Use a more capable model for a complex code review if
available. - Compare output quality and usage. - Avoid concurrent edits
to the same files.

**Deliverable** - Short comparison and lessons learned.

------------------------------------------------------------------------

# 🎤 Interview preparation

## Q1. What is Claude Code?

> Claude Code is an AI coding assistant that can work with a project
> workspace. Depending on the environment and permissions, it can
> inspect files, propose or make edits, and run terminal commands. I use
> it to understand test projects, draft strategies, generate tests and
> investigate failures. I review its changes and verify them by
> executing the tests.

## Q2. How do you use Claude Code in Playwright automation?

> I first provide the application and project context. I ask Claude to
> prepare a testing strategy and save it in the repository. Then I
> implement tests incrementally, review the generated POM and
> assertions, run focused tests and fix verified issues. I use
> persistent project instructions to keep generated code aligned with
> our Python and Pytest conventions.

## Q3. What is `CLAUDE.md`?

> `CLAUDE.md` is a project instruction file that provides persistent
> context and conventions to Claude Code. It can describe the technology
> stack, project structure, commands, coding standards and testing
> rules. It helps reduce repeated instructions, but it should be
> reviewed and kept up to date.

## Q4. Why do you generate tests incrementally?

> Incremental implementation makes AI-generated changes easier to review
> and debug. I start with one feature, verify the structure and test
> quality, and then continue with the remaining scenarios. This reduces
> the risk of generating a large, inconsistent test suite.

## Q5. How do you handle a failing AI-generated test?

> I reproduce the failure and inspect the traceback. I provide the
> relevant test and error to the assistant and ask it to separate
> confirmed facts from possible causes. I review the proposed minimal
> fix, ensure that it does not weaken the assertion, and rerun the
> focused test and related tests.

## Q6. Why is hard-coded dynamic test data risky?

> If backend-driven data changes legitimately, a test that expects an
> old fixed list can fail even though the application is correct. I
> control test data when exact values matter, or assert the stable
> contract when content is expected to vary. The assertion must still
> reflect the requirement.

## Q7. How do you safely use AI to run terminal commands?

> I review the command, its working directory and its side effects
> before approval. I prefer narrow permissions, especially for file
> deletion, dependency changes, Git operations or commands that can
> affect shared environments. I inspect the final diff and test results
> before accepting the work.

------------------------------------------------------------------------

# 🧠 When you get stuck --- Claude Code recovery sequence

Do not immediately say "fix everything".

Use this order:

### 1. Explain

``` text
Do not edit anything yet.
Explain the relevant files and the current behaviour.
```

### 2. Plan

``` text
Propose a minimal implementation plan.
List files that would be changed.
Wait for approval.
```

### 3. Diagnose

``` text
Analyse the failure.
Separate facts from hypotheses.
Do not change code yet.
```

### 4. Fix

``` text
Suggest the smallest safe correction.
Do not remove or weaken the intended assertion.
```

### 5. Verify

``` text
Run the focused test.
Then identify related tests that should be run.
Report actual results.
```

### 6. Review

``` text
Summarise the diff.
Identify any assumptions or risks.
Confirm whether any unrelated files changed.
```

------------------------------------------------------------------------

# 📊 Module 6 progress tracker

  -----------------------------------------------------------------------
  Lesson                  Status                  Evidence required
  ----------------------- ----------------------- -----------------------
  6.1 Claude Code basics  ⬜ Not started          Explain terminal vs VS
                                                  Code usage

  6.2 Project             ⬜ Not started          Set up Python project
  initialization                                  and review commands

  6.3 Testing strategy    ⬜ Not started          Reviewed strategy
                                                  Markdown file

  6.4 Incremental test    ⬜ Not started          One Python test file
  generation                                      and optional POM

  6.5 Dynamic data        ⬜ Not started          Resilient assertion
                                                  with justified
                                                  requirement

  6.6 `CLAUDE.md`         ⬜ Not started          Reviewed Python project
                                                  instruction file

  6.7 Complete test suite ⬜ Not started          Remaining tests and
                                                  full-suite result

  6.8 Model/session       ⬜ Not started          Explain capability/cost
  selection                                       trade-off

  6.9 Insights            ⬜ Not started          Reflect on usage
                                                  patterns and
                                                  improvements

  Python practical        ⬜ Not started          Complete assignments
  assignments                                     1--8
  -----------------------------------------------------------------------

## Mastery scale

-   **L1 --- Awareness:** Can explain the concept.
-   **L2 --- Guided:** Can complete the workflow with mentor
    instructions.
-   **L3 --- Independent:** Can use Claude Code, review its changes and
    debug independently.
-   **L4 --- Interview-ready:** Can explain the design, safety controls,
    limitations and trade-offs.

------------------------------------------------------------------------

# 📌 Source coverage and limitations

## Explicitly present in Module 6 transcripts

-   Starting Claude Code from terminal or VS Code extension.
-   Asking Claude to initialise a Playwright project.
-   Approving terminal commands.
-   Optional Git add/commit/push workflow.
-   Asking Claude to inspect a running application.
-   Generating a testing strategy and saving it to a file.
-   Adding a file plan to the strategy.
-   Generating a first test file incrementally.
-   Creating a POM and menu test.
-   Reviewing generated code manually.
-   Replacing hard-coded expected menu items with values read from the
    DOM.
-   Creating and extending `CLAUDE.md`.
-   Described auto memory and project/user instruction files.
-   Generating the remaining test files.
-   Running the full suite and fixing notification test failures.
-   Selecting different Claude models.
-   Running multiple Claude sessions.
-   Generating an HTML insights report.

## Not fully covered in the source

-   Complete Python-specific Claude Code setup.
-   A full Python POM implementation.
-   A full explanation of every `CLAUDE.md` location and precedence
    rule.
-   Current exact model names, quotas and pricing.
-   Complete permission/security configuration.
-   A complete production-grade Python framework.

The Python examples, prompts, review checklists and exercises are mentor
adaptations. They translate the course workflow to your Python
background; they are not claimed to be verbatim course code.

------------------------------------------------------------------------

# 🏁 Final mentor standard

Module 6 is mastered when you can independently:

1.  Start Claude Code in the correct Python project.
2.  Explain what it can and cannot access.
3.  Review a proposed terminal command before approving it.
4.  Generate a testing strategy without prematurely generating tests.
5.  Save and reuse the approved strategy.
6.  Implement one Python test feature at a time.
7.  Review POM, locators and assertions.
8.  Replace brittle dynamic-data assertions without losing business
    coverage.
9.  Maintain a useful `CLAUDE.md`.
10. Run and debug a larger test suite safely.
11. Explain model selection and usage trade-offs.
12. Defend every AI-generated change you keep.

**Final principle:** AI should increase your speed, not reduce your
engineering judgment. If Claude writes a test that you cannot explain,
debug or defend, that test is not yet your work.
