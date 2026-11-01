# SDET Python Mentor Master Guide

**Python-first QA Automation / SDET playbook | Hinglish mentor notes**
Tumhare 4 course-notes (Software Testing Fundamentals, Minnesota Intro to Testing, Launching Your QA Career, Gen-AI for QA) ka consolidated, duplicate-free version.

---

# Part 0 — Pehle ye padho

## 0.1 Ye guide kya hai (aur kya nahi)

- Ye **ek single file** hai. Purane ~180k words ke notes me jo concepts 3-3 baar repeat the, yahan ek baar hain.
- Har part ke end me **"Original notes me depth"** likha hai, jahan zyada detail chahiye wahan wo file kholo.
- Ye **notes** hain, skill nahi. Skill tab banti hai jab tum khud test cases likho, code chalao, fail hone do aur debug karo. Isliye har part me practice hai aur end me proof-of-work checklist hai.
- Code examples ke baare me honest baat: pytest, requests, mock aur SQL ke examples maine chala ke check kiye hain (sab pass). **Playwright aur Selenium ke examples maine browser me nahi chalaye** (is environment me browser download possible nahi). Unhe tum apni machine par run karke confirm karo. Jo error aaye wo bhi seekhne ka hissa hai.

## 0.2 Har topic ka format

Core topics (jisme code hai) ka flow:

`WHY` (kyun chahiye) → `WHAT` (kya hai) → `HOW` (kaise kaam karta hai) → `CODE` → `LINE-BY-LINE` → `REAL-WORLD` → `COMMON MISTAKES` → `PRACTICE` → `REVIEW`

Theory topics me ye flow chhota hai. **Har part ke start me "Pehle terms" hai.** Jo term use hoga wo pehle define hoga.

**Interview answers sirf concept samajhne ke baad aate hain.** Format: simple English → strong 1–2 minute answer → keywords.

## 0.3 Study ka 3-pass rule

1. **Pass 1:** sirf WHY aur WHAT padho. File band karo. Apne words me bolo ya likho.
2. **Pass 2:** PRACTICE khud karo. Answer key baad me dekho.
3. **Pass 3 (24 ghante baad):** interview answer memory se bolo. Jo atka use mistake tracker me daalo (Part 13.4).

## 0.4 Honest reality check: language strategy

Tumhara sawaal tha: "Python me bahut time diya hai, naya language master nahi kar sakta."

**Seedhi baat:** tumhe Java ya TypeScript master karne ki zaroorat nahi hai. Lekin ye bhi sach hai ki job market ke baare me kuch cheezein jaan lo:

- Jo job postings aur blogs maine dekhe (India, 2026), unme Playwright aur Selenium bahut aate hain, aur unke saath **Java ya JavaScript/TypeScript** zyada common hai. Python wale roles hain, par kam. Ye aggregator aur blog data hai, census nahi. Direction ke liye lo, final truth nahi.
- Isliye strategy "sab kuch seekh lo" nahi, balki **teen layers** hai:

| Layer | Kya | Level | Kahan |
|---|---|---|---|
| 1. Mastery | Python, pytest, Playwright-Python, requests, SQL, Git, GitHub Actions | Interview me defend kar sako (L3) | Part 6–9 |
| 2. Working knowledge | Selenium **in Python** (kyunki "Selenium" keyword bahut JDs me hai) | Basics aur explicit waits samjho (L2) | Part 10.1–10.2 |
| 3. Reading literacy | Java aur TypeScript code **padhna** | Code dekh ke samajh jao ki kya ho raha hai. Likhna zaroori nahi | Part 10.3–10.5 |

Good news: **Playwright ka concept language-independent hai.** Locators, auto-wait, contexts, expect, POM, storage_state sab same hain. Sirf syntax badalta hai (`get_by_role` vs `getByRole`, aur TypeScript me `await`). Isliye Layer 3 ka bojh kam hai.

**Apply kaise karna hai:**
- JD me "Python" ya "Python/Java" ya "any language" ho to apply karo.
- "Java mandatory" ho to blindly apply mat karo. Time waste hoga.
- Interview me jo nahi aata wo **bolo mat ki aata hai**. Part 10.5 me exact truthful lines hain.

## 0.5 Level system (har topic ke liye)

| Level | Matlab |
|---|---|
| L1 Recall | Bina dekhe apne words me explain kar sakte ho |
| L2 Apply | Naye scenario par khud test/code likh sakte ho |
| L3 Defend | Batao kyun ye approach, alternatives aur risks kya hain |

Target: P0 topics (test design, API, SQL, Python, pytest, Playwright) me **L3**. Baaki me L2.

---

# Part 1 — Testing Foundations

## Pehle terms

- **Software testing:** software ko chala ke dekhna ki wo expected behaviour deta hai ya nahi, aur defects dhundhna.
- **Defect / bug:** expected aur actual behaviour me gap.
- **Requirement:** ek line jo batati hai software ko kya karna chahiye. Example: "Password kam se kam 8 characters ka hona chahiye." Test likhne se pehle requirement padhna aur uski ambiguity pakadna tester ka pehla kaam hai.
- **Test case:** ek specific check (input + steps + expected result).
- **SUT (System Under Test):** jo cheez tum test kar rahe ho.

## 1.1 Quality, QA, QC, Testing, UAT

**WHY:** Companies me log in teeno words ko mix karte hain. Interview me ye pehla sawaal hota hai.

**WHAT:**

| Term | Focus | Question | Example |
|---|---|---|---|
| **QA** (Quality Assurance) | **Process.** Defects hone se pehle rokna | "Hum sahi tareeke se kaam kar rahe hain?" | Code review rules, test strategy, definition of done |
| **QC** (Quality Control) | **Product.** Defects dhundhna | "Jo banaya wo sahi hai?" | Test execution, bug finding |
| **Testing** | QC ki main activity | "Is feature me bug hai?" | Test cases chalana |
| **UAT** | Business/end user validate karta hai | "Kya ye hamari zaroorat poori karta hai?" | Client release se pehle try karta hai |

**Verification vs Validation:**
- Verification = "Are we building the product **right**?" (spec ke hisaab se bana? reviews, static checks)
- Validation = "Are we building the **right product**?" (user ki zaroorat poori hui? UAT, demo)

**Real-world:** Checkout me coupon bug mila. QC = bug dhundha. QA = sochna ki coupon logic ke liye requirement review aur unit tests pehle kyun nahi the, aur process fix karna.

**Common mistakes:**
- "QA matlab testing" bolna. Testing QA ka sirf ek hissa hai.
- UAT ko QA team ka kaam batana. UAT business side ka hota hai.

**Interview answer: QA vs QC**
- *Simple:* QA prevents defects through good process. QC finds defects in the product.
- *Strong (1 min):* "QA is process-focused and preventive. It covers things like defining the test strategy, review practices and standards, so defects are less likely to occur. QC is product-focused and detective. It covers executing tests and finding defects in the built software. For example, if a coupon bug reaches checkout, QC is finding and reporting it, and QA is asking why requirements review or unit tests didn't catch it and fixing that process."
- *Keywords:* process vs product, preventive vs detective, verification, validation.

## 1.2 Seven testing principles

**WHY:** Ye batate hain ki limited time me testing kaise sochni hai. Definitions ratne ke liye nahi hain.

| # | Principle | Matlab | Tester kya kare |
|---|---|---|---|
| 1 | Testing shows presence of defects, not absence | 100 test pass ≠ bug-free | "Maine kya test kiya, kya baaki hai?" ye batao |
| 2 | Exhaustive testing impossible | Har input/combination test nahi ho sakta | Risk ke hisaab se prioritise karo |
| 3 | Early testing saves cost | Requirement stage ke bug sasta fix hota hai | Requirements review me shamil ho |
| 4 | Defect clustering | Bugs kuch modules me zyada hote hain | Un modules par zyada focus |
| 5 | Pesticide paradox | Same tests baar baar chalane se naye bug nahi milte | Tests ko update karo, naye cases add karo |
| 6 | Testing is context-dependent | Banking app aur game ki testing alag | Context ke hisaab se approach |
| 7 | Absence-of-errors fallacy | Bug-free software bhi bekaar ho sakta hai agar user ki zaroorat poori nahi karta | Validation (user need) bhi check karo |

**Common mistake:** Principle 2 ka matlab "kam test karo" nahi hai. Matlab "smart test karo".

## 1.3 Static vs dynamic testing, test levels, pyramid

- **Static testing:** code **chalaye bina**. Requirements review, code review, linting.
- **Dynamic testing:** code **chala ke**. Test execution.

**Test levels** (kitna bada hissa test ho raha hai):

| Level | Kya test hota hai | Kaun |
|---|---|---|
| Unit | Ek function/class | Developer (SDET bhi kabhi) |
| Integration | Do ya zyada components saath (API + DB) | Dev + SDET |
| System | Poori application, requirements ke against | QA/SDET |
| Acceptance | Business needs poori hui? | Business/UAT |

**Test pyramid:** Bahut saare fast unit tests (neeche), medium API/integration tests (beech me), kam UI end-to-end tests (upar). Kyun? UI tests slow aur fragile hote hain. Ye guide hai, rigid ratio nahi.

## 1.4 Test types

| Type | Kya check karta hai |
|---|---|
| **Functional** | Feature sahi kaam karta hai? (login, cart) |
| **Non-functional** | Kaise kaam karta hai? (speed, usability, security) |
| **Black-box** | Andar ka code dekhe bina, input/output se |
| **White-box** | Code structure ke basis par (branches, statements) |
| **Grey-box** | Thoda internal knowledge (API + DB dekhna) |
| **Smoke** | Build itna stable hai ki aage testing ho sake? Broad aur shallow |
| **Sanity** | Ek specific fix/change ke around focused check |
| **Retest (confirmation)** | Jo test fail hua tha wahi dobara, check karne ke liye ki bug fix hua |
| **Regression** | Change ke baad purani cheezein toot to nahi gayi |
| **Maintenance** | Live software me change ke baad testing |

