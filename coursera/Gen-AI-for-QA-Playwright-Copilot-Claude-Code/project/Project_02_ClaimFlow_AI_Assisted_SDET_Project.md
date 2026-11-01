# PROJECT 02 — ClaimFlow Insurance Claims SDET Automation
## AI-assisted project: AI ko assistant/teammate ki tarah use karna, decision-maker ki tarah nahi

**Level target:** 2-year experience SDET / QA Automation Engineer  
**Primary stack:** Python, Pytest, Playwright Python, Requests, Git, GitHub Actions  
**AI tools:** ChatGPT / Claude / Copilot / CLI coding agent (jo tumhare paas available ho)  
**Language:** Hinglish teaching + professional English requirements/prompts/artifacts

> **Project 02 ka goal:** AI se project banwana nahi; AI ke saath engineering karna seekhna. Tum requirements samjhoge, AI se analysis karwaoge, output verify karoge, code review karoge, tests run karoge, failures debug karoge, aur final ownership tumhari hogi.

**Security note:** Insurance/claim data sensitive hota hai. Is training project mein synthetic data only. Real customer PII, policy numbers, medical documents, credentials, tokens, or confidential company code public AI tools mein paste nahi karna.

---

# 0. Product and your role

## 0.1 Product: ClaimFlow

ClaimFlow ek fictional insurance claims portal hai. Policy holder claim submit karta hai; claims officer claim review karta hai; supervisor approve/reject karta hai.

Roles:
- **Customer:** claim create, own claims view, supporting documents upload.
- **Claims Officer:** assigned claims view, request information, recommend decision.
- **Supervisor:** approve/reject eligible claims, audit trail review.
- **Admin:** user/role management (training scope mein limited).

## 0.2 Business workflow

```text
Customer submits claim
        |
        v
Claim status = SUBMITTED
        |
        v
Claims Officer reviews
        |
        +---- Missing information ----> NEEDS_INFORMATION
        |                                  |
        |                                  v
        |                           Customer responds
        |                                  |
        |                                  v
        |                           UNDER_REVIEW
        |
        v
Officer recommends decision
        |
        v
Supervisor decision
       / \
      /   \
 APPROVED  REJECTED
```

## 0.3 Tumhara role

Tum SDET ho. Tum:
1. Requirements and role permissions analyze karoge.
2. AI se initial risk/scenario ideas nikalwaoge.
3. AI output ko critique karke correct test design banaoge.
4. Framework architecture decide karoge.
5. AI se small implementation tasks mein help loge.
6. Har generated code ko inspect/run/test karoge.
7. AI-generated bugs/hallucinations identify karoge.
8. CI pipeline aur reports integrate karoge.
9. Defects, test gaps, and release risks communicate karoge.

---

# 1. Client requirement pack (professional English)

## Feature CF-001 — Submit a claim

**Business requirement:**  
An authenticated customer must be able to submit an insurance claim against an active policy owned by that customer.

**Acceptance criteria:**
- AC1: Only authenticated customers can submit a claim.
- AC2: A customer can submit a claim only against a policy they own.
- AC3: Policy must be active on the date of loss.
- AC4: Claim amount must be greater than zero.
- AC5: Loss date cannot be in the future.
- AC6: Required claim description must not be blank.
- AC7: Successful submission creates a unique claim reference.
- AC8: New claim status is `SUBMITTED`.
- AC9: Customer can view only their own claims.

## Feature CF-002 — Claims officer review

- AC1: Claims officer can view claims assigned to them.
- AC2: Claims officer cannot approve/reject a claim directly.
- AC3: Officer can request missing information.
- AC4: Requesting information changes status to `NEEDS_INFORMATION`.
- AC5: Every status change records actor, timestamp, old status, and new status.

## Feature CF-003 — Supervisor decision

- AC1: Supervisor can approve/reject claims in `UNDER_REVIEW`.
- AC2: Supervisor cannot decide on an unassigned or already closed claim.
- AC3: Rejection requires a reason.
- AC4: Approval requires an eligible claim and documented officer recommendation.
- AC5: Decision is recorded in audit history.

## Feature CF-004 — Document upload

- AC1: Only claim owner can upload documents for their claim.
- AC2: Supported formats: PDF, JPG, PNG.
- AC3: Maximum file size: 5 MB.
- AC4: Empty files and unsupported file types are rejected.
- AC5: File name and upload metadata are stored safely.
- AC6: Uploaded document is not publicly accessible without authorization.

