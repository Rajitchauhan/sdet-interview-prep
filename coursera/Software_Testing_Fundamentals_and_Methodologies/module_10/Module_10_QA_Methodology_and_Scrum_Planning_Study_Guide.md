# Module 10 — QA Methodology & Scrum Planning: QA Strategy Project

> **QA / SDET Mentor Study Guide**
>
> Ye guide sirf uploaded **Module 10 — QA Methodology and Scrum Planning** ZIP ke available material par based hai. Explanations Hinglish mein hain. Extra learning examples ko **Mentor-created example** label kiya gaya hai.

---

## 🎯 Learning outcomes

Is module ke baad aap:
- QA Strategy document ka purpose explain kar paoge.
- UI, API aur Database layers ke liye testing ownership define kar paoge.
- RACI matrix ka use samajh paoge.
- Static aur dynamic testing ko feature strategy mein map kar paoge.
- BDD se vague Jira story ko testable user story mein convert kar paoge.
- Happy path, edge case aur error condition ke Given-When-Then scenarios likh paoge.
- Staging environment mein manual tests execute kar paoge.
- DevTools Network tab se API defect evidence identify kar paoge.
- Responsive UI defect ko mobile viewport mein reproduce kar paoge.
- Defect report aur evidence ko QA Strategy document mein capture kar paoge.

---

# Part 1 — QA Strategy document kyun important hai?

## WHY — “Developer ke machine par working tha” enough nahi

Course video ek Friday release scenario se start hota hai:
- No test plan.
- No acceptance criteria.
- Team ne agree nahi kiya ki “Done” ka meaning kya hai.
- Monday ko support tickets aa rahe hain.
- Feature mobile par crash hota hai.
- Incomplete data submit karne par API server error return karti hai.
- Developer kehta hai machine par work kar raha tha.
- Product Manager kehta hai QA ne sign-off kiya.
- Lekin QA ke paas clear brief hi nahi tha.

**Core lesson:** QA ka role sirf release ke baad bugs find karna nahi. QA ko testing structure build karne mein help karni chahiye, taaki ambiguity aur quality risks pehle identify hon.

## WHAT — QA Strategy document

Course reading ke according deliverable ek **3–4 page QA Strategy and Execution document** hai.

Ye feature ke testing plan, ownership, acceptance criteria aur execution evidence ka single source of truth hai.

Four main components:

1. Architecture and RACI Matrix.
2. STLC Strategy.
3. BDD Acceptance Criteria.
4. Defect Log and Execution Evidence.

## Four components ka connection

`Ownership define → Testing approach plan → Requirements testable banao → Execute and record evidence`

Har component next step ko support karta hai.

## 🎤 Interview answer

**Simple English:**

A QA Strategy document defines who is responsible for testing, which testing techniques and environments will be used, what the feature is expected to do, and how execution results and defects will be documented.

**Stronger answer:**

A QA Strategy document creates a shared plan for feature quality. It identifies ownership across the UI, API, and database layers through a RACI matrix, defines static and dynamic testing activities and the target environment, records clear BDD acceptance criteria, and captures execution results with defect evidence. It helps the team plan testing before execution and makes quality decisions traceable.

**Keywords:** QA strategy, ownership, RACI, STLC, BDD, staging, execution evidence, defect log.

---

# Part 2 — Architecture layers: UI, API, Database

## WHY — Application ko layers mein kyun dekhna chahiye?

Web application ek single screen nahi hoti. User interface, backend API aur database milkar feature deliver karte hain.

Agar share link create nahi ho raha, issue:
- UI mein ho sakta hai (button/validation).
- API mein ho sakta hai (request processing/server response).
- Database mein ho sakta hai (data persistence/retrieval).

QA Strategy mein har layer ke liye ownership clear honi chahiye.

## WHAT — Three layers

| Layer | Simple meaning | Example responsibility |
|---|---|---|
| UI (User Interface) | Jo user browser/screen par dekhta aur interact karta hai | Form, button, validation, responsive layout |
| API (Application Programming Interface) | Frontend aur backend/services ke beech communication | Request payload, response, status code, error handling |
| DB (Database) | Data store/retrieve karne ki layer | Data persistence, integrity, correct records |

