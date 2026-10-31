# Module 6 — Waterfall Model, V-Model & Agile Foundations

> **Mentor notes | QA / Software Testing**
>
> Ye file sirf Module 6 ke uploaded material par based hai. Course ke concepts ko Hinglish mein explain kiya gaya hai. Jahan practical example mentor-created hai, wahan clearly label kiya gaya hai.

## 🎯 Module outcome

Is module ke baad aap:
- SDLC aur STLC ka purpose explain kar paoge.
- Waterfall model ka sequential flow aur QA risk samajh paoge.
- V-Model mein development phases aur corresponding testing levels ka relationship samajh paoge.
- Agile approach ko Waterfall se compare kar paoge.
- Jira/Azure DevOps board par work ko phases/tasks ke saath align karne ka basic idea samajh paoge.

---

# Part 1 — SDLC aur STLC: big picture

## WHY — Process ki zaroorat kyun?

Software banana sirf code likhna nahi hai. Requirements samajhna, design karna, build karna, verify karna, release karna aur maintain karna bhi zaroori hai. Agar team ke paas shared process nahi hoga, to tasks miss ho sakte hain, responsibilities unclear ho sakti hain aur defects late discover ho sakte hain.

## WHAT

- **SDLC (Software Development Life Cycle):** Software ko plan, design, build, test, deploy aur maintain karne ka broader lifecycle.
- **STLC (Software Testing Life Cycle):** Testing work ko organize karne ka structured lifecycle—requirements samajhne se test closure/reporting tak.

**Relationship:** STLC, SDLC ke andar testing-focused activities ko structure karta hai. Testing ek isolated last-minute activity nahi honi chahiye; quality work lifecycle ke multiple stages mein hota hai.

## HOW — Example

**Mentor-created example:** E-commerce app mein order tracking feature:
- SDLC view: business need → design → development → testing → deployment → maintenance.
- STLC view: requirement analysis → test planning → test design → environment setup → test execution → test cycle closure.

---

# Part 2 — Waterfall Model

## WHY — Waterfall model kyun samajhna chahiye?

Har project iterative speed ke liye design nahi hota. Aerospace, automotive aur medical-device manufacturing jaise high-stakes areas mein upfront planning, documentation, verification aur regulatory controls bahut important ho sakte hain. Physical manufacturing shuru hone ke baad design change karna bahut expensive ya practically impossible ho sakta hai.

## WHAT — Waterfall model

Waterfall ek **linear, sequential project-management approach** hai. Project distinct phases mein aage badhta hai; traditional form mein ek phase largely complete aur formally reviewed hone ke baad next phase shuru hota hai.

Course transcript ke diagram mein five phases:
1. Requirements
2. Design
3. Implementation
4. Verification
5. Maintenance

> Note: Different organizations/books Waterfall phases ko slightly different labels or granularity mein present kar sakte hain. Yahan course transcript ke five-phase representation ko follow kiya gaya hai.

## HOW — Flow samjho

`Requirements → Design → Implementation → Verification → Maintenance`

### 1. Requirements
Project ko kya karna hai, kya constraints hain, kya expected outcomes hain—ye define hota hai.

### 2. Design
Requirements ke basis par solution/architecture/design prepare hota hai.

### 3. Implementation
Actual development/coding ya product construction hota hai.

### 4. Verification
Built product ko requirements ke against verify/test kiya jata hai.

### 5. Maintenance
Release ke baad fixes, updates aur ongoing support.

## QA risk — Defects late milna

Waterfall ka important QA risk hai: requirement ya design stage mein introduce hua defect formal testing ke waqt late discover ho sakta hai.

Example:
- Requirement mein discount rule galat define hua.
- Design aur implementation usi wrong requirement par based rahe.
- Verification mein issue discover hua.
- Ab requirement, design aur code tak rework karna pad sakta hai.

**Key chain:** Early defect → late discovery → larger rework → higher cost/time.

## Waterfall kab suitable ho sakta hai?

Course material ke examples:
- Extensive planning and documentation required.
- Regulatory compliance important.
- Strict contractual milestones.
- Aerospace, automotive, medical-device manufacturing jaise high-stakes/physical engineering contexts.

[!NOTE]
Course ka point ye nahi ki Waterfall har software project ke liye best hai. It explains why structured, sequential approaches remain relevant where requirements, safety and physical manufacturing constraints demand strong upfront control.

## 🎤 Interview answer

**Simple English:**

Waterfall is a linear and sequential development model. The project moves through phases such as requirements, design, implementation, verification, and maintenance. Each phase is largely completed before the next begins.

**Stronger answer:**

The Waterfall model organizes work into distinct, sequential phases with formal reviews or gates. It supports upfront planning and documentation, which can be valuable in regulated or hardware-dependent industries. Its major QA risk is that formal testing may happen late, so defects introduced in requirements or design can be discovered only after substantial implementation, making rework more expensive.

