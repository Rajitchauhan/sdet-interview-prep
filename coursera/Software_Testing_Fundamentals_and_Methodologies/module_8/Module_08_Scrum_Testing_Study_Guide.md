# Module 8 — Scrum Testing, Definition of Done, BDD & Work Management Tools

> **QA / SDET Mentor Study Guide**
>
> Ye file sirf uploaded **Module 8 — Scrum Testing** ZIP ke material par based hai. Explanations Hinglish mein hain. Jahan practical examples source se extra hain, unhe **Mentor-created example** label kiya gaya hai.

---

## 🎯 Module learning outcomes

Is module ke baad aap:
- Scrum sprint mein testing ko continuous activity ke roop mein samajh paoge.
- Backlog refinement mein tester ki responsibility explain kar paoge.
- Acceptance Criteria aur Definition of Done (DoD) ka difference clear kar paoge.
- BDD aur Given-When-Then (Gherkin) scenarios likh paoge.
- Happy path aur negative path scenarios design kar paoge.
- Jira mein QA workflow board/backlog setup ka purpose samajh paoge.
- Azure DevOps mein Jira ke equivalent work-management concepts locate kar paoge.
- BDD criteria ko manual testing se validate karke Pass/Fail record kar paoge.

---

# Part 1 — Scrum sprint mein testing kab hoti hai?

## WHY — Last day testing problem

Course video ek situation se start hota hai: two-week sprint ka last day hai, developer ne user registration form complete kiya hai aur release do ghante mein hai. Tester form open karta hai aur basic questions hi unanswered hain:
- Password kitna long hona chahiye?
- Invalid email par kya hoga?
- Phone par form work karega?
- Requirements written kyun nahi hain?

Developer ne ek assumption banayi, Product Owner ne doosri. Ab tester ke paas testing ke liye bahut kam time hai.

**Core lesson:** Ye sirf technical problem nahi, communication aur early requirement clarity ki problem hai.

## WHAT — Testing at the speed of sprints

Testing ko sprint ke final day tak postpone karne ke bajay, quality thinking ko sprint ke throughout include karna chahiye.

Course video ke according:
- Late testing confusion aur rework create karti hai.
- Early quality involvement developers aur testers ko align karti hai.
- Tester backlog refinement mein upcoming work review karta hai.
- Tester vague user story par questions poochkar acceptance criteria clarify karne mein help karta hai.

## Backlog refinement kya hai?

Backlog refinement wo meeting/activity hai jahan team sprint start hone se pehle upcoming work review karti hai.

Tester ka kaam hai aise questions poochna jo expected behavior ko clear karte hain.

Course video ke registration example mein:
1. Agar email pehle se registered hai to kya hoga?
2. Password ki minimum length kya hai?
3. Required field blank ho to user ko kaunsa error message milega?

Ye questions acceptance criteria banane mein help karte hain.

## Shift testing left — is context mein

Furniture analogy samjho: shelf assemble karne ke baad measurement galat pata chale to poori shelf disassemble karni pad sakti hai. Agar wood cut karne se pehle measurement check kar liya, to correction quick aur cheap hai.

Software mein bhi:
- Early ambiguity identify → requirement clarify.
- Late ambiguity identify → code/design rework, delays, last-minute pressure.

[!IMPORTANT]
Tester ka role sirf checklist execute karna nahi. Tester ko requirements par sharp questions poochne, gaps identify karne aur team ko costly rework se bachane mein help karni chahiye.

## 🎤 Interview answer

**Simple English:**

Testing should happen throughout a sprint, not only at the end. Testers should participate in backlog refinement, clarify requirements, help define acceptance criteria, test during development, and verify the completed story.

**Stronger answer:**

In Scrum, QA should be involved from the earliest conversations. During backlog refinement, the tester challenges vague user stories and asks about edge cases, validation rules, and expected error messages. These discussions produce clear acceptance criteria before development begins. During the sprint, QA collaborates with developers, performs testing and reports defects early. This reduces misunderstandings, rework, and last-minute release pressure.

