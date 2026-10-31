# Module 13 — CI/CD with GitHub Actions for Playwright
## AI-Assisted Pipeline Creation, Debugging, Reports & Optimization
### Complete Hinglish Study Guide | QA Automation / SDET | Python + Pytest + Playwright

> **Module ka central focus:** Playwright project ko GitHub repository ke saath connect karke GitHub Actions workflow banana, push/PR par automated tests run karwana, reports artifacts ke roop mein upload karna, failures debug karna aur AI-assisted workflow ko carefully optimize karna.
>
> **Course instructor ka important opinion:** AI simple CI/CD tasks mein help kar sakta hai, lekin complex pipelines mein wrong advice ya hallucination se harm bhi ho sakta hai. Generated YAML ko blindly trust nahi karna.

---

## 0. ZIP inspection and source coverage

Uploaded ZIP mein 4 transcript `.txt` files aur 4 matching English subtitle `.vtt` files hain. Transcript/subtitle pairs same lesson content ko represent karte hain; duplicate content consolidate kiya gaya.

### Course source mein covered lessons

| Lesson | Course coverage |
|---|---|
| 1 | CI/CD section introduction; instructor's caution about AI limitations; GitHub Actions as the demo platform |
| 2 | Prerequisites: remote repository, Git, basic Git commands; create GitHub repository, clone locally, VS Code, optional GitHub MCP |
| 3 | Initialize Playwright project; create `npm test` script; commit/push; ask Copilot to generate GitHub Actions workflow; explain YAML triggers/jobs/steps |
| 4 | Run workflow; diagnose failure from raw logs; align installed Chromium browser with Playwright project configuration; upload Playwright report artifact |
| 5 | AI-generated workflow warnings; update deprecated action/runtime references; browser caching; verify changes; AI hallucination and official documentation reference |

**Source boundary:**
- Course demo is a **TypeScript + Playwright Test + Node.js** project.
- The optional section assumes learners already know basic CI/CD concepts.
- Course does not teach a complete Python/Pytest GitHub Actions pipeline. A Python adaptation is included separately as a mentor addition.
- The transcript mentions recording-time action versions and Node.js 20 deprecation warning. These are historical observations from that recording, not current version recommendations.
- The instructor does not claim AI is highly reliable for complex CI/CD; in fact, he explicitly warns that AI can do more harm than good on complex pipelines.

---

# Part 1 — CI/CD kya hai aur QA ke liye kyun important hai?

## 1.1 WHY: Local machine par tests pass hona enough kyun nahi?

Maan lo tumne local machine par 50 Playwright tests run kiye aur sab pass ho gaye.

Lekin:
- Developer ne new code push kar diya.
- Kisi aur developer ke changes se login flow break ho gaya.
- Tumne test run nahi kiya.
- Bug main branch mein merge ho gaya.

CI/CD ka purpose development workflow mein repeatable automated steps introduce karna hai, taaki changes par build/test checks consistently run ho sakein.

## 1.2 WHAT: CI and CD

**CI — Continuous Integration**

Developers code changes frequently shared repository mein integrate karte hain. Automated checks — build, lint, unit/integration/UI tests — changes par run ho sakte hain.

**CD — Continuous Delivery / Continuous Deployment**

- **Continuous Delivery:** Software changes deploy-ready state mein rakhe jaate hain; production deployment often approval/manual decision ke baad hota hai.
- **Continuous Deployment:** Successful changes automatically production tak deploy ho sakte hain, according to configured controls.

Course ka practical focus deployment pipeline nahi, balki **GitHub Actions mein Playwright tests run karna** hai.

## 1.3 QA engineer ke perspective se

CI pipeline mein QA automation:
- Har push par smoke/regression tests run kar sakti hai.
- Pull request par merge se pehle quality signal deti hai.
- Failures ko logs/reports ke through visible banati hai.
- Browser/environment differences detect karne mein help karti hai.
- Team ko repeatable test execution deti hai.

