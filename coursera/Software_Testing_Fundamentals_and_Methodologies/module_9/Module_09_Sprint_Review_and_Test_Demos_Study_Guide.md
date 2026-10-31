# Module 9 — Scrum Testing: Sprint Review & Test Demonstrations

> **QA / SDET Mentor Study Guide**
>
> Ye guide sirf uploaded **Module 9 — Scrum Testing Demos** ZIP ke source material par based hai. Explanation Hinglish mein hai. Jahan additional example diya gaya hai, use **Mentor-created example** mark kiya gaya hai.

---

## 🎯 Learning outcomes

Is module ke baad aap:
- Sprint Review ka actual purpose aur QA tester ka role explain kar paoge.
- Business value ke basis par demo scenarios select kar paoge.
- Happy path, high-value negative path aur DoD evidence ko present kar paoge.
- Sprint Review se pehle environment aur test data prepare kar paoge.
- Demo ko Context → Execution → Result structure mein present kar paoge.
- Live demo fail hone par professional response de paoge.
- Test result ko acceptance criteria se connect karke stakeholders ko evidence de paoge.

---

# Part 1 — Sprint Review kya hai?

## WHY — Sirf feature bana dena enough kyun nahi?

Imagine karo development team ne two weeks mein ek feature complete kiya. Stakeholders, managers aur client ke saamne ab aapko demonstrate karna hai ki feature sirf finish nahi hua, balki agreed requirements aur quality standards ke according sahi bhi hai.

Agar demo ka structure clear nahi hai, to perfectly working feature bhi audience ko confusion mein daal sakta hai.

## WHAT — Sprint Review

Sprint Review Scrum ki core ceremony hai jo har sprint ke end par hoti hai. Ye sirf “developers apna kaam dikha dein” wali meeting nahi hai. Ye Scrum Team aur key stakeholders ke beech collaborative working session hai.

Course reading ke according Sprint Review ke 3 primary goals hain:

### 1. Inspect the Increment

- Team completed work demonstrate karti hai.
- Sirf woh stories showcase honi chahiye jo Definition of Done (DoD) meet kar chuki hain.
- Stakeholders inspect karte hain ki increment expected quality aur functionality meet karta hai ya nahi.

### 2. Gather Feedback

- Stakeholders new functionality review karte hain.
- Questions poochte hain.
- Changes ya improvements suggest karte hain.
- Feedback expected aur valuable hota hai.

### 3. Adapt the Backlog

Discussion ke basis par Product Owner:
- Product backlog reprioritize kar sakta hai.
- New user stories add kar sakta hai.
- Aisa work remove kar sakta hai jo current business needs ke saath align nahi karta.

## QA tester ka role

QA tester ka kaam sirf button click karke “working” prove karna nahi. Tester ko evidence dikhana hai ki:
- Feature agreed acceptance criteria meet karta hai.
- Team ke quality standards follow hue hain.
- Important negative behavior bhi validate hua hai.
- Stakeholders ko clear picture milti hai ki kya deliver hua.

[!IMPORTANT]
Sprint Review mein aap apna personal performance prove nahi kar rahe. Aap quality aur completed increment ka evidence present kar rahe ho.

## 🎤 Interview answer

**Simple English:**

A Sprint Review is a Scrum event held at the end of a sprint. The team inspects the completed increment, gathers stakeholder feedback, and adapts the product backlog based on that feedback.

**Stronger answer:**

The Sprint Review is a collaborative session between the Scrum Team and stakeholders. The team demonstrates completed work that meets the Definition of Done, stakeholders inspect the increment and provide feedback, and the Product Owner may update backlog priorities or add and remove items. As a QA tester, I use this opportunity to demonstrate that important acceptance criteria and quality expectations have been validated.

**Keywords:** sprint review, increment, Definition of Done, stakeholder feedback, backlog adaptation, quality evidence.

---

# Part 2 — Demo mein kaunse test scenarios showcase karein?

## WHY — Saare test cases demo kyun nahi karne chahiye?

Real project mein tester dozens ya hundreds of tests execute kar sakta hai. Sprint Review limited time mein hota hai. Har test case demonstrate karne ki zaroorat nahi.

Aapko woh scenarios choose karne hain jo:
- Business value show karein.
- Stakeholder impact ke liye important hon.
- Feature ki reliability par confidence build karein.

Course reading ke according Acceptance Criteria, especially BDD format, demo script ka best starting point hain.