**Keywords:** backlog refinement, early quality involvement, acceptance criteria, shift-left, continuous testing, rework prevention.

---

# Part 2 — Definition of Done (DoD)

## WHY — “Developer says done” ka matlab QA ke liye done hai?

Imagine developer kehta hai login feature done hai. QA check karta hai aur happy path pass ho jata hai. Lekin:
- Code peer-reviewed nahi hua.
- Unit tests CI pipeline mein pass nahi hue.
- Documentation update nahi hui.
- High-severity defect abhi open hai.

Kya story genuinely complete hai? Course ke according, nahi.

## WHAT — Definition of Done

**Definition of Done (DoD)** Scrum team ka shared, written agreement/checklist hai jo define karta hai ki har user story ko complete aur release-ready consider karne se pehle minimum quality standard kya meet karna hoga.

DoD:
- Entire Scrum Team agree karti hai: developers, testers, Product Owner.
- Har story par apply hota hai.
- Team-wide contract hai.
- Work start hone se pehle agree hona chahiye, baad mein nahi.

### DoD ko “floor, not ceiling” kyun kaha gaya?

Floor = minimum acceptable quality bar. Ye best possible feature define nahi karta; ye minimum conditions define karta hai jinhe har story ko clear karna hai.

## Standard DoD checklist — Course reading

Course material mein typical DoD items:

- [ ] Code written and peer-reviewed by at least one other developer.
- [ ] Unit tests written and passing with no failures in CI pipeline.
- [ ] Acceptance criteria QA tester ne agreed scenarios ke against verify kiye.
- [ ] No critical or high-severity defects left open.
- [ ] Documentation updated where applicable.
- [ ] Feature Product Owner ne review and approve kiya.

Team product, industry aur pipeline maturity ke according checklist adjust kar sakti hai. Important hai ki team pehle se agree kare.

## Acceptance Criteria vs Definition of Done

Ye module ka very important distinction hai.

| Comparison | Acceptance Criteria | Definition of Done |
|---|---|---|
| Scope | One specific user story | Every story/team work |
| Main question | “Is particular feature ko kya karna chahiye?” | “Har work item ko complete hone ke liye kya meet karna hai?” |
| Focus | Feature-specific user-visible behavior | Shared minimum quality standard |
| Example | Wrong password par error message show ho | Code reviewed, tests pass, no critical/high defects, documentation updated |
| Applies to | Specific story | Team-wide across stories |

### Critical concept — Story AC pass kar sakti hai, phir bhi DoD fail

Example:
- Login story ke happy path, wrong password aur empty email scenarios pass.
- Lekin code review pending hai.
- Unit tests CI mein add/pass nahi hue.

Acceptance Criteria pass hue, but DoD complete nahi hua. Story ko “Done” mark nahi karna chahiye jab tak both standards satisfy na hon.

[!WARNING]
Acceptance Criteria aur DoD ko synonyms mat samajhna. Dono meet karne zaroori hain; ek doosre ka replacement nahi hai.

## QA DoD ko kaise verify karta hai?

### 1. Backlog refinement ke during
- Upcoming story ke acceptance criteria review karo.
- Missing/unclear criteria flag karo.
- Testable criteria ke bina story DoD meet karne ke liye ready nahi ho sakti.

### 2. Sprint ke during
- DoD checklist ke against progress continuously track karo.
- Final day tak wait mat karo.
- Missing review/tests/docs/defects ko early surface karo.

### 3. Sprint review se pehle
- Board par “Done” mark hui har story ka DoD verify karo.
- Agar koi checklist item incomplete hai, story ko Done nahi rehna chahiye; work ko appropriate state mein return karo.

