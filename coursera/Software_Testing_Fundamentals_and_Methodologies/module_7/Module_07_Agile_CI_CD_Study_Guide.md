# Module 7 — Agile, CI/CD & QA Integration

> **QA / SDET Mentor Study Notes**
>
> Ye document sirf uploaded **Module 7 — Agile CI-CD** ZIP ke content par based hai. Explanations Hinglish mein hain. Extra practical examples ko **Mentor-created example** label kiya gaya hai, taaki course content aur additional teaching mix na ho.

---

## 🎯 Learning outcomes

Is module ke baad aap:
- Waterfall, Agile aur CI/CD ke differences explain kar paoge.
- Agile sprint ke planning, development aur sprint-end stages mein QA ka role samajh paoge.
- Shift-left testing ka meaning aur benefit explain kar paoge.
- CI/CD pipeline mein Unit, Integration aur End-to-End tests ka sequence samajh paoge.
- Automated test fail hone par pipeline kyun stop hoti hai, explain kar paoge.
- QA automation engineer ke role ko modern delivery process se connect kar paoge.

---

# Part 1 — Waterfall vs Agile vs CI/CD

## WHY — Humein development models kyun samajhne chahiye?

Software teams alag-alag tareeke se software plan, build, test aur release karti hain. Iska direct impact QA ke kaam par padta hai.

Agar team Waterfall follow karti hai, to testing ka major phase development ke baad aa sakta hai. Agile mein tester sprint ke start se hi involved hota hai. CI/CD mein automated checks code changes ke saath pipeline mein execute hote hain.

**Tester ke liye important question:** Team ka development model kya hai, aur us model mein quality ensure karne ka kaam kab aur kaise hota hai?

## 1.1 Waterfall Model

### Hinglish explanation

Waterfall ko ek staircase ya waterfall ki tarah imagine karo. Pehle requirements finalize, phir design, phir coding, phir testing, phir deployment aur maintenance.

Traditional Waterfall mein ek phase largely complete hone ke baad next phase start hota hai. Isliye process sequential hota hai.

### Course reading ke six phases

| Phase | Kya hota hai? |
|---|---|
| Requirements | Business needs upfront document hoti hain |
| System Design | Architects technical blueprint banate hain |
| Implementation | Developers code likhte hain |
| Testing | QA completed product test karti hai |
| Deployment | Product users ko release hota hai |
| Maintenance | Release ke baad bugs fix aur updates hote hain |

### Waterfall kab useful ho sakta hai?

Course reading ke according:
- Requirements clearly defined hon.
- Requirements ke change hone ki possibility low ho.
- Scope aur deadline fixed ho.
- Government contracts ya compliance-driven projects jaise contexts hon.

### QA risk — Late testing

Agar requirement mein mistake hui aur testing ke time discover hui, to team ko earlier phase par wapas jaana pad sakta hai. Isse rework, time aur cost badh sakti hai.

**Example (mentor-created):** Checkout requirement mein tax calculation ka rule galat define hua. Developers ne usi rule ke basis par implementation kar di. QA ko issue final testing mein mila. Ab requirement, design aur code teeno review karne pad sakte hain.

[!WARNING]
Waterfall ka main QA concern sirf ye nahi ki process sequential hai. Important risk ye hai ki defect late discover ho sakta hai, jab correction expensive aur disruptive ho.

## 1.2 Agile Model

### Hinglish explanation

Agile mein poora product ek baar mein banakar end par deliver karne ke bajay, work ko chhote repeating cycles mein divide kiya jata hai. In cycles ko **sprints** kaha jata hai.

Course reading ke according sprints typically **1–4 weeks** ke hote hain. Har sprint ke end par working, tested software increment deliver kiya jata hai. Feedback collect hota hai, priorities adjust hoti hain aur next sprint start hota hai.

### Agile ki key characteristics

