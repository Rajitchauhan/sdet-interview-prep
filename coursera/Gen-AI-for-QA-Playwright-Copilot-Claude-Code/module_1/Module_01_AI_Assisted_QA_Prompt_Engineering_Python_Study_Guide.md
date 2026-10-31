# 🚀 Module 3 --- AI-Assisted QA & Prompt Engineering

## Python + Pytest + Playwright Learning Track \| Hinglish Mentor Notes

> **Course source:** Uploaded `module_3.zip`\
> **Included source files reviewed:** `Prompt_Engineering_QA.pdf`,
> `Prompt-plan.pdf`, lesson subtitles and VTT transcripts.\
> **Teaching language:** Hinglish explanations + professional English
> terminology.\
> **Your implementation stack:** Python, Pytest, Playwright Python.
>
> **Important source boundary:** The uploaded Module 3 material
> introduces AI-assisted QA, prompt engineering, prompt patterns,
> context sharing, learning with AI, voice prompting and log analysis.
> It lists tools including ChatGPT, Claude, GitHub Copilot, Claude Code,
> Cursor, Amazon Q, Cline, Windsurf, NotebookLM, n8n and Playwright MCP.
> The source does not provide a complete step-by-step Python
> implementation of every listed tool. Dedicated Copilot/Claude Code
> hands-on lessons will be taught as separate practical lessons when the
> corresponding course material or workflow is available.

------------------------------------------------------------------------

# 🧭 Module map

  -----------------------------------------------------------------------
  Lesson                  Topic                   What you will be able
                                                  to do
  ----------------------- ----------------------- -----------------------
  3.1                     AI-assisted QA          Identify where AI can
                          introduction            help in a QA workflow
                                                  and where human
                                                  validation is essential

  3.2                     Prompt engineering      Turn vague instructions
                                                  into precise QA prompts

  3.3                     Prompt constraints      Control role, scope,
                                                  format, quality,
                                                  technology, quantity
                                                  and exclusions

  3.4                     Prompt patterns         Use zero-shot,
                                                  few-shot, step-guided
                                                  and iterative prompting

  3.5                     Prompt mistakes         Diagnose vague prompts,
                                                  overloaded tasks,
                                                  missing constraints and
                                                  missing context

  3.6                     Context engineering     Give AI relevant
                                                  documentation, source
                                                  code, tickets, files
                                                  and logs

  3.7                     Learn with AI           Generate interactive
                                                  quizzes from a topic or
                                                  official documentation

  3.8                     Voice prompting         Dictate structured QA
                                                  requests and verify
                                                  transcription

  3.9                     AI tools landscape      Understand chat
                                                  assistants, coding
                                                  assistants and
                                                  specialised tools

  3.10                    AI limitations          Manage hallucinations,
                                                  non-determinism, cost,
                                                  long answers and
                                                  privacy

  3.11                    Python QA lab           Apply the module
                                                  techniques to Pytest
                                                  and Playwright Python
                                                  tasks
  -----------------------------------------------------------------------

**Learning rule:** Reading a prompt is not mastery. You must write it,
run it, inspect the output, challenge it and improve it.

------------------------------------------------------------------------

# 🎯 Lesson 3.1 --- AI-assisted QA: introduction

```{=html}
<blockquote>
```
AI is a productivity assistant for the QA engineer. It does not own the
quality decision.
```{=html}
</blockquote>
```
## WHY --- Why use AI in QA?

A QA engineer may need to: 1. Understand requirements. 2. Identify
positive, negative and boundary scenarios. 3. Prepare test data. 4.
Write or review automation code. 5. Investigate failed tests and logs.
6. Find coverage gaps. 7. Prepare defect reports and test documentation.

AI can help create a first draft or accelerate analysis. The QA engineer
must still verify that the output matches the requirement and actual
application behaviour.

