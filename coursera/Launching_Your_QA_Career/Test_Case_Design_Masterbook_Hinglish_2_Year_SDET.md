# TEST CASE DESIGN MASTERBOOK
## Beginner se 2-Year Experience SDET Interview Level tak — Hinglish Practical Workbook

**Purpose:** Requirements ko samajhna, test conditions derive karna, right test-design technique choose karna, clear test cases likhna, coverage/risk explain karna aur interview mein confidently answer dena.

**Target:** Manual QA + Automation QA/SDET (0–2 years)  
**Scope:** Sirf test case design. Framework coding is workbook ka focus nahi.  
**Learning style:** Hinglish explanations + professional English test artifacts.

> **How to use:** Har topic padhne ke baad file band karke concept apne words mein explain karo. Examples par pehle khud test cases likho, phir model answer se compare karo. Neeche ke Markdown checkboxes ko tick karke progress track kar sakte ho.

---

## Progress tracker

- [ ] 1. Test design foundations
- [ ] 2. Requirement reading
- [ ] 3. Professional test case writing
- [ ] 4. Easy level — 5 worked examples
- [ ] 5. Equivalence Partitioning (EP)
- [ ] 6. Boundary Value Analysis (BVA)
- [ ] 7. Decision Table Testing
- [ ] 8. State Transition Testing
- [ ] 9. Use Case / End-to-End Testing
- [ ] 10. Pairwise / Combinatorial Testing
- [ ] 11. Error Guessing / Exploratory Testing
- [ ] 12. Medium level — 5 worked examples
- [ ] 13. Hard / SDET level — 5 worked examples
- [ ] 14. Risk-based prioritization and RTM
- [ ] 15. Interview questions and answers
- [ ] 16. Mock interview and final revision

# 1. Test case design kya hai?

**Definition:** Test case design is the process of deriving test conditions, test data, steps, and expected results from requirements and risks to verify whether a product behaves as expected.

Simple Hinglish: Requirement padhkar decide karna:
- Kya verify karna hai?
- Kis condition mein?
- Kaunsa data use hoga?
- Kya steps perform karne hain?
- Correct observable result kya hoga?
- Kaunse cases sabse important hain?

## 1.1 Scenario vs condition vs case vs data

| Term | Meaning | Login example |
|---|---|---|
| Requirement | Product ka expected behavior | Registered user login kar sake |
| Test condition | Kya verify karna hai | Valid credentials par login |
| Test scenario | High-level situation | Successful login verify karna |
| Test case | Detailed executable check | Email/password enter, Sign in click, dashboard verify |
| Test data | Input values | Approved test email/password |
| Expected result | Observable outcome | Authenticated landing page appears |

**Interview line:** Scenario tells *what to test* at a high level; test case tells *how to test it* with preconditions, data, steps and expected results.

## 1.2 QA thought process

```text
Requirement
   ↓
Understand actor, goal, rules, constraints
   ↓
Identify test conditions
   ↓
Think positive, negative, boundary, role, state
   ↓
Choose suitable test-design technique
   ↓
Prepare controlled test data
   ↓
Write steps + observable expected result
   ↓
Prioritize by risk
   ↓
Review coverage and remove duplicates
```

# 2. Requirement kaise read karte hain?

Requirement ko five passes mein read karo.

1. **Business goal:** User/company kya achieve karna chahti hai?
2. **Actor and permission:** Kaun action kar sakta hai? Kaun nahi?
3. **Rules and constraints:** Required fields, allowed values, limits, date/status rules?
4. **Outcomes:** Success, validation error, access denied, state change?
5. **Gaps and risks:** Kya unclear hai? Failure ka impact kya hoga?

## 2.1 Requirement keywords

| Keyword | Test-design reaction |
|---|---|
| must / shall | Mandatory behavior verify karo |
| only | Permission/eligibility boundary |
| minimum / at least | Lower boundary |
| maximum / up to | Upper boundary |
| unique | Duplicate-value test |
| before / after | Date/time boundary or sequence |
| within X minutes | Timing boundary |
| active / inactive | State and eligibility |
| cannot / must not | Negative/security test |
| optional | Provided and omitted inputs |
| once / only once | Duplicate submission/idempotency question |

## 2.2 Worked requirement breakdown

**Requirement:** "Registered customers can sign in using a valid email address and password. Invalid credentials must not create an authenticated session."

| Question | Answer |
|---|---|
| Actor? | Registered customer |
| Preconditions? | Account exists and is active |
| Main action? | Enter email/password and sign in |
| Positive outcome? | Authenticated session and landing page |
| Negative outcome? | No authenticated session |
| Input dimensions? | Email valid/unknown/empty; password correct/wrong/empty |
| Security angle? | Protected page must not be accessible without authentication |

Derived conditions:
1. Valid email + valid password.
2. Valid email + wrong password.
3. Unknown email + password.
4. Empty email.
5. Empty password.
6. Both fields empty.
7. Inactive/locked account, only if states are defined.
8. Direct protected URL without login.

