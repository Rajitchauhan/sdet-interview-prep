# QA / Automation QA / SDET Interview Cheat Sheet — 2026 Preparation

> **Purpose:** A practical interview workbook grounded in your Modules 1–10, your separate Pytest/Playwright learning, and a review of current 2026 QA/SDET interview material.
>
> **Important:** This is not a claim that every company asks the same questions. Interview rounds vary by job description, domain, seniority and stack. Use the job description to prioritise.

---

# 1. What interviewers are testing now

Current 2026 interview material and role-skill summaries point to a combination of:
- Testing fundamentals and test design.
- API testing and backend validation.
- SQL and data checks.
- Selenium/Playwright automation and framework design.
- Python/Java/TypeScript coding, depending on role.
- CI/CD, Git and debugging.
- Flaky-test diagnosis, test data and parallel execution.
- Scenario-based reasoning and communication.

Recent India-focused skill summaries list CI/CD, SQL, Selenium, API testing, Python and Playwright among frequently requested skills. These are sample-based reports, not a universal hiring census. SDET interview guides also describe coding, automation framework, API, CI/CD and testing-scenario rounds. Check the actual job description first.

**Practical implication:** Do not prepare only definitions. Expect “How would you test this?”, “Show me how you debug it”, “What would you automate?”, “Why did you choose this design?” and “What happens when this fails in CI?”

---

# 2. The answer framework — use this for most technical questions

Use **D-E-A-R**:

1. **D — Define:** Give a direct one- or two-sentence answer.
2. **E — Explain:** Explain how it works or why it matters.
3. **A — Apply:** Give a real example from course/lab/practice/project.
4. **R — Risks / trade-off:** Mention limitation, alternative or what you would check next.

Example: “What is regression testing?”

- Define: Re-running relevant existing tests after a change to check that previously working behavior has not broken.
- Explain: A code change can affect dependent features.
- Apply: After fixing coupon calculation, recheck login, product search, cart and checkout.
- Risk: Running every test manually may be slow, so prioritise risk and automate stable repetitive checks.

**Answer length guide:**
- Definition question: 20–40 seconds.
- Concept + example: 45–75 seconds.
- Scenario question: 1–2 minutes.
- Framework/project walkthrough: 3–5 minutes.

Do not stretch a simple answer into a speech. Answer the question, then stop and invite follow-up.

---

# 3. Your opening introduction

Use a truthful introduction. Adapt it to the actual job and your verified experience.

## 45–60 second version

“I have a software development background and hands-on experience with Python and web application development. I have been building my QA and automation skills around software testing fundamentals, STLC, Agile/Scrum, API testing, Pytest and Playwright. I focus on understanding requirements, designing meaningful positive and negative scenarios, validating APIs and building maintainable automation. I am now looking for a QA Automation role where I can combine my development background with a strong quality mindset.”

## If asked: “Why are you moving from development to QA?”

“My development experience helps me understand how applications are built, how UI, API and database layers interact, and how defects can originate. I found that I also enjoy analysing expected behaviour, identifying edge cases and improving product reliability. I am moving toward QA automation because it combines problem-solving, coding and product quality. I am not treating testing as only executing test cases; I want to contribute to test design, automation and reliable delivery.”

## If asked: “Are you an experienced QA professional?”

Be accurate. Do not convert development experience or course practice into professional QA employment.

“I have professional software development experience and I have been building practical QA automation capability through structured learning and hands-on projects. I can explain which parts I have used professionally and which parts I have practised in training projects.”

Replace this with your real dates, employer responsibilities and actual project evidence. Never claim production QA ownership unless it happened.

---

# 4. Fundamentals — high-frequency questions

## Q1. What is software testing?

**Answer:** Software testing evaluates a software product or component to find defects and provide information about quality and risk. It checks whether actual behaviour meets specified or expected behaviour.

**Add an example:** For login, test valid credentials, invalid credentials, empty fields, locked account and session behaviour.

## Q2. QA vs QC vs Testing?

- **QA:** Process-oriented; aims to prevent defects by improving the way software is developed.
- **QC:** Product-oriented; evaluates whether the product meets quality expectations.
- **Testing:** A major QC activity that exercises/reviews software to reveal defects and assess behaviour.

