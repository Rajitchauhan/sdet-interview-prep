# 🧪 MODULE 3 — TEST PLANNING, RISK-BASED TESTING & DEFECT REPORTING
## Hinglish Mentor Notes | University of Minnesota — Introduction to Software Testing

> 🎯 **Module ka real objective:** Ab tak humne samjha testing kyun zaroori hai aur test kaise sochte hain. Is module mein professional tester ka kaam samjhenge: testing ko plan karna, risk ke basis par priorities decide karna, progress report karna, aur defect ko analyse karke close karwana.

> 🧭 **Notes ka use:** English lecture ko repeat karna mera objective nahi. Main instructor ki baat, unki examples/stories aur assignment resources ko tumhari Hinglish mein explain kar raha hoon.  
> `🎓 COURSE STORY` = lecture ki story/example.  
> `🧠 MENTOR EXPLAINS` = concept ko simple language mein todna.  
> `💼 SDET CONNECTION` = real project/automation mein use.  
> `⭐ INTERVIEW` = interview-ready response.  
> `🔴 IMPORTANT` = must-remember point.  
> `⚠️ SOURCE GAP` = ZIP ke available material mein exact detail nahi mili; wahan guess nahi karunga.

---

# 🗺️ 0. Module 3 mein kya-kya hai?

ZIP mein 10 lecture transcript sets aur 3 assignment resources (GolfScore SRS, test plan template, example test plan) mile. Lectures ka learning route:

| Lecture | Topic | Iska practical meaning |
|---|---|---|
| 1 | What goes into a Test Plan? | Test plan ka structure aur purpose |
| 2 | Test Planning Process / Testing Stages | Unit, DVT, SVT, customer acceptance |
| 3 | Test Reports / Test Status Reports | Stakeholders ko testing progress aur risk batana |
| 4 | Risk-Based Testing | Impact × likelihood ke basis par test priority |
| 5 | Software Defect Reports — Overview | Defect reporting kyun important hai |
| 6 | Defect Lifecycle — Analysis | Defect report karne se pehle analysis |
| 7 | Defect Lifecycle — Reporting | Clear, concise, reproducible defect report |
| 8 | Defect Report Components | Report ke fields, severity, priority, status, evidence |
| 9 | Defect Lifecycle — Tracking, Retest, Close | Fix follow-up, retest aur closure |
| Assignment | GolfScore Test Plan | SRS padhkar actual test plan + test cases banana |

**Difficulty:** Medium → Hard  
**Interview relevance:** High — Test Plan, Risk-Based Testing, Defect Lifecycle, Severity/Priority, Test Reporting.

---

# 1. 🎓 LECTURE 1 — What Goes Into a Test Plan?

## 1.1 Pehle testing stages ka context samjho

Instructor test plan samjhane se pehle testing ke stages revise karte hain.

| Stage | Main responsibility | Focus |
|---|---|---|
| **Unit Testing** | Primarily developer | Apne code ki low-level functionality aur error-prone constructs |
| **Design Verification Testing (DVT)** | Integration mainly developers; functional testing developers ya test team | Modules sahi tarah integrate hue? System specified behaviour deta hai? |
| **System Validation Testing (SVT)** | Primarily test team | Complete system ka high-level behaviour aur non-functional quality |
| **Customer Acceptance Testing** | Test team + customer; field personnel bhi execute kar sakte hain | Final product customer ki actual need meet karta hai? |

### 🧠 MENTOR EXPLAINS

Ek application ko layers mein socho:

- Developer apna function/method test karta hai — unit.
- Multiple modules ek saath kaam karte hain ya nahi — integration.
- Complete application functional aur non-functional requirements meet karti hai ya nahi — system validation.
- Customer real business situation mein product accept karta hai ya nahi — acceptance.

Instructor ke model mein DVT aur SVT ke liye formal test documentation kaafi useful hoti hai. Unit testing ka plan practical projects mein developer ke mind/workflow mein ho sakta hai; zaroori nahi har baar separate formal document ho.

## 1.2 Test Plan product hai ya tool?

### 🎓 COURSE SOURCE

Instructor batate hain ki kuch experts Test Plan ko **product/document** ke roop mein dekhte hain, kuch ise **tool** ke roop mein. Is lecture mein focus Test Plan as a **tool** hai.

Test plan ka use:
- Kaun kya karega aur kab karega, clearly define karna.
- Possible tests list karna.
- Development team ko koi test artifact/tool create karna ho toh woh mention karna.
- Testable requirements ko identify karna.
- Schedule, resources aur project expectations align karna.
- Management ko testing effort ka benchmark dena.

### 🧠 MENTOR EXPLAINS — test plan sirf paperwork nahi

Maan lo manager poochta hai: “Testing kab complete hogi?”

Agar tumhare paas plan nahi:
- Kitne tests hain, clear nahi.
- Kitne testers available hain, clear nahi.
- Environment kab milega, clear nahi.
- Dependencies kya hain, clear nahi.
- Testing complete declare karne ka criteria kya hai, clear nahi.

Agar plan hai, tum facts ke saath bata sakte ho:
- 250 planned test cases.
- 3 testers, each 50% allocation.
- Test environment 10 November ko available.
- 20 critical test cases blocked.
- Exit criteria abhi meet nahi hua.

**Plan ka benefit:** Conversation assumptions ke bajaye data par based ho jaati hai.

## 1.3 Test Plan ke four important components — QAI reference

Instructor Quality Assurance Institute (QAI) ke reference se four highlighted components batate hain:

### 1. Scope

Project/domain ki boundaries samjho:
- Kya test hoga?
- Kya test nahi hoga?
- Product ke kaunse modules/features in scope hain?
- Kaunse systems/dependencies relevant hain?

**Example:** Retail application mein checkout, payment aur order history scope mein hain; third-party courier provider ka internal algorithm tumhare scope mein nahi, lekin uske saath integration in scope ho sakta hai.

### 2. Schedule

Instructor suggest karte hain:
- Original/planned schedule include karo.
- Current/actual schedule bhi track karo.
- Example: “Final build ke 10 weeks baad testing complete hogi.”

Schedule ke bina delay ya progress ko objectively measure karna mushkil hai.

### 3. Resources

Resources sirf testers nahi hote:
- People.
- Materials/consumables.
- Equipment.
- Servers/environments.
- Time/effort.
- Testing tools.
- Domain expert.
- Technical expert.
- Testing expert.

**Mentor example:** Payment testing ke liye payment sandbox credentials, test cards, API environment, database access aur payment-domain knowledge chahiye ho sakta hai.

### 4. Entry and Exit Criteria

**Entry criteria:** Testing start karne se pehle kya conditions satisfy honi chahiye?

Example:
- Build deploy ho.
- Environment stable ho.
- Critical dependencies available hon.
- Smoke test pass ho.
- Required test data ready ho.

**Exit criteria:** Testing complete/phase exit declare karne ke liye kya conditions meet honi chahiye?

Example:
- Planned critical tests execute ho chuke.
- No open blocker/critical defects.
- Agreed pass rate achieved.
- Known residual risks documented.

Instructor ka example: “Hum testing tab tak start nahi karenge jab tak…” ya “Agar 5 defects milte hain toh testing stop karke build development ko wapas bhejenge.” Exact criteria project process se aane chahiye; numbers universal rule nahi hain.

> 🔴 **IMPORTANT:** Entry/exit criteria test team ki personal convenience nahi. Ye project process aur stakeholders ke saath agreed conditions honi chahiye.

## 1.4 Requirements Matrix / Traceability Matrix

### 🎓 COURSE SOURCE

Instructor kehte hain requirements matrix bahut important hai. Isse:
1. Aisi requirements milti hain jinhe koi test case cover nahi kar raha.
2. Aise test cases milte hain jo kisi documented requirement se linked nahi hain.
3. Requirement change hone par identify kar sakte hain kaunse tests rerun karne hain.
4. Confirm kar sakte hain ki testable requirements covered hain.

Instructor example dete hain: product requirement ke hisaab se ek system mein four color modules tak support hona chahiye, lekin team ne four-module configuration kabhi test hi nahi ki. Ye requirement coverage gap hai.

Ek aur subtle point: engineer kabhi aisi functionality test kar sakta hai jo requirement mein explicitly likhi hi nahi. Ye test useless zaroori nahi; ho sakta hai requirement hi incomplete ho. Is issue ko managers/designers ke saamne clarify karna chahiye.

