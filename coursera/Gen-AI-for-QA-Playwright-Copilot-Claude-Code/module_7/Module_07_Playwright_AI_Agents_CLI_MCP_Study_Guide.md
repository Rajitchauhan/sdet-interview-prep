# Module 10 — Playwright AI Agents, Playwright CLI, MCP & Skills
## Complete Hinglish Study Guide | Python + Pytest + Playwright | QA Automation / SDET

> **Module ka central focus:** Playwright ecosystem ke AI features — Playwright Test Agents (Planner, Generator, Healer), Playwright CLI, skills, MCP aur in approaches ka practical comparison.

---

## 0. ZIP inspection and source coverage

Uploaded ZIP mein:
- 8 transcript `.txt` files
- 8 matching English subtitle `.vtt` files
- Total 16 files

Transcript aur subtitle pairs ka spoken content match karta hai. Ek subtitle/transcript section token-efficient DOM snapshots explain karta hai; baaki main lessons Playwright AI section, Test Agents setup, Planner/Generator/Healer workflows, Playwright CLI setup/use aur MCP-vs-CLI token comparison cover karte hain.

| Lesson | Course source mein kya cover hai |
|---|---|
| 1 | Playwright AI features ka introduction; optional section; TypeScript demo, Python/Java learners follow along kar sakte hain |
| 2 | Playwright snapshots ka simplified structure aur token-saving purpose |
| 3 | Playwright Test Agents: Planner, Generator, Healer; installation and generated project files |
| 4 | Planner se test plan; Generator se selected test cases; Healer se broken tests repair |
| 5 | Playwright CLI, token-efficiency idea, Node.js 20+, global installation, skills installation |
| 6 | Playwright CLI se test plan, test generation aur test repair |
| 7 | Playwright MCP vs CLI token comparison using same browser task |

**Source boundary:** Course demo TypeScript Playwright project aur pizza-store app (`localhost:3000`) par based hai. Tum Python + Pytest + Playwright use karte ho, isliye Python examples/adaptations ko “Mentor adaptation” mark kiya hai. Course transcript Python-specific Test Agents setup/code demonstrate nahi karta.

**Version caveat:** Instructor apni recording ke waqt available commands, agents, tool counts aur client support batata hai. Ye values change ho sakti hain. Install karne se pehle current official Playwright documentation check karna; transcript ke command fragments ko blindly copy mat karna.

---

# Part 1 — Playwright AI features: overview

## 1.1 WHY: Playwright ke AI features kyun?

Traditional automation mein tester ko:
1. Application explore karni hoti hai.
2. Test scenarios identify karne hote hain.
3. Test cases likhne hote hain.
4. Tests execute karne hote hain.
5. Failures investigate karke code fix karna hota hai.

AI-assisted Playwright workflow in steps ko accelerate kar sakta hai:
- Application explore karna.
- Markdown test plan draft karna.
- Test plan se tests generate karna.
- Failing test mein likely issue identify karke repair propose/apply karna.

**Important:** AI feature tester ka replacement nahi hai. Requirements, coverage, assertions, test data aur final verification tumhari responsibility hai.

## 1.2 Course ke teen Test Agents

<box border radius="lg" padding={3} gap={3}>
  <row align="center" gap={3}>
    <icon name="clipboard-list" size="2xl"/>
    <box flex="1" gap={1}>
      **1. Planner Agent**
      <text color="secondary" size="sm">Application explore karke Markdown test plan banata hai.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="center" gap={3}>
    <icon name="code" size="2xl"/>
    <box flex="1" gap={1}>
      **2. Generator Agent**
      <text color="secondary" size="sm">Test plan/scenario ke basis par Playwright tests generate karta hai.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="center" gap={3}>
    <icon name="wrench" size="2xl"/>
    <box flex="1" gap={1}>
      **3. Healer Agent**
      <text color="secondary" size="sm">Failing/broken Playwright tests inspect karke repair karta hai.</text>
    </box>
  </row>
</box>

### End-to-end workflow

