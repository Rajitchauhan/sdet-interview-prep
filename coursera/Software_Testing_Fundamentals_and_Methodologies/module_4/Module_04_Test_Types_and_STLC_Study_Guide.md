# 🌈 MODULE 04 --- TEST TYPES & SOFTWARE TESTING LIFE CYCLE (STLC)

> **Is module ka goal:** Tum samjho ki software ko *kis angle se test
> karna hai* (Test Types), aur testing ko *systematically kaise organize
> karna hai* (STLC).

::: {align="center"}
🟣 **UNDERSTAND** → 🔵 **CLASSIFY** → 🟢 **MAP TO STLC** → 🟠
**PRACTICE**
:::

  ------------------------------------------------------------------------
  Module                Level                         Suggested study time
  --------------------- --------------------- ----------------------------
  Module 04 --- Test    🟡 Medium                  3--4 focused sessions ·
  Types & STLC                                              2.5--3.5 hours

  ------------------------------------------------------------------------

------------------------------------------------------------------------

## 👋 Is module ko kaise padhna hai?

Har concept ko is order mein samjhaya gaya hai:

1.  **Pehle Hinglish:** Ye kya hai aur kyun zaroori hai?
2.  **Real-world example:** Shopping, login, checkout ya camera example.
3.  **English definition:** Interview aur professional communication ke
    liye.
4.  **Tester perspective:** Project mein kaise apply karoge?
5.  **Interview answer + practice:** Samajh ko check karne ke liye.

> \[!IMPORTANT\] Is file ka content tumhare **Module 4 ZIP** ke reading,
> subtitles aur detailed video transcripts par based hai. Jahan main
> example ko easy banane ke liye apni taraf se scenario add karta hoon,
> use **Mentor example** mark kiya hai. Course ke source mein jo framing
> hai, use bina bataye replace nahi kiya gaya hai.

## 🧭 Learning map

  Section   Topic                                    Difficulty
  --------- ---------------------------------------- ------------
  1         Test Types ka overview                   🟢 Easy
  2         Functional Testing                       🟢 Easy
  3         Black-box vs White-box                   🟡 Medium
  4         Non-functional Testing                   🟡 Medium
  5         Maintenance & Regression Testing         🟢 Easy
  6         STLC --- 6 phases                        🟡 Medium
  7         Test Types ko STLC phases se map karna   🟡 Medium
  8         Swim-lane diagram                        🟡 Medium
  9         Practical scenario & exercises           🟡 Medium

------------------------------------------------------------------------

# 🟣 PART 1 --- TEST TYPES: SOFTWARE KO KIS TARAH TEST KARTE HAIN?

## 1. Test Types kya hote hain?

### 🧠 Pehle apni language mein samjho

Socho tumne ek naya smartphone kharida.

Tum phone ko sirf ek baar on karke decide nahi kar sakte ki phone achha
hai. Tum alag-alag cheezein check karoge:

-   Camera photo le raha hai ya nahi?
-   Battery poora din chalti hai ya nahi?
-   Menu use karna easy hai ya confusing?
-   Software update ke baad pehle wale features abhi bhi kaam kar rahe
    hain ya nahi?

Har check ka purpose alag hai. Software mein bhi hum different **Test
Types** use karte hain, kyunki ek hi type ki testing se product ki saari
qualities check nahi hoti.

### 📘 English definition

**Test Type:** A classification of testing based on the particular
quality characteristic, behavior, or objective being evaluated.

### Course reading ke according 3 broad categories

`<box>`{=html}

`</box>`{=html}

  -----------------------------------------------------------------------
  Category                Simple question         Kya check karti hai?
  ----------------------- ----------------------- -----------------------
  **Functional Testing**  Feature kya karta hai?  Requirements ke
                                                  according behavior

  **Non-functional        Feature kitni achhi     Performance, usability
  Testing**               tarah kaam karta hai?   jaise characteristics

  **Maintenance Testing** Change ke baad pehle    Modification ke baad
                          wale features abhi bhi  existing behavior
                          theek hain?             
  -----------------------------------------------------------------------

### 📌 Yaad rakhne ka shortcut

-   Functional = **What does it do?**
-   Non-functional = **How well does it work?**
-   Maintenance = **Does it still work after a change?**

### 🎤 Interview answer

"Software testing includes different test types because we need to
evaluate both feature behavior and overall product quality. Functional
testing checks what the software does, non-functional testing checks how
well it works, and maintenance testing checks the impact of changes on
the existing system."

------------------------------------------------------------------------

# 🔵 PART 2 --- FUNCTIONAL TESTING

## 2. Functional Testing kya hoti hai?

### 🧠 Pehle apni language mein samjho

Maan lo tum ek website par **Forgot Password** use kar rahe ho.

Tum registered email enter karte ho aur Submit click karte ho. Ab
expected behavior kya hai?

-   Registered email doge → password reset email send honi chahiye.
-   Invalid email doge → error message show hona chahiye.

Yahan hum check kar rahe hain ki feature requirement ke according kaam
kar raha hai ya nahi.

Yahi Functional Testing hai.

### 📘 English definition

**Functional Testing:** Testing that verifies whether software functions
behave according to specified requirements.

### Course reading ka example --- Forgot Password

  Input                                        Expected output
  -------------------------------------------- --------------------------------------
  Valid registered email: `user@example.com`   Reset email sent
  Invalid email: `notanemail`                  "Email not found" type error message

### Tester ka focus

Functional testing mein tester check karta hai: - Correct input dene par
correct output milta hai? - Invalid input par expected error aata hai? -
Button/action expected behavior perform karta hai? - Business rule
correctly apply hota hai?