## WHAT --- AI-assisted QA areas from the course

  -----------------------------------------------------------------------
  Area                    How AI may help         QA engineer must verify
  ----------------------- ----------------------- -----------------------
  🧪 Test generation      Draft scenarios, test   Requirement coverage,
                          cases and code          correctness and missing
                                                  cases

  💻 Code assistance      Generate, explain,      Runtime behaviour,
                          review or fix code      assertions,
                                                  maintainability and
                                                  security

  🧰 Test data            Generate or transform   Validity, uniqueness,
                          JSON/CSV data           boundary values and
                                                  privacy

  💡 Brainstorming        Suggest approaches,     Relevance to the
                          risks and edge cases    product and business
                                                  rules

  📚 Data extraction      Extract information     Accuracy against the
                          from long               original document
                          specifications          
  -----------------------------------------------------------------------

## HOW --- Example: registration requirement

Requirement: - Name is mandatory. - Email must be valid. - Password must
contain at least 8 characters. - Duplicate email is not allowed.

Ask AI for a first draft:

``` text
Act as a QA analyst.

Analyse this registration requirement:
- Name is mandatory.
- Email must be valid.
- Password must contain at least 8 characters.
- Duplicate email registration is not allowed.

Generate positive, negative and boundary test scenarios.
Do not invent additional business rules.
List missing or ambiguous requirements separately.
```

Review the response: - Is empty name covered? - Is invalid email
covered? - Are password lengths 7, 8 and 9 covered? - Is duplicate email
covered? - Did the AI invent password complexity rules that were not
specified?

**Remember:** A generated test case is a proposal, not proof of
coverage.

## Python + Pytest example

Illustrative API test. Endpoint, fixture and expected status codes must
be adapted to the actual API contract.

``` python
import pytest

@pytest.mark.parametrize(
    "password, expected_status",
    [
        ("abc1234", 400),
        ("abc12345", 201),
        ("abc123456", 201),
    ],
)
def test_registration_password_length(
    api_client,
    password,
    expected_status,
):
    payload = {
        "name": "Test User",
        "email": "unique-test-user@example.com",
        "password": password,
    }

    response = api_client.post(
        "/api/register/",
        json=payload,
    )

    assert response.status_code == expected_status
```

### Code review questions

-   Does the fixture actually exist?
-   Does the API return these status codes?
-   Is the email unique for each test execution?
-   Is test data cleaned up?
-   Does the test assert only status code, or also response body and
    persisted state where appropriate?
-   Are tests isolated and repeatable?

### Interview answer

**Question: How can AI help in software testing?**

> AI can help QA engineers generate test scenarios, prepare test data,
> review automation code, analyse logs and identify possible coverage
> gaps. However, AI-generated outputs must be validated against
> requirements and actual application behaviour. I use AI to improve
> productivity, not to replace testing knowledge or quality ownership.

------------------------------------------------------------------------

# 🧠 Lesson 3.2 --- Prompt engineering

## WHAT is prompt engineering?

The course defines it as designing and refining prompts to guide AI
models toward more accurate and relevant outputs. It also suggests that
"prompt optimisation" or "prompt crafting" may describe the activity
more simply.

**Simple Hinglish meaning:** AI ko kaam clearly samjhana --- kya karna
hai, kis context mein karna hai, kitna karna hai, kis format mein result
chahiye aur kya nahi karna.

## WHY does prompt quality matter?

Vague prompt → vague or incomplete output.\
Clear prompt + relevant context + constraints → more useful and
reviewable output.

### Course example: vague vs clear

```{=html}
<details>
```
```{=html}
<summary>
```
❌ Vague prompt
```{=html}
</summary>
```
``` text
Write tests for the login page.
```

Problems: - Number of tests unknown. - No field details. - No scenario
types. - No output format. - No business rules.
```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
✅ Clear prompt
```{=html}
</summary>
```
``` text
Write 10 functional test cases for a login page
with an email field, a password field and a
"Sign In" button.

Include positive, negative and edge-case scenarios.

Format each test case as:
ID | Title | Steps | Expected Result