## 2.1 Happy Path — Pehle success dikhao

Happy path main success scenario hai.

Stakeholder ka first question hota hai: “Kya feature woh kaam karta hai jo humne request kiya tha?”

Example from course:
- User login page par hai.
- Registered user valid credentials enter karta hai.
- Submit karta hai.
- Dashboard par redirect hota hai.

Happy path se core functionality working hone ka baseline establish hota hai.

## 2.2 High-value Negative Path — Phir important error handling

Har edge case demo karna zaroori nahi. Ek aisa negative path choose karo jo business ke liye meaningful ho.

Course example:
- User invalid email enter karta hai.
- Application clear, helpful error message show karti hai.
- Invalid data submit nahi hota.

Isse stakeholders ko confidence milta hai ki system sirf ideal input par hi nahi, invalid input par bhi expected behavior show karta hai.

## 2.3 Definition of Done ka ek quality point

Har non-functional requirement demo karna zaroori nahi. Lekin ek relevant quality point mention karna useful ho sakta hai.

Course example:
- Login feature demonstrate karne ke baad tester mention karta hai ki password transmission security standards meet karne ke liye encrypted verify ki gayi.

Isse stakeholders ko pata chalta hai ki QA ne visible functionality ke alawa security, reliability aur other quality expectations bhi consider ki hain.

## Scenario selection summary

| Demo priority | Kya show karna hai? | Purpose |
|---|---|---|
| 1 | Happy path | Main business functionality works |
| 2 | One high-value negative path | Important error handling is correct |
| 3 | One relevant DoD quality point | Broader quality standards ka evidence |

[!TIP]
Demo ka goal test suite reproduce karna nahi. Demo ka goal limited time mein important quality evidence communicate karna hai.

## 🎤 Interview answer

**Simple English:**

I select a few scenarios based on business value and stakeholder impact. I start with the happy path, then show one important negative path, and mention a relevant quality requirement from the Definition of Done.

**Stronger answer:**

I do not demonstrate every test case during a Sprint Review. I use the agreed acceptance criteria to select a small, high-value set. I start with the happy path to show the primary business behavior, then demonstrate one critical negative path to show graceful error handling. Where relevant, I also mention a non-functional quality check from the Definition of Done, such as secure password transmission. This keeps the demo focused and meaningful to stakeholders.

**Keywords:** business value, stakeholder impact, happy path, negative path, DoD, focused demo.

---

# Part 3 — Demo se pehle preparation

## WHY — Working feature bhi demo mein fail kyun ho sakta hai?

Feature correct ho sakta hai, lekin:
- Demo server down ho.
- Last-minute code change se behavior change ho gaya ho.
- Test account locked ho.
- Duplicate username already exist na karta ho.
- Tester live typing mein typo kar de.

Unexpected technical issues stakeholder confidence reduce kar sakte hain. Isliye demo preparation testing ka important part hai.

## 3.1 Prepare the Environment

Course reading recommend karti hai:
- Personal development machine ke bajay stable shared environment use karo, whenever possible.
- Staging/demo server production ke close mirror hona chahiye.
- Demo environment ko last-minute code changes se shield karna chahiye, jo demo ko break kar sakte hain.

## 3.2 Prepare the Data

Har chosen scenario ke liye exact data pehle ready rakho.

Course examples:
- Successful login ke liye username/password text file mein ready.
- Duplicate username error demonstrate karna hai to demo database mein woh username already exist hona chahiye.
- Live demo mein unnecessary typing avoid karo; copy-paste faster hai aur typo risk kam karta hai.

[!WARNING]
Credentials ko public presentation mein expose mat karo. Demo data/credentials ko approved, safe test accounts tak limited rakho. Ye mentor safety clarification hai; course reading simply demo data ready rakhne ko kehti hai.

## 3.3 Do a Dry Run

Dry run ka meaning hai actual Sprint Review se pehle complete demo ko kam se kam ek baar rehearse karna.

Verify:
- Environment online hai.
- Required test data present hai.
- Correct account available hai.
- Chosen scenarios execute ho rahe hain.
- Expected result visible hai.
- Demo flow smooth hai.

Course reading kehti hai five-minute dry run ek uncomfortable live demo se bacha sakta hai.

## Preparation checklist

- [ ] Stable staging/demo environment selected.
- [ ] Last-minute code changes ka risk controlled.
- [ ] Chosen happy path data ready.
- [ ] Chosen negative path data/state ready.
- [ ] Required test accounts accessible.
- [ ] Acceptance Criteria available.
- [ ] Complete dry run performed.
- [ ] Expected outcomes confirmed.

