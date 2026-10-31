# Module 09 — Agentic AI Skills for QA
## Complete Hinglish Study Guide | Custom Skills, Templates, Scripts & QA Automation

> **Module ka central idea:** AI assistant ko reusable, repeatable instructions dena, taaki woh ek specific workflow ko consistent tareeke se perform kar sake. Skills mein instructions ke saath supporting templates aur executable scripts bhi ho sakte hain.

---

## 0. ZIP inspection aur source coverage

Uploaded ZIP mein:
- 5 `.txt` transcript files
- 5 matching English `.vtt` subtitle files

Transcript/subtitle pairs ka content duplicate hai. Ek transcript section test-plan-from-ticket aur count-tests skills cover karta hai; baaki skill creation, skill iteration aur skill discovery cover karte hain.

| Course lesson/topic | Actual source coverage |
|---|---|
| Build a basic skill | `skills` folder, per-skill folder, `skill.md`, name and description |
| Skill invocation | LLM name/description ke basis par decide karta hai ki skill invoke karni hai ya nahi |
| Reusable template | `template.md` ko skill instructions se reference karna |
| Execute code from a skill | `scripts` folder, JavaScript script, process arguments, stdout/console output |
| QA skill example 1 | Jira ticket se test plan aur test cases generate karna |
| QA skill example 2 | Local script se project mein test files count karna |
| Create your own skills | Workflow identify → clear input/output → implement → iterate/refine |
| Find existing skills | ClaudeSkills repository, ClaudeSkills.info, skills.sh |
| Install a skill | `npx`/Node.js based installation example; project-level placement |
| GitHub Copilot example | `.github/skills` style configuration shown in course |
| Claude example | Assistant-specific configuration folder ka concept |

**Source boundary:** Transcript mein `test-from-ticket` skill ka complete `skill.md` content aur exact Jira ticket details fully present nahi hain. Isliye guide us example ka workflow explain karti hai, missing prompt/template ko course ka exact content batakar invent nahi karti. Course ke demo mein JavaScript script hai; Python example neeche mentor adaptation hai.

---

# Part 1 — AI Skills kya hoti hain?

## 1.1 WHY: Har baar same instructions kyun nahi likhni chahiye?

Maan lo tum har sprint mein Jira ticket se test cases banate ho. Har baar AI ko tumhe batana padta hai:

- Ticket ka requirement carefully read karo.
- Acceptance criteria identify karo.
- Positive aur negative test cases banao.
- Boundary conditions cover karo.
- Test data mention karo.
- Output ko specific table format mein do.
- Missing requirements ko clearly flag karo.

Har naye ticket par same long prompt type karna repetitive hai. Agar ye workflow reusable hai, toh uski instructions ko ek skill mein save kiya ja sakta hai.

## 1.2 WHAT: Skill ki definition

**Simple definition:** AI skill ek reusable set of instructions aur optional supporting resources hota hai jo AI assistant ko kisi particular task/workflow ko perform karne ka tareeka batata hai.

Skill mein ho sakta hai:
- `skill.md` — skill ka name, description aur instructions.
- `template.md` — reusable output format/template.
- `scripts/` — helper scripts jo local computation ya file processing karte hain.
- Other reference files — workflow-specific guidance/data.

Course ke example mein AI assistant `skill.md` ke name aur description se decide karta hai ki user prompt par skill relevant hai ya nahi.

### Skill ≠ MCP

| AI Skill | MCP |
|---|---|
| Workflow instructions ko package/reuse karta hai | AI application ko external tools/systems se connect karne ka protocol |
| Task perform karne ka process batata hai | Tools/resources access karne ka interface deta hai |
| Templates aur scripts include kar sakta hai | MCP server tools expose karta hai |
| Example: Jira ticket se test plan banana | Example: browser/network inspection tool call |

Dono ek saath useful ho sakte hain: skill AI ko workflow samjha sakti hai aur MCP external system se data laane mein help kar sakta hai. Ye combined example mentor explanation hai, course ka direct demo nahi.

## 1.3 QA mein skills ke practical use cases

- Jira ticket → test plan.
- Acceptance criteria → test cases.
- Project → test/spec file count.
- Failed test logs → structured failure summary.
- API contract → positive/negative test checklist.
- Bug report → defect template.
- Release checklist → QA readiness summary.
- Playwright project → test code review checklist.