The application uses email/password authentication.
Minimum password length is 8 characters.
```

Why it is better: - Quantity is specified. - Input fields are known. -
Scenario types are stated. - Output structure is defined. - Relevant
business context is supplied.
```{=html}
</details>
```
## Four core prompt principles

1.  **Clarity:** Remove ambiguity.
2.  **Specificity:** Name the exact task and scope.
3.  **Constraints:** Set boundaries and output requirements.
4.  **Context:** Provide information the model cannot safely guess.

## Python QA example

``` text
Act as a Senior Python QA Automation Engineer.

Task:
Review the Pytest test below for correctness.

Scope:
Review only test logic, fixtures, assertions and test-data isolation.

Technology:
Python, Pytest and Playwright Python sync API.

Output:
1. Findings
2. Why each finding matters
3. Suggested correction
4. One improved code example

Do not:
- Convert the code to JavaScript or TypeScript.
- Invent application behaviour.
- Rewrite the whole framework unnecessarily.

Here is my code:
[PASTE CODE]
```

This is aligned with your Python background. The course PDF sometimes
uses Playwright with TypeScript as an example of a technology
constraint; for our exercises, replace it with Python + Pytest +
Playwright Python.

------------------------------------------------------------------------

# 🧩 Lesson 3.3 --- Prompt constraints

The course identifies seven constraint types.

  -----------------------------------------------------------------------
  Constraint              What it controls        QA example
  ----------------------- ----------------------- -----------------------
  🎭 Role                 Who AI should act as    "Act as a Senior QA
                                                  Automation Engineer."

  🎯 Scope                What is                 "Cover checkout only,
                          included/excluded       not account settings."

  🧾 Format               Output structure        "Return ID, Steps,
                                                  Expected Result."

  🏅 Quality              Depth and rigor         "Include positive,
                                                  negative and boundary
                                                  cases."

  🛠️ Technology           Tools and stack         "Use Python, Pytest and
                                                  Playwright."

  🔢 Quantity             Output volume           "Provide exactly 10
                                                  scenarios."

  🚫 Exclusion            What must be avoided    "Do not invent
                                                  undocumented API
                                                  endpoints."
  -----------------------------------------------------------------------

## Master prompt template from the course

``` text
Act as [ROLE].

Task: [EXACT QA/TESTING TASK].

Scope: [FEATURES IN] — exclude [FEATURES OUT].

Constraints: [NUMBER OF TESTS], [TEST TYPES],
[TOOLS/STACK], [OUTPUT FORMAT].

Quality bar: [EDGE CASES, NEGATIVE CASES, PRIORITIZATION].

Do not: [UNWANTED BEHAVIOUR].
```

## Your reusable Python QA master prompt

``` text
Act as a Senior QA Automation Engineer with strong
Python, Pytest and Playwright experience.

Task:
[Describe the exact task.]

Application context:
[Describe the application and relevant behaviour.]

Scope:
[Features to cover.]

Out of scope:
[Features not to cover.]

Technology:
Python + Pytest + Playwright Python.

Quality requirements:
- Positive, negative and boundary cases where relevant.
- Stable semantic locators.
- Meaningful assertions.
- Independent and repeatable tests.
- No hardcoded secrets.
- No invented requirements.

Output format:
[Specify table, code, checklist or explanation.]

Before making assumptions:
List missing information and ask clarifying questions.
```

------------------------------------------------------------------------

# 🔄 Lesson 3.4 --- Prompt patterns

The course covers four patterns.

## 1. Zero-shot prompting

**Meaning:** One prompt contains the instructions; no example is
supplied.

Best for a simple, well-defined task.

``` text
Write a concise Jira bug title for this issue:

On mobile Safari, the Place Order button does nothing
after selecting Cash on Delivery.

Justify the likely user impact in one sentence.
```

Use when: - Task is straightforward. - Expected output is simple. - You
do not need a specialised format.

## 2. Few-shot prompting

**Meaning:** Give one or more examples so the AI can imitate the
expected format or style.

Best for structured and repeatable output.

``` text
Create a bug report for the issue below.

Follow this example format:

Title:
[Short, specific issue summary]

Preconditions:
[Required setup]

Steps:
[Numbered reproduction steps]