## 🎤 Interview answer

**Simple English:**

Before a Sprint Review, I prepare a stable staging or demo environment, create the exact test data needed for the selected scenarios, and perform a dry run to make sure everything works.

**Stronger answer:**

A successful demo depends on preparation. I prefer a stable shared staging or demo environment rather than an unstable personal development setup. I prepare the accounts and data required for the happy and negative paths, avoid unnecessary live typing, and perform a complete dry run. This helps confirm that the environment is available, the data is correct, and the demonstration can proceed without avoidable surprises.

**Keywords:** staging, stable environment, test data, dry run, demo readiness, risk reduction.

---

# Part 4 — Context, Execution, Result (CER) demo framework

## WHY — Demo ko story ki tarah present karo

Agar aap bina explain kiye screen par clicks karna start kar doge, stakeholder ko nahi pata hoga:
- Aap kya prove kar rahe ho?
- Ye steps kyun perform kar rahe ho?
- Result ka requirement se kya relation hai?

Course reading isse “Tell, Show, Tell” model bhi kehti hai: pehle batao, phir dikhao, phir result explain karo.

## 4.1 Context — Tell them what you will show

Action start karne se pehle:
- User story ka goal simple language mein explain karo.
- Specific BDD scenario/Acceptance Criteria state karo.
- Stakeholders ko batao ki kaunsa behavior demonstrate hoga.

Course example:
“This user story is about allowing users to reset their passwords. I'm going to demonstrate the happy path: Given I am on the password reset page, when I enter my registered email and click submit, then I should receive a password reset link.”

## 4.2 Execution — Show them

- Prepared data use karo.
- Described steps ko cleanly execute karo.
- Actions ko simple language mein narrate karo.
- Unnecessary technical jargon avoid karo.

Course example:
“I'm pasting in a registered email address... and now I'm clicking the Submit button.”

## 4.3 Result — Tell them what you showed

Action ke baad:
- Actual result announce karo.
- Acceptance Criteria se explicitly connect karo.
- Confirm karo ki expected outcome achieve hua ya nahi.

Course example:
“As you can see, the application confirms a reset link has been sent. This behavior successfully meets the Acceptance Criteria we just discussed.”

## CER template

| Stage | Presenter kya bole/ kare? |
|---|---|
| Context | User story goal + BDD scenario explain |
| Execution | Prepared test data se steps perform and narrate |
| Result | Actual outcome explain and acceptance criteria se map |

## Mentor-created example — E-commerce coupon

**Context:** “Aaj main valid coupon apply karne ka happy path demonstrate karunga. Acceptance Criteria ke mutabik, valid coupon apply hone par cart total discount ke according reduce hona chahiye.”

**Execution:** Cart open karo, valid coupon enter karo, Apply select karo.

**Result:** “Cart total expected discount se reduce hua. Ye outcome acceptance criteria ke Then clause ko satisfy karta hai.”

## 🎤 Interview answer

**Simple English:**

I structure my demo using Context, Execution, and Result. First I explain the user story and scenario, then perform the steps, and finally explain the outcome by linking it to the acceptance criteria.

**Stronger answer:**

I use a Tell-Show-Tell approach. In the Context stage, I explain the user story and the specific acceptance criterion being demonstrated. In Execution, I perform the prepared steps and narrate them in simple language. In Result, I describe the observed behavior and explicitly connect it to the expected outcome. This keeps the demo focused and gives stakeholders clear evidence rather than a sequence of unexplained clicks.

**Keywords:** Context, Execution, Result, Tell-Show-Tell, BDD, acceptance criteria, observable evidence.

---

# Part 5 — Live demo fail ho jaye to kya karein?

## WHY — Failure ke time professionalism kyun important hai?

Live demo mein failure ho sakta hai. Panic, issue ignore karna, ya audience ke saamne repeatedly debug karna situation ko worse bana sakta hai.

Course reading ke according, failure handle karne ka professional tareeka four steps ka hai.

## Four-step recovery approach

### Step 1 — Acknowledge calmly

Failure ko ignore mat karo. Calmly acknowledge karo.

Example:
“That wasn't expected.”

### Step 2 — State the expected outcome

Acceptance Criteria refer karke batao ki expected behavior kya tha.

Example:
“What we should have seen was a confirmation message, as defined in our success scenario.”