**Common mistake:** Retest aur regression ko same bolna. Retest = specific bug fix check. Regression = baaki cheezein safe hain.

## 1.5 STLC (Software Testing Life Cycle)

**WHAT:** Testing ke 6 phases. Har phase ka ek entry (kab shuru) aur exit (kab khatam) condition hota hai.

| Phase | Kya hota hai | Output |
|---|---|---|
| 1. Requirement analysis | Requirements padhna, ambiguity nikalna | Questions list, testable requirements |
| 2. Test planning | Scope, approach, risks, resources | Test plan |
| 3. Test case development | Test cases + test data | Test cases, RTM |
| 4. Environment setup | Test environment ready karna | Ready environment, smoke check |
| 5. Test execution | Tests chalana, bugs report karna | Results, defect reports |
| 6. Test closure | Summary, lessons learned | Test summary report |

**Interview answer: What is STLC?**
- *Simple:* STLC is the sequence of testing activities, from understanding requirements to closing testing.
- *Strong:* "STLC has six phases: requirement analysis, test planning, test case development, environment setup, execution and closure. Each phase has entry and exit criteria and a deliverable. In practice, in Agile these phases overlap inside a sprint rather than happening one after another, but the activities still exist."
- *Keywords:* entry/exit criteria, deliverables, requirement analysis, RTM.

## PRACTICE 1 (sirf upar padhe hue se)

1. Ek app me "Forgot password" feature hai. Ye QA ka kaam hai ya QC ka? Review process banana vs reset flow chala ke dekhna, dono ko label karo.
2. Tumne 50 tests chalaye, sab pass. Principle 1 ke hisaab se manager ko kya bologe?
3. Ek bug fix hua. Pehle wahi failed test dobara chalaya. Phir login, search aur cart bhi check kiye. Dono steps ke naam batao.

**Answer key:** (1) Process banana = QA, reset flow chala ke dekhna = QC. (2) "Ye prove nahi karta ki bug nahi hai. Mere tests ye ye cover karte hain, ye ye uncovered hain." (3) Pehla = retest/confirmation. Doosra = regression.

---

# Part 2 — Web Application Layers, DevTools aur HTTP

## Pehle terms

- **UI (presentation layer):** jo user dekhta hai (browser me page).
- **API (application layer):** jo backend business logic chalata hai. UI iske saath baat karta hai.
- **DB (data layer):** jahan data permanently store hota hai.
- **Request / Response:** browser server ko request bhejta hai, server response deta hai.
- **HTTP method:** request ka type (GET, POST...).
- **Status code:** response ka number jo result batata hai (200 = ok).

## 2.1 Three layers

**WHY:** Bug UI me dikh sakta hai par root cause API ya DB me ho sakta hai. Jab tum layer jaante ho to bug jaldi dhundh lete ho. SDET ke liye ye bahut zaroori hai.

**Example: "Add to cart"**

| Layer | Kya hota hai | Tester kya check kare |
|---|---|---|
| UI | Button click, cart count badalna | Button kaam karta hai? Count sahi dikha? |
| API | `POST /api/cart/items` request jaata hai | Request body sahi? Status 201? Response sahi? |
| DB | `cart_items` table me row insert | Row bani? Duplicate to nahi? Quantity sahi? |

**Real-world:** UI me "Added" dikha par refresh ke baad cart khaali. Matlab UI ne success dikhaya par API ya DB me save nahi hua. Ye tabhi pakad me aayega jab tum layers check karoge.

## 2.2 Browser DevTools (Network tab)

1. Page par right-click → Inspect (ya F12).
2. **Elements tab:** HTML aur CSS (UI layer).
3. **Network tab:** saari requests. Action karo (login click) aur request dekho.
4. Request select karo: **Headers** (URL, method, status), **Payload** (bheja hua data), **Response** (server ka jawab), **Timing**.

Practice habit: har bug report se pehle Network tab me dekho ki kaunsi request fail hui.

## 2.3 HTTP methods aur status codes

| Method | Kaam | Safe? | Idempotent? |
|---|---|---|---|
| GET | Data padhna | Haan | Haan |
| POST | Naya resource banana / action | Nahi | Nahi |
| PUT | Poora replace/update | Nahi | Haan |
| PATCH | Partial update | Nahi | Zaroori nahi |
| DELETE | Delete | Nahi | Haan |

- **Safe** = data change nahi karta. **Idempotent** = same request baar baar karne ka final result same rehta hai.
- POST idempotent nahi hai: double-click se do order ban sakte hain. Isliye "duplicate submit" ek important test hai.

| Code | Matlab |
|---|---|
| 200 OK / 201 Created / 204 No Content | Success |
| 400 Bad Request | Request galat/invalid |
| 401 Unauthorized | Login nahi hua ya token invalid (authentication) |
| 403 Forbidden | Login hai par permission nahi (authorization) |
| 404 Not Found | Resource nahi mila |
| 409 Conflict | Current state se conflict (duplicate) |
| 422 Unprocessable | Request samajh aayi par validation fail |
| 429 Too Many Requests | Rate limit |
| 500 Internal Server Error | Server me kuch toota |

**Important:** Sirf status code dekh ke conclusion mat nikalo. Body, requirement aur app ka design bhi dekho. 400 vs 422 kaunsa use hoga ye app design par depend karta hai.

**Interview answer: 401 vs 403**
- *Simple:* 401 means "who are you?" and 403 means "I know you, but you cannot do this."
- *Strong:* "401 is an authentication problem: the user isn't logged in or the token is missing or invalid. 403 is authorization: the user is authenticated but lacks permission. In API tests I check both, for example a normal user calling an admin endpoint should get 403, and a request with no token should get 401."
- *Keywords:* authentication, authorization, token, role-based access.

## PRACTICE 2

1. Login par tum email/password dalte ho. Teeno layers me kya hoga likho (UI, API, DB).
2. Server ne login par 200 diya par body me `{"error":"invalid"}` hai. Tum kya karoge?
3. User A ne user B ka order dekhne ki koshish ki. Kaunsa status code expected hai aur kyun?

**Answer key:** (1) UI: form submit. API: `POST /login` with credentials, response token. DB: user row lookup, password hash compare, session/last_login update. (2) Ye bug ho sakta hai (200 ke saath error body inconsistent hai). Requirement dekho, API contract se compare karo, dev se confirm karo. Sirf 200 dekh ke pass mat karo. (3) 403 (authenticated par permission nahi). Kuch apps 404 dete hain taaki existence na leak ho. Requirement check karo.

**Original notes me depth:** `Software_Testing_Fundamentals.../module_3/...Modules_1_to_3_Study_Guide.md` (ye cumulative file hai, baaki duplicates skip). Minnesota Module 1 me "why testing is hard" ka story.


---

# Part 3 — Test Design Techniques (sabse important part)

Interview me sabse zyada "isko kaise test karoge?" pucha jaata hai. Is part ko sabse zyada time do.

## Pehle terms

- **Test condition:** ek cheez jo test honi chahiye ("age 18 par accept ho").
- **Test scenario:** high-level situation ("user valid age se register kare").
- **Test data:** test me use hone wali values (17, 18, 19).
- **Expected result:** requirement ke hisaab se kya hona chahiye. **Actual result dekhne se pehle likho.**
- **Positive test:** valid input par sahi behaviour. **Negative test:** invalid input par sahi error.
- **Partition / class:** values ka group jo same tarah behave karna chahiye.

## 3.1 Requirement kaise padhein

**WHY:** Galat/adhoora requirement se galat test banta hai.

**HOW:** Har requirement me ye dhundho:
- **Kaun** (role) aur **kya** (action)?
- **Limits** (min, max, length, count)?
- **Rules** ("AND/OR/only if")?
- **Missing info:** empty input par kya hoga? Error message kya? Timezone? Inclusive ya exclusive?

**Example requirement:** "User ki age 18 se 60 tak ho to registration allowed."

**Ambiguity log (tester ke sawaal):**
- "18 aur 60 dono allowed (inclusive)?"
- "Decimal age (18.5)? Negative? Text?"
- "Blank age par error message kya?"

Ye sawaal requirement stage par poochna hi Principle 3 (early testing) hai.

## 3.2 Equivalence Partitioning (EP)

**WHAT:** Input ko groups (partitions) me baanto jo same tarah behave karenge. Har group se **ek representative** value lo. Har value test karne ki zaroorat nahi.

**Age 18–60:**

| Partition | Values | Valid? | Representative |
|---|---|---|---|
| Below min | ≤ 17 | Nahi | 17 (ya 5) |
| In range | 18–60 | Haan | 35 |
| Above max | ≥ 61 | Nahi | 61 (ya 100) |
| Non-numeric | "abc" | Nahi | abc |
| Empty | blank | Rule par depend | blank |

## 3.3 Boundary Value Analysis (BVA)

**WHAT:** Bugs aksar edges par hote hain (off-by-one: `<` vs `<=`). Isliye min aur max ke **upar-neeche** ki values test karo.

**Age 18–60 inclusive:** 17, 18, 19, 59, 60, 61.

**EP vs BVA:** EP = har group se ek value. BVA = group ke kinaare ki values. Dono saath use hote hain.

## 3.4 CODE: EP + BVA pytest me (verified)

```python
# shop.py
def is_eligible_age(age: int) -> bool:
    """18 se 60 tak (dono inclusive) eligible."""
    return 18 <= age <= 60
```

```python
# test_age.py
import pytest
from shop import is_eligible_age

@pytest.mark.parametrize(
    "age, expected",
    [(17, False), (18, True), (19, True), (59, True), (60, True), (61, False)],
    ids=["below-min", "min", "min+1", "max-1", "max", "above-max"],
)
def test_age_boundaries(age, expected):
    assert is_eligible_age(age) is expected
```

