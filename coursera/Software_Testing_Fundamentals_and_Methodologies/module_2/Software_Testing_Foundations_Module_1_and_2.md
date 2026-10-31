# Software Testing Foundations --- Study Guide (Module 1 & 2)

**A practical Hinglish course for learning testing theory, understanding
web applications, and preparing for real QA/SDET work.**

-   Level: Beginner to early intermediate
-   Suggested effort: 5--7 focused study sessions
-   Main goal: Understand the reasoning behind testing, not just
    memorize definitions.
-   Learning style: Concept → example → real testing situation →
    interview explanation → practice.

------------------------------------------------------------------------

# How to use this guide

Is guide ko textbook ki tarah ek baar padhkar khatam mat karna. Har
section mein:

1.  Pehle concept samjho.
2.  Example ko apne words mein explain karo.
3.  Diye gaye scenario par apply karo.
4.  Interview answer ko ratto mat; concept samajhne ke baad apni
    language mein bolo.
5.  Practice questions solve karo.

**Important distinction:** Uploaded course resources ke concepts ko
"Course foundation" ke roop mein explain kiya gaya hai. Jahan practical
industry detail add ki gayi hai, wahan "Extra practical knowledge" likha
hai. Extra details course ke exact words ya official answer hone ka
claim nahi hain.

# Learning roadmap

  --------------------------------------------------------------------------
  Session          Topic              Difficulty                Approx. time
  ---------------- ------------------ ---------------- ---------------------
  1                Quality, QA, QC,   Easy--Medium                60--75 min
                   Testing and UAT                     

  2                RACI and           Easy--Medium                30--45 min
                   responsibilities                    
                   in a delivery team                  

  3                Seven fundamental  Medium                      75--90 min
                   testing principles                  

  4                How a web          Easy--Medium                    60 min
                   application works:                  
                   three layers                        

  5                Browser DevTools:  Medium                      60--90 min
                   tracing UI to API                   
                   and response                        

  6                Mapping tests      Medium                          60 min
                   across layers +                     
                   defect                              
                   investigation                       

  7                Revision, scenario Medium                      45--60 min
                   practice and                        
                   interview                           
                   assessment                          
  --------------------------------------------------------------------------

------------------------------------------------------------------------

# PART 1 --- Quality, QA, QC, Testing and UAT

## 1.1 First understand: What is quality?

Software quality ka simple meaning sirf "application crash nahi hoti"
nahi hai.

Quality ka matlab hai software: - Intended requirements ko satisfy
kare. - User ke real problem ko solve kare. - Expected behavior
consistently provide kare. - Important risks ko acceptable level tak
control kare. - Us context mein usable, reliable aur maintainable ho.

### Example

E-commerce website par Place Order button click karne se order create ho
raha hai. Technically button work kar raha hai.

Lekin: - Wrong total charge ho raha hai. - Duplicate orders create ho
rahe hain. - Invalid address accept ho raha hai. - User ko order
confirmation nahi mil raha.

Sirf button ka click work karna product ko quality product nahi banata.

**Remember:** Quality is about the product meeting expectations and
serving its intended purpose---not merely about having no visible crash.

## 1.2 What is Software Testing?

Software testing is the activity of evaluating software and related work
products to find defects, check expected behavior, and provide
information about quality and risk.

Simple Hinglish: Tester application ko systematically check karta hai
taaki samajh sake ki software expected requirements ke according kaam
kar raha hai ya nahi, aur kahan failure ka risk hai.

Testing ke do important purposes: 1. **Verification-oriented checks:**
Kya product specified requirements/design ke according build hua? 2.
**Validation-oriented checks:** Kya product actual user/business need
solve karta hai?

In dono ko ek beginner-friendly question se yaad rakho: - Verification:
"Are we building the product right?" - Validation: "Are we building the
right product?"

Ye short phrases helpful memory aids hain; real projects mein
verification/validation multiple activities se hoti hain.

## 1.3 QA --- Quality Assurance

### Meaning

QA is a process-oriented approach that focuses on establishing and
improving the processes, standards, and practices used to build quality
software.

Course foundation ke mutabik QA proactive hai. Iska focus defect ko sirf
end mein pakadna nahi, balki development process mein quality build
karne ke conditions create karna hai.

### QA activities

-   Requirements review karna aur ambiguity identify karna.
-   Quality standards aur team practices define karna.
-   Test strategy/approach plan karna.
-   Risks identify karna.
-   Development aur testing activities ko plan karna.
-   Process improvement aur compliance par focus karna.

### Example