### Step 3 — Promise to investigate

Stakeholders ko reassure karo ki issue track aur investigate hoga.

Example:
“The team and I will investigate this immediately after the review. I will write a new bug ticket to track this so we don't lose sight of it.”

### Step 4 — Move on

- Live demo ke beech fix karne ki koshish mat karo.
- Same action five different ways repeat mat karo.
- Next scenario par move karo.
- Failure ko later bug ticket ke through investigate karo.

Course ka reason: repeated live debugging time waste karti hai aur team unprepared lag sakti hai.

[!IMPORTANT]
Professional response ka matlab failure hide karna nahi. Failure acknowledge karo, expected behavior state karo, follow-up commit karo, aur demo ko continue karo.

## Sample response — Complete

“That wasn't expected. According to our acceptance criteria, the system should display a confirmation message. I will log this as a defect and investigate it with the team after the review. Let's move to the next scenario.”

## 🎤 Interview answer

**Simple English:**

If a demo fails, I acknowledge it calmly, explain the expected behavior using the acceptance criteria, confirm that I will log and investigate the issue, and move to the next scenario instead of debugging live.

**Stronger answer:**

I would not hide or repeatedly retry an unexpected failure during a stakeholder demo. First, I would acknowledge it calmly. Then I would state the expected outcome from the agreed acceptance criteria, explain that the team will investigate it, and create a defect ticket so the issue is tracked. Finally, I would move to the next planned scenario to respect the meeting time and keep the review productive.

**Keywords:** acknowledge, expected behavior, acceptance criteria, defect ticket, investigation, move on, professionalism.

---

# Part 6 — Results ko Acceptance Criteria se connect karna

## WHY

Casual “show and tell” aur professional QA validation mein difference evidence aur requirement traceability ka hai.

Aapko stakeholders ko clear proof dena hai ki jo result dikhaya gaya, woh agreed requirement ko satisfy karta hai.

## Useful linking phrases from course reading

- “This outcome fulfills the 'Then' clause of the scenario.”
- “This demonstrates that we have met the acceptance test for invalid passwords.”
- “As you can see, the system behaves exactly as we defined in the ticket.”

## How to use them

1. Scenario ka expected Then clause identify karo.
2. Actual result observe karo.
3. Compare karo: actual vs expected.
4. Match hone par explicitly say it meets the criterion.
5. Match na ho to failure acknowledge karke defect follow-up karo.

## Example

Acceptance Criteria:
```gherkin
Given I am on the registration page
When I enter a valid username, email, and password and select Register
Then the account is created and I am redirected to the welcome page
```

Demo result:
- Account created.
- Welcome page displayed.

Professional explanation:
“The account was created successfully and the application redirected to the welcome page. This fulfills the Then clause of our agreed acceptance criterion.”

## 🎤 Interview answer

**Simple English:**

I connect every demonstrated result to the acceptance criteria so stakeholders can see exactly which expected behavior has been verified.

**Stronger answer:**

After executing a scenario, I compare the observed result with the expected Then clause. I explicitly state whether the behavior meets the agreed acceptance criterion. If it does not, I acknowledge the mismatch and record it as a defect. This makes the Sprint Review evidence-based and confirms that the team is validating the product against shared expectations.

**Keywords:** expected vs actual, Then clause, traceability, evidence, stakeholder confidence.

---

# Part 7 — Course demo: MindBridge registration

> **Source example:** The video transcript and detailed PDF demonstrate a user registration feature.

## Happy path

User story:
“As a new user, I want to create an account so I can access the application.”

Acceptance Criteria:
```gherkin
Given I'm on the registration page
When I enter a valid username, email, and password and select Register
Then the account is created and I'm redirected to the welcome page
```

Execution:
1. Unique username enter karo.
2. Valid email enter karo.
3. Security standards meet karta password enter karo.
4. Register select karo.

Expected result:
- Account successfully created.
- Welcome page par redirect.

## Negative path — Invalid email

Acceptance Criteria:
```gherkin
Given I'm on the registration page
When I enter an email that is missing an @ symbol
Then I should see a validation error message
```

Execution:
1. Valid username enter karo.
2. Valid password enter karo.
3. Email mein `@` symbol omit karo.
4. Register select karo.

Expected result:
- Invalid email detect ho.
- Helpful validation error show ho.
- Invalid data submit na ho.

Detailed transcript visual shows message: `Please enter a valid email address`.