Expected Result:
[Expected behaviour]

Actual Result:
[Observed behaviour]

Now create a report for:
On mobile Safari, Place Order does nothing after
Cash on Delivery is selected.
```

Use when: - Your team follows a standard Jira template. - You want
consistent test case tables. - You need the same style across many
outputs.

## 3. Step-guided prompting

The course calls this "chain-of-thought" prompting and demonstrates
asking the model to follow a sequence of steps. In practice, request a
concise rationale, checklist or structured analysis rather than private
internal reasoning.

``` text
Analyse this failure using the following process:

1. Summarise the observed failure.
2. List the known preconditions.
3. Identify missing information.
4. Draft reproduction steps using only known facts.
5. Separate observed facts from hypotheses.
6. Suggest evidence needed for investigation.

Do not claim a root cause unless evidence supports it.
```

Best for: - Multi-step analysis. - Bug report drafting. - Root-cause
investigation support. - Test strategy review.

## 4. Iterative prompting

**Meaning:** Start broad, then improve the response through follow-up
prompts.

Example sequence:

**Prompt 1 --- Initial draft**

``` text
The Place Order button does not work on mobile Safari
when Cash on Delivery is selected. Draft a bug report.
```

**Prompt 2 --- Add structure**

``` text
Rewrite using:
Title, Preconditions, Steps to Reproduce,
Expected Result, Actual Result, Frequency,
Severity and Attachments Needed.

The user is logged in with a valid shipping address.
```

**Prompt 3 --- Add verified environment details**

``` text
Add the verified environment:
iOS 17.4, Safari 17.4, iPhone 15,
production build v2.3.1.

Do not add any environment detail that I have not supplied.
```

**Important:** The course's sample assigns Critical severity because all
COD orders on iOS are blocked. In real work, severity must be based on
verified scope and impact, not copied automatically.

------------------------------------------------------------------------

# ⚠️ Lesson 3.5 --- Common prompt mistakes

  -----------------------------------------------------------------------
  Mistake                 Why it fails            Fix
  ----------------------- ----------------------- -----------------------
  Vague task              AI cannot infer your    State task and desired
                          exact expectation       result

  Too many tasks in one   Output becomes          Split into smaller
  prompt                  unfocused               tasks or ask for a plan
                                                  first

  Missing constraints     Output may be           Specify role, scope,
                          inconsistent            format and quality

  Missing context         AI fills gaps with      Supply requirement,
                          assumptions             examples, code or logs
  -----------------------------------------------------------------------

## A practical workflow for a large task

For a large request, do not immediately ask AI to build the entire
automation framework.

1.  Ask AI to analyse the goal and propose a plan.
2.  Review and correct the plan.
3.  Save the agreed plan in a project document.
4.  Implement one small task at a time.
5.  Run tests after each meaningful change.
6.  Review the diff and evidence before accepting changes.

This reflects the course transcript's recommendation to split complex
work into smaller achievable tasks.

------------------------------------------------------------------------

# 🧠 Lesson 3.6 --- Context engineering in practice

The course demonstrates providing context in several ways:

1.  Open a documentation page and ask the assistant to explain a topic
    using that page as context.
2.  If the assistant cannot fetch the page, copy relevant page
    source/text and provide it as context.
3.  Attach an existing ticket and ask the assistant to use it as a
    structure example for a new ticket.
4.  Attach a log file and ask the assistant to analyse it.
5.  Ask the assistant to request clarification when information is
    missing.

## What is context?

Context can include: - Current conversation. - Requirements and
acceptance criteria. - Official documentation. - Existing Jira ticket
examples. - Code files. - Test output and logs. - Project structure and
configuration.

**Hinglish:** Prompt batata hai AI ko kya karna hai. Context batata hai
AI ko kis information ke basis par kaam karna hai.

## Example A --- Official Playwright documentation

``` text
Use the attached official Playwright Python documentation
as the source.

Explain the retries configuration in Python.

Include:
1. What retries do.
2. Where they are configured.
3. A small Python example.
4. What happens when a test fails.
5. Important limitations.

