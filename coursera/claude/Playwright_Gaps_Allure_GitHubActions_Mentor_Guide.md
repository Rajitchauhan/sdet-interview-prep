# Playwright Gap Review + Allure + GitHub Actions: Mentor Guide

**Beginner-friendly, step-by-step | Hinglish | Python + pytest + Playwright**
Tumhari repo `Rajitchauhan/sdet-interview-prep` (branch `master`, folder `playwright/ex_1` se `ex_6`) ko padh ke ye guide banayi gayi hai.

---

# Part 0: Pehle ye padho

## 0.1 Is guide me kya hai

| Part | Kya milega |
|---|---|
| **A** | Tumhare Playwright code ka strict review: kya sahi, kya galat, gap list |
| **B** | Reporting aur CI ke basic concepts (zero se) |
| **C** | Project ko "CI-ready" banana (config files, structure) |
| **D** | **Allure Report**: step by step (6 chunks) |
| **E** | **GitHub Actions CI/CD**: step by step (8 chunks) |
| **F** | Sab jod ke capstone, interview answers, confidence checklist |

## 0.2 Har chunk ka format

Har bade topic ko chhote chunks me toda hai. Har chunk me:

`WHY` → `WHAT` → `HOW` → `CODE` → `LINE-BY-LINE` → `KYUN YE CHOICE?` → `AS A STUDENT` → `AS AN SDET` → `COMMON MISTAKES` → `PRACTICE`

- **KYUN YE CHOICE?** = Python/tools me jab kai options hain, to humne ye wala kyun chuna (aur baaki kyun nahi).
- **AS A STUDENT** = seekhte waqt tumhe kaise sochna hai.
- **AS AN SDET** = job me ek engineer ki tarah cheez ko kaise dekhna hai.

## 0.3 Kya verify hua, kya nahi (honest table)

| Cheez | Status |
|---|---|
| Tumhari repo ke findings (ImportError, URL error, test collection, `goto` missing) | **Maine code run karke verify kiya** |
| Allure 3 CLI (`generate`, `open`, history, config file) | **Real CLI se chalaya** (v3.22.1) |
| `allure-pytest` results: labels, steps, parametrize titles, attachments | **Chalaya** |
| Failure par screenshot attach karne wala hook | **Chalaya** (nakli `page` object ke saath) |
| Parallel (`-n`) + retries (`--reruns`) ke saath Allure | **Chalaya** |
| 5 GitHub Actions workflows ki YAML | **`actionlint` se lint kiya, pass** |
| Action versions (checkout, setup-python...) | Official repos ke **tags se** nikale |
| Real browser me Playwright tests | **Nahi chala paya** (is environment me browser download nahi hota) |
| SauceDemo ka actual behaviour | **Nahi dekha** (site yahan se accessible nahi). Jahan shak hai wahan "tum run karke confirm karo" likha hai |
| GitHub par real workflow run / Pages deploy | **Nahi** (mere paas tumhara GitHub account nahi hai). Tum chalaoge to wahi final proof hoga |

**Rule:** jo "run karke confirm karo" likha hai, usse tum khud chala ke dekho. Wahi tumhari practice hai.

---

# Part A: Tumhari Repo ka Strict Review

## A.1 Overall verdict

**PASS WITH CORRECTIONS** (concept level) aur **NEEDS REWORK** (execution level).

Seedhi baat: tumhe locator scoping aur POM ka design sochna aata hai. Par tumhara code kai jagah **chalta hi nahi** (commit se pehle run nahi hua). Interview me "maine Playwright framework banaya" bolne ke liye code ka **green run** chahiye. Wo abhi nahi hai.

Exercise-wise:

| Exercise | Verdict | Ek line me kyun |
|---|---|---|
| ex_1 | NEEDS REWORK | Import galat hai, test collect hi nahi hota |
| ex_2 | NEEDS REWORK | Fictional DOM par likha, real site par pass nahi ho sakta |
| ex_3 | NEEDS REWORK | URL galat, fake site, design idea sahi |
| ex_4 | PASS WITH CORRECTIONS | Fixture + scoping sahi, duplication aur locator risk |
| ex_5 | PASS WITH CORRECTIONS | Sorting check sahi approach, cleanup chahiye |
| ex_6 | NEEDS REWORK | Architecture achha, par `goto` missing aur apni hi DoD adhoori |

## A.2 Skill levels (multidimensional, reasons ke saath)

| Area | Level | Reason |
|---|---|---|
| Locator scoping (`filter`, chaining) | Early-intermediate | Har exercise me product card ke andar scoped locator. Ye sahi pattern hai |
| Assertions | Beginner+ | `expect` sahi use kiya, par ex_1 me galat cheez assert ki |
| Fixtures / conftest | Beginner+ | Auth fixture hai, par 3 jagah copy-paste |
| POM design | Early-intermediate | Page methods agla page object return karte hain (achha). `open()` missing |
| **Run-and-verify discipline** | **Beginner (weakest)** | 3 exercises chalte hi nahi |
| pytest features (parametrize, markers, config) | Beginner | Ek bhi `parametrize`/marker nahi, `pytest.ini` khali |
| API + UI hybrid | Beginner | Idea sahi, code unrunnable |
| Reporting / CI | Zero | Koi workflow, Allure ya report nahi |
| Repo hygiene | Beginner | `.pyc`, `state.json` commit, README khali |

## A.3 Jo sahi hai (credit evidence ke saath)

1. **Scoped locators:** `page.locator(".inventory_item").filter(has_text=name).get_by_role("button", ...)`. Ye "sahi product ka sahi button" wali problem ko theek solve karta hai (ex_2, 4, 5, 6).
2. **POM me responsibility split:** ex_6 me page objects locators/actions dete hain aur `expect` tests me hai. Ye sahi rule hai.
3. **Fluent navigation:** `inventory_page.go_to_cart()` return karta hai `CartPage`. Achha design.
4. **Sorting ka double check (ex_5):** dropdown value **aur** actual numeric order dono check kiye. Sirf dropdown dekhna galat hota.
5. **`time.sleep()` kahin nahi.** Auto-wait par bharosa. Sahi.
6. **Exercise specs khud likhi** constraints ke saath. Ye achhi habit hai.
7. **ex_3 ka idea:** API se data banao, UI se verify karo. Ye industry pattern hai.
8. ex_4/ex_5 ke `.pyc` files batate hain ki tumne unhe local me chalaya (Python 3.15, pytest 9.1.1). Ye credit hai, par ye "pass hua" ka proof nahi hai.

## A.4 Jo galat hai: Tumne ye kiya / Karna chahiye tha / Why

Priority: **P0** = pehle fix, **P1** = important, **P2** = baad me.

### G1 [P0] ex_6: site kabhi open hi nahi hoti
- **Tumne ye kiya:** `conftest.py` me `auth_page` fixture seedha `LoginPage(page).login(...)` call karta hai. `LoginPage` me `goto`/`open()` nahi hai. Poore `ex_6` me `goto` shabd kahin nahi (maine `grep` se check kiya).
- **Karna chahiye tha:** login se pehle site open honi chahiye.
- **Why:** pytest-playwright ka `page` fixture ek **khali tab** se shuru hota hai. Locator lazy hota hai, to `get_by_placeholder("Username").fill(...)` 30 sec wait karke timeout dega. (Ye mera code padh ke nikala hua nishkarsh hai. Browser me chalake tum confirm karo.)
- **Direction:** page object ko "kholne" ka tareeka do, aur URL ko config se lo (Part C).

### G2 [P0] ex_1: test collect hi nahi hota (verified)
- **Tumne ye kiya:** `from playwright import Page, expect`
- **Chalane par:** `ImportError: cannot import name 'Page' from 'playwright'`
- **Sahi:** `from playwright.sync_api import Page, expect`
- **Aur do galtiyan:** (a) `page.goto(...)` nahi hai. (b) Aakhri assertion `expect(product_card).to_have_count(1)` **product card ki ginti** check karta hai. Requirement thi "**cart count** 1 ho gaya".
- **Principle:** test wahi assert kare jo requirement kehti hai. Paas wali koi aasan cheez assert karoge to test green ho sakta hai jabki requirement verify hi nahi hui. Isse jhoota confidence milta hai.

### G3 [P0] ex_3: API call chal hi nahi sakti (verified)
- **Tumne ye kiya:** `url = "api/orders"` aur `requests.post(url, ...)`.
- **Chalane par:** `MissingSchema: Invalid URL 'api/orders': No scheme supplied`
- **Aur issues:**
  - Saari pages `example.com` par hain, jo real app nahi hai.
  - Fixture ke andar `assert response.status_code == 201`. Setup fail hone par report me "test fail" ki jagah "setup error" dikhta hai (ye theek bhi ho sakta hai, par jaan-boojh ke socho).
  - `expect(page.get_by_text("2"))`: "2" page par kai jagah ho sakta hai. Kamzor assertion.
  - Order ke baad cleanup nahi.
  - `test_navigate_to_orders` bina login seedha dashboard khol raha hai.
- **Karna chahiye tha:** ek real, chalta hua target (API + UI) chuno, base URL config me rakho, aur assertions ko scope karo.
- **Credit:** design idea (API setup, UI validate) sahi hai.

### G4 [P1] ex_2: fictional DOM par exercise
- **Tumne ye kiya:** `saucedemo.com` ka URL, par spec ka login "Email/Password" label aur "Dashboard" heading wala fictional HTML.
- **Mismatch:** spec me price class `.price` hai, tumhare code me `.product-price`.
- **Why dikkat:** ye test real site par pass nahi ho sakta. "Likh diya" aur "chal gaya" me fark hai.
- **Direction:** fictional-DOM exercises ko ya to SauceDemo par re-map karo, ya `_archive/` folder me daalo.

### G5 [P1] Copy-paste ki jagah sharing
- **Tumne ye kiya:** `auth_page` fixture ex_4, ex_5, ex_6 me alag-alag likha. `test_add_product_to_cart` aur `test_product_details` ex_4 aur ex_5 me copy hain. Comment-out code files me pada hai. `print(...)` test me.
- **Karna chahiye tha:** shared cheez `conftest.py` me, ek jagah. Commented code git history me rehta hai, file me nahi.
- **Why:** login UI badla to 3 jagah fix. Aur reviewer ko lagta hai "ye cleanup nahi karta".

### G6 [P1] Locator inconsistency (shak: run karke confirm karo)
- ex_4/ex_5: `get_by_role("link", name="Shopping Cart")`. ex_6: `.shopping_cart_link` (CSS). **Dono me se ek tareeka kaam nahi karta hoga, isiliye shayad tumne ex_6 me badla.**
- ex_4/5: `get_by_role("link", name="Sauce Labs Backpack")`. Mujhe shak hai ki SauceDemo par image-link aur title-link dono ka accessible naam same ho sakta hai. Aisa hua to Playwright **strict mode violation** dega (ek se zyada element match).
- **Karna chahiye tha:** jis exercise me locator toota, wahan seekha hua principle likho ("is site me cart link ka accessible naam nahi hai, isliye CSS/test-id") aur sab jagah ek policy rakho.
- **Direction:** Playwright me `get_by_test_id` ka attribute badla ja sakta hai (SauceDemo `data-test` use karta hai). Ye P2 topic hai.

### G7 [P1] ex_5: sorting check ka sync point
- `select_option(...)` ke turant baad `all_text_contents()` ek baar padh ke raw `assert`. Raw `assert` retry nahi karta.
- **Principle:** pehle ek **sync point** (jaise sabse sasta item pehle position par dikhe, `expect` se), phir list padho. Ye race-condition se bachata hai.