**Clarifications required before implementation:**
- Is amount capped by policy coverage?
- Are duplicate claims allowed for same policy and loss date?
- Is a claim editable after submission?
- What happens if a policy expires after loss but before claim submission?
- Are multiple documents allowed?
- What is the exact retention policy?

Do not ask AI to invent business rules. Ask AI to list ambiguities; product owner supplies answers. For this training exercise, record assumptions explicitly.

---

# 2. AI collaboration rules

## 2.1 Four non-negotiable rules

1. **You own correctness.** AI output is a proposal, not proof.
2. **Small tasks only.** One feature/file/test at a time.
3. **Evidence required.** No claim of success without command output/test result.
4. **No blind overwrite.** Review diff before accepting code.

## 2.2 AI workflow

```text
You provide requirement + context
          |
          v
AI analyzes and asks questions
          |
          v
You validate assumptions
          |
          v
AI proposes test scenarios / design
          |
          v
You review and approve
          |
          v
AI helps implement one small task
          |
          v
You inspect diff and run tests
          |
          v
Failure? ---- yes ----> manual debugging + AI hypotheses
   |
   no
   v
Commit + update traceability + report
```

## 2.3 Project context file

Create `AGENTS.md` in repository root. It helps AI tools understand project rules. It is not a security boundary.

```markdown
# ClaimFlow SDET Project Rules

## Stack
- Python 3.12
- Pytest
- Playwright Python sync API
- Requests for API tests
- Page Object Model for UI behavior

## Engineering rules
- Do not invent API endpoints, UI labels, selectors, or business rules.
- Ask for missing requirements instead of guessing.
- Use semantic Playwright locators first.
- Do not use time.sleep() as a default synchronization strategy.
- Do not use force=True to hide actionability problems.
- Tests must be independent and deterministic.
- Never hardcode credentials, tokens, or personal data.
- Use synthetic test data only.
- Add assertions for business outcomes, not implementation details.
- Keep changes small and explain each changed file.
- Do not claim tests passed unless command output proves it.
- Preserve existing behavior unless a requirement explicitly changes it.
- Include negative and authorization tests for role-protected operations.
```

---

# 3. Phase 1 — Requirement analysis with AI

## 3.1 Prompt 1: requirement decomposition

Copy this prompt and attach/paste only the synthetic training requirement:

```text
You are acting as a senior SDET reviewing a product requirement.

Do not write code yet.

Analyze the requirement and return:
1. Actors and roles
2. Preconditions
3. Main success flow
4. Negative flows
5. Boundary cases
6. Authorization/security risks
7. Data validation rules explicitly stated
8. Ambiguities that require product-owner clarification
9. Acceptance-criteria-to-test-scenario mapping

Rules:
- Do not invent missing business rules.
- Label every assumption as an assumption.
- Quote the requirement phrase supporting each derived rule.
- Ask concise clarification questions.
- Prioritize scenarios P0/P1/P2 and explain why.
```

**Tum kya verify karoge?**
- Kya AI ne customer aur officer ke permissions mix to nahi kiye?
- Kya future loss date negative case identify hua?
- Kya policy ownership authorization case included hai?
- Kya AI ne undocumented amount limit invent to nahi ki?
- Kya every acceptance criterion covered hai?

## 3.2 Prompt 2: challenge AI

```text
Review your previous test analysis as a skeptical QA lead.
Find:
- Missing negative tests
- Missing boundary tests
- Authorization gaps
- Duplicate or low-value scenarios
- Assumptions presented as facts
- Requirements that cannot yet be tested because expected behavior is unclear

Return a corrected scenario list and explain every change.
Do not generate code.
```

## 3.3 Your deliverable

Create `docs/requirements/claimflow_analysis.md`:
- requirement summary
- roles/permissions matrix
- clarification log
- assumptions
- test scenarios
- P0/P1/P2 rationale

AI output ko direct paste mat karo. Tumhare review ke baad final document banao.

---

# 4. Phase 2 — Test design and traceability

## 4.1 Roles and permissions matrix

| Action | Customer | Claims Officer | Supervisor |
|---|---:|---:|---:|
| Submit own claim | Yes | No | No |
| View own claim | Yes | No | No |
| View assigned claim | No | Yes | Yes (authorized scope) |
| Request information | No | Yes | Yes (if business permits) |
| Recommend decision | No | Yes | No |
| Approve/reject | No | No | Yes |
| View audit history | Own claim only | Assigned claim | Authorized scope |