If the supplied documentation does not answer a point,
say that it is not covered in the source.
```

Always verify version-sensitive behaviour against the official
documentation for the version installed in your project.

## Example B --- Existing Jira ticket as a template

``` text
Study the attached Jira ticket.

Use its structure and writing style as a template.
Create a new draft ticket for a dark-mode feature.

Do not copy the old ticket's facts.
If required details are missing, ask me questions
instead of inventing them.
```

## Example C --- Analyse a Pytest log

``` text
Act as a Senior Python QA Automation Engineer.

Analyse the attached Pytest failure log.

Return:
1. First failing test and error type.
2. Exact error message.
3. Relevant traceback location.
4. Facts directly supported by the log.
5. Possible causes, clearly labelled as hypotheses.
6. Next debugging steps.

Do not claim that a hypothesis is the root cause
until it is verified.
```

## Example D --- Ask clarification questions

The course demonstrates adding this instruction:

``` text
If more information is required, ask me clarifying
questions before generating the final result.
```

Use this when requirements are incomplete or ambiguous.

## Context engineering for your future framework

A useful project context pack may include:

``` text
project/
├── README.md
├── pytest.ini
├── requirements.txt
├── conftest.py
├── config/
├── pages/
├── tests/
├── test_data/
├── utils/
└── docs/
    ├── requirements.md
    ├── test_strategy.md
    └── architecture.md
```

Give the AI only the relevant files for the current task. Do not dump
the entire repository if a small, focused context is enough.

------------------------------------------------------------------------

# 🎓 Lesson 3.7 --- Learn with AI

The course demonstrates using an AI assistant to: - Generate
multiple-choice questions. - Provide one correct answer. - Explain why
an answer is right or wrong. - Build a quiz from official framework
documentation. - Use a specific framework's documentation as the
learning source.

## Your reusable learning prompt

``` text
Act as my strict QA Automation mentor.

Teach me [TOPIC] using Python and Pytest/Playwright Python.

First, explain the concept in Hinglish.
Then ask one multiple-choice question at a time.
Give four options and only one correct answer.

Wait for my answer.
Then:
1. Tell me whether I am correct.
2. Explain why.
3. Explain why the other options are incorrect.
4. Give a practical Python QA example.
5. Track my weak areas.

Use official documentation when supplied.
Do not invent documentation behaviour.
```

## Documentation-based quiz prompt

``` text
Use the supplied official Playwright Python documentation.

Create a 10-question quiz based only on the supplied content.
Ask one question at a time.
Use practical QA scenarios.
After each answer, explain the relevant documentation concept.
Mention if a question requires information not present
in the supplied source.
```

------------------------------------------------------------------------

# 🎙️ Lesson 3.8 --- Voice prompting

The course shows dictating a prompt instead of typing it. Its example
asks for five realistic but fake registration users in JSON: - One valid
user. - One invalid email. - One password shorter than eight
characters. - One name containing a special character. - One empty
required field.

Example dictated prompt:

``` text
Generate a JSON array of five test user objects
for a registration form.

Each object should have:
first name, last name, email, password and phone.

Include:
1. One valid user.
2. One invalid email format.
3. One password shorter than 8 characters.
4. One name with a special character.
5. One empty required field.