## HOW — MindBridge share feature example

**Mentor-created explanation based on the lab feature:**

- UI: learner note enter karta hai aur Generate share link button select karta hai.
- API: browser share-link request server ko bhejta hai.
- DB: feature ke design ke mutabik share data persist/retrieve ho sakta hai.

Agar empty note par server error aata hai, DevTools Network tab API layer ki investigation mein help karega. Agar mobile par confirmation banner header ke saath overlap kare, ye UI/layout issue ho sakta hai.

---

# Part 3 — RACI Matrix

## WHY — Ownership clear na ho to problem

Suppose API layer par defect milta hai. QA kehta hai developer fix karega, developer kehta hai QA ne validate nahi kiya, aur manager ko pata nahi hota final accountability kiski hai.

RACI matrix work ownership clear karti hai.

## WHAT — RACI

RACI ek responsibility assignment framework hai:

| Letter | Full form | Meaning |
|---|---|---|
| R | Responsible | Jo task actually perform karta hai |
| A | Accountable | Jo final ownership/answerability leta hai |
| C | Consulted | Jiski expertise/input li jaati hai |
| I | Informed | Jise progress/result ki information di jaati hai |

### R vs A — Most important difference

- **Responsible:** Kaam kaun execute karega?
- **Accountable:** Final result ke liye answerable kaun hoga?

Course reading kehti hai matrix specific honi chahiye, roles name kare, aur UI/API/DB layers mein koi gap na chhode.

## Example matrix — Mentor-created, not a prescribed course answer

Course template mein Development Team Role aur QA Team Role placeholders hain, lekin source koi universal correct RACI assignments prescribe nahi karta. Neeche ek illustrative starting point hai; actual project mein team responsibilities ke mutabik agree karo.

| Application layer | QA Team role | Development Team role |
|---|---|---|
| UI | R — UI functional/responsive tests execute | A — UI implementation/fix ownership |
| API | R — API behavior and response validation | A — API implementation/fix ownership |
| DB | C — clarify expected data behavior and validate agreed outcomes | R/A — DB changes and data-layer ownership |

**Important:** Is example ko universal standard mat samajhna. RACI team structure, access permissions aur organizational accountability par depend karta hai. A project should agree who is Accountable for each activity; avoid assigning multiple final owners if the organization requires a single A.

## RACI ka QA benefit

- Testing ownership clear hoti hai.
- API/UI/DB issues ka routing easier hota hai.
- Teams ke beech ambiguity reduce hoti hai.
- Work handoff aur communication improve hoti hai.

## 🎤 Interview answer

**Simple English:**

RACI stands for Responsible, Accountable, Consulted, and Informed. It clarifies who performs a task, who owns the final outcome, whose input is needed, and who must be kept updated.

**Stronger answer:**

In QA planning, a RACI matrix assigns clear ownership across areas such as UI, API, and database testing. Responsible identifies the person or team doing the work, Accountable identifies the final owner, Consulted identifies people whose expertise is needed, and Informed identifies people who need updates. This reduces confusion during testing and defect resolution. The exact assignments should be agreed by the project team.

**Keywords:** RACI, responsibility, accountability, consulted, informed, ownership, UI/API/DB.

---

# Part 4 — STLC Strategy: Static vs Dynamic testing

## WHY — Test strategy mein kya define karna hota hai?

QA ko feature test karne se pehle decide karna hota hai:
- Requirements ko kaise review karenge?
- Actual application behavior ko kaise validate karenge?
- Tests kis environment mein execute honge?

Course reading ke according strategy mein static techniques, dynamic techniques aur environment identify karna zaroori hai.

## 4.1 Static Testing

### Hinglish

Static testing mein software ko execute kiye bina artifacts review kiye jaate hain. Example: requirements document, user story, acceptance criteria ya code review.

MindBridge share feature ke liye:
- User story review karo.
- Missing acceptance criteria identify karo.
- Empty note behavior clarify karo.
- Mobile confirmation behavior clarify karo.
- Error handling expectations identify karo.

**Simple question:** “Code run kiye bina kya hum requirements/documentation mein problem identify kar sakte hain?”

## 4.2 Dynamic Testing

### Hinglish

Dynamic testing mein application execute karke actual behavior observe kiya jata hai.