Requirement: "Checkout must validate the postal code."

QA-minded team questions: - Supported country kaunsa hai? - Postal code
ka format kya hai? - Spaces allowed hain? - Empty value ka behavior kya
hoga? - Error message kya dikhna chahiye? - Valid/invalid examples
acceptance criteria mein documented hain?

Coding se pehle ambiguity clarify karne se rework aur defects ka risk
reduce hota hai.

### QA ka central question

"Are we following a suitable process to build and deliver quality?"

## 1.4 QC --- Quality Control

### Meaning

QC is product-oriented. It checks the actual product or output to
identify defects and determine whether it meets specified expectations.

Course foundation QC ko hands-on checking, test execution, output
inspection aur defect identification se connect karta hai.

### QC activities

-   Test cases execute karna.
-   Actual result ko expected result se compare karna.
-   UI, API aur data behavior check karna.
-   Defects reproduce aur report karna.
-   Fix ke baad retesting karna.

### Example

Checkout ZIP field ke liye tester: - Valid postal code enter kare. -
Alphabetic text enter kare. - Too-short value enter kare. - Too-long
value enter kare. - Blank value submit kare. - Confirm kare ki error
message understandable hai.

### QC ka central question

"Does the actual product behave as expected?"

## 1.5 QA vs QC --- Difference

  -----------------------------------------------------------------------
  Area                    QA                      QC
  ----------------------- ----------------------- -----------------------
  Focus                   Process                 Product/output

  Nature in course        Proactive               Reactive
  framing                                         

  Main goal               Defects introduce hone  Product mein defects
                          ka risk reduce karna    identify karna

  Typical activities      Standards, requirement  Test execution,
                          reviews, process,       inspection, defect
                          strategy, risk          reporting

  Main question           Quality build karne ka  Built product sahi
                          process sahi hai?       behave kar raha hai?
  -----------------------------------------------------------------------

**Common misconception:** QA aur QC dono quality ke liye hain. Inhe "QA
person vs tester" ki rigid boundary mat samjho. Organizations mein
titles aur responsibilities vary kar sakti hain; quality poori team ki
responsibility hai.

## 1.6 UAT --- User Acceptance Testing

UAT ka purpose ye validate karna hai ki software real business workflows
aur user expectations ko satisfy karta hai.

Usually UAT mein: - Business stakeholders - Product Owner - Customer
representatives - Selected end users

participate karte hain. QA/development team environment, test data aur
defect investigation mein support de sakti hai.

### Example

MindBridge learning platform mein course purchase flow:

QC tester checks: - Course cart mein add hota hai? - Checkout API
correct response deti hai? - Invalid input reject hota hai? - Order
details expected hain?

Business user/UAT checks: - Kya student course purchase karke access kar
pa raha hai? - Kya displayed course price aur actual business policy
match karte hain? - Kya end-to-end purchase workflow business ke liye
acceptable hai?

### QA, QC and UAT --- One-line memory

-   QA: Process ko quality-friendly banana.
-   QC: Product ko check karna.
-   UAT: Business/user need satisfy ho rahi hai ya nahi validate karna.

**Timing nuance:** Course video UAT ko go-live se pehle final validation
ke roop mein explain karta hai. Real projects mein UAT ka exact timing
delivery model aur release process ke hisaab se vary kar sakta hai.
Purpose aur participants ko samajhna zyada important hai.

## 1.7 Verification vs Validation

  -----------------------------------------------------------------------
  Verification                        Validation
  ----------------------------------- -----------------------------------
  Specified requirements/design ke    Actual user/business need ke
  against evaluation                  against evaluation

  "Are we building the product        "Are we building the right
  right?"                             product?"

  Reviews, inspections,               Executing software, realistic
  requirement/design checks, static   workflows, UAT
  analysis                            

  Defect early identify karne mein    Product usefulness/fitness evaluate
  help                                karne mein help
  -----------------------------------------------------------------------

Example: - Requirement says ZIP field is mandatory. Requirement review
mein confirm karna ki rule clear hai = verification-oriented activity. -
Actual customer checkout karke confirm kare ki purchase flow unki need
meet karta hai = validation-oriented activity.

## 1.8 Interview answer

**Simple English:**

"QA focuses on improving the process used to build software, while QC
focuses on checking the actual product and finding defects. UAT is
performed mainly by business stakeholders or representative users to
confirm that the product meets business needs."

**Stronger answer:**