**Important:** Error wording, lockout threshold, password complexity etc. requirement mein nahi hain to invent mat karo. Clarification raise karo.

## 2.3 Ambiguity log

| ID | Unclear point | Question to PO/BA | Why |
|---|---|---|---|
| Q-01 | Email case sensitivity | Is email matching case-insensitive? | Input behavior |
| Q-02 | Failed login limit | Is account locked after repeated failures? | Security |
| Q-03 | Error message | What exact message is expected? | Assertion |
| Q-04 | Session expiry | What is idle timeout? | Session tests |

**Interview answer:** "I clarify ambiguous acceptance criteria with the product owner or BA, document agreed assumptions, and avoid inventing expected behavior."

# 3. Professional test case kaise likhein?

## 3.1 Recommended template

| Field | What to write |
|---|---|
| Test Case ID | Unique ID, e.g. AUTH-001 |
| Title | One clear behavior |
| Requirement ID | Requirement/AC reference |
| Preconditions | State needed before execution |
| Priority | P0/P1/P2 or team scale |
| Test data | Controlled inputs or secure data reference |
| Steps | Numbered, reproducible actions |
| Expected result | Observable outcome |
| Technique/type | Positive, negative, BVA, decision table etc. |
| Automation candidate | Yes/No/Later with reason |

## 3.2 Complete example

**TC ID:** AUTH-001  
**Title:** Verify active customer can sign in with valid credentials  
**Requirement:** AUTH-REQ-01  
**Priority:** P0  
**Type:** Positive / Happy path

**Preconditions:**
- An active customer account exists in QA.
- Approved test credentials are available securely.
- User is logged out.

**Test data:** Registered email and correct password from secure test data.

**Steps:**
1. Navigate to the login page.
2. Enter the registered email.
3. Enter the correct password.
4. Select **Sign in**.
5. Observe the landing page and account navigation.

**Expected result:**
- Authentication succeeds.
- User is redirected to the agreed authenticated landing page.
- Account-specific navigation is visible.
- An authenticated session is established.
- No login validation error is displayed.

## 3.3 Weak vs strong

**Weak:** "Check login works."

Problems: no input, precondition, steps, expected result or reproducibility.

**Strong:** "Verify an active registered customer is redirected to the account dashboard after submitting valid credentials."

Writing rules:
- One primary objective per case.
- Avoid vague words: properly, correctly, works fine.
- Use exact data or controlled data reference.
- Expected result must be observable.
- Avoid dependency on another test.
- Mention cleanup if test creates data.
- Don't combine unrelated behaviors into one giant test.

# 4. EASY LEVEL — 5 common interview examples

## Example 1 — Login page

**Prompt:** "How would you test a login page?"

Assumption: Active registered user signs in with email/password. Invalid credentials must not authenticate.

| ID | Test case | Test data | Expected result |
|---|---|---|---|
| LOG-01 | Valid email + valid password | Active user + correct password | Login succeeds; authenticated page appears |
| LOG-02 | Valid email + wrong password | Active user + incorrect password | Login denied; no session |
| LOG-03 | Unknown email + password | Unregistered email | Login denied; no session |
| LOG-04 | Email blank | Blank email + password | Required validation |
| LOG-05 | Password blank | Email + blank password | Required validation |

Extra: both blank, spaces, email case, password masking, Enter key, logout, protected URL, session expiry — as requirements define.

**Interview explanation:** "I start with the happy path, then invalid credentials and mandatory fields. I also consider session and authorization because login is security-sensitive. I clarify error-message and lockout rules instead of assuming them."

## Example 2 — Search box

Assumption: Search returns products matching the keyword.

| ID | Input/action | Expected result |
|---|---|---|
| SRCH-01 | Existing exact product name | Matching product shown |
| SRCH-02 | Partial product name | Partial matches shown if supported |
| SRCH-03 | Non-existing term | Clear no-results state |
| SRCH-04 | Empty search | Defined behavior followed |
| SRCH-05 | Leading/trailing spaces | Behavior follows trimming rule |

Clarify: case sensitivity, special characters, minimum length, searchable fields, relevance, pagination.

**Interview explanation:** "I cover exact, partial, no-result, empty and whitespace inputs. I clarify matching rules and verify that results actually match the query."

## Example 3 — Contact form

Assumption: Name, email, subject, message required; email format validated.

| ID | Input | Expected result |
|---|---|---|
| FORM-01 | All valid fields | Submission succeeds; confirmation shown |
| FORM-02 | Name empty | Required validation |
| FORM-03 | Malformed email | Email validation; no submission |
| FORM-04 | Message empty | Required validation |
| FORM-05 | All fields empty | Required validation for mandatory fields |

Extra: max length, spaces-only values, safe handling of special input, duplicate submission, network failure.

## Example 4 — Password field

Assumption: mandatory, masked by default, length policy defined by requirement.