### 🧠 MENTOR EXPLAINS

Traceability ka simple flow:

```text
Requirement
    ↓
Test Scenario
    ↓
Test Case
    ↓
Execution Result
    ↓
Defect (if failed)
```

Example:
- REQ-101: User valid credentials se login kar sake.
- TS-LOGIN-01: Valid login.
- TC-LOGIN-001: Correct email/password enter karke login.
- Result: Pass/Fail.
- Defect: Agar login fail hua toh defect reference.

### 💼 SDET CONNECTION

Automation framework mein `@pytest.mark` ya test metadata se requirement ID link kar sakte ho. Test Management System (TMS) mein test case requirement ke saath linked ho sakta hai. CI report se requirement coverage/status nikal sakte hain.

**Traceability matrix ka purpose sirf audit nahi:** Requirement change hui toh impact analysis karke relevant tests rerun karna.

## 1.5 Stakeholder feedback aur plan ko review karwana

Instructor recommend karte hain ki plan ke choices review karwao:
- Kya kuch miss hua?
- Kya test data sufficient hai?
- Schedule realistic hai?
- Resources available hain?

Agar later schedule slip hota hai, stakeholders ne pehle hi plan dekha hota hai. Isse testing ke end par surprise kam hota hai.

### 🎓 COURSE STORY — 10,000 tests, 3 people, half-time

Instructor ek planning reality check dete hain:
- 10,000 tests.
- 2 weeks.
- 3 people.
- Har person half-time available.

Aise mein “testing complete kar denge” bolna enough nahi. Plan numbers ke saath show karta hai ki available capacity realistic hai ya nahi.

### Project risks jo instructor highlight karte hain

- **Rapid change:** too many builds ya frequent requirement changes.
- **Incomplete requirements:** milestone tick karne ke liye TBD requirements accept kar lena.
- **Scope creep:** planned scope ke beech new features/requirements add hona.
- **Resource preemption:** testers/resources ko doosre projects mein shift kar dena.
- **Release pressure:** QA ko release delay karne ka blame milna; aur agar jaldi stop kare toh field defects ka blame bhi QA par.

Instructor strongly kehte hain: **TBD (To Be Determined) requirement ko casually accept mat karo.** Incomplete requirement se expected behaviour aur testing unclear ho jaati hai.

## 1.6 Test Plan living document hai

Requirements, schedule, scope aur builds change ho sakte hain. Isliye plan update hona chahiye. Instructor kehte hain plan mein **what cannot be tested** bhi include karo. Baad mein test report mein **what was not tested** clearly batana hai.

### ⭐ INTERVIEW — What is a Test Plan?

**Simple English:**  
“A test plan is a document or working tool that defines the scope, schedule, resources, responsibilities, entry and exit criteria, test approach and traceability for a testing effort.”

**Strong professional answer:**  
“A test plan provides a controlled baseline for the testing effort. It defines what is in and out of scope, which requirements will be verified, who will perform the work, what resources and environments are needed, how testing is scheduled, and what entry and exit criteria will be used. It also establishes traceability so we can identify uncovered requirements and assess the impact of changes. A test plan is a living document and should be updated as project conditions change.”

**Keywords:** scope, schedule, resources, entry criteria, exit criteria, traceability, risks, living document.

---

# 2. 🎓 LECTURE 2 — Test Planning Process & Testing Stages

## 2.1 Four categories of testing — instructor ka detailed breakdown

### A. Unit Testing

- Primarily developers perform karte hain.
- White-box testing at its core.
- Risk-based approach.
- Code ko directly challenge karte hain.
- Loop boundaries/off-by-one errors.
- Array bounds.
- Error-prone constructs.
- Unit-level functionality correct hai ya nahi.

**Important nuance:** Unit test pass hone ka matlab complete module/system behaviour verified hai, aisa nahi. Unit apne local level par correct ho sakta hai, lekin modules ka interaction phir bhi fail ho sakta hai.

### B. Design Verification Testing (DVT)

DVT ke andar lecture do areas explain karta hai:

**1. Integration Testing**
- Primarily developers.
- Properly unit-tested modules ek saath design ke according kaam karte hain ya nahi.
- Higher-level behaviour achieve hota hai ya nahi.

**2. Functional Testing**
- Test group perform kar sakta hai; developers bhi involved ho sakte hain.
- Final design implement hote waqt test cases develop/debug kiye ja sakte hain.
- Lecture ke model mein ye testing ka largest segment hai.

### C. System Validation Testing (SVT)

- Primarily test team.
- Full system complete ya nearly complete hone par.
- Expected high-level behaviour test.
- Non-functional quality bhi test.

Instructor examples:
- Usability.
- Security.
- Performance.
- Portability.
- Scalability.
- Other quality attributes — “the ilities”.

### D. Customer Acceptance Testing

- Test group customer input ke saath plan/write kar sakta hai.
- Often field personnel execute karte hain.
- Live data, real situations aur operational environment ka use ho sakta hai.
- Beta testing bhi include ho sakti hai.

### 🧠 MENTOR EXPLAINS — ek food delivery app par

| Stage | Example |
|---|---|
| Unit | `calculate_delivery_fee()` correct fee calculate karta hai? |
| Integration | Order service payment service ko correct amount bhejti hai? |
| Functional/DVT | Coupon apply, checkout aur order confirmation requirements ke according hain? |
| SVT | Full system performance, security, usability, scalability |
| Acceptance | Restaurant/customer operations mein actual workflow acceptable hai? |

## 2.2 Test plan documentation kis stages ke liye?

Instructor kehte hain:
- Unit test plan developer ka working plan ho sakta hai; always formal document zaroori nahi.
- DVT aur SVT ke liye formal test plan/documentation useful hai.
- Kabhi DVT aur SVT ke separate plans hote hain; kabhi comprehensive system test plan.

### ⭐ INTERVIEW — DVT vs SVT

**DVT:** “Design Verification Testing checks whether integrated modules and functional behaviour conform to the design and requirements.”

**SVT:** “System Validation Testing evaluates the completed or nearly completed system at a higher level, including functional behaviour and non-functional quality attributes such as performance, usability, security and scalability.”

> ⚠️ **Course framing note:** Different companies testing-stage names/ownership ko differently organize kar sakti hain. Interview mein concept explain karo aur clarify karo ki tumhare project mein terminology kya thi.

---

# 3. 🎓 LECTURE 3 — Test Reports / Test Status Reports

## 3.1 Test Status Report vs Final Test Report

| Report | Kab send hota hai? | Purpose |
|---|---|---|
| **Test Status Report** | Testing ke beech mein, periodically | Current progress, schedule, risk aur open issues |
| **Final Test Report** | Testing complete/phase close hone par | Final testing status aur outcome |

Status reporting cadence process par depend karti hai:
- Waterfall/phase-gate: phase ke milestones par.
- Agile/Scrum: sprint cadence ya agreed reporting cycle.

## 3.2 Report mein kya hona chahiye?

Instructor ke according managers ko clear picture chahiye:

1. **What was tested** — kaunse areas/test cases execute hue.
2. **What was not tested** — kaunse tests pending/blocked/skip hue.
3. **Planned vs actual schedule** — testing expected timeline ke comparison mein kahan hai.
4. **Open defects** — abhi kya problems unresolved hain.
5. **Risk/launch impact** — open issues ki wajah se kaunse features release se blocked ho sakte hain.
6. **Action items** — development/team ko kya karna hai.

Test report mein information testing effort se related honi chahiye. Postmortem/lessons-learned ke liye planned aur actual schedule dono useful ho sakte hain.

## 3.3 🎓 COURSE STORY — Testing black box nahi honi chahiye

Instructor ka strong point:

> Testing independent ho sakti hai, lekin development se isolated nahi honi chahiye.

Testing ek black box nahi hai jahan time spend hota rahe aur kisi ko pata na chale:
- Kya progress hai?
- Kya risk hai?
- Kya launch blocked hai?
- Kya defects open hain?

Manager ka main kaam risk manage karna hai; risk manage karne ke liye data chahiye. Marketing/customer expectations manage karne ke liye bhi testing status pata hona chahiye.

### 🧠 MENTOR EXPLAINS — sample status report