Avoid saying QA and testing are exactly the same.

## Q3. Verification vs Validation?

- **Verification:** Are we building the product right? Check work products against specifications, e.g. requirement/design review.
- **Validation:** Are we building the right product? Check whether the product meets user/business needs, e.g. executing acceptance tests.

## Q4. What are the seven testing principles?

1. Testing shows presence of defects, not their absence.
2. Exhaustive testing is impossible (except trivial cases).
3. Early testing saves time and cost.
4. Defects cluster in a small number of modules.
5. Pesticide paradox: repeated same tests may stop finding new defects; review/update tests.
6. Testing is context-dependent.
7. Absence-of-errors fallacy: defect-free software can still fail user needs.

Be ready to explain any two with examples.

## Q5. What is the difference between a test scenario and test case?

- Scenario: high-level condition or feature behaviour to test.
- Test case: specific preconditions, steps, test data and expected result.

Example:
- Scenario: Verify login with invalid password.
- Test case: Open login, enter registered email and wrong password, select Sign in, verify the expected error and that access is denied.

## Q6. What is a test plan?

A test plan describes the scope, objectives, approach, resources, schedule, environment, risks, entry/exit criteria and deliverables for a testing effort.

## Q7. What is the difference between test plan and test strategy?

A test strategy describes the overall testing approach/principles for a product, programme or organisation. A test plan applies an approach to a specific project/release/feature with scope, resources, schedule and execution details. Organisations may use these terms differently, so explain how your team uses them.

## Q8. What is STLC?

The course's six phases:
1. Requirement Analysis.
2. Test Planning.
3. Test Design.
4. Test Environment Setup.
5. Test Execution.
6. Test Cycle Closure.

Explain the output of each phase, not just the names.

## Q9. Smoke vs Sanity vs Retesting vs Regression?

- **Smoke:** Broad, shallow checks that a build's critical functions are stable enough for further testing.
- **Sanity:** Focused checks around a specific change/fix or affected area.
- **Retesting / Confirmation testing:** Re-run the failed test to verify that the specific defect has been fixed.
- **Regression:** Check that the change has not broken existing behaviour elsewhere.

## Q10. What is severity vs priority?

- Severity = technical/business impact of the defect.
- Priority = urgency/order in which the team should fix it.

Example:
- Payment processing fails for all users: high severity, high priority.
- Typo on a rarely used internal page: low severity, low priority.
- A legal/compliance text error may have high priority even if it does not crash the system.

Do not use a fixed mapping without understanding context.

---

# 5. Test design — scenario questions

## Q11. What is Equivalence Partitioning?

Divide input data into groups expected to behave similarly and select representative values.

Example: age 18–65 inclusive:
- below 18 = invalid partition;
- 18–65 = valid partition;
- above 65 = invalid partition.

Possible representatives: 17, 30, 66.

## Q12. What is Boundary Value Analysis?

Test values at and around the edges of input partitions.

For 18–65 inclusive:
- 17, 18, 19;
- 64, 65, 66.

Explain whether the interviewer expects 2-value or 3-value BVA if asked.

## Q13. What is Decision Table Testing?

Use a table when combinations of conditions determine business outcomes.

Example: discount depends on membership, cart value and coupon validity. List condition combinations and expected outcomes; derive tests from meaningful rules.

## Q14. What is State Transition Testing?

Model states and events that move a system between states.

Example: Order Created → Paid → Packed → Shipped → Delivered. Test valid and invalid transitions, repeated events and cancellation/refund rules.

## Q15. What is exploratory testing?

Testing where learning, test design and execution happen together. It is guided by a mission/charter and tester observations rather than only pre-written steps.

## Q16. How would you test a login page?

Answer in layers:

1. Requirements: registered user, password rules, lockout/session, error messages.
2. Positive: valid credentials.
3. Negative: wrong password, unknown user, empty fields, malformed email.
4. Boundaries: password min/max length.
5. Security: password masking, no sensitive data in URL/logs, session/logout, brute-force protections as specified.
6. Usability/accessibility: labels, keyboard navigation, error clarity.
7. API/data: authentication response, token/session behaviour, account state if accessible.
8. Regression: related flows such as forgot password and logout.
9. Automation: stable high-value paths at API/UI level.