MindBridge lab:
- Share note enter karo.
- Generate share link select karo.
- Confirmation observe karo.
- Empty note submit karo.
- DevTools Network tab mein API response inspect karo.
- Mobile viewport mein banner layout observe karo.

**Simple question:** “Application run karne par actual result expected result se match karta hai?”

## Static vs Dynamic comparison

| Area | Static testing | Dynamic testing |
|---|---|---|
| Execution | Software execute nahi hota | Software execute hota hai |
| Input | Requirements, user stories, design/code artifacts | Running application and test data |
| Goal | Ambiguity/defects early identify | Actual runtime behavior validate |
| Example | Acceptance criteria review | Share link generate karke response check |

## 4.3 Environment — Staging

Course reading ke according project ke liye relevant environment **staging environment** hai.

Staging:
- Controlled environment hota hai.
- Production ko mirror karta hai.
- Real users ko affect kiye bina testing support karta hai.

[!NOTE]
Course reading is project ke liye staging specify karti hai. Ye note kisi organization ke har test type ke liye universal environment rule prescribe nahi karta.

## Example STLC Strategy — 3–5 bullets (mentor-created draft)

Aap template ke STLC Strategy section mein apne feature ke according kuch is tarah likh sakte ho:

- Static: Review the share-dashboard user story and BDD acceptance criteria to identify missing validation, error-handling, and mobile-layout expectations.
- Dynamic functional: Execute the happy-path share-link scenario and verify the confirmation behavior.
- Dynamic negative/API: Submit an empty note and inspect the share-link API request and response in browser DevTools.
- Dynamic UI/responsive: Generate a share link at a phone-sized viewport and inspect the confirmation banner layout.
- Environment: Execute the scenarios in the provided staging environment, using the lab test account and controlled test data.

This is a mentor-created draft based on the lab scenarios; adjust it to the exact final acceptance criteria you write.

## 🎤 Interview answer

**Simple English:**

Static testing reviews documents or code without executing the software. Dynamic testing executes the application and checks its actual behavior. For this project, the tests are executed in the staging environment.

**Stronger answer:**

My STLC strategy combines static and dynamic techniques. I first review the user story and acceptance criteria to identify ambiguity and missing behavior. Then I execute functional and negative scenarios against the staging application, inspect API responses using browser DevTools, and validate the UI under a mobile viewport. Static review helps identify issues before execution, while dynamic testing confirms the running feature behaves as expected.

**Keywords:** static review, dynamic execution, acceptance criteria, staging, API response, responsive UI.

---

# Part 5 — BDD Acceptance Criteria: vague story ko testable banao

## WHY — Vague Jira ticket QA ke liye problem kyun?

Course project ka user story:

“As a learner, I want to share my dashboard with others so they can see it.”

Story mein missing:
- Acceptance criteria.
- Definition of Done.
- Error handling.
- Device expectations.

Aise vague story par developer apni assumption se build karega aur QA apni assumption se test karega. Result mismatch ho sakta hai.

## WHAT — BDD

Behavior-Driven Development (BDD) requirements ko plain language mein expected behavior ke basis par define karta hai.

Given-When-Then:
- **Given:** Starting condition/context.
- **When:** User action.
- **Then:** Expected result.

Three scenarios required by this lab:
1. Happy path.
2. Edge case.
3. Error condition.

Har scenario itna clear hona chahiye ki doosra tester bhi bina clarification ke execute kar sake.

## MindBridge share dashboard feature

Course lab instructions specify:
- Signed-in learner share link generate karta hai with a note (happy path).
- Small mobile screen par share confirmation (edge case).
- Empty note ke saath link generate karna (error condition); friendly validation message show hona chahiye.

### Scenario 1 — Happy Path

```gherkin
Given the learner is signed in and is viewing the dashboard
When the learner enters a share note and selects Generate share link
Then the application generates a share link and displays a "Share link ready" confirmation with the URL
```

### Scenario 2 — Edge Case: Small mobile viewport

```gherkin
Given the learner is signed in and the dashboard is displayed in a phone-sized viewport
When the learner enters a share note and selects Generate share link
Then the share confirmation is displayed without overlapping or being obscured by the page header
```