**Accountability nuance:** QA DoD ko champion aur verify karne mein help karta hai, lekin DoD meet karne ki accountability poori Scrum Team ki hai — sirf QA ki nahi.

## 🎤 Interview answer — DoD

**Simple English:**

The Definition of Done is a team-wide checklist that defines the minimum quality standard every user story must meet before it is considered complete. It may include code review, passing unit tests, verified acceptance criteria, no critical defects, updated documentation, and Product Owner approval.

**Stronger answer:**

The Definition of Done is a shared agreement across the Scrum Team that applies to every story. Acceptance criteria describe the behavior of one specific feature, whereas the DoD defines the common quality bar for all work. A story can satisfy its acceptance criteria but still fail the DoD—for example, if code review is pending or CI tests have not passed. QA helps verify the checklist throughout the sprint, but the whole Scrum Team is accountable for meeting it.

**Keywords:** team-wide agreement, minimum quality standard, all stories, acceptance criteria, CI, peer review, shared accountability.

---

# Part 3 — BDD (Behavior-Driven Development)

## WHY — “Authenticate securely” test karne ke liye enough requirement hai?

Course reading ka example:

“As a user, I want to authenticate securely.”

Sentence reasonable lagta hai, lekin tester ke liye bahut vague hai:
- Valid password ke rules kya hain?
- Wrong password par kya message aayega?
- Blank email field par kya hoga?
- Successful login ke baad user kahan jayega?

Jab tak behavior clear nahi, tester exact test nahi likh sakta aur developer exact expected feature build nahi kar sakta.

## WHAT — BDD kya hai?

Behavior-Driven Development (BDD) ek collaborative approach hai jisme team feature requirements ko user ke perspective se expected behavior ke basis par define karti hai.

BDD ka focus sirf tests likhna nahi. Iska focus development se pehle right conversations karna hai.

BDD:
- Technical aur non-technical team ke beech communication gap reduce karta hai.
- Requirements ko plain, structured language mein express karta hai.
- Team ko behavior par agree karne deta hai.
- Behavioral scenarios create karta hai jo user story ke acceptance criteria ban sakte hain.

## BDD ka practical flow

`Vague User Story → Team Discussion → Behavioral Scenarios → Acceptance Criteria → Development & Testing`

## Gherkin — Given / When / Then

BDD mein commonly used simple syntax ko Gherkin kaha jata hai. Course reading Given-When-Then structure explain karti hai.

| Keyword | Meaning | Purpose |
|---|---|---|
| Given | Starting condition / precondition | Test kis state se start ho raha hai? |
| When | User action / event | User kya action perform karta hai? |
| Then | Observable expected outcome | Action ke baad kya result dikhna chahiye? |
| And | Additional condition/step | Extra context add karna without repeating same keyword |

### Simple Hinglish example

```gherkin
Given the user is on the login page
And the user has a registered account
When the user submits the form with valid credentials
Then the user is redirected to the dashboard
```

- **Given:** Starting state. User login page par hai aur registered account hai.
- **And:** Additional precondition. Account registered hai.
- **When:** Action. Valid credentials submit hue.
- **Then:** Observable result. Dashboard open hua.

[!TIP]
Given = “Pehle se kya condition hai?”
When = “User ne kya kiya?”
Then = “Uske baad kya observable result aana chahiye?”

## Happy path vs Negative path

- **Happy path:** Expected successful flow.
- **Negative path:** Invalid input, missing data ya incorrect action ke case mein expected behavior.

Course login example:

### Scenario 1 — Successful Login (Happy Path)

```gherkin
Given the user is on the login page and has a registered account
When the user enters a valid email and correct password and selects Submit
Then the system authenticates the user and redirects them to their dashboard
```

### Scenario 2 — Incorrect Password (Negative Path)

```gherkin
Given the user is on the login page
When the user enters a valid email and an incorrect password and selects Submit
Then the system displays "Invalid email or password" and does not grant access
```