"Quality Assurance is a proactive, process-oriented approach. It
includes activities such as reviewing requirements, defining standards,
identifying risks, and improving the development process. Quality
Control is product-oriented and evaluates the actual application through
test execution, inspection, and defect reporting. User Acceptance
Testing validates whether real business workflows and user expectations
are satisfied. These activities complement each other, and quality is a
shared responsibility across the team."

**Keywords:** Process-oriented, product-oriented, defect prevention,
defect detection, business workflow, user acceptance, quality ownership.

### Practice

1.  QA aur QC ka difference apne words mein explain karo.
2.  Kya QA coding start hone se pehle contribute kar sakta hai? Example
    do.
3.  Functional test pass hone ke baad bhi UAT fail kyun ho sakta hai?
4.  "Quality is everyone's responsibility" ka practical meaning kya hai?

------------------------------------------------------------------------

# PART 2 --- RACI and Team Responsibilities

## 2.1 RACI kya hai?

RACI ek responsibility mapping technique hai. Isse team ko clear hota
hai ki kisi task mein kaun kaam karega, final ownership kiski hai, kisse
input lena hai aur kisko update dena hai.

  Letter   Full form     Meaning
  -------- ------------- -----------------------------------------------
  R        Responsible   Task perform karta hai
  A        Accountable   Final ownership/approval leta hai
  C        Consulted     Input ya expertise deta hai
  I        Informed      Progress/result ke baare mein update hota hai

### Easy example

Task: Checkout ke acceptance criteria define karna.

-   Product Owner: A --- final business acceptance own karta hai.
-   QA Lead: R --- criteria ko testable banane mein work karta hai.
-   Developer: C --- technical feasibility par input deta hai.
-   Support team: I --- agreed behavior ke baare mein informed rehti
    hai.

Ye illustrative example hai. Actual RACI organization aur task ke
according change ho sakta hai.

## 2.2 R aur A ka difference

-   Responsible = kaam kaun karega?
-   Accountable = final outcome/approval ka owner kaun hai?

Example: Developer code implement karta hai (Responsible); engineering
lead code review process ke final ownership ke liye Accountable ho sakta
hai. Exact assignment team process par depend karta hai.

**Practical rule:** RACI ko title-based assumptions se mat bharo. Actual
task aur decision rights samajhkar fill karo.

## 2.3 Interview answer

"RACI is a responsibility assignment matrix. Responsible performs the
task, Accountable owns the final outcome, Consulted provides input, and
Informed receives updates. It helps reduce confusion and responsibility
gaps in a project."

### Practice

Checkout feature ke liye in tasks par RACI banao: 1. Acceptance criteria
define karna. 2. Code implement karna. 3. Test cases prepare karna. 4.
Tests execute karna. 5. Defect fix karna. 6. Business acceptance dena.

------------------------------------------------------------------------

# PART 3 --- Seven Fundamental Testing Principles

Ye seven principles testing decisions guide karte hain. Inka purpose
definitions yaad karwana nahi, balki limited time mein effective testing
karne ki thinking develop karna hai.

## Principle 1 --- Testing shows the presence of defects, not their absence

Testing defects reveal kar sakti hai. Passing tests prove nahi karte ki
software mein koi defect nahi hai.

### Example

100 test cases pass hue. Lekin kisi untested input par application crash
kar sakti hai.

Checkout: - `94105` pass hua. - Isse ye prove nahi hota ki `testing`,
blank, ya unusually long input bhi correct handle hoga.

**Tester mindset:** "What have I tested, and what remains untested?"

## Principle 2 --- Exhaustive testing is impossible

Har possible input, state, browser, device, user action aur combination
test karna usually practical nahi hota.

### Example

Shopping app mein: - Multiple payment methods - Shipping options -
Discount codes - User account states - Browsers/devices

In sab combinations ko test karna bahut expensive ho sakta hai.

### What should tester do?

Risk-based prioritization: - Failure hone ki possibility. - Failure ka
business/user impact. - Feature kitni frequently use hota hai. - Change
kitna complex hai. - Historical defects.

Simple thought model:

`Testing priority increases when likelihood or impact of failure increases.`

Ye conceptual guide hai, universal numeric formula nahi.

## Principle 3 --- Early testing saves time and cost

Testing mindset requirements aur design phase se start hota hai. Code
complete hone ka wait karna zaroori nahi.

### Example

Requirement: "Postal code should be validated."

Questions: - Which country format? - Length? - Alphanumeric allowed? -
Spaces/hyphens? - Error message? - Empty input?

Agar ambiguity requirements stage par resolve ho jaye, to later
implementation rework reduce ho sakta hai.

## Principle 4 --- Defect clustering