```text
Running application
       |
       v
Planner Agent
       |
       v
Markdown test plan
       |
       v
Generator Agent
       |
       v
Playwright test files
       |
       v
Run and review tests
       |
       v
Test fails?
       |
       v
Healer Agent
       |
       v
Review fix + rerun independently
```

**Mentor note:** Healer ka goal test ko green karna bhar nahi hona chahiye. Agar requirement, application ya test expectation hi wrong hai, blindly test ko modify karna defect ko hide kar sakta hai.

---

# Part 2 — Playwright snapshots and token efficiency

## 2.1 WHY: Full webpage AI ko kyun nahi bhejni chahiye?

Ek webpage mein bahut saara HTML/DOM content ho sakta hai. Agar AI agent ko har interaction par poora page content bheja jaye, toh context/token consumption badh sakti hai.

Course explain karta hai ki Playwright ke snapshots page ka simplified representation provide karte hain. Ye structure preserve karte hue unnecessary details reduce karne mein help karte hain.

## 2.2 WHAT: Snapshot mein kya dikh sakta hai?

Course transcript ke examples:
- ARIA role.
- Stable ID/reference.
- Attributes jaise `pointer`, `active`, `level`.
- Text content.
- Simplified structure of the page.

Ye snapshot browser page ka complete raw HTML dump nahi hota. Course ka point hai ki AI tools ko interaction ke liye useful structure mil sake, while tokens save ho sakte hain.

Illustrative simplified snapshot:

```text
- heading "Pizza Menu" [level=1]
- button "Change theme"
- textbox "Search pizzas"
- list:
  - listitem "Margherita"
  - listitem "Pepperoni"
```

**Note:** Ye teaching example hai, course se copied exact snapshot output nahi.

## 2.3 Tumhe snapshot internals kitne samajhne hain?

Course instructor kehta hai ki in files ka internal format deeply samajhna mandatory nahi; project mein generated files dikh sakti hain aur unka purpose token/context efficiency samajhna hai.

As a QA engineer, tumhe itna samajhna chahiye:
- Snapshot browser state ka simplified view hai.
- AI agent isse elements identify kar sakta hai.
- Snapshot complete requirement/test oracle nahi hai.
- Actual assertions still expected behaviour validate karte hain.

---

# Part 3 — Playwright Test Agents install karna

## 3.1 Course prerequisites and setup

Course demo:
- Existing Playwright project.
- Application already running.
- VS Code + GitHub Copilot, or supported alternative AI coding environment.
- Playwright package/tooling.

Instructor recording ke waqt teen agents available batata hai:
- Planner.
- Generator.
- Healer.

Course `init agents` workflow use karta hai aur environment/client ke liye loop specify karta hai. Transcript mein examples:
- `vscode` loop — GitHub Copilot in VS Code.
- Claude Code ke liye Claude loop.
- Codex / OpenCode ke liye respective loops.

**Important:** Ye course recording ke waqt ka support matrix hai, permanent/current compatibility guarantee nahi. Current Playwright docs se exact command, loop spelling aur supported clients verify karo.

## 3.2 Course-generated files

Instructor ke VS Code project mein generated files/folders:

```text
project/
├── .github/
│   ├── agents/
│   │   ├── planner agent file
│   │   ├── generator agent file
│   │   └── healer agent file
│   └── workflows/
├── .vscode/
│   └── mcp.json
└── seed.spec.ts
```

Ye conceptual tree hai. Exact file names aur folder contents package/version ke hisaab se differ kar sakte hain.

### Agent Markdown files mein kya tha?

Course ke mutabik:
- Agent name.
- Tools list.
- Model selection.
- MCP server configuration/reference.
- Instructions — agent kya karega.

Course highlight: Agents under the hood Playwright MCP tools use karte hain.

### Custom instructions ka example

Instructor ko snapshot tests pasand nahi the, kyunki unke experience mein unstable ho sakte hain. Isliye unhone generator instructions mein add kiya:

- Snapshot testing generate/use mat karo.
- Assertions use karo.

**Important nuance:** Ye instructor ki personal preference hai, universal testing law nahi. Snapshot tests kuch situations mein useful ho sakte hain, lekin unka maintenance, review aur brittleness assess karna chahiye. Business behaviour ke liye explicit assertions often clearer hoti hain.