**Good skill candidate:** Workflow repeated ho, input clear ho, output clear ho, aur steps reasonably stable hon.

---

# Part 2 — Apni first skill banana

## 2.1 WHY: Skill ko folder structure mein kyun rakhte hain?

Skill ek single prompt se zyada ho sakti hai. Jab instructions, templates aur scripts alag files mein hote hain, toh:
- Instructions readable rehti hain.
- Template independently update ho sakta hai.
- Script independently test/run ho sakti hai.
- Reusable resources ek skill ke saath organized rehte hain.

## 2.2 Course demonstration: Hello skill

Course instructor ne VS Code + GitHub Copilot use kiya.

Conceptual structure:

```text
project/
└── .github/
    └── skills/
        └── hello/
            └── skill.md
```

Claude Code ya doosre assistants ke liye configuration folder/path alag ho sakta hai. **Exact folder convention client-specific hai.** Course ka point hai: jis AI assistant ko skill deni hai, uski documented skill location use karo.

### `skill.md` mein kya hota hai?

Course ke demo mein do required metadata fields highlight hue:
- `name`
- `description`

Inke baad skill instructions likhe jaate hain.

Illustrative course-style example:

```markdown
---
name: hello
description: A simple skill that responds when the user enters hello.
---

When the user says hello, respond with:
"You are awesome."
```

> Ye teaching example hai, exact current GitHub Copilot/Claude schema ki guarantee nahi. Current client documentation ke mutabik metadata format verify karo.

## 2.3 Skill invocation kaise hota hai?

Course demonstration:
1. Instructor ne Copilot se poocha: “What skills do you have?”
2. Assistant ne built-in customizations ke saath custom `hello` skill identify ki.
3. New chat mein `hello` prompt diya.
4. Assistant ne skill instructions follow karke “You are awesome” response diya.
5. Instruction update karke response badla.
6. Dobara invoke karke updated instruction ka effect verify kiya.

**Important concept:** Name aur description AI assistant ko skill ka purpose samjhate hain. Poor description se skill wrong time par invoke ho sakti hai ya relevant prompt par invoke nahi hogi.

## 2.4 Common mistakes

- Description vague rakhna: “This skill helps with testing.”
- Ek skill mein unrelated workflows bhar dena.
- Instructions mein contradictory rules.
- Skill file save/update karne ke baad invocation verify na karna.
- Assistant-specific folder structure ko doosre client par blindly copy karna.

## 2.5 Interview answer

**Simple English:**

“An AI skill is a reusable set of instructions for a specific workflow. It can include a skill definition, supporting templates and scripts. The assistant uses the skill description to decide when it is relevant.”

**Stronger answer:**

“I use a skill when I have a repeatable workflow with reasonably clear inputs and outputs. The skill contains metadata and instructions, and it can reference reusable templates or execute helper scripts. For QA, an example is converting a Jira ticket into a structured test plan. I still validate the generated cases against the acceptance criteria and refine the skill based on actual results.”

**Keywords:** reusable workflow, `skill.md`, name, description, invocation, template, script, iteration.

---

# Part 3 — Skill ko template ke saath extend karna

## 3.1 WHY

Agar skill ka output har baar same structure mein chahiye, toh response format ko instructions ke andar hard-code karne ke bajay separate template file mein rakh sakte hain.

Example: Bug report, test plan, test case, sprint QA summary.

## 3.2 Course demonstration

Instructor ne `hello` skill ke folder mein `template.md` create ki.

Conceptual structure:

```text
.github/
└── skills/
    └── hello/
        ├── skill.md
        └── template.md
```

Course flow:
1. `template.md` mein expected response likha.
2. `skill.md` mein assistant ko template reference/use karne ko kaha.
3. Skill invoke ki.
4. Assistant ne template ka content response mein use kiya.

### Mentor example: Test plan template

Neeche QA use case ke liye mentor-created template hai; course ka exact template nahi.

```markdown
# Test Plan — [Feature Name]

## 1. Objective
[What are we validating?]

## 2. Scope
### In Scope
- [Feature/behaviour]

### Out of Scope
- [Excluded behaviour]

## 3. Preconditions
- [Required setup]

## 4. Test Scenarios
| ID | Scenario | Expected Result | Priority |
|---|---|---|---|

## 5. Risks and Open Questions
- [Risk or missing requirement]

## 6. Exit Criteria
- [Completion condition]
```