This is a training assumption. Confirm exact role permissions before treating it as product truth.

## 4.2 High-priority test scenarios

| ID | Scenario | Priority |
|---|---|---|
| CLM-01 | Customer submits valid claim | P0 |
| CLM-02 | Anonymous user submits claim | P0 |
| CLM-03 | Customer submits against another user's policy | P0 |
| CLM-04 | Claim amount zero | P1 |
| CLM-05 | Negative claim amount | P1 |
| CLM-06 | Future loss date | P1 |
| CLM-07 | Blank description | P1 |
| CLM-08 | New claim status is SUBMITTED | P0 |
| CLM-09 | Customer views own claim | P0 |
| CLM-10 | Customer views another user's claim | P0 |
| CLM-11 | Officer sees assigned claim | P0 |
| CLM-12 | Officer attempts approval | P0 |
| CLM-13 | Officer requests information | P1 |
| CLM-14 | Supervisor approves eligible claim | P0 |
| CLM-15 | Supervisor rejects without reason | P1 |
| CLM-16 | Closed claim decision attempted again | P1 |
| DOC-01 | Valid PDF upload | P1 |
| DOC-02 | Unsupported extension upload | P1 |
| DOC-03 | File larger than 5 MB | P1 |
| DOC-04 | Other customer downloads document | P0 |

## 4.3 AI test case review prompt

```text
Act as a QA lead. Review these test scenarios against the supplied acceptance criteria.

For each scenario, assess:
- Requirement coverage
- Expected result clarity
- Test data required
- Independence
- Risk/priority
- Whether it belongs at API, UI, or both levels

Do not add unapproved business rules.
Return gaps separately from recommended improvements.
```

**Quality gate:** Test design tab tak complete nahi jab tak every AC traceable na ho and critical authorization boundaries covered na hon.

---

# 5. Phase 3 — Repository and framework setup

## 5.1 Create project

```bash
mkdir claimflow-sdet
cd claimflow-sdet
git init
python -m venv .venv
```

Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

Install:
```bash
python -m pip install --upgrade pip
pip install pytest playwright requests python-dotenv pytest-html
playwright install
pip freeze > requirements.txt
```

## 5.2 Structure

```text
claimflow-sdet/
├── AGENTS.md
├── README.md
├── requirements.txt
├── pytest.ini
├── .env.example
├── .gitignore
├── config/
│   └── settings.py
├── docs/
│   ├── requirements/
│   ├── test-design/
│   ├── bug-reports/
│   └── test-summary/
├── src/
│   ├── api/
│   │   └── client.py
│   ├── pages/
│   └── utils/
│       └── logger.py
├── tests/
│   ├── api/
│   └── ui/
└── .github/
    └── workflows/
        └── tests.yml
```

## 5.3 Ask AI to review architecture, not invent it

```text
Review this proposed Python/Pytest/Playwright repository structure for a role-based claims portal.

Return:
1. Responsibilities of each folder
2. Missing essential files
3. Risks of overengineering
4. A minimal implementation order

Do not create files or code yet.
Do not add tools unless they solve a stated need.
```

Tum architecture ko samjho. Har proposed folder ka purpose explain kar pao.

---

# 6. Phase 4 — Configuration and API client

`config/settings.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")
API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000/api")
TIMEOUT = int(os.getenv("TIMEOUT", "10"))
```

`.env.example`:

```env
BASE_URL=http://127.0.0.1:8000
API_BASE_URL=http://127.0.0.1:8000/api
TIMEOUT=10
```

`src/api/client.py`:

```python
import requests

class ApiClient:
    def __init__(self, base_url: str, timeout: int = 10, token: str | None = None):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        if token:
            self.session.headers.update(
                {"Authorization": f"Bearer {token}"}
            )

    def get(self, path: str, **kwargs):
        return self.session.get(
            f"{self.base_url}/{path.lstrip('/')}",
            timeout=self.timeout,
            **kwargs,
        )

    def post(self, path: str, **kwargs):
        return self.session.post(
            f"{self.base_url}/{path.lstrip('/')}",
            timeout=self.timeout,
            **kwargs,
        )

    def patch(self, path: str, **kwargs):
        return self.session.patch(
            f"{self.base_url}/{path.lstrip('/')}",
            timeout=self.timeout,
            **kwargs,
        )

    def close(self):
        self.session.close()
```