## Negative path — Expired invitation link

Video ka second scenario:
- Team ne expired invitation link test kiya.
- Expected: expired invitation se access block hona chahiye.
- Actual: application ne user ko playlist partially edit karne diya.
- This exposed a permissions defect that could have become a production security issue.
- Sprint Review mein scenario demonstrate karne se team ko defect identify karne mein help mili.

[!WARNING]
Ye third scenario successful test nahi tha; ye unexpected access behavior tha. Is example ka lesson hai ki negative/permission scenario ka failure bhi stakeholders ke saamne relevant evidence ho sakta hai.

## Source transcript nuance

Video ka opening registration example hai, lekin expired invitation scenario mein playlist editing ka separate permission defect mention hota hai. Dono scenarios ko ek hi registration flow ka part samajhna incorrect hoga.

---

# Part 8 — Common mistakes

1. Sprint Review ko sirf developers ka show-and-tell samajhna.
2. DoD meet na karne wali story ko completed increment ke roop mein showcase karna.
3. Demo mein har test case dikhane ki koshish karna.
4. Happy path skip karke directly negative cases dikhana.
5. Demo se pehle test data/environment prepare na karna.
6. Dry run skip karna.
7. Bina context diye screen par clicks karna.
8. Technical jargon se non-technical stakeholders ko confuse karna.
9. Result ko acceptance criteria se connect na karna.
10. Live failure ko hide karna ya repeatedly debug karna.
11. Defect ticket create kiye bina issue ko verbally mention karke chhod dena.
12. Expected result aur actual result ka difference clearly communicate na karna.

---

# Module 9 — Practice exercises

## Exercise 1 — Scenario selection

Aapko password reset feature Sprint Review mein demonstrate karna hai. Choose:
- One happy path.
- One high-value negative path.
- One DoD quality point to mention.

Har choice ka business reason explain karo.

## Exercise 2 — Prepare a demo script

User story:
“As a customer, I want to apply a discount coupon to my cart.”

Write:
1. Context — 2–3 sentences.
2. Execution — exact steps.
3. Result — acceptance criteria se link.

## Exercise 3 — Live demo failure role-play

Demo ke dauran valid coupon apply karne par cart total update nahi hota.

Stakeholder ke saamne aap exactly kya bologe? Four-step recovery approach follow karo.

## Exercise 4 — Dry-run checklist

Login demo ke liye environment, test data aur scenario readiness ki checklist likho.

## Exercise 5 — Explain the Sprint Review

Simple English mein 60-second answer do:
- Purpose.
- Stakeholders.
- QA role.
- Feedback/backlog.

---

# Module 9 — Progress tracker

- [ ] Sprint Review purpose
- [ ] Inspect increment
- [ ] Gather stakeholder feedback
- [ ] Adapt product backlog
- [ ] QA role in Sprint Review
- [ ] Happy path selection
- [ ] High-value negative path selection
- [ ] DoD quality point
- [ ] Stable demo environment
- [ ] Test data preparation
- [ ] Dry run
- [ ] Context → Execution → Result
- [ ] Tell-Show-Tell
- [ ] Live demo failure recovery
- [ ] Link results to Acceptance Criteria
- [ ] MindBridge registration demo
- [ ] Expired invitation permission defect
- [ ] Practice exercises completed

---

## Source coverage & accuracy notes

- ZIP contains two readings: **Preparing for the Sprint Review** and **Best Practices for Showcasing Tests**.
- It includes subtitle text/VTT and a detailed transcript PDF for **Demoing Completed Tests to Stakeholders**. Subtitle versions were treated as alternate representations of the same video, not separate topics.
- Sprint Review reading defines three goals: inspect the increment, gather feedback, and adapt the backlog.
- It says only stories that meet DoD are eligible to be shown.
- Scenario selection guidance: happy path, one high-value negative path, and a relevant DoD quality point.
- Preparation guidance: stable shared staging/demo environment, prepared test data, and dry run.
- Demo structure is called “Context, Execution, Result” in the reading and also described as “Tell, Show, Tell.”
- Live failure recovery has four steps: acknowledge calmly, state expected outcome, promise investigation/log a bug, move on.
- Video examples: successful registration, invalid email validation, and an expired invitation link that unexpectedly allowed partial playlist editing (permissions defect).
- The source does not specify a mandatory demo duration or exact slide format; none is invented here.
- E-commerce coupon role-play is a mentor-created practice example.