### `workflows/` folder

Course ke mutabik generated workflows CI/CD workflow mein usable ho sakte hain. Is lecture mein instructor ne workflows ka detailed explanation nahi diya; isliye unka exact behaviour assume nahi karna chahiye.

### `.vscode/mcp.json`

VS Code + GitHub Copilot environment ke liye Playwright MCP configuration.

Instructor ne server start karke tools install/list hote dekhe. Recording mein 86 tools ka mention hai — **ye recording-time tool count hai, current fixed count nahi.**

### `seed.spec.ts`

Course ke mutabik, seed file bootstrap execution ke liye ready-to-use page context provide karne mein help karti hai. Complex setup/POM projects mein relevant ho sakti hai. Instructor ke simple demo app mein iska practical role minimal tha.

## 3.3 Common mistakes

- Apne AI client ke liye wrong loop select karna.
- Current documentation verify kiye bina old install command chalana.
- Generated agent instructions ko review na karna.
- Agent ko unnecessary tools/permissions dena.
- Seed file ko samjhe bina delete/modify kar dena.
- Course ke 86 tools ko current package count samajhna.

---

# Part 4 — Planner Agent in action

## 4.1 Course workflow

Prerequisite: pizza application terminal mein already running thi.

Instructor ne:
1. GitHub Copilot mein **Playwright Test Planner** select kiya.
2. Prompt diya: application ke liye test plan generate karo.
3. Test plan ko `.md` file mein save karne ko kaha.
4. Agent ne Playwright MCP call invoke ki.
5. Browser start hua.
6. Instructor ne MCP calls approve ki.
7. Application explore hui.
8. Test plan `specs` folder mein create hua.
9. Markdown preview mein menu display aur other application features ke scenarios dekhe.

### Real application ke liye instructor ki advice

Demo app chhoti thi, isliye full application plan ek prompt mein generate kiya. Real application mein:
- Puri application ko ek hi task mein explore karwana avoid karo.
- Feature/module ke basis par scope narrow karo.
- Example: login, add to cart, checkout.
- Chhote scope se agent ka task focused rehta hai.

## 4.2 Better Planner prompt — mentor adaptation

```text
Use the Playwright Test Planner agent.

Explore only the login functionality of the running application.

Create a Markdown test plan in the specs folder.

Include:
1. Observed UI elements and available actions.
2. Positive scenarios.
3. Negative scenarios.
4. Validation and boundary scenarios supported by the UI/requirements.
5. Preconditions and test data.
6. Open questions where behaviour is unclear.

Do not invent business rules.
Do not modify application data.
Clearly distinguish observed behaviour from assumptions.
```

## 4.3 Planner output ko kaise review karein?

- Kya agent ne correct feature explore ki?
- Kya login ke positive/negative paths cover hue?
- Kya assumptions clearly marked hain?
- Kya acceptance criteria ke against traceability hai?
- Kya security-relevant cases (e.g., invalid credentials) included hain?
- Kya test plan mein unsupported behaviour invent toh nahi hua?

**Remember:** Planner UI explore karke observations nikal sakta hai; woh hidden business rules automatically know nahi karta.

---

# Part 5 — Generator Agent in action

## 5.1 Course workflow

1. Planner ka generated test plan open kiya.
2. Test plan ko agent context mein include kiya.
3. Playwright Test Generator agent select kiya.
4. Entire app ke tests ek saath generate karne ke bajay sirf first feature — menu display — select kiya.
5. Agent ne Playwright MCP ke through browser interact kiya.
6. Tests generate hue.
7. Agent ne generated tests execute bhi kiye.
8. Instructor ne khud tests run karke verify kiya.
9. Generated tests mein menu display aur pizza images gracefully fail/not-found behaviour jaise checks dekhe.

Course transcript mein ek MCP call ke dauran “text not found” type output aaya, lekin browser interaction/tests phir bhi kaam kar rahe the. Iska matlab ye nahi ki har MCP error harmless hota hai; output aur actual execution result separately verify karo.