**AI prompt for code review:**

```text
Review this API client for correctness and maintainability.
Check URL joining, timeout behavior, token handling, session lifecycle,
error handling, and testability.

Do not rewrite the whole file. First list concrete issues with line references.
Do not log secrets. Do not assume the backend's error schema.
```

Review response yourself. If AI recommends raising exceptions for every non-2xx response, assess whether tests need to inspect error responses; don't accept blindly.

---

# 7. Phase 5 — Pytest fixtures and test data

`conftest.py`:

```python
import pytest
from config.settings import API_BASE_URL
from src.api.client import ApiClient

@pytest.fixture
def api_client():
    client = ApiClient(API_BASE_URL)
    yield client
    client.close()
```

Synthetic test data `data/claims.json`:

```json
{
  "valid_claim": {
    "amount": 1250.00,
    "loss_date": "2026-01-15",
    "description": "Synthetic training claim for damaged equipment"
  },
  "zero_amount_claim": {
    "amount": 0,
    "loss_date": "2026-01-15",
    "description": "Synthetic training claim"
  },
  "future_date_claim": {
    "amount": 500,
    "loss_date": "2099-01-01",
    "description": "Synthetic training claim"
  }
}
```

Do not treat a future date fixed to 2099 as universally valid forever; it is deliberately future for this exercise, but a robust suite should calculate relative to current date.

Example dynamic test data:

```python
from datetime import date, timedelta

future_date = (date.today() + timedelta(days=1)).isoformat()
```

## 7.1 API test pattern

Backend contract (training contract; actual app must implement/confirm it):
- `POST /claims`
- `GET /claims/{claim_id}`
- `GET /claims`
- `POST /claims/{claim_id}/request-information`
- `POST /claims/{claim_id}/decision`

`tests/api/test_claim_validation.py`:

```python
def test_claim_amount_must_be_positive(api_client):
    payload = {
        "policy_id": "POLICY-OWNED-BY-TEST-CUSTOMER",
        "amount": 0,
        "loss_date": "2026-01-15",
        "description": "Synthetic test claim",
    }

    response = api_client.post("/claims", json=payload)

    assert response.status_code == 400
```

**Important:** This test is executable only when the training backend implements the stated contract and test authentication setup. Never point it at a real insurer. In the project, you must create/use a local mock/training backend or a supplied QA environment. Do not claim the test passed until it actually runs.

## 7.2 AI prompt to generate negative tests

```text
Given the approved claim submission contract and this existing test file,
propose up to five additional negative tests.

For each:
- State the exact acceptance criterion.
- State test data.
- State expected HTTP status and response contract only if specified.
- If status/body is not specified, mark it as a clarification, not a fact.
- Do not edit files.
```

You decide which cases are valid before implementation.

---

# 8. Phase 6 — UI automation and Page Objects

## 8.1 Browser fixture

Use one fixture strategy consistently. If using Playwright's official pytest plugin, prefer its `page` fixture:

```python
# tests use the plugin-provided page fixture
# no custom fixture named page is required
```

Install plugin if needed:
```bash
pip install pytest-playwright
playwright install
```

`pytest.ini`:
```ini
[pytest]
testpaths = tests
python_files = test_*.py
addopts = -ra
markers =
    smoke: critical workflow
    api: API tests
    ui: UI tests
    security: authorization tests
```

## 8.2 Page Object example

`src/pages/claim_submission_page.py`:

```python
from playwright.sync_api import Page, expect

class ClaimSubmissionPage:
    def __init__(self, page: Page):
        self.page = page
        self.policy_id = page.get_by_label("Policy ID")
        self.amount = page.get_by_label("Claim amount")
        self.loss_date = page.get_by_label("Date of loss")
        self.description = page.get_by_label("Description")
        self.submit_button = page.get_by_role("button", name="Submit claim")

    def open(self, base_url: str):
        self.page.goto(f"{base_url}/claims/new")

    def submit_claim(self, policy_id, amount, loss_date, description):
        self.policy_id.fill(policy_id)
        self.amount.fill(str(amount))
        self.loss_date.fill(loss_date)
        self.description.fill(description)
        self.submit_button.click()

    def expect_form_visible(self):
        expect(self.policy_id).to_be_visible()
        expect(self.submit_button).to_be_visible()
```