Defects aksar kuch specific components/modules mein zyada concentrate ho
sakte hain.

### Example

Application ke 8 modules hain. Historical defects mein cart aur checkout
modules se disproportionate issues aa rahe hain. Next release mein un
modules ko extra regression attention dena sensible hai.

**Important:** Defect clustering ek tendency/observation hai, guarantee
nahi. Historical data guide karta hai; tester ko naye risks bhi assess
karne chahiye.

## Principle 5 --- Pesticide paradox

Same test cases baar-baar run karne se eventually naye defects milna kam
ho sakta hai. Test suite ko review aur refresh karna chahiye.

### Example

Har release mein sirf same valid ZIP `94105` test karna enough nahi.

Add/rotate: - Alphabetic values - Too-short values - Too-long values -
Special characters - Empty values - Leading/trailing spaces - Boundary
values

Automation suite stable ho sakti hai, lekin test coverage ko evolve
karte rehna chahiye.

## Principle 6 --- Testing is context-dependent

Testing approach product ke purpose, risk, users, technology aur
regulatory needs par depend karti hai.

### Example

Medical device software aur internal leave-management portal ke risk
same nahi hote. Medical software mein safety and regulatory risks ki
wajah se deeper evidence and controls required ho sakte hain.

**Tester mindset:** "What can go wrong in this specific product, and how
serious would it be?"

## Principle 7 --- Absence-of-errors fallacy

Software mein defects na milna ya tests pass hona guarantee nahi karta
ki product user ki actual need satisfy karta hai.

### Example

Ride booking app fare calculate kar rahi hai. All test cases pass hue
because tests followed written requirements. Lekin peak-hour surge
pricing ka business rule requirement mein missing tha. Real users ko
incorrect fare mila.

Issue incomplete requirement/business understanding ka tha.

## 3.8 Seven principles --- revision table

  ------------------------------------------------------------------------
                            \# Principle             Memory line
  ---------------------------- --------------------- ---------------------
                             1 Presence of defects   Testing defects show
                                                     karti hai, absence
                                                     prove nahi

                             2 Exhaustive testing    Prioritize based on
                               impossible            risk

                             3 Early testing         Requirements se
                                                     testing start

                             4 Defect clustering     Defects kuch areas
                                                     mein concentrate ho
                                                     sakte hain

                             5 Pesticide paradox     Same tests ko refresh
                                                     karo

                             6 Context-dependent     Approach product/risk
                               testing               ke hisaab se

                             7 Absence-of-errors     Passing tests ≠ user
                               fallacy               satisfaction
  ------------------------------------------------------------------------

## 3.9 Interview answer

"The seven testing principles guide effective testing. Testing can show
the presence of defects but cannot prove their absence. Exhaustive
testing is impossible, so we prioritize based on risk. Testing should
start early. Defects may cluster in certain areas. Repeating the same
tests can become less effective, so test cases should be reviewed and
varied. Testing depends on context, and passing tests do not guarantee
that the software meets user needs."

### Practice

1.  100% test cases pass hue---kya conclude kar sakte ho?
2.  Risk-based testing ka example do.
3.  Requirement review early testing ka example kaise hai?
4.  Pesticide paradox ko automation regression suite se explain karo.
5.  Defect clustering ke basis par testing effort kaise allocate karoge?
6.  Test suite pass ho, lekin customer unhappy ho---kaunsa principle
    apply hota hai?

------------------------------------------------------------------------

# PART 4 --- How a Web Application Works: Three Layers

Web application ko test karne ke liye sirf screen par kya dikh raha hai
ye samajhna enough nahi. Ek user action ke peeche frontend, backend/API
aur database interact kar sakte hain.

Course foundation three-layer model use karta hai:

1.  Presentation Layer
2.  Application Layer
3.  Data Layer

## 4.1 Presentation Layer --- What user sees

Presentation layer browser mein visible/interactable part hai: -
Buttons - Text - Images - Forms - Menus - Tables - Product cards

Main responsibilities: - Information display karna. - User input capture
karna. - User action ke response ko show karna.

### Example

Login page par: - Email field - Password field - Sign in button -
Validation message

Ye presentation/UI layer ka part hai.

### Tester kya check karega?

-   Button visible/enabled hai?
-   Labels correct hain?
-   Input accept ho raha hai?
-   Error message meaningful hai?
-   Layout responsive hai?
-   User action ke baad correct UI state show hoti hai?

## 4.2 Application Layer --- Business logic / backend

Application layer user request receive karke business rules apply karti
hai.