## 5.2 Mentor addition — Python + Pytest + Playwright equivalent

Course test code TypeScript mein tha. Tumhari Python stack ke liye illustrative adaptation:

```python
from playwright.sync_api import Page, expect


def test_menu_heading_is_visible(page: Page):
    page.goto("http://localhost:3000")

    expect(
        page.get_by_role("heading", name="Pizza Menu")
    ).to_be_visible()
```

**Note:** `"Pizza Menu"` aur URL illustrative hain. Actual page text, route aur test fixture project ke hisaab se verify karna hoga.

### Generator review checklist

| Area | Review question |
|---|---|
| Test scope | Sirf requested feature ke tests generate hue? |
| Locator | Role/label/test-id based stable locator hai? |
| Assertion | User-visible/business outcome verify ho raha hai? |
| Test data | Deterministic hai? |
| Waits | Fixed sleeps avoid kiye? |
| Isolation | Test independent hai? |
| Fixtures | Existing pytest fixtures reuse hue? |
| POM | Project conventions follow hui? |
| Negative paths | Relevant failure cases cover hue? |
| Side effects | Real orders/payments/data mutation toh nahi? |

---

# Part 6 — Healer Agent in action

## 6.1 Course demonstration

Instructor ne intentionally generated tests ko break kiya:
- Ek expected count mein typo/value change ki.
- Heading locator ko button locator se replace kiya.
- Ek aur typo introduce ki.

Then:
1. New conversation start ki.
2. Playwright Test Healer agent select kiya.
3. Broken menu display test ko context mein diya.
4. Prompt diya: “Fix this test.”
5. Healer ne wrong count aur typo identify ki.
6. Wrong role — heading vs button — bhi identify kiya.
7. Test repair hua.

Course ka demonstration intentionally broken test ko AI se repair karne ka hai.

## 6.2 Healer ko blindly trust kyun nahi karna?

A failing test ke possible causes:
1. Test code wrong.
2. Application code wrong.
3. Requirement/expected result wrong.
4. Test data/environment issue.
5. Timing/network issue.
6. Locator stale/ambiguous.

Agar Healer har failure par assertion weaken kar de ya test delete kar de, toh suite green ho sakti hai but product bug hide ho sakta hai.

### Mentor addition — safe healing prompt

```text
Use the Playwright Test Healer agent to investigate this failing test.

Before changing code:
1. Identify the exact failure.
2. Determine whether it appears to be a test issue, application issue,
   test-data issue or environment issue.
3. Explain the evidence for your diagnosis.

Do not:
- Remove assertions just to make the test pass.
- Weaken expected values without requirement evidence.
- Add fixed sleeps as a default fix.
- Modify application code unless I explicitly approve it.

After proposing a fix:
1. Show the diff.
2. Run the focused test.
3. Report the exact command and result.
4. Explain any remaining uncertainty.
```

## 6.3 Interview answer

**Simple English:**

“Playwright Test Agents include Planner, Generator and Healer. Planner creates a test plan, Generator creates Playwright tests, and Healer helps repair failing tests.”

**Stronger answer:**

“The Planner Agent explores a scoped part of the application and creates a Markdown test plan. The Generator Agent uses that plan and browser context to generate Playwright tests. The Healer Agent investigates failing tests and proposes repairs. I would review generated tests and fixes carefully because a green test does not necessarily mean the correct business behaviour is covered. I would never accept removal or weakening of assertions without requirement-based justification.”

**Keywords:** Planner, Generator, Healer, test plan, test generation, repair, assertion review, human oversight.

---

# Part 7 — Playwright CLI

## 7.1 WHY: MCP ke alawa CLI kyun?

Course introduces Playwright CLI as a command-line interface for browser automation designed for coding agents.

Instructor ka main stated selling point: **token-efficient commands and skill-based workflow**.

MCP and CLI dono AI agents ke saath kaam kar sakte hain, lekin interaction mechanism different hai:
- MCP: AI client MCP server ke tools invoke karta hai.
- CLI: AI client terminal/CLI commands execute karwata hai, often skills/instructions ke through.

## 7.2 Course ke mutabik Playwright CLI features