**Keywords:** linear, sequential, phase gates, upfront planning, documentation, late defect discovery, rework.

---

# Part 3 — V-Model

## WHAT — V-Model kya hai?

V-Model ko Waterfall ka verification-and-validation focused representation samajh sakte hain. Iska visual shape “V” jaisa hota hai:
- Left side: development/specification activities.
- Bottom: implementation/coding.
- Right side: corresponding testing activities.

**Important:** V-Model ka central idea hai ki development ke har major stage ke saath corresponding test level plan/design kiya jata hai. Testing planning ko end tak postpone nahi karna chahiye.

## Common correspondence

| Left side — Development / specification | Right side — Testing level |
|---|---|
| Business/User Requirements | Acceptance Testing |
| System Requirements | System Testing |
| High-Level Design / Architecture | Integration Testing |
| Low-Level / Detailed Design | Unit Testing |
| Implementation / Coding | V ka bottom; code is built |

The pairing is a common V-Model explanation. Exact naming can vary by organization and course diagram.

## Hinglish example

Maan lo e-commerce app ka requirement hai: “Customer successful payment ke baad order confirmation receive kare.”

- User/business requirement ke against Acceptance Test plan hoga: kya customer ka complete business flow satisfy hota hai?
- System requirements ke against System Test plan hoga: complete application payment and order flow requirements meet karta hai?
- Architecture/high-level design ke against Integration Test plan hoga: payment service, order service aur notification service sahi communicate karte hain?
- Detailed design ke against Unit Test plan hoga: individual functions/classes expected result dete hain?
- Implementation par code likha jata hai.

## V-Model ka QA benefit

- Test planning early start hoti hai.
- Requirements/design ke saath test thinking parallel chalti hai.
- Traceability improve ho sakti hai: requirement se related test identify karna easier.
- Defects ko late stage tak chhodne ka risk reduce karne mein help milti hai.

## Common confusion

- V-Model ka matlab ye nahi ki testing sirf coding ke baad hi sochi jati hai.
- V-Model aur Waterfall related hain, lekin exact same diagram/representation nahi.
- V-Model test levels ko development stages se pair karta hai; STLC phases ek testing-process sequence describe karte hain. Dono concepts ko mix mat karna.

## 🎤 Interview answer

**Simple English:**

The V-Model is a software development model in which each development phase has a corresponding testing phase. Test planning begins early, and testing levels are linked to requirements and design activities.

**Stronger answer:**

The V-Model emphasizes verification and validation by pairing development activities on the left side with corresponding test levels on the right. For example, user requirements map to acceptance testing, system requirements to system testing, architecture to integration testing, and detailed design to unit testing. This encourages early test planning and traceability rather than waiting until implementation is complete.

**Keywords:** verification, validation, early test planning, test levels, traceability, development-test pairing.

---

# Part 4 — Agile approach and comparison

## WHY — Agile ki zaroorat kyun?

Software requirements change ho sakti hain. Customer feedback, market needs aur new learning ke basis par team ko product adjust karna pad sakta hai. Purely sequential process mein changes ko earlier phases tak wapas le jaana expensive/slow ho sakta hai.

## WHAT — Agile (course framing)

Course video Agile ko more flexible and iterative approach ke roop mein contrast karta hai. Work smaller cycles/iterations mein organize hota hai, feedback liya jata hai aur product incrementally improve hota hai.

> The uploaded material introduces Agile as a flexible/iterative contrast to Waterfall. Is module ke source material se beyond detailed Scrum roles/events/ceremonies ko course content ke roop mein claim nahi kiya ja raha.

## Waterfall vs Agile

| Area | Waterfall | Agile |
|---|---|---|
| Flow | Linear, sequential | Iterative, incremental |
| Requirements | More upfront definition | Can evolve with feedback |
| Feedback | Often later at formal stages | Repeated during iterations |
| Change | Later changes may require significant rework | Designed to accommodate change more readily |
| Delivery | Often larger planned release | Smaller increments are common |
| QA implication | Risk of late defect discovery | QA feedback can happen repeatedly |

## QA engineer ka role

- Waterfall: requirements/design review early; test design and planning before formal execution; formal verification may be later in the flow.
- Agile: QA should collaborate early and continuously, clarify acceptance expectations, test increments and provide fast feedback.

**Mentor-created example:** Team har sprint mein checkout feature ka small increment deliver karti hai. QA har increment par functional/API/UI checks karta hai, bugs report karta hai aur regression scope update karta hai.

## 🎤 Interview answer

**Simple English:**

Waterfall is a sequential model where phases are completed one after another. Agile is iterative and flexible, allowing teams to deliver work in smaller increments and use feedback to adapt.