Selectors and route are based on the training contract. Real implementation must inspect the actual DOM/accessibility tree and confirm names.

## 8.3 UI test

```python
import os
from config.settings import BASE_URL
from src.pages.claim_submission_page import ClaimSubmissionPage

def test_customer_can_open_claim_form(page):
    page.goto(BASE_URL)
    # Authentication setup must be performed using the approved test account flow.
    claim_page = ClaimSubmissionPage(page)
    claim_page.open(BASE_URL)
    claim_page.expect_form_visible()
```

This is only a form availability smoke test. Full submission test needs an authenticated customer, owned active policy, and a test backend that implements the contract.

## 8.4 AI prompt for locator proposal

```text
I will provide a DOM/accessibility snapshot of the claim form.
Suggest Playwright Python locators using this priority:
1. get_by_role
2. get_by_label
3. get_by_placeholder
4. stable test id
5. CSS only if needed

For every locator, quote the exact evidence from the snapshot.
Do not invent labels or selectors.
Flag ambiguous locators.
Do not write the full test.
```

After AI suggests locators:
1. Verify each locator in Inspector.
2. Check count.
3. Check accessible role/name.
4. Run the action.
5. Assert business outcome.

---

# 9. Phase 7 — Authorization and security-focused tests

Authorization is a high-value SDET area. Test both allowed and forbidden behavior.

Examples:
- Customer A cannot read Customer B's claim.
- Customer cannot use officer endpoint.
- Officer cannot approve claim.
- Supervisor cannot decide a claim outside authorized scope.
- Unauthenticated request cannot access protected endpoint.
- Uploaded document cannot be fetched by a different customer.

Do not test only UI visibility. Backend must enforce authorization even if someone calls API directly.

Test pattern (endpoint contract must be implemented):

```python
def test_customer_cannot_read_another_customers_claim(customer_a_client):
    response = customer_a_client.get("/claims/CLAIM-OWNED-BY-CUSTOMER-B")
    assert response.status_code in (403, 404)
```

**Important:** Whether unauthorized resource returns 403 or 404 is a product/security design decision. Confirm it. The example accepts either only as an interim training assertion; final test must match the agreed contract.

AI review prompt:

```text
Act as an application security-minded SDET.
Review these role/ownership test scenarios.
Look for IDOR/BOLA risks, privilege escalation, missing server-side checks,
and test-data isolation issues.

Do not provide exploit payloads beyond this authorized local training app.
Do not invent expected status codes; list questions where contract is unclear.
```

---

# 10. Phase 8 — AI-assisted debugging (manual evidence first)

## 10.1 Failure example

Suppose test fails:

```text
AssertionError: expected 201, got 400
```

Before asking AI:
1. Read complete traceback.
2. Print status, safe response body, request method/path.
3. Confirm test user role and policy ownership.
4. Confirm required fields and date format.
5. Confirm API contract.
6. Reproduce with same payload in a controlled API client.

Do not paste access tokens or customer data into AI.

## 10.2 Evidence-first debugging prompt

```text
You are assisting an SDET with debugging.
Do not modify code and do not guess.

Context:
[brief feature and expected behavior]

Failure:
[paste traceback and assertion]

Relevant code:
[paste smallest relevant code excerpt]

Observed evidence:
- HTTP method/path:
- Status:
- Sanitized response body:
- Test user role:
- Test data setup:
- Environment/build:

Tasks:
1. Separate facts from assumptions.
2. Give up to three ranked hypotheses.
3. For each hypothesis, state what evidence supports it.
4. Give one verification step that can prove/disprove it.
5. Do not suggest a code fix until root cause is verified.
6. Identify whether likely product, test, data, or environment failure.
```

## 10.3 After root cause is confirmed

```text
Root cause has been verified:
[explain evidence]

Propose the smallest safe fix.
Requirements:
- Do not refactor unrelated code.
- Explain each changed line.
- Identify regression tests.
- Identify possible side effects.
- Show a diff, not a full file replacement.
- Do not claim tests pass.
```

Then you run the tests yourself and inspect the diff.

## 10.4 AI output verification checklist

- [ ] Does the proposed API/locator/method actually exist in this project/version?
- [ ] Does it match current documentation?
- [ ] Does it preserve the requirement?
- [ ] Are negative cases covered?
- [ ] Does it leak secrets or personal data?
- [ ] Does it introduce sleeps, force clicks, broad exception swallowing, or brittle selectors?
- [ ] Did I run the exact relevant test?
- [ ] Did I run the regression subset?
- [ ] Can I explain the change without AI?