### G8 [P0] ex_6 ki apni Definition of Done adhoori hai
Tumhari `ex_6.md` me 20-item DoD hai. Code me:
- **Sorting (Req 3):** ek bhi test me sorting nahi.
- **Parametrize (Req 7):** `parametrize` kahin nahi.
- **Checkout completion (Req 5):** `test_user_can_complete_checkout` `# Overview validations...` par ruk jaata hai. `get_checkout_complete_message()` define hai par kabhi use nahi hua.
- Postal code `"263..."` (placeholder, spec me `282001` tha).
- `test_inventory_page` aur `test_authenticated_user_can_access_inventory` ke assertions overlap.
- Unused imports (`expect`, `LoginPage`, `CartPage`) kai files me.

**Principle:** "Mostly done" ko "done" mat bolo. DoD ke har box ko evidence se tick karo.

### G9 [P0] Repo hygiene
- `pytest.ini` aur `README.md` **khali** hain.
- `requirements.txt` nahi. Koi dusra insaan (ya CI) setup nahi kar sakta.
- `.gitignore` nahi, to commit me `__pycache__/*.pyc` aur `ex_4/state.json` chale gaye. `state.json` me session cookie hota hai. Yahan demo site hai, par **ye aadat khatarnak hai**.
- URL `https://www.saucedemo.com/inventory.html` kai jagah hard-coded. `base_url` config nahi.
- `state.json` bana par use nahi hua (`storage_state` adhoora).

### G10 [P0] CI ke liye repo ready nahi
- `.github/workflows/` hai hi nahi.
- `git/ci-cd-practice` ek **broken submodule pointer** hai. (`git ls-tree` me mode `160000`, aur `.gitmodules` file nahi.) Ye tab banta hai jab ek git repo ke andar dusri git repo `git add` kar do. GitHub par ye khali/click-na-hone-wala folder dikhta hai.
- Default branch `main` hai jisme sirf `README.md` hai. Tumhara saara kaam `master` branch me hai. **GitHub Actions ke `schedule` aur manual run (`workflow_dispatch`) default branch par hi dikhte/chalte hain.** Isliye branch strategy theek karni hogi (Part E).

### G11 [P2] Repo me course-notes public hain
`coursera/` folder me Coursera course se bane tumhare notes public repo me hain. Course content ke terms alag hote hain. Safe side: repo ko ya to private rakho ya wo folder public repo se hata do. (Ye legal advice nahi hai, bas risk flag hai.)

## A.5 Repeated mistakes (patterns)

| # | Pattern | Evidence |
|---|---|---|
| M1 | **Run kiye bina commit** | ex_1 import, ex_3 URL, ex_6 `goto` |
| M2 | **Requirement ki jagah paas wali cheez assert** | ex_1 card count, ex_2 selector mismatch |
| M3 | **Share karne ki jagah copy-paste** | `auth_page` 3 baar, tests 2 baar |
| M4 | **Adhoora kaam placeholder ke saath commit** | `"263..."`, `# Overview validations...` |
| M5 | **Hygiene ignore** | `.pyc`, `state.json`, khali README/ini |

M1 sabse badi weakness hai. **Ek rule banao: "Jo test maine green nahi dekha, wo commit nahi hoga."**

## A.6 Gap checklist (kya aana baaki hai)

| Priority | Gap | Is guide me |
|---|---|---|
| P0 | Har exercise real site par **green run** | Fix Lab |
| P0 | `pytest.ini` (`base_url`, markers, `addopts`), `requirements.txt`, `.gitignore` | Part C |
| P0 | `parametrize` ka sahi use | Fix Lab FL-2 |
| P0 | Failure evidence (screenshot, trace) | Part C, D |
| P0 | **Allure report** | Part D |
| P0 | **GitHub Actions CI** | Part E |
| P1 | `storage_state` poora implement (file bani par unused) | Part F |
| P1 | Real API testing (requests) ek chalte target par | Fix Lab FL-3 |
| P1 | Network: `expect_response`, `route` (mocking) | Part 7 of previous guide |
| P1 | Parallel run (`pytest-xdist`), retries ka sahi use | Part E |
| P2 | Frames, dialogs, popups/new tab, upload/download | Baad me |
| P2 | Custom test-id attribute, accessibility, mobile emulation | Baad me |

## A.7 Fix Labs (khud re-implement karo)

Mai yahan **solution nahi de raha**. Har lab ke end me acceptance check hai. Tum code likho, chalao, phir mujhe bhejo to strict review karenge.

**FL-1: "Green run" rule (P0)**
Task: `ex_4`, `ex_5` ko local me chalao. Jo fail ho, uska reason likho (1 line) aur fix karo.
Accept when: `pytest -v` me sab pass, aur tumhare paas har fix ka "kya toota tha / kyun" note hai.

**FL-2: ex_6 ko sach me complete karo (P0)**
Task: (a) site open hone ka tareeka add karo. (b) Sorting test (dropdown + numeric order). (c) `parametrize` ek jagah jahan sach me kaam aaye. (d) Checkout ko final "order complete" tak assert karo. (e) Unused imports aur placeholder hatao.
Accept when: ex_6 ke DoD ke saare boxes ke samne evidence (test ka naam) likha hai.

**FL-3: Real API + UI hybrid (P1)**
Task: ex_3 ko ek **chalte hue** target par banao. Koi public practice API/app chuno (availability khud check karo). Base URL config me. Setup API se, validate UI se, cleanup karo.
Accept when: test local me green, bina hard-coded URL.

**FL-4: Fictional exercises (P1)**
Task: ex_1 aur ex_2 ko SauceDemo par re-map karo ya `_archive/` me daalo.
Accept when: koi bhi aisa test repo me nahi jo kabhi pass nahi ho sakta.

**FL-5: Hygiene (P0)**
Task: `.gitignore` banao, `git rm --cached` se `.pyc`/`state.json` hatao, README me "kaise chalayein" likho.
Accept when: naye folder me clone karke README follow karke tests chal jayein.

**FL-6: Broken submodule cleanup (P1)**
Task: `git/ci-cd-practice` pointer hatao (commands Part E me hain).
Accept when: GitHub par wo broken entry nahi dikhti.


---

# Part B: Reporting aur CI ke Concepts (zero se)

## Pehle terms (har term define)

| Term | Matlab |
|---|---|
| **Test report** | Test run ka result jo insaan padh sake: kitne pass/fail, kyun fail hue |
| **Artifact** | Run ke baad bachne wali files (screenshot, trace, report) |
| **CI (Continuous Integration)** | Code push hote hi machine **apne aap** build + tests chalaye |
| **CD (Continuous Delivery/Deployment)** | Tested code ko release/deploy tak le jana. **Delivery** = deploy ke liye ready, button insaan dabata hai. **Deployment** = bina insaan ke apne aap deploy |
| **Pipeline / Workflow** | CI ke steps ka sequence |
| **Runner** | Wo machine jahan pipeline chalti hai |
| **Exit code** | Command khatam hone par ek number. `0` = success, non-zero = fail. CI isi se jaanta hai step fail hua |

## B.1 Test result dikhane ke 4 tareeke

| Tareeka | Kya hai | Kab useful |
|---|---|---|
| Console output | Terminal me `PASSED/FAILED` | Developer local me |
| **JUnit XML** (`--junitxml=r.xml`) | Machine-readable file | CI tools (Jenkins/GitHub) result parse karne ke liye |
| HTML plugin (`pytest-html`) | Ek simple HTML page | Chhota project, quick share |
| **Allure** | Rich report: steps, screenshots, history, graphs | Team/manager/dev ko dikhana |

**KYUN YE CHOICE? (Allure)**
- Console aur XML insaan ke liye padhna mushkil. HTML plugin simple hai par steps/attachments/history kamzor.
- Allure me **steps, attachments (screenshot/API response), severity labels, parametrize, history** milte hain. Aur Allure industry me bahut common hai, isliye interview me puchha jata hai.
- Trade-off: Allure ko ek extra tool (CLI) install karna padta hai.

**AS A STUDENT:** report ko "decoration" mat samjho. Sochna: *"Agar mai kal wahan na hu, to kya dusra insaan sirf report dekh ke samajh jayega ki kya toota?"*

**AS AN SDET:** report tumhara **product** hai. Manager code nahi padhta, report padhta hai. Failure me evidence (screenshot, response, trace) na ho to developer tumhe bolega "reproduce karke dikhao".

## B.2 CI ka mental model: "saaf machine par chalao"

- Tumhare laptop par Python, packages, browser, saved login sab pehle se hai. Isliye "meri machine par chalta hai".
- CI ek **bilkul saaf machine** deta hai. Wahan sab kuch **kod se** install hona chahiye (packages, browser).
- Isliye `requirements.txt`, `pytest.ini`, aur config **zaroori** hain. Agar tumhara project sirf tumhare laptop par chal sakta hai, to wo CI-ready nahi hai.

**AS AN SDET:** CI failure ka sabse bada hissa "test ki galti" nahi, **environment ki** hoti hai (missing browser, galat path, alag timezone, secret nahi mila).

## B.3 Exit code ek baar dekh lo (hands-on)

```bash
pytest -q                 # kuch test fail karo, phir:
echo $?                   # Linux/Mac: 1 (non-zero)
# Windows PowerShell:  echo $LASTEXITCODE
```

CI me jab `pytest` non-zero deta hai, wo step **fail** ho jaata hai aur pipeline red. Yahi mechanism tests ko "gate" banata hai.

## PRACTICE B

1. CI aur CD me ek line me fark batao.
2. "Meri machine par chalta hai, CI par nahi" ke 3 reasons likho.
3. Ek failing aur ek passing test banake `echo $?` dono ka output dekho.

**Answer key:** (1) CI = code merge hote hi build/test automatically. CD = tested code ko release/deploy karna. (2) CI me browser install nahi, dependency pin nahi, hard-coded local path/credentials. (3) Fail par non-zero (aksar 1), pass par 0.

---

# Part C: Project ko "CI-ready" banana

**Goal:** ek aisa folder jo koi bhi (ya GitHub ki machine) clone karke bina tumhari madad ke chala sake.

## C.1 Target structure (`playwright/ex_6`)

```text
playwright/ex_6/
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   └── test_checkout_workflow.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── allurerc.json
└── README.md
```

Repo ke **root** par:

```text
.gitignore
.github/workflows/...      # Part E
```

> **Note:** `.github/workflows` hamesha **repo root** par hota hai, `playwright/ex_6` ke andar nahi. Tumhara project ek subfolder me hai, isliye workflow me `working-directory` use karenge (Part E).

## C.2 `requirements.txt`: kya, kyun, kaise

**WHY:** CI ki saaf machine ko pata hona chahiye kaunsa package kaunsa version.

```text
pytest==9.2.0
pytest-playwright==0.10.0
allure-pytest==2.16.2
pytest-xdist==3.8.0
pytest-rerunfailures==16.7
```

**Ye versions maine yahan install karke check kiye** (resolve hote hain). Tum apne machine ke versions se banao:

```bash
pip freeze | grep -i -E "pytest|playwright|allure"
```

Output me jo versions dikhein unhe `==` ke saath file me daalo.