### Scenario 3 — Error Condition: Empty note

```gherkin
Given the learner is signed in and is viewing the dashboard
When the learner leaves the share note empty and selects Generate share link
Then the application displays a friendly validation message and does not return an unhandled server error
```

[!IMPORTANT]
These are mentor-authored, testable formulations based on the lab's required behavior. The exact source says the happy path generates a share link with a note, the mobile edge case checks the confirmation on a small screen, and the empty-note case should show a friendly validation message. The wording above makes those outcomes explicit.

## What makes BDD criteria good?

- Given clearly defines precondition.
- When describes one action or event.
- Then describes observable outcome.
- Avoid vague words like “works correctly.”
- Include the exact state/message/result when the source or product defines it.
- Keep happy path, edge case and error condition distinct.

## 🎤 Interview answer

**Simple English:**

BDD acceptance criteria describe expected behavior using Given, When, and Then. Given defines the starting condition, When describes the action, and Then defines the expected result.

**Stronger answer:**

I start by reviewing the user story and identifying missing behavior. I discuss unclear cases with the team and write separate Given-When-Then scenarios for the happy path, edge cases, and error conditions. Each Then clause must describe an observable result so that developers, testers, and stakeholders share the same understanding and the scenario can be executed consistently.

**Keywords:** BDD, Gherkin, Given-When-Then, happy path, edge case, error condition, testability.

---

# Part 6 — Execute the MindBridge lab

> **Source lab instructions:** The uploaded DOCX describes the setup and execution flow below. The lab app is intended to run inside the provided lab VM.

## 6.1 Required setup

Source instructions list:
- MindBridge application: `http://localhost:3000`
- Jira Cloud workspace.
- Word processor.
- Spreadsheet program.
- Lab VM and browser.

Start application using the DOCX's primary command:

```bash
cd /home/coder/Desktop/Files/lab && npm install && bash start.sh
```

If the path is different, source DOCX provides this fallback:

```bash
bash "$(find /app $HOME -maxdepth 5 -name start.sh -not -path '*/node_modules/*' 2>/dev/null | head -n 1)"
```

Wait for the server to report that it is running. Keep the terminal open. Then open Chrome and navigate to:

```text
http://localhost:3000
```

Stop the lab with `Ctrl-C` in the terminal when finished.

## 6.2 Supporting files referenced by the DOCX

The lab instructions say files should be in `supporting-files` next to `start.sh`:

- `MindBridge_LC1_Project_Seed.csv` — Jira backlog seed.
- `QA Strategy and Execution Template.docx` — central deliverable template.
- `RACI_Matrix_Template.csv` — optional RACI spreadsheet template.
- `Test_Execution_Log_Template.csv` — optional execution log template.

**Uploaded ZIP limitation:** The ZIP supplied in this conversation contains the project requirement reading, project instruction reading, subtitle/VTT and the “Why This Project Matters” transcript PDF. It does not include the supporting CSV files or the actual QA Strategy template DOCX. The DOCX lab instructions refer to those files as downloadable lab assets, but they are not present as standalone files in this ZIP. Do not assume their exact formatting or column layout from this guide.

## 6.3 Jira setup — Import backlog

1. Log in to Jira Cloud.
2. Open your project/board.
3. Locate CSV import. Depending on Jira version and permissions, it may appear under Project Settings, Jira administration, or system settings.
4. Upload `MindBridge_LC1_Project_Seed.csv` from the lab supporting files.
5. Map CSV columns to Jira fields.
6. Complete import and open the backlog.
7. Verify one Epic and one User Story appear.

Source says:
- An Epic is a significant body of work too large to complete in one step.
- It is broken into smaller user stories.
- The imported user story is intentionally vague and needs refinement.

User Story:
“As a learner, I want to share my dashboard with others so they can see it.”

## 6.4 Complete Architecture/RACI Matrix

Open the QA Strategy and Execution Template and fill the RACI section.

Required application layers:
- UI.
- API.
- DB.

Required team columns in the described template:
- QA Team Role.
- Dev Team Role.

Assign R, A, C, I roles for each layer. The source says the matrix should:
- Cover all three layers without gaps.
- Name roles rather than leaving vague ownership.
- Avoid ambiguous responsibilities.