**LINE-BY-LINE:**
- `@pytest.mark.parametrize(...)` ek hi test function ko 6 baar alag data ke saath chalata hai. Har case alag test ban jaata hai.
- `"age, expected"` = argument names. List ke har tuple me (age, expected) hai.
- `ids=[...]` failure report me readable naam deta hai (`test_age_boundaries[min]`).
- `assert ... is expected` = result expected se match na kare to test fail.

**COMMON MISTAKES:**
- Sirf valid value test karna (35) aur samajhna ho gaya.
- Boundary me `<=` vs `<` ka bug miss karna.
- Ek test me 6 asserts daalna. Pehla fail hua to baaki chalte hi nahi. Parametrize behtar hai.

## 3.5 Decision Table Testing

**WHAT:** Jab output **kai conditions ke combination** par depend kare. Saari meaningful combinations ko table me likho.

**Requirement:** "Member ho **AND** cart ≥ ₹2000 **AND** coupon valid ho, tabhi 10% discount."

3 conditions = 2³ = 8 combinations:

| Rule | Member? | Cart ≥ 2000? | Coupon valid? | Discount? |
|---|---|---|---|---|
| R1 | Y | Y | Y | **Haan** |
| R2 | Y | Y | N | Nahi |
| R3 | Y | N | Y | Nahi |
| R4 | Y | N | N | Nahi |
| R5 | N | Y | Y | Nahi |
| R6 | N | Y | N | Nahi |
| R7 | N | N | Y | Nahi |
| R8 | N | N | N | Nahi |

```python
# shop.py (continued)
def apply_discount(total: float, is_member: bool, coupon_valid: bool) -> float:
    if is_member and coupon_valid and total >= 2000:
        return round(total * 0.9, 2)
    return total
```

```python
# test_discount.py
import pytest
from shop import apply_discount

@pytest.mark.parametrize(
    "member, coupon, total, expected",
    [
        (True,  True,  2000, 1800.0),   # R1: sab true, boundary 2000
        (True,  True,  1999, 1999),     # R3: cart boundary ke neeche
        (True,  False, 2500, 2500),     # R2: coupon invalid
        (False, True,  2500, 2500),     # R5: member nahi
        (False, False, 2500, 2500),     # R6
    ],
)
def test_discount_decision_table(member, coupon, total, expected):
    assert apply_discount(total, member, coupon) == expected
```

**Note:** Decision table + BVA saath use hue: `2000` aur `1999` cart ki boundary hai. Ye interview me achha point hai.

**REAL-WORLD:** Insurance claim, loan eligibility, shipping rules me yahi technique chalti hai.

## 3.6 State Transition Testing

**WHAT:** Jab koi cheez **states** me badalti hai (Order: Created → Paid → Packed → Shipped → Delivered). Valid aur **invalid** transitions test karo.

| Se / Event | Paid | Packed | Shipped | Delivered | Cancelled |
|---|---|---|---|---|---|
| Created | Valid | Invalid | Invalid | Invalid | Valid |
| Paid | - | Valid | Invalid | Invalid | Valid (refund) |
| Packed | - | - | Valid | Invalid | Requirement poochho |
| Shipped | - | - | - | Valid | Invalid |
| Delivered | - | - | - | - | Invalid |

*(Cancelled rules assumption hain. Real project me requirement se confirm karo.)*

```python
ALLOWED = {
    "CREATED":   {"PAID", "CANCELLED"},
    "PAID":      {"PACKED", "CANCELLED"},
    "PACKED":    {"SHIPPED"},
    "SHIPPED":   {"DELIVERED"},
    "DELIVERED": set(),
    "CANCELLED": set(),
}

def can_transition(current: str, nxt: str) -> bool:
    return nxt in ALLOWED[current]
```

Test idea: har valid transition True, har **invalid** (jaise `DELIVERED → PACKED`) False. Plus repeated event (do baar Pay) aur role permission.

## 3.7 Error guessing aur Exploratory testing

- **Error guessing:** experience se anumaan karna ki kahan bug hoga: empty field, duplicate submit, special characters, expired session, slow network, double click, bahut lamba input.
- **Exploratory testing:** ek time-box (jaise 30 min) aur charter ("checkout ko payment failure ke saath explore karo"). Dekho, seekho, likho. Script nahi, par notes zaroor.

## 3.8 Technique kab konsi

| Situation | Technique |
|---|---|
| Range/length/limit wala input | EP + BVA |
| Multiple conditions combine | Decision table |
| Status/workflow | State transition |
| Kai options ke combinations (browser × OS × plan) | Pairwise (kam combos me coverage) |
| Requirement unclear ya naya feature | Exploratory + error guessing |

## 3.9 Worked example: "Login page kaise test karoge?"

Is tarah structure me bolo (interview ke liye):
1. **Functional positive:** valid credentials → dashboard.
2. **Functional negative:** wrong password, unregistered email, empty fields, locked/inactive account.
3. **Validation:** email format, password length limits (BVA).
4. **Security:** password masked, brute-force lockout, SQL injection string field me, session expire, logout ke baad back button.
5. **Usability:** error messages clear, Enter key, tab order.
6. **Non-functional:** response time, concurrent logins.
7. **Layers:** Network tab me request/response, API se bhi test, DB me last_login.
8. **Automation:** kaunse tests regression me jayenge (smoke: valid login; baaki API level par).

Ye answer **structure** dikhata hai. Interviewer ko "random list" nahi, thinking dikhni chahiye.

## PRACTICE 3 (sirf Part 3 se)

1. **Requirement:** "Quantity 1 se 10 tak allowed." EP ke partitions aur BVA ke values likho.
2. **Requirement:** "Free shipping agar user Premium ho **OR** cart ≥ $100." 4 rules ka decision table banao.
3. Ek **password length 8–20** field ke liye BVA values likho.
4. State transition: ek user account `ACTIVE → LOCKED` 3 galat password ke baad. 2 invalid transitions batao.

**Answer key:**
1. EP: <1 (0), 1–10 (5), >10 (11), decimal (2.5), non-numeric (abc), empty. BVA: 0, 1, 2, 9, 10, 11.
2. (Premium N, ≥100 N → No), (N, Y → Yes), (Y, N → Yes), (Y, Y → Yes).
3. Lengths: 7, 8, 9, 19, 20, 21 (exact-length strings banao).
4. Example: `LOCKED → ACTIVE` without unlock/reset flow; `ACTIVE → LOCKED` after sirf 1 galat try (agar rule 3 hai).

**Interview answer: EP vs BVA**
- *Simple:* EP picks one value from each group. BVA tests the edges of those groups.
- *Strong:* "Equivalence partitioning reduces test count by grouping inputs expected to behave the same and picking a representative from each. Boundary value analysis targets the edges, because off-by-one bugs usually live there. For an age field of 18 to 60, EP gives me 35, 17 and 61, and BVA gives me 17, 18, 19, 59, 60, 61. I use them together, and add decision tables when conditions combine."
- *Keywords:* partition, representative, boundary, off-by-one, black-box.

**Original notes me depth:** `Launching_Your_QA_Career/Test_Case_Design_Masterbook_Hinglish_2_Year_SDET.md` (easy/medium/hard worked examples, RTM, risk).

---

# Part 4 — Defects, Planning aur Risk

## Pehle terms

- **Bug report:** defect ka likhit record jisse koi aur use reproduce kar sake.
- **Severity:** bug ka **impact** (kitna kharab).
- **Priority:** fix karne ki **urgency** (kab).
- **Test plan:** is project/release ke liye testing ka plan.
- **Test strategy:** organisation/product level ka general approach.
- **Entry/Exit criteria:** testing shuru/khatam karne ki shartein.
- **Risk:** kuch galat hone ki sambhavna aur uska impact.

## 4.1 Achhi bug report

| Field | Example |
|---|---|
| Title | Checkout: 'Pay' double-click par do orders ban jaate hain |
| Environment | QA, Chrome 126, build 2.4.1 |
| Steps | 1) Cart me item daalo 2) Checkout 3) 'Pay' par jaldi do baar click |
| Expected | Ek hi order, ek hi charge |
| Actual | Do orders, do charges |
| Evidence | Screenshot, Network request ID, logs |
| Severity / Priority | High / High |

**Rules:** reproducible steps, ek bug = ek report, facts likho (opinion nahi), evidence attach karo, "doesn't work" jaisi vague title mat likho.

## 4.2 Severity vs Priority

- Payment sab users ke liye fail: **High severity, High priority**.
- Internal page par typo: **Low, Low**.
- Legal/compliance text me galti: **Low severity, High priority** (crash nahi par urgent).
- Bahut rare crash ek obscure feature me: **High severity, Low priority**.

Fixed mapping mat ratto. Context dekho.

## 4.3 Defect lifecycle

`New → Assigned → Open → Fixed → Retest → Verified → Closed`
Side paths: `Reopened` (fix fail), `Rejected` (bug nahi), `Duplicate`, `Deferred` (baad me).

## 4.4 Test plan vs strategy

| | Test strategy | Test plan |
|---|---|---|
| Level | Organisation/product | Project/release |
| Badalta hai? | Kam | Har release |
| Content | Approach, tools, levels, automation policy | Scope, schedule, resources, risks, entry/exit |

## 4.5 Risk-based testing

**Thinking model:** priority badhti hai jab **failure ki sambhavna** ya **uska impact** badhta hai. Ye formula nahi, soch ka tareeka hai.

Priority tay karne ke sawaal: feature kitna use hota hai? Fail hone par paisa/user-trust ka nuksan? Change kitna complex? Pehle yahan bug mile the?

Example: Payment (high likelihood × high impact) pehle. Profile avatar change baad me.

## 4.6 RTM (Requirement Traceability Matrix)

| Requirement | Test cases | Defects |
|---|---|---|
| REQ-01 Login | TC-01…TC-08 | BUG-12 |
| REQ-02 Cart | TC-09…TC-20 | BUG-15, BUG-18 |

Kaam: kaunsi requirement ke liye test nahi hai? kaunsa test kis requirement ko cover karta hai?

## PRACTICE 4