Example: - Login credentials validate karna. - Product availability
check karna. - Cart total calculate karna. - Discount apply karna. -
Checkout request process karna. - Authorization check karna.

Frontend backend ko API request bhej sakta hai. Backend response return
karta hai.

### Tester kya check karega?

-   Correct API endpoint call hua?
-   HTTP method correct hai?
-   Request payload correct hai?
-   Response status/body correct hai?
-   Business rules apply hue?
-   Invalid input par correct error response aaya?

## 4.3 Data Layer --- Persistent storage

Data layer usually database ya persistent storage hota hai. Iska kaam
data store aur retrieve karna hai.

Examples: - User profile - Course catalogue - Cart items - Orders -
Payment records

### Tester kya check karega?

-   Correct data save hua?
-   Duplicate record create to nahi hua?
-   Update correct record par apply hua?
-   Read operation expected data return karti hai?
-   Failed transaction ke baad inconsistent data to nahi?

Database testing ka depth project access, architecture aur risk par
depend karta hai. UI tester ko har project mein direct database access
ho, ye guaranteed nahi.

## 4.4 Three layers --- complete flow

Example: User profile address update karta hai.

``` text
USER clicks Save
       |
       v
PRESENTATION LAYER
Captures address and user action
       |
       v
HTTP/API REQUEST
       |
       v
APPLICATION LAYER
Receives request, validates business rules
       |
       v
DATA LAYER
Updates user's address record
       |
       v
APPLICATION LAYER
Receives save result and prepares response
       |
       v
PRESENTATION LAYER
Shows success or error message
       |
       v
USER sees result
```

### Restaurant analogy

-   Presentation = dining area/menu where customer interacts.
-   Application = waiter/manager who processes the order and applies
    rules.
-   Data = kitchen/store records where ingredients/orders are stored.

Analogy concept samjhane ke liye hai; real web architecture mein
components isse zyada complex ho sakte hain.

## 4.5 One action, three perspectives --- Add to cart

User Add to Cart click karta hai:

  -----------------------------------------------------------------------
  Layer                               What happens
  ----------------------------------- -----------------------------------
  Presentation                        Button click, cart count update

  Application                         POST request receive,
                                      item/availability/business rules
                                      process

  Data                                Cart item persist ho sakta hai

  Response path                       Backend result frontend ko return
                                      karta hai; UI update hoti hai
  -----------------------------------------------------------------------

Agar cart count update nahi hua, root cause UI event, network request,
backend logic, ya data operation mein ho sakta hai. Evidence collect
kiye bina assume mat karo ki issue frontend ka hi hai.

## 4.6 Interview answer

"A typical web application can be understood through three layers. The
presentation layer displays the UI and captures user actions. The
application layer processes requests and applies business logic, often
through APIs. The data layer stores and retrieves information, usually
from a database. When a user performs an action, data flows between
these layers and the response is returned to the UI."

------------------------------------------------------------------------

# PART 5 --- Browser Developer Tools: Trace UI to Backend

Browser DevTools tester ke liye important investigation tool hai. Isse
hum dekh sakte hain ki UI action ke baad browser ne kaunsi network
request bheji aur server ne kya response diya.

## 5.1 DevTools kaise open karein?

Chrome mein: - `F12` - or `Ctrl + Shift + I` - Right-click an element →
Inspect

Important tabs: - Elements - Console - Network - Application - Sources

Is lesson mein main focus Elements aur Network par hai.

## 5.2 Elements tab --- Presentation layer inspect karna

Elements tab rendered HTML/DOM inspect karne mein help karta hai.

Example:

``` html
<button type="submit" class="btn btn-primary">
  Sign in
</button>
```

Tester dekh sakta hai: - Element ka tag `button` hai. - `type` attribute
`submit` hai. - `class` attribute `btn btn-primary` hai. - Visible text
`Sign in` hai.

**Important:** CSS class dekhna useful ho sakta hai, lekin automation
locator ke liye class hamesha best choice nahi. Stable accessible
role/name/label often better hota hai.

## 5.3 Network tab --- Application/API layer inspect karna

Steps: 1. DevTools open karo. 2. Network tab select karo. 3. Fetch/XHR
filter select karo. 4. Agar needed ho to Preserve log enable karo. 5.
Existing requests clear karo. 6. Application mein action perform karo.
7. New request select karo. 8. Headers, Payload, Preview/Response aur
Status inspect karo.