| Characteristic | Simple meaning |
|---|---|
| Sprints | Short, time-boxed development cycles |
| Cross-functional teams | Developers, testers, designers, stakeholders collaborate karte hain |
| Continuous feedback | Stakeholder feedback ke basis par priorities/requirements evolve ho sakti hain |
| Early and frequent testing | QA har sprint mein involved hota hai, sirf end mein nahi |

### Agile mein QA ka role

Traditional gatekeeper mindset se shift hokar QA active collaborator banta hai:
- Requirements clarify karta hai.
- Acceptance criteria define karne mein help karta hai.
- Developers ke saath test cases prepare karta hai.
- Early bugs identify karta hai.
- Sprint ke dauran automated aur exploratory testing karta hai.
- Team ke shared Definition of Done mein quality contribute karta hai.

**Example (mentor-created):** E-commerce team ek sprint mein product search filter deliver karti hai. QA sprint planning mein clarify karta hai ki price range inclusive hai ya exclusive, phir sprint ke dauran test cases aur automation prepare karta hai, aur sprint end par regression run karta hai.

## 1.3 CI/CD — Automation ke saath frequent delivery

### Hinglish explanation

Agile work ko short cycles mein deliver karta hai. CI/CD code changes ko frequently integrate, automatically build aur test karne ke liye pipeline automation use karta hai.

Course reading CI/CD ko Agile ka replacement nahi, balki frequent delivery ko automation se accelerate karne wala approach batati hai.

### Continuous Integration (CI)

- Developers code changes shared repository mein frequently merge karte hain.
- Merge/commit par automated build aur tests trigger ho sakte hain.
- Test fail ho to team ko alert milta hai.
- Issue ko jaldi fix kiya jata hai, before it compounds.

### Continuous Deployment (CD) — Module source terminology

Course reading CD ko **Continuous Deployment** ke roop mein explain karti hai:
- CI process se validated code aage deploy hota hai.
- Automated checks pass hone ke baad code staging ya production environment mein automatically deploy ho sakta hai.
- Isse changes users tak minutes mein pahunch sakte hain, manual intervention ke bina.

> **Source terminology note:** Is module mein CD ka expansion “Continuous Deployment” diya gaya hai. Notes mein course ki terminology preserve ki gayi hai.

### CI/CD mein QA ka role

- Automated test scripts likhna aur maintain karna.
- Pipeline test results monitor karna.
- Failures investigate karna.
- Reliable automated safety net maintain karna.
- Frequent changes ke saath quality checkpoints ko effective rakhna.

## 1.4 Side-by-side comparison

| Area | Waterfall | Agile | CI/CD |
|---|---|---|---|
| Main idea | Sequential phases | Short iterative cycles | Automated integration and delivery/deployment pipeline |
| Work delivery | Larger planned release | Working increment per sprint | Validated changes can move through pipeline frequently |
| Feedback | Often later/formal stages | Repeated during sprints | Automated checks give rapid technical feedback |
| QA involvement | Testing phase can be late | QA throughout sprint | Automation integrated into pipeline |
| QA focus | Execute planned testing and report defects | Collaborate, prevent and detect defects early | Build/maintain/monitor automated checks |

[!IMPORTANT]
Agile aur CI/CD ko exact same cheez mat samajhna. Agile ek development approach hai; CI/CD automated integration and delivery/deployment practices/pipeline hai. Course inhe connected batata hai, interchangeable nahi.

## 🎤 Interview answer — Waterfall, Agile, CI/CD

**Simple English:**

Waterfall is a sequential development model where phases are completed one after another. Agile delivers software in short iterations called sprints and encourages continuous feedback. CI/CD automates code integration, builds, tests, and deployment so that changes can be delivered more frequently and safely.

**Stronger answer:**

Waterfall follows a planned sequence of phases, so testing may happen late and changes can cause significant rework. Agile breaks work into short sprints, with cross-functional collaboration, early testing, and frequent feedback. CI/CD complements frequent delivery by automating builds and quality checks whenever code is integrated, and by moving validated changes through deployment stages. From a QA perspective, the role shifts from late-stage defect detection toward early collaboration, test automation, and continuous quality feedback.