1. Bug report title likho: "Search me special character `&` dalne par 500 error."
2. 3 bugs ko Severity/Priority do: (a) Login sab ke liye down, (b) Footer me logo ka rang thoda alag, (c) Refund amount galat calculate hota hai.
3. Time kam hai, 3 features: Payment, Wishlist, Profile photo. Priority order aur ek line me kyun.

**Answer key:** (1) "Search: query me '&' dalne par 500 Internal Server Error" + steps/expected/actual/evidence. (2) (a) High/High, (b) Low/Low, (c) High/High (paisa). (3) Payment → Wishlist → Profile photo. Payment me impact aur usage dono high hai.

---

# Part 5 — Agile, Scrum, CI/CD, Shift-left

## Pehle terms

- **SDLC:** software banane ke phases.
- **Waterfall:** phases ek ke baad ek, peeche nahi. Testing late hoti hai (risk).
- **V-Model:** Waterfall jaisa, par har development phase ke saamne ek testing phase.
- **Agile:** chhote iterations me kaam. **Sprint** = fixed time-box (aksar 1–4 hafte).
- **Backlog:** kaam ki list. **User story:** "As a user, I want ... so that ...".
- **Acceptance criteria:** story pass hone ki specific shartein.
- **Definition of Done (DoD):** team-level checklist (code reviewed, tests pass, etc.) jo har story par lagti hai.
- **CI (Continuous Integration):** code baar baar merge hota hai aur har baar automatic build + tests chalte hain.
- **CD:** tested code ko release/deploy karna.
- **Shift-left:** testing ko process me **pehle** laana.

## 5.1 Agile me QA kya karta hai

| Sprint stage | QA activity |
|---|---|
| Planning/refinement | Story review, acceptance criteria clarify, ambiguity sawaal, testability |
| Active sprint | Test cases, automation, story-wise testing, bug reporting, regression |
| Review/release | Demo support, release risk summary, retrospective inputs |

**Acceptance criteria vs DoD:** AC = *is story* ke liye. DoD = *saari stories* ke liye.

## 5.2 BDD / Gherkin

```gherkin
Feature: Login
  Scenario: Valid user logs in
    Given the user is on the login page
    When the user enters valid credentials
    Then the user sees the dashboard
```

Given = starting state, When = action, Then = expected result. Ye business aur tech dono ke liye readable hai. (Python me `pytest-bdd` ya `behave` use hote hain. Pehle plain pytest pakka karo.)

## 5.3 CI/CD pipeline me tests

`Commit → Build → Unit tests → Integration/API tests → E2E (UI) tests → Deploy`

- Jo test pehle fail hua pipeline wahin ruk jaati hai (fail fast).
- Fast tests pehle, slow UI tests baad me.
- Fail hone par developer ko report/artifacts (screenshot, trace) milne chahiye.

## 5.4 Shift-left: example

Requirement meeting me tester poochta hai "postal code ka format kaunse country ka? empty par kya?" → ambiguity coding se pehle solve. Rework sasta.

**Interview answer: Shift-left**
- *Simple:* Start testing activities earlier in the lifecycle.
- *Strong:* "Shift-left means involving QA from requirements and design, not after coding. I review stories for testability, ask about edge cases, define acceptance criteria and add automated checks early in the pipeline. The benefit is that defects found earlier are cheaper to fix and fewer reach staging."
- *Keywords:* early testing, testability, acceptance criteria, cost of defects, CI.

## PRACTICE 5

1. Story: "User apna profile photo upload kare." QA planning me 3 sawaal poochho.
2. Ek pipeline me E2E tests unit tests se pehle chal rahe hain. Kya galat hai?

**Answer key:** (1) Allowed formats? Max size? Upload fail/duplicate par kya? Crop/preview? (2) Slow aur fragile tests pehle chalne se feedback der se milta hai. Fast unit tests pehle, fail fast.

**Original notes me depth:** `Software_Testing_Fundamentals.../module_7` (Agile/CI-CD), `module_8` (Scrum testing), `module_9` (Sprint review), `module_10` (QA methodology). Interview ke liye inhe skim karna kaafi hai.

---

# Part 6 — pytest (tumhara main framework)

## Pehle terms

- **Test runner:** tool jo tests dhundh ke chalata aur result dikhata hai (pytest).
- **Fixture:** reusable setup/teardown. Test ko jo cheez chahiye (browser, data, config) wo fixture deta hai.
- **Scope:** fixture kitni der zinda rehta hai (har test, module, ya poora session).
- **Parametrize:** ek test ko alag-alag data ke saath chalana.
- **Marker:** test par label (`smoke`, `regression`) taaki select karke chala sako.
- **Mock:** asli dependency (API/DB) ki jagah nakli object, taaki test fast aur predictable ho.

## 6.1 Basics

**WHY pytest:** simple `assert`, powerful fixtures, parametrize, plugins (Playwright, xdist, reports).

**Rules:** file `test_*.py` ya `*_test.py`, function `test_*`. Test fail hota hai jab `assert` fail ho ya exception aaye.

```text
project/
├── pytest.ini
├── conftest.py            # shared fixtures
├── pages/                 # Page Objects
├── tests/
│   ├── api/
│   └── ui/
└── requirements.txt
```

## 6.2 Fixtures

```python
# conftest.py
import pytest

@pytest.fixture
def db_records():
    records = ["a", "b"]      # setup
    yield records             # test yahan chalta hai
    records.clear()           # teardown (test fail ho tab bhi chalta hai)

@pytest.fixture(scope="session")
def base_config():
    return {"env": "qa"}      # poore run me ek baar
```

```python
def test_uses_fixtures(db_records, base_config):
    assert db_records == ["a", "b"]
    assert base_config["env"] == "qa"
```

**LINE-BY-LINE:**
- Test ne argument ka naam `db_records` likha, pytest wahi fixture dhundh ke de deta hai (dependency injection).
- `yield` se pehle = setup, baad me = teardown.
- `conftest.py` ke fixtures usi folder aur uske neeche ke tests ko import kiye bina milte hain.
- `scope="session"` = ek baar. Default `function` = har test ke liye naya.

**Scopes:** `function` (default) < `class` < `module` < `package` < `session`. Chhota scope = zyada isolation. Bada scope = fast par shared state ka risk.

**COMMON MISTAKES:**
- Bade scope me aisa data rakhna jo test badal deta hai (tests ek doosre par depend karne lagte hain).
- Fixture me bahut kuch karna (login + data + browser). Chhote composable fixtures banao.
- Test order par depend karna. Har test akele chalna chahiye.

## 6.3 Markers aur pytest.ini

```ini
# pytest.ini
[pytest]
pythonpath = .
markers =
    smoke: critical quick checks
    regression: full regression suite
```

```python
@pytest.mark.smoke
def test_login_basic():
    ...
```

Run: `pytest -m smoke`. Markers register karo, warna typo silently ignore ho sakte hain.

## 6.4 Exceptions, mocking, monkeypatch

```python
import pytest

def test_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

**Mock: "patch where it is used".**

```python
# shop.py
import requests

def get_user_name(base_url: str, user_id: int) -> str:
    resp = requests.get(f"{base_url}/users/{user_id}", timeout=5)
    resp.raise_for_status()
    return resp.json()["name"]
```

```python
# test_shop.py
from unittest.mock import patch, Mock
from shop import get_user_name

def test_get_user_name_with_mock():
    fake = Mock()
    fake.json.return_value = {"name": "RK"}
    fake.raise_for_status.return_value = None
    with patch("shop.requests.get", return_value=fake) as m:
        assert get_user_name("http://x", 7) == "RK"
        m.assert_called_once_with("http://x/users/7", timeout=5)
```

**LINE-BY-LINE:**
- `Mock()` ek nakli response. `fake.json.return_value = {...}` batata hai `.json()` kya lautayega.
- `patch("shop.requests.get")` = **shop module me** `requests.get` ko replace karo. Rule: jahan use ho raha hai wahan patch karo.
- `assert_called_once_with(...)` = verify karo ki sahi arguments se ek baar call hua. (Ye "mock" ka output-verification hai.)

**monkeypatch** (pytest ka built-in): environment/attributes temporarily badalna.

```python
def test_env(monkeypatch):
    import os
    monkeypatch.setenv("APP_ENV", "qa")
    assert os.environ["APP_ENV"] == "qa"
```

**Test double ki terminology (Minnesota course se, language-independent):**

| Type | Kaam |
|---|---|
| Dummy | Sirf argument fill karne ke liye, use nahi hota |
| Stub | Fixed answer deta hai |
| Fake | Chhota working implementation (in-memory DB) |
| Mock | Verify karta hai ki call hua ya nahi |
| Spy | Asli object ko wrap karke calls record karta hai |

Python me `unittest.mock.Mock/MagicMock/patch` se ye sab ban jaate hain. Java me Mockito wahi kaam karta hai (Part 10).

**COMMON MISTAKES:**
- Galat jagah patch karna (`requests.get` ko global patch karke chhod dena).
- Over-mocking: sab mock kar diya to test kuch real verify hi nahi karta.
- Mock ko UI automation me use karna jab real flow test karna tha.

## 6.5 Useful commands

| Command | Kaam |
|---|---|
| `pytest -v` | Detail me result |
| `pytest -s` | `print()` output dikhao |
| `pytest -x` / `--maxfail=1` | Pehle failure par ruk jao |
| `pytest -k "login"` | Naam me "login" wale tests |
| `pytest -m smoke` | Marker se |
| `pytest --lf` | Last failed tests dobara |
| `pytest --tb=short` | Chhota traceback |
| `pytest --pdb` | Fail par debugger |
| `pytest -n auto` | Parallel (pytest-xdist plugin chahiye) |

## PRACTICE 6

1. Ek function `is_even(n)` ke liye parametrize test likho 5 values ke saath (negative aur zero include).
2. Ek fixture banao jo temporary list de aur test ke baad clear kare. Dono ka alag test likho. Kya list share hoti hai? (Scope ke saath socho.)
3. `get_user_name` ke liye ek test likho jisme `raise_for_status` exception de. Test kya verify karega?

**Review checklist (L2):** Kya tum bina dekhe fixture, scope, parametrize aur patch ka example likh sakte ho?

---

# Part 7 — Playwright (Python)

## Pehle terms

- **Browser:** browser process (Chromium/Firefox/WebKit).
- **BrowserContext:** ek isolated browser "profile". Apni cookies aur storage. Do context = do alag users.
- **Page:** context ke andar ek tab.
- **Locator:** page par element dhundhne ka tareeka. Playwright me locator **lazy** hota hai: action ke time par element dhundhta hai.
- **Auto-wait / actionability:** click jaise action se pehle Playwright khud check karta hai ki element visible, stable, enabled aur click receive kar sakta hai ya nahi.
- **Web-first assertion:** `expect(...)` jo condition poori hone tak retry karta hai (default ~5 sec).
- **POM (Page Object Model):** har page ke locators aur actions ek class me.
- **storage_state:** login ke baad cookies/localStorage ko file me save karna taaki baar baar login na karna pade.

## 7.1 Setup

```bash
pip install pytest-playwright
playwright install chromium
pytest --base-url http://localhost:3000 --headed
```

`pytest-playwright` tumhe `page`, `context`, `browser` fixtures deta hai. `--base-url` set ho to `page.goto("/login")` chalega.

## 7.2 First test

```python
import re
from playwright.sync_api import Page, expect