Do not claim a security test passed unless you actually performed it.

## Q17. How would you test a shopping cart?

- Add/remove/update quantity.
- Quantity boundaries and stock limits.
- Price, tax, discount and rounding.
- Duplicate clicks and concurrent updates.
- Cart persistence after refresh/login.
- Out-of-stock product.
- Coupon eligibility/expiry/stacking.
- Checkout handoff and payment failure.
- API response and persisted order/cart data.
- Regression of product search and order history.

---

# 6. Course-specific questions — Modules 1–10

## Q18. Explain UI, API and DB layers.

UI is what the user interacts with. API carries requests/responses between frontend and backend/services. DB stores/retrieves persistent data. When a user submits a form, the browser may send an API request; backend logic validates/processes it and reads/writes data.

## Q19. Static vs Dynamic testing?

Static testing reviews work products without executing the software, such as requirements or design. Dynamic testing executes the software and checks actual behaviour.

## Q20. Functional vs Non-functional testing?

Functional testing checks what the system does against requirements. Non-functional testing checks quality characteristics such as performance, usability and security.

## Q21. Black-box vs White-box testing?

Black-box derives tests from external behaviour/specification without needing internal code knowledge. White-box uses internal structure/logic to derive tests, such as statements and branches.

## Q22. Explain the test environments.

- Dev: active development and initial checks.
- QA/Test: controlled formal functional/API/regression testing.
- Staging/UAT: production-like setup for final business acceptance.
- Production: live users and real data; only controlled, authorised validation/monitoring.

## Q23. Waterfall vs V-Model?

Waterfall is sequential phases. V-Model links development/specification stages with corresponding test levels. In the common mapping, user requirements ↔ acceptance testing, system requirements ↔ system testing, architecture ↔ integration testing, detailed design ↔ unit testing.

## Q24. Agile vs Waterfall?

Waterfall follows a largely sequential plan. Agile delivers work in shorter iterations/sprints, gathers feedback and adapts. QA should be involved throughout Agile work, not only at sprint end.

## Q25. What is CI/CD?

CI automatically integrates code changes and runs build/test checks. CD can mean Continuous Delivery or Continuous Deployment depending on context. Your Module 7 source specifically uses Continuous Deployment. Clarify the team's meaning before assuming.

## Q26. What is Shift-left testing?

Move quality activities earlier: review requirements, ask questions, define acceptance criteria and plan tests before implementation is complete. It complements, not replaces, later execution.

## Q27. Acceptance Criteria vs Definition of Done?

Acceptance Criteria are specific to one user story and define its expected behaviour. DoD is a team-wide minimum quality checklist that applies to every story. A story can pass AC but still fail DoD if code review or CI tests are incomplete.

## Q28. What is BDD?

BDD is a collaborative approach to defining expected behaviour from the user's perspective, commonly using Given-When-Then scenarios. Given = precondition, When = action, Then = observable result.

## Q29. What happens in Sprint Review?

Inspect the completed increment, gather stakeholder feedback and adapt the backlog. QA demonstrates a few high-value scenarios, not the entire test suite.

## Q30. How do you prepare for a stakeholder demo?

Use Context → Execution → Result (Tell–Show–Tell). Prepare stable environment/data, perform a dry run, explain the acceptance criterion, execute the scenario, then connect actual outcome to the expected Then clause.

## Q31. What is a RACI matrix?

Responsible performs the task; Accountable owns the final outcome; Consulted provides input; Informed receives updates. Use it to clarify UI/API/DB ownership.

---

# 7. API testing — likely technical round

## Q32. What is an API?

An API defines how software components communicate. In REST API testing, validate request method, URL, headers, authentication, payload, status, response body and side effects.

## Q33. GET vs POST vs PUT vs PATCH vs DELETE?

- GET: retrieve resource; should not modify server state.
- POST: submit data/create or trigger processing; not generally idempotent.
- PUT: replace/update a resource representation; designed to be idempotent.
- PATCH: partially modify a resource; idempotency depends on the operation.
- DELETE: remove a resource; intended to be idempotent in HTTP semantics.