**Keywords:** sequential, sprint, iterative, cross-functional, continuous feedback, CI, CD, automated pipeline.

---

# Part 2 — Mapping QA activities to Agile sprint phases

## WHY — Agile mein testing “last phase” kyun nahi hai?

Waterfall mein testing ko ek later phase ke roop mein describe kiya ja sakta hai. Agile mein testing development ke parallel chalti hai. Quality sirf tester ki responsibility nahi; developers, testers aur product owners sab contribute karte hain.

Course reading ka central idea:

> **Testing is an activity throughout the sprint, not a separate final phase.**

## 2.1 Sprint Planning — Development se pehle

### Tester kya karta hai?

**1. Requirements clarify karna**

User story mein ambiguity ya missing detail identify karna.

Course reading ka example:
“As a user, I want to export a report.”

Tester ke questions:
- Format CSV hoga ya PDF?
- Report mein data na ho to kya hoga?
- Maximum kitni rows support hongi?

**2. Acceptance criteria define karna**

Acceptance criteria specific, testable conditions hoti hain jinhe user story “done” hone ke liye satisfy karna hota hai.

Course reading ka example:

- Given I am a logged-in user,
- When I click the “Export to CSV” button,
- Then a file named `report.csv` is downloaded,
- And it contains the correct data.

Isse expected behavior measurable aur testable ban jata hai.

**3. Test planning and strategy**

Tester high-level plan banata hai:
- Kya automate hoga?
- Kahan manual exploratory testing chahiye?
- Risks aur dependencies kya hain?

### Simple takeaway

Sprint planning mein tester ka goal hai: **feature banne se pehle hi expected behavior clear karna.**

## 2.2 Active Sprint — Development ke dauran

### Tester kya karta hai?

**1. Automated tests likhna**

Developer feature build kar raha hota hai, QA parallel mein automation scripts likh sakta hai. Baad mein ye tests regression suite mein add kiye ja sakte hain.

**2. Exploratory testing**

Automation known paths ko repeat karne mein useful hai. Lekin unexpected behavior, unusual combinations aur edge cases explore karne ke liye human investigation bhi zaroori hai.

Course reading example:
- Data analyst ek malformed data file upload karta hai.
- Tester check karta hai ki application us file ko gracefully handle karti hai ya crash hoti hai.

**3. Integration and API testing**

Individual components complete hone par tester check karta hai ki modules correctly connect aur communicate kar rahe hain. Iske liye APIs test ki ja sakti hain.

**4. Defect management**

- Clear reproducible steps ke saath bug log karo.
- Developer ke saath diagnosis mein collaborate karo.
- Fix ready hone par retest karo.

### Simple takeaway

Active sprint mein tester ka goal hai: **fast feedback dena, bugs jaldi identify karna aur feature ko continuously validate karna.**

## 2.3 Sprint End — Showcase and Release

### Tester kya karta hai?

**1. Final verification**

Completed user stories ko acceptance criteria ke against verify karna.

**2. Regression testing**

Automated regression suite run karna, taaki new functionality existing features ko break na kare.

**3. Sprint demo support**

Sprint review/demo mein feature stakeholders ko demonstrate karne mein help karna aur confirm karna ki feature unki needs meet karta hai.

**4. Release testing / Smoke tests**

Agar sprint ke end par production deployment hota hai, to deployment ke baad limited smoke tests kiye ja sakte hain, taaki critical functions aur application stability verify ho.

## 2.4 Agile sprint QA summary