def test_valid_login(page: Page):
    page.goto("/login")
    page.get_by_label("Username").fill("user")
    page.get_by_label("Password").fill("pass")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url(re.compile(r".*/protected\.html"))
    expect(page.get_by_role("heading", name="Protected Area")).to_be_visible()
```

**LINE-BY-LINE:**
- `page: Page` fixture se aata hai. Type hint sirf editor help ke liye.
- `get_by_label("Username")` = label text se input dhundho (user jaisa sochta hai waisa).
- `get_by_role("button", name="Login")` = accessibility role + naam. Sabse stable approach.
- `.fill(...)` text daalta hai. `.click()` click karta hai. Dono pehle auto-wait karte hain.
- `expect(page).to_have_url(...)` URL badalne tak retry. Regex isliye ki base URL change ho sakta hai.
- Aakhri line stronger evidence hai: sirf URL nahi, page ka content bhi check.

## 7.3 Locator priority

| Priority | Locator | Kyun |
|---|---|---|
| 1 | `get_by_role(...)` | User/accessibility ke jaisa, stable |
| 2 | `get_by_label`, `get_by_placeholder` | Forms ke liye |
| 3 | `get_by_text` | Visible text par, text change se toot sakta hai |
| 4 | `get_by_test_id("...")` | Jab dev `data-testid` de. Stable |
| 5 | CSS | Sirf jab upar wale na chalein |
| Last | XPath (khaaskar lambe absolute) | Brittle |

## 7.4 expect vs plain assert (bahut common mistake)

```python
# GALAT: turant value padhta hai, retry nahi karta
assert page.get_by_role("status").inner_text() == "Saved"

# SAHI: condition hone tak retry karta hai
expect(page.get_by_role("status")).to_have_text("Saved")
```

`to_have_text` = poora text match. `to_contain_text` = text ke andar present hona. Requirement ke hisaab se strictness chuno.

## 7.5 Page Object Model

```python
# pages/login_page.py
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_label("Username")
        self.password = page.get_by_label("Password")
        self.submit = page.get_by_role("button", name="Login")

    def open(self):
        self.page.goto("/login")

    def login(self, user: str, pwd: str):
        self.username.fill(user)
        self.password.fill(pwd)
        self.submit.click()
```

```python
# conftest.py
import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.open()
    return lp
```

```python
# tests/ui/test_login.py
from playwright.sync_api import expect

def test_login_success(login_page, page):
    login_page.login("user", "pass")
    expect(page.get_by_role("heading", name="Protected Area")).to_be_visible()
```

**Locators `__init__` me kyun chalte hain?** Kyunki Playwright locators lazy hain: element tab dhundha jaata hai jab action hota hai.

**POM ka WHY:** locator change hua to ek jagah badlo, 50 tests nahi.
**POM ki galti:** assertions aur poore business workflows ek giant page class me bharna. Page object **kaise** karna wo batata hai, **kya verify** karna wo test batata hai.

## 7.6 Login ek baar, storage_state se (bahut important)

**WHY:** Har test me UI login karna slow hai aur flaky. Ek baar login karo, state save karo, har test naye context me wo state load kare.

```python
# conftest.py (additional)
import pytest
from playwright.sync_api import expect

@pytest.fixture(scope="session")
def auth_state_file(browser, base_url, tmp_path_factory):
    path = tmp_path_factory.mktemp("auth") / "user.json"
    context = browser.new_context(base_url=base_url)
    page = context.new_page()
    page.goto("/login")
    page.get_by_label("Username").fill("user")
    page.get_by_label("Password").fill("pass")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="Protected Area")).to_be_visible()
    context.storage_state(path=str(path))
    context.close()
    return str(path)

@pytest.fixture
def auth_page(browser, base_url, auth_state_file):
    context = browser.new_context(base_url=base_url, storage_state=auth_state_file)
    page = context.new_page()
    yield page
    context.close()
```

**LINE-BY-LINE:**
- `scope="session"`: login poore run me ek baar.
- `browser` aur `base_url` pytest-playwright/pytest-base-url ke fixtures hain.
- `context.storage_state(path=...)` cookies + localStorage JSON me save.
- `auth_page` har test ke liye **naya context** banata hai usi saved state ke saath. Isse isolation bhi rehta hai.
- `yield` ke baad `context.close()` = teardown.

**COMMON MISTAKES:**
- Ek hi authenticated context ko poore session me share karna. Ek test logout kare to baaki toot jaate hain, aur parallel runs me state mutate hoti hai.
- State file ko git me commit karna (isme session cookies hoti hain). `.gitignore` me daalo.
- Real credentials code me likhna. Environment variables/secret manager use karo.

## 7.7 Network: wait, check, mock

```python
# Request ka response verify karna
with page.expect_response("**/api/login") as resp_info:
    page.get_by_role("button", name="Login").click()
assert resp_info.value.status == 200
```

```python
# Backend ko fake karna (UI ko error state me dekhne ke liye)
page.route(
    "**/api/products",
    lambda route: route.fulfill(status=200, json=[{"id": 1, "name": "Test"}]),
)
```

## 7.8 Debugging aur evidence

```bash
pytest --tracing retain-on-failure --screenshot only-on-failure --video retain-on-failure
playwright show-trace test-results/<test-folder>/trace.zip
```

| Tool | Kaam |
|---|---|
| Trace viewer | Step-by-step timeline, DOM snapshot, network, console |
| `page.pause()` / Playwright Inspector | Test rok ke interactively dekhna |
| `locator.count()`, `locator.highlight()` | Kitne elements match hue, kaunsa |
| Screenshots/video | Failure ka visual proof |

**Strict mode error:** locator ek se zyada elements match kare to Playwright error deta hai. Locator ko aur specific banao (`name=`, scope container). `.first` shortcut se bacho jab tak zaroori na ho.

## 7.9 Common mistakes (Playwright)

- `time.sleep()` ya `page.wait_for_timeout()` har jagah. Condition par wait karo (`expect`, `expect_response`).
- `force=True` se actionability bypass karna. Pehle pata lagao element kyun actionable nahi hai.
- Retries se flaky test chhupana. Pehle root cause (Part 9).
- Raw `assert` + `inner_text()` (7.4).
- Brittle XPath (`/html/body/div[3]/...`).

## PRACTICE 7 (sirf Part 7 se)

1. Is locator ko behtar karo: `page.locator("div:nth-child(3) > button")` jabki button ka text "Add to cart" hai.
2. Ye test flaky kyun hai? `page.click("#save"); time.sleep(3); assert page.inner_text("#msg") == "Saved"`. Fix likho.
3. `LoginPage` me `expect(...)` assertion daalna kya sahi hai? Apna jawab POM ke rule se justify karo.

**Answer key:** (1) `page.get_by_role("button", name="Add to cart")`. (2) Fixed sleep timing par bet hai aur raw assert retry nahi karta. Fix: `page.get_by_role("button", name="Save").click()` phir `expect(page.locator("#msg")).to_have_text("Saved")`. (3) Generally nahi: page object actions deta hai, verification test ki zimmedari hai. Chhote helper-state checks (jaise `is_loaded()`) acceptable ho sakte hain.

**Original notes me depth:** `Gen-AI.../module_8` (storage_state), `module_10` (CI), `Software_Testing_Fundamentals.../misc/...Interview_Cheat_Sheet_2026.md` (Playwright Q&A 51–61).

---

# Part 8 — API Testing aur SQL

## Pehle terms

- **API testing:** UI ke bina seedha backend endpoints ko test karna.
- **Endpoint:** API ka URL + method (`GET /users/1`).
- **Payload / body:** request ke saath bheja gaya data (aksar JSON).
- **JSON:** key-value data format.
- **Schema / contract:** response ka expected structure (kaunsi keys, kaunsa type).
- **Authentication token:** login ke baad mila "pass" jo har request ke saath jaata hai (`Authorization: Bearer ...`).
- **SQL:** database se data padhne/badalne ki language.

## 8.1 API test me kya check karte hain

1. **Status code** sahi?
2. **Response body**: keys, types, values.
3. **Headers**: `Content-Type`.
4. **Negative cases**: missing field, galat type, invalid ID, bina token (401), galat role (403).
5. **Boundaries**: lambe strings, 0/negative numbers.
6. **Idempotency/duplicates**: POST do baar.
7. **Data side-effects**: DB me asar hua?
8. **Response time** (basic).

**WHY API tests UI se behtar:** fast, stable, root cause jaldi mil jaata hai. Test pyramid ka beech wala hissa.

## 8.2 requests library (verified)

> Neeche `base_url` ek pytest fixture hai (conftest me define karo, ya `pytest-base-url` plugin ka `--base-url` option use karo). Examples me yahi maan ke chala hai.

```python
import requests