Skill instructions mein keh sakte ho:
- Ticket ko read karo.
- Missing requirements ko invent mat karo.
- Template ka structure preserve karo.
- Open questions ko separate section mein rakho.

## 3.3 Template vs instruction

| File | Responsibility |
|---|---|
| `skill.md` | Task kaise perform karna hai |
| `template.md` | Output ka format/structure kya hona chahiye |
| `scripts/` | Deterministic computation/file processing kaise karna hai |

---

# Part 4 — Skills ke andar scripts execute karna

## 4.1 WHY: Simple counting AI se kyun nahi karwana?

Course ka example: Project mein kitne test files hain?

AI assistant poore workspace ko inspect karke count karne ki koshish kar sakta hai, lekin sirf file count karne ke liye har file ka content read karna inefficient ho sakta hai.

Course ka approach:
1. Local script project files scan kare.
2. Test/spec file patterns identify kare.
3. Count calculate kare.
4. Output assistant ko de.
5. Assistant result ko user-friendly summary mein present kare.

**Core principle:** Deterministic/local computation ko script se karna, phir concise result AI ko dena token-efficient ho sakta hai.

## 4.2 Course example: `count tests`

Course demonstration mein:
- JavaScript script project files scan karti hai.
- Test/spec file patterns search karti hai.
- User prompt `count tests` skill invoke karta hai.
- Assistant ko local script execute karne ki permission di jaati hai.
- Script result se project test overview milta hai.

## 4.3 Course example: Hello-name skill

Instructor ne second skill banayi:
- Prompt format: `hello, my name is [name]`.
- `scripts/awesomename.js` file.
- Script process arguments se name read karti hai.
- `generateAwesomeName` function name ko split karke ek part lowercase aur doosra uppercase karta hai.
- Script output stdout/console par expose karti hai.
- Skill instructions script run karne aur result template mein use karne ko kehti hain.
- Assistant command run karne se pehle permission maangta hai.
- Demo ke liye Node.js installed hona zaroori tha.

Conceptual folder:

```text
.github/
└── skills/
    └── hello-name/
        ├── skill.md
        ├── template.md
        └── scripts/
            └── awesomename.js
```

### Script arguments ka mental model

```text
User prompt
   |
   v
AI skill selected
   |
   v
Skill instructions tell assistant to run script
   |
   v
Script receives arguments
   |
   v
Script computes result
   |
   v
stdout/output
   |
   v
AI uses result in response
```

**Important:** AI assistant ko script run karne ki permission dena ek security decision hai. Unknown script ko blindly approve mat karo.

---

# Part 5 — Python adaptation: QA skills ke helper scripts

Course script JavaScript mein tha. Tum Python background rakhte ho, isliye neeche Python adaptations hain. Ye mentor-created examples hain, course ke original code nahi.

## 5.1 Python script: test files count karna

Example project:

```text
qa-project/
├── tests/
│   ├── test_login.py
│   ├── test_checkout.py
│   ├── login.spec.ts
│   └── checkout.spec.ts
└── tools/
    └── count_tests.py
```

Python script:

```python
from pathlib import Path

ROOT = Path.cwd()

TEST_PATTERNS = (
    "test_*.py",
    "*_test.py",
    "*.spec.ts",
    "*.test.ts",
    "*.spec.js",
    "*.test.js",
)

test_files = set()

for pattern in TEST_PATTERNS:
    test_files.update(ROOT.rglob(pattern))

print(f"Total test files: {len(test_files)}")

for file_path in sorted(test_files):
    print(file_path.relative_to(ROOT))
```

### Line-by-line explanation

- `Path.cwd()` current working directory leta hai.
- `TEST_PATTERNS` supported file naming patterns define karta hai.
- `set()` duplicate paths avoid karta hai.
- `rglob()` project ke subfolders mein recursively search karta hai.
- `sorted()` output ko predictable order mein deta hai.
- `relative_to(ROOT)` output mein relative path show karta hai.

**Limitation:** Ye test files count karta hai, individual test functions/test cases nahi. Ek file mein 20 tests ho sakte hain; file count 1 hi rahega.