---

# 11. Phase 9 — AI-assisted test generation and code review

## 11.1 Generate test ideas, not blind test files

Prompt:

```text
Given this approved requirement and current test suite:
1. Identify uncovered acceptance criteria.
2. Suggest missing boundary and negative scenarios.
3. Explain why each scenario adds value.
4. Map each to API or UI layer.
5. Do not duplicate existing tests.
6. Do not edit code.
```

You compare AI suggestions with RTM and accept only justified additions.

## 11.2 Review a test

```text
Review this Pytest test as a senior SDET.

Check:
- Arrange/Act/Assert clarity
- Independence
- Test data isolation
- Assertion quality
- Locator reliability
- Timeout/synchronization strategy
- Cleanup
- Security/secret handling
- Whether the test checks a business outcome

Return:
A. Blocking issues
B. Improvements
C. Things that are already good

Do not rewrite unless I ask.
```

## 11.3 Validate AI-generated tests

For every generated test:
1. Read it line by line.
2. Confirm requirement mapping.
3. Verify test data and preconditions.
4. Run only that test.
5. Deliberately break the expected behavior if safe in local training environment.
6. Confirm the test fails for the right reason.
7. Restore behavior and confirm it passes.
8. Run related regression tests.
9. Check for duplicate/low-value coverage.

A test that always passes is not automatically a good test.

---

# 12. Phase 10 — Reporting and CI

## 12.1 Run locally

```bash
pytest -v
pytest -m smoke -v
pytest -m api -v
pytest -m ui -v
pytest --lf -v
```

HTML report:
```bash
pytest --html=reports/report.html --self-contained-html
```

## 12.2 GitHub Actions workflow

`.github/workflows/tests.yml`:

```yaml
name: ClaimFlow SDET Tests

on:
  push:
    branches: [main]
  pull_request:
  workflow_dispatch:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          playwright install --with-deps chromium

      - name: Run tests
        run: |
          pytest -v --junitxml=reports/junit.xml

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: claimflow-test-results
          path: reports/
```

This workflow assumes the ClaimFlow training application is available to the runner. If it is not hosted, add a separate service/container startup step; do not pretend that setting a base URL creates the application.

## 12.3 CI failure + AI prompt

```text
Analyze this sanitized CI failure.
Do not assume it is a product bug.

Classify likely cause:
- dependency/runtime
- browser installation/version
- environment/configuration
- network/service
- test data
- test synchronization
- product defect

Give a ranked diagnosis and exact evidence to inspect.
Do not propose retry loops or longer timeouts as the first fix.
```

---

# 13. Phase 11 — Final project artifacts

Repository must include:

```text
docs/
├── requirements/
│   ├── claimflow_analysis.md
│   └── clarification_log.md
├── test-design/
│   ├── test_scenarios.md
│   └── traceability_matrix.md
├── bug-reports/
│   └── sample_defect.md
└── test-summary/
    └── release_test_summary.md
```

## Sample defect

```text
Bug ID: CF-DEF-008
Title: Customer can retrieve another customer's claim by changing claim ID
Environment: Local training QA
Severity: Critical (proposed)
Priority: P0

Precondition:
Two synthetic customers exist, each with a separate claim.

Steps:
1. Authenticate as Customer A.
2. Capture Customer A's own claim request.
3. Request Customer B's claim ID using Customer A's session.
4. Inspect response and returned data.

Expected:
Access is denied according to the agreed authorization contract.
No data belonging to Customer B is disclosed.

Actual:
[Record actual observed behavior; do not pre-fill an unobserved result.]

Evidence:
Sanitized request/response, timestamp, build, test ID.

Impact:
Potential unauthorized disclosure of claim data.
```

Do not mark this bug as actually found unless your test reproduces it.

## Final QA summary

```text
Product: ClaimFlow
Build:
Environment:
Execution date:

Total tests:
Passed:
Failed:
Skipped:

P0 scenarios:
Authorization coverage:
Open critical/high defects:
Known environment issues:

AI assistance used for:
- Requirement analysis:
- Scenario review:
- Code review:
- Debugging hypotheses:

Human verification performed:
- [ ] Requirements reviewed
- [ ] Generated code reviewed
- [ ] Tests executed
- [ ] Failures investigated
- [ ] Regression suite run
- [ ] Secrets checked

Release recommendation:
GO / GO WITH RISKS / NO-GO

Evidence and rationale:
```