Course reading ke according functional testing inputs aur expected
outputs par focus karti hai; result kaise produce hua, us internal
implementation par zaroori nahi ki tester depend kare.

## 2.1 Functional Testing ke two approaches

Course reading functional testing ke do primary approaches batati hai:

1.  Black-box Testing
2.  White-box Testing

Inka difference next section mein detail se samjhenge.

### 🎤 Interview answer

"Functional testing verifies that application features work according to
the specified requirements. For example, in a forgot-password feature, a
registered email should trigger a reset email, while an invalid email
should display an appropriate error."

`<badge color="success">`{=html}Key point`</badge>`{=html} Functional
testing feature ke expected behavior ko validate karti hai.

------------------------------------------------------------------------

# 🟡 PART 3 --- BLACK-BOX VS WHITE-BOX TESTING

## 3. Black-box Testing

### 🧠 Pehle apni language mein samjho

Maan lo tum ATM use kar rahe ho. Tumhe ATM ke andar ka source code nahi
pata. Tum bas: - Card insert karte ho. - PIN enter karte ho. - Amount
select karte ho. - Cash receive hota hai ya error, ye check karte ho.

Tum input aur output ke basis par test kar rahe ho. System ke andar code
kaise likha hai, uski knowledge required nahi.

Ye Black-box Testing ka basic idea hai.

### 📘 English definition

**Black-box Testing:** A testing approach in which the tester evaluates
software behavior through inputs and outputs without needing knowledge
of the internal code structure or implementation.

### Course reading ke according

-   Tester ko internal code ka knowledge nahi hota.
-   Focus inputs aur outputs par hota hai.
-   External user perspective se application evaluate hoti hai.
-   Course reading is approach ko QA testers ke common approach ke roop
    mein describe karti hai.

### Example --- Login form

  Step   Action
  ------ --------------------------------------------------------
  1      Username enter karo
  2      Password enter karo
  3      Sign In click karo
  4      Dashboard load hota hai ya error aata hai, verify karo

Tumhe login function ka internal code dekhne ki zaroorat nahi. Tum
expected behavior check kar rahe ho.

## 3.1 White-box Testing

### 🧠 Pehle apni language mein samjho

Ab imagine karo tum developer ho aur tumhare paas login function ka
source code available hai.

Code mein conditions hain:

``` python
if username_exists and password_is_valid:
    login_success()
else:
    show_error()
```

Ab tum check kar sakte ho ki: - `if` condition true hone par correct
branch execute hoti hai? - `else` condition par error path execute hota
hai? - Different internal paths correctly behave karte hain?

Yahan tum system ke internal logic ko dekhkar test kar rahe ho.

### 📘 English definition

**White-box Testing:** A testing approach in which tests are designed
with knowledge of the internal code structure, logic, conditions, and
execution paths.

### Course reading ke according

-   Tester/developer ko internal code aur architecture ka access hota
    hai.
-   Focus internal logic, branches, loops aur code paths par hota hai.
-   Course reading ise typically developers ke saath associate karti
    hai.

### Black-box vs White-box --- Comparison

  -----------------------------------------------------------------------
  Point                   Black-box               White-box
  ----------------------- ----------------------- -----------------------
  Code visibility         Code knowledge required Internal code access
                          nahi                    hota hai

  Focus                   Inputs and outputs      Internal logic and code
                                                  paths

  Perspective             External / user         Internal / code
                          perspective             perspective

  Course reading: typical QA testers              Developers
  performer                                       

  Example                 Login form behavior     If-else branch test
                          test                    
  -----------------------------------------------------------------------

> \[!NOTE\] Course reading typical roles batati hai, lekin ye strict
> rule nahi ki QA engineer kabhi white-box testing nahi kar sakta ya
> developer black-box testing nahi kar sakta. Is module ka main
> distinction code visibility aur testing focus hai.

### 🎤 Interview answer

"Black-box testing checks the behavior of an application through inputs
and outputs without requiring knowledge of internal code. White-box
testing uses knowledge of the internal implementation to verify logic,
branches, loops, and execution paths. Black-box testing focuses on
external behavior, while white-box testing focuses on internal code
structure."

### 🧪 Quick check

Login page par: - Valid username/password enter karke dashboard verify
karna --- Black-box. - Login function ke true/false branches test karna
--- White-box.

------------------------------------------------------------------------

# 🟠 PART 4 --- NON-FUNCTIONAL TESTING

## 4. Non-functional Testing kya hoti hai?

### 🧠 Pehle apni language mein samjho

Maan lo tumne ek online shopping website banayi.

Website ka search feature correctly product find kar leta hai.
Functional requirement pass hai.

Lekin: - Search result aane mein 20 seconds lagte hain. - 500 users ek
saath search karein to website crash ho jati hai. - Search button aur
filters itne confusing hain ki users product find nahi kar paate.

Feature kaam to kar raha hai, lekin overall experience achha nahi.

Yahan Non-functional Testing important hai.

### 📘 English definition

**Non-functional Testing:** Testing that evaluates system quality
characteristics such as performance, usability, and other aspects of how
well the software operates.

### Functional vs Non-functional

  -----------------------------------------------------------------------
  Functional                          Non-functional
  ----------------------------------- -----------------------------------
  Feature kya karta hai?              Feature kitni achhi tarah karta
                                      hai?

  Expected behavior                   Quality characteristics

  Example: Login successful hota hai? Example: Login response fast hai?

  Example: Search correct result deta Example: Search use karna easy hai?
  hai?                                
  -----------------------------------------------------------------------

## 4.1 Performance Testing

### 🧠 Pehle apni language mein samjho

Ek railway ticket booking website par normal time mein 10 users hain,
sab kuch fast chal raha hai.