### Scenario 3 — Empty Email Field (Negative Path)

```gherkin
Given the user is on the login page
When the user leaves the email field blank and selects Submit
Then the system displays a validation error and prevents the form from submitting
```

## Good BDD scenario ki qualities

1. Given clear starting state bataye.
2. When specific action describe kare.
3. Then observable outcome define kare.
4. Expected result vague na ho, e.g. “system responds” is not enough.
5. Scenario ek particular behavior cover kare.
6. Team ke technical aur non-technical members ise samajh saken.

## BDD ke benefits

- **Shared understanding:** Team ek hi expected behavior par agree karti hai.
- **Living documentation:** Scenarios system behavior ka plain-language record ban sakte hain.
- **Automation readiness:** Gherkin scenarios ko suitable automation frameworks ke saath connect kiya ja sakta hai.
- **Less guesswork:** Developer ko build karna aur tester ko verify karna clear hota hai.

[!NOTE]
BDD scenario automation ke liye useful foundation ho sakta hai, lekin Gherkin text apne aap executable browser test nahi ban jata. Automation framework ko steps ki implementation chahiye hoti hai. Ye last sentence mentor clarification hai; uploaded reading says scenarios can often be connected to automation frameworks.

## 🎤 Interview answer — BDD

**Simple English:**

BDD is a collaborative approach in which teams define software requirements through expected behavior from the user's perspective. It commonly uses Given-When-Then scenarios to make acceptance criteria clear and testable.

**Stronger answer:**

Behavior-Driven Development helps business stakeholders, developers, and testers build a shared understanding before implementation. Instead of leaving a user story vague, the team discusses concrete behaviors and documents them using Gherkin. Given describes the precondition, When describes the action, and Then describes the observable outcome. These scenarios guide development and testing, act as living documentation, and can provide a foundation for automation.

**Keywords:** collaboration, user behavior, Gherkin, Given-When-Then, acceptance criteria, living documentation, automation.

---

# Part 4 — MindBridge BDD lab: Write and validate scenarios

> **Source lab:** ZIP mein MindBridge app lab instructions, backlog CSV aur BDD solution key included hain. Is part mein source lab ke exact expected behaviors preserve kiye gaye hain.

## Lab goal

1. Jira mein Sprint 1 backlog import karna.
2. Secure-login user story select karna.
3. Given-When-Then acceptance criteria likhna.
4. Har scenario MindBridge app par manually execute karna.
5. Pass/Fail record karna.

## Lab setup — Source instructions

- MindBridge lab app terminal se start hoti hai:
  ```bash
  bash /app/lab/start.sh
  ```
- App Chrome mein `http://localhost:3000` par open hoti hai.
- Lab finish par terminal mein `Ctrl-C` se stop karna.
- Supporting files lab interface ke Lab Files icon → Files → app → lab → supporting-files mein milti hain.
- Jira Cloud par Scrum project create karna aur Sprint 1 backlog CSV import karna.
- Seeded account:
  - Email: `admin@mindbridge.local`
  - Password: `admin12345`
- Ya lab mein naya account register kar sakte ho.

[!WARNING]
Ye credentials uploaded lab ke local demo application ke liye hain. Inhe kisi real website/account par use nahi karna.

## Backlog mein kaunsi stories hain?

Uploaded CSV mein 3 records hain:

| Issue Type | Summary |
|---|---|
| Task | Set up development environment for Q3 projects |
| Story | As a user, I can view my order history |
| Story | As a user, I want to authenticate securely |

Secure-login story par lab focus karta hai.

## Jira board workflow — Source video

Jira setup walkthrough:
1. Free Jira Cloud account create karo.
2. Workspace/space aur Scrum project configure karo.
3. Board columns set karo:
   - To Do
   - In Progress
   - In QA
   - Done
4. CSV backlog import karo.
5. Imported work items verify karo.