Explain based on the endpoint contract, not just memorised verbs.

## Q34. Common status codes?

- 200 OK — request succeeded.
- 201 Created — resource created.
- 204 No Content — success, no response body.
- 400 Bad Request — invalid request.
- 401 Unauthorized — authentication missing/invalid.
- 403 Forbidden — authenticated/known caller lacks permission.
- 404 Not Found — resource/route not found.
- 409 Conflict — request conflicts with current state.
- 422 Unprocessable Content — syntactically valid but semantically invalid content, where API uses it.
- 429 Too Many Requests — rate limit.
- 500 Internal Server Error — unexpected server-side failure.
- 503 Service Unavailable — service temporarily unavailable.

Status semantics can depend on API contract; inspect response body and headers too.

## Q35. How do you test an API?

1. Understand endpoint contract.
2. Check method, path, query/path params and headers.
3. Test valid payload.
4. Test missing, invalid and boundary data.
5. Test authn/authz.
6. Validate status, response schema, fields and types.
7. Validate data side effects where possible.
8. Test duplicate/retry/idempotency behaviour.
9. Check response time against agreed expectations.
10. Record reproducible evidence.

## Q36. Authentication vs Authorization?

Authentication verifies who the caller is. Authorization checks what that caller is allowed to do.

## Q37. PUT vs PATCH?

PUT usually replaces the target resource representation; PATCH applies partial modifications. Validate omitted fields, null fields, repeated requests and endpoint contract.

## Q38. What is API automation?

Using code to send requests and assert status, headers, body, schema, business rules and side effects. It helps run repeatable checks quickly in CI.

---

# 8. SQL — tester questions

## Q39. How do you verify data saved from UI?

1. Perform the action in a safe test environment.
2. Capture a unique identifier (user/order ID).
3. Query the relevant table with read-only access.
4. Validate expected columns/values.
5. Check related tables and duplicates where needed.
6. Compare DB state with API/UI result.

## Q40. INNER JOIN vs LEFT JOIN?

- INNER JOIN returns matching rows from both tables.
- LEFT JOIN returns all rows from left table plus matching right rows; unmatched right-side columns are NULL.

## Q41. Find orders without payments.

```sql
SELECT o.order_id
FROM orders o
LEFT JOIN payments p
  ON p.order_id = o.order_id
WHERE p.order_id IS NULL;
```

Explain the join key and why NULL identifies missing matching payment rows.

## Q42. Count orders by status.

```sql
SELECT status, COUNT(*) AS order_count
FROM orders
GROUP BY status;
```

## Q43. Find duplicate emails.