Lekin Tatkal booking open hote hi 10,000 users ek saath website use
karte hain. Website slow ho jati hai ya crash kar deti hai.

Ab question ye nahi ki booking feature exist karta hai ya nahi. Question
hai ki load/pressure mein system ka behavior kaisa hai.

### 📘 English definition

**Performance Testing:** Testing that evaluates how a system behaves in
terms of speed, responsiveness, and stability under a particular
workload.

### Course reading ke questions

-   1,000 users ek saath sign in karein to login page kitni der mein
    load hota hai?
-   Very large file upload karne par application crash hoti hai?
-   Mobile app kitni battery consume karti hai?

### Performance testing kya evaluate karti hai?

-   Load time
-   Response speed
-   Stability under workload
-   Multiple active users ke time behavior

### Course video ka STLC connection

Performance testing **Test Execution** phase mein map ki gayi hai,
kyunki actual running software chahiye jiske load time, response speed
aur stability ko measure kiya ja sake.

## 4.2 Usability Testing

### 🧠 Pehle apni language mein samjho

Maan lo ek app mein Logout button available hai, lekin itna hidden hai
ki 5 users mein se 4 users use find nahi kar pa rahe.

Technically logout feature present hai. Lekin use karna difficult hai.

Usability testing check karti hai ki real users application ko easily
samajh aur use kar pa rahe hain ya nahi.

### 📘 English definition

**Usability Testing:** Testing that evaluates how easy, intuitive, and
user-friendly software is by observing users as they attempt to complete
tasks.

### Course reading ka example

Agar multiple users: - Logout button find nahi kar pa rahe. - Error
message samajh nahi pa rahe. - Application navigate karne mein confused
hain.

To usability problem ho sakti hai.

### Course video ka STLC connection

Usability testing bhi **Test Execution** phase mein map ki gayi hai,
kyunki running software ko real users ke saamne rakhkar unka behavior
observe karna hota hai.

### Performance vs Usability

  -----------------------------------------------------------------------
  Performance Testing                 Usability Testing
  ----------------------------------- -----------------------------------
  Speed, response, stability          Ease of use, navigation, clarity

  System workload mein kaisa behave   User task easily complete kar pata
  karta hai?                          hai?

  Example: 1,000 users ke load par    Example: User easily Login/Logout
  login                               find kar sakta hai?
  -----------------------------------------------------------------------

### 🎤 Interview answer

"Non-functional testing evaluates how well a system operates rather than
only checking whether a feature works. Performance testing evaluates
speed, responsiveness, and stability under workload. Usability testing
evaluates whether users can navigate and use the application easily."

------------------------------------------------------------------------

# 🟢 PART 5 --- MAINTENANCE TESTING & REGRESSION TESTING

## 5. Maintenance Testing kya hoti hai?

### 🧠 Pehle apni language mein samjho

Maan lo tumhari shopping app already production mein chal rahi hai.

Developer ne: - New discount feature add kiya. - Existing checkout bug
fix kiya. - Payment code update kiya.

Ab change ke baad application ko dobara evaluate karna zaroori hai.
Kyunki software ke ek area mein change ka impact doosre areas par bhi aa
sakta hai.

### 📘 English definition

**Maintenance Testing:** Testing performed to evaluate a software system
after it has been modified, updated, or otherwise changed.

## 5.1 Regression Testing

### 🧠 Pehle apni language mein samjho

Tumhari shopping website mein developer ne discount code apply karne ka
bug fix kiya.

Ab sirf discount feature check karna enough nahi. Ho sakta hai code
change ki wajah se: - Login break ho gaya. - Product search kaam na
kare. - Cart total wrong ho jaye. - Payment flow fail ho jaye.

Isliye pehle se working features ko dobara test karte hain. Ye
Regression Testing hai.

### 📘 English definition

**Regression Testing:** Re-executing existing tests after a change to
confirm that previously working functionality has not been
unintentionally broken.

### Course reading ka example

Developer discount-code bug fix karta hai. Regression test mein: -
Login - Product search - Payment process

dobara validate kiye jate hain, taaki fix ne doosre features ko break na
kiya ho.

### Course video ka important nuance

Video Regression Testing ko STLC ke **Test Cycle Closure** phase mein
map karta hai, kyunki fixes ke baad existing tests rerun kiye jaate
hain.

Lekin video explicitly ye bhi kehta hai:

-   Regression testing sirf ek baar nahi hoti.
-   Project ke dauran significant change hone par bhi trigger hoti hai.
-   Ye recurring safety net hai.

### Maintenance vs Regression

  -----------------------------------------------------------------------
  Maintenance Testing                 Regression Testing
  ----------------------------------- -----------------------------------
  Modification ke baad system         Existing behavior ko change ke baad
  evaluate karna                      recheck karna

  Broad category in course reading    Course reading ke mutabik important
                                      maintenance test type

  Updates, bug fixes, changes ke baad Check karta hai ki old features
                                      accidentally break na hue
  -----------------------------------------------------------------------

### 🎤 Interview answer

"Maintenance testing is performed after software changes or updates.
Regression testing is an important type of maintenance testing in which
existing tests are rerun to ensure that recent changes have not broken
previously working functionality."

`<badge color="success">`{=html}Remember`</badge>`{=html} Regression
Testing = "New change ne purana working feature to nahi toda?"

------------------------------------------------------------------------

# 🔵 PART 6 --- SOFTWARE TESTING LIFE CYCLE (STLC)

## 6. STLC kya hai?

### 🧠 Pehle apni language mein samjho

Socho tum ghar bana rahe ho.

Kya tum bina plan ke seedha bricks lagana start kar doge? Nahi.