**LINE-BY-LINE:**
- `pytest-playwright` = `page`, `browser` fixtures aur CLI options deta hai. Ye `playwright` package khud kheench leta hai.
- `allure-pytest` = pytest me `--alluredir` aur `allure.*` functions.
- `pytest-xdist` = parallel run (`-n`).
- `pytest-rerunfailures` = `--reruns N` (sirf last resort, Part E).

**KYUN YE CHOICE?** `requirements.txt` vs `poetry`/`pyproject.toml`: beginner ke liye `requirements.txt` sabse simple aur har CI me `pip install -r` se chalta hai. Poetry baad me seekh sakte ho, abhi zaroorat nahi.

**COMMON MISTAKE:** version pin na karna. Kal naya version aaya aur CI toot gaya, jabki tumne kuch nahi badla.

## C.3 `pytest.ini`

```ini
[pytest]
base_url = https://www.saucedemo.com
testpaths = tests
addopts =
    -ra
    --tracing retain-on-failure
    --screenshot only-on-failure
    --video retain-on-failure
markers =
    smoke: quick critical checks
    regression: full regression suite
```

**LINE-BY-LINE:**
- `base_url`: ab test me `page.goto("/")` likhne se site khulti hai. URL ek jagah, kal change ho to ek line badlo. Command line se override: `pytest --base-url https://staging.example.com`.
- `testpaths = tests`: bina argument ke `pytest` sirf `tests/` me dhundhe.
- `addopts`: har run me ye options **automatically** lag jaate hain.
  - `-ra`: end me failed/skipped ka summary.
  - `--tracing retain-on-failure`: har test ka trace record hota hai, par **sirf fail hone par** file bachti hai.
  - `--screenshot only-on-failure`, `--video retain-on-failure`: failure ka evidence.
- `markers`: test par label (`@pytest.mark.smoke`). Register karna zaroori, warna typo chup-chap ignore ho sakta hai. Chalane ke liye: `pytest -m smoke`.

**KYUN YE CHOICE?** `pytest.ini` vs `pyproject.toml`/`tox.ini`: pytest sab padhta hai. `pytest.ini` sabse seedha aur is file me sirf pytest config hota hai, beginner confuse nahi hota.

**AS A STUDENT:** pehle `pytest --tracing retain-on-failure` command line se chalake dekho, phir use `addopts` me daalo. Seekhne ka tareeka: cheez pehle haath se, phir config me.

**AS AN SDET:** `addopts` me jo daaloge wo har developer aur CI par lagega. Isliye wahi daalo jo **hamesha** chahiye. Kabhi-kabhi wale options (jaise `--headed`) command line par rakho.

**Note:** pytest-playwright ke saath pytest 9.x me ek deprecation warning aa sakti hai (`base_url fixture ... session-scoped`). Ye plugin ki apni warning hai, tumhari galti nahi.

## C.4 `.gitignore` (repo root)

```text
__pycache__/
*.pyc
.pytest_cache/
.venv/
venv/
test-results/
allure-results/
allure-report/
history.jsonl
state.json
playwright/.auth/
.env
node_modules/
```

**WHY:** ye sab **generated** ya **secret** files hain. Repo me sirf wo cheez jaaye jo tum likhte ho.

**Already commit ho chuki files hatane ke liye** (file disk par rahegi, git se hategi):

```bash
git rm --cached -r playwright/ex_4/__pycache__ playwright/ex_5/__pycache__
git rm --cached playwright/ex_4/state.json
git add .gitignore
git commit -m "chore: add .gitignore, untrack generated files"
```

**COMMON MISTAKE:** `.gitignore` baad me banana aur sochna ki purani file apne aap hat jayegi. Nahi hatti, `git rm --cached` chahiye.

## C.5 `conftest.py`: failure evidence hook (Allure se pehle seekho)

Abhi tak tum `conftest.py` me sirf fixture rakhte the. Ab ek **hook** seekhte hain: pytest ke andar ek jagah jahan hum apna code "jod" sakte hain.

Part D me Allure ke saath ye hook screenshot attach karega. Pehle concept samjho:

```python
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        print("FAILED TEST HAD PAGE:", page is not None)
```

**LINE-BY-LINE:**
- **Hook** = pytest ka predefined function naam. `pytest_runtest_makereport` har test ke har phase ke result banate waqt call hota hai.
- Test ke 3 phase: `setup` → `call` (asli test) → `teardown`. `report.when` batata hai kaunsa phase.
- `hookwrapper=True` + `yield`: pytest asli kaam kare, phir hum result dekh sakein.
- `outcome.get_result()`: us phase ka report object.
- `report.failed`: wo phase fail hua.
- `item.funcargs`: us test ko mile saare fixtures ka dict. `page` fixture yahin se milta hai, **chahe test ne `page` direct maanga ho ya `auth_page` ke through**.

**KYUN YE CHOICE?** Is kaam ke kai tareeke hain:
| Tareeka | Fark |
|---|---|
| `try/except` har test me screenshot lena | Har test me repeat. Bhool jaoge |
| `pytest_runtest_makereport` hook (humne chuna) | Ek jagah, har test par apne aap, fail hone par hi chalta hai |
| Allure ki official guide ka `pytest_runtest_teardown` hook | Wo pytest-playwright ke **save kiye hue** screenshot file ko dhundh ke attach karta hai. Ye bhi valid hai, par ek aur layer (file naam ka pattern) par depend karta hai |

Humne `makereport` isliye chuna kyunki wo seedha `page.screenshot()` leta hai, file naam par depend nahi karta.

**COMMON MISTAKES:**
- `report.when == "call"` check na karna. Tab setup/teardown ke phase me bhi chalega.
- Hook me exception aane par poora test run pe asar. Isliye production me try/except lagate hain (Part D me).

## PRACTICE C

1. `pytest.ini` banao aur `pytest --markers` chalao. Tumhare 2 markers dikhne chahiye.
2. `base_url` set karke test me `page.goto("/")` use karo. (Ye FL-2 ka hissa hai.)
3. `.gitignore` laga ke `git status` dekho. `test-results/` ab untracked list me nahi aana chahiye.
4. Upar wala chhota hook `conftest.py` me daalo, ek test jaan-boojh ke fail karo, console me `FAILED TEST HAD PAGE: True` aana chahiye.

**Review checklist (L2):** kya tum bata sakte ho ki `addopts` kya karta hai aur `hookwrapper` kyun?


---

# Part D: Allure Report (step by step)

**Is part me tum ye seekhoge:** results kaise bante hain, report kaise banti hai, report ko readable kaise banate hain, failure par screenshot kaise lagate hain, history kaise rakhte hain, aur report kaise padhte hain.

> Is part ke code maine **real Allure 3 CLI (v3.22.1)** aur `allure-pytest 2.16.2` se chalaya hai. Browser wale hisse (screenshot) maine nakli `page` object se test kiye. Real browser par tum chalaoge.

---

## D1. Allure kya hai aur pehli report

### WHY
Console me `FAILED test_x - AssertionError` dikhta hai. Isse team ko ye nahi pata chalta ki **kaunsa step toota, us waqt screen kaisi thi, API ne kya diya.** Allure ye sab ek jagah deta hai.

### WHAT: do alag cheezein (bahut zaroori)

```text
pytest ──(--alluredir)──▶  allure-results/   ──(allure generate)──▶  allure-report/  ──(allure open)──▶ browser
                           (kaccha data, JSON)                        (taiyar HTML)
```

| Folder | Kya hai | Kisne banaya |
|---|---|---|
| `allure-results/` | Har test ka raw JSON + attachments | `allure-pytest` (pytest ke andar plugin) |
| `allure-report/` | Dekhne layak HTML report | `allure` CLI (alag tool) |

Analogy: `allure-results` = kaccha saaman, `allure-report` = bana hua khaana.

**Isliye 2 install chahiye:**
1. `allure-pytest`: Python plugin (`pip`)
2. `allure` CLI: report banane wala tool (`npm`)

### HOW: Step by step

**Step 1. Node check karo** (Allure 3 Node.js par chalta hai):
```bash
node -v
```
Version dikhna chahiye. Nahi dikha to Node.js ka LTS version install karo.

**Step 2. Python plugin:**
```bash
pip install allure-pytest
```
(Ye tumhare `requirements.txt` me pehle se hai.)

**Step 3. Allure CLI:**
```bash
npm install -g allure
allure --version      # maine yahan 3.22.1 dekha
```
Permission error aaye to install ke bina seedha `npx allure ...` use kar sakte ho (maine ye tareeka chalaya hai).

**Step 4. Ek practice file banao (browser ki zaroorat nahi), `test_allure_demo.py`:**

```python
import allure
import pytest


@allure.epic("RetailHub")
@allure.feature("Cart")
class TestCart:

    @allure.story("Add to cart")
    @allure.title("Backpack ko cart me add kar sakte hain")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_add_item(self):
        with allure.step("Cart khali hai"):
            cart = []
        with allure.step("Backpack add karo"):
            cart.append("Sauce Labs Backpack")
        with allure.step("Cart me 1 item hona chahiye"):
            assert len(cart) == 1

    @allure.story("Price")
    @allure.title("Price total sahi hai: {price} x {qty}")
    @pytest.mark.parametrize("price, qty, total", [(10, 2, 20), (5, 3, 15)])
    def test_total(self, price, qty, total):
        assert price * qty == total

    @allure.story("Price")
    @allure.title("Ye test jaan-boojh ke fail hota hai (demo)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_failing_demo(self):
        allure.attach("{'order_id': 42}", name="api-response",
                      attachment_type=allure.attachment_type.JSON)
        assert 1 + 1 == 3, "arithmetic broke"
```

**Step 5. Results banao:**
```bash
pytest --alluredir=allure-results --clean-alluredir
```

**Step 6. Report banao:**
```bash
allure generate allure-results --clean
```
`allure-report/` folder ban jayega.

**Step 7. Report kholo:**
```bash
allure open allure-report
```
Terminal me kuch aisa dikhega: `Allure is running on http://localhost:<port>. Press CTRL+C to stop.` Us link ko browser me kholo.

### LINE-BY-LINE
- `--alluredir=allure-results`: allure-pytest ko batata hai ki raw results kahan likhne hain.
- `--clean-alluredir`: pehle us folder ko saaf karo. **Nahi lagaya to purane run ke results naye ke saath mix ho jaate hain** aur report me ghalat count aata hai.
- `allure generate <results> --clean`: results se report banao, purani report folder hata ke.
- `allure open <report-folder>`: report ko ek chhote local server par serve karta hai (maine HTTP 200 check kiya).

### Is demo se tumhe kya dikhna chahiye
Total **4 tests** (3 passed, 1 failed). Report me epic `RetailHub`, feature `Cart`, stories `Add to cart` aur `Price`, test titles me `10 x 2` jaisi values, aur 1st test ke andar 3 steps. (Maine in sab ko generated data me check kiya.) Report ki exact screen/layout version ke saath alag ho sakti hai, isliye jo tum dekho wahi padho.

### KYUN YE CHOICE?
| Option | Fark |
|---|---|
| **Allure 3** (npm, humne chuna) | Current version. Java nahi chahiye. Ek `npm install -g allure` |
| Allure 2 (`allure-commandline`, Java) | Purana/legacy. Java install, purane blog-commands |
| `pytest-html` | Simple HTML, par steps/attachments/history kamzor |

Internet par bahut tutorials Allure 2 ke hain (`allure serve` wagairah). Command copy karne se pehle check karo ki wo Allure 3 ka hai. `allure serve` Allure 3 CLI me bhi maujood hai (help me dikha), par hum **generate + open** use karte hain kyunki CI me report ko file/artifact ke roop me chahiye hoti hai.