- Token efficiency is highlighted as a key feature.
- Skill-based approach.
- Browser automation through CLI commands.
- AI coding agents ke saath use.
- Browser installation available; course says Chromium default browser included, other browsers separately install kiye ja sakte hain.

## 7.3 Installation prerequisites

Course recording mein:
- Node.js 20 or newer.
- Global NPM dependency installation.
- `--help` command se installation verify.
- Skills separately install karna.

Transcript install command ka package-name segment speech-to-text mein incomplete/ambiguous ho sakta hai. Isliye exact package command yahan invent nahi kiya gaya. Current official Playwright CLI docs se install command copy karo.

Conceptual workflow:

```text
Install supported Node.js
        |
        v
Install Playwright CLI
        |
        v
Run CLI --help
        |
        v
Install Playwright skills
        |
        v
Use CLI through coding agent
```

## 7.4 Skills installation and course bug

Course instructor ne `install skills` command run ki.

Expected behaviour: tool environment/client detect kare — GitHub Copilot or Claude Code.

Recording-time bug:
- Instructor GitHub Copilot use kar raha tha.
- Installer ne Claude Code ka `.claude` folder create kar diya.
- Instructor ne skills folder manually GitHub folder mein copy kiya.
- New skills folder mein Playwright CLI main skill aur reference files the.
- Main skill umbrella ki tarah multiple CLI workflows/references ko point karti thi.

**Important:** Ye instructor ke recording-time environment mein observed bug tha. Isko current installer ka permanent behaviour mat samajhna.

### Course skill folder concept

```text
project/
└── .github/
    └── skills/
        └── playwright-cli/
            ├── skill.md
            └── references/
                └── [CLI workflow references]
```

Ye conceptual structure hai. Actual folder names/package version ke hisaab se vary kar sakte hain.

## 7.5 Why explicitly ask the agent to use Playwright CLI?

Course instructor ne observe kiya:
- AI assistant by default kisi aur browser tool ya built-in browsing capability ko choose kar sakta hai.
- Isliye prompt mein specifically “use Playwright CLI” likhna useful hai.
- CLI commands terminal mein execute hote hain.
- VS Code ke hidden chat terminals view se commands inspect kiye ja sakte hain.
- Course mein CLI usually headless mode mein operate karta tha; headed mode explicitly request kiya gaya toh browser visible hua.

### Mentor prompt

```text
Use the Playwright CLI skills for this task.
Do not switch to Playwright MCP or another browser tool.

Open the local application in headed mode.
Generate a test plan for the checkout feature.
Save the plan in specs/checkout-test-plan.md.

Do not modify application data or source code.
Show the CLI commands executed and summarize the output.
```

---

# Part 8 — Playwright CLI in action

## 8.1 Course demo: plan → generate → repair

Instructor ka workflow:

1. AI assistant ko explicitly Playwright CLI use karne ko kaha.
2. Pizza app open karne aur test plan generate karne ko kaha.
3. CLI commands terminal mein execute hue.
4. Test plan create hua — instructor ne approximately 1,000 lines ka plan mention kiya.
5. Test plan ke specific test case `TC1.1` ke liye test generate karwaya.
6. Generated `successful initial page load.spec.ts` file ko manually execute kiya.
7. Test pass hua.
8. Test mein typo introduce karke deliberately fail karwaya.
9. AI ko Playwright CLI use karke fix karne ko kaha.
10. CLI ne typo identify karke fix kiya.

**Learning:** Test plan se selected test case generate karna, then independently run/review karna.

## 8.2 1,000-line test plan achha hai?

Not automatically.

Large test plan ka matlab:
- More scenarios ho sakte hain.
- But duplicate/low-value scenarios bhi ho sakte hain.
- Review and maintenance difficult ho sakte hain.
- Scope creep ho sakta hai.

**Mentor recommendation:** Plan ko feature-wise split karo, priority do, duplicates remove karo aur requirements se trace karo. “More lines” ≠ “better coverage”.

---

# Part 9 — Playwright MCP vs Playwright CLI: course token comparison

## 9.1 Course experiment design

