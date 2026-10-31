# QA/SDET Practice Workbook — 30 Sessions + Capstone

> **Purpose:** Turn the first 10 software-testing modules into practical skill. This is a session-based plan, not a calendar commitment. Complete a session's output before moving to the next.
>
> **Mentor approach:** Hinglish understanding → independent attempt → review → correction → interview explanation. Do not copy solutions before attempting the task.

---

# 1. Practice rules

1. **Attempt first, read later.** Try the task without notes for 10–20 minutes.
2. **Explain your reasoning.** A tester must explain why a scenario matters.
3. **Keep evidence.** Save test cases, screenshots, bug reports, API responses, SQL queries and automation reports.
4. **Separate expected and actual.** Never write an expected result after seeing the actual result without recording the requirement basis.
5. **Don't invent defects.** A defect report must describe something you observed and can reproduce.
6. **One feature, multiple layers.** Follow one user journey from UI to API to data where access is available.
7. **Use safe test environments.** Never test destructive actions on a real production account or real payment.
8. **Revisit mistakes.** Keep a mistake log and redo weak exercises after a gap.

---

# 2. Your practical workspace

Create a repository:

```text
qa-sdet-practice/
├── README.md
├── requirements/
│   └── sample_user_stories.md
├── strategy/
│   ├── qa_strategy.md
│   └── raci.md
├── test-design/
│   ├── scenarios.md
│   ├── test-cases.md
│   ├── ep-bva.md
│   ├── decision-table.md
│   └── state-transition.md
├── defects/
│   └── bug-reports.md
├── api/
│   ├── postman/
│   └── pytest/
├── sql/
│   └── validation_queries.sql
├── ui/
│   └── playwright/
├── reports/
└── .github/
    └── workflows/
```

Use a demo/training application or a small app you control. Do not use a real production site for destructive tests.

---

# 3. 30-session practice plan

## Phase A — Testing foundations to applied test design

### Session 1 — Explain the first 10 modules from memory
<badge>Easy · 45–60 min</badge>

Tasks:
- Explain QA vs QC vs UAT.
- Explain verification vs validation.
- List the seven testing principles.
- Explain UI/API/DB flow.
- Explain static vs dynamic testing.
- Explain test levels and test types.
- Explain six STLC phases.
- Explain Dev/QA/Staging/Production.
- Explain Waterfall/V-Model/Agile/CI-CD.
- Explain DoD, BDD and Sprint Review.

Deliverable: `revision/module-1-to-10-recall.md`

Pass condition: explain each topic without reading notes; mark anything you cannot explain as “needs revision”.

### Session 2 — Requirement review and ambiguity hunting
<badge>Easy–Medium · 60 min</badge>

Requirement:
“As a customer, I want to apply a coupon so that I can save money.”

Find at least 12 questions:
- coupon expiry;
- minimum order;
- maximum discount;
- user eligibility;
- one-time/repeated use;
- stacking with other offers;
- currency/rounding;
- empty/invalid coupon;
- case sensitivity;
- product/category restrictions;
- cancellation/refund;
- concurrent checkout.

Deliverable: requirement review checklist + clarified assumptions.

### Session 3 — Test scenarios and test cases
<badge>Medium · 60–90 min</badge>

Write:
- 10 high-level scenarios for login.
- 15 detailed test cases for login.
- Include ID, title, preconditions, steps, test data, expected result, priority.

Review: can another tester execute the test case without asking you questions?

### Session 4 — Equivalence Partitioning and BVA
<badge>Medium · 60 min</badge>

Rule: age allowed 18–65 inclusive.

Tasks:
- Identify valid and invalid partitions.
- Pick representative values.
- Derive 2-value and 3-value boundary sets.
- Explain why each value is selected.

Second rule: password length 8–20 characters. Repeat the exercise.

Deliverable: `test-design/ep-bva.md`

### Session 5 — Decision tables
<badge>Medium · 60 min</badge>

Mentor-created rule:
A customer receives free delivery if:
- membership is active; OR
- cart total is at least ₹999.

A restricted item cannot use free delivery.

Tasks:
- Identify conditions.
- Create a decision table.
- Remove impossible/redundant combinations only after explaining why.
- Derive test cases for each meaningful rule.

Deliverable: `test-design/decision-table.md`

### Session 6 — State transition testing
<badge>Medium · 60 min</badge>

Order states:
`Created → Paid → Packed → Shipped → Delivered`

Also include:
- cancellation allowed before shipping;
- refund after payment;
- no direct Created → Delivered transition.

Tasks:
- Draw state transitions.
- List valid transitions.
- List invalid transitions.
- Test duplicate events and repeated actions.

Deliverable: `test-design/state-transition.md`

### Session 7 — Exploratory testing and error guessing
<badge>Medium · 45–60 min</badge>