### AS A STUDENT
Pehle ye demo file ke saath har step haath se karo. Report me ek failed test kholo aur khud bolo: "mujhe ye test dekh ke kya samajh aaya?" Samajh nahi aaya to report kharab hai, tum nahi.

### AS AN SDET
`allure-results` ko CI me artifact banake rakh lena **sabse safe** hai, kyunki usse kabhi bhi report dobara ban sakti hai. Report sirf "view" hai.

### COMMON MISTAKES
- `--clean-alluredir` bhool jana (purana data mix).
- `allure generate` ko galat folder me chalana (path galat, report khali).
- `index.html` ko double-click karke kholna. Report data alag JSON files se load karti hai, browsers local file par aisa block kar sakte hain. `allure open` use karo.
- Sirf `allure-pytest` install karna aur CLI bhool jana (ya ulta).

### PRACTICE D1
1. Demo file chalake report kholo. Failed test ka message aur attached `api-response` dekho.
2. `--clean-alluredir` hata ke do baar run karo. Report me kya fark aaya?
3. `allure-results` folder me kaunsi files hain? (`*-result.json`, `*-attachment...`). Ek result JSON kholke `status` field dhundho.

**Answer key:** (2) Tests duplicate dikhte hain ya count badh jaata hai, kyunki dono runs ke results ek folder me hain.

---

## D2. Report ko padhne layak banana (labels, titles, steps)

### WHY
`test_checkout_workflow.py::test_user_can_complete_checkout` manager ko kuch nahi batata. "User ek product khareed ke order complete kar sakta hai" batata hai.

### WHAT: Allure ke tools

| Tool | Kaam | Example |
|---|---|---|
| `@allure.title` | Padhne layak naam | `"Backpack cart me add hota hai"` |
| `@allure.epic/feature/story` | Report me grouping (bada → chhota) | RetailHub → Cart → Add to cart |
| `@allure.severity` | Test kitna critical | `CRITICAL`, `NORMAL`, `MINOR`... |
| `@allure.tag`, `@allure.link`, `@allure.issue` | Tag, link, bug link | |
| `allure.step(...)` | Test ke andar ke steps | "Login karo" |
| `{param}` title me | Parametrize ki values title me | `"... {price} x {qty}"` |

### CODE: Page Object me steps (SAFE tareeka)

```python
# pages/login_page.py
import allure
from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def login(self, username: str, password: str):
        with allure.step(f"Login as {username}"):
            self.username.fill(username)
            self.password.fill(password)
            self.login_button.click()
```

### LINE-BY-LINE
- `with allure.step("..."):` is block ke andar ka kaam report me ek **step** ban jaata hai. Fail hua to wahi step lal dikhega.
- f-string me sirf `username` hai, **password nahi**.

### SECURITY: `@allure.step` decorator ka jaal (maine verify kiya)

Aise likhna **galat** hai:
```python
@allure.step("Login as {username}")
def login(self, username, password):   # <- password bhi report me chala jayega
    ...
```
Maine chalake dekha: decorator function ke **saare arguments** step ke "parameters" me daal deta hai, `password='secret_sauce'` bhi. Argument ka naam `_password` karne se bhi nahi rukta.

| Tareeka | Password report me? |
|---|---|
| `@allure.step("Login as {username}")` decorator | **Haan, leak** |
| `with allure.step(f"Login as {username}")` block | **Nahi** (verified) |

**Rule:** jis function me password/token/API key ho, wahan decorator mat lagao, `with allure.step(...)` use karo. Report ko log share karte hain, aur kabhi public bhi ho sakti hai (Pages).

### KYUN YE CHOICE?
- **Decorator vs context manager:** decorator seedha-saada hai (ek line) par arguments report karta hai. Context manager thoda lamba hai par tum control karte ho ki kya dikhe. Secrets ho to context manager.
- **Steps POM me, tests me nahi:** ek hi `login()` har test me wahi step deta hai. Test me sirf "kya verify karna hai" (business assertion) rakho. Ye wahi rule hai jo tumne POM me seekha: HOW page object me, WHAT test me.
- **Allure labels vs docstring/comments:** comments report me nahi dikhte. Allure labels report me filter/group ke liye kaam aate hain.

### AS A STUDENT
Pehle ek test me `with allure.step` lagao aur report me dekho. Jab dikhe, tab POM me daalo.

### AS AN SDET
Steps ka naam **business language** me likho ("Cart me Backpack add karo"), implementation me nahi ("click button #add-to-cart-sauce-labs-backpack"). Report ka reader developer + manager dono hai.

### COMMON MISTAKES
- Har choti line ko step bana dena. Report lambi, par info kam.
- Step me password/token.
- Title me `{param}` likhna par parametrize ka naam alag. (Param ka naam wahi jo test function ka argument hai.)

### PRACTICE D2
1. Demo file me `@allure.severity` aur `@allure.story` badlo aur report me grouping dekho.
2. Apne `LoginPage.login` me `with allure.step` lagao (FL-2 ke saath).
3. Ek test jaan-boojh ke `@allure.step` decorator + password argument ke saath likho, report me leak khud dekho. Phir context manager se fix karo.

---

## D3. Failure par evidence: screenshot aur URL (sabse useful part)

### WHY
Developer ka pehla sawaal: "Test fail hua, us waqt page kaisa tha?" Screenshot ek line me jawab deta hai.

### WHAT
Hum pytest ka hook (Part C.5) use karke, **jaise hi test fail ho**, `page.screenshot()` ko Allure me attach karenge.

### CODE: `conftest.py` (maine isko nakli `page` ke saath chalake verify kiya)

```python
import allure
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.failed and report.when in ("setup", "call"):
        page = getattr(item, "page_for_report", None)
        if page is None:
            return
        try:
            allure.attach(
                page.screenshot(full_page=True),
                name=f"screenshot-{report.when}",
                attachment_type=allure.attachment_type.PNG,
            )
            allure.attach(
                page.url,
                name="page-url",
                attachment_type=allure.attachment_type.TEXT,
            )
        except Exception as exc:
            print(f"[evidence] screenshot lena fail hua: {exc}")


@pytest.fixture(autouse=True)
def _expose_page_for_report(request):
    if "page" in request.fixturenames:
        request.node.page_for_report = request.getfixturevalue("page")
```

### LINE-BY-LINE
- `report.failed and report.when in ("setup", "call")`: test body (`call`) **ya fixture** (`setup`) me fail hua. **Tumhara login fixture me hai**, to `setup` bahut zaroori hai. Sirf `call` rakhoge to login fixture fail hone par screenshot nahi milega (maine ye test karke dekha).
- `page.screenshot(full_page=True)`: poora page, bytes me. `allure.attach(bytes, name=, attachment_type=PNG)`: disk par file banaye bina seedha report me.
- `try/except`: screenshot lena khud fail ho sakta hai (browser crash). Evidence ki wajah se asli failure chhup na jaye.
- **autouse fixture `_expose_page_for_report`:** kyun chahiye? Jab fixture (jaise `auth_page`) fail hota hai, tab `item.funcargs` me `page` abhi store nahi hua hota (maine check kiya). Ye fixture `page` ko pehle hi test item par rakh deta hai.
- `if "page" in request.fixturenames`: sirf un tests me `page` banao jinko sach me chahiye. **API-only tests me browser nahi khulega.**
- `autouse=True`: har test par apne aap lagta hai, naam me `_` isliye ki ye internal helper hai.

### KYUN YE CHOICE?
| Option | Kyun chuna / nahi chuna |
|---|---|
| Har test me `try/except + screenshot` | Repeat, bhool jaoge |
| `makereport` hook (chuna) | Ek jagah, har test par, sirf fail par |
| Allure ki official guide ka teardown hook | Playwright jo screenshot file save karta hai use dhundh ke attach karta hai. Valid, par file naam ke pattern par depend aur fixture-setup failure me alag behave kar sakta hai |
| `--screenshot only-on-failure` akele | Screenshot disk par aata hai (`test-results/`), report me nahi lagta |

**Dono saath rakhna theek hai:** `--screenshot only-on-failure` (pytest.ini) + ye hook. Pehla file artifact deta hai, doosra Allure me jodta hai.

### API response bhi attach karo (API tests me)

```python
import allure
import requests

def test_get_user(base_url):
    resp = requests.get(f"{base_url}/users/1", timeout=5)
    allure.attach(resp.text, name="response-body",
                  attachment_type=allure.attachment_type.JSON)
    assert resp.status_code == 200
```

Fail hone par report me exact response dikhega. (Authorization header ya token attach mat karna.)

### Trace aur video
Playwright trace (`test-results/<test>/trace.zip`) Allure ke andar nahi khulta. Use **CI artifact** ki tarah rakho aur `playwright show-trace trace.zip` se kholo. Allure ki official guides me video attach karne ka bhi tareeka hai, par pehle screenshot + trace pakke karo.

### AS A STUDENT
Ek test jaan-boojh ke fail karwao (galat expected text), report kholo, screenshot dekho. Fir fixture ke andar fail karwao (galat password), dekho `screenshot-setup` aaya ya nahi.

### AS AN SDET
Screenshot me **sensitive data** (email, token) aa sakta hai. Public report (Pages) par daalne se pehle sochna. Test data fake/demo rakho.

### COMMON MISTAKES
- Sirf `call` phase handle karna (fixture failures miss).
- Har test me browser page bana dena (autouse me condition na lagana).
- `allure.attach(page.screenshot(path=...))`: `path` dene par bytes nahi milte. Seedha `page.screenshot()` use karo.

### PRACTICE D3
1. Hook `conftest.py` me daalo, ek UI test fail karwao, screenshot report me dekho.
2. Login fixture me galat password dekar fail karwao. `screenshot-setup` dikhna chahiye.
3. Ek API-only test chalao. Browser nahi khulna chahiye.

---

## D4. Config file, history aur retries

### WHY
Report ka naam, folder, aur **pichhle runs ka comparison (history)** config se aata hai.

### CODE: `allurerc.json` (project folder me)

```json
{
  "name": "RetailHub UI Report",
  "output": "./allure-report",
  "historyPath": "./history.jsonl"
}
```

### LINE-BY-LINE
- `name`: report ka title (maine check kiya, report me yahi aaya).
- `output`: report kahan banegi.
- `historyPath`: ek file jisme har run ka summary **append** hota hai. Maine do baar generate kiya to `history.jsonl` me 2 lines aayi. Allure is file se "pichhle runs me ye test pass tha/fail" dikhata hai.

Allure CLI ye file **current folder** me dhundhta hai (`allurerc.json`/`.yml`/`.mjs`...). Isliye `allure generate` ko `playwright/ex_6` ke andar chalao.

### KYUN YE CHOICE? JSON vs `.mjs`
Docs me `allurerc.mjs` ka example `import { defineConfig } from "allure"` use karta hai, jiske liye `allure` package project me install hona chahiye. **JSON me import nahi hota**, beginner ke liye safe. Advanced options chahiye to baad me `.mjs`.

### Retries aur flaky
```bash
pytest -n 2 --reruns 1 --alluredir=allure-results --clean-alluredir
```
Maine ek test banaya jo pehli baar fail hota hai aur retry me pass. Allure summary me **retries = 1** aaya. Matlab report khud batata hai ki "ye test ek baar me pass nahi hua". Retry se green dikhna aur flaky ko chhupana alag cheez hai. Isliye report me retries dekhte raho.