Use realistic but fake data.
```

### Voice prompting checks

-   Review the transcription before sending.
-   Check technical terms such as `pytest`, `Playwright`, `locator`,
    `fixture` and `API`.
-   Confirm numbers, file names and code identifiers.
-   Never dictate real passwords, access tokens or private customer
    information.

Voice is useful for brainstorming and describing a problem. For exact
code, commands and structured requirements, typing is often safer.

------------------------------------------------------------------------

# 🧰 Lesson 3.9 --- AI tools landscape

The PDF groups tools into three broad categories.

## A. Chat assistants

  Tool      Course-listed provider/name
  --------- -----------------------------
  ChatGPT   OpenAI
  Claude    Anthropic
  Gemini    Google

Useful for explanation, brainstorming, requirements analysis, test case
drafts and log analysis.

## B. Coding assistants

The PDF lists: - GitHub Copilot - Claude Code - Cursor - Amazon Q -
Cline - Windsurf

These tools can assist with coding workflows. Exact capabilities,
integrations and available modes depend on product version, subscription
and configuration.

## C. Other/specialised tools listed in the PDF

-   NotebookLM
-   n8n
-   Playwright MCP
-   Chrome DevTools MCP
-   TestRigor
-   TestSprite

The PDF lists these tools but does not provide complete implementation
instructions for all of them. We will not pretend that it does.

## Our planned tool-learning sequence

  --------------------------------------------------------------------------
  Stage                   Tool                    Planned use in your
                                                  learning
  ----------------------- ----------------------- --------------------------
  1                       ChatGPT                 Learn concepts, review
                                                  test cases, debug code and
                                                  practise interviews

  2                       Claude chat             Compare explanations, use
                                                  supplied docs/files and
                                                  analyse logs

  3                       GitHub Copilot          Explore code completion,
                                                  chat and repository-aware
                                                  coding assistance

  4                       Claude Code             Explore
                                                  terminal/workspace-based
                                                  coding assistance and
                                                  controlled code changes

  5                       Playwright MCP          Understand tool-connected
                                                  browser interaction and
                                                  its boundaries

  6                       Other tools             Evaluate only when there
                                                  is a clear QA use case
  --------------------------------------------------------------------------

**This is our mentor roadmap, not a claim that all these tools are
taught in the uploaded Module 3.** Dedicated hands-on lessons will be
added when we have the relevant source material and can verify the
current tool workflow.

### Python-first rule

If a course demo uses:

``` typescript
test("login", async ({ page }) => {
  // TypeScript example
});
```

We will translate the concept into Python:

``` python
def test_login(page):
    page.goto("https://example.com/login")
    page.get_by_label("Email").fill("qa@example.com")
    page.get_by_label("Password").fill("ExamplePass123")
    page.get_by_role("button", name="Sign in").click()