Board ka QA purpose:
- Developer-completed work In QA mein move hota hai.
- QA testing/approval ke baad hi Done mein transition hota hai.

### CSV import field mapping — Important source inconsistency

Jira walkthrough PDF/video mein CSV import ke dauran five fields mapping ka mention hai, aur video says 12 issues imported. Lekin uploaded lab CSV files mein 3 columns (`Issue Type`, `Summary`, `Description`) aur 3 data records hain; DOCX lab instructions bhi 3 backlog items describe karti hain.

Isliye actual lab ZIP ke supplied CSV/DOCX ko follow karte waqt 3 records aur 3 columns ko source evidence maana gaya hai. Video ke 12-issue/five-field narration ko is lab CSV ke saath silently reconcile nahi kiya ja sakta. Jira UI version ke hisaab se navigation/labels bhi differ kar sakte hain.

## Step 1 — Select secure-login story

Ticket:
`As a user, I want to authenticate securely`

Description login functionality aur successful login ke baad dashboard redirect explain karti hai. Lekin testable acceptance criteria missing hain. Ye gap tester ko close karna hai.

## Step 2 — Happy path

Lab app login page par jao. Source instructions ke according:
- Home page se Log in select karo.
- Subheading: `Sign in to continue your courses.`
- Submit button label: `Sign in`.

Write:

```gherkin
Given that the user is on the MindBridge login page and has a registered account
When the user enters a valid email address and the correct password and selects Sign in
Then the system authenticates the user and redirects them to their dashboard
```

## Step 3 — Negative scenarios

Lab mein minimum 3 scenarios total required hain: one successful login plus at least two negative paths.

### Incorrect password

```gherkin
Given the user is on the MindBridge login page
When the user enters a valid email address and an incorrect password and selects Sign in
Then the system displays "Email or password is incorrect." and does not grant access
```

Expected:
- Inline error appears.
- User login page par rehta hai.
- Dashboard show nahi hota.

### Empty email

```gherkin
Given the user is on the MindBridge login page
When the user leaves the email field blank and selects Sign in
Then the system displays "Enter a valid email address." and prevents the form from submitting
```

Expected:
- Email field ke liye validation message.
- User login page par rehta hai.
- Dashboard redirect nahi hota.

### Optional stronger coverage — Unregistered email

```gherkin
Given the user is on the MindBridge login page
When the user enters an email address that is not registered in the system and any password and selects Sign in
Then the system displays a generic credentials error and does not reveal whether the email is registered
```

Expected:
- Generic invalid-credentials message.
- Access denied.
- App confirm nahi karti ki email registered hai ya nahi.

### Optional stronger coverage — Empty password

```gherkin
Given the user is on the MindBridge login page
When the user enters a valid email address, leaves the password field blank, and selects Sign in
Then the system displays "Password is required." and prevents the form from submitting
```

Expected:
- Password field validation message.
- User login page par rehta hai.
- Dashboard show nahi hota.

## Exact lab UI messages — Source DOCX and solution key

| Condition | Expected message / behavior |
|---|---|
| Successful login | Dashboard redirect; login error nahi |
| Incorrect password | `Email or password is incorrect.` |
| Empty or invalid email | `Enter a valid email address.` |
| Empty password | `Password is required.` |
| Unregistered email | Generic credentials error; registration status reveal nahi |

**Formatting rules from lab:**
- Use `Select`, not `click`, for user actions.
- Each Given, When, Then should be on its own line.
- Use exact button label `Sign in`.
- Then should describe an observable outcome.

## Step 4 — Manual validation and result log

Har scenario execute karo aur actual UI ko Then clause ke saath compare karo.

| Scenario | Expected outcome | Actual outcome | Result |
|---|---|---|---|
| Successful login | Dashboard redirect |  |  |
| Incorrect password | Exact credentials error; stay on login page |  |  |
| Empty email | Exact email validation message |  |  |
| Empty password (optional) | Exact password validation message |  |  |
| Unregistered email (optional) | Generic credentials error |  |  |