- `-n 2`: 2 workers me parallel (pytest-xdist). Maine check kiya ki parallel run me bhi results ek folder me sahi aate hain.
- `--reruns 1`: fail hone par 1 baar dobara (pytest-rerunfailures).

### History CI me
Local machine par `history.jsonl` file bachi rehti hai. **CI ki machine har run par naye sire se banti hai**, to file kho jaati hai. CI me history chahiye to is file ko run ke beech save karna padta hai (cache ya kisi branch me). Ye advanced hai, pehle Part E ke Level 1 aur 2 pakke karo. (Maine CI ka history flow GitHub par chalaya nahi hai.)

### AS AN SDET
History se pata chalta hai ki kaunsa test **baar-baar** flaky hai. Wo list team ko do aur fix karo. Retries ka count bhi quality metric hai.

### COMMON MISTAKES
- `historyPath` set karna par file ko `.gitignore` na karna (local history commit ho jati).
- Config file galat folder me rakhna, report ka naam default hi rehta hai.
- `--reruns` ko default bana dena. Flaky test chhup jaate hain.

### PRACTICE D4
1. `allurerc.json` banao, 2 baar run + generate karo, `history.jsonl` ki lines ginno.
2. Report ka naam badlo aur check karo.

---

## D5. Report ko SDET ki tarah padhna

### WHY
Report banana half kaam hai. **Failure ko 2 minute me samajhna** SDET ka asli kaam hai.

### Failed test padhne ka routine (5 sawaal)

1. **Kaunsa test, kaunsi feature/story?** (labels se grouping)
2. **Kaunsa step toota?** (steps list me lal step)
3. **Kya error message hai?** (assertion kya expected tha, kya mila)
4. **Evidence kya kehta hai?** (screenshot, page URL, API response)
5. **Pehle bhi toota tha?** (history/retries)

Ye 5 jawab milte hi tum decide kar sakte ho: **product bug / test bug / environment issue.**

| Evidence | Likely cause |
|---|---|
| Screenshot me error banner, API 500 | Product/backend bug |
| Screenshot khali ya galat page | Test ne site open nahi ki, galat URL (tumhara G1!) |
| Element nahi mila, UI badla | Locator / test bug |
| Sirf CI me fail, local me pass | Environment (timing, data, secret) |
| Kabhi pass, kabhi fail | Flaky (history/retries dekho) |

### AS A STUDENT
Demo project me ek test jaan-boojh fail karao aur upar ke 5 sawaal likhke jawab do.

### AS AN SDET
Manager ko 30 second me bolo: "Total X, Y fail. Do product bug (links), ek test issue (fix in progress), ek flaky (known)." Ye format interview me bhi kaam aata hai.

### PRACTICE D5
Apne demo run ke failed test par 5 sawaalon ka jawab ek paragraph me likho.

---

## D6. Apne `ex_6` me Allure lagana (tumhara kaam)

**Tumhe karna hai** (solution main nahi de raha):
1. `LoginPage`, `InventoryPage`, `CartPage`, `CheckoutPage` ke main actions me `with allure.step(...)` lagao (business language me).
2. Tests par `@allure.epic/feature/story/title/severity` lagao. Ek test `smoke`, baaki `regression` mark karo.
3. `conftest.py` me D3 ka hook + autouse fixture daalo.
4. `allurerc.json` banao.
5. `pytest --alluredir=allure-results --clean-alluredir` → `allure generate allure-results --clean` → `allure open allure-report`.
6. Ek test jaan-boojh fail karwao. Screenshot report me dikhna chahiye.

**Done jab:** report me tumhare checkout test ke steps aur ek failure ka screenshot dikh raha ho.

**Review checklist (L3):** kya tum bata sakte ho ki `allure-results` aur `allure-report` me fark kya hai, password leak kaise hota hai, aur setup-phase failure ka screenshot kyun alag handle hota hai?


---

# Part E: GitHub Actions CI/CD (step by step)

> Is part ki saari YAML files maine **`actionlint` (v1.7.12)** se lint ki hain (sab pass). Par maine ye workflows **real GitHub par nahi chalaye**, mere paas tumhara GitHub account nahi hai. Asli proof tab hoga jab tum push karke Actions tab me green tick dekhoge.

**Roadmap (levels):**

| Level | Kya | Chunk |
|---|---|---|
| 0 | Concepts + pehla "hello" workflow | E1 to E3 |
| 1 | pytest CI me chalana | E4 |
| 2 | Playwright + Allure CI me, artifacts | E5, E6 |
| 3 | Report ko link par publish (Pages) | E7 |
| 4 | Triggers, matrix, gating, debugging, security | E8 to E11 |

Ek level pakka hone ke baad hi agla lo.

---

## E1. Concepts: GitHub Actions kaise sochta hai

### WHY
Tum ye har baar haath se karte ho: code badla → local me `pytest` → result dekha. Team me 5 log hain to koi bhool jayega. CI ye kaam **har push par automatically** karta hai, aur tumhara code toot jaye to turant pata chalta hai.

### WHAT: vocabulary (har term define)

```text
Event (push / pull_request / schedule ...)
   └─▶ Workflow  (ek .yml file)
          └─▶ Job  (ek machine par kaam ka group)
                 └─▶ Step  (ek ek kaam)
                        ├─ run:   (shell command)
                        └─ uses:  (taiyar Action, jaise checkout)
```

| Term | Matlab |
|---|---|
| **Event** | Jo workflow ko chalata hai (code push, PR, manual button, time) |
| **Workflow** | Ek YAML file jo `.github/workflows/` me hoti hai |
| **Job** | Steps ka group. Har job **alag, saaf machine** par chalta hai |
| **Runner** | Wo machine (`ubuntu-latest` = GitHub ki Linux machine) |
| **Step** | Ek kaam. Ek job ke steps ek ke baad ek, **ek hi machine** par |
| **Action** | Kisi aur ka likha reusable step (`actions/checkout`) |

### Teen zaroori jagah ki baatein (tumhari repo ke liye)

1. **Workflow files hamesha repo ke root par** `.github/workflows/` me honi chahiye. `playwright/ex_6/.github/...` me nahi chalegi.
2. **Default branch:** tumhari repo ki default branch `main` hai jisme sirf `README.md` hai, aur tumhara asli kaam `master` branch me hai. GitHub ke `schedule` aur manual "Run workflow" button **default branch** par hi dikhte/chalte hain. Do raste:
   - **Option A (aasan):** `master` ko default banao. GitHub par repo ke **Settings → Branches** me default branch badalne ka option milta hai. (Exact label GitHub ke UI par depend karta hai.)
   - **Option B:** `master` ko `main` me merge karo.
   Is guide me `branches: [main, master]` likha hai taaki dono par chale.
3. **Tumhara project subfolder me hai** (`playwright/ex_6`). To workflow me `working-directory` batana padega (E4 me).

### AS A STUDENT
CI ko "GitHub ka free computer" samjho jo tumhari ek file padhta hai aur wahi commands chalata hai jo tum terminal me chalate ho. Jo tum terminal me nahi chala sakte, wo CI me bhi nahi chalega.

### AS AN SDET
CI ka maqsad **bharosa** hai: "main branch par jo bhi merge hua, wo tests se guzra." Agar CI me tests ignore hote hain, to CI sirf decoration hai.

---

## E2. YAML 101 (workflow files isi me likhte hain)

### WHAT
YAML = key: value ka format, **indentation (spaces) se structure**.

```yaml
name: Mera Workflow          # key: value
on:                          # key jiske andar kuch aur hai
  push:
    branches: [main, master] # list (square brackets)
jobs:
  test:
    steps:
      - run: echo "one"      # list ka item "- " se shuru
      - run: |               # multi-line text
          echo "two"
          echo "three"
```

### Rules
- **Spaces use karo, Tab nahi.** Standard 2 spaces.
- `- ` se list item. Same level ke items ka indentation same.
- `|` ke baad ka block multi-line command hai.
- `#` comment hai.

### Sabse common jaal: version ko quote karo (maine verify kiya)

```yaml
python-version: 3.10     # YAML ise number 3.1 samajhta hai!
python-version: "3.10"   # sahi: text "3.10"
```

Maine PyYAML se check kiya: bina quote ke `3.10` ban gaya `3.1`. CI ne galat Python version install kar diya hota.

### COMMON MISTAKES
- Indentation me 1 space ka fark, poora workflow invalid.
- Colon ke baad space bhoolna (`name:value`).
- Special characters wali string ko quote na karna.

### PRACTICE E2
Is ko theek karo (3 galtiyan hain):
```yaml
jobs:
 test:
  runs-on:ubuntu-latest
  steps:
	- run: echo hi
```
**Answer key:** `runs-on: ubuntu-latest` me colon ke baad space; indentation consistent (2 spaces); Tab hatao (spaces).

**Tool:** `pip install actionlint-py` ke baad repo root par `actionlint` chalao. Ye workflow file ki galtiyan push se **pehle** pakad leta hai (maine ise use kiya).

---

## E3. Pehla workflow: "Hello"

### Step 1: file banao
Repo root par: `.github/workflows/01-hello.yml`

```yaml
# .github/workflows/01-hello.yml
name: Hello CI

on:
  push:
  workflow_dispatch:

jobs:
  hello:
    runs-on: ubuntu-latest
    steps:
      - name: Say hello
        run: echo "Hello from GitHub Actions"
      - name: Who triggered me
        run: echo "Triggered by ${{ github.actor }} on branch ${{ github.ref_name }}"
      - name: Show machine info
        run: |
          python3 --version
          pwd
          ls
```

### LINE-BY-LINE
- `name`: Actions tab me dikhne wala naam.
- `on`: kab chale. `push:` = kisi bhi branch par push. `workflow_dispatch:` = manual "Run workflow" button.
- `jobs.hello`: ek job, naam `hello`.
- `runs-on: ubuntu-latest`: GitHub ki Linux machine.
- `steps`: ek ke baad ek.
- `run:` = shell command. `${{ ... }}` = GitHub ka expression. `github.actor` = kisne push kiya, `github.ref_name` = branch ka naam.
- `ls` se dikhega ki machine par abhi **kuch bhi nahi** hai (repo bhi nahi!). Kyunki humne checkout nahi kiya. Yahi concept E4 me kaam aayega.

### Step 2: push karo
```bash
git add .github/workflows/01-hello.yml
git commit -m "ci: add hello workflow"
git push
```

### Step 3: result dekho
GitHub repo → **Actions** tab → "Hello CI" → run kholo → job `hello` → har step ke logs expand karo. Green tick = sab step ka exit code 0.

### KYUN YE CHOICE? `ubuntu-latest`
| Runner | Kab |
|---|---|
| `ubuntu-latest` (humne chuna) | Sabse common, tez, Playwright ke liye achha, aur zyada plans me sasta/free |
| `windows-latest`, `macos-latest` | Jab app sach me un OS par chalna ho. Slow/costly ho sakte hain |

### AS A STUDENT
Pehle ye workflow chalao, phir `echo "..."` badal ke dobara push karo. Dekho har push par naya run bana.

### AS AN SDET
Run ke logs ko "sabut" samjho. Koi pooche "kal ka test kyun fail hua?" to run ka link do.

### COMMON MISTAKES
- Workflow file galat folder me (`.github/workflow/` me `s` bhoolna).
- Branch par push kiya par workflow ka `on` us branch ko nahi chahta.
- File push hi nahi ki (sirf local me hai).