| ID | Input/action | Expected result |
|---|---|---|
| PWD-01 | Valid password in allowed range | Accepted |
| PWD-02 | Below minimum length | Rejected |
| PWD-03 | Above maximum length | Rejected/constrained as specified |
| PWD-04 | Empty password | Required validation |
| PWD-05 | Show/hide toggle | Visibility changes; value remains same |

Clarify allowed characters, Unicode, whitespace, max length and complexity. Never assume policy.

## Example 5 — File upload

Assumption: PDF/JPG/PNG allowed; max 5 MB.

| ID | File | Expected result |
|---|---|---|
| FILE-01 | Valid PDF under 5 MB | Accepted |
| FILE-02 | Valid JPG under 5 MB | Accepted |
| FILE-03 | Unsupported EXE | Rejected |
| FILE-04 | File above 5 MB | Rejected with size validation |
| FILE-05 | No file selected, then submit | Required validation if upload mandatory |

Extra: zero-byte, corrupted file, misleading extension, duplicate filename, interrupted upload, multiple files. Server-side content validation and access control matter.

# 5. Equivalence Partitioning (EP)

<badge color="success">Must know</badge>

**Definition:** Divide input values into groups expected to behave similarly. Select representative values from valid and invalid groups instead of testing every value.

Example: age allowed 18–60 inclusive.

| Partition | Values | Valid? | Representative |
|---|---|---:|---:|
| Below 18 | 0–17 | No | 17 |
| 18–60 | 18–60 | Yes | 35 |
| Above 60 | 61+ | No | 61 |
| Non-numeric | abc | No | abc |
| Empty | blank | Depends on mandatory rule | blank |

## Five EP examples

1. **Age 18–60:** valid 18–60; invalid below, above, non-numeric, empty. Representatives: 35, 17, 61, abc, blank.
2. **Username length 5–12:** valid length 5–12; invalid 0–4 and 13+; unsupported characters as a separate partition if rule exists.
3. **File types PDF/JPG/PNG:** one representative per allowed type; one unsupported type. Size is a separate boundary dimension.
4. **Quantity 1–10:** valid 1–10; invalid below 1, above 10, decimal, non-numeric, empty.
5. **Discount code:** active valid, unknown, expired, inactive, wrong customer segment. Use one representative per distinct business partition.

**When:** large input space with groups expected to behave alike. EP alone is insufficient when exact boundaries, combinations or state transitions matter.

**Interview answer:** "Equivalence Partitioning is a black-box technique. I divide input data into valid and invalid groups expected to behave similarly, then select representative values. For age 18–60, I might test 35, 17 and 61, plus non-numeric and empty inputs if relevant."

**Keywords:** valid class, invalid class, partition, representative value, redundancy reduction.

# 6. Boundary Value Analysis (BVA)

<badge color="success">Must know</badge>

BVA tests values at and around range edges because off-by-one defects often occur there.

For inclusive range 18–60 test: **17, 18, 19, 59, 60, 61**.

| EP | BVA |
|---|---|
| Groups similar values | Focuses on range edges |
| Representative from each class | Minimum/maximum and neighbors |
| Example: 35, 17, 61 | Example: 17,18,19,59,60,61 |

## Five BVA examples

1. **Age 18–60:** 17 reject, 18 accept, 19 accept, 59 accept, 60 accept, 61 reject.
2. **Password length 8–20:** test lengths 7,8,9,19,20,21 using exact-length strings.
3. **Upload max 5 MB:** one byte below, exactly at, one byte above. Clarify MB decimal vs MiB binary.
4. **Quantity 1–10:** 0,1,2,9,10,11; test decimals separately.
5. **Booking today through 90 days:** yesterday, today, tomorrow, day 89, day 90, day 91. Clarify timezone and inclusivity.

**Interview answer:** "Boundary Value Analysis focuses on minimum, maximum and values just outside/inside the limits. For 1–10, I test 0,1,2,9,10,11. It helps catch off-by-one defects."

**Keywords:** min, max, just below, just above, inclusive/exclusive, off-by-one.

# 7. Decision Table Testing

<badge color="success">Must know</badge>

Use when expected behavior depends on combinations of conditions.

Example: login depends on registered user, correct password, active account.

| Rule | Registered? | Password correct? | Active? | Expected |
|---|---|---|---|---|
| R1 | Yes | Yes | Yes | Login allowed |
| R2 | Yes | No | Yes | Denied |
| R3 | No | Any | Any | Denied |
| R4 | Yes | Yes | No | Denied |

"Any" means that condition doesn't change that rule's outcome.

## Five decision-table examples

1. **Login:** registered? password correct? active? Map each meaningful combination to allow/deny.
2. **Free shipping:** premium OR cart >= $100 gives free shipping.

| Premium? | Cart >= $100? | Free shipping? |
|---|---|---|
| No | No | No |
| No | Yes | Yes |
| Yes | No | Yes |
| Yes | Yes | Yes |