Instructor ne same task dono approaches se run kiya:

**Task:** Pizza web store open karo aur theme change karo.

Comparison setup:
- Claude Code use kiya.
- Same model family/settings select karne ki koshish ki (recording mein Haiku model).
- First run: Playwright MCP.
- `/context` command se context usage inspect kiya.
- New instance: Playwright CLI.
- Same task CLI se execute kiya.
- Context usage side-by-side compare kiya.

## 9.2 Course observation

Instructor ne roughly 28,000 tokens ka MCP context usage note kiya. CLI run ka comparison dekhkar unka conclusion tha:
- Dono ka token usage almost same tha.
- Is particular demo mein MCP kabhi-kabhi slightly better bhi tha.
- MCP optimization ke baad earlier assumption — CLI always more token-efficient — universally true nahi raha.
- Final choice task complexity, client, workflow aur personal preference par depend kar sakti hai.

**Critical interpretation:** Ye ek instructor-run demonstration hai, controlled benchmark ya universal performance guarantee nahi. Same simple browser task par observed result ko har project, model, application ya task par generalize nahi karna.

## 9.3 Decision guide

| Situation | Starting choice | Reason |
|---|---|---|
| Existing MCP-based workflow already configured | Playwright MCP | Existing tools and agent setup reuse |
| CLI/skills-based coding-agent workflow | Playwright CLI | Terminal + skill-driven commands |
| Specific CLI commands inspect karne hain | Playwright CLI | Commands terminal mein visible |
| MCP tools and permissions centrally manage karne hain | Playwright MCP | MCP server/tool configuration |
| Token usage compare karna hai | Measure both | No universal winner established by this demo |

### Fair comparison kaise karoge? (Mentor addition)

- Same task and app state.
- Same model and context settings.
- Fresh session for each run.
- Same output requirements.
- Count input/output/context tokens.
- Record time and tool calls.
- Compare result quality, not only token count.
- Repeat multiple times.
- Include a complex task, not only a theme toggle.

---

# Part 10 — Python + Pytest + Playwright adaptation

Course demonstrations TypeScript mein hain. Neeche Python adaptations mentor-created hain; transcript mein Python-specific agents/CLI commands demonstrate nahi hue.

## 10.1 Python test plan se test tak

Suppose Planner output mein scenario:

```text
TC1.1 — Initial page load
Given the pizza store application is running
When the user opens the home page
Then the page heading is visible
And the menu section is displayed
```

Illustrative Python test:

```python
from playwright.sync_api import Page, expect


def test_initial_page_load(page: Page):
    page.goto("http://localhost:3000")

    expect(
        page.get_by_role("heading", name="Pizza Store")
    ).to_be_visible()

    expect(
        page.get_by_role("heading", name="Menu")
    ).to_be_visible()
```

Selectors and names actual app ke according verify karne honge. Ye code example hai, source-derived test nahi.

## 10.2 Python test healing review example

Suppose test mein:

```python
expect(page.get_by_role("button", name="Menu")).to_be_visible()
```

But application mein Menu ek heading hai. Healer might suggest:

```python
expect(page.get_by_role("heading", name="Menu")).to_be_visible()
```

Ye correct ho sakta hai — **provided DOM/requirement evidence confirm karta hai ki element heading hai.**

Lekin agar actual UI mein button expected tha aur application ne galti se heading render ki, toh test ko heading locator mein badalna product bug ko hide karega.

**Healer ka fix accept karne se pehle expected product behaviour verify karo.**

---

# Part 11 — Test Agent/CLI safety and review checklist

## Before generation
- [ ] App correct environment mein running hai?
- [ ] Feature scope defined hai?
- [ ] Requirements/test plan available hai?
- [ ] Test data safe hai?
- [ ] Agent ko correct project context mila?

## Before accepting generated tests
- [ ] Assertions meaningful hain?
- [ ] Locators stable hain?
- [ ] Test independent hai?
- [ ] Fixed sleeps avoid hue?
- [ ] Duplicate tests nahi?
- [ ] Negative/boundary scenarios relevant hain?
- [ ] Generated tests correct expected behaviour validate karte hain?