### PRACTICE E3
1. Workflow chalake Actions tab me log dekho. `ls` ka output kya tha? Khali kyun?
2. Ek step add karo jo `echo` se tumhara naam print kare.
3. `workflow_dispatch` se manual run karne ki koshish karo. (Button tab dikhega jab workflow file default branch par ho, E1 dekho.)

---

## E4. pytest ko CI me chalana

### WHY
Pehle bina browser ke simple tests CI me green karo. Agar pehle hi Playwright lagaoge aur fail hoga to samajh nahi aayega ki problem CI ki hai ya browser ki. **Ek time par ek naya cheez.**

### Practice project banao: `ci-demo/` (repo root par)

`ci-demo/requirements.txt`:
```text
pytest==9.2.0
```

`ci-demo/test_basic.py`:
```python
import os


def test_addition():
    assert 2 + 2 == 4


def test_string_upper():
    assert "ci".upper() == "CI"


def test_runs_inside_github_actions():
    # GitHub Actions har run me GITHUB_ACTIONS=true set karta hai.
    # Local machine par ye variable nahi hota, isliye dono jagah test pass hona chahiye.
    in_ci = os.getenv("GITHUB_ACTIONS") == "true"
    print("Running in CI:", in_ci)
    assert isinstance(in_ci, bool)
```

(Pehle local me `cd ci-demo && pytest` chalao. Maine ye 3 tests local me chalaye, sab pass.)

### Workflow: `.github/workflows/02-pytest-basic.yml`

```yaml
# .github/workflows/02-pytest-basic.yml
name: Python Tests (basic)

on:
  push:
    branches: [main, master]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: ci-demo
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with:
          python-version: "3.12"
          cache: pip
          cache-dependency-path: ci-demo/requirements.txt
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest -v
```

### LINE-BY-LINE
- `pull_request:` PR banne/update hone par bhi chale. (Merge se pehle test check.)
- `defaults.run.working-directory: ci-demo`: **saare `run:` steps** is folder me chalenge. (`cd` har jagah likhne se behtar.)
- `uses: actions/checkout@v7`: tumhari repo ko runner par laata hai. **Iske bina runner par tumhara code hota hi nahi** (E3 ka khali `ls`).
- `uses: actions/setup-python@v7` + `with:`: Python install. `python-version` quote me. `cache: pip` = pip packages cache hote hain, agli runs fast. `cache-dependency-path` = cache ki key kis file se bane (path **repo root se**).
- `run: pip install -r requirements.txt`: `working-directory` ki wajah se `ci-demo` ke andar chalega.
- `run: pytest -v`: tests. Koi test fail hua to non-zero exit code, step red, job red.

> **Bahut zaroori fark:** `defaults.run.working-directory` sirf `run:` steps par lagta hai, **`uses:` steps par nahi.** Isliye `cache-dependency-path: ci-demo/requirements.txt` me poora path likha hai.

### Action versions
`@v7` ka matlab: us action ka major version 7. Maine in actions ke official repos ke tags dekhe: `checkout` v7, `setup-python` v7, `upload-artifact` v7, `download-artifact` v8, `upload-pages-artifact` v5, `deploy-pages` v5 (ye sab Node 24 par chalte hain). Versions badalte rehte hain. Naya workflow likhte waqt us action ke repo ka README dekh ke latest major lo.

### KYUN YE CHOICE?
| Sawaal | Choice | Kyun |
|---|---|---|
| Python kaise install | `actions/setup-python` | Official, version control, pip cache built-in |
| Packages | `pip install -r requirements.txt` | Wahi file jo local me use hoti hai (same versions) |
| Folder | `defaults.run.working-directory` | Har `run` me `cd` nahi |
| Version tag | `@v7` (major) | Chhote fixes apne aap, breaking change nahi |

### AS A STUDENT
Ek test jaan-boojh fail karwa ke push karo. Actions me **red cross** dekho aur log me failing assertion padho. Phir theek karke green karo. Ye "red → fix → green" loop CI ki jaan hai.

### AS AN SDET
`pull_request` trigger ke saath "required status check" (E9) lagake merge ko test-pass par rokte hain. Isse CI ka asli faida milta hai.

### COMMON MISTAKES
- `checkout` bhoolna (code hi nahi).
- `working-directory` ke bina galat folder me pytest.
- `python-version: 3.10` bina quote.
- `requirements.txt` ka path galat.

### PRACTICE E4
1. `ci-demo` banao, push karo, green run dekho.
2. Ek test fail karwao, red dekho, fix karo.
3. `checkout` step hata ke push karo. Kya error aaya? Wapas lagao.

---

## E5. Playwright + Allure ko CI me chalana

### WHY
Ab tumhara asli `ex_6` project. CI ki saaf machine par browser bhi install karna padega.

### Pehle local checklist (CI se pehle yehi chalao)
```bash
cd playwright/ex_6
pip install -r requirements.txt
playwright install chromium
pytest -v --alluredir=allure-results --clean-alluredir
```
Agar ye local me green nahi, CI me bhi nahi hoga. **FL-1/FL-2 pehle.**

### Workflow: `.github/workflows/03-playwright-allure.yml`

```yaml
# .github/workflows/03-playwright-allure.yml
name: Playwright + Allure

on:
  push:
    branches: [main, master]
    paths:
      - "playwright/ex_6/**"
      - ".github/workflows/03-playwright-allure.yml"
  pull_request:
    paths:
      - "playwright/ex_6/**"
  workflow_dispatch:

concurrency:
  group: playwright-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    defaults:
      run:
        working-directory: playwright/ex_6
    steps:
      - uses: actions/checkout@v7

      - uses: actions/setup-python@v7
        with:
          python-version: "3.12"
          cache: pip
          cache-dependency-path: playwright/ex_6/requirements.txt

      - uses: actions/setup-node@v7
        with:
          node-version: "22"

      - name: Install Python dependencies
        run: pip install -r requirements.txt

      - name: Install Playwright browser
        run: playwright install --with-deps chromium

      - name: Run tests
        run: pytest -v --alluredir=allure-results

      - name: Install Allure CLI
        if: ${{ !cancelled() }}
        run: npm install -g allure@3

      - name: Generate Allure report
        if: ${{ !cancelled() }}
        run: allure generate allure-results --clean

      - name: Upload Allure report
        if: ${{ !cancelled() }}
        uses: actions/upload-artifact@v7
        with:
          name: allure-report
          path: playwright/ex_6/allure-report
          if-no-files-found: warn
          retention-days: 14

      - name: Upload Playwright traces and screenshots
        if: ${{ !cancelled() }}
        uses: actions/upload-artifact@v7
        with:
          name: playwright-test-results
          path: playwright/ex_6/test-results
          if-no-files-found: ignore
          retention-days: 14
```

### LINE-BY-LINE (naye hisse)
- `paths:` filter: sirf jab `playwright/ex_6/**` ya yahi workflow file badle tab chalao. Repo me DSA/SQL notes badle to CI nahi chalega (monorepo ke liye zaroori).
- `concurrency` + `cancel-in-progress: true`: ek hi branch par naya push aaye to purani chal rahi run cancel (resource bachta hai).
- `permissions: contents: read`: workflow ke token ko **sirf padhne ka haq**. Least privilege.
- `timeout-minutes: 15`: atka hua test CI ko ghanto nahi rokega.
- `setup-node`: Allure CLI Node par chalta hai.
- `playwright install --with-deps chromium`: browser **aur Linux system libraries** install. `--with-deps` CI me zaroori hai.
- **Headless:** CI me screen nahi hoti. pytest-playwright default me headless chalata hai (`--headed` sirf tab jab tum mangte ho).
- `pytest -v --alluredir=allure-results`: CI ki saaf machine hai, to `--clean-alluredir` ki zaroorat nahi.
- **`if: ${{ !cancelled() }}`:** tests **fail** hon tab bhi report/artifacts banao. (Default me pichhla step fail to agle skip hote hain.) Fail hone par hi to evidence chahiye!
- `upload-artifact`: files ko run ke saath save. `path` repo root se (kyunki `uses:` par `working-directory` nahi lagta).

### Credentials / secrets (jab real app ho)
SauceDemo ke credentials public demo ke hain, to code me default rakhna chalega. Real app me:

```python
import os
username = os.getenv("APP_USER", "standard_user")
password = os.getenv("APP_PASSWORD", "secret_sauce")   # default sirf demo site ke liye
```

Workflow me:
```yaml
      - name: Run tests
        run: pytest -v --alluredir=allure-results
        env:
          APP_PASSWORD: ${{ secrets.APP_PASSWORD }}
```
Secret add karne ke liye GitHub repo **Settings → Secrets and variables → Actions** me "New repository secret" (UI ka exact label badal sakta hai). Secret ki value logs me `***` ban jaati hai.

### KYUN YE CHOICE?
| Sawaal | Choice | Kyun |
|---|---|---|
| `always()` vs `!cancelled()` | `!cancelled()` | `always()` cancel hone par bhi chalta hai. `!cancelled()` fail par chalta hai par cancel par skip, behtar |
| Report CI me banana | haan | Artifact me ready report mile, download karke khol lo |
| Chromium hi | haan (abhi) | Pehle ek browser pakka. Cross-browser E8 me |
| Pinned Allure | `allure@3` (major) | Naya major version aaye to CI na toote |

### AS A STUDENT
Pehle workflow me sirf checkout + install + `pytest` rakho, green karo. Phir Allure steps ek ek karke jodo.

### AS AN SDET
CI me jo fail ho wo **reproducible** hona chahiye. Isliye same Python/Playwright versions pin karo, aur local me wahi commands chalao jo CI chalata hai.

### COMMON MISTAKES
- `playwright install` bhoolna ("Executable doesn't exist" error).
- `--with-deps` bhoolna (system library missing).
- `upload-artifact` ka `path` `working-directory` ke hisaab se likhna (galat).
- Allure steps ko `if` ke bina rakhna, to tests fail par report hi nahi banti.
- `paths` filter galat, workflow trigger hi nahi hota.

### PRACTICE E5
1. Local checklist green karo, phir workflow push karo.
2. Ek test jaan-boojh fail karwao. Run red hoga. Kya tab bhi artifacts upload hue?
3. `playwright install` step hata ke dekho kya error aata hai. (Wapas lagao.)

---

## E6. Artifacts: CI ke baad kya mil sakta hai

### WHY
CI ki machine run ke baad **gayab** ho jaati hai. Evidence tabhi bachta hai jab wo artifact ke roop me upload ho.

### Kaise download karo
Run page ke neeche **Artifacts** section me `allure-report` aur `playwright-test-results` dikhenge. Download karke unzip karo.

**Allure report kholna:**
```bash
allure open allure-report        # unzip hua folder
```

**Playwright trace kholna** (failure par `--tracing retain-on-failure` se banta hai):
```bash
playwright show-trace test-results/<test-folder>/trace.zip
```
Trace me step-by-step timeline, DOM snapshot, network aur console dikhte hain. CI failure debug karne ka sabse powerful tarika.

### KYUN YE CHOICE? `upload-artifact` vs Pages
- **Artifact:** private-ish, run ke saath, `retention-days` baad hat jaata hai. Debug ke liye perfect.
- **Pages (E7):** ek permanent link, team ko share karne ke liye.
Pehle artifact, baad me Pages.

### AS AN SDET
Artifact retention (kitne din rakhna) ek cost/privacy decision hai. Screenshots me sensitive data ho sakta hai, to bahut din mat rakho.