Pehle: 1. Samjhoge ghar mein kya-kya chahiye. 2. Budget aur resources
decide karoge. 3. Blueprint banaoge. 4. Construction site ready karoge.
5. Building construct/check karoge. 6. Final inspection aur report
banaoge.

Software testing mein bhi aisa structured process hota hai. Tester
randomly application open karke buttons click nahi karta. Testing ko
organize karne ke liye STLC follow kiya jata hai.

### 📘 English definition

**Software Testing Life Cycle (STLC):** A structured sequence of testing
activities that guides a testing team from understanding what needs to
be tested through planning, test design, environment setup, execution,
and test cycle closure.

### STLC kyun zaroori hai?

Without a structured process: - Team same kaam repeat kar sakti hai. -
Important test areas miss ho sakte hain. - Test execution inconsistent
ho sakta hai. - Defects properly record nahi honge. - Stakeholders ko
release readiness ka clear picture nahi milega.

### Course video ke according STLC ki 6 phases

`<box border radius="lg" padding={3} gap={2}>`{=html}
`<row align="center" gap={2}>`{=html}
`<badge color="info">`{=html}01`</badge>`{=html} **Requirement
Analysis** `</row>`{=html}
`<text color="secondary" size="sm">`{=html}What exactly needs to be
tested?`</text>`{=html} `<divider color="subtle"/>`{=html}
`<row align="center" gap={2}>`{=html}
`<badge color="info">`{=html}02`</badge>`{=html} **Test Planning**
`</row>`{=html} `<text color="secondary" size="sm">`{=html}How will we
test, and with what?`</text>`{=html} `<divider color="subtle"/>`{=html}
`<row align="center" gap={2}>`{=html}
`<badge color="info">`{=html}03`</badge>`{=html} **Test Design**
`</row>`{=html} `<text color="secondary" size="sm">`{=html}What are the
exact steps for each test?`</text>`{=html}
`<divider color="subtle"/>`{=html} `<row align="center" gap={2}>`{=html}
`<badge color="info">`{=html}04`</badge>`{=html} **Test Environment
Setup** `</row>`{=html} `<text color="secondary" size="sm">`{=html}Where
and on what will we test?`</text>`{=html}
`<divider color="subtle"/>`{=html} `<row align="center" gap={2}>`{=html}
`<badge color="info">`{=html}05`</badge>`{=html} **Test Execution**
`</row>`{=html} `<text color="secondary" size="sm">`{=html}Does the
software behave as expected?`</text>`{=html}
`<divider color="subtle"/>`{=html} `<row align="center" gap={2}>`{=html}
`<badge color="info">`{=html}06`</badge>`{=html} **Test Cycle Closure**
`</row>`{=html} `<text color="secondary" size="sm">`{=html}What did we
learn, and are we ready to ship?`</text>`{=html} `</box>`{=html}

Course video STLC ko building blocks ke jaisa describe karta hai: har
phase ka output next phase ko support karta hai.

------------------------------------------------------------------------

## 6.1 Phase 1 --- Requirement Analysis

### 🧠 Hinglish explanation

Testing start karne se pehle tester ko samajhna hoga ki feature karna
kya chahta hai.

Example: Shopping website ka Search Bar.

Requirement mein likha hai: "User product search kar sake."

Tester questions: - Product name se search hoga? - Partial name allowed
hai? - Uppercase/lowercase matter karta hai? - No result par kya show
hoga? - Empty search ka behavior kya hoga?

Agar requirement unclear hai to tester ko usko flag karna chahiye.

### 📘 English definition

**Requirement Analysis:** The STLC phase in which testers read and
analyze requirements, feature descriptions, and user stories to
understand what needs to be tested and identify unclear or contradictory
information.

### Course video ka key question

**"What exactly needs to be tested?"**

### Key activities

-   Requirement documents read karna.
-   Feature descriptions/user stories understand karna.
-   Testable requirements identify karna.
-   Missing, unclear ya contradictory requirements flag karna.

### Output / result

Course video is phase ke liye exact named deliverable list nahi karta.
Practical result hota hai requirements ki testing understanding aur
clarification points, jin par planning ki ja sake.

------------------------------------------------------------------------

## 6.2 Phase 2 --- Test Planning

### 🧠 Hinglish explanation

Ab tumhe pata hai kya test karna hai. Next question: testing karoge
kaise?

Example: Search feature test karna hai.

Team decide karegi: - Kaun test karega? - Kaunse tools use honge? -
Kitna time lagega? - Resources/budget kya hain? - Testing ka scope kya
hoga?

### 📘 English definition

**Test Planning:** The STLC phase in which the team defines the testing
strategy, scope, resources, responsibilities, tools, schedule, and
budget.

### Course video ka key question

**"How will we test, and with what?"**

### Key activities

-   Testing approach/strategy decide karna.
-   Tools select karna.
-   Responsibilities assign karna.
-   Time/schedule estimate karna.
-   Budget/resources consider karna.

### Course source ka output

**Test Plan** --- master document jo aage ke testing decisions guide
karta hai.

> \[!NOTE\] Subtitle extraction mein ek jagah "test flight" likha hua
> tha, lekin detailed transcript aur context clearly "test plan" confirm
> karte hain. Is guide mein correct source term **Test Plan** use kiya
> gaya hai.

------------------------------------------------------------------------

## 6.3 Phase 3 --- Test Design

### 🧠 Hinglish explanation

Ab team ko pata hai kya test karna hai aur kaise organize karna hai.

Ab individual test cases likhe jayenge.

Example: Login feature.

1.  Username enter karo.
2.  Password enter karo.
3.  Sign In click karo.
4.  Expected: Dashboard successfully load ho.