Uploaded solution key ke according lab build mein seeded defects nahi hain; listed scenarios pass hone chahiye. Agar actual result different aaye, actual behavior record karo. Difference useful defect information ho sakta hai.

## Self-assessment — BDD solution key

Solution key ke according verify:
- Each scenario has distinct Given, When, Then lines.
- Outcomes observable hain.
- Minimum coverage: successful login, incorrect password, empty email.
- Additional coverage: unregistered email, empty password.
- No duplicate scenarios that test the same behavior without adding value.

---

# Part 5 — Jira and Azure DevOps: same QA thinking, different platform

## WHY — Tool change ho sakta hai, process thinking nahi

Course videos Jira setup aur Azure DevOps navigation demonstrate karte hain. QA workflow ka purpose dono mein similar hai: work items, backlog, board states aur acceptance criteria ko visible rakhna.

## Jira setup walkthrough — Course video

Video mein:
- Jira Cloud workspace/space create kiya.
- Software development/Scrum board template choose kiya.
- Project create kiya.
- Default board ko QA workflow ke liye customize kiya.
- `In QA` column ko `In Progress` aur `Done` ke beech place kiya.
- CSV se backlog import kiya.
- Imported work items verify kiye.

### Four-stage QA board

`To Do → In Progress → In QA → Done`

Meaning:
- **To Do:** Work start nahi hua.
- **In Progress:** Developer/team actively working.
- **In QA:** Build QA verification ke liye ready/under test.
- **Done:** QA approval ke baad work complete.

## Jira CSV import — Source walkthrough

Video flow:
1. Space/project settings mein import section locate karo.
2. CSV option choose karo.
3. Backlog CSV upload karo.
4. CSV columns ko Jira fields se map karo.
5. Import execute karo.
6. Backlog view mein imported items verify karo.
7. Ticket detail panel mein acceptance criteria review/refine karo.

Video narration mein five fields/12 issues ka mention hai, lekin supplied lab CSV and DOCX describe three items and three columns. Is mismatch ko note kiya gaya hai; actual supplied exercise file ke content ko priority di gayi hai.

## Azure DevOps mapping — Course video

Course transcript ke mapping:

| Jira concept | Azure DevOps equivalent (as presented in video) |
|---|---|
| Space | Organization |
| Project | Project |
| Ticket | Work item |
| Scrum board | Board |
| Backlog view | Backlogs |
| Workflow columns | Board columns / workflow states |
| Acceptance criteria | Work item ka dedicated Acceptance Criteria field |

Azure DevOps video mein:
- Organization top-level container hai.
- Project board, backlog aur work items hold karta hai.
- Boards section mein Work items, Boards aur Backlogs use hote hain.
- Board columns: To Do, Doing, In QA, Done.
- Backlogs upcoming work items ko prioritized list mein show karte hain.
- Work item detail mein Acceptance Criteria field visible hota hai.

[!NOTE]
Video says terminology slightly different hai, lekin structure/purpose similar hai. Jira aur Azure DevOps ke exact UI labels/configuration organization aur product version ke hisaab se vary kar sakte hain.

## Tester ke liye practical importance

Tool ya board name yaad karna enough nahi. Aapko ye samajhna chahiye:
- Story ki requirement kahan milegi?
- Acceptance criteria kahan likhe/review honge?
- Work ka current status kaise dikhega?
- QA handoff kis state mein hota hai?
- QA approval ke baad Done kaun mark karta hai, aur team ka workflow kya hai?

---

# Part 6 — Production-style thinking: one story from start to done

> **Mentor-created integrated example:** MindBridge login story ko poore Module 8 concepts se connect karte hain.

### 1. Backlog refinement
Story: “As a user, I want to authenticate securely.”