### COMMON MISTAKES
- Artifact ka naam same do jobs me (conflict). Matrix me naam me variable lagao (E8).
- `if-no-files-found` ignore karke path galat hone par chup rehna. Isliye humne `warn` rakha report ke liye.

### PRACTICE E6
Red run se artifact download karo, trace kholo aur failing step dhundho.

---

## E7. Allure report ko GitHub Pages par publish karna

### WHY
Artifact download karna har baar mushkil hai. Pages par ek **link** hota hai jo team khol sake.

### Pehle ek baar setup (haath se, GitHub UI me)
Repo **Settings → Pages** me "Build and deployment → Source" ko **GitHub Actions** par set karo. (UI ka exact text badal sakta hai.)

### Workflow: `.github/workflows/04-publish-pages.yml`

```yaml
# .github/workflows/04-publish-pages.yml
name: Playwright + Allure + Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

concurrency:
  group: pages
  cancel-in-progress: false

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: playwright/ex_6
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with:
          python-version: "3.12"
          cache: pip
          cache-dependency-path: playwright/ex_6/requirements.txt
      - uses: actions/setup-node@v7
        with:
          node-version: "22"
      - run: pip install -r requirements.txt
      - run: playwright install --with-deps chromium
      - name: Run tests
        run: pytest -v --alluredir=allure-results
      - name: Generate Allure report
        if: ${{ !cancelled() }}
        run: |
          npm install -g allure@3
          allure generate allure-results --clean
      - name: Package report for GitHub Pages
        if: ${{ !cancelled() }}
        uses: actions/upload-pages-artifact@v5
        with:
          path: playwright/ex_6/allure-report

  deploy-report:
    needs: test
    if: ${{ !cancelled() && needs.test.result != 'skipped' }}
    runs-on: ubuntu-latest
    permissions:
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v5
```

### LINE-BY-LINE
- **Do jobs:** `test` (tests + report banao) aur `deploy-report` (publish).
- `upload-pages-artifact`: report folder ko Pages ke format me package karta hai.
- `needs: test`: deploy job tab chale jab `test` job khatam ho.
- **`if: ${{ !cancelled() && needs.test.result != 'skipped' }}`:** default me `needs` wala job tabhi chalta hai jab pichhla **pass** ho. Humein report **fail hone par bhi** chahiye, isliye ye condition.
- `permissions: pages: write, id-token: write`: deploy karne ke liye ye 2 haq zaroori (official README ke mutabiq).
- `environment: github-pages`: Pages ka deployment environment, aur `url` se run page par link dikhta hai.
- `deploy-pages`: package kiya hua artifact publish karta hai.

### Dhyan rakho (security / privacy)
- **Public repo ka Pages site public hota hai.** Report me screenshots/URLs aate hain. Real company ka data **kabhi** public report me mat daalo. Practice me SauceDemo jaise demo site hi theek hai.
- Private repo me Pages ki availability tumhare GitHub plan par depend karti hai (maine check nahi kiya).
- Agar deploy "branch not allowed" jaisa error de, to repo ke **Settings → Environments → github-pages** me deployment branch rules dekho. Default branch hi allowed hoti hai, isliye humne trigger `main` rakha. (Ye E1 ke default-branch point se jura hai.)

### KYUN YE CHOICE? Official Pages actions vs third-party
Allure ki purani guides `peaceiris/actions-gh-pages` aur `simple-elf/allure-report-action` jaise **third-party** actions use karti hain (wo Allure 2 ke liye likhi hain). Humne GitHub ki **apni** actions (`upload-pages-artifact`, `deploy-pages`) chuni kyunki:
1. Third-party code ko tumhare repo ka token milta hai (supply-chain risk). Official me kam.
2. Allure 3 ke saath simple: report folder bana do, publish.
Trade-off: **history** (trends) is simple flow me carry nahi hoti. Wo advanced step hai.

### AS A STUDENT
Pehle E5 (artifact) pakka karo. Pages tab try karo jab report khud khol kar dekh chuke ho.

### AS AN SDET
"Latest report ka link" README me daalna ek bahut achhi aadat hai. Reviewer ek click me tumhara kaam dekh leta hai. Par pehle sochna ki public karna theek hai ya nahi.

### COMMON MISTAKES
- Pages source "GitHub Actions" set karna bhoolna.
- `permissions` na dena (deploy "Resource not accessible" error).
- Deploy job ko `needs` + default `if` ke saath chhod dena, to fail run par report publish hi nahi hoti.

### PRACTICE E7
1. Pages setup karo, workflow chalao, `page_url` se report kholo.
2. Ek test fail karwao. Kya failed run ki report bhi publish hui?

---

## E8. Triggers, matrix, parallel aur nightly runs

### Triggers (kab chalao)

| Trigger | Kab | Kaam |
|---|---|---|
| `push` | Code push | Har commit par feedback |
| `pull_request` | PR banne/update | Merge se pehle check |
| `workflow_dispatch` | Manual button | On-demand run |
| `schedule` | Time par (cron) | Nightly regression |

**cron example:** `"30 20 * * *"` = roz 20:30 **UTC** = bharat me raat ~2:00 AM (IST = UTC+5:30). Cron me time **UTC** hota hai, isliye hisaab karna padta hai. Scheduled runs default branch par chalte hain aur load ke time der se shuru ho sakte hain. Bahut din repo me activity na ho to GitHub scheduled workflows band bhi kar sakta hai (public repos par).

### Cross-browser matrix: `.github/workflows/05-matrix.yml`

```yaml
# .github/workflows/05-matrix.yml
name: Cross-browser matrix

on:
  workflow_dispatch:
  schedule:
    - cron: "30 20 * * *"   # UTC; India me raat ~2:00 AM

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        browser: [chromium, firefox]
    defaults:
      run:
        working-directory: playwright/ex_6
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with:
          python-version: "3.12"
          cache: pip
          cache-dependency-path: playwright/ex_6/requirements.txt
      - run: pip install -r requirements.txt
      - run: playwright install --with-deps ${{ matrix.browser }}
      - run: pytest -v --browser ${{ matrix.browser }} --alluredir=allure-results
      - uses: actions/upload-artifact@v7
        if: ${{ !cancelled() }}
        with:
          name: allure-results-${{ matrix.browser }}
          path: playwright/ex_6/allure-results

  report:
    needs: test
    if: ${{ !cancelled() }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/setup-node@v7
        with:
          node-version: "22"
      - uses: actions/download-artifact@v8
        with:
          pattern: allure-results-*
          merge-multiple: true
          path: allure-results
      - run: |
          npm install -g allure@3
          allure generate allure-results --clean
      - uses: actions/upload-artifact@v7
        with:
          name: allure-report
          path: allure-report
```

### LINE-BY-LINE
- `strategy.matrix.browser`: ek job ki **do copies**, ek chromium ke saath, ek firefox ke saath.
- `fail-fast: false`: ek browser fail ho to doosra band na ho. Dono ka result chahiye.
- `${{ matrix.browser }}`: us copy ki value.
- Artifact ka naam `allure-results-${{ matrix.browser }}`: **har copy ka naam alag** zaroori hai (same naam conflict deta hai).
- `report` job: `download-artifact` ke `pattern` + `merge-multiple` se dono browsers ke results ek folder me jodta hai, phir ek combined report.

### Parallel (ek machine par kai tests ek saath)
```bash
pytest -n auto
```
`pytest-xdist` ke workers. Isse CI fast hota hai **par sirf tab jab tests independent hon** (ex_6 ka Requirement 6!). Agar ek test ka cart doosre ko affect karta hai, to parallel me random fail aayenge. Maine Allure ke saath `-n 2` check kiya (results sahi aaye).

### Retry (sirf last resort)
`--reruns 1`. Allure report me retries dikhte hain (maine verify kiya). Retry se test **chhupana** nahi, flaky list banake fix karna.

### KYUN YE CHOICE?
- `schedule` nightly: poora regression raat ko, PR par sirf `smoke`. Isse developer ko fast feedback milta hai aur poori coverage bhi.
- Matrix pehle 2 browsers (chromium + firefox): zyada browser = zyada time/cost. Webkit baad me.

### AS AN SDET
Har job ka cost hota hai (time, minutes). "Sab kuch har push par" mat chalao. Fast set PR par, bhari set nightly.

### PRACTICE E8
1. `workflow_dispatch` se matrix run karo. Dono browsers ka result dekho.
2. Cron ko apne local time ke hisaab se UTC me convert karke likho.

---

## E9. CD aur "gating": tests ko merge ka darwaza banana

### CD ka matlab tumhare liye
- **Continuous Delivery:** tested build **deploy ke liye taiyar**, deploy ka button insaan dabata hai.
- **Continuous Deployment:** pass hote hi automatically deploy.
SDET ka kaam: **pipeline me aise tests rakhna jo ye faisla karein ki build aage jaye ya nahi.**

### Gating: "tests pass nahi to merge nahi"
GitHub me **branch protection / rulesets** me "Require status checks to pass before merging" aur apne workflow ka job select karte hain. Phir red CI wala PR merge nahi hota. (Settings ke exact menu names badalte rehte hain, repo **Settings** me branch rules dekho. Maine ye UI khud nahi chalaya.)

### Smoke on PR, full regression nightly
Tumhare markers (Part C) yahan kaam aate hain:
```yaml
      - name: Smoke tests (fast)
        run: pytest -m smoke -v
```
PR par `smoke`, raat ko poora. Ye production teams ka common pattern hai.

### AS A STUDENT
Sirf yaad rakho: **marker laga ke subset chalana** seekhna hi CD ke liye SDET ka pehla step hai.

### AS AN SDET
Ek flaky test jo merge rokta hai, team ka bharosa tod deta hai. Gate me sirf **stable** tests rakho. Flaky ko quarantine (alag marker, gate se bahar) karke fix karo.

---

## E10. CI failure debug karna (sabse zaroori skill)

### Routine
1. **Kaunsa step fail hua?** Run page par lal cross wala step kholo.
2. **Log neeche se upar padho.** Asli error aksar aakhir ke paas hota hai.
3. **Same command local me chalao** (jo CI me tha). Reproduce hua? To code bug hai.
4. **Local me pass, CI me fail?** To environment difference hai.
5. **Artifacts dekho:** Allure report, screenshot, trace.
6. Fix karo, push karo, dobara dekho.

### Common errors table

| Error / symptom | Likely reason | Fix |
|---|---|---|
| Workflow chala hi nahi | File galat folder, `on` branch/paths mismatch, YAML invalid | Folder, branch, `actionlint` |
| `No such file or directory` | `working-directory` galat ya `checkout` nahi | Path/step dekho |
| `Executable doesn't exist` (Playwright) | `playwright install` nahi chala | Step add karo |
| Browser launch fail / missing lib | `--with-deps` nahi | `playwright install --with-deps chromium` |
| `ModuleNotFoundError` | `requirements.txt` me package nahi | Add + pin |
| Artifact upload "No files found" | Path galat (`working-directory` galat samjha) | Repo-root se path |
| Local pass, CI fail | Timing, data, viewport, secret, timezone | Trace dekho, evidence se prove karo |
| Pages deploy "Resource not accessible" | `permissions` ya Pages source set nahi | E7 dekho |
| Python version galat | `3.10` bina quote | `"3.10"` |

### AS AN SDET
"CI fail hua" kehna kaafi nahi. **Kaunsa step, kya evidence, product bug ya test bug ya environment** ye batao. Part D5 ke 5 sawaal yahan bhi lagte hain.