## 5.2 Python script: pytest test function count (basic AST approach)

Agar Python test functions ka approximate count chahiye, AST use kar sakte hain:

```python
import ast
from pathlib import Path

ROOT = Path.cwd()
total = 0

for file_path in ROOT.rglob("test_*.py"):
    try:
        source = file_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
    except (OSError, SyntaxError, UnicodeDecodeError):
        continue

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name.startswith("test_"):
                total += 1

print(f"Discovered test functions (basic count): {total}")
```

**Limitation:** Ye pytest ke full collection semantics reproduce nahi karta. Parametrized tests ke runtime cases, `conftest.py` effects, dynamic generation, class methods aur pytest configuration is simple count se accurately represent nahi hote. Actual collection ke liye project ke venv mein `pytest --collect-only -q` zyada reliable starting point hai.

## 5.3 Python script skill ka safe contract

Skill instructions mein clear likho:
- Script ka exact path.
- Expected arguments.
- Expected output.
- Allowed folders.
- Read-only behaviour.
- Failure handling.
- User approval requirement if script changes files or data.

---

# Part 6 — QA skill example: Jira ticket to test plan

## 6.1 Course demonstration

Course mein instructor ne `test from ticket` type skill use ki.

Workflow:
1. Jira ticket sample open/focus kiya.
2. User ne prompt diya: “Generate a test plan for this ticket.”
3. GitHub Copilot ne relevant skill identify ki.
4. Skill ke instructions ke according ticket analyze kiya.
5. Test plan aur test cases generate hue.
6. Instructor ne generated output ko inspect kiya aur satisfactory bataya.

Transcript mein exact full skill instructions aur Jira ticket content nahi diya gaya. Isliye neeche ka design mentor addition hai.

## 6.2 Mentor addition: Better ticket-to-test-plan skill design

### Inputs
- Jira ticket description.
- Acceptance criteria.
- Relevant UI/API details, if available.
- Existing test conventions (optional).

### Expected outputs
- Requirement summary.
- Acceptance criteria list.
- Positive scenarios.
- Negative scenarios.
- Boundary scenarios.
- Test data.
- Preconditions.
- Open questions.
- Risks.
- Traceability from criterion to scenario.

### Suggested `skill.md` instructions

```markdown
---
name: ticket-to-test-plan
description: Use this skill when the user asks to create a QA test plan or test cases from a Jira ticket or feature requirement.
---

1. Read the complete ticket and acceptance criteria.
2. Summarize the expected behaviour without changing its meaning.
3. Identify missing, ambiguous or conflicting requirements.
4. Do not invent business rules or expected results.
5. Generate positive, negative and boundary scenarios where supported.
6. Map each scenario to an acceptance criterion.
7. Include preconditions and required test data.
8. Mark assumptions explicitly.
9. Use the referenced test-plan template.
10. Finish with open questions and risks.
```

### Quality check: AI-generated test plan

| Check | What to verify |
|---|---|
| Requirement fidelity | Ticket ka meaning change toh nahi hua? |
| Coverage | Har acceptance criterion covered hai? |
| Negative paths | Invalid/missing input included? |
| Boundaries | Min/max/empty/length conditions? |
| Test data | Values and setup defined? |
| Expected result | Observable and unambiguous? |
| Assumptions | Clearly marked, not hidden? |
| Traceability | Scenario → acceptance criterion mapping? |

### Example: Reset password ticket

Illustrative requirement:
- Registered user reset password request submit kar sakta hai.
- Valid email par reset link issue hota hai.
- Unknown email par privacy-safe response show hota hai.
- Expired reset token accept nahi hona chahiye.

Possible scenario ideas:
1. Registered email with valid reset flow.
2. Unknown email.
3. Empty email.
4. Invalid email format.
5. Expired reset token.
6. Already-used token.
7. Password below minimum policy.
8. Password/confirm password mismatch.
9. Reuse old password, if policy specifies restriction.
10. Token reuse after successful reset.

**Important:** Scenarios 9–10 tabhi valid requirements honge jab ticket/business rules support karein. Otherwise open questions ke roop mein rakho.

---

# Part 7 — Skills kaise create karein: course workflow

Course ka recommended process:

<list marker="number" gap={2}>
  <list-item>
    **Identify a workflow to automate**

    Aisa repetitive task choose karo jisme input aur output clear ho.
  </list-item>
  <list-item>
    **Define the input and output**

    Example: Jira ticket → structured test plan.
  </list-item>
  <list-item>
    **Implement the skill**

    `skill.md`, templates aur zaroorat ho toh scripts create karo.
  </list-item>
  <list-item>
    **AI assistant se help lo**

    Workflow describe karke first draft generate karwa sakte ho.
  </list-item>
  <list-item>
    **Run and validate**

    Different realistic inputs par skill execute karo.
  </list-item>
  <list-item>
    **Iterate and refine**

    Wrong invocation, missing cases, weak formatting aur script errors fix karo.
  </list-item>
</list>

Course explicitly batata hai ki AI-generated skill first attempt mein exactly desired behaviour nahi degi. Multiple runs aur refinement expected hain.

## 7.1 Skill design worksheet

| Design question | Your answer |
|---|---|
| Repetitive workflow kya hai? | |
| Trigger prompt kya hoga? | |
| Input files/data kya hain? | |
| Output format kya chahiye? | |
| Instructions kya honge? | |
| Template chahiye? | |
| Script chahiye? | |
| Script read-only hai ya write action? | |
| Success kaise validate hoga? | |
| Failure par kya report hoga? | |

---

# Part 8 — Existing skills discover and install karna

## 8.1 Course mein mentioned resources

Course ne ye resources introduce kiye:

1. **ClaudeSkills GitHub repository** — domain-wise skills; repository clone karke project mein add karne ka example.
2. **ClaudeSkills.info** — functionality ke basis par skills explore karne ka resource.
3. **skills.sh** — course instructor ke opinion mein useful/broad skill directory, jahan search, popular, trending/hot skills dekh sakte hain.

Ye course ke time par dikhaye gaye resources hain; availability, trustworthiness aur installation commands time ke saath change ho sakte hain.

## 8.2 Course installation demonstration

Course mein:
- skills.sh par ek skill select ki.
- Installation command `npx` based thi.
- Node.js required tha.
- First run par package download prompt aaya.
- Instructor ne install allow kiya.
- Tool ne `.agents` folder create kiya.
- Demo mein instructor ne folder ko GitHub Copilot ke project skill location ke hisaab se rename/move kiya.
- `skill.md` aur scripts project mein available hue.
- Copilot ne brainstorming skill invoke ki.

**Important source caveat:** Transcript mein folder naming ke kuch spoken forms ambiguous hain. Current client ke liye exact folder path guess mat karo. GitHub Copilot/Claude ki current official documentation check karo. Course demo ke project-local installation concept ko samjho, exact path ko universal rule mat banao.

## 8.3 Security checklist before installing a community skill

- [ ] Repository/maintainer verify kiya?
- [ ] `skill.md` instructions read ki?
- [ ] Scripts inspect kiye?
- [ ] Script shell commands execute karti hai?
- [ ] Network requests bhejti hai?
- [ ] Files delete/modify karti hai?
- [ ] Credentials ya environment variables read karti hai?
- [ ] Dependencies and install lifecycle scripts inspect kiye?
- [ ] Isolated test project mein try kiya?
- [ ] Untrusted skill ko production secrets se access nahi diya?

**GitHub stars/popularity trust guarantee nahi hain.** Skill instructions bhi prompt injection ya unsafe behaviour introduce kar sakti hain; scripts actual executable code hain.

---

# Part 9 — Python + Pytest + Playwright skill ideas

Ye section mentor-created applications hain, course ke direct demos nahi.

## 9.1 Skill: Playwright test reviewer

**Trigger:** “Review this Playwright test.”

Checklist:
- Locator quality.
- Assertion quality.
- Fixed sleeps.
- Test independence.
- Fixture reuse.
- Test data.
- Cleanup.
- POM consistency.
- Failure diagnostics.

Expected output:
1. Critical issues.
2. Maintainability issues.
3. Suggested changes.
4. Questions/assumptions.
5. Final reviewed code (only when requested).

## 9.2 Skill: API test scenario generator

**Input:** OpenAPI endpoint, request schema, acceptance criteria.