The source does not provide one universal correct set of RACI assignments. Agree assignments with the project/team structure.

## 6.5 Complete STLC Strategy section

Write 3–5 bullet points covering:
- Static testing activities.
- Dynamic testing activities.
- Environment where tests execute — staging environment in the lab VM.

Use Part 4's sample as a starting point, but align it with your actual scenarios and team responsibilities.

## 6.6 Update Jira story with three BDD scenarios

Edit the imported user story description and add:

1. Happy path — signed-in learner generates a share link with a note.
2. Edge case — share confirmation on small mobile screen.
3. Error condition — empty note should produce a friendly validation message.

Each scenario:
```gherkin
Given [starting condition]
When [user action]
Then [expected result]
```

Save the Jira ticket and capture a screenshot showing all three scenarios. This screenshot belongs in Section 3 of the final QA Strategy document.

---

# Part 7 — Execute tests and find seeded defects

## Login to MindBridge

Source DOCX seeded test account:

- Email: `admin@mindbridge.local`
- Password: `admin12345`

Open Dashboard from navigation. Feature appears at the top:
- Share note field.
- Generate share link button.

[!WARNING]
These are credentials for the local training lab only. Do not reuse them on a real website or account.

## Scenario 1 — Happy path

Steps:
1. Enter a short note, e.g. `My course progress`.
2. Select **Generate share link**.
3. Observe the result.

Expected result from lab instructions:
- A **“Share link ready”** banner appears.
- A URL is displayed.

Record:
- Expected result.
- Actual result.
- Pass/Fail.
- Screenshot if useful as evidence.

## Scenario 2 — Error condition: empty note

Steps:
1. Clear the note field.
2. Leave it empty.
3. Open browser DevTools using `F12`.
4. Switch to the **Network** tab.
5. Select Generate share link.
6. Watch the share-link request's status code.

Source says this scenario targets a functional API defect. The reading does not specify the exact status code or response body. Therefore, do not assume a specific code before observing the actual request.

What to record:
- Request URL/name.
- HTTP status code.
- Response body/message, if available.
- Expected behavior: friendly validation message.
- Actual behavior.
- Screenshot showing app state and Network evidence.

## Scenario 3 — Edge case: small mobile viewport

Steps:
1. Open DevTools (`F12`).
2. Enable device toolbar with `Ctrl+Shift+M`.
3. Select a phone-sized viewport, e.g. iPhone SE.
4. Enter a share note.
5. Generate share link.
6. Observe confirmation banner in relation to the page header.

Source says this scenario targets a non-functional UI defect.

What to record:
- Viewport/device preset.
- What overlaps, breaks, or becomes obscured.
- Expected layout.
- Actual layout.
- Screenshot showing the UI in context.

## Two seeded defects — Source description

| Defect category | Scenario | How to investigate |
|---|---|---|
| Functional API defect | Empty-note error condition | Network tab; inspect share-link request status |
| Non-functional UI defect | Small mobile viewport edge case | Device toolbar; inspect confirmation banner vs page header |

Lab instructions say finding and documenting at least one defect is sufficient.

[!NOTE]
The uploaded project instruction reading does not state the exact API status code or exact UI overlap dimensions. Those must be observed in the lab. Do not fabricate these values in your defect report.

---

# Part 8 — Defect log and evidence

## WHY — Bug report without evidence incomplete kyun?

Developer ko issue reproduce karne ke liye clear information chahiye. Sirf “share feature not working” likhne se issue actionable nahi hota.

Course instructions require:
- Clear defect title.
- Simple reproducible steps.
- Defect description.
- Screenshot that demonstrates the issue.
- Full browser context where possible, including application and DevTools output.

## Defect report template — Mentor-created format

| Field | What to write |
|---|---|
| Defect ID | Jira-generated ID, if available |
| Title | Short, specific summary |
| Environment | Staging / lab VM |
| Preconditions | Login state, note state, viewport |
| Steps to reproduce | Numbered, repeatable steps |
| Expected result | Acceptance Criteria outcome |
| Actual result | What actually happened |
| Evidence | Screenshot / Network response |
| Severity/Priority | As agreed by team; don't guess without impact assessment |

## Example title patterns