def test_get_user(base_url):
    r = requests.get(f"{base_url}/users/1", timeout=5)
    assert r.status_code == 200
    assert r.json()["name"] == "RK"
    assert r.headers["Content-Type"].startswith("application/json")

def test_not_found(base_url):
    assert requests.get(f"{base_url}/users/999", timeout=5).status_code == 404

def test_create_validation(base_url):
    ok = requests.post(f"{base_url}/users", json={"email": "a@b.com"}, timeout=5)
    bad = requests.post(f"{base_url}/users", json={}, timeout=5)
    assert ok.status_code == 201
    assert bad.status_code == 400
```

**LINE-BY-LINE:**
- `timeout=5` hamesha do. Warna server na jawab de to test atka rahega.
- `json=payload` dict ko JSON body bana ke bhejta hai aur header khud set karta hai.
- `r.json()` response ko Python dict me badalta hai.
- Negative test (`bad`) utna hi zaroori hai jitna positive.

**Session + auth:**

```python
import requests

with requests.Session() as s:
    s.headers.update({"Authorization": "Bearer <token>"})
    r = s.get(f"{base_url}/users/1", timeout=5)
```

Session har request me headers/cookies reuse karta hai. pytest me isse fixture bana do.

**COMMON MISTAKES:**
- Sirf status code assert karna, body nahi.
- Hard-coded IDs jo kisi aur ke data par depend karte hain. Test apna data banaye aur cleanup kare.
- Tokens aur passwords code me likhna.
- Response schema ko loosely check karna. Required keys aur types assert karo (bade schemas ke liye `jsonschema` library use kar sakte ho).

## 8.3 SQL for testers

**WHY:** UI/API pe "success" dikha par data sach me save hua ya nahi, ye DB hi batayega. Interviews me SQL basics aate hain.

| Clause | Kaam |
|---|---|
| `SELECT` | Kaunse columns |
| `WHERE` | Row filter |
| `GROUP BY` + `COUNT` | Group karke ginna |
| `HAVING` | Group par filter |
| `JOIN` | Tables jodna |

**INNER JOIN** = dono me match wali rows. **LEFT JOIN** = left table ki saari rows + match, na mile to right side `NULL`.

Teen queries jo har tester ko aani chahiye (maine sqlite par chala ke verify ki):

```sql
-- 1) Orders jinke payment nahi hue
SELECT o.order_id
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE p.order_id IS NULL;

-- 2) Status ke hisaab se count
SELECT status, COUNT(*) AS order_count
FROM orders
GROUP BY status;

-- 3) Duplicate emails
SELECT email, COUNT(*) AS occurrences
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

**Query 1 kyun kaam karti hai?** LEFT JOIN me jis order ka payment nahi hai uska `p.order_id` `NULL` aa jaata hai. `WHERE ... IS NULL` wahi rows nikalta hai.

**WHERE vs HAVING:** `WHERE` group banne se pehle rows filter karta hai. `HAVING` group banne ke baad.

**Python me DB check (concept demo, sqlite):**

```python
import sqlite3

def test_no_duplicate_emails():
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
        CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT);
        INSERT INTO users VALUES (1,'a@x.com'),(2,'b@x.com');
    """)
    rows = conn.execute(
        "SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1"
    ).fetchall()
    assert rows == []
    conn.close()
```

Real project me tum apne DB ka driver use karoge (PostgreSQL/MySQL), par pattern wahi: query chalao, rows par assert karo.

**Safety rules:** sirf test environment me, read-only access jahan possible, production par kabhi destructive query nahi.

## 8.4 UI → API → DB ek flow me

Order place karo (UI) → Network tab me request/response → `SELECT` se order aur payment rows dekho → teeno ek jaise hone chahiye. Ye "grey-box" thinking SDET ki pehchaan hai.

## PRACTICE 8

1. `POST /users` ke liye 6 test ideas likho (positive, negative, boundary, auth).
2. Query likho: har `user_id` ke kitne orders hain? Phir sirf wo users jinke 2 se zyada orders hain.
3. `LEFT JOIN` me `WHERE p.order_id IS NULL` ki jagah `WHERE p.order_id IS NOT NULL` likhne se kya milega?

**Answer key:** (1) valid payload (201), missing required field (400), invalid email format, duplicate email (409 ya app ke hisaab se), bina token (401), email ke lambe length par boundary. (2) `SELECT user_id, COUNT(*) AS n FROM orders GROUP BY user_id HAVING COUNT(*) > 2;` (3) Wo orders jinke payment **hain** (INNER JOIN jaisa result).

**Original notes me depth:** `Gen-AI.../module_4` (Bruno, API debugging), `Interview_Cheat_Sheet_2026.md` (API Q32–38, SQL Q39–43). Dhyan do: SQL aur API ka original notes me depth kam hai. Isliye is part ko extra practice do.

---

# Part 9 — CI (GitHub Actions), Flaky Tests aur Debugging

## Pehle terms

- **Pipeline / workflow:** automatic steps ka sequence jo code push par chalta hai.
- **Runner:** machine jahan pipeline chalti hai.
- **Artifact:** run ke output files (reports, screenshots, traces) jo save hote hain.
- **Flaky test:** same code par kabhi pass, kabhi fail.
- **Root cause:** failure ki asli wajah (symptom nahi).
- **Traceback:** Python ka error report jo batata hai kaunsi line, kaunse call chain se fail hua.

## 9.1 GitHub Actions workflow

```yaml
name: Tests
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: pip
      - run: pip install -r requirements.txt
      - run: playwright install --with-deps chromium
      - name: Run tests
        run: pytest -v --base-url "$BASE_URL" --tracing retain-on-failure
        env:
          BASE_URL: ${{ secrets.QA_BASE_URL }}
      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: test-results
          path: test-results/
          if-no-files-found: ignore
```

**LINE-BY-LINE:**
- `on:` kab chale (push aur PR par main branch ke liye).
- `checkout` code laata hai. `setup-python` Python install karta hai (`cache: pip` dependencies fast).
- `playwright install --with-deps chromium` browser + OS libraries.
- `env` + `secrets`: URL/credentials repo secrets me, code me nahi.
- `if: always()` = test fail ho tab bhi artifacts upload ho (warna failure ka proof gayab).

**Important:** Action versions (`@v4`, `@v5`) samay ke saath badalte hain. Use karne se pehle official docs me latest major version dekh lo. Ye YAML maine run nahi kiya, apni repo me chala ke confirm karo.

**CI me common failures:** browser install bhoola, secret missing, headless me timing alag, environment data alag, tests parallel me ek doosre ka data badalte hain.

## 9.2 Flaky tests

**WHY dangerous:** team ka tests par trust khatam. "Re-run kar lo" culture bug chhupa deta hai.

| Cause | Example | Fix |
|---|---|---|
| Timing/race | Element aane se pehle assert | `expect` (retry), condition par wait |
| Shared data | Do tests ek hi user/order badalte hain | Har test ka apna data, cleanup |
| Order dependency | Test B tabhi pass hota hai jab A chala ho | Tests independent banao |
| Environment | Staging slow/down, third-party API | Mock ya stable test env |
| Unstable locator | Dynamic ID, text change | Role/test-id locator |
| Parallel collision | Do workers ek record par | Unique data per worker |
| Concurrency/hash order | Set/dict order par assert | Order-independent assert (sorted ya set compare) |

**Retries** (`pytest --reruns 2` plugin `pytest-rerunfailures` se) = **last resort**. Retry se test green dikhta hai par bug aur flakiness chhup jaati hai. Agar retry use karo to flaky tests ki list rakho aur fix karo.

**Interview answer: How do you handle flaky tests?**
- *Simple:* Find the root cause. Don't just retry.
- *Strong:* "First I check if it is reproducible and collect evidence: trace, screenshot, logs, network. Then I classify the cause: timing, shared data, test order, environment or an unstable locator. For timing I replace fixed sleeps with condition-based waits. For data I make tests independent with their own setup and cleanup. I use retries only as a temporary guard, and I track flaky tests until they're fixed, because retries can hide real bugs."
- *Keywords:* root cause, trace, independent tests, condition-based wait, quarantine.

## 9.3 Debugging: 7-step process

1. **Reproduce** (same input, same env).
2. **Traceback neeche se upar padho:** aakhri line = error, upar wali lines = call chain.
3. **Isolate:** sabse chhota failing example banao.
4. **Hypothesis** likho ("price me comma hai isliye float fail").
5. **Evidence se prove karo** (print/repr, breakpoint, logging, trace).
6. **Minimal fix.**
7. **Regression test** likho jo is bug ko dobara pakde.

**CODE: ek chhota debugging example**

```python
def parse_price(text: str) -> float:
    return float(text.replace("₹", ""))

parse_price("₹1,299")
# ValueError: could not convert string to float: '1,299'
```

- Traceback ki aakhri line batati hai: `'1,299'` string float nahi ban sakti.
- Hypothesis: comma hata nahi. Proof: `print(repr(text.replace("₹", "")))` → `'1,299'`.
- Fix + regression test:

```python
def parse_price(text: str) -> float:
    return float(text.replace("₹", "").replace(",", ""))

def test_parse_price_with_comma():
    assert parse_price("₹1,299") == 1299.0
```

**Tools:**

| Tool | Use |
|---|---|
| `print(repr(x))`, `type(x)` | Value aur hidden whitespace dekhna |
| `breakpoint()` | Us line par pdb me ruk jao (`n` next, `s` step into, `c` continue, `p var` print, `q` quit) |
| `pytest --pdb` | Fail hone par debugger |
| `pytest -x -s --tb=short` | Pehla failure, prints dikhao, chhota traceback |
| `logging` | Production-style diagnostic output |
| Playwright trace / `page.pause()` | UI failures |

## PRACTICE 9