**Important:** CI green hona overall product quality ki guarantee nahi. Sirf configured checks pass hue hain.

---

# Part 2 — Course prerequisites: Git and remote repository

## 2.1 Course ke mutabik kya chahiye?

1. GitHub ya kisi other remote repository provider ka account.
2. Git installed.
3. Basic Git commands ki familiarity:
   - `git add`
   - `git commit`
   - `git push`
   - `git branch`
4. Local project directory.
5. VS Code (course demo environment).
6. Playwright project.

Instructor specifically recommend karta hai ki agar learner Git mein completely beginner hai, toh pehle basic Git tutorial complete kare.

## 2.2 Course workflow: repository create and clone

1. GitHub par new repository create karo.
2. Course example repository ka naam `AICICD` tha.
3. README initialize karne ka option select kiya.
4. Repository create ki.
5. HTTPS clone URL copy kiya.
6. Terminal mein repository clone ki.

```bash
git clone <repository-url>
```

7. VS Code mein cloned folder open kiya.

```bash
code <project-folder>
```

`<repository-url>` aur `<project-folder>` placeholders hain; apne actual values use karo.

## 2.3 GitHub MCP (optional course mention)

Instructor GitHub Copilot ke saath GitHub MCP install/use karne ka mention karta hai. Is module ke main hands-on workflow ke liye GitHub MCP mandatory nahi tha. Main workflow repository, Git aur GitHub Actions par based hai.

---

# Part 3 — Playwright project ready karna

## 3.1 Course demonstration

Instructor ek empty directory mein Playwright project initialize karta hai.

- Playwright project setup wizard use kiya.
- Defaults accept kiye.
- Wizard ne GitHub Actions workflow create karne ka option diya.
- Instructor ne is option par **No** select kiya, kyunki woh Copilot se workflow generate karwana chahta tha.

Project mein example test file create hui:

```text
tests/
└── example.spec.ts
```

Course ka project TypeScript Playwright Test based hai.

## 3.2 `npm test` script kyun?

Instructor `package.json` mein script add karta hai, taaki tests ko simple command se run kar sake.

Illustrative script:

```json
{
  "scripts": {
    "test": "playwright test"
  }
}
```

Ab:

```bash
npm test
```

Playwright test runner execute karega.

### `node_modules/.bin` ka role

Project dependencies install hone ke baad local executable commands `node_modules/.bin` mein available hote hain. NPM scripts local binaries ko resolve kar sakti hain, isliye `npm test` mein full executable path likhne ki zaroorat nahi hoti.

## 3.3 Local test run

Course:
1. `npm test` execute karta hai.
2. Example Playwright test run hota hai.
3. Basic tests green/pass hote hain.
4. Changes Source Control view mein visible hote hain.

**CI se pehle local run important hai:** Pipeline setup karne se pehle confirm karo ki project locally expected command se execute hota hai.

## 3.4 Changes commit/push

Course AI assistant se current changes commit and push karwata hai, taaki workflow ke liye clean starting point ho.

Typical Git sequence:

```bash
git status
git add .
git commit -m "Set up Playwright project"
git push
```

Ye illustrative Git workflow hai. Commit karne se pehle `git status` aur staged diff review karo.

---

# Part 4 — GitHub Actions workflow generate karna

## 4.1 Course prompt

Instructor GitHub Copilot ko prompt deta hai:

```text
Generate a GitHub Actions workflow for this project.
```

Copilot project structure inspect karke workflow create karta hai.

Generated location:

```text
.github/
└── workflows/
    └── [workflow-name].yml
```

**Important:** GitHub Actions workflow YAML files `.github/workflows/` folder ke andar hoti hain.

## 4.2 Workflow ke main building blocks

Course instructor workflow file ko AI se explain karwata hai aur key concepts identify karta hai.