Feature: profile update.

Create a 30-minute exploratory charter:
- mission;
- scope;
- test data;
- risks;
- notes;
- findings;
- questions.

Explore empty values, Unicode, long strings, repeated clicks, slow network and session expiry.

Deliverable: one exploratory test charter and findings log.

---

## Phase B — Defect management and test management

### Session 8 — Write professional bug reports
<badge>Medium · 60 min</badge>

Create three observed/reproducible defect reports in a demo app or controlled test app.

Each report must contain:
- concise title;
- environment/build;
- preconditions;
- numbered reproduction steps;
- expected result and its source;
- actual result;
- evidence;
- severity/priority rationale.

Do not invent a bug just to fill the template.

### Session 9 — Severity vs Priority and defect lifecycle
<badge>Medium · 45 min</badge>

For five hypothetical defects, independently assign severity and priority, then justify:
- checkout blocked for all users;
- typo on a rarely visited page;
- crash on a critical but rarely used admin flow;
- duplicate charge;
- wrong sort order on a secondary listing.

Map defect states: New → Assigned → Open/In Progress → Fixed → Retest → Closed, including Reopened, Rejected, Deferred where the team's workflow uses them.

### Session 10 — Test plan, entry/exit criteria, risk
<badge>Medium · 60 min</badge>

For a coupon release:
- scope/in-scope/out-of-scope;
- test approach;
- environment and data;
- entry criteria;
- exit criteria;
- risks and mitigations;
- roles;
- deliverables.

Create a risk matrix with likelihood × impact and rank the tests.

### Session 11 — Traceability and test summary
<badge>Medium · 60 min</badge>

Map each requirement to:
- test scenario;
- test case;
- execution result;
- linked defect.

Then create a test summary:
- planned/executed/passed/failed/blocked;
- open critical/high defects;
- known risks;
- recommendation and rationale.

---

## Phase C — API and SQL

### Session 12 — HTTP and REST basics
<badge>Easy–Medium · 45–60 min</badge>

Explain and demonstrate:
- GET, POST, PUT, PATCH, DELETE;
- path vs query parameters;
- headers;
- JSON body;
- status codes;
- authentication vs authorization;
- idempotency concept.

Deliverable: one-page API notes with examples.

### Session 13 — Postman API testing
<badge>Medium · 60–90 min</badge>

For a safe practice API:
- positive GET;
- create with POST;
- update with PUT/PATCH;
- delete;
- invalid payload;
- missing auth;
- unauthorized role;
- nonexistent resource.

Validate status, headers, response schema/fields, data types and error message.

### Session 14 — Python API automation
<badge>Medium–Hard · 90 min</badge>

Use `requests` + `pytest`:
- create reusable API client/helper;
- validate status and response;
- validate negative cases;
- manage test data;
- avoid hard-coded secrets;
- keep tests independent.

Deliverable: runnable API test folder.

### Session 15 — SQL foundations
<badge>Medium · 60 min</badge>

Practice:
- SELECT, WHERE, ORDER BY;
- COUNT, GROUP BY, HAVING;
- INNER JOIN, LEFT JOIN;
- NULL handling;
- subqueries.

### Session 16 — SQL for defect investigation
<badge>Medium–Hard · 60–90 min</badge>

Scenarios:
- orders without payment records;
- duplicate emails;
- order count by status;
- customer with no orders;
- verify UI count against DB result.

Use a local practice database or approved read-only environment only.

Deliverable: `sql/validation_queries.sql` with comments and expected interpretation.

---

## Phase D — Python, Pytest and Playwright engineering

### Session 17 — Python coding for SDET
<badge>Medium · 60–90 min</badge>

Write and test:
- reverse string;
- palindrome;
- character frequency;
- remove duplicates while preserving order;
- second-largest unique number;
- merge dictionaries;
- count words;
- parse JSON safely.

For each problem: clarify input, handle edge cases, write function, write tests, explain complexity where relevant.

### Session 18 — OOP and clean test code
<badge>Medium · 60 min</badge>

Explain and demonstrate:
- class/object;
- inheritance vs composition;
- encapsulation;
- abstraction;
- exceptions;
- context managers;
- type hints.

Apply to a small API client or page object.

### Session 19 — Pytest framework design
<badge>Medium–Hard · 90 min</badge>

Build:
- test discovery;
- fixtures and scopes;
- yield teardown;
- parametrization;
- markers;
- conftest;
- configuration;
- useful assertions;
- failure diagnostics.

Deliverable: clean test framework with README run instructions.

### Session 20 — Playwright locator and reliability practice
<badge>Medium · 90 min</badge>

Automate:
- login;
- search;
- add to cart;
- sort products;
- validate checkout.