1. Ek test CI me kabhi-kabhi fail hota hai, local me hamesha pass. 3 possible causes batao.
2. Upar ke workflow me `if: always()` hata do to kya nuksan?
3. Debugging ke 7 steps ko ek real failure par apply karo jo tumne kabhi dekha ho.

**Answer key:** (1) CI me slower machine/timing, environment/data alag, parallel collision ya headless difference. (2) Test fail hone par artifacts upload nahi honge, to failure ka evidence nahi milega.

---

# Part 10 — Selenium (Python me) aur Java/TypeScript Reading Bridge

**Ye part tumhari language strategy ka core hai** (Part 0.4). Maqsad: Selenium keyword ka jawab dena aur Java/TS code padh sakna, master karna nahi.

## 10.1 Selenium in Python

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    driver.get("http://localhost:3000/login")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("user")
    driver.find_element(By.ID, "password").send_keys("pass")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    wait.until(EC.url_contains("protected"))
    assert "Protected" in driver.find_element(By.TAG_NAME, "h1").text
finally:
    driver.quit()
```

**LINE-BY-LINE:**
- `webdriver.Chrome()` browser kholta hai. (Selenium 4.6+ me driver binary Selenium Manager khud sambhalta hai.)
- `By.ID`, `By.CSS_SELECTOR` = locator strategy. Playwright ke `get_by_role` jaisa user-facing locator Selenium me built-in nahi hai.
- `WebDriverWait(driver, 10).until(EC...)` = **explicit wait**: condition hone tak 10 sec tak poll karo. Selenium me waits **tumhari zimmedari** hain.
- `finally: driver.quit()` browser hamesha band ho.

**pytest fixture:**

```python
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()
```

**Selenium ki common mistakes:** implicit aur explicit waits mix karna, `time.sleep()`, fragile XPath, driver quit na karna.

## 10.2 Playwright vs Selenium (interview ka favourite)

| | Playwright | Selenium |
|---|---|---|
| Waiting | Built-in auto-wait + retrying `expect` | Explicit waits khud likhne padte hain |
| Debug tools | Trace viewer, Inspector built-in | Zyada tooling khud jodni padti hai |
| Languages | JS/TS, Python, Java, .NET | Java, Python, C#, JS, Ruby, etc. |
| Browsers | Chromium, Firefox, WebKit (bundled) | Real browsers + Grid ecosystem |
| Mobile native apps | Nahi (sirf emulation) | Appium ke saath |
| Maturity/legacy suites | Naya, tezi se badh raha | Bahut purane enterprise suites |

**Honest answer interview me:** "Dono tools kaam ke hain. Naye projects me Playwright ke built-in waits aur tracing se kam flaky suite banta hai. Purane enterprise suites aur mobile ke liye Selenium/Appium ka ecosystem bada hai. Concepts (locators, waits, POM) dono me same hain."

## 10.3 Python vs Java vs TypeScript: syntax ka mapping

| Concept | Python | Java | TypeScript |
|---|---|---|---|
| Variable | `x = 5` | `int x = 5;` | `let x: number = 5;` |
| String format | `f"Hi {name}"` | `"Hi " + name` | `` `Hi ${name}` `` |
| List | `[1, 2]` | `List<Integer> l = List.of(1, 2);` | `[1, 2]` |
| Dict/Map | `{"a": 1}` | `Map<String, Integer>` | `{ a: 1 }` |
| Function | `def f(a): ...` | `int f(int a) { ... }` | `function f(a: number) { ... }` |
| Loop | `for x in items:` | `for (String x : items) { }` | `for (const x of items) { }` |
| Null | `None` | `null` | `null` / `undefined` |
| Test | `def test_x():` | `@Test void x() { }` | `test('x', async ({ page }) => { })` |
| Assert | `assert a == b` | `assertEquals(b, a)` (JUnit: expected pehle) | `expect(a).toBe(b)` |
| Setup | `@pytest.fixture` | `@BeforeEach` | `test.beforeEach(...)` |
| Dependencies | `requirements.txt` | `pom.xml` (Maven) / `build.gradle` | `package.json` |

## 10.4 Same test, teen languages

**Python (Playwright):**
```python
def test_login(page):
    page.goto("/login")
    page.get_by_label("Username").fill("user")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url(re.compile(r".*/protected"))
```

**TypeScript (Playwright):**
```typescript
import { test, expect } from '@playwright/test';