3. **Loan eligibility:** age eligible AND income eligible AND credit check passed. Test all-yes plus each individual failed condition.
4. **Discount:** active code AND minimum cart met AND segment eligible. Test all-yes and each condition false.
5. **Insurance claim:** authenticated AND owns policy AND policy eligible AND amount valid. Test all-valid plus each condition independently invalid. Four binary conditions have 16 theoretical combinations; use constraints/don't-care rules carefully.

**Interview answer:** "Decision Table Testing is useful when behavior depends on multiple condition combinations. I list conditions, identify meaningful rules and map each to expected action. It prevents missing business-rule combinations."

**Keywords:** conditions, combinations, rules, actions, business logic.

# 8. State Transition Testing

<badge color="success">Must know for workflows</badge>

Use when behavior depends on current state and an event.

Example order: `CREATED → PAID → SHIPPED → DELIVERED`.

| Current state | Event | Next state | Allowed? |
|---|---|---|---|
| Created | Payment succeeds | Paid | Yes |
| Created | Payment fails | Payment failed | Yes |
| Paid | Shipment created | Shipped | Yes |
| Shipped | Delivery confirmed | Delivered | Yes |
| Delivered | Ship again | Shipped | No, unless rule permits |

## Five state-transition examples

1. **Login lockout:** Active → Temporarily Locked → Unlocked. Test failed-attempt threshold, valid login and unlock event; threshold/duration must be specified.
2. **Order lifecycle:** Created → Paid → Packed → Shipped → Delivered; test allowed transitions and prohibited jumps.
3. **Password reset token:** Generated → Used or Expired; test valid once, reuse, expired and unknown token.
4. **Insurance claim:** Submitted → Under Review → Needs Information → Under Review → Approved/Rejected; verify role and terminal-state rules.
5. **Subscription:** Trial → Active → Past Due → Suspended → Cancelled; test payment success/failure and permitted transitions.

**Interview answer:** "I identify states, events, allowed and invalid transitions. For an order, I verify Created to Paid to Shipped to Delivered and ensure prohibited transitions are rejected."

**Keywords:** state, event, transition, valid/invalid transition, state model.

# 9. Use Case / End-to-End Testing

Use case testing validates a realistic user goal through a sequence of interactions, including alternate and exception flows.

## Five common examples

1. **E-commerce purchase:** login → search → product detail → add to cart → update quantity → checkout → address → payment → confirmation → order history. Alternatives: out of stock, invalid address, payment decline, session expiry.
2. **ATM withdrawal:** insert card → PIN → withdrawal → amount → balance/limit check → dispense cash → update balance. Alternatives: wrong PIN, insufficient funds, limit exceeded, ATM out of cash, network failure.
3. **Flight booking:** search route/date → select flight → passenger details → seat/add-ons → payment → booking reference. Alternatives: no seats, fare changes, payment failure, duplicate submission.
4. **Food delivery:** address → restaurant → items → coupon → order → tracking → delivery. Alternatives: restaurant closed, item unavailable, coupon invalid, unsupported address.
5. **Insurance claim:** login → select own policy → incident details → documents → submit → claim reference → track status → respond to information request.

**Interview answer:** "I model the main success flow and alternate/exception flows for a real user goal, then verify the important business outcomes across the involved components."

**Keywords:** actor, goal, main flow, alternate flow, exception flow, end-to-end.

# 10. Pairwise / Combinatorial Testing

When many parameters exist, exhaustive combinations can become huge. Pairwise selects a smaller set so every pair of parameter values appears at least once. It does **not** guarantee every 3-way or higher-order interaction.

Example parameters:
- Browser: Chrome, Firefox
- Role: Customer, Admin
- Language: English, Hindi

Full combinations = 2×2×2 = 8. For this small set, running all 8 may be simplest. For larger sets, use a pairwise generator and review coverage.

## Five use cases
1. Browser × OS × screen size.
2. Role × permission × operation.
3. Payment method × currency × country.
4. Device × browser × locale.
5. Account type × subscription plan × feature flag.

**Interview answer:** "Pairwise testing selects cases so every pair of parameter values occurs at least once. It reduces combinations, while I retain explicit high-risk combinations."

# 11. Error Guessing and Exploratory Testing

**Error guessing:** Use experience and common defect patterns to predict likely failures. Examples: empty input, spaces-only, double-click, refresh during transaction, expired session, very long text, network interruption, duplicate request.

**Exploratory testing:** Learning, test design and execution happen together, guided by a charter.

Example charter: "Explore cart quantity and price recalculation for valid, invalid and repeated quantity changes. Focus on subtotal accuracy and persistence after refresh. Timebox: 30 minutes."

Record what you explored, data, observations, defects, questions and follow-up cases.

## Five error-guessing ideas
1. Submit button clicked twice rapidly.
2. Form submitted after session expires.
3. Text field receives spaces only.
4. Browser refreshed during payment/claim submission.
5. Same coupon or claim submitted twice.

**Interview answer:** "I use experience to identify likely failure patterns after understanding requirements and applying systematic techniques. I document findings so they are reproducible."

# 12. MEDIUM LEVEL — 5 worked examples