- `API: Empty share note request returns an unexpected server error`
- `UI: Share confirmation banner overlaps the page header on a phone-sized viewport`

These are title patterns based on the lab's defect categories. Use them only if the observed evidence supports them.

## Screenshot evidence

For API defect:
- App visible.
- Empty note state visible.
- DevTools Network request selected.
- Status/response visible.

For UI defect:
- Mobile viewport/device toolbar visible.
- Confirmation banner and page header visible together.
- Overlap/layout issue clearly shown.

## Defect report quality check

- [ ] Title states the problem clearly.
- [ ] Environment/build context recorded where available.
- [ ] Preconditions included.
- [ ] Steps can be repeated.
- [ ] Expected result is based on BDD criterion.
- [ ] Actual result is factual, not guessed.
- [ ] Screenshot shows issue in context.
- [ ] API evidence includes actual request/response when applicable.

---

# Part 9 — Final QA Strategy and Execution document

Source reading says final deliverable is one 3–4 page document with four components:

| Section | Required content |
|---|---|
| 1. Architecture and RACI Matrix | UI/API/DB ownership |
| 2. STLC Strategy | Static + dynamic techniques and staging environment |
| 3. BDD Acceptance Criteria | Three scenarios and screenshot of updated Jira ticket |
| 4. Defect Log and Execution Evidence | Defect description and screenshot evidence |

The project instruction says compile the screenshots and written components into one PDF for the graded assignment.

## Submission checklist

- [ ] RACI matrix complete for UI, API, DB.
- [ ] STLC strategy includes static and dynamic techniques.
- [ ] Staging environment identified.
- [ ] Jira user story rewritten with three BDD scenarios.
- [ ] Screenshot of updated Jira ticket.
- [ ] At least one seeded defect identified.
- [ ] Clear defect title and reproducible steps.
- [ ] Screenshot of defect evidence.
- [ ] Final QA Strategy and Execution document compiled.
- [ ] Exported final document as PDF.

## Common issues and source solutions

| Problem | Source-provided guidance |
|---|---|
| Jira CSV import fails | Check CSV formatting and project-admin/equivalent permissions |
| Cannot find seeded API bug | Open DevTools Network tab before submitting empty note |
| Cannot find seeded UI bug | Enable device emulation (`Ctrl+Shift+M`) and use phone-sized viewport |
| Unsure where CSV import lives | Check Project Settings, Jira administration/system settings, or search Jira for CSV import |

---

# Part 10 — Common mistakes

1. QA Strategy ko sirf test case list samajhna; it also defines ownership, techniques and environment.
2. UI/API/DB layers mein se kisi ko leave out karna.
3. RACI mein Responsible aur Accountable ka difference confuse karna.
4. Static testing ko application execute karke testing samajhna.
5. Dynamic testing mein expected vs actual record na karna.
6. Staging environment ka naam likhna, lekin reason na dena.
7. Vague BDD scenario likhna, e.g. “Then share link works.”
8. Happy path, edge case aur error condition mein se koi omit karna.
9. Mobile edge case ko desktop viewport par test karna.
10. Empty-note API test ke waqt Network tab observe na karna.
11. Defect title mein unverified status code likh dena.
12. Screenshot ke bina defect submit karna.
13. Expected result aur actual result ko mix kar dena.
14. RACI assignment ko universal standard samajhna; it must reflect the actual team.

---

# Module 10 — Interview preparation

## Q1. What is a QA Strategy document?

**Simple English:**

A QA Strategy document defines testing ownership, testing techniques, environments, acceptance criteria, and execution evidence for a feature.

**Stronger answer:**

It is a planning and execution artifact that creates a shared understanding of how a feature will be validated. It identifies ownership across UI, API and DB layers, defines static and dynamic testing approaches, records BDD acceptance criteria, and captures defects with reproducible steps and evidence.

## Q2. What is a RACI matrix?

**Simple English:**

RACI stands for Responsible, Accountable, Consulted, and Informed. It clarifies task ownership.

**Stronger answer:**

RACI assigns roles to work activities. Responsible performs the task, Accountable owns the final outcome, Consulted provides input, and Informed receives updates. In QA, it helps clarify ownership across UI, API and database testing.

## Q3. Static vs Dynamic testing?