| Metric | Example |
|---|---:|
| Planned test cases | 200 |
| Executed | 150 |
| Passed | 125 |
| Failed | 15 |
| Blocked | 10 |
| Not run | 50 |
| Open critical defects | 1 |
| Open high defects | 3 |

Is example se stakeholders ko immediately samajh aata hai ki testing complete nahi hui aur critical defect open hai.

> 🟠 **Caution:** Numbers sirf illustrative hain. Real report mein pass/fail/blocked/not-run definitions consistent honi chahiye. “Not run” aur “blocked” ko ek category mein mix mat karo.

### ⭐ INTERVIEW — What is a Test Status Report?

“A test status report is a periodic update during testing. It communicates execution progress, planned-versus-actual schedule, tested and untested areas, open defects and risks. It helps stakeholders make informed release and resource decisions.”

**Keywords:** progress, schedule variance, executed, pending, blocked, open defects, risk, stakeholder communication.

---

# 4. 🎓 LECTURE 4 — Risk-Based Testing

## 4.1 Risk-Based Testing ka purpose

Instructor explain karte hain ki software failure ke risks ko identify, measure, report aur mitigate karke testing priorities decide kar sakte hain.

**Core idea:** Har feature ko equal testing effort dena practical nahi. Jahan failure ka impact high aur failure likelihood high ho, wahan testing effort zyada focus karo.

## 4.2 Risk equation

Lecture risk ko generally financial impact × probability ke form mein explain karta hai. Ye expected-value style estimate deta hai.

\[
Risk \approx Impact \times Probability
\]

Agar impact monetary terms mein estimate ho aur probability 0–1 range mein ho, expected loss estimate kiya ja sakta hai.

**Example:**
- Failure impact = ₹10,00,000.
- Probability = 0.10.
- Estimated risk = ₹1,00,000.

> ⚠️ **SOURCE GAP:** Transcript mein instructor slide par definitions pause karke padhne ko kehte hain, lekin actual slide definitions captions mein available nahi hain. Isliye upar equation ko lecture ke spoken explanation ke basis par explain kiya hai; exact slide wording claim nahi kar raha.

## 4.3 Impact — failure ho gaya toh kitna damage?

Instructor impact examples:
- Incorrect results produced.
- Security compromised.
- Data corrupted.
- Processing cannot continue.

Impact categories ko checklist ke roop mein consider karna chahiye:

- **Financial:** direct monetary loss.
- **Material:** physical materials/product damage, e.g. smart-chip card ruin hona.
- **Personnel:** employee dissatisfaction, demotivation ya loss.
- **Human life/safety:** NASA/aviation jaise critical environments mein safety impact.

## 4.4 🎓 COURSE STORY — Credit card logo vs wrong account number

Instructor apne employer ka example dete hain:

- Credit card par wrong company logo print hona: **medium impact**, banks unhappy.
- Credit card par wrong account number print hona: **very high impact**, bank ke customers unhappy, jisse bank bhi unhappy.

Instructor ke example mein dono ki likelihood low thi, lekin impact different tha.

### 🧠 MENTOR EXPLAINS

Dono errors visible printing defects hain, lekin consequences same nahi:
- Logo error brand/presentation issue ho sakta hai.
- Wrong account number customer/account association ko damage kar sakta hai.

**Tester ka lesson:** Sirf defect kitna visible hai, usse severity/risk decide mat karo. Business consequence samjho.

## 4.5 Likelihood — failure hone ke chances kitne?

Instructor factors list karte hain jo failure likelihood badha sakte hain:

1. **Module size:** Very large modules mein risk generally higher.
2. **New technology:** Team unfamiliar technology use kare toh risk higher.
3. **Lack of skill/experience:** New language, peripheral, tool ya technology experience kam ho.
4. **Complexity:** Complex features/modules error-prone ho sakte hain.
5. **New modules:** Newly built areas mein uncertainty zyada.
6. **Developer handover:** Ek developer se doosre developer ko module transfer hone par risk badh sakta hai.
7. **Lack of unit testing:** Unit tests na hona risk increase karta hai.

### 💼 SDET CONNECTION

Automation project mein likelihood factors:
- New payment gateway integration.
- Complex authentication flow.
- Frequently changed checkout module.
- Poorly documented legacy API.
- Flaky environment.
- Recently changed test data setup.
- Code ownership/team handover.

## 4.6 Risk ko control/mitigate kaise karein?

Instructor three broad approaches explain karte hain:

### A. Risk Avoidance

Risky feature/requirement ko avoid kar do:
- Feature advertise hi na karo.
- Enhancement skip kar do.
- Risky functionality release mein include na karo.

Ye risk avoid karne ka direct route hai, lekin business ke liye always possible nahi.

### B. Risk Transfer

Risk/responsibility kisi doosre party ko transfer karna.

### 🎓 COURSE STORY — Outsourcing and indemnity

Instructor financial institution ka example dete hain jahan particularly risky subsystem ka development outsource kiya gaya. Company chahti thi ki failure ki responsibility contractual terms ke through vendor par transfer ho sake; vendor ke against legal/financial remedy available ho.

**Important:** Risk transfer ka matlab risk magically disappear nahi hota. Responsibility/financial exposure shift hota hai; product failure ka user impact phir bhi ho sakta hai.

### C. Risk Management / Mitigation

Jab organization risk accept karti hai, toh impact ya likelihood reduce karne ke actions leti hai.

Instructor examples:
- Loss prevention.
- Crisis management.
- Training.
- Requirements peer review.
- Code peer review.
- Test peer review.
- Development process.
- Test process.

### 🧠 MENTOR EXPLAINS — example

Risk: Payment amount duplicate charge ho sakta hai.

Mitigation:
- Idempotency handling review.
- Retry scenarios test.
- API integration test.
- Payment logs/monitoring.
- Rollback/refund process.
- Production alerting.

Ye practical examples mentor extension hain; lecture ke core mitigation idea ko SDET context mein apply karte hain.

## 4.7 Release decision — “Testing abhi stop karke release kar dein toh risk kya hai?”

Instructor kehte hain test report mein **tests not run** mention karna important hai. Management ko pata hona chahiye ki release decision kis evidence aur kis remaining uncertainty par based hai.

Project-level risks:
- Test resources doosre projects mein shift ho jana.
- Scope creep.
- Requirement changes.
- Incomplete requirements.
- Frequent builds.

Instructor ka advice:
- Testing jaldi start karo.
- Available time mein zyada tests execute ho paayenge.
- Har development deliverable test karo.
- Time kam ho toh risk ke basis par defects/features prioritize karo.

### ⭐ INTERVIEW — Risk-Based Testing

“Risk-based testing prioritizes testing based on the likelihood of failure and the impact if that failure occurs. We identify high-risk areas, allocate more testing effort to them, and use mitigation actions such as reviews, additional testing, training and process controls. It also helps stakeholders understand the risk of releasing with tests not executed or defects still open.”

**Keywords:** impact, likelihood, probability, risk exposure, prioritization, mitigation, avoidance, transfer, release risk.

---

# 5. 🎓 LECTURE 5 — Software Defect Reports: Overview

## 5.1 Defect reporting testing ka major part hai

Instructor ek practical observation share karte hain:

> Testing effort ka roughly half actual testing mein aur half reporting, test changes, other people's work verify karne aur related activities mein spend ho sakta hai.

Ye lecture ka experience-based estimate hai, universal industry metric nahi.

Defect reporting:
- Important hai.
- Auditable process ka part hai.
- Sirf QA role ke liye nahi; software development roles ke liye bhi relevant hai.

## 5.2 Defect report ka purpose

Ideal goal:
1. Defect discover.
2. Properly report.
3. Development team fix kare.
4. Tester retest kare.
5. Confirm fix.
6. Close report.

Lekin instructor ek reality batate hain: **har reported defect fix nahi hota.** Kuch defects:
- Defer hote hain.
- Product ke liye issue nahi maane jaate.
- Not reproducible hote hain.
- Fix karne se aur problems ho sakti hain.
- Release ke baad ke liye postpone hote hain.

Phir bhi unka record rehna chahiye; decision process ka part hai.

## 5.3 Naming — Defect Report / Software Change Request / Incident Report

Different organizations alag terminology use kar sakti hain:
- Software Defect Report.
- Bug Report.
- Trouble Report.
- Incident Report.
- Software Change Request (SCR).