Test case aisa hona chahiye ki team ka koi bhi tester same steps follow
karke consistent result verify kar sake.

### 📘 English definition

**Test Design:** The STLC phase in which detailed test cases are
created, including the actions to perform, test data to use, and
expected results.

### Course video ka key question

**"What are the exact steps for each test?"**

### Course video example

  Field             Login test case
  ----------------- ------------------------------
  Username          `Alex@example.com`
  Password          `test@1234`
  Action            Select Sign In
  Expected result   Dashboard loads successfully

Ye course video ka example hai; ise real credential ke roop mein use
nahi karna.

### Test case mein kya clear hona chahiye?

-   What to do --- action/steps.
-   What data to use --- inputs.
-   What result to expect --- expected outcome.

------------------------------------------------------------------------

## 6.4 Phase 4 --- Test Environment Setup

### 🧠 Hinglish explanation

Test case ready hai, lekin test run kahan karoge?

Maan lo tum mobile app test kar rahe ho. Tumhe correct: - Device/OS -
App version - Network settings - Test data - User account and
permissions

ready chahiye.

Wrong environment mein test pass ho sakta hai, lekin real environment
mein fail ho sakta hai.

### 📘 English definition

**Test Environment Setup:** The STLC phase in which the required
hardware, software, network settings, test data, and configurations are
prepared for reliable testing.

### Course video ka key question

**"Where and on what will we test?"**

### Course source ke activities

-   Servers setup karna.
-   Correct software versions install karna.
-   Database mein test data load karna.
-   Correct permissions ke saath user accounts configure karna.
-   Hardware/software/network conditions prepare karna.

### Course ka important message

A test that passes in the wrong environment but fails in the real one is
not a reliable passing result.

------------------------------------------------------------------------

## 6.5 Phase 5 --- Test Execution

### 🧠 Hinglish explanation

Ab planning, test cases aur environment ready hain. Ab actual testing
start hogi.

Tester: - Test cases follow karega. - Inputs enter karega. - Actions
perform karega. - Actual result record karega. - Expected aur actual
compare karega.

Agar pass hua, pass record karo. Agar fail hua, defect document karo.

### 📘 English definition

**Test Execution:** The STLC phase in which testers run the designed
test cases in the prepared environment, record results, and report
defects when actual behavior differs from expected behavior.

### Course video ka key question

**"Does the software behave as expected?"**

### Course source ke activities

-   Phase 3 ke test cases follow karna.
-   Phase 4 ke environment mein tests run karna.
-   Results record karna.
-   Passed tests log karna.
-   Failed tests ko defects ke roop mein document karna.
-   Defect report development team ko dena for investigation and fix.

### Defect report mein course ke mutabik

-   What was tested.
-   What was expected.
-   Exactly what went wrong.

------------------------------------------------------------------------

## 6.6 Phase 6 --- Test Cycle Closure

### 🧠 Hinglish explanation

Testing execute ho gayi. Ab team ko overall picture dekhni hai.

Maan lo: - 100 tests run hue. - 85 pass hue. - 10 fail hue. - 5 blocked
hue. - 4 defects fix hue. - 6 issues abhi open hain.

Ab stakeholders ko pata hona chahiye ki testing ka outcome kya raha aur
release ke liye kya risks abhi bhi hain.

### 📘 English definition

**Test Cycle Closure:** The STLC phase in which the team reviews and
summarizes testing outcomes, documents lessons learned, and provides
information to support release decisions.

### Course video ka key question

**"What did we learn, and are we ready to ship?"**

### Course source ke review questions

-   Kitne tests run hue?
-   Kitne pass hue?
-   Kitne defects find/fix hue?
-   Kya open issues abhi risk carry karte hain?

### Course source ka output

**Test Summary Report** --- final quality record jise stakeholders
release readiness decision mein use karte hain.

### Lessons learned

-   Kya achha work kiya?
-   Kis cheez ne team ko slow kiya?
-   Next cycle ko faster/sharper kaise banaya ja sakta hai?

------------------------------------------------------------------------

## 6.7 Six phases --- Complete revision table

  -----------------------------------------------------------------------
  Phase             Key question      Main work         Course source
                                                        output / result
  ----------------- ----------------- ----------------- -----------------
  1\. Requirement   What needs        Requirements      Testing
  Analysis          testing?          read, understand, understanding /
                                      flag gaps         clarification
                                                        points

  2\. Test Planning How will we test  Strategy, tools,  Test Plan
                    and with what?    roles, time,      
                                      budget            

  3\. Test Design   What are the      Test cases, data, Test cases
                    exact test steps? expected results  

  4\. Environment   Where and on what Servers,          Prepared test
  Setup             will we test?     software, data,   environment
                                      accounts,         
                                      permissions       

  5\. Test          Does software     Run tests, record Test results and
  Execution         behave as         pass/fail, report defect reports
                    expected?         defects           

  6\. Test Cycle    What did we       Review results,   Test Summary
  Closure           learn; ready to   open risks,       Report
                    ship?             lessons           
  -----------------------------------------------------------------------

### STLC flow

``` text
REQUIREMENT ANALYSIS
        |
        v
TEST PLANNING
        |
        v
TEST DESIGN
        |
        v
TEST ENVIRONMENT SETUP
        |
        v
TEST EXECUTION
        |
        v
TEST CYCLE CLOSURE
        |
        v
TEST SUMMARY REPORT
```

------------------------------------------------------------------------

# 🟣 PART 7 --- MAPPING TEST TYPES TO STLC PHASES

## 7. Course video ka main idea

### 🧠 Pehle apni language mein samjho