| Sprint stage | QA activity | Main purpose |
|---|---|---|
| Sprint Planning | Requirements clarification | Ambiguity/missing details discover karna |
| Sprint Planning | Acceptance criteria | “Done” ko testable banana |
| Sprint Planning | High-level test strategy | Automation, exploratory scope, risks identify karna |
| Active Sprint | Automated test writing | Repeatable checks prepare karna |
| Active Sprint | Exploratory testing | Unexpected defects/edge cases discover karna |
| Active Sprint | Integration/API testing | Components ke communication ko validate karna |
| Active Sprint | Defect management and retesting | Fix verify karna |
| Sprint End | Final verification | Acceptance criteria confirm karna |
| Sprint End | Regression | Existing features protect karna |
| Sprint End | Demo support | Stakeholder feedback/confirmation |
| Sprint End / Release | Smoke tests | Deployment ke baad critical health validate karna |

## 🎤 Interview answer — QA in Agile

**Simple English:**

In Agile, testing happens throughout the sprint. Testers clarify requirements and acceptance criteria during planning, perform automation, exploratory, API and integration testing during development, and run final verification and regression testing before the sprint review or release.

**Stronger answer:**

Agile testing is continuous rather than a separate phase at the end. During sprint planning, QA helps clarify user stories, define acceptance criteria, and identify risks and test strategy. During active development, QA writes automated tests, performs exploratory and API/integration testing, manages defects, and retests fixes. At sprint end, QA verifies acceptance criteria, runs regression tests, supports the demo, and may perform controlled smoke testing after deployment. This allows the team to detect issues earlier and provide rapid feedback.

**Keywords:** continuous testing, acceptance criteria, exploratory testing, API testing, regression, retesting, smoke testing.

---

# Part 3 — Shift-left testing

## WHY — Defect ko jaldi find karna kyun useful hai?

Imagine karo building banne ke baad pata chale ki foundation ka design hi wrong tha. Ab correction karna expensive aur difficult hoga.

Software mein bhi agar requirement unclear hai aur QA usse development ke baad discover karta hai, to rework badh sakta hai. Agar tester planning ke time hi ambiguity identify kar le, to team implementation se pehle issue resolve kar sakti hai.

## WHAT — Shift-left

**Shift-left** ka meaning hai quality/testing activities ko development lifecycle mein earlier stages par le aana.

Course reading ke according, QA early involvement ke through:
- Requirements clarify karta hai.
- Acceptance criteria define karne mein help karta hai.
- Test planning early karta hai.
- Defects prevent karne ki koshish karta hai, sirf end mein detect nahi.

## HOW — Example

**Mentor-created example:** User story: “User can reset password.”

Late testing approach:
- Developer feature complete karta hai.
- QA ko test karte waqt pata chalta hai ki reset link expiry behavior define hi nahi tha.
- Requirement clarify karne aur implementation change karne mein rework hota hai.

Shift-left approach:
- Sprint planning mein QA poochta hai: reset link kitni der valid rahega?
- Expired link click karne par kya message aayega?
- Already-used link dobara use ho sakta hai?
- Acceptance criteria finalize hote hain.
- Developer implementation se pehle expected behavior clear hota hai.

## Shift-left ka practical benefit

- Ambiguity early identify hoti hai.
- Testability improve hoti hai.
- Defects prevent karne ke chances badhte hain.
- Rework late stage par discover hone ke comparison mein kam ho sakta hai.
- QA team product decisions mein meaningful contribution karti hai.

[!NOTE]
Shift-left ka matlab ye nahi ki later testing unnecessary ho gayi. Early reviews ke saath execution, regression, end-to-end aur release checks bhi important hain.

## 🎤 Interview answer — Shift-left

**Simple English:**

Shift-left means moving testing and quality activities earlier in the software development lifecycle. QA participates in requirement reviews, acceptance criteria, and test planning before or during development.

**Stronger answer:**

Shift-left is a quality approach in which testing is introduced as early as possible instead of waiting until development is complete. QA reviews user stories, identifies ambiguity, helps define testable acceptance criteria, and plans test coverage early. This helps prevent defects at their source and reduces the cost and disruption of late rework. It does not eliminate later testing; it complements execution and regression activities.