Instructor kehte hain enterprise change management mein Software Change Request generic term ke roop mein use ho sakta hai, jo software changes ko formally record karta hai.

## 5.4 Five-stage defect lifecycle

```text
ANALYZE
   ↓
REPORT
   ↓
TRACK
   ↓
RETEST
   ↓
CLOSE
```

| Stage | Main activity |
|---|---|
| Analyze | Confirm issue, root cause direction, reproducibility |
| Report | Defect tracking system mein clear report create |
| Track | Owner/status/fix progress monitor |
| Retest | Fixed build par same issue verify |
| Close | Fix acceptable ho toh defect close |

### 🔴 IMPORTANT

Defect lifecycle ka objective sirf bug enter karna nahi. Objective hai defect ko controlled process ke through resolution tak le jana.

---

# 6. 🎓 LECTURE 6 — Defect Lifecycle Stage 1: Analysis

## 6.1 Defect mila — ab pehle analysis karo

Defect aa sakta hai:
- Manual test execution se.
- Automated test logs se.
- Developer report se.
- User/customer report se.

Instructor kehte hain pehla question: **Fault kiski taraf hai — test, tester ya product?**

### A. Test fault

- Test case inaccurate tha.
- Expected result wrong tha.
- Test setup incorrect tha.
- Test environment assumption wrong thi.

### B. Tester fault

- Test properly execute nahi kiya.
- Steps galat follow kiye.
- System/environment ke baare mein incorrect assumption bana li.
- Result ko misinterpret kiya.

### C. Product fault

- Implementation written requirement ke against wrong — verification failure.
- Requirement/product definition hi wrong — validation failure.

### 🧠 MENTOR EXPLAINS

Har failed automation test product bug nahi hota.

Example:
- Locator wrong hai → test issue.
- Test data expired hai → setup/test data issue.
- Test ne wrong expected value assert ki → test issue.
- API response actual contract se differ karta hai → possible product defect.
- Requirement itself contradictory hai → requirement/validation issue.

## 6.2 Reproducibility vs Repeatability — very important distinction

Instructor is difference par emphasis karte hain.

### Reproducible

Issue ko **on demand** same steps/conditions ke through dobara trigger kar paana.

### Repeatable

Issue baar-baar hota hai, lekin tester use apni marzi se exactly us waqt trigger nahi kar paata.

### 🎓 COURSE STORY — Memory leak

Memory leak ka example: application kuch time baad fail ho sakti hai. Tester issue ko instantly trigger nahi kar paata, lekin sufficient time/run ke baad problem repeat hoti rehti hai.

Logs aur log analysis repeating defect ko reproducible banane mein help kar sakte hain.

| Reproducible | Repeatable |
|---|---|
| On demand trigger ho sakta hai | Repeatedly hota hai, timing/conditions uncertain ho sakti hain |
| Steps/conditions identify kiye ja sakte hain | Exact trigger difficult ho sakta hai |
| Debugging easier | Logs, environment data aur isolation useful |

> ⚠️ Terminology note: Industry teams kabhi reproducible/repeatable ko loosely interchange bhi karte hain. Is course mein instructor ka distinction yaad rakho: reproducible = on demand; repeatable = happens again but not necessarily on demand.

## 6.3 Isolation — root cause narrow karna

Instructor kehte hain issue kis wajah se hua aur kis wajah se nahi hua, ye isolate karna developer ke liye helpful hota hai.

Tester questions:
- Kya same issue doosre path se bhi trigger hota hai?
- Kya same input par different environment mein hota hai?
- Kya issue specific user/data/state se related hai?
- Kya test case khud issue create kar raha hai?
- Developer mujhse kaunse questions pooch sakta hai?

Agar alternate route se bhi same issue milta hai, product defect ka evidence stronger ho sakta hai.

### 💼 SDET CONNECTION

Automated test fail:
1. CI logs dekho.
2. Screenshot/video/trace dekho.
3. Request/response inspect karo.
4. Test data confirm karo.
5. Same steps manually ya local run mein reproduce karo.
6. Environment/browser/build compare karo.
7. Minimal reproduction steps identify karo.

## 6.4 Project stage matters

Instructor kehte hain early project phase mein test cases khud debug karne pad sakte hain; har failure immediately product defect nahi hoga. Development defects aur final system validation phase ke defects ko handle karne ka process different ho sakta hai.

**Golden principle:** Defect report karne se pehle enough analysis karo. Har failure blindly developer ke paas mat bhejo.

### ⭐ INTERVIEW — How do you analyse a defect before logging it?

“First, I verify that the test case, test data and environment are correct. Then I reproduce the issue, compare actual and expected behaviour, collect logs and evidence, and try to isolate the conditions that trigger it. I also check whether it is a product defect, a test issue or an execution mistake before creating the report.”

---

# 7. 🎓 LECTURE 7 — Defect Lifecycle Stage 2: Reporting the Defect

## 7.1 Report create karne se pehle duplicate check

Instructor suggest karte hain:
- Defect tracking system mein keyword search karo.
- Existing similar report check karo.
- Zaroorat par developer se discuss karo.
- Duplicate reports avoid karo.

Developer se discussion useful hai:
- Test correct tha?
- Requirement understanding same hai?
- Expected behaviour agreed hai?

Lekin instructor caution karte hain: developer se discuss karo, par developer tumhe defect log karne se discourage kar de toh blindly report mat drop karo. Apni analysis ke basis par decision lo.

## 7.2 Formal defect report kahan enter karna hai?

- Defect tracking system ho toh wahan.
- Process additional steps require karta ho toh follow karo.
- Report searchable aur traceable honi chahiye.
- Sirf verbal communication par depend mat karo.

Instructor source/configuration-control ka example dete hain: ek organization mein tests change karne ke liye bhi SCR (Software Change Request), approval aur review required tha. Automated test code bhi controlled artefact ho sakta hai.

## 7.3 Good defect report ki characteristics

1. **Numbered:** Unique ID/number for tracking.
2. **Simple:** One issue per report.
3. **Written:** Verbal memory par depend nahi.
4. **Concise but complete:** Reproduce karne ke liye necessary detail.
5. **Legible:** Clear language, reasonable grammar/spelling.
6. **Traceable:** Related defects/tests/requirements reference ho sakte hain.

### One issue per report

Agar two unrelated defects hain, separate reports. Agar related hain, separate IDs create karo aur cross-reference/link karo.

Exception lecture ka example: help file mein multiple spelling mistakes ek related group ke roop mein report ho sakti hain.

## 7.4 Reproduction steps concise rakho

Long, confusing reproduction steps developers ko discourage kar sakte hain. Lekin itna short bhi mat karo ki issue reproduce hi na ho.

**Good rule:** Minimum steps that reliably reproduce the issue — no missing precondition.

### ⭐ INTERVIEW — What makes a good bug report?

“A good defect report is unique, searchable, concise but complete, and focused on one issue. It includes clear reproduction steps, expected and actual results, environment/build details and supporting evidence. Before logging it, I check for duplicates and validate that the test and setup are correct.”

---

# 8. 🎓 LECTURE 8 — Defect Report ke Components

Instructor report ko multiple sections/fields mein divide karte hain. Har company ka tool/field names different ho sakta hai; lecture ke categories conceptual hain.

## 8.1 Identifying Information

| Field | Purpose |
|---|---|
| Defect ID | Unique tracking number; tool often auto-generates |
| Submitter | Kisne defect report kiya |
| Submit Date | Defect kab submit hua; age/aging analysis |
| Project/SUT | Kis project/software mein defect hai |
| Version/Revision/Build Found | Kis build mein issue mila |
| Version/Revision/Build Fixed | Kis build mein fix hua |

Build information important hai, especially large systems mein multiple intermediate builds hote hain. Fix ke beech kisi intermediate build change se new issue aa sakta hai.

## 8.2 Title

Instructor suggest karte hain title ki shuruaat module/feature abbreviation se ho.

Example:
`ACM: No error messages when 'Print on Error' is on`

ACM = Advanced Color Module.

Title:
- Short.
- Searchable.
- Feature/module identifiable.
- Problem ka essence convey kare.

## 8.3 Description — defect report ka bread and butter

Description mein:
- Kya action kiya?
- Kya actual result mila?
- Kya expected result tha?
- Kya wrong tha?
- Kaunsa test case execute hua?
- Koi additional observation?
- Attachments list.