**Stronger answer:**

Waterfall emphasizes upfront planning, documentation and phase-based progression. Agile emphasizes iterative delivery, collaboration and feedback. From a QA perspective, Waterfall can create a risk of late defect discovery if testing is delayed, whereas Agile encourages continuous testing and earlier feedback. The right approach depends on project constraints, risk, compliance and the ability to accommodate change.

**Keywords:** sequential, iterative, incremental, feedback, flexibility, continuous testing, risk.

---

# Part 5 — Work tracking: Jira / Azure DevOps board

Uploaded module material includes a guided task-alignment activity and an Azure DevOps/Kanban board transcript. Board ka purpose work ko visible banana hai: task kya hai, kis phase/workstream se related hai, owner kaun hai, aur current status kya hai.

## Jira / Azure DevOps board ka basic idea

- Work items/tasks ko board par represent kiya jata hai.
- Columns workflow status show kar sakte hain, for example To Do, In Progress, Review, Done.
- Cards/tasks ko relevant phase or workstream se align karna hota hai.
- Board team ko progress, ownership aur blockers visible banata hai.

## QA project example (mentor-created)

| Work item | Example status |
|---|---|
| Review checkout requirement | To Do |
| Prepare payment test cases | In Progress |
| Configure QA test data | To Do |
| Execute payment regression | To Do |
| Report and retest defect | To Do |

**Remember:** Board columns and workflow names organization-specific hote hain. Jira aur Azure DevOps mein labels/configuration vary kar sakti hai.

## What to understand from the module activity

Uploaded ZIP mein:
- Jira task-alignment board CSV.
- Task-alignment instructions DOCX/PDF.
- Azure DevOps translation/Kanban board detailed transcript.
- V-Model task CSV.

Ye artifacts practical alignment exercise ke liye hain. CSV tasks ko blindly memorize karne ke bajay samjho ki task ko correct lifecycle phase/board lane mein kyun place kiya gaya hai.

---

# Part 6 — Common mistakes

1. SDLC aur STLC ko same thing bolna.
2. Waterfall aur V-Model ko identical kehna.
3. V-Model mein testing planning early hoti hai, ye miss kar dena.
4. Waterfall ka QA risk sirf “slow process” kehna; actual risk late defect discovery aur costly rework hai.
5. Agile ka matlab “no planning” samajhna.
6. Agile ko Scrum ke saath interchangeable term maan lena.
7. Jira/Azure DevOps board columns ko universal standard samajhna.

---

# Module 6 — Practice & progress tracker

## Quick knowledge check

1. SDLC aur STLC mein kya difference hai?
2. Waterfall ke five phases course ke according kaunse hain?
3. Waterfall mein early requirement defect late milne par cost kyun badh sakti hai?
4. V-Model mein user requirements ka corresponding test level kya hai?
5. V-Model mein detailed design ka corresponding test level kya hai?
6. Agile ko Waterfall se kaise distinguish karoge?
7. Jira/Azure DevOps board QA team ko kaise help karta hai?

## Practical exercise

**Scenario:** Food delivery application mein “Schedule Order” feature add ho raha hai.

A. Waterfall view mein requirements, design, implementation, verification aur maintenance activities identify karo.

B. V-Model view mein:
- User requirement ke liye acceptance test idea.
- System requirement ke liye system test idea.
- Integration design ke liye integration test idea.
- Detailed design ke liye unit test idea.

C. Agile view mein feature ko small increments mein kaise deliver/test karoge?

## Progress checklist

- [ ] SDLC vs STLC
- [ ] Waterfall model definition and phases
- [ ] Waterfall QA risk
- [ ] Waterfall use cases / constraints
- [ ] V-Model structure
- [ ] Development-to-testing correspondence
- [ ] Agile fundamentals
- [ ] Waterfall vs Agile comparison
- [ ] Jira/Azure DevOps board basics
- [ ] Practical scenario completed

## Source coverage & limitations

- Uploaded ZIP includes Waterfall video transcript, V-Model transcript, SDLC/STLC and Agile overview transcript, Jira task-alignment instructions/board CSV, Azure DevOps/Kanban transcript, and V-Model task CSV.
- The detailed transcript for Waterfall explicitly presents five phases: Requirements, Design, Implementation, Verification, Maintenance.
- Some transcripts include visual descriptions. These were used where they clarify the diagram or learning objective.
- V-Model mapping is explained using the standard correspondence represented in the course activity. Exact naming may vary across organizations.
- The course ZIP introduces Agile in contrast to Waterfall; detailed Scrum framework content is not added as if it came from the course.
- Jira/Azure DevOps board examples in the guide are explanatory mentor-created examples unless explicitly identified as source activity content.