### Request mein kya dekhna hai?

  Field             Meaning
  ----------------- ---------------------------------------
  Request URL       Request kis endpoint par gayi
  Request Method    GET, POST, PUT, PATCH, DELETE etc.
  Status Code       Server/network response status
  Request Payload   Client ne kya data bheja
  Response          Server ne kya return kiya
  Timing            Request/response mein kitna time laga

### Example

``` http
GET /api/courses
```

Meaning: Browser courses data request kar raha hai.

Possible response:

``` json
[
  {
    "id": 1,
    "title": "Python Basics",
    "level": "Beginner"
  }
]
```

Frontend is data ko course cards mein display kar sakta hai.

## 5.4 Common HTTP methods --- tester perspective

  Method   Common purpose                  Example
  -------- ------------------------------- ----------------------------
  GET      Data read/retrieve              `GET /api/courses`
  POST     Resource create/action submit   `POST /api/cart/items`
  PUT      Resource replace/update         `PUT /api/users/12`
  PATCH    Partial update                  `PATCH /api/users/12`
  DELETE   Resource delete                 `DELETE /api/cart/items/5`

Ye common REST conventions hain. Actual API design project ke according
vary kar sakta hai.

## 5.5 Common HTTP status codes

  ------------------------------------------------------------------------
                        Status General meaning       Example
                                                     interpretation
  ---------------------------- --------------------- ---------------------
                           200 OK                    Request successful

                           201 Created               Resource created

                           204 No Content            Successful response
                                                     with no response body

                           400 Bad Request           Request
                                                     invalid/malformed or
                                                     rejected

                           401 Unauthorized          Authentication
                                                     missing/invalid

                           403 Forbidden             User not allowed

                           404 Not Found             Resource/endpoint not
                                                     found

                           409 Conflict              Conflict with current
                                                     resource state

                           422 Unprocessable Content Request understood
                                                     but
                                                     validation/semantic
                                                     issue

                           500 Internal Server Error Server encountered an
                                                     unexpected condition
  ------------------------------------------------------------------------

**Critical testing note:** Status code ko akela dekhkar final conclusion
mat nikalo. Response body, request, product requirement aur server
behavior bhi inspect karo. For example, 400/422 validation behavior
application design ke hisaab se differ kar sakta hai.

## 5.6 Network request ko detail mein inspect karna

Request select karne ke baad:

-   **Headers:** URL, method, status, request/response headers.
-   **Payload:** POST/PUT/PATCH request mein bheja gaya data.
-   **Preview/Response:** Server response.
-   **Timing:** Request processing/network timing.

### Example: Login

User email/password enter karta hai.

Possible request:

``` http
POST /api/login
Content-Type: application/json
```

Payload:

``` json
{
  "email": "user@example.com",
  "password": "example-password"
}
```

Possible response:

``` json
{
  "access": "token-value",
  "user_id": 42
}
```

Ye illustrative example hai, kisi actual system ka captured response
nahi.

Security reminder: Real credentials, access tokens, cookies, personal
data ya payment information screenshots/logs mein share mat karo.
Evidence attach karne se pehle sensitive values redact karo.

## 5.7 UI error vs backend failure --- difference investigate karo

Suppose page par "Something went wrong" toast aata hai.

Possible causes: - Frontend JavaScript error. - Request send hi nahi
hui. - API ne 400/401/403/404 return kiya. - Backend ne 500 return
kiya. - Request timeout/network failure. - Backend response successful
tha, lekin frontend ne response incorrectly render kiya.

Tester ka kaam evidence collect karna hai: 1. Console mein error? 2.
Network request bani? 3. Request URL/method correct? 4. Status code kya
hai? 5. Response body kya hai? 6. UI ne response ko correctly handle
kiya?

**Don't jump to "backend bug" just because UI toast appears.** Network
evidence aur reproduction se root cause narrow down karo.

## 5.8 404 and 500 ka difference

-   404 generally means requested resource/route was not found.
-   500 means server encountered an unexpected internal error while
    processing the request.

Course transcript mein ek example 404 endpoint/routing issue dikhata
hai. MindBridge lab mein special-character payment input se POST
checkout request 500 return karti hai.

Ye dono different failure examples hain---unhe mix mat karna.

------------------------------------------------------------------------

# PART 6 --- Mapping Tests Across Web Layers

Ab theory ko real tester workflow mein convert karte hain.

## 6.1 Course lab ka purpose

MindBridge lab ka objective user actions ko Presentation, Application
aur Data layers ke across trace karna hai.

Lab ke six actions:

1.  Load catalogue.
2.  View one course.
3.  Filter by level.
4.  Search by title.
5.  Add course to cart.
6.  Submit payment with a specific special character in card number.