## Before accepting healed code
- [ ] Root cause identify hua?
- [ ] Assertion remove/weaken toh nahi hui?
- [ ] App bug ko test change karke hide toh nahi kiya?
- [ ] Diff review hua?
- [ ] Focused test run hua?
- [ ] Full relevant suite rerun hua?
- [ ] Failure repeatability check hui?

## Before running CLI/MCP actions
- [ ] Command inspect ki?
- [ ] Permission scope samjha?
- [ ] Destructive action toh nahi?
- [ ] External network/data mutation toh nahi?
- [ ] Secrets protected hain?
- [ ] Test/staging environment use ho raha hai?

---

# Part 12 — Interview preparation

## Q1. What are Playwright Test Agents?

**Simple answer:**

“Playwright Test Agents are AI agents for test planning, test generation and test healing. The course demonstrates Planner, Generator and Healer.”

**Detailed answer:**

“The Planner Agent explores an application and creates a Markdown test plan. The Generator Agent uses the plan and browser context to generate Playwright tests. The Healer Agent investigates failing tests and helps repair them. I treat generated code as a draft and verify assertions, locators and business requirements before accepting it.”

## Q2. What is the role of the Planner Agent?

“It explores a scoped part of the application and creates a structured Markdown test plan. For a real application, I would ask it to focus on one feature at a time, such as login or checkout.”

## Q3. What is the role of the Generator Agent?

“It converts selected scenarios from a test plan into Playwright tests, using browser interaction and the available Playwright tools.”

## Q4. What is the role of the Healer Agent?

“It investigates failing Playwright tests and proposes or applies fixes. I verify the root cause because a test can be made green by weakening an assertion, which may hide a real product defect.”

## Q5. What is Playwright CLI?

“The course introduces Playwright CLI as a command-line browser automation interface designed for coding agents. It uses skills and CLI commands to perform browser tasks and is presented as a token-efficient workflow.”

## Q6. Playwright MCP vs Playwright CLI?

“Playwright MCP exposes browser automation tools through an MCP server, while Playwright CLI is used through terminal commands and skill-based workflows. The course compares token usage on one task and finds no universal winner. I would choose based on the project workflow, required tools and measured results.”

## Q7. Why should the agent use a scoped feature?

“Smaller scope helps the agent focus on relevant workflows and reduces irrelevant output. For a real application, I would generate a plan for login, checkout or another feature separately rather than asking it to explore the entire application in one step.”

## Q8. Would you accept an AI-healed test automatically?

“No. I would first inspect the failure and determine whether it is caused by the test, application, data or environment. I would review the diff, ensure assertions were not weakened and rerun the test independently.”

---

# Part 13 — Practical assignments

## Assignment 1: Planner Agent

Choose a small feature in your demo app, e.g. login or product search.

Ask Planner to create a scoped Markdown test plan.

**Submit/check:**
- Feature scope.
- Positive scenarios.
- Negative scenarios.
- Boundary cases.
- Open questions.
- Assumptions.

## Assignment 2: Generator Agent

Select only 2–3 scenarios from the plan. Generate tests.

**Review:**
- Locator strategy.
- Assertions.
- Test data.
- Fixtures/POM.
- Independence.
- Test execution result.

## Assignment 3: Healer Agent

Intentionally break one locator or expected value in a test.

Ask Healer to investigate and fix it.

**Your task:** Decide whether its proposed fix is justified by the requirement and DOM evidence.

## Assignment 4: CLI workflow

If current supported tooling is available in your environment:
1. Install Playwright CLI using current official instructions.
2. Verify installation with help output.
3. Install the appropriate skills.
4. Explicitly ask your AI client to use the CLI.
5. Generate a scoped plan.
6. Generate one test.
7. Run it yourself.
8. Break and repair it.

Record:
- CLI command(s).
- Agent/client.
- Test plan file.
- Generated test.
- Test result.
- Any permission prompts.

## Assignment 5: MCP vs CLI comparison

Run the same simple task through both approaches. Record:
- Context/token usage, if available.
- Number of tool/CLI calls.
- Completion time.
- Output quality.
- Reliability.
- Manual review effort.