test('login', async ({ page }) => {
  await page.goto('/login');
  await page.getByLabel('Username').fill('user');
  await page.getByRole('button', { name: 'Login' }).click();
  await expect(page).toHaveURL(/.*protected/);
});
```

**Java (Selenium + JUnit 5):**
```java
@Test
void loginWorks() {
    driver.get("http://localhost:3000/login");
    driver.findElement(By.id("username")).sendKeys("user");
    driver.findElement(By.cssSelector("button[type='submit']")).click();
    assertTrue(driver.getCurrentUrl().contains("protected"));
}
```

**Padhne ke rules (Python se aa rahe ho to):**
- **TypeScript:** har async call se pehle `await` lagta hai (Python Playwright sync API me nahi). `async`/`await` dikhe to "ye step wait karta hai" samjho. `camelCase` (`getByRole`) vs Python `snake_case` (`get_by_role`). `{ page }` = fixture destructuring (pytest ke `page` argument jaisa). `=>` arrow function = lambda jaisa.
- **Java:** har variable ka type likha hota hai, `;` aur `{ }` hote hain, sab kuch class ke andar. `@Test`, `@BeforeEach` annotations = pytest ke markers/fixtures ke cousins. `driver.findElement` = Selenium `find_element`.
- **Mockito (Minnesota course):** `when(x.call()).thenReturn(y)` = Python me `mock.call.return_value = y`. `verify(mock).call()` = `mock.call.assert_called_once()`. JaCoCo = coverage tool (Python me `pytest-cov`). Concepts same, syntax alag.

## 10.5 Interview me truthful lines

- **"Java/TypeScript aata hai?"** → "Mera primary language Python hai aur maine Python me pytest + Playwright framework banaya hai. Java/TypeScript code padh sakta hu aur Playwright ya Selenium ke concepts (locators, waits, POM, fixtures) language-independent hain. Production me Java nahi use kiya, par naya syntax seekhne me concepts ki wajah se time kam lagta hai."
- **"Selenium use kiya?"** → Agar practice ki hai: "Python me Selenium se login/checkout flows banaye, explicit waits aur POM ke saath." Agar nahi ki, to pehle Part 10.1 practice karo, phir bolo.
- **Kabhi mat bolo** ki aata hai jab nahi aata. Follow-up me pakde jaoge.

## PRACTICE 10

1. Part 10.1 ka login test Playwright me likho (bina dekhe).
2. Ye TypeScript line padho aur Python me likho: `await page.getByRole('button', { name: 'Save' }).click();`
3. Is Java line ka matlab batao: `assertEquals(200, response.statusCode());`

**Answer key:** (2) `page.get_by_role("button", name="Save").click()` (3) Assert karo ki response ka status code 200 hai (expected pehle, actual baad me).

---

# Part 11 — AI-assisted QA (chhota aur honest)

Tumhare Gen-AI notes me Copilot, Claude Code, MCP, Playwright agents, Ollama wale modules hain. Ye **tools badalte rehte hain**, isliye yahan sirf wo hai jo stable rehta hai.

## 11.1 AI kahan madad karta hai

- Requirement se test ideas nikalna (EP/BVA/negative cases).
- Boilerplate (POM skeleton, fixtures).
- Failure logs samajhna aur debugging hypotheses.
- Test plan ya bug report ka draft.

## 11.2 AI par bharosa kab nahi

- AI ko tumhare product ke hidden business rules nahi pata.
- AI aksar **weak assertions**, hard-coded data aur fixed sleeps likh deta hai.
- "Healer" jaisa tool test ko green kar sakta hai assertion kamzor karke ya test hata ke. **Green ≠ correct.** Product bug chhup sakta hai.

## 11.3 Review checklist (AI-generated test par)

| Check | Sawaal |
|---|---|
| Requirement | Kya ye test sach me requirement verify karta hai? |
| Assertions | Kya meaningful state check hui ya sirf "page khula"? |
| Locators | Role/label/test-id ya brittle CSS/XPath? |
| Waits | `sleep`/`wait_for_timeout` to nahi? |
| Data | Hard-coded ya shared data to nahi? |
| Isolation | Kya test akela chal sakta hai? |

## 11.4 Prompt template (test design ke liye)

```text
Role: Senior QA/SDET.
Context: <feature + requirement in 3-5 lines>
Task: Test scenarios banao using EP, BVA aur negative cases.
Constraints: Python + pytest + Playwright. Role/label locators prefer karo.
Output: Table (ID, scenario, technique, expected result). Assumptions alag likho.
```

Phir tum output ko Part 3 ke rules se review karte ho. AI draft deta hai, **decision tumhara hai.**

## 11.5 Playwright Test Agents (planner, generator, healer)

Official docs ke mutabiq Playwright Test Agents (planner/generator/healer) Playwright ke saath aate hain. Planner Markdown test plan banata hai, generator tests, aur healer failing tests ko repair karne ki koshish karta hai. Agent definitions ko Playwright update hone par dobara generate karna padta hai. Ye Playwright Test (JS/TS runner) ka feature hai. Python pytest ke liye official support ke baare me ek feature request open tha. **Current status official docs me check karo.** Isliye Python me ise "pakka workflow" mat maano. Tum AI tool (Copilot/Claude Code) + Playwright MCP se app explore karwa sakte ho aur code khud review karke likho.

**Rule:** Project 1 bina AI ke karo. Phir Project 2 AI-assisted. Warna tum AI ke output ko judge hi nahi kar paoge.

---

# Part 12 — Interview Bank (Python SDET, fresher/0–2 years)

Har answer: simple English → strong 1–2 min → keywords. **Pehle concept samjho, phir bolna practise karo.** Ratta mat maaro.

**Q1. What is the test pyramid?**
- *Simple:* Many fast unit tests, fewer API tests, fewest UI tests.
- *Strong:* "It's a guide for balancing test types. Unit and component tests are fast and stable so I'd have many. API and integration tests check behaviour between components, so a meaningful set. UI end-to-end tests are slow and fragile, so I keep them for critical user journeys. It's a guideline, not a fixed ratio."
- *Keywords:* speed, stability, cost, coverage at right level.

**Q2. Severity vs priority?**
- *Simple:* Severity is impact. Priority is urgency.
- *Strong:* "Severity measures how badly the defect affects the system. Priority is the order in which the business wants it fixed. They can differ: a crash in a rarely used admin page is high severity, low priority. A wrong legal disclaimer is low severity but high priority."
- *Keywords:* impact, urgency, business context, triage.

**Q3. Retesting vs regression?**
- *Simple:* Retesting confirms a fix. Regression checks nothing else broke.
- *Strong:* "After a bug fix, retesting re-runs the failed test to confirm the fix. Regression testing runs relevant existing tests to ensure the change did not break other areas. I automate stable regression checks and prioritise by risk."
- *Keywords:* confirmation, side effects, risk-based, automation.

**Q4. What should you automate, and what not?**
- *Simple:* Automate stable, repeated, high-value checks. Don't automate unstable or one-off things.
- *Strong:* "I automate stable, repeatable, business-critical flows, especially at API level where it's faster and more reliable. I avoid automating unstable requirements, one-off checks, and subjective usability judgement. I also ask whether a scenario is better covered at unit or API level than through slow UI tests."
- *Keywords:* ROI, maintenance cost, pyramid, stability.

**Q5. What is a pytest fixture? What are scopes?**
- *Simple:* A reusable setup and teardown helper.
- *Strong:* "A fixture provides test dependencies like data, a browser or a config. Code before `yield` is setup, after is teardown. Scope controls lifetime: function by default, then class, module, package and session. Smaller scope gives better isolation, bigger scope is faster but risks shared state. Shared fixtures live in `conftest.py`."
- *Keywords:* setup/teardown, yield, scope, conftest, isolation.

**Q6. What is auto-waiting in Playwright?**
- *Simple:* Playwright waits for an element to be ready before acting.
- *Strong:* "Before actions like click, Playwright checks actionability: visible, stable, enabled and able to receive events. This removes many timing-related failures. But it doesn't know my app's business conditions, so I still assert the expected state with `expect`, which retries until the condition is met or times out."
- *Keywords:* actionability, web-first assertions, no fixed sleeps.

**Q7. Why Page Object Model?**
- *Simple:* It keeps locators and page actions in one place.
- *Strong:* "POM encapsulates a page's locators and actions so tests read like user intent and a UI change needs a fix in one place. I keep assertions in the tests and avoid giant page classes that contain whole business workflows."
- *Keywords:* maintainability, reuse, separation, single place of change.

**Q8. Browser vs BrowserContext vs Page?**
- *Simple:* Browser is the process, context is an isolated profile, page is a tab.
- *Strong:* "A context has its own cookies and storage, so two contexts behave like two separate users. I create a new context per test for isolation, and load saved `storage_state` to skip repeated logins."
- *Keywords:* isolation, storage_state, parallel safety.

**Q9. PUT vs PATCH?**
- *Simple:* PUT replaces the resource. PATCH updates part of it.
- *Strong:* "PUT sends the full representation and is idempotent. PATCH sends only changed fields. In API tests I check that omitted fields are handled correctly in each case, and that repeating the same PUT gives the same result."
- *Keywords:* idempotent, partial update, full replace.

**Q10. INNER JOIN vs LEFT JOIN?**
- *Simple:* INNER returns only matches. LEFT returns all left rows plus matches.
- *Strong:* "INNER JOIN returns rows with matches in both tables. LEFT JOIN keeps every row from the left table and fills unmatched right-side columns with NULL. I use LEFT JOIN with `WHERE right.id IS NULL` to find missing data, for example orders without payments."
- *Keywords:* NULL, missing records, data validation.

**Q11. Playwright vs Selenium?** → Part 10.2 ka answer.

**Q12. Explain your automation framework.** (Template, 3–5 min)
1. Language aur runner: Python, pytest, Playwright.
2. Structure: `pages/`, `tests/ui`, `tests/api`, `conftest.py`, config.
3. Fixtures: auth via storage_state, per-test context, test data setup/cleanup.
4. Design choices (aur kyun): role locators, POM, assertions in tests.
5. API + SQL checks for backend validation.
6. CI: GitHub Actions on push/PR, artifacts (trace, screenshots).
7. Reliability: koi flaky test mila to root cause kaise nikala.
8. Limitations: kya automate nahi kiya aur kyun.

**Q13. "Java/TypeScript aata hai?"** → Part 10.5.

**Q14. "Aapke paas job experience nahi hai, hum kyun hire karein?"**
- *Strong (honest):* "I don't have formal QA employment, so I built evidence instead. I have a test design package, bug reports with evidence, API and SQL checks, and a Playwright + pytest framework running in CI with traces on failure. I can clone the repo, show a real failure, explain the root cause and justify what I chose not to automate. I'd be happy to walk through it."
- *Keywords:* evidence, project, root cause, honesty.
- **Project ko job experience ki tarah mat bolo.** Sach bolo: independent project.

---

# Part 13 — Study Plan, Proof of Work aur Mistake Tracker

## 13.1 Phases (har phase ka output pura karne ke baad hi aage)

| Phase | Parts | Output (proof) |
|---|---|---|
| 1. Test thinking | 1–5 | 30 test cases (EP/BVA/decision table/state), 5 bug reports with evidence |
| 2. pytest + API + SQL | 6, 8 | 15 API tests (positive/negative/auth), 10 SQL queries, mock example |
| 3. Playwright framework | 7 | POM login + 3 flows, storage_state fixture, trace on failure |
| 4. CI + reliability | 9 | Green GitHub Actions run, artifacts, ek flaky/failure ka root-cause note |
| 5. Language bridge | 10 | Selenium-Python mini test, Java/TS snippets reading practice |
| 6. Projects + interviews | 11, 12 | Project 1 (bina AI), Project 2 (AI-assisted), mock interviews |

Time-estimate tum apne schedule se rakho. Rule simple hai: output nahi to phase complete nahi.

## 13.2 Proof-of-work repository (portfolio)

```text
qa-sdet-portfolio/
├── README.md              # overview, stack, setup, how to run, known limitations
├── requirements/          # user stories + ambiguity log
├── strategy/              # qa_strategy.md, risk matrix, RTM
├── test-design/           # scenarios, test cases, EP/BVA, decision tables
├── defects/               # bug reports with evidence
├── api_tests/             # pytest + requests
├── sql/                   # validation queries
├── ui_tests/              # Playwright + POM
├── conftest.py
├── pytest.ini
└── .github/workflows/tests.yml
```

**"Project-ready" ki definition:** koi bhi repo clone karke tests chala sake, tum architecture samjha sako, ek real failure dikha ke diagnose kar sako, aur bata sako kya automate **nahi** kiya aur kyun.

## 13.3 Job targeting (Python-first)

1. 15–20 JDs collect karo (NCR + remote).
2. Har JD me mark karo: Python / Java / TypeScript / "any" / Selenium / Playwright / API / SQL / CI.
3. Dekho kitni JDs Python allow karti hain. Wahi tumhara real target pool hai.
4. Bar-bar aane wale gaps (jaise Docker, Jenkins) ko next learning list me daalo.

## 13.4 Mistake tracker (repeat mistakes pakadne ke liye)

| Date | Topic | Galti | Kyun hui | Sahi tareeka | Dobara hui? |
|---|---|---|---|---|---|
| | | | | | |

Har practice ke baad 1–2 line bharo. Jo galti 3 baar aaye wo weakness hai, uspar alag drill banao.

## 13.5 Final honest note

- Is guide se tum **concepts aur structure** pakad sakte ho. Job-readiness proof se aati hai: tests, repo, CI run, aur bolne ki practice.
- Python-first strategy realistic hai, par job pool chhota ho sakta hai. Isliye JD analysis (13.3) aur Part 10 ka bridge important hain.
- Jo cheezein original notes me kam thi aur yahan bhi thin hain: **SQL depth, Docker/Jenkins, performance testing, security basics.** Inhe baad me alag se add karo jab JD me baar-baar dikhein.

---

**Original notes ka quick map (depth chahiye to):**

| Topic | File |
|---|---|
| Foundations (QA/QC, principles, layers, static/dynamic) | `Software_Testing_Fundamentals.../module_3/...Modules_1_to_3_Study_Guide.md` |
| Test types, STLC | `.../module_4/Module_04_Test_Types_and_STLC_Study_Guide.md` |
| Agile, Scrum, Sprint | `.../module_7`, `module_8`, `module_9`, `module_10` |
| Test design (worked examples) | `Launching_Your_QA_Career/Test_Case_Design_Masterbook_Hinglish_2_Year_SDET.md` |
| Resume + GitHub + behavioural | `Launching_Your_QA_Career/Launching_Your_QA_Career_Complete_Study_Guide.md` |
| Interview Q&A (65 questions) | `.../misc/QA_Automation_SDET_Interview_Cheat_Sheet_2026.md` |
| Gap analysis | `.../misc/QA_SDET_Bridge_Course_Missing_Topics_and_Next_Roadmap.md` |
| Test doubles, flaky (concept) | `Introduction to Software Testing.../module_4/...` (Java syntax skip) |
| Playwright + AI tools | `Gen-AI.../module_2,3,5,7,8,10` |
| Debugging | `Gen-AI.../debugging/*` |
| Projects | `Gen-AI.../project/Project_01...` (bina AI), `Project_02...` (AI-assisted) |

*(Folder numbering original zip me inconsistent hai. Gen-AI folder `module_N` ke andar headings me alag number hain. File names se pehchano, heading se nahi.)*