**Output:**
- Positive cases.
- Missing required field.
- Invalid type.
- Invalid enum.
- Boundary values.
- Unauthorized/forbidden.
- Not found.
- Duplicate/conflict.
- Rate-limit case, if applicable.
- Response schema checks.

Skill ko explicitly kehna chahiye: undocumented business rules invent mat karo.

## 9.3 Skill: Failed pytest summary

**Input:** pytest output / JUnit XML / log file.

**Output:**
- Failed test names.
- Assertion error.
- Exception type.
- Relevant stack trace.
- Possible cause (clearly labelled hypothesis).
- Next investigation steps.

Script-based parsing deterministic fields extract kar sakta hai; AI unka readable summary bana sakta hai.

## 9.4 Skill: Test inventory report

- Test file count.
- Test function count.
- Test folders.
- Markers.
- Naming convention violations.
- Files missing test docstrings (if your team requires them).

Count script aur pytest collection ko confuse mat karo: file count, function count aur collected parametrized test count different metrics hain.

---

# Part 10 — Skill quality: kaise pata chale skill achhi hai?

| Dimension | Weak skill | Strong skill |
|---|---|---|
| Trigger | Vague description | Specific task and trigger |
| Input | Undefined | Required input documented |
| Output | Random format | Stable template |
| Rules | Generic | Explicit constraints |
| Assumptions | Hidden | Marked clearly |
| Script | Unreviewed | Small, scoped, tested |
| Safety | Broad permissions | Least privilege |
| Validation | One demo only | Multiple representative cases |
| Maintenance | Never updated | Iterated from feedback |

### Suggested validation set

Har skill ko at least in cases par test karo:
1. Normal valid input.
2. Missing required input.
3. Ambiguous input.
4. Large/complex input.
5. Invalid/unexpected input.
6. Repeated invocation.
7. Script failure/permission denied.

Ye mentor-recommended validation approach hai, course ka stated numerical requirement nahi.

---

# Part 11 — Interview preparation

## Q1. What is an AI skill?

**Simple:**
“An AI skill is a reusable set of instructions for a specific task. It can include supporting templates and scripts.”

**Detailed:**
“An AI skill packages a repeatable workflow for an AI assistant. Its metadata helps the assistant identify when it is relevant. The instructions define the process, while optional templates and scripts provide consistent output and deterministic helper operations. In QA, I can use a skill to generate a test plan from a Jira ticket or summarize a test inventory.”

## Q2. What should a skill contain?

- Name.
- Description.
- Instructions.
- Optional templates.
- Optional scripts.
- Optional supporting reference files.

## Q3. Why separate a template from skill instructions?

“To keep workflow logic and output formatting separate. The instructions describe what to do; the template defines how the result should be structured. This makes both easier to maintain.”

## Q4. Why execute a local script from a skill?

“For deterministic tasks such as counting files or parsing structured data, a local script can do the computation more efficiently than asking the model to inspect every file. The script returns concise results that the AI can summarize.”

## Q5. How would you create a QA skill?

“I would first identify a repetitive workflow with clear inputs and outputs. Then I would create the skill instructions, add a template if the output needs a fixed format, and add a script only if deterministic local processing is required. I would test it with valid, incomplete and edge-case inputs, review its permissions and refine it based on failures.”

## Q6. What are the risks of installing third-party skills?

“Third-party skills may contain unsafe instructions or scripts. Scripts can access files, execute commands or make network requests depending on permissions. I inspect the source, verify the maintainer, understand dependencies and permissions, and test in an isolated project before using it.”

## Q7. How do you know a ticket-to-test-plan skill is producing good output?

- Acceptance criteria traceability.
- Positive and negative coverage.
- Boundary cases.
- Correct expected results.
- Test data.
- Preconditions.
- Open questions and assumptions.
- No invented requirements.

---

# Part 12 — Practical assignments

## Assignment 1: Build your first QA skill

Create a skill called `bug-report-helper`.

Input:
- Bug title.
- Steps to reproduce.
- Expected result.
- Actual result.
- Environment.
- Evidence.

Output:
- Structured bug report.
- Missing information checklist.
- Reproducibility concerns.

**Pass criteria:** Missing fields invent na hon; assistant questions/flags them.

## Assignment 2: Build a test count helper