Har test type ko har phase mein run nahi kar sakte.

Example: - Requirement document ko review karne ke liye application ka
running hona zaroori nahi. - Performance test karne ke liye working
application chahiye. - Usability test mein real users ko software use
karte dekhna hota hai. - Regression test changes/fixes ke baad existing
features ko recheck karta hai.

Isliye course video test types ko STLC phases ke saath map karta hai.

### 📘 English definition

**Test Type Mapping to STLC:** Assigning testing activities to the STLC
phases where they are most effective and can produce useful results.

## 7.1 Course video ka swim-lane diagram concept

Video ke according: - Har **column** ek STLC phase represent karta
hai. - Har **horizontal lane** ek testing category represent karti
hai. - Test types ko un phases mein place kiya jata hai jahan unka
purpose best serve hota hai.

Video visual legend: - 🔵 Blue = Functional testing. - 🟠 Orange =
Non-functional testing. - 🟣 Purple = STLC phase labels/static testing
marker in the visual.

## 7.2 Test type mapping --- course video

  --------------------------------------------------------------------------
  STLC phase              Course video mein       Why here?
                          mapped test type        
  ----------------------- ----------------------- --------------------------
  Requirement Analysis    Static Testing ---      Requirements code se pehle
                          requirements review     review ho sakti hain

  Test Planning           Video mein specific     Strategy/scope/resources
                          test type place nahi    decide hote hain
                          kiya                    

  Test Design             Equivalence             Functional test cases/data
                          Partitioning, Boundary  design hote hain
                          Value Analysis          

  Test Environment Setup  Video mein specific     Test environment prepare
                          test type place nahi    hota hai
                          kiya                    

  Test Execution          Performance Testing,    Running software aur real
                          Usability Testing       user/system behavior
                                                  observe karna hota hai

  Test Cycle Closure      Regression Testing      Fixes ke baad existing
                                                  tests rerun; changes par
                                                  project ke dauran bhi
                                                  repeat
  --------------------------------------------------------------------------

> \[!IMPORTANT\] Ye table **uploaded course video ka specific mapping**
> hai. Iska matlab ye nahi ki real-world teams sirf in phases mein hi ye
> test types perform karti hain. Video khud kehta hai regression testing
> significant changes ke baad poore project mein repeat hoti hai.

## 7.3 Static Testing → Requirement Analysis

### Hinglish explanation

Software abhi bana hi nahi. Lekin requirements document available hai.
Tester document padhkar check kar sakta hai: - Koi requirement unclear
hai? - Do requirements contradict kar rahi hain? - Koi important rule
missing hai?

### English definition

**Static Testing:** Examining work products such as requirements without
executing the software.

### Why this phase?

Course video ke according requirement analysis mein written requirements
review hoti hain, code likhne se pehle.

------------------------------------------------------------------------

## 7.4 Equivalence Partitioning → Test Design

### Hinglish explanation

Maan lo age field mein 18 se 65 years tak ki age accept hoti hai.

Possible values bahut saari hain: - 18, 19, 20, 21... - 65 tak.

Har number test karna zaroori nahi. Hum inputs ko groups mein divide kar
sakte hain jinke behavior same expected hain.

Example groups: - Below 18 = invalid group. - 18--65 = valid group. -
Above 65 = invalid group.

Har group se representative value choose karte hain.

### English definition

**Equivalence Partitioning:** A test design technique that divides
possible input values into groups expected to behave similarly, then
selects representative values from those groups.

### Course-style example

  Partition     Example value Expected
  ----------- --------------- ----------
  Below 18                 17 Reject
  18 to 65                 30 Accept
  Above 65                 66 Reject

### Why Test Design?

Course video ke according equivalence partitions identify karke
representative test data aur test cases design kiye jaate hain.

------------------------------------------------------------------------

## 7.5 Boundary Value Analysis → Test Design

### Hinglish explanation

Bugs aksar range ke edges par mil sakte hain.

Agar age 18--65 allowed hai, to important values: - Minimum se just
below: 17 - Minimum: 18 - Maximum: 65 - Maximum se just above: 66

Hum beech ke har number ko test nahi kar rahe; range ke boundaries check
kar rahe hain.

### English definition

**Boundary Value Analysis (BVA):** A test design technique that focuses
on values at the edges of input ranges, such as minimum, maximum, and
values just outside those limits.

### Course video ka exact example

Rule: Ages 18--65 accepted.

    Test value Expected
  ------------ ----------
            17 Reject
            18 Accept
            65 Accept
            66 Reject

### Why Test Design?

Ye technique test cases aur test data create karte waqt use hoti hai.
Course video isse STLC ke Test Design phase mein place karta hai.

------------------------------------------------------------------------

## 7.6 Performance Testing → Test Execution

### Hinglish explanation

Performance test karne ke liye running application chahiye. Tabhi
response speed, load time aur workload ke under stability
observe/measure kar sakte ho.

### English definition

**Performance Testing:** Evaluating system speed, responsiveness, and
stability under a specified workload.

### Why Test Execution?

Course video ke according software ko execute/run karna zaroori hai,
tabhi pressure/load ke under behavior evaluate kar sakte hain.

------------------------------------------------------------------------

## 7.7 Usability Testing → Test Execution

### Hinglish explanation

Usability check karne ke liye actual interface working condition mein
chahiye. Real users ko tasks perform karte observe karna hota hai.

### English definition

**Usability Testing:** Evaluating how easily and intuitively users can
navigate and complete tasks in an application.

### Why Test Execution?

Course video ke according working software real users ke saamne rakhkar
unka interaction observe karna hota hai.

------------------------------------------------------------------------

## 7.8 Regression Testing → Test Cycle Closure (and recurring throughout project)

