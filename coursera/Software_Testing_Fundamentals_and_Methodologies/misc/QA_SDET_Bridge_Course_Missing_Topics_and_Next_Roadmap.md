# QA/SDET Bridge Course — Missing Topics, Knowledge Gaps & Next Learning Path

> **Purpose:** Your first 10 course modules have built a foundation in software testing, web layers, STLC, environments, SDLC models, Agile/Scrum, BDD, Jira/Azure DevOps, Sprint Reviews and a QA Strategy project. This document identifies what is still needed to become interview-ready and practically capable as a QA Automation Engineer / SDET.
>
> **Source discipline:** “Covered in Modules 1–10” refers to the uploaded course ZIPs and their transcripts/activities. “Bridge topic” means it was not sufficiently taught in those ZIPs. “Previously practised separately” refers to our earlier Pytest/Playwright/API learning, not to the Coursera module contents.

---

# 1. What the first 10 modules actually covered

| Course area | What the uploaded course covered | Readiness note |
|---|---|---|
| Testing mindset and principles | QA vs QC, UAT, SDLC roles, testing principles, defect reporting, testing mindset | Foundation |
| Web architecture | UI, API, DB layers; browser DevTools; tracing data flow | Foundation |
| Static/dynamic and test levels | Static vs dynamic testing; unit, integration and higher test levels | Foundation |
| Test types and STLC | Functional, non-functional, black-box, white-box, performance, usability, maintenance, regression; six STLC phases | Foundation |
| Environments | Dev, QA, staging/UAT, production; choosing environments; production risks | Foundation |
| SDLC models | Waterfall, V-Model, Agile introduction, Jira/Azure DevOps board concepts | Foundation |
| Agile and CI/CD | Agile vs Waterfall vs CI/CD; QA through sprint; pipeline test checkpoints | Foundation |
| Scrum testing | Backlog refinement, DoD, acceptance criteria, BDD/Gherkin, Jira backlog, ADO mapping | Foundation + lab |
| Sprint Review | Scenario selection, demo preparation, Context–Execution–Result, failure recovery | Foundation |
| QA strategy project | UI/API/DB ownership, RACI, static/dynamic strategy, staging, BDD, defect evidence | Practical project outline |

## What is not automatically proven by completing the course

Completing a lesson or reading a guide does not prove that you can:
- derive test cases from a new requirement without notes;
- write a strong bug report from an observed failure;
- explain a testing decision with business risk;
- test an API independently;
- validate backend data with SQL;
- write and debug maintainable automation;
- diagnose flaky tests or CI failures;
- explain a real project architecture and defend your choices.

**Readiness is demonstrated by output:** test cases, executed tests, defect reports, SQL queries, API collections, automation code, pipeline runs and clear verbal explanations.

---

# 2. Gap analysis — what to add next

Priority meanings:
- **P0 — Must learn before applying/interviewing for QA roles.**
- **P1 — Strongly expected for Automation QA / SDET roles.**
- **P2 — Valuable differentiator or role-dependent.**

| Missing / under-covered topic | Priority | Why it matters | Expected practical output |
|---|---:|---|---|
| Equivalence Partitioning and Boundary Value Analysis in depth | P0 | Derive efficient tests from input ranges/classes | Test set for age, amount, password limits |
| Decision Table Testing | P0 | Validate combinations of business rules | Discount/eligibility rule table |
| State Transition Testing | P0 | Test workflows, status changes and invalid transitions | Order/login-lock state model |
| Error guessing and exploratory testing | P0 | Discover risks not obvious from requirements | Exploratory charter + findings |
| Test case design and review | P0 | Convert requirements into executable cases | Test scenarios, test cases, test data |
| Severity vs Priority | P0 | Communicate impact and urgency correctly | Defect triage examples |
| Defect lifecycle and retesting vs regression | P0 | Manage bugs through resolution | Defect lifecycle workflow |
| Test plan vs test strategy; entry/exit criteria | P0 | Plan and control test work | One-page test plan |
| Risk-based testing and prioritisation | P0 | Decide what to test first under time pressure | Risk matrix and priority order |
| RTM / traceability and coverage | P1 | Link requirements to tests and defects | Requirement-to-test mapping |
| Test estimation, progress and test summary | P1 | Communicate scope, progress and release risk | Estimate + summary report |
| API testing fundamentals and automation | P0 | QA roles commonly validate backend behavior | Postman collection + Python requests tests |
| SQL for testers | P0 | Verify persisted data and investigate defects | SELECT, JOIN, GROUP BY, subqueries |
| Git and Linux command-line basics | P1 | Test code and CI workflows live in repositories | Clone, branch, commit, logs, shell basics |
| Python coding for SDET | P0 | Automation interviews include coding/problem solving | Functions, collections, strings, OOP, exceptions |
| Pytest framework design | P1 | Fixtures, parametrisation, markers, plugins, reports | Maintainable test framework |
| Playwright framework design | P1 | Reliable UI automation is more than locator syntax | POM, fixtures, config, traces, parallel runs |
| CI/CD hands-on (GitHub Actions/Jenkins) | P1 | Explain and demonstrate pipeline execution | Tests run on push/PR |
| Debugging flaky tests | P1 | A reliable suite must be diagnosable | Root-cause investigation notes |
| Performance testing basics | P2 | Some roles require load/performance awareness | k6/JMeter simple load test and metrics |
| Security testing basics | P2 | Understand auth, access control and common risks | Basic OWASP-oriented test checklist |
| Accessibility testing basics | P2 | Keyboard, labels, contrast and semantics affect usability | Accessibility smoke checklist |
| Mobile/responsive testing | P2 | Mobile viewport and device behavior matter | Responsive test matrix |
| Test reporting (Allure/HTML) | P1 | Stakeholders need readable execution evidence | Report attached to a test run |