```

The goal is to learn the underlying automation concept and use your
chosen stack, not to switch languages unnecessarily.

------------------------------------------------------------------------

# ⚙️ Lesson 3.10 --- How AI works: concepts introduced in the PDF

## Large Language Models (LLMs)

The PDF describes LLMs as neural networks trained on large text datasets
to understand and generate language. It explains that they generate text
by predicting the next token based on learned patterns.

Capabilities listed: - Text generation. - Summarisation. -
Translation. - Code writing. - Reasoning-style responses. - Question
answering.

## Tokens and context window

-   A token is a chunk of text processed by the model; it may be a word,
    part of a word or punctuation.
-   A context window is the amount of input and output context a model
    can process in one interaction.
-   Prompt + supplied context + generated response must fit within the
    available context window.

The PDF gives "roughly three-quarters of a word" as an intuition, not a
universal token conversion formula.

## Agentic AI

The PDF describes agentic AI as systems that can plan, use tools, take
actions and interact with an environment across multiple steps.

Potential QA examples mentioned: - Writing tests. - Running tests. -
Analysing failures. - Filing bugs. - Suggesting fixes.

**Important distinction:** An AI agent taking actions is not the same as
a normal chat response. Tool permissions, review gates, environment
access and safety controls matter. Do not allow an agent to modify or
submit work blindly.

------------------------------------------------------------------------

# ⚠️ Lesson 3.11 --- AI limitations and responsible use

The PDF lists six limitations and suggested mitigations.

  -----------------------------------------------------------------------
  Limitation in source                Practical response
  ----------------------------------- -----------------------------------
  💸 AI can be expensive              Use focused prompts and avoid
                                      unnecessary repeated context

  🧑‍💻 AI does not replace experience   Learn the underlying concepts and
                                      verify outputs

  📜 Answers can be too long          Specify concise format and response
                                      length

  🎭 Hallucinations                   Cross-check with requirements, logs
                                      and official docs

  🎲 Non-deterministic outputs        Review each result; do not assume
                                      repeated prompts give identical
                                      output

  🔐 Privacy concerns                 Follow company policy and avoid
                                      sharing sensitive data with
                                      unapproved tools
  -----------------------------------------------------------------------

### QA-specific safety checklist

-   Never paste production passwords, API keys, access tokens or private
    customer records into an unapproved AI tool.
-   Replace real customer data with synthetic or anonymised data.
-   Do not assume AI-generated locators or assertions are correct.
-   Run generated tests in a safe environment.
-   Review file changes before accepting them.
-   Keep human approval for destructive actions, deployments and bug
    submissions.
-   Record the source of requirements and distinguish observed facts
    from hypotheses.

------------------------------------------------------------------------

# 🧪 Python Practical Lab --- Apply the module

## Lab 1: AI-generated test scenarios

Requirement:

-   Login uses email and password.
-   Both fields are required.
-   Password minimum length is 8.
-   Invalid credentials show an error message.
-   Successful login redirects to the dashboard.

Task: 1. Generate 12 test scenarios. 2. Group them into positive,
negative and boundary cases. 3. Identify ambiguous requirements. 4.
Manually review the output. 5. Mark each case as Accept / Modify /
Reject and explain why.

## Lab 2: AI-assisted Pytest review

Give AI a small Pytest test and ask it to review: - Fixture scope. -
Test independence. - Assertions. - Test data collisions. - Cleanup. -
Readability.

Do not ask it to rewrite the code before it has explained the issues.

## Lab 3: AI-assisted Playwright debugging

Provide: - The failing Python test. - The traceback. - Relevant locator
or page object. - Expected behaviour. - Actual behaviour.

Ask AI to separate: - Evidence from the log. - Possible hypotheses. -
Next diagnostic steps. - Proposed code change.

Then run the test and verify the fix.

## Lab 4: Test data generation

Ask for synthetic JSON data with: - Valid user. - Invalid email. - Empty
required field. - Short password. - Boundary-length password.

Validate the generated JSON and check that it follows your application's
actual rules.

------------------------------------------------------------------------

# 🧠 Interview preparation

## Q1. What is prompt engineering?

**Simple answer:**

> Prompt engineering is the process of writing and refining instructions
> so that an AI model produces more accurate and relevant results.

**Stronger answer:**

> In QA, prompt engineering means defining the task, role, scope,
> context, constraints and expected output format clearly. For example,
> instead of asking AI to write login tests, I specify the fields,
> authentication rules, positive and negative scenarios, expected format
> and exclusions. This makes the output easier to review and reduces
> ambiguity. I still validate every generated test against the actual
> requirements.

## Q2. What is the difference between zero-shot and few-shot prompting?

> Zero-shot prompting gives the model instructions without examples.
> Few-shot prompting includes examples to guide the expected format or
> style. I may use zero-shot for a simple test title and few-shot when I
> need bug reports or test cases in a consistent team format.

## Q3. What is context engineering?

> Context engineering is providing the relevant information an AI
> assistant needs to perform a task correctly. In QA, this can include
> requirements, acceptance criteria, code, logs, API documentation or an
> existing Jira ticket. I provide only relevant context and verify the
> output against the original source.

## Q4. Can AI replace a QA engineer?

> No. AI can accelerate repetitive and analysis-heavy activities, but it
> can generate incorrect assumptions and miss business context. A QA
> engineer must understand requirements, evaluate risk, design
> meaningful tests, validate results and communicate release risks. AI
> is an assistant, while quality ownership remains with the team.

## Q5. How do you use AI to debug a failed Playwright test?

> I provide the failing Python test, traceback, relevant locator and
> expected behaviour. I ask the assistant to identify facts from the log
> separately from possible causes. Then I inspect the page and locator,
> reproduce the issue, apply a controlled fix and rerun the test. I do
> not accept a suggested fix without verification.

------------------------------------------------------------------------

# 🧩 Practice prompts --- copy and use

## Prompt A --- Test design

``` text
Act as a Senior QA Analyst.

Analyse the requirement below and create test scenarios.