| Concept | Meaning |
|---|---|
| Trigger / `on` | Workflow kab run hoga |
| Job | Logical unit of work |
| Runner | Machine/environment jahan job run hota hai |
| Step | Job ke andar individual action/command |
| Action | Reusable unit, e.g. checkout/setup |
| Artifact | Workflow output file/report jo upload/store hoti hai |

## 4.3 Trigger — workflow kab run hoga?

Course example:
- Main branch par push.
- Main branch ke against pull request.

Conceptual YAML:

```yaml
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
```

Iska matlab:
- `main` par push hua toh workflow run.
- `main` ko target karne wala pull request update hua toh workflow run.

Course instructor unnecessary `master` branch entry remove karta hai, kyunki uski repository mein `main` enough tha.

**Mentor note:** Apne repository ka actual default/target branch use karo. Branch name assume mat karo.

## 4.4 Job and runner

Course workflow job Ubuntu latest runner par run hota hai.

Conceptual structure:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
```

Meaning:
- `jobs` ke andar `test` job define hai.
- `runs-on` batata hai job kis runner environment par execute hoga.
- GitHub-hosted runner ek fresh virtual machine/environment provide karta hai.

**Important:** Fresh runner ka matlab local machine ke installed dependencies/browser automatically available nahi. Workflow ko required setup repeat karna padta hai.

## 4.5 Steps — course workflow ka sequence

Course workflow mein ye steps hain:

1. Repository code checkout.
2. Node.js environment setup.
3. Dependencies clean install.
4. Playwright browser install.
5. Playwright tests run.
6. Playwright report artifact upload.

### Step 1 — Checkout repository

Course example action `actions/checkout` use karta hai.

Purpose:
- Runner machine par repository source code available karna.
- Without checkout, job ko project files nahi milengi.

### Step 2 — Setup Node.js

Course project Node.js/TypeScript based hai.

Purpose:
- Runner par required Node.js environment configure karna.
- NPM commands execute karne layak environment banana.

### Step 3 — Clean install

Course instructor `npm ci` / clean install ko CI ke liye preferred batata hai, normal `npm install` ke comparison mein.

```bash
npm ci
```

High-level:
- Lockfile-based dependency installation.
- CI mein repeatable dependency installation ke liye suitable.
- Lockfile aur package metadata mismatch ho toh fail ho sakta hai.

### Step 4 — Playwright browsers install

Course mein browser installation ek time-consuming step tha.

Playwright tests ko browser binaries ki zaroorat hoti hai. Runner par browser install karna hota hai.

Course initially browser install step mein Chromium-only approach try karta hai, taaki other browsers download na karne padein.

### Step 5 — Tests run

Course script:

```bash
npm test
```

### Step 6 — Report upload

Course workflow Playwright report upload karta hai, taaki GitHub Actions job ke Artifacts section se download ki ja sake.

---

# Part 5 — Browser installation aur Playwright configuration mismatch

## 5.1 Course mein actual failure kya hua?

Instructor ne workflow ko modify karke sirf Chromium browser download karwaya.

Lekin project ke Playwright configuration mein tests three browser projects ke liye configured the.

Result:
- Workflow ne sirf Chromium install kiya.
- Playwright tests Chromium ke alawa other configured browsers ke liye bhi run karne lage.
- Required browser binaries absent the.
- GitHub Actions job fail ho gaya.

## 5.2 Root cause

<badge color="warning">Course ka actual debugging lesson</badge>

**Workflow installation scope aur Playwright project configuration aligned nahi the.**

| Workflow | Playwright config | Outcome |
|---|---|---|
| Only Chromium installed | Chromium + Firefox + WebKit projects | Missing browsers ke karan failure |
| Only Chromium installed | Only Chromium project | Browser configuration aligned |

## 5.3 Course fix

Instructor ne AI ko prompt diya:

```text
Update the Playwright configuration to only run Chromium.
```

Copilot ne other browser projects remove kar diye.

Then:
1. Change review/accept kiya.
2. Commit/push kiya.
3. New workflow run hua.
4. Tests successful hue.
5. Job green hua.

### Mentor warning

Agar project ka requirement cross-browser testing hai, toh sirf CI ko green karne ke liye Firefox/WebKit projects delete mat karo.

Correct decision:
- Agar pipeline intentionally Chromium smoke suite hai, config scope align karna acceptable ho sakta hai.
- Agar release gate mein cross-browser testing required hai, toh all required browsers install karo.

**Pipeline ko test strategy ke according configure karo, test strategy ko pipeline ki convenience ke liye weaken mat karo.**

---

# Part 6 — GitHub Actions failure logs and artifacts

## 6.1 Course workflow failure investigate kaise hua?

Instructor:
1. GitHub repository par Actions tab open karta hai.
2. Failed workflow run select karta hai.
3. Job details inspect karta hai.
4. `View raw logs` open karta hai.
5. Complete logs select/copy karta hai.
6. Logs AI assistant ko deta hai.
7. Copilot root cause identify karta hai: Chromium-only install vs three-browser configuration.

## 6.2 Good debugging process

AI se poochhne se pehle:
- Failed step identify karo.
- First meaningful error locate karo.
- Relevant lines collect karo.
- Runner OS, runtime and browser config note karo.
- Error ke pehle ke setup steps bhi inspect karo.

### Better prompt — mentor addition

```text
Analyze these GitHub Actions logs.