At this level, combine techniques. Interviewer expects structured thinking, not just happy-path cases.

## Medium 1 — Shopping cart

Assumption: available products can be added; quantity 1–10; users can update/remove; totals recalculate.

| ID | Scenario | Technique | Expected result |
|---|---|---|---|
| CART-01 | Add available product | Use case | Product appears with correct price |
| CART-02 | Set quantity to 1 and 10 | BVA | Both accepted |
| CART-03 | Set quantity 0 or 11 | BVA | Validation; quantity unchanged |
| CART-04 | Add unavailable product | Decision rule | Add prevented |
| CART-05 | Remove item | State/action | Item removed; totals recalculate |

**Interview explanation:** "I focus on cart correctness and price integrity. I combine BVA for quantity with availability rules and add/update/remove flows. I verify subtotal and grand total against defined tax/discount rules."

## Medium 2 — ATM withdrawal

Assumption: PIN validated; withdrawal positive, within balance and daily limit.

| ID | Scenario | Technique | Expected result |
|---|---|---|---|
| ATM-01 | Correct PIN + valid amount | Positive | Cash dispensed; balance reduced |
| ATM-02 | Incorrect PIN | Negative/state | Denied; balance unchanged |
| ATM-03 | Amount equals balance | Boundary/rule | Result follows documented zero-balance policy |
| ATM-04 | Amount exceeds balance | Negative | Denied; balance unchanged |
| ATM-05 | Amount exceeds remaining daily limit | Decision/BVA | Denied; balance unchanged |

Clarify denomination multiples, daily reset timezone, retry/lockout rules.

## Medium 3 — Hotel booking

Assumption: checkout after check-in; room available; guests within capacity.

| ID | Scenario | Technique | Expected result |
|---|---|---|---|
| HOTEL-01 | Valid dates and room | Positive/use case | Booking confirmed |
| HOTEL-02 | Checkout equals check-in | BVA | Rejected |
| HOTEL-03 | Checkout before check-in | BVA/negative | Rejected |
| HOTEL-04 | Room unavailable | Decision table | Booking not created |
| HOTEL-05 | Guest count exceeds capacity | EP/BVA | Rejected |

Explain timezone, inventory race conditions, cancellation and duplicate booking as additional risks.

## Medium 4 — Coupon / discount

Assumption: code active, unexpired, minimum cart met, customer eligible.

| ID | Scenario | Technique | Expected result |
|---|---|---|---|
| COUP-01 | Active eligible code + minimum met | Decision table | Discount applied |
| COUP-02 | Expired code | Negative/state | Rejected |
| COUP-03 | Cart just below minimum | BVA | Rejected |
| COUP-04 | Cart exactly at minimum | BVA | Accepted |
| COUP-05 | Customer ineligible | Decision table | Rejected |

Explain: "I use a decision table for multiple eligibility conditions and BVA for minimum cart value. I verify final payable amount, not only the success message."

## Medium 5 — Create-user REST API

Assumption: `POST /users` creates user with required name/email; email unique.

| ID | Scenario | Technique | Expected result |
|---|---|---|---|
| API-01 | Valid payload | Positive | Documented success; user ID returned |
| API-02 | Missing email | Negative | Documented validation response |
| API-03 | Malformed email | EP | Rejected |
| API-04 | Duplicate email | Business/state | Duplicate prevented |
| API-05 | Empty body/invalid JSON | Negative | Documented client error; no user created |

API tests should verify status, response schema/data, side effects and authorization. Exact status/error contract comes from API specification.

# 13. HARD / SDET LEVEL — 5 worked examples

At around 2 years' experience, interviewers may assess risk thinking, roles, data isolation, concurrency, APIs and integrations.

## Hard 1 — Insurance claim workflow with roles

Requirement: customer submits only against own active policy; officer reviews assigned claims and can request information; supervisor approves/rejects eligible claims; every status change audited.

| ID | Scenario | Technique | Expected result |
|---|---|---|---|
| CLM-01 | Customer submits valid claim on own active policy | Use case | Claim created in SUBMITTED |
| CLM-02 | Customer uses another customer's policy | Decision/security | Denied; no claim created |
| CLM-03 | Officer attempts supervisor-only approval | Permission | Denied; status unchanged |
| CLM-04 | Officer requests information | State transition | NEEDS_INFORMATION; audit event recorded |
| CLM-05 | Supervisor approves eligible UNDER_REVIEW claim | State transition | APPROVED; actor/time recorded |

Further risks: duplicate submission, concurrent decisions, stale state, document access, audit completeness, notifications.

**Interview answer:** "I start with a role-permission matrix and claim state model. I test allowed and forbidden actions at API level, not only by hiding UI controls. I verify transitions and audit records because authorization and traceability are high-impact risks."

## Hard 2 — Payment checkout

Assumption: gateway can approve, decline, timeout or return unknown result; duplicate charge must be prevented.