**Keywords:** early involvement, requirement review, acceptance criteria, defect prevention, early feedback, reduced rework.

---

# Part 4 — QA checkpoints inside a CI/CD pipeline

## WHY — CI/CD pipeline mein automated tests kyun?

Course video car factory ki analogy use karta hai. Car ka blueprint code hai. Developer jab change add karta hai, wo commit hota hai. Har change ke baad automated assembly line quality checks chalati hai.

Agar har code change ko manually test karna pade, to frequent integration/delivery slow ho jayegi. Automated checkpoints repeatable feedback dete hain.

## WHAT — Pipeline

CI/CD pipeline ek automated workflow hai jo code changes ko build, test aur deployment stages se move kar sakta hai.

Module video ka learning focus:
- Unit, Integration aur End-to-End tests ka sequence.
- Test failure par pipeline stop karna.
- Failed code ko live application tak pahunchne se rokna.

## 4.1 Step-by-step pipeline (video sequence)

<CodeBlock language="text" editable>
Developer commit
      |
      v
Continuous Integration starts
      |
      v
Unit Tests (isolated checks)
      |
      | pass
      v
Build Stage (assemble working app)
      |
      v
Integration Tests
      |
      | pass
      v
End-to-End Tests
      |
      | pass
      v
Continuous Deployment
      |
      v
Application deployed
</CodeBlock>

**Important:** Ye diagram uploaded video ke explained sequence ko represent karta hai. Real organizations pipelines mein additional stages, parallel jobs, security checks, approvals aur different test ordering configure kar sakti hain; ye extra details is module transcript mein specify nahi ki gayi hain.

## 4.2 Commit

Commit ka simple meaning: developer apne code changes ko version-control repository mein record karta hai.

Course analogy:
- Car blueprint = code.
- Blueprint mein new improvement add karna = commit.
- Commit ke baad automated assembly line trigger hoti hai.

## 4.3 Unit Test — Small part in isolation

Car analogy mein pehle door handle ko separately check karte hain. Abhi poori car mein install karke test nahi kar rahe.

Software mein unit test individual component/function ko isolation mein verify karta hai.

**Mentor-created example:**
- Function `calculate_discount()` ko input price aur discount percentage do.
- Expected calculated amount verify karo.
- Database, UI ya external service ko involve karna zaroori nahi, agar test ka goal function ko isolate karna hai.

Video ke according agar unit test fail ho, pipeline immediately stop hoti hai jab tak developer fix na kare.

## 4.4 Build Stage

Unit checks pass hone ke baad software ke different pieces ko combine karke working application version create kiya jata hai.

**Simple analogy:** Car ke individual parts check hone ke baad unhe assemble karna.

## 4.5 Integration Test — Components together

Door handle, door, lock aur electrical system aapas mein correctly work kar rahe hain ya nahi.

Software mein modules/services/components ke beech communication verify hota hai.

**Mentor-created example:**
- Checkout service payment service ko request bhejti hai.
- Payment response checkout service ko correct format mein milta hai.
- Order service payment result ke basis par order status update karti hai.

## 4.6 End-to-End (E2E) Test — User journey

Video ke according E2E test real user journey simulate karta hai aur entire experience ko start se finish tak verify karta hai.

**Mentor-created example:**
1. User login karta hai.
2. Product search karta hai.
3. Product cart mein add karta hai.
4. Checkout complete karta hai.
5. Order confirmation verify karta hai.

E2E test ka focus isolated function nahi, poora connected workflow hai.

## 4.7 Test fail ho to kya hota hai?

Video ke according:
- Pipeline stop hoti hai.
- Team ko red alert/notification milta hai.
- Notification batati hai kaunsa test fail hua aur kyun.
- Developer issue fix karta hai.
- Required tests pass hone ke baad hi pipeline aage proceed karti hai.