---

# 3. Important testing techniques to complete

The first 10 modules mention Equivalence Partitioning and Boundary Value Analysis, but the uploaded material does not provide a full practical course in all major test-design techniques. The following should be taught and practised separately.

## 3.1 Equivalence Partitioning (EP)

Divide input values into groups expected to behave similarly. Choose representative values from each valid/invalid partition.

**Example — age allowed from 18 to 65 inclusive:**
- Invalid: below 18
- Valid: 18 to 65
- Invalid: above 65

Representative values could be 17, 30, 66.

## 3.2 Boundary Value Analysis (BVA)

Test values at and around partition boundaries.

For 18–65 inclusive, a useful 2-value boundary set is:
- 17, 18
- 65, 66

For a richer 3-value approach, include boundary and adjacent values around each edge:
- 17, 18, 19
- 64, 65, 66

## 3.3 Decision Table Testing

Use when multiple conditions combine to determine an outcome.

**Mentor-created example — discount eligibility:**
- Is customer a member?
- Is cart total at least ₹2,000?
- Does coupon remain valid?

Build combinations and expected outcomes. Do not test only one condition at a time if the business rule depends on combinations.

## 3.4 State Transition Testing

Use when an entity moves between states due to events.

**Mentor-created example — order lifecycle:**
`Created → Paid → Packed → Shipped → Delivered`

Test:
- valid transitions;
- invalid transitions (e.g. Delivered → Packed);
- repeated events;
- cancellation/refund paths;
- role permissions for transitions.

## 3.5 Exploratory testing and error guessing

Exploratory testing combines learning, test design and execution. Use a time-boxed charter, record what you explored and what you discovered.

Error guessing uses experience and product knowledge to anticipate likely failures:
- empty fields;
- duplicate submissions;
- expired sessions;
- slow network;
- repeated clicks;
- special characters;
- stale browser state.

**External reference:** ISTQB CTFL v4.0.1 includes EP, BVA, decision tables, state transitions, statement/branch testing, error guessing and exploratory testing. Use the current official syllabus and sample exams as a structured reference, not as a substitute for hands-on practice.

---

# 4. Recommended next course

## Course name

**QA Automation Engineer / SDET Practical Engineering — From Testing Foundations to Interview-Ready Projects**

This is the natural next step after Modules 1–10. It should not repeat the same foundation lessons. It should convert concepts into practical skills and evidence.

## Proposed modules

| Next module | Topic | Main deliverable |
|---|---|---|
| 11 | Test Design Techniques Deep Dive | EP, BVA, decision table, state transition, exploratory charter |
| 12 | Test Management & Defect Engineering | Bug lifecycle, severity/priority, risk, RTM, exit criteria, test summary |
| 13 | API Testing for QA | Postman, HTTP semantics, auth, negative tests, schema/contract basics |
| 14 | SQL for Testers | Joins, aggregation, subqueries, data validation |
| 15 | Python for SDET Interviews | Coding drills, collections, strings, OOP, exceptions, files, debugging |
| 16 | Pytest Engineering | Fixtures, parametrisation, markers, conftest, config, plugins, reporting |
| 17 | Playwright Engineering | Locator strategy, waits/actionability, POM, contexts, storage state, downloads, frames |
| 18 | Automation Framework Project | UI + API tests, test data, configuration, reusable components |
| 19 | Git, CI/CD & Reports | Git workflow, GitHub Actions/Jenkins, reports, artifacts, failure diagnosis |
| 20 | Reliability & Quality Engineering | Flaky tests, parallelism, retries, test pyramid, performance/security/accessibility basics |
| 21 | Capstone Project & Interview Defence | End-to-end QA project, README, evidence, architecture walkthrough, mock interview |

## Suggested capstone

**MindBridge / E-commerce QA project** — use a training application or a safe demo application, not a real production system.

Project should include:
1. Product requirements and assumptions.
2. QA strategy and RACI.
3. Test scenarios and test cases.
4. EP/BVA/decision-table/state-transition examples.
5. Bug reports with screenshots and evidence.
6. API tests.
7. SQL validation exercises (against a local training database).
8. Pytest test framework.
9. Playwright UI automation with Page Objects.
10. CI pipeline and test report.
11. Known limitations and release-risk summary.

**Definition of project-ready:** You can clone the repository, run the tests, explain the architecture, show a real failure, diagnose it, and justify what should/should not be automated.

---

# 5. How to decide that a topic is actually learned

Use three levels:

| Level | What you can do | Status |
|---|---|---|
| L1 — Recall | Explain the concept in your own words without reading | Basic understanding |
| L2 — Apply | Solve a new scenario or write a test without copying an example | Practical understanding |
| L3 — Defend | Explain why you chose that approach, alternatives, risks and limitations | Interview / project readiness |

A topic is not complete just because you watched a video or copied notes. Aim for L3 on P0 topics and at least L2 on P1/P2 topics.

---

# 6. External references to use carefully

- ISTQB CTFL v4.0.1 syllabus and sample exams: https://www.istqb.org/certifications/ctfl/
- ISTQB official India board / CTFL information: https://www.istqb.in/
- The ISTQB syllabus is useful for systematic test-design and test-management coverage. It does not replace hands-on API, SQL, Python, Playwright and CI project practice.

---

# Final mentor recommendation

Do not start another broad theory course immediately. First complete the bridge modules and build one project that combines manual testing, API, SQL, Python, Playwright and CI.

The first priority should be:
1. Test design techniques + defect engineering.
2. API + SQL.
3. Python coding + Pytest/Playwright framework work.
4. Git + CI/CD.
5. Capstone + interview defence.

This path turns the first 10 modules from “course completion” into demonstrable QA/SDET capability.