| ID | Scenario | Technique | Expected result |
|---|---|---|---|
| PAY-01 | Gateway approves | Use case/state | One successful payment and confirmed order |
| PAY-02 | Gateway declines | Decision | Order not marked paid |
| PAY-03 | Gateway times out after request | Error/state | Status reconciled; no blind second charge |
| PAY-04 | User double-clicks Pay | Error guessing/idempotency | No duplicate charge/order |
| PAY-05 | Callback arrives twice | State/idempotency | One final payment effect |

Interview point: timeout does not always mean payment failed. Verify amount, currency, order linkage, idempotency and reconciliation.

## Hard 3 — Secure file upload

Requirement: PDF/JPG/PNG, max 5 MB, private access.

| ID | Scenario | Technique | Expected result |
|---|---|---|---|
| UP-01 | Valid PDF exactly at limit | BVA | Accepted |
| UP-02 | One byte above limit | BVA | Rejected |
| UP-03 | Unsupported content renamed as .pdf | Security/error guessing | Server validates content; rejects |
| UP-04 | Another user accesses document URL | Authorization | Denied |
| UP-05 | Empty/corrupted file | EP/negative | Rejected safely |

Further risks: MIME spoofing, unsafe filename, malware scan, expired download URL, interrupted upload. Only test security cases in authorized environment.

## Hard 4 — Last-seat booking / concurrency

Requirement: a slot can be confirmed for only one customer.

| ID | Scenario | Technique | Expected result |
|---|---|---|---|
| BOOK-01 | One customer books available slot | Positive | Booking confirmed |
| BOOK-02 | Another user books reserved slot | State/business | Rejected or waitlisted per rule |
| BOOK-03 | Two customers book same last slot simultaneously | Concurrency/risk | At most one confirmed |
| BOOK-04 | Payment fails after temporary reservation | State | Inventory released per expiry rule |
| BOOK-05 | Retry after network timeout | Idempotency | No duplicate booking |

A sequential UI test cannot prove race safety. Coordinate parallel API requests in a controlled environment and verify final inventory/records.

## Hard 5 — Role-based API and data isolation

Requirement: customer reads own records; staff reads assigned records; admin has approved broader access.

| ID | Scenario | Technique | Expected result |
|---|---|---|---|
| RBAC-01 | Customer reads own record | Positive auth | Allowed |
| RBAC-02 | Customer changes record ID to another user's ID | Security | Denied; no data leak |
| RBAC-03 | Staff reads unassigned record | Permission boundary | Denied |
| RBAC-04 | Expired token accesses protected endpoint | Auth/state | Authentication failure |
| RBAC-05 | User attempts admin-only action | Privilege boundary | Denied; no side effect |

**Interview answer:** "I create a role-action-resource matrix, then cover allowed and denied combinations. I test server-side authorization directly through APIs because UI restrictions alone are not security controls. I verify response and absence of unauthorized side effects."

# 14. Risk-based prioritization

Limited time mein all cases equal nahi hote. Consider:
- **Impact:** Customer/business/security effect.
- **Likelihood:** Failure probability.
- **Exposure:** How many users/how often feature is used.
- **Detectability:** Failure easy to detect or hidden?

A simple team scoring aid: `Risk Score = Impact × Likelihood` using a defined 1–5 scale. Not a universal standard.

| Feature | Impact | Likelihood | Score | Suggested priority |
|---|---:|---:|---:|---|
| Duplicate payment charge | 5 | 3 | 15 | P0 |
| Login failure | 5 | 3 | 15 | P0 |
| Product image alignment | 1 | 2 | 2 | P2 |
| Cart total incorrect | 5 | 3 | 15 | P0 |
| Footer typo | 1 | 1 | 1 | P2 |

**Severity vs priority:**
- Severity = defect impact.
- Priority = how urgently it should be fixed.
- Related, but not identical; business context matters.

# 15. RTM and coverage

Requirement Traceability Matrix maps requirements to test cases.

| Requirement | Requirement statement | Test cases | Coverage |
|---|---|---|---|
| AUTH-01 | Valid login | AUTH-001 | Covered |
| AUTH-02 | Invalid password denied | AUTH-002 | Covered |
| AUTH-03 | Logout ends session | AUTH-008 | Covered |
| AUTH-04 | Protected page requires auth | AUTH-009 | Covered |

Before saying testing is complete:
- Every acceptance criterion mapped?
- Positive and negative paths?
- Boundaries?
- Roles and permissions?
- State transitions?
- Important integrations?
- Test data combinations justified?
- Gaps/risks documented?

**100% requirement mapping does not mean defect-free.** RTM proves traceability, not absence of defects.

# 16. Interview questions and model answers

## Q1. What is test case design?
"Test case design is the process of deriving test conditions, data, steps and expected results from requirements and risks so that product behavior can be verified systematically."

## Q2. How do you design test cases from a requirement?
"I understand the business goal, actor, preconditions, rules and expected outcome. Then I identify positive, negative, boundary and permission-related conditions. I select suitable techniques such as EP, BVA, decision tables or state transitions. Finally, I write clear steps and observable expected results, map them to requirements and prioritize by risk."