Instructor ek weak report ka example batate hain: “I did X and got error message XXX.” Problem ye hai ki developer ko pata hi nahi expected error kya tha, ya error aana hi nahi chahiye tha.

**Expected result explicitly likho.**

### Example — mentor-created format

**Title:** `Checkout: Total amount is incorrect after applying percentage coupon`

**Precondition:** User logged in; cart subtotal ₹1,000; coupon SAVE10 active.

**Steps:**
1. Open cart.
2. Apply SAVE10.
3. Proceed to order summary.

**Expected:** Discount ₹100 apply ho aur payable amount ₹900 (tax/shipping rules ke according additional amounts included/excluded as specified).

**Actual:** Discount ₹10 show hota hai.

**Evidence:** Screenshot + network response + test case ID.

> 🔴 **IMPORTANT:** Expected result requirement se aana chahiye. Agar tax/shipping behaviour unclear hai toh report mein assumption ko fact mat banao.

## 8.4 Report Status vs Resolution Status

Instructor dono ko separately explain karte hain; kuch tracking tools inhe combine kar sakte hain.

### Report Status

Generally:
- **Open**
- **Closed**

Ye report overall active hai ya closed, ye batata hai.

### Severity vs Priority — very important interview topic

**Severity:** Defect ka impact/seriousness kitna hai?

**Priority:** Defect ko kitni jaldi fix karna chahiye?

Instructor ke process mein:
- Initial severity generally tester assign karta hai (default medium ho sakta hai).
- Defect Review Board severity adjust kar sakta hai.
- Priority product/development manager assign karta hai.

### 🎓 COURSE STORY — Logo typo vs system crash

- Company name splash screen/webpage par misspelled: **High priority, low severity** ho sakta hai — brand/public visibility ke karan jaldi fix karna chahiye, lekin system functionality break nahi.
- System crash: generally **high severity + high priority**.

Marketing/release context priority change kar sakta hai. Koi severe issue rare feature mein ho aur first customers us feature ko use hi na karenge, toh manager priority low rakh sakta hai — lekin risk record rehna chahiye.

### Instructor severity categories

| Severity | Instructor framing | Example |
|---|---|---|
| High | Show-stopper; “close up shop and go home” | System crash / cannot restart |
| Medium | Most defects; nuisance se zyada, workaround possible | Some functionality problem but avoidable |
| Low | Nuisance/minor | Extra prompt, rare inconvenience |
| Trivial (mentioned) | Very small impact | Documentation spelling/help-file issue |

Some organizations Critical/Showstopper ko High se upar define kar sakti hain.

### Severity/Priority matrix — mentor explanation

| | Low Priority | High Priority |
|---|---|---|
| Low Severity | Minor cosmetic issue, later fix | Public-facing logo/company-name typo |
| High Severity | Rare feature with release-specific low urgency (decision documented) | System crash/data loss/security breach |

> 🔴 **Remember:** Severity = impact. Priority = urgency/order of fixing. Dono related hain, same nahi.

## 8.5 Resolution Status — lecture ke statuses

Instructor kehte hain status subjective ho sakta hai; company names differ kar sakte hain. Har stage par kisi owner ki responsibility honi chahiye ki status update kare.

| Resolution status | Meaning in lecture |
|---|---|
| **None** | Report open hai; kisi ne review nahi kiya |
| **In Process** | Investigation/fix chal raha hai |
| **Fixed** | Code issue locate/update hua aur fix build process mein check-in hua; pre-build |
| **Ready for Test** | New build available; test ke liye ready; post-build |
| **Retest** | Tester ko dobara execute karna hai |
| **Not Repeatable** | Issue reproduce nahi ho raha; developer ko code mein suspicious issue nahi mila |
| **Not a Problem** | Report withdrawn/assumption mistake/environment issue/product ke liye valid defect nahi |
| **Do Not Fix** | Fix se existing customers/other behaviour ko zyada harm ho sakta hai |
| **Deferred** | Later feature/release ke liye postpone; next review date define honi chahiye |

### Deferred defects

Instructor caution:
- Deferred defects ko kab review karna hai, process mein define karo.
- Tracking system due date/reminder support kar sakta hai.
- Release ke paas open defects ko review karke decide karo: fix now ya defer.

### Regulated environment note

Regulated environment mein application code changes aur test code changes independently verify karne pad sakte hain. Sirf “developer ne change kiya” verify karna enough nahi; change correct hai aur required behaviour fully corrected hai, ye establish karna harder hota hai.

## 8.6 Miscellaneous fields

| Field | Why useful |
|---|---|
| Steps to Reproduce | On-demand reproduce karne ke liye |
| Environment | Product version, OS, platform, peripherals, relevant setup |
| Closed Release / Closed Date | Kis release/date mein close hua |
| Owner | Status/follow-up ki responsibility; change ho sakta hai |
| Discovered By | DVT, SVT, service, manufacturing, customer etc. |
| Defect Type / Root Cause | Software, hardware, mechanical, design, requirement, test case etc. |
| Software Component | Component/module classification |
| Fix Hours / Test Hours | Effort metrics and future estimation |
| Workaround | Issue avoid karne ka temporary way |

### Reproducible vs Repeatable — report field mein bhi important

Agar defect on-demand reproduce nahi hota, toh jo conditions mein dekha tha unhe best possible detail mein record karo. Repeat hone wala intermittent defect logs/environment evidence se diagnose ho sakta hai.

## 8.7 Supporting Information / Attachments

Instructor suggest karte hain:
- Error message screenshots.
- Execution logs.
- Trace files.
- Relevant debug information.
- Attachment list description mein mention karo.
- Developer ko pata hona chahiye kaunse files attached hain.

Example:
`Attached: checkout_failure.png, pytest_run.log, trace.zip`

Har tester ko debug build setup karna zaroori nahi; instructor kehte hain kuch cases mein detailed debug information developer collect kar sakta hai.

## 8.8 Good defect report ka final rule

- Concise but complete.
- Standard terminology use karo.
- Unnecessary details avoid karo.
- Reproduction ke liye necessary detail omit mat karo.
- Template/process follow karo.
- Organization ki need ke hisaab se fields tailor karo.

### ⭐ INTERVIEW — Severity vs Priority

**Simple English:**  
“Severity describes how serious the defect's impact is. Priority describes how urgently it should be fixed.”

**Strong answer:**  
“Severity is based on the technical or business impact of a defect, while priority is based on the urgency and order in which the organization wants it fixed. A typo on a highly visible company page may have low severity but high priority. A crash in a rarely used feature may be high severity but could receive a different priority depending on release context and risk. The final priority should be agreed by the responsible stakeholders.”

---

# 9. 🎓 LECTURE 9 — Defect Lifecycle: Tracking, Retest and Close

## 9.1 Tracking — Defect Review Board

Instructor recommend karte hain **Defect Review Board**.

Board mein:
- Lead tester at minimum.
- Testers (as appropriate).
- Development.
- Management.
- Business analysis.
- Database stakeholders, if relevant.

Sirf testers ka board banana instructor ka recommendation nahi. Multiple stakeholders chahiye kyunki defect ka technical impact, business impact aur release priority different perspectives se assess hota hai.

### Board ka role

- Defects triage.
- Impact/probability ke basis par risk assess.
- Severity/priority decisions.
- Owner assign.
- Fix vs defer vs other resolution.
- Review schedule set.

Har organization mein formal board nahi hota. Agar nahi hai toh testers/lead ko process-defined responsibilities handle karni padti hain. Instructor pair programming jaisi collaborative practice ka analogy testing decisions ke liye mention karte hain.

## 9.2 Board meeting cadence

Instructor example:
- DVT mein builds week mein twice scheduled: board build ke next day meet karta hai.
- SVT near release: board daily meet kar sakta hai, build ho ya na ho.

Exact cadence company/process par depend karta hai. Main point: **regular review process hona chahiye aur follow hona chahiye.**

## 9.3 Retest

Developer fix investigate karke build mein deliver karta hai. Defect status Ready for Test/Retest hota hai. Tester:
1. Correct build/version confirm kare.
2. Original reproduction steps repeat kare.
3. Expected behaviour verify kare.
4. Related regression area bhi consider kare.
5. Result/evidence update kare.

### If retest fails