Please:
1. Identify the first meaningful failure.
2. Separate the direct error from later cascading errors.
3. Explain which workflow step failed.
4. Compare the installed browser/runtime with the project configuration.
5. Give the most likely root cause and supporting log evidence.
6. Suggest the smallest safe fix.
7. Do not remove tests or weaken the test configuration just to make CI green.
8. If current action/runtime documentation is needed, ask for or use an official current reference.

Logs:
[PASTE RELEVANT LOGS]
```

## 6.3 Playwright HTML report

Course instructor locally Playwright report open karke dekhta hai:
- Kaunse tests run hue.
- Kaunse pass hue.
- Kaunse fail hue.
- Failure details.

## 6.4 Artifact kya hota hai?

Artifact workflow ke run se produce hui file/output hoti hai jo GitHub Actions job ke saath upload/store ki ja sakti hai.

Course example:
- Playwright HTML report.
- GitHub Actions run ke Artifacts section mein report available.
- User report download kar sakta hai.
- Local aur CI results compare/debug kar sakta hai.

**Important distinction:**
- Workflow logs = execution steps and command output.
- Test report = structured test execution details.
- Artifact = uploaded output file(s) preserved with the run.

---

# Part 7 — AI-generated workflow ko review karna

## 7.1 Course ka actual warning: generated code outdated ho sakta hai

Course ke next lesson mein workflow annotations warning dikhati hain ki Node.js 20 deprecated hai (recording-time warning).

Instructor warning copy karke Copilot ko deta hai.

Copilot suggest karta hai:
- Checkout action update.
- Setup Node action update.
- Upload artifact action update.

Instructor action versions update karta hai, commit/push karta hai aur workflow green verify karta hai.

**Historical note:** Recording mein action versions v4 se v7 update hone ka mention hai, aur instructor ko ek action ke liye v6/v7 ka uncertainty tha. Ye current latest versions ki recommendation nahi hai. Current official action repositories/release notes se exact version verify karo.

## 7.2 AI hallucination — course ka important example

Instructor Copilot se workflow optimization poochta hai.

AI incorrectly claim karta hai ki newer action versions exist nahi karte aur v4 latest stable hai.

Instructor is advice ko reject karta hai, kyunki:
- AI training data stale ho sakta hai.
- Model ko current release knowledge nahi ho sakti.
- Confident answer bhi wrong ho sakta hai.

**Course ka direct lesson:** Generated YAML aur AI review dono verify karna zaroori hai.

## 7.3 Better approach: official documentation as reference

Instructor:
1. Web browser open karta hai.
2. GitHub Actions caching dependencies ki official documentation search karta hai.
3. Official docs URL copy karta hai.
4. AI assistant ko prompt deta hai ki is URL ko reference ke roop mein use karo.
5. AI caching solution suggest karta hai.
6. Instructor change apply karta hai.
7. Commit/push karke actual workflow verify karta hai.

**Lesson:** Time-sensitive CI/CD details ke liye model memory par rely mat karo. Official current documentation use karo.

---

# Part 8 — Playwright browser caching

## 8.1 WHY: Browser install step slow kyun hota hai?

Course ke run mein Playwright browser installation noticeable time leta tha.

CI runner fresh environment par start hota hai, isliye browser binaries repeat download karne pad sakte hain.

Caching ka purpose:
- Reusable downloaded browser files preserve karna.
- Subsequent workflow runs mein installation/download overhead reduce karna.
- Pipeline execution time improve karna.

## 8.2 Course result

Instructor comparison:

| Step | Before caching | After caching |
|---|---:|---:|
| Install Playwright browsers | 22 seconds | 0 seconds |
| Install Playwright system dependencies | — | 12 seconds |

Instructor ne approximately 10 seconds ka net saving mention kiya.

**Caveat:** Ye specific course run ka measurement hai, guaranteed result nahi. Cache hit/miss, runner, browser version, dependency changes aur cache configuration se timings vary karengi.

## 8.3 Caching kya preserve kar sakti hai?

Course mein Playwright browser caching focus hai.

Mentor explanation:
- Cache key ko OS/browser/Playwright version ke saath align karna important ho sakta hai.
- Browser version change hone par stale cache use nahi hona chahiye.
- Cache hit/miss logs inspect karo.
- System dependencies browser binaries se separate concern hain; caching browser download ka matlab OS packages automatically cached/installed hona nahi.

Exact implementation current official Playwright and GitHub Actions docs se verify karo.

---

# Part 9 — Python + Pytest + Playwright adaptation

> **Important:** Course ka workflow TypeScript/Node.js Playwright Test project par based hai. Neeche Python + Pytest + Playwright example mentor adaptation hai; ye uploaded transcript ka original workflow nahi.

## 9.1 Python project mein CI ka conceptual sequence

```text
Git push / Pull Request
          |
          v