[!IMPORTANT]
Pipeline ko fail par stop karna quality gate hai. Iska purpose faulty build ko next stage ya deployment tak pahunchne se rokna hai. Failed test ko ignore karke green status dikhana safe practice nahi hai.

## 4.8 Continuous Deployment

Video CD ko Continuous Deployment ke roop mein explain karta hai. Automated quality checks pass hone ke baad system validated code ko automatically ship/deploy karta hai.

Course video ka central message: QA ek slow manual step at the end nahi; automated checkpoints pipeline mein embedded hote hain.

## CI/CD pipeline test sequence summary

| Stage | Check | Kya validate hota hai? |
|---|---|---|
| Commit / CI trigger | Code change submitted | Pipeline starts |
| Unit tests | Individual units | Small component isolation mein correct hai |
| Build | Working app assembled | Pieces combine hokar build banate hain |
| Integration tests | Connected components | Modules communicate correctly |
| E2E tests | Complete user journey | End-to-end experience works |
| CD | Deployment | Passed build environment/users tak deploy hoti hai |

## 🎤 Interview answer — QA in CI/CD

**Simple English:**

In a CI/CD pipeline, automated tests run at different checkpoints. Unit tests validate individual components, integration tests validate communication between components, and end-to-end tests validate complete user journeys. If a test fails, the pipeline can stop and notify the team so the defect is fixed before deployment.

**Stronger answer:**

QA is integrated into the CI/CD pipeline through automated quality gates. When a developer commits code, the CI process triggers a build and automated checks. Unit tests validate isolated components. After the build is assembled, integration tests verify communication between modules, followed by end-to-end tests that simulate real user workflows. If a required test fails, the pipeline is stopped and the team is notified. Once the issue is fixed and the checks pass, validated code can proceed to deployment. This provides fast feedback and reduces the risk of defective changes reaching users.

**Keywords:** commit, CI trigger, build, unit test, integration test, E2E, quality gate, pipeline failure, deployment.

---

# Part 5 — Connect this module to Playwright and Pytest

> **Mentor-created application examples:** The uploaded module explains test categories and CI/CD sequence. The following examples connect those ideas to your Python/Playwright practice; they are not presented as code copied from the course.

| Pipeline concept | Python / QA example |
|---|---|
| Unit test | Pytest test for a pure Python calculation function |
| Integration test | API/service interaction test using `requests` |
| E2E test | Playwright browser flow: login → search → cart → checkout |
| Regression test | Re-run existing critical tests after a change |
| Smoke test | Quick check of critical app functions after deployment |
| Pipeline failure | Pytest non-zero exit status causes required pipeline job to fail |

### Example: E-commerce test suite organization

```text
tests/
├── unit/
│   └── test_discount.py
├── integration/
│   └── test_order_api.py
└── e2e/
    ├── test_login.py
    └── test_checkout.py
```

**Important:** Folder names and exact pipeline configuration are mentor-created examples. The course reading lists unit, integration, regression and smoke tests as common automated tests in CI/CD; the video focuses on unit → build → integration → E2E sequence.

---

# Part 6 — Common mistakes and misconceptions

1. **Agile = no documentation/planning** — wrong. Agile mein planning hoti hai, but feedback ke saath adapt bhi kiya jata hai.
2. **Agile = CI/CD** — wrong. Agile development approach hai; CI/CD automation practices/pipeline hai.
3. **QA sirf sprint ke end mein test karta hai** — wrong. QA planning se sprint-end tak involved hota hai.
4. **Shift-left means only early testing** — incomplete. Early quality work later testing ko replace nahi karta.
5. **Unit, Integration and E2E same hain** — wrong. Scope and purpose different hain.
6. **Pipeline fail hone ke baad bhi deploy kar dena normal hai** — module ke explained quality-gate flow ke opposite hai.
7. **Automation means no manual testing** — wrong. Agile reading explicitly exploratory testing ko bhi important batati hai.
8. **CI/CD always means production deployment after every commit** — uploaded reading describes automatic deployment of validated code to staging or production; actual deployment target and controls pipeline configuration par depend karte hain.