- Developer ko direct communicate karo (verbal/email/team channel).
- Status In Process/try again par wapas.
- Evidence aur failure details attach/update.

### If different problem appears

Instructor kehte hain different issue ko original defect mein confuse mat karo; original issue close ho sakta hai (if fixed) aur new problem ke liye new defect lifecycle start ho.

### If retest passes

- Close release/version record.
- Tester notes.
- Close date.
- Board/company process ke according closure.
- Kuch organizations mein tester directly close nahi karta; closure recommendation board ko jaati hai.

## 9.4 Postmortem / Lessons Learned

Successful fix ke baad bhi poochho:
- Defect ka root cause kya tha?
- Ye future mein kaise prevent hoga?
- Kya requirement review miss hua?
- Kya test case missing tha?
- Kya code review/testing process improve karna hai?
- Retest sufficient tha?

## 9.5 Risk-based triage

Instructor kehte hain koi bhi defect enter kar sakta hai; testers defects ko impact aur probability ke basis par triage karte hain.

Testing status, severity, priority aur risk ka relation samjho:
- Severity defect ke impact ko describe karti hai.
- Probability batati hai failure kitna likely hai.
- Priority batati hai organization fix ko kab karna chahti hai.
- Triage decide karta hai next action/owner.

### ⭐ INTERVIEW — Explain defect lifecycle

“A defect lifecycle typically includes analysis, reporting, tracking, retesting and closure. First, I validate the failure and determine whether it is a product, test or execution issue. Then I create a clear, reproducible report. The defect is triaged and assigned an owner. After the fix is delivered in a new build, I retest the original scenario and relevant regression areas. If the issue is resolved, it is closed according to the team's process; otherwise, it is returned for further investigation.”

---

# 10. 🧩 ASSIGNMENT — GolfScore Test Plan

## 10.1 ZIP mein assignment ka actual task

Assignment file ke according tumhe:
1. `golfsrsrev.pdf` read/understand karna hai.
2. SRS ko finished maana hai — **lekin necessarily correct nahi**.
3. Provided Test Plan Template (`.docx` ya `.rtf`) use karna hai.
4. Test plan ke sections complete karne hain.
5. Jo include/exclude kiya hai usko justify karna hai.
6. Schedule estimates reasonable hone chahiye; assumptions explain karo.
7. Actual test cases include karne hain — appendix ya separate section.
8. Submission PDF format mein hoti hai.

Assignment example mein four sample test cases diye gaye:
- Course number `1` accepted.
- Course number `5` accepted.
- Course number `6` error return.
- Course number `0` error return.

**Important:** Ye examples course-number validation ke liye hain, full assignment solution nahi.

## 10.2 GolfScore SRS — product ko samjho

### Product purpose

GolfScore command-line program golf tournament scores process karke reports generate karta hai:
- Tournament ranking report.
- Individual golfer report.
- Course report.

No GUI. Input formatted text file se aata hai; output text report files mein jata hai.

### Platform / architecture

SRS:
- C ya C++.
- Windows 2000 ya later Windows PC.
- Stand-alone executable.
- Command-line execution.

### Command-line format

```text
golf options filename output-directory
```

Options:
- `-h` = help display; filename/output directory ignore.
- `-c` = Course Report.
- `-t` = Tournament Ranking Report.
- `-g` = Golfer Report.
- Options combine ho sakte hain, e.g. `-ct`.

Filename:
- Input file.
- Full path ho sakta hai.
- Path absent ho toh execution directory use.

Output directory:
- Output reports ka destination.
- Agar absent ho toh filename wali directory use.

### Tournament assumptions

| Rule | SRS requirement |
|---|---|
| Courses | 1 to 5 |
| Golfers | 2 to 12 |
| Holes per course | 18 |
| Par per hole | 3, 4 or 5 |
| Each golfer | Every course once play karega |
| Stroke count | 18 holes ke strokes ka sum |
| Course score | 18 holes ke earned scores ka sum |
| Tournament score | All courses ke scores ka sum |
| Ranking | Higher score is better (descending order) |

### Scoring rule — carefully understand

| Strokes relative to par | Earned score |
|---|---:|
| Over par | 0 |
| Par | 1 |
| 1 under par | 2 |
| 2 under par | 4 |
| 3 or more under par | 6 |

🔴 **Common confusion:** GolfScore ka earned score normal golf scorecard ke stroke count jaisa nahi. SRS explicitly kehta hai lower stroke count relative to par ka earned score higher hota hai. Is assignment mein SRS ka custom scoring rule follow karna hai.

## 10.3 Input file structure

Input file mein records specified order mein hain. Each record line ending se terminate hota hai.

### Course Records

- Each golf course ke liye one record.
- All course records first.
- Column 1 blank.
- Columns 2–19: course name.
- Column 20: single-character course identifier.
- Columns 21–38: 18 hole par values (each 3, 4 or 5).

### First Delimiter Record

- Course records ke end ko mark karta hai.
- Column 1 non-blank.

### Golfer Records

- Each golfer for each course one record.
- Records any order mein aa sakte hain.
- Column 1 blank.
- Column 2: course identifier.
- Columns 3–9 ignored.
- Columns 10–29: golfer name.
- Column 30 ignored.
- Columns 31–48: 18 hole stroke counts.

### Final Delimiter Record

- Golfer records/input file ka end.
- Column 1 non-blank.

## 10.4 Output reports

### Tournament Ranking Report — `trank.rep`

- All golfers.
- Golfer name.
- Each course ka score.
- Total tournament score.
- Final standing.
- Descending score order (best first).
- Tie ho toh alphabetical order.

### Golfer Report — `golfer.rep`

- Tournament Ranking Report jaisa content.
- Difference: golfers alphabetical by last name.

### Course Report — `course.rep`

- Each input course ke liye section.
- All golfers.
- Golfer name.
- Hole-by-hole stroke count.
- Total score for that course.
- Descending course score order.

## 10.5 Error handling requirements

### Input Parameter Errors

- Unrecognizable options → stop + explanatory message.
- Missing/nonexistent input file → input parameter error.
- Nonexistent output directory → input parameter error.
- First field after options filename maana jayega.
- First field after filename output directory maana jayega.
- Output directory omitted ho toh input filename ki directory use.
- Output-directory ke baad extra fields ignored; error nahi.

### Input Data Errors

1. Numeric expected but non-numeric data → stop + appropriate error message.
2. Par value 3, 4, 5 ke alawa → stop + appropriate error message.
3. Same golfer ke same course ke two or more records → first ke baad additional records ignore, message display, processing continue.

### Output Errors

- Requested output file already exists → user se overwrite confirmation.
- Separate prompt each requested report ke liye.
- `Y` → overwrite.
- `N` → generated output discard.
- Output path mein report file absent → create.
- Other write errors → behaviour unspecified.

> ⚠️ **SRS ambiguity:** “Any other output write error” ka behaviour unspecified hai. Tester ko is par expected message/exit code invent nahi karna. Requirement clarification ya test plan mein limitation document karni hai.

## 10.6 Performance requirement

Program execute hone ke baad processing **one minute ke andar complete** honi chahiye.

Ye measurable non-functional requirement hai. Test plan mein dataset size, environment aur timing method specify karna hoga. SRS transcript mein maximum dataset details beyond 5 courses/12 golfers nahi; un bounds ko performance test ke maximum functional input ke roop mein consider kar sakte hain, lekin assumptions document karo.

---

# 11. 🧠 GolfScore assignment — Test Plan kaise build karna hai?

## 11.1 Template ke sections

Provided DOCX template mein ye structure hai:

1. Introduction
   - Objective
   - Project Description
   - Process Tailoring
   - Referenced Documents
2. Assumptions / Dependencies
3. Test Requirements
4. Test Tools
5. Resource Requirements
6. Test Schedule
7. Risks / Mitigation
8. Metrics
9. Appendix A — Detailed Resource Requirements
10. Appendix B — Detailed Test Schedule

Example Test Plan PDF mein kuch additional headings hain:
- Objectives.
- Test Description.
- Schedule.
- Resources.
- Dependencies.
- Entry Criteria.
- Exit Criteria.
- Test Tools.
- Owner.
- Metrics.
- Test Plan Requirements Matrix.
- Document History.
- Definitions/Acronyms.
- Appendices with test case matrices.

### 🧠 MENTOR EXPLAINS