GitHub Actions runner
          |
          v
Checkout repository
          |
          v
Set up Python
          |
          v
Install Python dependencies
          |
          v
Install Playwright browsers/dependencies
          |
          v
Run pytest
          |
          v
Generate report
          |
          v
Upload report/artifacts
```

## 9.2 Example Python workflow structure

Illustrative YAML — action versions and Python version should be checked against your project and current official documentation before use.

```yaml
name: Python Playwright Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@<VERIFIED_VERSION>

      - name: Set up Python
        uses: actions/setup-python@<VERIFIED_VERSION>
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Install Playwright browser
        run: |
          python -m playwright install --with-deps chromium

      - name: Run pytest
        run: |
          pytest -v

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@<VERIFIED_VERSION>
        with:
          name: pytest-results
          path: |
            test-results/
            report.html
          if-no-files-found: ignore
```

### Is example ko samjho

- `on`: push/PR triggers.
- `jobs.test`: test job.
- `runs-on`: Ubuntu runner.
- Checkout: repository files.
- Setup Python: Python runtime.
- `pip install`: dependencies.
- `playwright install --with-deps chromium`: Chromium and required OS dependencies.
- `pytest -v`: test execution.
- `if: always()`: test fail hone par bhi artifact upload step attempt ho.
- Upload artifact: report/results preserve.

**Important:** `report.html` tabhi upload hoga jab tumne HTML reporting plugin/config install kiya ho aur report generate ki ho. Example path apne actual project output se match karo. `test-results/` bhi project ke configured output directory se match hona chahiye.

## 9.3 Python `requirements.txt` example

Illustrative:

```text
pytest
pytest-playwright
playwright
pytest-html
```

Actual project ke pinned versions aur lock/dependency management approach follow karo. CI mein reproducible dependencies ke liye exact versions/lockfile use karna useful hai.

## 9.4 Python report generate karna

Agar `pytest-html` use kar rahe ho:

```bash
pytest -v --html=report.html --self-contained-html
```

CI workflow mein test command accordingly update karo.

**Mentor note:** HTML report plugin optional hai. Playwright trace/video/screenshots configure karne ke liye separate pytest-playwright/Playwright settings use ho sakti hain.

---

# Part 10 — CI/CD troubleshooting checklist

| Symptom | Possible cause | What to inspect |
|---|---|---|
| Workflow not triggered | Wrong branch/event filters | `on.push`, `on.pull_request`, branch names |
| Checkout failure | Repository permissions/token | Checkout step logs, permissions |
| Node/Python command missing | Runtime setup absent/wrong | Setup step and runtime version |
| Dependency install fails | Lockfile mismatch/package conflict | `npm ci`/pip logs |
| Browser executable missing | Browser install missing or mismatch | Playwright version and installed browsers |
| Only Chromium installed but Firefox tests run | Browser/config mismatch | Playwright projects and install command |
| Tests pass locally but fail in CI | OS, viewport, timing, env, data differences | First failure, traces, screenshots, env |
| Report not uploaded | Wrong path or upload step skipped | Artifact path, `if`, previous step result |
| Deprecated action warning | Old action/runtime version | Annotation URL and official release docs |
| Pipeline slow | Repeated downloads/install, unnecessary browser matrix | Cache, scope, parallelism, setup time |
| AI suggests old action versions | Stale model knowledge | Current official GitHub docs |
| Cache doesn't hit | Key mismatch/OS/version changes | Cache key and logs |

---

# Part 11 — AI-assisted CI/CD: safe usage rules

Course instructor strongly cautions that AI assistance for CI/CD is limited, especially for complex pipelines.

## AI se kya karwa sakte ho?

- Basic workflow skeleton generate karna.
- YAML explain karwana.
- Simple syntax issue identify karwana.
- Raw logs summarize karwana.
- Missing setup step suggest karwana.
- Official docs ke basis par caching proposal lena.

## AI ko blindly kya nahi karna dena chahiye?

- Production deployment permissions modify.
- Secrets/credentials expose.
- Test matrix delete/disable.
- Assertions/tests remove.
- Security permissions broad karna.
- Unknown third-party actions add karna.
- Outdated action versions recommend karna.
- Pipeline green karne ke liye quality gate weaken karna.

## Strong AI review prompt — mentor addition

```text
Review this GitHub Actions workflow for a Playwright test project.