## 6.2 Mapping table

  -----------------------------------------------------------------------------------------
  User action       Presentation      Application/API                     Data layer
  ----------------- ----------------- ----------------------------------- -----------------
  Load catalogue    Course grid       `GET /api/courses`                  Courses rows read
                    appears                                               

  View one course   Course detail     `GET /api/courses/{id}`             One course row
                    page                                                  read

  Filter by level   Filtered grid     `GET /api/courses?level=beginner`   Matching rows
                                                                          read

  Search by title   Search results    `GET /api/courses?search=python`    Matching rows
                                                                          read

  Add to cart       Cart count        `POST /api/cart/items`              Cart line written
                    increases                                             after course
                                                                          check

  Submit payment    Error message     `POST /api/checkout` returns 500    Lab says data
  with `$` in card                                                        layer is not
  number                                                                  reached
  -----------------------------------------------------------------------------------------

Ye table lab instructions aur supplied mapping template ke expected
observations summarize karti hai.

## 6.3 Payment special-character defect

Lab instructions ke mutabik: - Card number ke prefilled value mein `$`
add karo. - Place Order select karo. - Order complete nahi hota; error
message appear hota hai. - Network mein `POST /api/checkout` status
`500` aata hai. - Lab ke expected finding ke mutabik failure Application
layer par hota hai; Data layer reach nahi hoti.

Important detail: Lab specifically `$` (ya `<`, `>`, `&`, `(`, `)`) ko
seeded crash input batata hai. Instructions ke mutabik `@` aur `#` is
seeded crash ko trigger nahi karte aur order create ho sakta hai.

**Do not generalize:** "All special characters fail" is not what the lab
says. Specific test data matters.

## 6.4 Tester ka conclusion kaise likhna hai?

Weak conclusion: "Payment page is broken."

Better evidence-based observation: "When the card-number field contains
the seeded special character `$`, submitting checkout triggers
`POST /api/checkout`, which returns HTTP 500. The UI displays a generic
error message. Based on the lab's expected mapping, the request fails in
the application layer before data-layer access."

Is conclusion mein: - Action clear hai. - Input clear hai. - Endpoint
clear hai. - Status code clear hai. - UI symptom clear hai. -
Layer-level interpretation clear hai.

## 6.5 Layer-based testing matrix --- extra practical knowledge

  -----------------------------------------------------------------------
  Layer                   Example test ideas      Useful evidence
  ----------------------- ----------------------- -----------------------
  Presentation            Labels, validation      Screenshot, DOM,
                          messages, button state, browser behavior
                          layout, accessibility   

  Application             API method/path,        Network
                          request body, response, request/response, API
                          business rules, auth    test result

  Data                    Record created/updated, DB query/logs,
                          no duplicate, correct   authorized test data
                          relationship            inspection
  -----------------------------------------------------------------------

Data-layer access har tester ko available nahi hota. Access na ho to API
response, UI state, audit logs ya developer-provided test evidence se
verification kar sakte ho---lekin database write ko verified claim mat
karo jab tak evidence na ho.

## 6.6 Interview answer

"When I investigate a web application issue, I trace the user action
across the presentation, application, and data layers. I first observe
the UI behavior, then inspect the Network tab to identify the request
method, endpoint, payload, status code, and response. If authorized data
access is available, I also verify whether the expected data was read or
written. This helps me narrow down the failing layer instead of assuming
every visible issue is a UI defect."

------------------------------------------------------------------------

# PART 7 --- Practical exercises

## Exercise 1: QA, QC or UAT?

Har activity ko QA, QC ya UAT perspective se classify karo. Kuch
activities team ke context ke hisaab se overlap kar sakti hain; apni
reasoning likhna.

1.  Requirement ambiguity review karna.
2.  Login test cases execute karna.
3.  Business user confirm karta hai ki invoice workflow business need
    meet karta hai.
4.  Team-wide code review standard define karna.
5.  Checkout API ka response inspect karna.
6.  Product Owner final business acceptance deta hai.

## Exercise 2: Seven principles

Checkout feature ke context mein: 1. Har possible ZIP input test kyun
nahi kar sakte? 2. Kaunse 5 test inputs choose karoge aur kyun? 3. Same
test suite ko next release mein kaise improve karoge? 4. Kaunsi
requirement ambiguity testing start hone se pehle resolve karni chahiye?

## Exercise 3: Three layers

Login flow ke liye identify karo: - Presentation layer components. -
Application layer responsibility. - Data layer responsibility. - Invalid
password par expected UI behavior. - Network tab mein kya evidence
inspect karoge?