**Simple English:**

Static testing reviews artifacts without running the software. Dynamic testing runs the software and checks its behavior.

**Stronger answer:**

Static testing can include requirement and document reviews to identify ambiguity before execution. Dynamic testing validates actual runtime behavior using test data and a running application. Both complement each other in a test strategy.

## Q4. Why staging environment?

**Simple English:**

Staging is a controlled environment that mirrors production and allows testing without affecting real users.

**Stronger answer:**

Staging provides a controlled, production-like environment for validating features before release. It helps teams identify issues using representative configurations and test data while avoiding the impact of testing directly on live customers.

## Q5. How do you investigate an API defect in browser?

**Simple English:**

I open DevTools, go to the Network tab, perform the action, and inspect the request, status code, and response.

**Stronger answer:**

I first reproduce the issue with clear preconditions. In browser DevTools, I monitor the Network tab, trigger the action, and inspect the relevant request. I record the request details, actual status code, response body, and compare them with the expected behavior. I capture a screenshot and include reproducible steps in the defect report.

---

# Module 10 — Practical exercises

## Exercise 1 — RACI understanding

Explain in your own words:
1. Responsible vs Accountable.
2. Who should be Consulted for an API contract question?
3. Why should UI/API/DB all appear in the matrix?
4. Why is there no universal correct RACI table?

## Exercise 2 — STLC strategy

For the MindBridge share feature, write:
- Two static testing activities.
- Two dynamic testing activities.
- One sentence explaining why staging is used.

## Exercise 3 — BDD writing

Write your own Given-When-Then scenarios for:
1. Learner generates share link with a note.
2. Confirmation appears on a phone-sized viewport.
3. Empty note produces friendly validation.

## Exercise 4 — Defect investigation

For the empty-note API issue:
- What should be visible in DevTools?
- What actual details must be captured?
- Why should you not guess the HTTP status code?

## Exercise 5 — Defect report

Write a report with:
- Title.
- Preconditions.
- Steps.
- Expected.
- Actual.
- Evidence.

Only include details you actually observe in the lab.

---

# Module 10 — Progress tracker

- [ ] QA Strategy document purpose
- [ ] UI/API/DB layers
- [ ] RACI definitions
- [ ] Responsible vs Accountable
- [ ] RACI matrix drafted
- [ ] Static testing strategy
- [ ] Dynamic testing strategy
- [ ] Staging environment rationale
- [ ] MindBridge user story review
- [ ] Three BDD scenarios
- [ ] Jira backlog import
- [ ] Jira ticket screenshot
- [ ] Lab application setup
- [ ] Seeded account login
- [ ] Happy path execution
- [ ] Empty-note API investigation
- [ ] Mobile viewport UI investigation
- [ ] Defect report and screenshot
- [ ] QA Strategy document assembled
- [ ] Final PDF prepared

---

## Source coverage & accuracy notes

- ZIP includes two readings: **Project Requirements Feature – QA Strategy** and **Project Instructions Feature – QA Strategy**.
- It includes subtitle/VTT and a detailed transcript PDF for **Why This Project Matters**.
- Source defines a 3–4 page QA Strategy and Execution document with four components: Architecture/RACI, STLC Strategy, BDD Acceptance Criteria, Defect Log/Execution Evidence.
- Source requires UI, API and DB ownership, static and dynamic techniques, staging environment, and three BDD scenarios (happy path, edge case, error condition).
- Source lab describes two seeded defects: API defect on empty-note scenario and UI defect on small mobile viewport.
- Source does not specify the exact API status code or exact UI defect geometry. These must be observed in the running lab.
- The uploaded ZIP does not contain the supporting `MindBridge_LC1_Project_Seed.csv`, `QA Strategy and Execution Template.docx`, `RACI_Matrix_Template.csv`, or `Test_Execution_Log_Template.csv` referenced by the lab instructions. It only contains the two readings, subtitle/VTT, and “Why This Project Matters” PDF. The guide therefore explains the referenced workflow but does not invent the missing template layout or CSV contents.
- The lab's Jira import UI may vary by Jira configuration/version; source itself notes different possible locations.
- The example RACI matrix and sample STLC bullets are mentor-created illustrations, not a source-provided answer key.