```sql
SELECT email, COUNT(*) AS occurrences
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

Always adapt table/column names to the actual schema. Do not claim a query was run if you only wrote it on a whiteboard.

---

# 9. Python coding round — what to practise

For QA/SDET roles, practise writing small functions and tests, not only reciting Python definitions.

Common exercises:
1. Reverse a string.
2. Check palindrome.
3. Count character frequency.
4. Remove duplicates from list preserving order.
5. Find second-largest unique number.
6. Find missing number in a range.
7. Merge two dictionaries.
8. Find common elements in two lists.
9. Flatten a nested list (one level).
10. Parse JSON and handle missing keys.
11. Read a file and count lines/words.
12. Use `try/except/finally`.
13. Write a decorator or generator example.
14. Explain mutable vs immutable.
15. Explain list vs tuple vs set vs dict.
16. Explain OOP and composition.
17. Explain `*args`, `**kwargs`, lambda, comprehension.
18. Explain shallow vs deep copy.
19. Explain exception handling in automation.
20. Write unit tests for your own function.

**Answer method for coding:** clarify input/output → discuss edge cases → write readable solution → test normal/empty/invalid cases → explain complexity if relevant.

---

# 10. Pytest and framework questions

## Q44. What is a fixture?

A fixture provides reusable setup/data/resources to tests and can manage teardown. Use the narrowest appropriate scope; broad scope can introduce shared-state and isolation problems.

## Q45. Fixture scope?

- function: fresh for each test function.
- class: once per test class.
- module: once per module.
- package: once per package.
- session: once per test session.

Explain resource lifetime and isolation trade-offs.

## Q46. What does `yield` do in a fixture?

Code before `yield` is setup; code after `yield` is teardown after the test using the fixture completes.

## Q47. `@pytest.mark.parametrize`?

Runs the same test logic against multiple input/expected-output combinations. Useful for boundaries and negative cases.

## Q48. What is `conftest.py`?

A local pytest plugin/configuration file for sharing fixtures and hooks within a test directory hierarchy. Keep fixtures organised and avoid making every fixture global unnecessarily.

## Q49. What is mocking?

Replace a dependency with a controlled test double so a unit can be tested without relying on a real external service. `return_value` supplies a fixed return; `side_effect` can vary return values or raise exceptions. Patch the name where the code under test looks it up.

## Q50. How do you make tests independent?

Use controlled setup/teardown, unique test data, isolated contexts/resources, avoid test-order dependency, avoid mutable shared state, and clean up safely.

---

# 11. Playwright interview questions

## Q51. Browser, BrowserContext and Page?

- Browser: browser process/instance.
- BrowserContext: isolated browser session/profile with its own cookies/storage.
- Page: one tab/page inside a context.

Use separate contexts for user/session isolation.

## Q52. Why prefer role/label locators?

They align with user-facing semantics and accessibility, usually making tests more resilient than brittle DOM paths. Use stable test IDs where semantic locators are not suitable.

## Q53. What is auto-waiting?

Playwright waits for relevant actionability conditions before actions such as click, reducing many timing-related failures. It does not mean every application-specific condition is automatically understood; assert the actual expected state.

## Q54. What are actionability checks?

Depending on action, Playwright checks conditions such as visible, stable, enabled and receiving events. Know why an action may wait or fail.

## Q55. `to_have_text` vs `to_contain_text`?

- `to_have_text`: exact/full text expectation (depending on matcher/options).
- `to_contain_text`: expected text is present within the actual text.

Use the strictness appropriate to the requirement.

## Q56. What is Page Object Model?

A design pattern that encapsulates page locators and page-level actions so tests describe user intent and avoid repeating UI details. Do not put all test assertions/business workflows blindly into one giant page class.

## Q57. When use a new BrowserContext?

When tests need isolated cookies, local storage, authentication state or user sessions. Pages in the same context share that context's session state.

## Q58. How do you handle flaky Playwright tests?

Investigate root cause:
- unstable locator;
- race condition;
- missing app-ready condition;
- shared data;
- test-order dependency;
- environment/network;
- parallel collision.

Use trace, screenshot, logs and network evidence. Avoid using `force=True`, arbitrary long sleeps or retries as the first solution.

## Q59. How do you handle file upload/download?

Upload using `set_input_files()` or appropriate file chooser flow. Download with `expect_download()` and validate the downloaded file name/content/path as appropriate.

## Q60. How do you handle frames?

Use `frame_locator()` to locate elements inside an iframe; chain nested frame locators for nested frames. Confirm the frame is the correct one and avoid brittle positional selection.

## Q61. Sync vs Async Playwright?

Sync API uses blocking calls and is often simpler for straightforward pytest scripts. Async API uses `async/await` and fits asynchronous Python applications or concurrent async workflows. Choose one style consistently in a test suite.

---

# 12. CI/CD, Git and framework architecture

## Q62. How would you run tests in CI?

On push/PR:
1. Checkout code.
2. Set up Python/runtime.
3. Install dependencies.
4. Install browser binaries if needed.
5. Run unit/API/UI tests by stage or job.
6. Publish reports/artifacts.
7. Fail required quality gates on test failures.
8. Notify team and preserve diagnostic evidence.

Exact workflow depends on GitHub Actions/Jenkins/GitLab CI and project constraints.

## Q63. What should not be automated?

Not every test is worth automating. Avoid automating:
- unstable requirements;
- one-off checks with low repeat value;
- subjective usability judgement without a clear oracle;
- workflows whose maintenance cost exceeds benefit;
- scenarios better covered at API/unit level than through slow UI E2E.

Automate stable, repeatable, high-value regression and business-critical flows.

## Q64. Test pyramid?

A useful strategy is many fast unit/component tests, a meaningful set of API/integration tests, and a smaller number of high-value UI E2E tests. It is a guide, not a rigid numeric rule.

## Q65. How would you explain your automation framework?

Use this order:
1. Language and test runner.
2. Directory structure.
3. Config/environment management.
4. Fixtures and lifecycle.
5. Page Objects/helpers/API clients.
6. Test data strategy.
7. Assertions and reporting.
8. Parallelism and isolation.
9. CI execution.
10. Failure diagnostics and known limitations.

Only describe components that your project actually contains.

## Q66. How do you handle secrets?

Use CI secret storage/environment variables or an approved secret manager. Do not hard-code passwords/tokens in source control or screenshots.

---

# 13. Scenario-based questions — practise thinking aloud

Use this structure:
1. Clarify assumptions.
2. Identify users/roles and main workflow.
3. Identify positive/negative/boundary cases.
4. Identify state/data/dependencies.
5. Prioritise by risk.
6. Decide test level (unit/API/UI/E2E).
7. Explain evidence and exit criteria.

Practice:
- How would you test a lift/elevator?
- How would you test an ATM cash withdrawal?
- How would you test an e-commerce checkout?
- How would you test a password reset?
- How would you test a search box?
- How would you test a file upload?
- How would you test pagination?
- How would you test an order cancellation/refund?
- How would you test a login lockout after repeated failures?
- How would you test a feature when requirements are incomplete?

Do not start listing random cases. Clarify the intended behaviour and risk first.

---

# 14. If your mind goes blank in an interview

This is a skill to practise, not something to hide. Do not panic, bluff or invent an answer.

## The 5-step recovery method

### Step 1 — Pause
Take 2–3 seconds. A short pause is better than rushing into an incorrect answer.

Say:
“Let me think through that for a moment.”

### Step 2 — Repeat/reframe the question
Confirm what is being asked.

Say:
“If I understand correctly, you're asking how I would verify that the order is created correctly after checkout.”

### Step 3 — Start from a framework you know
For testing scenarios:
- requirement;
- positive path;
- negative path;
- boundaries;
- data/API;
- regression/risk.

For a concept:
- definition;
- purpose;
- example;
- limitation.

For debugging:
- reproduce;
- collect evidence;
- isolate layer;
- identify root cause;
- verify fix;
- regression.

### Step 4 — State what you know and what you do not
If you cannot recall a term, explain the underlying idea honestly.

Say:
“I don't recall the exact term right now, but the approach I would use is…”

Or:
“I haven't used that tool in a production project. I understand its purpose, and I can explain how I would approach it in a controlled setup.”

### Step 5 — Think aloud and recover
Break the problem into smaller pieces. Interviewers can assess your reasoning even if you do not immediately remember a definition.

## Exact recovery phrases

**When you forget a definition:**
“I know the concept, but I am not recalling the exact wording. Let me explain it with an example.”

**When you need clarification:**
“Can I clarify one assumption before I answer? Should I consider only the normal user flow, or also admin and failure scenarios?”

**When you don't know a tool:**
“I haven't used that tool hands-on yet. I have worked with a similar workflow using [truthful tool/approach]. The concepts I would transfer are…”

**When you make a mistake:**
“Let me correct that. I mixed up the two terms. The correct distinction is…”

**When a coding solution is not coming:**
“I'll first clarify the input and expected output, then handle the normal case and edge cases. I'll start with a simple correct solution and improve it if needed.”

**When you need time:**
“Could I take a few seconds to structure the answer?”

## What NOT to do

- Do not say “I know everything but forgot.”
- Do not bluff with technical jargon.
- Do not invent production experience.
- Do not argue when interviewer corrects you.
- Do not go silent for a long time; explain your reasoning.
- Do not apologise repeatedly.
- Do not turn one forgotten detail into a claim that you know nothing.

## Practice drill for blank moments

Ask a friend/mentor to interrupt you with:
- “Why?”
- “What if the API returns 500?”
- “What if two users do it simultaneously?”
- “How do you know the test passed?”
- “What would you automate?”
- “What could make this flaky?”

Train yourself to pause, clarify, structure and answer.

---

# 15. Behavioural questions — use STAR

STAR:
- **S — Situation:** Context.
- **T — Task:** Your responsibility.
- **A — Action:** What you personally did.
- **R — Result:** Outcome, evidence or learning.

Prepare truthful stories for:
1. A difficult defect you investigated.
2. A disagreement with a developer.
3. A time requirements were unclear.
4. A time you missed something and what you learned.
5. A time you improved a process or test.
6. A deadline where you prioritised risk.
7. A flaky test you debugged.
8. A time you learned a new tool quickly.

If you have no professional QA story, use a training project honestly and label it as a practice project.

---

# 16. Questions you should ask the interviewer

Choose 2–3 relevant questions:
- What is the current automation stack and what percentage of regression is automated?
- How are UI, API and database tests divided?
- How are tests executed in CI, and how are failures triaged?
- What is the team's definition of done?
- How does QA participate in backlog refinement and sprint planning?
- What are the main quality challenges for this product?
- What would success look like in the first 90 days?

Avoid asking all questions mechanically. Pick those relevant to the conversation.

---

# 17. Final 24-hour revision checklist

- [ ] 60-second introduction.
- [ ] Why QA / why automation?
- [ ] QA/QC/testing, verification/validation.
- [ ] Seven testing principles.
- [ ] STLC and test levels/types.
- [ ] Smoke/sanity/retest/regression.
- [ ] EP/BVA/decision table/state transition.
- [ ] Severity vs priority and defect lifecycle.
- [ ] Test plan/strategy, risk and exit criteria.
- [ ] Agile, DoD, BDD, Sprint Review.
- [ ] API methods/status/authentication.
- [ ] SQL joins and aggregation.
- [ ] Python coding exercises.
- [ ] Pytest fixtures/parametrize/markers.
- [ ] Playwright locators/auto-waiting/POM/context.
- [ ] CI pipeline and flaky test diagnosis.
- [ ] One project walkthrough.
- [ ] Three STAR stories.
- [ ] Blank-moment recovery phrases.
- [ ] Two questions to ask interviewer.

---

# 18. Interview self-scoring rubric

Score each answer 0–4:

| Score | Description |
|---:|---|
| 0 | No answer / incorrect |
| 1 | Memorised definition only |
| 2 | Correct explanation but no example |
| 3 | Explanation + relevant example + practical detail |
| 4 | Clear, structured, handles trade-offs and follow-ups |

A strong interview answer is not necessarily long. It is accurate, structured, relevant and honest.

---

# 19. Current interview trend references

The following public material was reviewed on **31 October 2026**. It is directional evidence, not a universal survey of every employer.

1. India-focused 2026 QA role skill sample: CI/CD, SQL, Selenium, API testing, Python and Playwright are among listed skills. The source describes a sample of 100 postings from 38 companies collected July–September 2026; treat percentages as that sample only: https://resumaxx.com/resume-job-description-match/qa-engineer
2. 2026 SDET interview guide describes coding, test design, Playwright/Selenium framework discussion, API testing and CI/CD as common areas: https://techscreen.app/articles/sdet-qa-automation-interview-guide-2026
3. 2026 QA automation interview guide highlights framework design, flaky tests, API/contract testing, CI and coding: https://www.ryzlabs.com/interview-questions/qa-automation
4. Naukri Code 360 interview experience (Automation Engineer, Jan 2026, 0–2 years) includes API experience and coding questions: https://www.naukri.com/code360/interview-experiences/setu/interview-experience-automation-engineer-jan-2026-exp-0-2-years
5. ISTQB CTFL v4.0.1 syllabus covers test fundamentals, lifecycle, static testing, test analysis/design, management and tools: https://www.istqb.org/certifications/ctfl/

**How to use these references:** Match your preparation to the job description. A manual QA role may emphasise test design, Jira, SQL and API basics; an automation/SDET role is more likely to probe coding, framework design, API automation, CI and debugging. Do not assume every role asks every topic.

---

# Final rule

**Do not memorise this document word for word.** Practise each answer aloud, replace examples with your own truthful work, and be ready for “why?”, “how do you know?”, “what if it fails?” and “what would you do next?”