---

# 14. How to use AI without becoming dependent

## Use AI for:
- Breaking down long requirements
- Finding possible missing scenarios
- Explaining unfamiliar errors
- Reviewing code and test quality
- Suggesting debugging hypotheses
- Drafting documentation
- Explaining unfamiliar library APIs (then verify against official docs)

## Do not delegate blindly:
- Final expected behavior
- Security decisions
- Test pass/fail judgment
- Root-cause confirmation
- Secret/data handling
- Release recommendation
- Code merge approval

## Measure whether AI actually saves time

For each task record:
- Manual time estimate
- AI-assisted time
- Review/correction time
- Number of incorrect AI suggestions
- Defects/gaps found by human review
- Whether final test is stable

AI is useful only if it improves speed without reducing correctness, maintainability, or your understanding.

---

# 15. Project completion criteria

You can call Project 02 complete when:

- [ ] You can explain ClaimFlow roles and workflow.
- [ ] You can convert requirements into test scenarios.
- [ ] You can identify AI-invented assumptions.
- [ ] You can maintain a traceability matrix.
- [ ] You can explain the framework structure.
- [ ] You can write and debug API tests.
- [ ] You can write and debug UI tests.
- [ ] You can cover role/ownership authorization.
- [ ] You can review AI-generated code and reject bad suggestions.
- [ ] You can use evidence-first AI debugging.
- [ ] You can run tests in CI and inspect artifacts.
- [ ] You can explain which parts AI helped with and what you personally verified.

---

# 16. Interview explanation

**Simple English:**

"I worked on an insurance claims automation project using Python, Pytest, Playwright, and Requests. I analyzed requirements, designed API and UI scenarios, automated customer and role-based workflows, and integrated test execution into CI. I also used AI tools for requirement analysis, test idea review, and debugging hypotheses, but I validated all generated code and test results myself."

**Stronger explanation:**

"I approached the project as an SDET rather than only writing UI scripts. I started with requirement decomposition, role-permission analysis, risk-based test design, and traceability. I built API and browser automation layers using Python, Pytest, Requests, and Playwright. I focused on authorization boundaries, negative cases, test isolation, diagnostic evidence, and CI execution. AI was used as a productivity assistant for analysis and code review, while requirements, root-cause decisions, test validation, and release recommendations remained human-owned."

**Honesty:** Describe it as a self-directed training project unless it was delivered for an actual employer/client. Do not claim production impact, team size, or business metrics you did not measure.

---

# 17. Suggested execution sequence

| Stage | Your work | AI role | Completion evidence |
|---|---|---|---|
| 1 | Read and annotate requirements | Clarification/gap analysis | Approved requirement notes |
| 2 | Create scenarios and RTM | Scenario critique | Reviewed traceability |
| 3 | Create repo and rules | Architecture review | Clean repo |
| 4 | Build API client and fixtures | Small code review | Passing unit/API tests |
| 5 | Build UI page objects | Locator proposal from DOM evidence | Passing UI smoke |
| 6 | Add role/ownership cases | Security scenario review | Authorization tests |
| 7 | Debug deliberate failures | Ranked hypotheses | Root cause evidence |
| 8 | Add reports and CI | Workflow review | CI artifacts |
| 9 | Final QA summary | Documentation review | Defensible release report |

**Do not move to the next stage just because AI produced code. Move only when you understand it, run it, inspect the result, and can explain it.**

---

# 18. Final difference between Project 01 and Project 02

| Area | Project 01 | Project 02 |
|---|---|---|
| Domain | E-commerce | Insurance claims |
| AI usage | None | Controlled and evidence-based |
| Main skill | Independent engineering | AI-assisted engineering judgement |
| Requirement analysis | You do it manually | AI suggests; you validate |
| Test design | You create from scratch | AI critiques and finds gaps |
| Coding | You write and debug | AI assists in small reviewed tasks |
| Debugging | Manual investigation | Manual evidence + AI hypotheses |
| Quality ownership | You | You |
| Main learning | How to do the work | How to use AI without losing control |

**Final rule:** Project 01 proves you can work independently. Project 02 demonstrates that you can use AI responsibly while retaining SDET-level engineering judgement.