### Hinglish explanation

Developer ne bug fix kiya. Ab confirm karna hai ki pehle se working
features break nahi hue.

Course video ise Test Cycle Closure ke saath map karta hai, kyunki fixes
ke baad existing tests rerun hote hain.

Lekin regression sirf closure par ek baar nahi hoti. Significant changes
ke baad project ke dauran bhi repeat hoti hai.

### English definition

**Regression Testing:** Re-running existing tests after software changes
to verify that previously working functionality has not been
unintentionally affected.

### Why this mapping?

Course video ke according changes/fixes ke baad regression testing
existing behavior ko protect karti hai. Isliye visual map mein Test
Cycle Closure par place ki gayi hai, with an explicit note that it
recurs throughout the project.

------------------------------------------------------------------------

## 7.9 Full mapping --- one-page revision

  -----------------------------------------------------------------------
  Test type / technique               STLC phase in course video
  ----------------------------------- -----------------------------------
  Static requirements review          Requirement Analysis

  Equivalence Partitioning            Test Design

  Boundary Value Analysis             Test Design

  Performance Testing                 Test Execution

  Usability Testing                   Test Execution

  Regression Testing                  Test Cycle Closure; also recurring
                                      after significant changes
  -----------------------------------------------------------------------

### 🎯 Course video ka central lesson

"Are we running the right tests at the right moments?"

Test type ka naam ya definition yaad karna enough nahi. Ye bhi samjho ki
usko particular phase mein kyun place kiya gaya hai.

------------------------------------------------------------------------

# 🧪 PART 8 --- PRACTICAL SCENARIO

## 8. E-commerce Search Bar --- STLC exercise

Course STLC video ke end mein shopping website ke Search Bar ka example
diya gaya hai. Tumhe first three phases ke liye ek key activity describe
karni hai.

### Scenario

Shopping website par user product search kar sakta hai.

### Phase 1 --- Requirement Analysis

**Mentor example:** - Search product name se hota hai ya category se? -
Partial keyword supported hai? - No results par kya show hoga? - Empty
input par kya hoga?

### Phase 2 --- Test Planning

**Mentor example:** - Search feature ka testing scope define karna. -
Manual/automation tools decide karna. - Tester responsibility assign
karna. - Schedule estimate karna.

### Phase 3 --- Test Design

**Mentor example:**

  Test case                 Input      Expected result
  ------------------------- ---------- -------------------------------------------
  Search existing product   `iPhone`   Matching products displayed
  Search unknown product    `xyz123`   No results message
  Empty search              blank      Requirement-defined behavior
  Partial keyword           `iph`      Requirement ke according matching results

Ye table practice ke liye mentor-created examples hain; uploaded source
mein exact test cases nahi diye gaye.

## 8.1 Full STLC for one feature

  -----------------------------------------------------------------------
  Phase                               Search feature par activity
  ----------------------------------- -----------------------------------
  Requirement Analysis                Search behavior and rules
                                      understand

  Test Planning                       Scope, tools, responsibilities,
                                      schedule decide

  Test Design                         Search test cases and input data
                                      create

  Environment Setup                   App, browser, server, test data
                                      ready

  Test Execution                      Test cases run; pass/fail and
                                      defects record

  Test Cycle Closure                  Results, open defects, risks and
                                      lessons summarize
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 🎤 PART 9 --- INTERVIEW PREPARATION

## 9.1 Important English definitions

  -----------------------------------------------------------------------
  Term                                English definition
  ----------------------------------- -----------------------------------
  Functional Testing                  Verifies that software functions
                                      behave according to specified
                                      requirements.

  Black-box Testing                   Evaluates behavior through inputs
                                      and outputs without requiring
                                      internal code knowledge.

  White-box Testing                   Designs tests using knowledge of
                                      internal code, logic, and execution
                                      paths.

  Non-functional Testing              Evaluates quality characteristics
                                      such as performance and usability.

  Performance Testing                 Evaluates speed, responsiveness,
                                      and stability under workload.

  Usability Testing                   Evaluates how easy and intuitive
                                      software is for users.

  Maintenance Testing                 Evaluates software after it has
                                      been modified or updated.

  Regression Testing                  Re-runs existing tests after
                                      changes to ensure existing
                                      functionality still works.

  STLC                                A structured sequence of activities
                                      that guides the testing process
                                      from requirements to closure.

  Test Planning                       Defines testing strategy, scope,
                                      resources, responsibilities, tools,
                                      and schedule.

  Test Design                         Creates test cases with steps, test
                                      data, and expected results.

  Test Execution                      Runs test cases and records
                                      results/defects.

  Test Cycle Closure                  Reviews testing outcomes, risks,
                                      lessons learned, and release
                                      readiness.

  Equivalence Partitioning            Divides inputs into groups expected
                                      to behave similarly and selects
                                      representatives.

  Boundary Value Analysis             Tests values at and around input
                                      range boundaries.
  -----------------------------------------------------------------------

## 9.2 Interview questions

1.  What are the main categories of software testing described in this
    module?
2.  What is the difference between functional and non-functional
    testing?
3.  Explain black-box and white-box testing.
4.  What is performance testing?
5.  What is usability testing?
6.  What is maintenance testing?
7.  What is regression testing and why is it important?
8.  What is STLC?
9.  Explain the six phases of STLC.
10. What is the output of test planning?
11. What happens during test design?
12. Why is test environment setup important?
13. What is test cycle closure?
14. What is equivalence partitioning?
15. What is boundary value analysis?
16. Why are performance and usability testing mapped to test execution
    in the course video?
17. Why does the course map regression testing to test cycle closure,
    and what nuance does it mention?