Use Python QA terminology where relevant.
Include positive, negative and boundary cases.
Do not invent missing business rules.

Separate:
1. Confirmed requirements
2. Assumptions
3. Clarification questions
4. Test scenarios

Requirement:
[PASTE REQUIREMENT]
```

## Prompt B --- Python code review

``` text
Act as a Senior Python QA Automation Engineer.

Review the supplied Pytest code.

Check:
- Correctness
- Fixture usage
- Test independence
- Assertions
- Test data management
- Maintainability

First list issues and explain them.
Then suggest a minimal corrected version.

Do not convert to JavaScript or TypeScript.
Do not invent application behaviour.

Code:
[PASTE CODE]
```

## Prompt C --- Log analysis

``` text
Analyse the supplied Pytest/Playwright log.

Return:
1. Failing test
2. Error type and exact message
3. Traceback location
4. Facts supported by the log
5. Possible causes labelled as hypotheses
6. Next debugging steps

Do not claim a root cause without evidence.

Log:
[PASTE LOG]
```

## Prompt D --- Interactive quiz

``` text
Act as my strict QA mentor.

Create a 10-question quiz on [TOPIC].
Ask one question at a time.
Use realistic QA scenarios.
Wait for my answer.
Explain why the correct answer is right and
why the other options are wrong.
Track my weak concepts.
Use Python + Pytest + Playwright examples.
```

------------------------------------------------------------------------

# 📊 Module mastery tracker

  -----------------------------------------------------------------------
  Lesson                  Status                  Evidence required
  ----------------------- ----------------------- -----------------------
  3.1 AI-assisted QA      ⬜ Not started          Explain five AI use
                                                  cases and their risks

  3.2 Prompt engineering  ⬜ Not started          Rewrite three vague
                                                  prompts

  3.3 Prompt constraints  ⬜ Not started          Build one master QA
                                                  prompt

  3.4 Prompt patterns     ⬜ Not started          Demonstrate all four
                                                  patterns

  3.5 Prompt mistakes     ⬜ Not started          Diagnose and fix weak
                                                  prompts

  3.6 Context engineering ⬜ Not started          Analyse docs, ticket
                                                  and log context

  3.7 Learning with AI    ⬜ Not started          Create a
                                                  documentation-based
                                                  quiz

  3.8 Voice prompting     ⬜ Not started          Dictate and verify a QA
                                                  prompt

  3.9 AI tools landscape  ⬜ Not started          Explain chat vs coding
                                                  assistants vs
                                                  specialised tools

  3.10 LLM concepts       ⬜ Not started          Explain tokens, context
                                                  window and agents

  3.11 Limitations        ⬜ Not started          Identify hallucination,
                                                  privacy and reliability
                                                  risks

  Python QA Lab           ⬜ Not started          Complete labs and
                                                  defend your changes
  -----------------------------------------------------------------------

## Mentor evaluation scale

-   **L1 --- Awareness:** Can define the concept.
-   **L2 --- Working knowledge:** Can use it with guidance.
-   **L3 --- Independent:** Can apply it, verify output and explain
    trade-offs.
-   **L4 --- Interview-ready:** Can defend decisions and handle
    follow-up questions.

A lesson is not complete just because you read the notes. You must
demonstrate the skill.

------------------------------------------------------------------------

# 🔜 What comes next?

1.  Prompt engineering in depth: role, scope, format, quality and
    exclusions.
2.  Zero-shot, few-shot, step-guided and iterative prompt practice.
3.  Context engineering with Playwright Python documentation, Jira-style
    tickets and test logs.
4.  AI-assisted Pytest and Playwright Python code review.
5.  Claude chat and Claude Code workflows.
6.  GitHub Copilot workflows for Python automation.
7.  Tool-assisted browser workflows such as Playwright MCP, with
    permission and safety boundaries.

**Course alignment note:** The uploaded Module 3 source explicitly
includes the tool names and concepts listed above, but does not provide
a complete practical walkthrough for every tool. We will add hands-on
tool lessons as separate mentor modules and verify product-specific
instructions against current official documentation when we reach them.