Do not declare a winner based on one run.

---

# Part 14 — Module 10 quick revision

| Concept | One-line revision |
|---|---|
| Planner Agent | Explores app and creates a Markdown test plan |
| Generator Agent | Generates Playwright tests from selected scenarios |
| Healer Agent | Helps diagnose and repair failing tests |
| Playwright snapshot | Simplified page representation that can reduce context/token use |
| Agent instructions | Markdown guidance defining tools and behaviour |
| MCP | Tool integration protocol used by agents |
| `mcp.json` | Course VS Code configuration file for Playwright MCP |
| `seed.spec.ts` | Bootstrap page context for agent execution in course setup |
| Playwright CLI | Browser automation CLI for coding-agent workflows |
| Playwright skills | Reusable instructions/references for CLI workflows |
| Headed mode | Browser UI is visible during execution |
| Headless mode | Browser runs without visible UI |
| Token comparison | Measure in context; no universal winner |

## 15 questions — notes band karke answer karo

1. Playwright Test Agents ke three agents kaunse hain?
2. Planner Agent ka output kya hota hai?
3. Generator Agent ko test plan dena useful kyun hai?
4. Healer Agent ka biggest risk kya hai?
5. Real application ko small features mein divide kyun karna chahiye?
6. Agent instruction file mein kaunse elements hote hain?
7. Playwright MCP tools agents ke saath kaise use hote hain?
8. `seed.spec.ts` ka course-level purpose kya tha?
9. Playwright CLI ka main selling point kya bataya gaya?
10. CLI installation ke liye course mein kaunsa Node.js version mention hua?
11. CLI skills installation mein instructor ko kya issue mila?
12. AI ko prompt mein CLI use karne ko explicitly kyun kehna useful hai?
13. Course ne MCP vs CLI token usage mein kya observe kiya?
14. Token usage ke basis par universal winner declare kyun nahi kar sakte?
15. AI-healed test accept karne se pehle kya verify karoge?

---

# Part 15 — Module progress tracker

| Topic | Status |
|---|---|
| Playwright AI features overview | ⬜ |
| Snapshot and token-efficiency concept | ⬜ |
| Planner / Generator / Healer roles | ⬜ |
| Test Agents setup and generated files | ⬜ |
| Agent instructions and MCP tools | ⬜ |
| Planner workflow | ⬜ |
| Generator workflow | ⬜ |
| Healer workflow | ⬜ |
| CLI purpose and installation concepts | ⬜ |
| CLI skills setup | ⬜ |
| CLI test plan generation | ⬜ |
| CLI test generation | ⬜ |
| CLI test repair | ⬜ |
| MCP vs CLI comparison | ⬜ |
| Python adaptation | ⬜ |
| Safety/review checklist | ⬜ |
| Practical assignments | ⬜ |
| Interview answers | ⬜ |

### Mentor scoring rubric

- **0 — Unknown:** Explain nahi kar pa rahe.
- **1 — Basic:** Three agents ke names/roles yaad hain.
- **2 — Working:** Scoped plan, generated tests aur repair workflow perform/review kar sakte ho.
- **3 — Strong:** MCP/CLI trade-offs, test quality, safety, token measurement aur false-healing risks explain kar sakte ho.

**Module 10 complete tab maana jayega jab tum AI se test plan/test generate karwa sako, deliberately broken test diagnose karwa sako, aur har generated/healed change ko independently validate kar sako.**

---

# Final mentor note

Is module ka sabse important lesson AI agents ke names ya CLI commands yaad karna nahi hai.

Real QA/SDET judgement ye hai:

1. Planner se relevant scope ka plan lena.
2. Generator ko clear scenario aur expected behaviour dena.
3. Healer ko root cause investigate karne dena — assertion weaken karne ki permission nahi.
4. MCP aur CLI ko measured use case ke basis par choose karna.
5. AI-generated code ko khud execute, inspect aur review karna.

**Green test is not automatically a correct test.** Test ka purpose product behaviour ko reliably verify karna hai — sirf pipeline ko green karna nahi.