### PRACTICE E10
Jaan-boojh ke 3 CI failures banao (E4 me checkout hata do, E5 me `playwright install` hata do, galat `working-directory`). Har ek ka error log padh ke root cause likho. Ye sabse tez seekhne ka tareeka hai.

---

## E11. CI ki security basics

| Rule | Kyun |
|---|---|
| Passwords/tokens **secrets** me, code ya YAML me nahi | Repo public ho sakta hai |
| `permissions: contents: read` default | Token ko kam haq |
| `state.json`, `.env` commit mat karo | Session/credentials leak |
| Report/screenshot me secret na aaye | Pages public hota hai |
| Sirf bharose wali actions (official ya jaani-maani), version tag ke saath | Third-party code tumhare token ko dekh sakta hai |
| Fork se aaye PR ko secrets nahi milte (normal behaviour) | Fork ka code tumhare secrets na padh sake |

**Advanced (baad me):** actions ko tag ki jagah **commit SHA** se pin karna sabse safe hai.

### Broken submodule cleanup (FL-6)
Tumhare `git/ci-cd-practice` pointer ko hatane ke liye:

```bash
git rm --cached git/ci-cd-practice
git commit -m "chore: remove broken submodule pointer"
git push
```
Agar wo folder asli me ek alag git repo hai jise tum alag push karna chahte ho, to usse alag GitHub repo me push karo aur is repo se hata do. Is repo me CI practice ke liye ab `.github/workflows` aur `ci-demo` hain.

### COMMON MISTAKES
- Secret ko `echo` karna (log me masked hota hai, par mat karo).
- Public Pages par real data.
- Version tag ke bina action (`@main`): koi bhi badlaav achanak aa sakta hai.

### PRACTICE E11
1. Apne repo me `grep -r "password" .` chalake dekho kahan hard-coded hai. Jo real ho wo secret me.
2. `state.json` ko `.gitignore` karke untrack karo (Part C.4).


---

# Part F: Sab Jodna: Capstone, Interview aur Confidence

## F1. Capstone: tumhara "CI-ready" repo kaisa dikhna chahiye

```text
sdet-interview-prep/                     # repo root
├── .gitignore
├── .github/
│   └── workflows/
│       ├── 01-hello.yml                 # seekhne ke liye (baad me hata sakte ho)
│       ├── 02-pytest-basic.yml
│       ├── 03-playwright-allure.yml     # tumhara main CI
│       ├── 04-publish-pages.yml         # optional
│       └── 05-matrix.yml                # optional
├── ci-demo/                             # CI mechanics ki practice
│   ├── requirements.txt
│   └── test_basic.py
└── playwright/
    └── ex_6/                            # tumhara asli framework
        ├── pages/
        ├── tests/
        ├── conftest.py                  # fixtures + Allure failure hook
        ├── pytest.ini
        ├── requirements.txt
        ├── allurerc.json
        └── README.md
```

**Ek sujhav:** `ex_6` ko `ex_6` naam se rakhne ki jagah `retailhub-playwright-framework` jaisa naam do, jab tumhara kaam stable ho jaye. Interviewer ko "ex_6" dekh ke kuch pata nahi chalta. (Rename karne par workflow ke `paths` aur `working-directory` bhi badalna.)

## F2. Kaam ka sahi order (kaun si cheez pehle)

| Step | Kya karna hai | Kahan se |
|---|---|---|
| 1 | Hygiene: `.gitignore`, `requirements.txt`, `pytest.ini`, README | FL-5, Part C |
| 2 | ex_4, ex_5 local me green | FL-1 |
| 3 | ex_6 complete (goto, sorting, parametrize, checkout end tak) | FL-2 |
| 4 | Fictional exercises (ex_1/2/3) ya to real target par ya archive | FL-3, FL-4 |
| 5 | Allure local me chalao | D1 se D6 |
| 6 | `ci-demo` GitHub par green | E3, E4 |
| 7 | ex_6 ka CI + artifacts | E5, E6 |
| 8 | Pages par report (optional) | E7 |
| 9 | Matrix / nightly (optional) | E8 |
| 10 | Broken submodule cleanup, repo public/private decision | FL-6, A.4 G11 |

**Rule:** step 2 se pehle CI ko mat chhuo. Local green nahi hai to CI sirf red dikhayega.

## F3. `ex_6/README.md` ka template (apne words me bharo)

```markdown
# RetailHub Playwright Framework (Python)

![Playwright + Allure](https://github.com/Rajitchauhan/sdet-interview-prep/actions/workflows/03-playwright-allure.yml/badge.svg)

## What this tests
SauceDemo checkout flow: login, sorting, add to cart, checkout completion.

## Stack
Python, pytest, Playwright, Allure, GitHub Actions.

## How to run locally
1. `pip install -r requirements.txt`
2. `playwright install chromium`
3. `pytest -v --alluredir=allure-results --clean-alluredir`
4. `allure generate allure-results --clean && allure open allure-report`

## Design decisions
- Page Objects for UI interaction, assertions stay in tests.
- Auth via fixture (and why).
- Evidence: screenshot on failure attached to Allure.

## Known limitations
(Honestly likho: kya cover nahi hai.)
```

Badge ka link `actions/workflows/<file>/badge.svg` format ka hai. File ka naam tumhare workflow se match hona chahiye. Public repo me badge dikhta hai.

## F4. Interview answers (CI/CD aur Allure)

Format: **simple English → strong 1–2 min answer → keywords.** Pehle upar ke concepts samjho, phir bolo.

**Q1. What is CI/CD?**
- *Simple:* CI runs build and tests automatically on every change. CD delivers or deploys tested code.
- *Strong:* "CI means every push or pull request automatically triggers a build and the test suite on a clean machine, so integration problems are found early. CD takes a tested build further, either to a ready-to-release state, which is continuous delivery, or straight to production, which is continuous deployment. As an SDET I own the test stages in that pipeline and decide which tests gate a merge, for example smoke tests on pull requests and full regression nightly."
- *Keywords:* clean runner, fail fast, gating, smoke vs regression.

**Q2. Explain your CI pipeline.**
- *Strong:* "My GitHub Actions workflow triggers on push and pull request, with path filters for my test folder. It checks out the code, sets up Python with pip caching, installs dependencies and Playwright's Chromium with system dependencies, runs pytest with Allure results, then generates the Allure report and uploads it with the Playwright traces as artifacts. Those upload steps run even when tests fail, because that is when I need the evidence."
- *Keywords:* triggers, working-directory, artifacts, `!cancelled()`, traces.
- **Sirf wahi bolo jo tumne sach me chalaya ho.**

**Q3. Why Allure over the default pytest output?**
- *Simple:* Allure shows steps, screenshots and history in one readable report.
- *Strong:* "Console output is fine for me locally, but a manager or developer needs to see which step failed, the screenshot at failure, the API response, and whether the test failed before. Allure gives structured steps, attachments, severity and feature grouping, parametrized titles, history and retries. I attach a screenshot in a pytest hook on failure, including failures that happen in fixtures."
- *Keywords:* steps, attachments, history, retries, evidence.

**Q4. A test passes locally but fails in CI. What do you do?**
- *Strong:* "I read the failing step's log from the bottom, then download the artifacts: the Allure report, screenshot and Playwright trace. I run the exact CI command locally. If it still passes, I suspect environment differences like timing, test data, viewport, timezone or a missing secret, and I confirm with the trace rather than guessing. Only after finding the root cause do I fix it, and I avoid blindly adding retries."
- *Keywords:* reproduce, trace, environment, root cause.

**Q5. How do you handle secrets in CI?**
- *Strong:* "Credentials go into repository secrets and are passed as environment variables, never committed. I keep the workflow token to least privilege with `permissions`, ignore files like storage state and `.env`, and make sure screenshots or published reports do not expose sensitive data. I also avoid putting passwords into Allure step parameters."
- *Keywords:* secrets, least privilege, `.gitignore`, no leaks in reports.

**Q6. Parallel execution aur flaky tests?**
- *Strong:* "I run with pytest-xdist when tests are independent: each test sets up its own state through fixtures. If a test depends on shared state, parallel runs expose it as random failures. I use retries only as a temporary guard and track retried tests in the Allure report, then fix the root cause."
- *Keywords:* isolation, xdist, retries, flaky tracking.

**Q7. What did you learn from reviewing your own framework?** (self-awareness answer)
- *Strong (honest):* "My early exercises had two kinds of mistakes: some code was committed without running, and some assertions checked something near the requirement instead of the requirement itself. I now run every test green before committing, check the assertion against the requirement text, and keep shared setup in conftest instead of copying it. That is why my repository now has CI that enforces the run."
- Ye answer tabhi bolo jab FL-1 se FL-5 sach me kar chuke ho.

## F5. Confidence map: kya tum sach me keh sakte ho

Confidence ka matlab hai: tum **jo bolte ho wo sach ho aur tum dikha sako.** Table ko evidence se tick karo.

| Claim | Tab bolo jab... |
|---|---|
| "Maine Playwright + pytest framework banaya" | ex_6 DoD ke saare boxes tick aur green run ho |
| "Maine POM use kiya" | Tum bata sako page object me kya aur test me kya, kyun |
| "Maine Allure report banayi" | Failure ka screenshot report me dekha ho, aur password leak wala jaal samajhte ho |
| "Maine GitHub Actions CI banayi" | Repo me green run, aur ek jaan-boojh ka red run fix kiya ho |
| "Report GitHub Pages par hai" | Link khulta ho, aur tumne socha ho kya public hai |
| "Maine parallel/matrix chalaya" | `-n` ya matrix run dekha ho |
| "Maine API + UI hybrid kiya" | FL-3 real target par green ho |

Jo tick nahi hai wo **abhi mat bolo.** Interview me ek jhooth pakda jaye to baaki sach bhi sandeh me aa jata hai.

**Abhi tumhare paas honestly:** concept level par locator scoping, POM layering, auth fixture, sorting verification. Execution level par kaam baaki hai (Part A). Ye sach hai, aur iska solution clear hai: Fix Labs.

## F6. Mujhe agla kya bhejna hai (review ke liye)

Tumhara pehle wala submission format hi use karo:

```text
Lab: FL-2

Project/Folder:
<folder structure>

Files:
<file name>

Code:
<paste your code>

Proof:
<pytest output ka last part + (agar CI hai) Actions run ka status>

Notes:
<koi design decision ya doubt>
```

Main phir wahi strict review dunga: GOOD / WRONG / RISK / IMPROVEMENT, aur repeated mistakes track karunga. **Proof** line naya hai: "green run ka output" bhejna ab zaroori hai (M1 mistake ko khatam karne ke liye).

## F7. Mistake tracker (copy karke rakho)

| Date | Lab | Galti | Kyun hui | Sahi tareeka | Dobara hui? |
|---|---|---|---|---|---|
| | | | | | |

M1 ("run kiye bina commit") agar 3 baar aaye, to wo weakness hai, alag drill banega.

## F8. Last honest note

- Ye guide tumhe **concepts, commands aur structure** deti hai. Confidence **evidence** se aati hai: green runs, report ka screenshot, CI ka tick.
- Maine jo cheezein chalaya (Allure 3, hook, YAML lint) wo verified hain. **Real browser aur real GitHub run tum karoge.** Wahi tumhara asli proof hai.
- Abhi bhi baaki (is guide me nahi): Allure history ko CI me persist karna, network mocking, frames/dialogs/popups, Docker, Jenkins. Jab JD me baar-baar dikhein tab add karo.