## Q3. Scenario vs test case?
"A scenario is a high-level situation to validate; a test case contains detailed preconditions, data, steps and expected results."

## Q4. EP vs BVA?
"EP groups inputs expected to behave similarly and selects representatives. BVA focuses on range limits and neighboring values. For 1–10, EP may choose 5, 0 and 11; BVA checks 0,1,2,9,10,11."

## Q5. When use decision tables?
"When expected behavior depends on combinations of conditions, such as coupon eligibility based on active status, cart minimum and customer segment."

## Q6. When use state transition?
"When behavior depends on current state and an event, such as order lifecycle, claim status, password reset token or account lockout."

## Q7. How test login?
"Clarify requirements and account states; test valid credentials, invalid/unknown credentials, empty/malformed inputs, password masking, session/logout/protected pages, and lockout/rate limits if specified."

## Q8. How test ATM?
"Cover card/PIN validation, amount EP/BVA, balance and daily limit rules, cash availability, balance update, receipt, cancel, timeout and network failure. Retry limits must come from requirements."

## Q9. Which tests automate?
"I prioritize stable, repeatable, high-value regression scenarios, critical business flows and data-driven validations. I avoid automating one-time exploratory checks or unstable flows before understanding them. I consider maintenance cost and the right test layer."

## Q10. Can we test everything?
"No. Exhaustive testing is usually impractical because input combinations and states can be enormous. I use risk-based testing and design techniques to select representative, boundary, high-risk and critical-path cases."

## Q11. Positive vs negative testing?
"Positive testing verifies valid inputs and expected user behavior. Negative testing verifies invalid inputs, unauthorized actions and error conditions are handled safely."

## Q12. Severity vs priority?
"Severity describes defect impact; priority describes how urgently it should be fixed."

## Q13. What is RTM?
"An RTM maps requirements to test cases and execution status. It helps find coverage gaps and supports impact analysis."

## Q14. Why is test data important?
"Test data is the input and system state used to execute a test. It should be controlled, repeatable, isolated and must not expose real customer information."

## Q15. What makes a good test case?
"Clear, traceable, reproducible, independent, risk-relevant, and has observable expected results. It verifies one main objective without unnecessary steps."

## Q16. What if requirement is unclear?
"I document the ambiguity, ask the BA/product owner, record agreed assumptions and avoid expected results based on guesses."

## Q17. What is pairwise testing?
"It selects tests so every pair of parameter values appears at least once. It reduces combinations but doesn't guarantee every higher-order interaction."

## Q18. What is exploratory testing?
"Learning, test design and execution happen together, guided by a charter and observations. I document findings and convert valuable ones into reproducible cases."

## Q19. How ensure coverage?
"I map acceptance criteria to cases using RTM, review positive/negative/boundary/state/role coverage, and document untested risks or environment limitations."

## Q20. Test passes but feature is wrong — what do you do?
"I review whether the expected result reflects the requirement, data is meaningful and assertion checks the business outcome rather than a superficial UI signal. Then I correct/add coverage."

# 17. Scenario interview answer framework — R-A-C-E

Use this structure for open-ended questions:

- **R — Requirement:** Restate what the system must do.
- **A — Areas:** Identify positive, negative, boundary, role, state, integration.
- **C — Cases:** Give representative cases and explain technique.
- **E — Expected result:** State observable outcomes and risks.

Example: "Test a registration page."

- **R:** User registers with name, email, password; email must be unique.
- **A:** Required fields, format, password policy, duplicate email, boundaries, verification.
- **C:** Valid registration, blanks, malformed email, duplicate email, password boundary, verification link.
- **E:** Account created once, correct state, duplicate prevented, validation clear, no unauthorized session before required verification.

**Don't answer:** "I will test valid, invalid, blank, refresh, everything."

**Better:** "I'll clarify field rules, use EP for valid/invalid formats, BVA for length limits, and negative tests for duplicate values. I'll verify the validation and that no unintended record is created."

When interviewer says "Give test cases now", speak in groups: happy path, negative validation, boundary, business rules, state/role/security, integration. Give 5–8 high-value cases first, then offer deeper edge cases.

# 18. Practice bank — 15 prompts

For each prompt, write requirement questions, at least five conditions, five detailed test cases, technique, priority and reason.

**Easy**
1. Login page
2. Search box
3. Contact form
4. Password field
5. File upload

**Medium**
6. Shopping cart
7. ATM withdrawal
8. Hotel booking
9. Coupon/discount
10. Create-user REST API

**Hard**
11. Insurance claim with three roles
12. Payment checkout with timeout and duplicate request
13. Secure document upload
14. Last-seat booking with concurrent users
15. Role-based API data isolation

## Self-review rubric (20 points)

Give each category 0, 1 or 2:
- 0 = missing
- 1 = partial
- 2 = clear and correct