Template ka exact section order use karo, lekin SRS/assignment requirements ko cover karne ke liye additional sections/appendices add kar sakte ho. Assignment explicitly kehta hai actual test cases include karo.

## 11.2 Section-by-section kya likhna hai?

### 1. Introduction

**Objective:** Is plan ka purpose. Example: GolfScore Release 1.1 ke functional requirements, input handling, report generation, error handling aur performance verify karna.

**Project Description:** CLI application, input text file, three report outputs, C/C++, Windows.

**Process Tailoring:** Kaunse testing types planned:
- Specification testing.
- Functional testing.
- Boundary/limits testing.
- Error handling.
- Compatibility/platform testing.
- Performance.
- Documentation/help.
- Regression.

**Referenced Documents:** GolfScore SRS Rev 1.1, provided assignment brief, project test plan template.

### 2. Assumptions / Dependencies

Assumptions:
- SRS is baseline, but ambiguities are raised.
- Test executable/build provided by development.
- Windows test environment available.
- Valid/invalid input files create kiye ja sakte hain.
- Expected output independently calculate kiya ja sakta hai.

Dependencies:
- Executable build.
- Input/output folder permissions.
- Test data.
- Supported Windows environment.
- Developer clarification for ambiguous requirements.

### 3. Test Requirements

SRS requirements ko testable items mein break karo:
- CLI options.
- Course count boundaries.
- Golfer count boundaries.
- Par validation.
- Input record structure.
- Score calculation.
- Ranking/tie sorting.
- Output filenames.
- Overwrite prompt.
- Error messages.
- 1-minute performance.

### 4. Test Tools

Possible tools:
- Windows command prompt/PowerShell.
- Text editor.
- Spreadsheet/test case tracker.
- File comparison tool.
- Timer/performance measurement.
- Defect tracking system.
- Test data generation script (if approved/available).

Tools jo actually available nahi, unhe available claim mat karo; plan mein proposed/required mark karo.

### 5. Resource Requirements

- Test engineer(s).
- Developer contact for clarification.
- Windows machine.
- GolfScore executable.
- Test data files.
- Input/output directories.
- Time for test design, execution, defect retest and regression.

### 6. Test Schedule

Work packages:
1. SRS analysis.
2. Test plan and test case design.
3. Test data preparation.
4. Environment/build readiness.
5. Smoke/entrance test.
6. Functional testing.
7. Error handling/boundary testing.
8. Performance testing.
9. Defect retest.
10. Regression.
11. Final report.

Schedule estimate assumptions ke saath do. Assignment realistic parameters chahta hai; arbitrary dates/effort mat likho.

### 7. Risks / Mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| SRS ambiguity | Expected result unclear | Clarification log |
| Build late | Schedule delay | Early build dependency |
| Test data wrong | False failures | Independent data review |
| Limited environment | Coverage gap | Document platform limits |
| Defects late | Regression time reduced | Risk-based priority |
| Output behaviour unspecified | Cannot assert exact result | Record limitation/clarify |

### 8. Metrics

Possible metrics:
- Planned/executed/passed/failed/blocked/not-run test cases.
- Open defects by severity.
- Defects found by test phase.
- Defect retest pass rate.
- Requirements coverage.
- Schedule variance.
- Test effort actual vs planned.
- Performance execution time.

### Appendix A — Resource detail

Activity, role/person, hours, equipment/tool.

### Appendix B — Detailed Schedule

Gantt-style activity timeline; dependencies show karne ke liye PERT-style flow/diagram. Provided template specifically Gantt and PERT charts mention karta hai.

---

# 12. 📋 GolfScore — Sample Test Case Design Bank

> **Important:** Ye mentor-designed test ideas SRS requirements se derive kiye gaye hain. Jahan SRS expected behaviour define nahi karta, wahan “Clarification needed / unspecified” mark kiya hai. Inhe assignment mein apne test plan ke format ke hisaab se use/refine karo.

## 12.1 Command-line parameter tests

| ID | Test idea | Expected result |
|---|---|---|
| GS-CLI-001 | `-h` option | Help display; filename/output directory ignore |
| GS-CLI-002 | `-c` only | Course report requested |
| GS-CLI-003 | `-t` only | Tournament ranking report requested |
| GS-CLI-004 | `-g` only | Golfer report requested |
| GS-CLI-005 | `-ctg` combined | All three reports requested |
| GS-CLI-006 | Unknown option | Stop and display explanatory error |
| GS-CLI-007 | Nonexistent input file | Input parameter error |
| GS-CLI-008 | Nonexistent output directory | Input parameter error |
| GS-CLI-009 | Output directory omitted | Use directory containing input file |
| GS-CLI-010 | Extra argument after output directory | Extra field ignored |

## 12.2 Course and golfer boundary tests

| ID | Input | Expected |
|---|---|---|
| GS-DATA-001 | 1 course | Accepted |
| GS-DATA-002 | 5 courses | Accepted |
| GS-DATA-003 | 0 courses | Error/invalid input handling; exact message per implementation/SRS interpretation |
| GS-DATA-004 | 6 courses | Error/invalid input handling |
| GS-DATA-005 | 2 golfers | Accepted |
| GS-DATA-006 | 12 golfers | Accepted |
| GS-DATA-007 | 1 golfer | Outside stated valid range; error handling needs specification |
| GS-DATA-008 | 13 golfers | Outside stated valid range; error handling needs specification |

Assignment's sample explicitly states course number 1/5 accepted, 6/0 error. Golfer boundary tests are derived from SRS's 2–12 rule.

## 12.3 Par and score calculation tests

| ID | Scenario | Expected |
|---|---|---|
| GS-SCORE-001 | Par value 3 | Accepted |
| GS-SCORE-002 | Par value 4 | Accepted |
| GS-SCORE-003 | Par value 5 | Accepted |
| GS-SCORE-004 | Par value 2 | Stop with appropriate error |
| GS-SCORE-005 | Par value 6 | Stop with appropriate error |
| GS-SCORE-006 | Non-numeric par | Stop with appropriate error |
| GS-SCORE-007 | Stroke count over par | Earned score 0 |
| GS-SCORE-008 | Stroke count equal par | Earned score 1 |
| GS-SCORE-009 | One under par | Earned score 2 |
| GS-SCORE-010 | Two under par | Earned score 4 |
| GS-SCORE-011 | Three under par | Earned score 6 |
| GS-SCORE-012 | More than three under par | Earned score 6 |

## 12.4 Duplicate and input record tests

| ID | Scenario | Expected |
|---|---|---|
| GS-INPUT-001 | Duplicate golfer record for same course | First retained; later duplicates ignored; message displayed; processing continues |
| GS-INPUT-002 | Golfer records in different order | Accepted; records can appear in any order |
| GS-INPUT-003 | Missing/invalid numeric field | Stop with appropriate error |
| GS-INPUT-004 | Valid course delimiter | Course section ends |
| GS-INPUT-005 | Valid final delimiter | Input records end |
| GS-INPUT-006 | Invalid/missing delimiter | **Clarification needed:** exact error behaviour not explicitly defined |
| GS-INPUT-007 | Course identifier does not match any course | **Clarification needed:** SRS does not clearly state exact handling |
| GS-INPUT-008 | Missing golfer/course record | SRS assumption says every golfer plays every course; exact error handling should be clarified |

## 12.5 Report generation tests

| ID | Scenario | Expected |
|---|---|---|
| GS-REPORT-001 | `-t` | `trank.rep` generated |
| GS-REPORT-002 | `-g` | `golfer.rep` generated |
| GS-REPORT-003 | `-c` | `course.rep` generated |
| GS-REPORT-004 | `-ct` | Course + tournament ranking reports generated |
| GS-REPORT-005 | Tournament ranking | Descending total score |
| GS-REPORT-006 | Tie in tournament score | Alphabetical ordering |
| GS-REPORT-007 | Golfer report | Alphabetical by last name |
| GS-REPORT-008 | Course report | One section per course |
| GS-REPORT-009 | Course report sorting | Descending course score |
| GS-REPORT-010 | Course report content | Hole-by-hole stroke counts + course total |
| GS-REPORT-011 | Report filename | Exact specified filename |
| GS-REPORT-012 | Existing output + user enters Y | Overwrite file |
| GS-REPORT-013 | Existing output + user enters N | Generated output discarded |
| GS-REPORT-014 | Multiple requested reports already exist | Separate prompt for each requested report |