---

# Module 7 — Practice exercises

## Exercise 1 — Identify the model

Har statement ko Waterfall, Agile ya CI/CD se match karo:

1. Requirements, design, implementation, testing, deployment, maintenance sequentially complete hote hain.
2. Team short sprints mein working increments deliver karti hai.
3. Code commit ke baad automated tests trigger hote hain.
4. QA sprint planning mein acceptance criteria clarify karta hai.
5. Test failure par pipeline stop hoti hai.

## Exercise 2 — Agile QA activities

User story:

“As a registered customer, I want to download my invoice so that I can keep a record of my purchase.”

Sprint planning mein tester ke minimum 5 clarification questions likho.

Then:
- Ek Given/When/Then acceptance criterion likho.
- Active sprint ke liye 2 automation ideas aur 2 exploratory ideas likho.
- Sprint end ke liye regression aur smoke test ka ek-ek example do.

## Exercise 3 — CI/CD sequence

Correct order arrange karo:

- Integration tests
- Commit
- Build
- End-to-end tests
- Unit tests
- Deployment

Then explain:
- Unit test fail hua to kya hoga?
- Integration test fail hua to team ko kya information chahiye?
- E2E tests ka purpose unit tests se kaise different hai?

## Exercise 4 — Real-world scenario

E-commerce application mein developer ne checkout calculation change ki.

Explain:
1. Agile sprint mein QA kab involved hoga?
2. Shift-left ke through requirement ambiguity kaise find karoge?
3. CI pipeline mein kaunse automated tests useful honge?
4. E2E test ka user journey kya ho sakta hai?
5. Required pipeline test fail ho to release par kya impact hona chahiye?

---

# Module 7 — Progress tracker

- [ ] Waterfall model and six phases
- [ ] Agile model and sprint concept
- [ ] CI/CD meaning and relationship with Agile
- [ ] Waterfall vs Agile vs CI/CD comparison
- [ ] QA role in sprint planning
- [ ] Acceptance criteria
- [ ] QA activities during active sprint
- [ ] Sprint-end verification, regression and smoke testing
- [ ] Shift-left approach
- [ ] Commit and CI trigger
- [ ] Unit test checkpoint
- [ ] Build stage
- [ ] Integration test checkpoint
- [ ] End-to-end test checkpoint
- [ ] Pipeline failure and quality gate
- [ ] Continuous Deployment
- [ ] Practical exercises completed

## Source coverage and accuracy notes

- ZIP contains two reading files: **Contrasting Agile, CI/CD, and Waterfall** and **Mapping Testing Activities to Agile Phases**.
- It also contains subtitle text/VTT for the CI/CD pipeline video and a detailed visual transcript PDF. Duplicate subtitle formats were treated as alternate representations of the same video, not as separate lessons.
- The Waterfall reading shows six phases: Requirements, System Design, Implementation, Testing, Deployment, Maintenance.
- The Agile reading describes sprints as typically 1–4 weeks and highlights cross-functional collaboration, continuous feedback and early/frequent testing.
- The Agile mapping reading organizes QA work into Sprint Planning, active Sprint, and sprint-end Showcase/Release activities.
- The CI/CD video explains commit → unit tests → build → integration tests → end-to-end tests → continuous deployment, with pipeline stop/alert on failure.
- The reading lists unit, integration, regression and smoke tests as common automated tests in CI/CD. The video sequence specifically focuses on unit, integration and E2E checks.
- The CI/CD video transcript calls CD “Continuous Deployment”; this guide preserves that source terminology.
- The ZIP does not provide a full Scrum framework lesson, detailed CI tool configuration, or a specific GitHub Actions/Jenkins YAML pipeline. Those topics are not represented as course content here.
- E-commerce examples, Python/Playwright connections and code/folder examples are mentor-created learning aids.