Tester asks:
- Wrong password par kya message?
- Blank email par kya validation?
- Unregistered email reveal hoga ya generic error?
- Successful login ke baad destination kya hai?

### 2. BDD acceptance criteria
Team Given-When-Then scenarios par agree karti hai:
- Successful login.
- Incorrect password.
- Empty email.
- Optional: unregistered email and empty password.

### 3. DoD agreement
Story tab tak Done nahi jab tak team checklist meet na kare:
- Code peer review.
- Unit tests pass in CI.
- QA acceptance criteria verified.
- No critical/high defects open.
- Relevant documentation updated.
- Product Owner approval.

### 4. Sprint tracking
Board state moves:
`To Do → In Progress → In QA → Done`

### 5. QA validation
QA har BDD scenario execute karta hai, actual result record karta hai, defects report/retest karta hai, aur DoD checklist verify karta hai.

**Core outcome:** “Feature working hai” aur “Story Done hai” do different claims hain. Acceptance criteria feature behavior validate karte hain; DoD shared completion standard validate karta hai.

---

# Part 7 — Common mistakes

1. Testing ko sprint ke last day tak postpone karna.
2. Backlog refinement mein tester ka participate na karna.
3. Vague story ko directly test case mein convert karne ki koshish karna.
4. Given, When, Then ko interchangeable samajhna.
5. Then clause mein vague outcome likhna, e.g. “system works.”
6. Happy path cover karke negative paths ignore karna.
7. Acceptance Criteria ko DoD ke equal samajhna.
8. QA ko DoD ki sole owner samajhna — accountability entire Scrum Team ki hai.
9. Acceptance criteria pass hote hi story ko Done mark kar dena, even when DoD incomplete hai.
10. Jira/Azure DevOps ke UI labels ko universal samajhna.
11. Board par In QA state ko skip karke developer work direct Done mark kar dena, jab team workflow QA approval require karta ho.
12. BDD text ko automatically executable test samajhna; automation ke liye step implementation/framework integration chahiye.

---

# Module 8 — Interview preparation

## Q1. What is the difference between Acceptance Criteria and DoD?

**Simple answer:**

Acceptance criteria are specific to one user story and describe what that feature must do. The Definition of Done is a team-wide checklist that applies to every story and defines the minimum quality standard.

**Strong answer:**

Acceptance criteria define feature-specific behavior from the user's perspective. The DoD defines the common quality bar every story must meet before it is complete. A story may pass all acceptance criteria but still fail the DoD if peer review, CI tests, documentation, or other agreed checks are incomplete. Both must be satisfied.

## Q2. What is BDD?

**Simple answer:**

BDD is a collaborative approach that defines requirements through expected user behavior. It commonly uses Given-When-Then scenarios.

**Strong answer:**

BDD brings business stakeholders, developers and testers together to discuss how a feature should behave before implementation. The team expresses agreed behavior in Gherkin scenarios: Given defines the precondition, When describes the action, and Then states the observable result. These scenarios improve shared understanding and can support manual and automated testing.

## Q3. What is shift-left testing?

**Simple answer:**

Shift-left means bringing quality and testing activities earlier into the development process.

**Strong answer:**

QA participates in backlog refinement, reviews requirements, asks questions about edge cases, and helps define acceptance criteria before development. This catches misunderstandings early and reduces late rework. It complements, rather than replaces, later test execution.

## Q4. What is backlog refinement?

**Simple answer:**

Backlog refinement is the activity where the team reviews upcoming work before a sprint and clarifies requirements, scope and acceptance criteria.

**Strong answer:**

During backlog refinement, testers help identify ambiguity, missing behavior, edge cases and testability gaps in upcoming stories. The team uses this discussion to make work clearer before sprint execution, reducing surprises during development and testing.

## Q5. How do you write a BDD scenario?

**Simple answer:**

I use Given for the starting condition, When for the action, and Then for the observable expected result.

**Strong answer:**