## Exercise 4: DevTools investigation

Scenario: Catalog page blank hai.

Investigation plan likho: 1. Elements tab mein kya inspect karoge? 2.
Console mein kya dekhoge? 3. Network Fetch/XHR mein kya filter karoge?
4. `GET /api/courses` ka status 200 ho to next kya inspect karoge? 5.
Request 404 ho to kya evidence record karoge? 6. Response 200 ho lekin
UI blank ho to frontend mapping/rendering issue kaise investigate
karoge?

## Exercise 5: MindBridge layer mapping

Six lab actions ki mapping table apne words mein banao: - User action -
Presentation observation - API method and path - Status - Data-layer
interpretation

Agar tum lab app execute nahi kar sakte, supplied lab observations ko
source-described result ke roop mein use karo. Apne observed result ka
false claim mat karo.

------------------------------------------------------------------------

# PART 8 --- Interview Revision Sheet

## Must-know definitions

**Software Testing:** Evaluating software to find defects, check
expected behavior and provide information about quality and risk.

**QA:** Process-oriented approach to establish/improve practices that
support quality.

**QC:** Product-oriented checking to identify defects in the actual
product.

**UAT:** Business/user validation that the product supports expected
workflows and needs.

**RACI:** Responsibility matrix: Responsible, Accountable, Consulted,
Informed.

**Risk-based testing:** Prioritizing testing based on likelihood and
impact of failure.

**Defect clustering:** Defects may be concentrated in certain
components.

**Pesticide paradox:** Repeating the same tests may stop revealing new
defects; test suites need refresh.

**Presentation layer:** UI that displays information and captures user
actions.

**Application layer:** Business logic that processes requests.

**Data layer:** Persistent storage and retrieval.

**Network tab:** Browser DevTools area to inspect browser-server
requests and responses.

## 10 interview questions

1.  What is the difference between QA and QC?
2.  What is UAT and who performs it?
3.  Explain verification vs validation.
4.  What is RACI?
5.  Explain the seven testing principles.
6.  What is risk-based testing?
7.  Explain the three layers of a web application.
8.  How do you inspect an API request in Chrome DevTools?
9.  What is the difference between HTTP 404 and 500?
10. How do you investigate a UI error that may originate from the
    backend?

## Strong answer structure

Interview answer dete waqt: 1. Definition do. 2. Difference/important
points explain karo. 3. One practical example do. 4. Tester perspective
se why it matters batao.

Example: "I use the Network tab not only to see the status code, but
also to inspect the request URL, method, payload and response. This
helps me distinguish a UI rendering issue from an API or server-side
failure."

------------------------------------------------------------------------

# PART 9 --- Progress tracker

  Topic                           Status          Confidence 1--5
  ------------------------------- ------------- -----------------
  Software quality and testing    Not started                 ---
  QA vs QC                        Not started                 ---
  UAT                             Not started                 ---
  Verification vs validation      Not started                 ---
  RACI                            Not started                 ---
  Seven testing principles        Not started                 ---
  Presentation layer              Not started                 ---
  Application layer               Not started                 ---
  Data layer                      Not started                 ---
  Elements tab                    Not started                 ---
  Network tab                     Not started                 ---
  HTTP methods and status codes   Not started                 ---
  MindBridge layer mapping        Not started                 ---
  Interview revision              Not started                 ---

Confidence score: - 1 = Definition bhi clear nahi. - 2 = Definition yaad
hai, example mein difficulty. - 3 = Apne words mein explain kar sakta
hoon. - 4 = Scenario par apply kar sakta hoon. - 5 = Interview mein
confidently explain aur practical investigation kar sakta hoon.

# Final mentor assessment

Module tab complete maana jayega jab tum:

-   QA, QC, UAT aur verification/validation ko examples ke saath explain
    kar sako.
-   Seven testing principles ko real feature par apply kar sako.
-   Web application ke three layers ka flow draw/explain kar sako.
-   DevTools Network tab mein method, URL, status, payload aur response
    inspect kar sako.
-   UI symptom dekhkar bina evidence ke frontend/backend blame na karo.
-   MindBridge ke six actions ki layer mapping explain kar sako.
-   `$` payment test ke 500 result ko accurately describe kar sako.

**Next learning step:** Is guide ka Session 1 padho. Uske baad apne
words mein QA vs QC vs UAT explain karo. Main mentor ki tarah answer
review karunga, gaps point out karunga, follow-up scenario dunga, aur
mastery ke baad next session par le jaunga.