Use role/label/text/test-id locators as appropriate. Avoid brittle selectors and unnecessary `nth()`.

### Session 21 — Playwright framework and POM
<badge>Hard · 90–120 min</badge>

Build:
- page objects;
- fixtures;
- browser/context/page lifecycle;
- isolated test data;
- authentication/storage state where appropriate;
- environment config;
- reusable assertions/helpers.

Explain why business logic belongs in a page object/helper rather than duplicating selectors in every test.

### Session 22 — Debugging and flaky tests
<badge>Hard · 60–90 min</badge>

Investigate:
- unstable locator;
- race condition;
- shared test data;
- wrong wait strategy;
- environment instability;
- parallel test collision;
- test-order dependency.

For each failure, record evidence, root cause, correction and prevention. Do not “fix” every failure by adding a large timeout or blind retry.

---

## Phase E — Git, CI/CD and project integration

### Session 23 — Git workflow
<badge>Medium · 60 min</badge>

Practice:
- clone;
- status;
- add/commit;
- branch;
- switch;
- merge;
- pull/push;
- resolve a simple conflict;
- inspect log/diff.

Deliverable: repository with meaningful commits.

### Session 24 — CI pipeline
<badge>Medium–Hard · 90 min</badge>

Create a pipeline that:
- installs dependencies;
- runs lint/basic checks if configured;
- runs Pytest;
- stores test results;
- fails when required tests fail.

Then add Playwright browser installation and a small UI test job if the runner supports it.

### Session 25 — Reports and evidence
<badge>Medium · 60 min</badge>

Generate an HTML or Allure report (choose one first). Include:
- test name;
- status;
- duration;
- failure reason;
- screenshot/trace where useful.

Explain what a report proves and what it does not prove.

---

## Phase F — Capstone and interview defence

### Session 26 — Build test strategy
<badge>Medium · 60 min</badge>

Choose a demo e-commerce feature. Write:
- scope;
- risk;
- UI/API/DB boundaries;
- RACI;
- test types;
- environment;
- entry/exit criteria.

### Session 27 — Manual test pack
<badge>Medium · 90 min</badge>

Create:
- test scenarios;
- detailed cases;
- EP/BVA;
- decision table;
- state transitions;
- exploratory charter;
- defect reports.

### Session 28 — Automation integration
<badge>Hard · 2–3 hours</badge>

Add:
- API tests;
- UI tests;
- fixtures;
- POM;
- config;
- test data;
- reports.

### Session 29 — CI and project README
<badge>Hard · 90 min</badge>

Run tests from a clean checkout. Document:
- setup;
- commands;
- architecture;
- test scope;
- limitations;
- sample report;
- known risks.

### Session 30 — Mock interview and project defence
<badge>Hard · 60–90 min</badge>

Deliver a 5-minute project walkthrough:
1. Product and feature.
2. Risks and strategy.
3. Test design.
4. API/SQL checks.
5. Automation framework.
6. CI execution.
7. Defect example.
8. What you would improve next.

Then answer follow-up questions without reading notes.

---

# 4. Daily practice structure

For a 2-hour session:

| Time | Activity |
|---|---|
| 15 min | Recall previous topic without notes |
| 25 min | Learn/revise one concept |
| 45 min | Hands-on task |
| 20 min | Explain your approach aloud |
| 15 min | Update evidence and mistake log |

For a 3-hour session, extend hands-on practice and add a second scenario. Do not increase passive video time.

---

# 5. Weekly review

At the end of each 5–6 sessions, check:
- Can I explain the topic without reading?
- Can I apply it to a new feature?
- Can I produce an artifact?
- Can I explain why I chose this method?
- Can I identify limitations and risks?
- Can I answer a follow-up question?

If two or more answers are “no”, repeat the relevant session with a different example.

---

# 6. Progress tracker

| Session | Status | Evidence link / notes |
|---|---|---|
| 1–5 | Not started | |
| 6–10 | Not started | |
| 11–15 | Not started | |
| 16–20 | Not started | |
| 21–25 | Not started | |
| 26–30 | Not started | |

Use these status labels: `Not started`, `In progress`, `Needs revision`, `Passed L2`, `Passed L3`.

---

# 7. Mentor review rubric

Score each artifact from 0–4:

| Score | Meaning |
|---:|---|
| 0 | Missing / cannot explain |
| 1 | Copied or incomplete |
| 2 | Correct with prompts |
| 3 | Independent and mostly correct |
| 4 | Clear, justified, handles edge cases and follow-ups |

Review dimensions:
- correctness;
- coverage;
- clarity;
- reproducibility;
- maintainability;
- risk awareness;
- communication.

**Strict rule:** A test that passes once but cannot be explained, reproduced or maintained is not a strong automation deliverable.