Do not modify it yet.

Analyze:
1. Trigger conditions and target branches.
2. Runner and runtime setup.
3. Dependency installation and lockfile usage.
4. Playwright version and browser installation alignment.
5. Test command and browser project matrix.
6. Report generation and artifact upload.
7. Caching opportunities.
8. Permissions and secret exposure.
9. Deprecated action/runtime warnings.

For every finding:
- Quote the relevant YAML section.
- Explain the risk.
- Label it as confirmed issue or recommendation.
- Cite current official documentation for version-sensitive claims.

Do not remove tests, reduce browser coverage or weaken quality gates just to make the workflow pass.
```

---

# Part 12 — Interview preparation

## Q1. What is CI/CD?

**Simple English:**

“CI/CD automates software integration, validation and delivery workflows. In QA, it helps execute automated tests on code changes and provides feedback before changes are merged or released.”

**Stronger answer:**

“Continuous Integration means developers integrate changes into a shared repository frequently, with automated checks such as builds and tests. Continuous Delivery keeps changes deploy-ready, while Continuous Deployment can automatically release successful changes. As a QA automation engineer, I contribute by integrating smoke, regression and other automated tests into the pipeline, reviewing failures and providing reports as quality feedback.”

## Q2. What is GitHub Actions?

“GitHub Actions is a GitHub automation platform where workflows defined in YAML can run in response to repository events such as pushes and pull requests.”

## Q3. What is a workflow, job, runner and step?

- Workflow: YAML-defined automation.
- Job: Group of steps.
- Runner: Machine/environment that executes a job.
- Step: Individual action or command within a job.

## Q4. Why use `npm ci` in CI?

“`npm ci` performs a clean, lockfile-based dependency installation and is suited to repeatable CI environments. It helps ensure the pipeline uses the dependency versions recorded in the lockfile.”

## Q5. What is an artifact?

“An artifact is a file or output uploaded from a workflow run, such as a Playwright HTML report, which can be downloaded later for investigation.”

## Q6. How do you debug a failing GitHub Actions test?

“I open the failed workflow run, identify the failed job and first meaningful error in the logs, then compare the runner setup, dependencies, browser installation and Playwright configuration. I also inspect reports, screenshots or traces if available. I fix the root cause rather than weakening the test.”

## Q7. Why did the course pipeline fail after installing only Chromium?

“The workflow installed only Chromium, but the Playwright configuration still had three browser projects. Tests attempted to run in browsers that were not installed. The course aligned the project configuration to Chromium for that specific pipeline.”

## Q8. What is caching in CI?

“Caching stores reusable dependencies or browser files between workflow runs so they do not need to be downloaded every time. Cache keys must account for relevant version changes to avoid using stale files.”

## Q9. Would you trust AI-generated CI/CD YAML?

“No. I use AI for a first draft or to explain logs, but I review triggers, permissions, dependency setup, browser matrix, artifacts and action versions. The course demonstrates that AI can hallucinate outdated action-version information, so I verify time-sensitive details against official documentation.”

---

# Part 13 — Practical assignments

## Assignment 1: GitHub Actions basics

1. Create a GitHub repository.
2. Clone it locally.
3. Create a Playwright project.
4. Add an `npm test` script.
5. Run tests locally.
6. Commit and push.

**Pass condition:** Local test command works before CI setup.

## Assignment 2: Generate a workflow

Ask Copilot to create a GitHub Actions workflow.

Manually inspect:
- Trigger.
- Job.
- Runner.
- Checkout.
- Runtime setup.
- Dependency installation.
- Browser install.
- Test execution.
- Artifact upload.

## Assignment 3: Reproduce browser mismatch

1. Configure project for Chromium + Firefox + WebKit.
2. Install only Chromium in CI.
3. Observe failure.
4. Decide whether CI should install all browsers or this job should intentionally target Chromium.
5. Make the correct change based on test strategy.

## Assignment 4: Debug raw logs

1. Open a failed workflow run.
2. Find first meaningful error.
3. Copy relevant logs.
4. Ask AI to analyze.
5. Independently verify diagnosis.
6. Apply minimal safe fix.
7. Rerun.

## Assignment 5: Browser cache

1. Record baseline browser installation time.
2. Add caching based on official current documentation.
3. Run workflow again.
4. Compare cache hit/miss and elapsed time.
5. Confirm browser version changes invalidate/refresh cache as appropriate.

## Assignment 6: Python adaptation

Build a GitHub Actions workflow for your Python + Pytest + Playwright project:
- Setup Python.
- Install dependencies.
- Install Chromium with system dependencies.
- Run pytest.
- Generate report.
- Upload report even when tests fail.

## Assignment 7: AI hallucination test

Ask AI for current GitHub Actions action versions without giving it current documentation. Then verify its answer against official repositories/docs.

**Learning objective:** Learn to detect confident but outdated AI suggestions.

---

# Part 14 — Module 13 quick revision

| Concept | One-line revision |
|---|---|
| CI | Frequently integrate code and run automated validation |
| CD | Continuous Delivery/Deployment |
| GitHub Actions | GitHub workflow automation platform |
| Workflow | YAML-defined automation |
| Trigger | Event that starts workflow |
| Job | Unit of work in workflow |
| Runner | Machine/environment executing job |
| Step | Individual action/command |
| Checkout | Get repository source on runner |
| Runtime setup | Configure Node/Python environment |
| `npm ci` | Clean lockfile-based Node dependency install |
| Playwright browser install | Install browser binaries required by tests |
| Artifact | Uploaded workflow output, e.g. report |
| Raw logs | Execution details used for debugging |
| Cache | Reuse downloads/dependencies between runs |
| Browser matrix alignment | Installed browsers must match configured test projects |
| AI hallucination | Confident but unsupported/incorrect suggestion |

## 15 questions — notes band karke answer karo

1. CI aur CD mein difference kya hai?
2. QA engineer ke liye CI pipeline kyun useful hai?
3. GitHub Actions workflow file kahan hoti hai?
4. Trigger, job, runner aur step kya hote hain?
5. Checkout action ka purpose?
6. Runtime setup step kyun required hai?
7. CI mein `npm ci` kyun use karte hain?
8. Playwright browsers install karna kyun zaroori hai?
9. Chromium-only installation ke saath three-browser config fail kyun hua?
10. Artifact kya hai aur report upload kyun useful hai?
11. Raw logs se failure debug kaise karoge?
12. Browser caching kya improve karti hai?
13. Cache key/version alignment kyun important hai?
14. AI-generated YAML mein kya review karoge?
15. AI ke outdated action-version suggestion ko kaise verify karoge?

---

# Part 15 — Module progress tracker

| Topic | Status |
|---|---|
| CI/CD concepts | ⬜ |
| GitHub/Git prerequisites | ⬜ |
| Repository clone and project setup | ⬜ |
| Playwright project and `npm test` | ⬜ |
| Git commit/push | ⬜ |
| GitHub Actions workflow structure | ⬜ |
| Triggers | ⬜ |
| Jobs and runners | ⬜ |
| Checkout and runtime setup | ⬜ |
| Clean dependency installation | ⬜ |
| Playwright browser installation | ⬜ |
| Test execution | ⬜ |
| Browser configuration mismatch debugging | ⬜ |
| Raw logs investigation | ⬜ |
| Playwright report artifact | ⬜ |
| Action/runtime deprecation warnings | ⬜ |
| Browser caching | ⬜ |
| AI hallucination awareness | ⬜ |
| Python + Pytest adaptation | ⬜ |
| Practical assignments | ⬜ |
| Interview answers | ⬜ |

### Mentor scoring rubric

- **0 — Unknown:** CI/CD and workflow structure explain nahi kar pa rahe.
- **1 — Basic:** Trigger/job/runner/step identify kar sakte ho.
- **2 — Working:** Playwright test pipeline create/run/debug kar sakte ho.
- **3 — Strong:** Browser matrix, artifacts, cache, logs, security and AI-generated workflow risks evaluate kar sakte ho.

**Module complete tab hoga jab tum ek working Playwright CI pipeline create kar sako, intentional browser mismatch diagnose kar sako, failure logs se root cause identify kar sako aur report artifact download kar sako.**

---

# Final mentor note

Module 13 ka most important lesson sirf GitHub Actions YAML banana nahi hai.

Real QA/SDET understanding:
1. Tests local aur CI dono environments mein run hone chahiye.
2. Runner fresh machine hoti hai; required runtime/dependencies/browser install karne hote hain.
3. Playwright config aur installed browser set aligned hona chahiye.
4. Failure par raw logs, reports aur artifacts inspect karne chahiye.
5. Caching pipeline ko faster bana sakti hai, but stale cache risk consider karo.
6. AI generated YAML ko review karo; current action versions official docs se verify karo.

**Course instructor ki warning ko seriously lo:** AI se CI/CD ka first draft lena useful ho sakta hai, lekin complex pipeline ka ownership aur validation engineer ki responsibility hai.