## 9.3 Strong answer --- Explain STLC

"STLC is a structured process that organizes testing activities into six
phases. Requirement Analysis helps testers understand what needs to be
tested and identify unclear requirements. Test Planning defines the
strategy, scope, resources, responsibilities, tools, and schedule. Test
Design creates detailed test cases with steps, test data, and expected
results. Test Environment Setup prepares the required hardware,
software, network, accounts, and data. Test Execution runs the test
cases and records results and defects. Finally, Test Cycle Closure
summarizes testing outcomes, open risks, and lessons learned through a
test summary report. Each phase provides inputs for the next phase and
makes testing more controlled and repeatable."

------------------------------------------------------------------------

# 📝 PART 10 --- PRACTICE & SELF-ASSESSMENT

## Exercise A --- Identify the test type

Har situation ko classify karo: Functional, Non-functional, ya
Maintenance/Regression.

1.  Registered email par password reset email aati hai.
2.  1,000 concurrent users ke time login response measure karna.
3.  Bug fix ke baad product search dobara check karna.
4.  User logout button easily find kar pata hai ya nahi observe karna.
5.  Invalid email par error message check karna.
6.  Large file upload par application stable rehti hai ya nahi.

## Exercise B --- Black-box or White-box?

1.  Login form mein valid/invalid credentials enter karke output verify
    karna.
2.  Source code ke if/else branches test karna.
3.  Search input dekar matching product list verify karna.
4.  Internal loop ke execution paths inspect karna.

## Exercise C --- STLC phase identify karo

1.  Requirement document review karna.
2.  Testing tools aur schedule decide karna.
3.  Login test case likhna.
4.  Browser, server aur test data configure karna.
5.  Test cases run karna aur defect report karna.
6.  Test summary report prepare karna.

## Exercise D --- Equivalence Partitioning & BVA

Rule: Age 18--65 accepted.

1.  Valid input partition identify karo.
2.  Invalid lower partition identify karo.
3.  Invalid upper partition identify karo.
4.  Equivalence Partitioning ke representative values choose karo.
5.  BVA values `17, 18, 65, 66` ka expected result likho.

## Exercise E --- Mapping

Har test type ko course video ke STLC phase se map karo:

-   Static requirements review
-   Equivalence Partitioning
-   Boundary Value Analysis
-   Performance Testing
-   Usability Testing
-   Regression Testing

Har answer ke saath reason bhi likho.

------------------------------------------------------------------------

# 📊 MODULE 04 --- PROGRESS TRACKER

Confidence score: - 1 = Concept clear nahi. - 2 = Definition yaad,
example difficult. - 3 = Apne words mein explain kar sakta hoon. - 4 =
Real scenario mein apply kar sakta hoon. - 5 = Interview mein
confidently explain aur reason de sakta hoon.

  Topic                       Status          Confidence (1--5)
  --------------------------- ------------- -------------------
  Test Types overview         Not started                   ---
  Functional Testing          Not started                   ---
  Black-box Testing           Not started                   ---
  White-box Testing           Not started                   ---
  Non-functional Testing      Not started                   ---
  Performance Testing         Not started                   ---
  Usability Testing           Not started                   ---
  Maintenance Testing         Not started                   ---
  Regression Testing          Not started                   ---
  STLC overview               Not started                   ---
  Requirement Analysis        Not started                   ---
  Test Planning               Not started                   ---
  Test Design                 Not started                   ---
  Test Environment Setup      Not started                   ---
  Test Execution              Not started                   ---
  Test Cycle Closure          Not started                   ---
  Equivalence Partitioning    Not started                   ---
  Boundary Value Analysis     Not started                   ---
  Test Type to STLC mapping   Not started                   ---

## 🏁 Module completion standard

Module 04 tab complete maana jayega jab tum:

-   Functional, non-functional aur maintenance testing ka difference
    explain kar sako.
-   Black-box aur white-box testing ka difference example ke saath bata
    sako.
-   Performance, usability aur regression testing ke purpose explain kar
    sako.
-   STLC ki six phases correct order mein explain kar sako.
-   Har phase ka key question aur main output/result bata sako.
-   Equivalence Partitioning aur Boundary Value Analysis ka age example
    solve kar sako.
-   Course video ke test type-to-STLC mapping ko reason ke saath explain
    kar sako.
-   Regression testing ke recurring nature ko samajh sako.

> \[!TIP\] **Next learning step:** Pehle Part 1 se Part 5 tak samjho.
> Phir STLC ke six phases padho. Uske baad mapping table aur exercises
> solve karna. Hum lesson-by-lesson chalenge; ek hi din mein poora
> module ratne ki zaroorat nahi.

------------------------------------------------------------------------

## 📚 Module 04 --- Uploaded source coverage

Is guide ko banane ke liye uploaded ZIP ke ye resources use kiye gaye:

-   `1 - types of testing.txt` --- Functional, non-functional,
    maintenance testing; black-box/white-box; performance, usability,
    regression.
-   `subtitle.txt` and its detailed transcript PDF --- STLC six phases,
    phase questions, activities, test plan, test cases, environment,
    execution, closure, test summary report.
-   `subtitle (1).txt` and its detailed transcript PDF --- Test type
    mapping to STLC phases, static requirements review, equivalence
    partitioning, boundary value analysis, performance, usability,
    regression, swim-lane diagram.
-   VTT subtitle files --- Spoken-content cross-check.

**Source boundary:** Is module ke liye notes uploaded Module 4 material
par based hain. Extra examples ko mentor-created mark kiya gaya hai. Is
guide mein kisi missing assignment, solution key, ya unprovided course
material ka claim nahi kiya gaya.