Create a Python script to:
- Count Python test files.
- List test file paths.
- Count basic `test_` functions.
- Clearly state that this is not equivalent to pytest collection count.

## Assignment 3: Build ticket-to-test-plan skill

Use a sample requirement from your own demo app. Generate:
- Requirement summary.
- Acceptance criteria.
- Test scenarios.
- Test data.
- Open questions.
- Traceability.

Manually review all generated expected results.

## Assignment 4: Skill iteration

First run ke output mein 3 weaknesses identify karo. Instructions/template update karo. Same input dobara run karo. Compare:
- Coverage.
- Correctness.
- Output consistency.
- Assumptions.
- Missing information handling.

## Assignment 5: Playwright reviewer skill

Apna existing Playwright test do. Skill se review karwao. Har recommendation ko accept mat karo; justify karo ki change kyun useful hai ya kyun unnecessary.

---

# Part 13 — Module 9 quick revision

| Concept | One-line revision |
|---|---|
| AI skill | Reusable instructions for a repeatable task |
| `skill.md` | Skill metadata and instructions |
| Name | Skill identity |
| Description | Helps assistant determine relevance/invocation |
| Template | Reusable output structure |
| Script | Deterministic helper code executed locally |
| `scripts/` | Convention used in course demo for helper scripts |
| stdout | Script output that can be read by the assistant |
| Input/output | Workflow should have clear input and output |
| Iteration | Run, evaluate and refine the skill |
| `npx` | Node.js package runner used in course install example |
| skills.sh | Skill discovery directory shown in course |

## 12 questions — notes band karke answer karo

1. AI skill kya hai?
2. Skill aur MCP mein difference kya hai?
3. Skill ke name aur description ka role kya hai?
4. `skill.md` ka purpose kya hai?
5. Template ko separate file mein kyun rakhte hain?
6. Script skill ko kaise extend karti hai?
7. Course ke `count tests` skill ka workflow kya tha?
8. Course ke hello-name skill mein process arguments ka use kyun hua?
9. AI-generated skill first attempt mein perfect kyun nahi hoti?
10. Skill banane ke liye clear input/output kyun important hai?
11. Third-party skill install karte waqt kya inspect karoge?
12. Jira ticket-to-test-plan output ko kaise validate karoge?

---

# Part 14 — Module progress tracker

| Topic | Status |
|---|---|
| AI skills concept and use cases | ⬜ |
| Skill folder structure | ⬜ |
| `skill.md` name and description | ⬜ |
| Skill invocation | ⬜ |
| Template reference | ⬜ |
| Scripts inside skills | ⬜ |
| Script arguments and output | ⬜ |
| Ticket-to-test-plan workflow | ⬜ |
| Count-tests workflow | ⬜ |
| Workflow → input/output → implementation | ⬜ |
| Iteration and refinement | ⬜ |
| Skill discovery resources | ⬜ |
| Installation and project-level use | ⬜ |
| Security review | ⬜ |
| Python QA helper script | ⬜ |
| Practical assignments | ⬜ |
| Interview answers | ⬜ |

## Mentor scoring rubric

- **0 — Unknown:** explain nahi kar pa rahe.
- **1 — Basic:** definition samajh aayi, practical structure nahi bana sakte.
- **2 — Working:** simple skill + template/script bana aur test kar sakte ho.
- **3 — Strong:** workflow design, edge cases, security, iteration aur output validation explain kar sakte ho.

**Module 9 complete tab hoga jab tum khud ek useful QA skill design, implement, test aur refine kar sako.**

---

# Final mentor note

Module 9 ka real lesson ye hai: **AI ko ek achha prompt dena aur AI ke liye reusable workflow banana alag skills hain.**

Agar tumhara workflow repeat hota hai, input/output defined hai, aur instructions stable hain, toh custom skill useful ho sakti hai. Lekin:
- Har task ke liye skill banana zaroori nahi.
- Simple one-time question ke liye normal prompt enough hai.
- Deterministic computation script ko dena better ho sakta hai.
- AI-generated output ko requirement ke against review karna zaroori hai.
- Third-party skill/script ko inspect kiye bina execute mat karna.

**SDET advantage:** Tum sirf tests automate nahi karoge; tum apne QA engineering workflows ko bhi repeatable aur efficient bana sakte ho.