First, I clarify the user story and identify the behavior to validate. Then I define the precondition using Given, the user action using When, and a specific observable outcome using Then. I create separate scenarios for the happy path and relevant negative paths, ensuring each scenario is clear enough to produce a Pass or Fail result.

---

# Module 8 — Practice and mentor assessment

## Exercise 1 — Explain in your own words

1. Last-day testing problem kya hai?
2. Backlog refinement mein QA ka role kya hai?
3. Shift-left ka practical benefit kya hai?
4. DoD ko “floor, not ceiling” kyun kaha gaya hai?
5. Ek story AC pass karke bhi DoD fail kaise kar sakti hai?

## Exercise 2 — BDD writing

User story:

“As a registered customer, I want to view my order history.”

At least 4 Given-When-Then scenarios likho:
- Happy path: user with past orders.
- Empty state: user with no orders.
- Order detail navigation.
- Unauthenticated user tries to access order history.

**Note:** Ye exercise ke scenarios mentor-created practice prompts hain; uploaded course solution key order-history scenarios provide nahi karti.

## Exercise 3 — DoD checklist

A story ke acceptance criteria pass ho gaye. Lekin:
- Peer review pending.
- Unit tests pass.
- QA verification pass.
- One high-severity defect open.
- Documentation updated.
- Product Owner approval pending.

Kya story Done hai? Har incomplete item ko identify karke explain karo.

## Exercise 4 — Jira / ADO mapping

1. Jira ticket ka Azure DevOps equivalent kya hai?
2. Jira Scrum board ka Azure DevOps equivalent kya hai?
3. Azure DevOps mein Acceptance Criteria kahan milta hai, as per course video?
4. `In QA` column ka purpose kya hai?

## Progress tracker

- [ ] Testing throughout sprint
- [ ] Backlog refinement and tester questions
- [ ] Shift-left testing
- [ ] Definition of Done
- [ ] Standard DoD checklist
- [ ] Acceptance Criteria vs DoD
- [ ] QA role in DoD enforcement
- [ ] BDD fundamentals
- [ ] Gherkin / Given-When-Then
- [ ] Happy path and negative path
- [ ] MindBridge login BDD scenarios
- [ ] Manual Pass/Fail validation
- [ ] Jira Scrum board setup
- [ ] Jira backlog import
- [ ] Azure DevOps organization/project/board/backlog
- [ ] Jira ↔ Azure DevOps mapping
- [ ] Practical exercises completed

---

## Source coverage & accuracy notes

- ZIP contains two main readings: **The Definition of Done (DoD)** and **Writing BDD Acceptance Criteria**.
- It includes subtitles and detailed transcript PDFs for **Testing at the Speed of Sprints**, **Guided Setup: Jira Configuration and Backlog Import**, and **ADO Translation: Navigating Backlogs in Azure DevOps**.
- It includes a DOCX lab guide for importing backlog data, writing BDD scenarios and validating them manually against MindBridge.
- It includes a BDD solution key and two copies of the same Sprint 1 backlog CSV; duplicate CSVs were not treated as separate exercises.
- The MindBridge solution key contains five scenarios: successful login, incorrect password, empty email, unregistered email, and empty password.
- The solution key states that the lab build has no seeded defects and all listed scenarios should pass.
- The Jira video narration mentions 12 imported issues and five mapped fields. However, the supplied CSV contains 3 records and 3 columns, and the DOCX lab guide also says 3 backlog items. This source inconsistency is explicitly preserved rather than silently reconciled.
- Jira transcript uses some UI labels that may vary between Jira versions; this guide preserves the workflow concept rather than guaranteeing current UI placement.
- Azure DevOps video maps Jira space to organization, ticket to work item, board to board, backlog to backlogs, and workflow columns to board columns/states.
- Order-history BDD exercise and integrated MindBridge lifecycle example are mentor-created practice material, not source solution-key content.