| Category | Score |
|---|---:|
| Requirement understanding | /2 |
| Positive coverage | /2 |
| Negative coverage | /2 |
| Boundary/EP coverage | /2 |
| Business rules/state/roles | /2 |
| Expected results | /2 |
| Test data | /2 |
| Priority/risk reasoning | /2 |
| Clarity and independence | /2 |
| Interview explanation | /2 |
| **Total** | **/20** |

- 0–9: Revisit fundamentals.
- 10–14: Developing; practice scenario breakdown.
- 15–17: Good working level.
- 18–20: Strong structured answer; still validate through review/execution.

# 19. Tips, tricks and common mistakes

## Practical tips
1. Ask "What can go wrong?" Think user, data, business rule, permission, state and integration.
2. Requirement keywords reveal test dimensions.
3. For numeric ranges, think EP + BVA together.
4. For multiple conditions, draw a decision table.
5. For workflows, draw a state table/diagram.
6. For many configuration dimensions, consider pairwise.
7. For critical user goals, design end-to-end cases.
8. For security, test unauthorized paths directly.
9. Verify side effects too. A rejected payment must not create a paid order.
10. Keep cases independent.
11. Prioritize critical business risks.
12. Use synthetic, controlled test data.

## Common mistakes

| Mistake | Better approach |
|---|---|
| Only happy path | Add negative, boundary, role/state cases |
| Guessing missing rules | Raise clarification |
| "System works fine" | State observable result |
| Duplicate cases | Use partitions and risk review |
| BVA without inclusive/exclusive rule | Clarify range semantics |
| Impossible decision combinations | Identify constraints/don't-care rules |
| Only UI permission checks | Verify backend authorization |
| All combinations blindly | Use pairwise/risk-based selection |
| One giant test | Split by objective |
| Real credentials in test data | Secure synthetic data |
| No meaningful assertion | Assert business outcome and side effects |
| Claiming "100% coverage" loosely | State the exact coverage metric |

## Fast mental checklist — P-N-B-R-S-I

Before finalizing:
- **P** — Positive: valid flow?
- **N** — Negative: invalid input/action?
- **B** — Boundary: min/max/just outside?
- **R** — Rules: condition combinations?
- **S** — State/Security: workflow and permissions?
- **I** — Integration: API, payment, notification, file, network?

Not every feature needs all six. Use judgement and requirements.

# 20. Seven-session study plan

| Session | Study | Output |
|---|---|---|
| 1 | Foundations + requirement reading | Login requirement breakdown |
| 2 | Case writing + easy examples | 25 core cases |
| 3 | EP + BVA | Age, password, quantity, file-size cases |
| 4 | Decision table + state transition | Coupon and order tables |
| 5 | Use case + pairwise + error guessing | ATM, booking, configuration coverage |
| 6 | Medium + hard scenarios | 10 scenario-based designs |
| 7 | Interview simulation + revision | Speak answers without notes |

Suggested practice: 60–90 minutes per session. Read, close the file, explain from memory, then write independently.

# 21. Final one-page revision

| Situation | Technique |
|---|---|
| Large input range / similar values | Equivalence Partitioning |
| Min/max limits | Boundary Value Analysis |
| Multiple condition combinations | Decision Table |
| Workflow/status changes | State Transition |
| User goal across steps | Use Case / End-to-End |
| Many configuration parameters | Pairwise |
| Experience-based likely failures | Error Guessing |
| Learn and test simultaneously | Exploratory Testing |
| Limited time | Risk-based Testing |
| Requirement-to-case mapping | RTM |

## Interview lines to remember
- "I derive test cases from acceptance criteria, not assumptions."
- "I cover positive, negative, boundary and risk-based scenarios."
- "I select the technique based on the nature of the requirement."
- "I verify observable business outcomes and side effects."
- "I map cases to requirements using traceability."
- "I prioritize by business impact and likelihood."
- "I clarify ambiguity with the product owner."
- "I do not claim exhaustive testing when the input space is large."

## Completion checklist
- [ ] I can explain scenario vs test case.
- [ ] I can break requirements into conditions.
- [ ] I can write a complete test case with expected result.
- [ ] I can apply EP and BVA.
- [ ] I can build a decision table.
- [ ] I can identify valid/invalid state transitions.
- [ ] I can design end-to-end workflows.
- [ ] I know when pairwise is useful.
- [ ] I can prioritize by risk.
- [ ] I can create an RTM.
- [ ] I can answer common interview questions in clear English.
- [ ] I can solve a new scenario using R-A-C-E.

---

## Final advice

Ek baar read karna foundation dega, lekin interview-ready hone ke liye active practice zaroori hai. Har scenario par pehle 5–10 minutes khud socho, test cases likho, phir model examples se compare karo. Jo case miss hua, uske peeche ka reason samjho — sirf answer memorize mat karo.

**2-year experience interview mein strong candidate woh nahi jo 50 random cases bol de. Strong candidate woh hai jo requirement structure kare, relevant technique choose kare, risk explain kare, expected result clear rakhe aur apne design ko confidently defend kare.**