## 12.6 Performance test

| ID | Scenario | Expected |
|---|---|---|
| GS-PERF-001 | Valid maximum-bound dataset (5 courses, 12 golfers) | Processing completes within one minute |

**Assumption to document:** Dataset size is based on SRS maximum courses/golfers; environment and execution timing method must be specified.

---

# 13. ⚠️ GolfScore SRS — Questions/ambiguities to raise

SRS finished maana gaya hai, **but necessarily correct nahi**. Tester ko ambiguity identify karni chahiye, silently expected result invent nahi karna.

1. Course count 0/6 ke liye exact error message and exit code specified nahi.
2. Golfer count 1/13 ke exact error message/handling detailed nahi.
3. Unknown course identifier ka behaviour clearly defined nahi.
4. Missing golfer-course record ka exact handling defined nahi.
5. Delimiter malformed/missing ho toh behaviour clear nahi.
6. Non-numeric data error message “appropriate” kaha gaya hai, exact wording nahi.
7. Output write errors other than existing-file overwrite unspecified.
8. Tie-breaking for Tournament Ranking explicitly alphabetical; Golfer Report alphabetical by last name. Same last name tie handling unspecified.
9. Alphabetical sorting case sensitivity/locale handling specified nahi.
10. Performance requirement one minute hai, but hardware baseline/input dataset details limited hain.

**Professional tester behaviour:** Question log banao, owner assign karo, answer/decision record karo, phir expected result finalize karo.

---

# 14. ⭐ Module 3 — Interview Preparation

## Test Planning

**Q: What is the purpose of a test plan?**  
A: “It defines the scope, approach, schedule, resources, responsibilities, entry/exit criteria, risks and traceability for the testing effort.”

**Q: What is a requirements traceability matrix?**  
A: “It maps requirements to test scenarios/test cases and execution results. It helps identify uncovered requirements and assess the impact of requirement changes.”

**Q: What are entry and exit criteria?**  
A: “Entry criteria define the conditions that must be satisfied before a test phase starts. Exit criteria define the conditions required to complete or exit that phase.”

## Testing stages

**Q: Explain Unit, Integration, System and Acceptance Testing.**  
A: “Unit testing checks a small code unit, integration testing checks interactions between components, system testing evaluates the complete system, and acceptance testing determines whether the product meets customer needs.”

## Reporting

**Q: Test status report vs test summary report?**  
A: “A status report is periodic and communicates ongoing progress and risks. A final test report summarizes the outcome at the end of the testing phase.”

## Risk

**Q: What is risk-based testing?**  
A: “It prioritizes testing based on failure likelihood and impact, so high-risk functionality receives more attention.”

**Q: What is risk mitigation?**  
A: “Actions that reduce the probability or impact of a risk, such as reviews, training, additional testing, monitoring or contingency planning.”

## Defect reporting

**Q: Severity vs priority?**  
A: “Severity describes impact; priority describes how urgently the defect should be fixed.”

**Q: Reproducible vs repeatable?**  
A: “In this course's terminology, reproducible means the issue can be triggered on demand, while repeatable means it occurs again but may be difficult to trigger on demand.”

**Q: What is defect triage?**  
A: “It is the process of reviewing defects, assessing their impact and risk, assigning ownership and deciding their priority and next action.”

**Q: What happens after a fix?**  
A: “The tester verifies the fix on the appropriate build, reruns the original reproduction steps and relevant regression tests, records evidence and closes the defect if the issue is resolved.”

---

# 15. 🧠 Practice Scenarios — answer before looking at notes

## Scenario A — No test plan

Manager asks QA to test a release in 2 weeks. Team has 2 testers, 300 test cases, and environment delivery is uncertain.

1. Test plan ke kaunse sections immediately important hain?
2. Entry criteria kya ho sakte hain?
3. Resource/schedule risk kaise communicate karoge?
4. Agar 300 tests execute nahi ho sakte, priority kaise decide karoge?

## Scenario B — High severity, low priority

A crash occurs in a rarely used admin report that will not be enabled for the first customer release.

1. Severity kya represent karti hai?
2. Priority ka decision kaun karega?
3. Kya defect ko ignore kar sakte hain?
4. Release risk kaise document karoge?

## Scenario C — Intermittent automation failure

Playwright test 20 runs mein ek baar fail hota hai. CI logs show network timeout.

1. Kya immediately product bug log karoge?
2. Reproducibility/repeatability distinction apply karo.
3. Kya evidence collect karoge?
4. Isolation ke next steps kya hain?

## Scenario D — Defect retest fails

Developer says bug fixed. New build deployed. Same steps still produce wrong total.

1. Defect status kya update karoge?
2. Developer ko kya evidence doge?
3. Kya new defect create karna chahiye ya original reopen? Kab?

## Scenario E — Risk-based priority

Feature A: failure probability 20%, impact ₹10 lakh.  
Feature B: failure probability 5%, impact ₹1 crore.

1. Simple expected-risk estimate calculate karo.
2. Kis feature ka estimated risk higher?
3. Kya sirf number ke basis par test priority decide karoge? Why/why not?

---

# 16. ✅ Practice Answer Guide

**A:** Scope, schedule, resources, dependencies, entry/exit criteria, test requirements and risk sections. Environment/build readiness entry criteria. Capacity calculation and risk-based selection. Untested cases explicitly report karo.

**B:** Crash high severity ho sakta hai; priority product/development manager and stakeholders decide karte hain. Ignore nahi; defer decision, rationale, affected users and release risk record karo.

**C:** Immediately product bug assume nahi. Logs, trace, network timing, environment, retry behaviour, test data, browser/build capture karo. On-demand reproduction try karo; intermittent repeat pattern note karo.

**D:** Original issue still exists toh retest fail record karke In Process/try-again state; developer ko evidence. Agar different issue hai toh separate defect create; original defect fix hua ho toh close per process.

**E:** A = ₹10,00,000 × 0.20 = ₹2,00,000. B = ₹1,00,00,000 × 0.05 = ₹5,00,000. B estimated risk higher. Lekin assumptions, safety/legal impact, uncertainty, dependency and mitigation options bhi consider karne honge.

---

# 17. 📊 Module 3 — Study Priority & Completion Criteria

| Topic | Difficulty | Focused study time | Priority |
|---|---|---:|---|
| Test Plan purpose + 4 components | Medium | 40–50 min | Must know |
| Traceability Matrix | Medium | 35–45 min | Must know |
| Unit/DVT/SVT/Acceptance | Medium | 40–50 min | Must know |
| Test Status/Final Report | Medium | 35–45 min | Must know |
| Risk-Based Testing | Hard | 50–60 min | Must know |
| Risk mitigation strategies | Medium | 35–45 min | Must know |
| Defect lifecycle | Medium | 40–50 min | Must know |
| Defect analysis + reproduce/isolate | Hard | 45–60 min | Must know |
| Defect report components | Medium–Hard | 60–75 min | Must know |
| Severity vs Priority | Medium | 30–40 min | Must know |
| Tracking/Retest/Close | Medium | 40–50 min | Must know |
| GolfScore SRS + Test Plan assignment | Hard | 3–5 hours | Must do |

## Module 3 completion criteria

Module complete tab hoga jab tum:
- Test plan ko apne words mein explain kar sako.
- Scope, schedule, resources, entry/exit criteria explain kar sako.
- RTM/traceability ka purpose bata sako.
- Unit, DVT, SVT, acceptance testing distinguish kar sako.
- Status report mein kya include hota hai, bata sako.
- Risk = impact × likelihood ko example ke saath samjha sako.
- Risk avoidance, transfer aur mitigation distinguish kar sako.
- Defect lifecycle ke five stages explain kar sako.
- Reproducible vs repeatable difference samjha sako.
- Severity vs priority ke examples de sako.
- Defect report ka clear example likh sako.
- GolfScore SRS se test requirements aur test cases derive kar sako.
- SRS ambiguity ko identify karke clarification log bana sako.

> 💚 **MENTOR NOTE:** Module 3 ko sirf padhkar finish mat karna. GolfScore assignment tumhari real learning checkpoint hai. Ismein SRS padhna, scope decide karna, risk identify karna, test cases design karna aur test plan justify karna — ye sab professional QA/SDET work ke core skills hain.
