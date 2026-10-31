# 🌈 SOFTWARE TESTING FOUNDATIONS

## Complete Learning Guide --- Modules 1, 2 & 3

> **Tumhara personal QA learning course**\
> Hinglish explanations • Real-world examples • English definitions •
> Interview preparation • Practical thinking

🟣 **UNDERSTAND** → 🔵 **APPLY** → 🟢 **EXPLAIN** → 🟠 **PRACTICE**

------------------------------------------------------------------------

## 👋 Is guide ko kaise padhna hai?

Is baar learning ka order tumhari understanding ke according rakha hai:

1.  **Pehle Hinglish mein samjho:** Ye concept kya hai aur real life
    mein kyun use hota hai?
2.  **Real-world example dekho:** Concept ko kisi app, shopping website,
    banking app ya MindBridge feature se connect karo.
3.  **English definition padho:** Ab jab meaning clear hai, technical
    definition easily samajh aayegi.
4.  **Testing example dekho:** QA tester is concept ko actual project
    mein kaise apply karega?
5.  **Interview answer practice karo:** Apne words mein answer bolne ki
    practice karo.
6.  **Exercise solve karo:** Sirf padhne se mastery nahi aati.

> [!IMPORTANT] **Learning rule:** English definition sabse pehle ratni
> nahi hai. Pehle concept apni language mein samjho, phir English
> terminology aur definition naturally yaad hogi.

### Difficulty aur time ka meaning

-   🟢 Easy --- basic concept; examples se samajh aana chahiye.
-   🟡 Medium --- concept ko scenario mein apply karna hoga.
-   🔴 Hard --- multiple concepts ko connect karke reasoning karni hogi.

Time estimates mentor ke study estimates hain, Coursera ke official
durations nahi.

## 🧭 Learning roadmap

  ----------------------------------------------------------------------------
  Module              Main topics                          Expected outcome
  ------------------- ------------------------------------ -------------------
  **01 --- Testing    Quality, QA, QC, UAT, RACI, seven    Tester mindset aur
  Foundations**       principles, bug report               quality
                                                           fundamentals

  **02 --- Web        Presentation, application, data      UI action ke peeche
  Application         layers; browser DevTools;            kya hota hai
  Architecture**      request/response tracing             samajhna

  **03 --- Testing    Static vs dynamic testing,           Kya test karna hai,
  Approaches &        shift-left,                          kab aur kis scope
  Levels**            unit/integration/system/acceptance   par
                      testing                              

  **04 --- Next       Start only after this guide's        Module-by-module
  module**            revision and your confirmation       progression
  ----------------------------------------------------------------------------

------------------------------------------------------------------------

# 🟣 MODULE 01 --- TESTING FOUNDATIONS

## 1. Software Quality --- Quality ka matlab kya hai?

### Pehle apni language mein samjho

Maan lo tumne ek food delivery app banayi. App open ho rahi hai, buttons
click ho rahe hain aur koi crash bhi nahi aa raha.

Lekin: - Restaurant ka price ₹200 hai, checkout par ₹250 charge ho raha
hai. - Order place hone ke baad restaurant ko order nahi milta. - User
ko payment successful dikhta hai, lekin payment actually fail ho gayi. -
App slow hai aur user order complete nahi kar pa raha.

Kya hum kahenge ki app achhi quality ki hai? Nahi.

Quality ka matlab sirf application ka crash na hona nahi. Software ko
apna intended kaam sahi karna chahiye, user ki need satisfy karni
chahiye aur expected behavior consistently dena chahiye.

### English definition

**Software Quality:** The degree to which a software product satisfies
stated and implied requirements, meets user needs, and performs
effectively in its intended context.

### Tester ke perspective se

Tester ye questions poochta hai: - Kya feature requirement ke according
kaam kar raha hai? - Kya user apna task complete kar sakta hai? - Kya
incorrect input safely handle hota hai? - Kya important business data
correct hai? - Kya failure ka impact acceptable hai?

> [!TIP] **Yaad rakho:** "No crash" ka matlab "good quality" nahi
> hota.

------------------------------------------------------------------------

## 2. Software Testing --- Testing kya hoti hai?

### Pehle apni language mein samjho

Maan lo Amazon jaisi website par tum ek mobile phone buy kar rahe ho.

Tum: 1. Product search karte ho. 2. Product details open karte ho. 3.
Cart mein add karte ho. 4. Address enter karte ho. 5. Payment karte ho.
6. Order confirmation check karte ho.

Tester bhi application ke flows ko systematically check karta hai. Lekin
tester sirf normal user ki tarah use nahi karta. Wo jaan-bujhkar
different inputs, unexpected actions aur edge cases try karta hai, taaki
failures identify kar sake.

### English definition

**Software Testing:** The process of evaluating software and related
work products to identify defects, verify expected behavior, and provide
information about product quality and risk.

### Testing ke do important perspectives

-   **Verification:** Kya hum product ko specified requirements ke
    according build kar rahe hain?
-   **Validation:** Kya hum wahi product build kar rahe hain jo
    user/business ko actually chahiye?

  -----------------------------------------------------------------------
  Perspective             Simple question         Example
  ----------------------- ----------------------- -----------------------
  Verification            Are we building the     Requirement review:
                          product right?          password rule clearly
                                                  defined hai?

  Validation              Are we building the     Business user confirms
                          right product?          registration workflow
                                                  actually meets the need
  -----------------------------------------------------------------------

### Interview answer

"Software testing is the process of evaluating an application to
identify defects, verify expected behavior, and assess quality and risk.
It helps the team understand whether the software meets its requirements
and user expectations."

🟢 **Difficulty:** Easy \| ⏱️ 20--30 minutes

------------------------------------------------------------------------

## 3. QA --- Quality Assurance

### Pehle apni language mein samjho

Socho ek construction company building bana rahi hai.

Agar architect ka plan hi incomplete hai, material standards define nahi
hain aur workers ko instructions clear nahi hain, to building banne ke
baad defects milne ke chances badh jayenge.

Isliye construction start hone se pehle: - Plan review hota hai. -
Quality standards decide hote hain. - Safety rules define hote hain. -
Responsibilities clear hoti hain.

Software development mein QA ka approach bhi aisa hi hai. QA ka focus
process ko improve karna hai, taaki defects introduce hone ka risk kam
ho.

### Software example

Team checkout feature bana rahi hai. QA activities: - Requirement review
karna. - Ambiguous acceptance criteria identify karna. - Test strategy
plan karna. - Quality standards aur process define karna. - Risks
identify karna. - Ensure karna ki team agreed process follow kare.

### English definition

**Quality Assurance (QA):** A process-oriented set of activities focused
on establishing and improving the processes and standards used to
develop and deliver quality software.

### QA ka main question

"Are we following a suitable process to build quality software?"

> [!NOTE] Course framing QA ko proactive aur process-oriented batata
> hai. Iska matlab QA sirf final testing phase mein nahi, SDLC ke across
> contribute kar sakta hai.

------------------------------------------------------------------------

## 4. QC --- Quality Control

### Pehle apni language mein samjho

Building banne ke baad inspector check karta hai: - Doors properly open
ho rahe hain? - Wiring safe hai? - Water supply work kar rahi hai? -
Construction approved plan ke according hai?

Software mein QC actual application ko check karta hai.

Checkout example: - Valid postal code accept ho raha hai? - Invalid
postal code reject ho raha hai? - Total amount correct hai? - Place
Order click karne par order create hota hai? - Error message correct
hai?

### English definition

**Quality Control (QC):** A product-oriented set of activities that
evaluates the actual software product to identify defects and check
whether it meets specified requirements.

### QC ka main question

"Does the actual product behave as expected?"

### QA vs QC

  -----------------------------------------------------------------------
  Point                   QA                      QC
  ----------------------- ----------------------- -----------------------
  Focus                   Process                 Product

  Course framing          Proactive               Reactive

  Goal                    Defect introduction ka  Existing defects
                          risk reduce karna       identify karna

  Examples                Requirement review,     Test execution,
                          standards, strategy     inspection, defect
                                                  report

  Main question           Process suitable hai?   Product correct behave
                                                  kar raha hai?
  -----------------------------------------------------------------------

### Important real-world nuance

QA aur QC ko rigid job-title boundary mat samajhna. Companies mein QA
Engineer, SDET, Test Engineer, Quality Engineer jaise titles aur
responsibilities vary kar sakte hain. Quality poori team ki
responsibility hai.

### English interview answer

"Quality Assurance focuses on improving the process used to build
software, while Quality Control focuses on evaluating the actual product
and identifying defects. QA is process-oriented, whereas QC is
product-oriented. Both contribute to software quality."

🟢 **Difficulty:** Easy \| ⏱️ 25--35 minutes

------------------------------------------------------------------------

## 5. UAT --- User Acceptance Testing

### Pehle apni language mein samjho

Maan lo ek company ne apne employees ke liye leave management software
banwaya.

QA team check karti hai: - Leave request submit ho rahi hai? - Manager
approve/reject kar sakta hai? - API correct response de rahi hai? -
Leave balance update ho raha hai?

Lekin HR team ko ye bhi check karna hai: - Kya leave approval ka actual
business process support hota hai? - Kya policy ke according leave
balance calculate ho raha hai? - Kya HR team apna daily work complete
kar pa rahi hai?

Ye business/user perspective se acceptance validate karna hai.

### English definition

**User Acceptance Testing (UAT):** A level of testing in which business
stakeholders or representative end users validate whether the software
supports real business workflows and meets their acceptance needs.

### UAT kaun karta hai?

Usually: - Business stakeholders - Product Owner - Customer
representatives - Selected end users

QA/development team test environment, test data aur defect investigation
mein support kar sakti hai.

### UAT ka main question

"Does this product meet the business need and provide the expected
value?"

> [!WARNING] Course video UAT ko go-live se pehle final validation ke
> roop mein present karta hai. Real projects mein UAT ka exact timing
> process aur release model ke hisaab se vary kar sakta hai. UAT ka
> purpose aur participants samajhna zyada important hai.

### QA, QC, UAT --- quick memory

-   QA = Process ko quality-friendly banana.
-   QC = Actual product ko check karna.
-   UAT = Business/user need satisfy ho rahi hai ya nahi validate karna.

------------------------------------------------------------------------

## 6. RACI Matrix --- Team mein responsibility kaise clear hoti hai?

### Pehle apni language mein samjho

Ek project mein 5 log kaam kar rahe hain. Bug milta hai. Sab ek doosre
se pooch rahe hain: - Isko fix kaun karega? - Final approval kaun
dega? - Kis se advice leni hai? - Kisko update dena hai?

Agar responsibility clear nahi hai, kaam delay ho sakta hai. RACI is
confusion ko reduce karne ke liye use hota hai.

### English definition

**RACI Matrix:** A responsibility assignment matrix that identifies who
is Responsible, Accountable, Consulted, and Informed for each task or
decision.

  Letter   Meaning       Simple language
  -------- ------------- --------------------------------------
  **R**    Responsible   Jo actual kaam karta hai
  **A**    Accountable   Jo final ownership/approval leta hai
  **C**    Consulted     Jis se input/advice li jati hai
  **I**    Informed      Jise progress/update diya jata hai

### Example --- Checkout feature

  Task                         Product Owner   QA Lead   Developer   Tester
  ---------------------------- --------------- --------- ----------- --------
  Acceptance criteria define   A               R         C           C
  Feature implement            I               C         R/A\*       I
  Test cases prepare           I               A         C           R
  Tests execute                I               A         I           R
  Business acceptance          A/R             C         I           C

`*` Illustrative example: actual accountability organization ke process
par depend karegi. Ye table course ka official answer nahi,
mentor-created example hai.

### R vs A ka difference

-   Responsible: "Kaam kaun karega?"
-   Accountable: "Final outcome ka owner kaun hai?"

### Interview answer

"RACI is a responsibility assignment matrix. Responsible performs the
task, Accountable owns the final outcome, Consulted provides input, and
Informed receives updates. It helps teams avoid unclear ownership and
communication gaps."

🟡 **Difficulty:** Easy--Medium \| ⏱️ 30--40 minutes

------------------------------------------------------------------------

## 7. Seven Fundamental Testing Principles

Ye principles tester ko decide karne mein help karte hain ki testing
kaise plan aur prioritize karni hai.

### Principle 1 --- Testing shows the presence of defects, not their absence

**Pehle samjho:** Tumne 100 test cases run kiye aur sab pass hue. Kya
application bug-free prove ho gayi? Nahi. Tumne bas ye establish kiya ki
un tested scenarios mein defect detect nahi hua.

**English definition:** Testing can reveal the presence of defects, but
it cannot prove that no defects exist.

**Example:** Valid ZIP `94105` pass ho gaya. Lekin alphabetic, blank ya
too-long input abhi test nahi hua.

**Interview line:** "Passing tests provide confidence about tested
scenarios, not proof that the software is defect-free."

### Principle 2 --- Exhaustive testing is impossible

**Pehle samjho:** E-commerce app mein millions of possible combinations
ho sakte hain: products, payment methods, addresses, discounts,
browsers, devices. Har combination test karna practical nahi.

**English definition:** Testing every possible input, condition, and
combination is generally impractical; therefore, testing must be
prioritized.

**Example:** High-risk checkout flow aur payment scenarios ko priority
do.

**Extra practical knowledge --- Risk-based thinking:** Failure ki
likelihood aur impact ko dekhkar testing effort prioritize karo. Ye ek
reasoning model hai, fixed universal formula nahi.

### Principle 3 --- Early testing

**Pehle samjho:** Requirement mein likha hai "password should be
secure." Lekin minimum length, special characters aur validation
behavior clear nahi. Agar ye confusion coding ke baad pata chali, rework
badh sakta hai.

**English definition:** Testing activities should begin as early as
possible in the software development lifecycle so that defects can be
identified sooner.

**Example:** Development se pehle requirements review karna.

### Principle 4 --- Defect clustering

**Pehle samjho:** Agar baar-baar checkout module mein defects mil rahe
hain, to next release mein checkout par extra testing effort dena
sensible hai.

**English definition:** A relatively small number of modules may contain
a large proportion of the defects discovered.

**Example:** Historical defect data show karta hai ki cart aur checkout
mein repeated issues hain.

### Principle 5 --- Pesticide paradox

**Pehle samjho:** Agar tum har release mein sirf same 10 test cases run
karoge, to naye type ke defects miss ho sakte hain. Test data aur
scenarios refresh karte raho.

**English definition:** Repeating the same tests over time may become
less effective at finding new defects; test cases and data should be
reviewed and varied.

**Example:** ZIP tests mein valid, alphabetic, blank, too-short,
too-long aur special-character inputs add karo.

### Principle 6 --- Testing is context-dependent

**Pehle samjho:** Banking software aur simple blog website ka risk same
nahi. Dono ko exactly same depth se test karna sensible nahi hoga.

**English definition:** Testing approaches, techniques, and rigor depend
on the context, purpose, risks, and characteristics of the software.

**Example:** Financial application mein security, transaction
correctness aur auditability ko high priority mil sakti hai.

### Principle 7 --- Absence-of-errors fallacy

**Pehle samjho:** Software written requirements ke according pass ho
gaya. Lekin requirements hi user ki real need ko miss kar rahi thi.
Product technically pass hoke bhi user ko disappoint kar sakta hai.

**English definition:** Software that contains few or no known defects
may still fail if it does not meet user needs or business expectations.

**Example:** Ride booking app fare calculate karti hai, lekin peak-hour
surge pricing requirement missing hai.

### Seven principles --- revision card

  ---------------------------------------------------------------------
                           \# Principle            One-line memory
  --------------------------- -------------------- --------------------
                            1 Presence of defects  Passing tests ≠
                                                   defect-free proof

                            2 Exhaustive testing   Har combination test
                                                   nahi ho sakta

                            3 Early testing        Requirements se hi
                                                   testing mindset

                            4 Defect clustering    Defects kuch modules
                                                   mein zyada mil sakte
                                                   hain

                            5 Pesticide paradox    Same tests ko
                                                   refresh karo

                            6 Context-dependent    Testing product/risk
                                                   ke hisaab se

                            7 Absence-of-errors    Bug-free-looking
                              fallacy              product bhi user
                                                   need fail kar sakta
                                                   hai
  ---------------------------------------------------------------------

🟡 **Difficulty:** Medium \| ⏱️ 75--90 minutes

------------------------------------------------------------------------

## 8. Bug Report --- Defect ko clearly communicate kaise karein?

### Pehle apni language mein samjho

Tumne checkout mein bug find kiya. Developer ko sirf "Checkout not
working" likh doge to wo kaise reproduce karega?

Developer ko pata hona chahiye: - Kahan issue aaya? - Kaunsa input use
kiya? - Kaunse steps follow kiye? - Expected kya tha? - Actual kya
hua? - Environment kya tha?

### English definition

**Bug Report / Defect Report:** A structured record describing a
software defect, including enough information for another team member to
understand, investigate, and reproduce it.

### Common fields

  Field                Kya likhna hai
  -------------------- --------------------------------------------
  Title                Short and specific issue
  Environment          App, browser, build, environment
  Preconditions        Issue se pehle required state
  Steps to reproduce   Exact numbered actions
  Expected result      Requirement ke according expected behavior
  Actual result        Execution mein observed behavior
  Severity             Defect ka impact
  Priority             Fix kitni jaldi chahiye
  Evidence             Screenshot, video, logs, if captured

### Severity vs Priority

-   **Severity:** Defect ka impact kitna serious hai?
-   **Priority:** Isko kitni urgency se fix karna chahiye?

Dono related hain, lekin same cheez nahi. Actual scales company ke
process par depend karti hain.

### MindBridge ZIP example

Uploaded lab ke according: - `94105` valid sample ZIP hai. - `testing`
alphabetic input hai. - Seeded defect mein `testing` accept ho jata
hai. - Expected behavior: invalid ZIP reject ho aur clear validation
message aaye.

Agar app execute nahi ki, to report mein source-described behavior
likho; apna observed result pretend mat karo.

🟡 **Difficulty:** Medium \| ⏱️ 40--50 minutes

------------------------------------------------------------------------

# 🔵 MODULE 02 --- WEB APPLICATION ARCHITECTURE

## 9. Web Application ki 3 layers

### Pehle apni language mein samjho

Maan lo tum food delivery app mein "Place Order" click karte ho.

Tumhare screen par button hai. Button click karne ke baad app order
details server ko bhejti hai. Server business rules check karta hai.
Phir database mein order save hota hai. Result wapas screen par show
hota hai.

Yaani ek user action ke peeche multiple parts kaam karte hain.

### English definition

**Three-layer web application architecture:** A common way of organizing
an application into presentation, application/business-logic, and data
layers, each with a distinct responsibility.

## 9.1 Presentation Layer

**Hinglish:** Jo user browser par dekhta aur interact karta hai: -
Buttons - Forms - Menus - Product cards - Text and images - Validation
messages

**English definition:** The presentation layer is the user-facing
interface responsible for displaying information and capturing user
interactions.

**Tester checks:** Visibility, labels, layout, validation message,
accessibility, button state.

## 9.2 Application Layer

**Hinglish:** Ye application ka decision-making/business logic part
hai: - Login credentials validate karna. - Cart total calculate karna. -
Discount apply karna. - Authorization check karna. - Checkout process
karna.

**English definition:** The application layer processes requests and
applies business rules and application logic.

**Tester checks:** API endpoint, HTTP method, request payload, response,
business rules, authentication and authorization.

## 9.3 Data Layer

**Hinglish:** Jahan application ka data persist/read hota hai, usually
database: - Users - Products - Cart items - Orders - Payment records

**English definition:** The data layer is responsible for storing,
retrieving, and managing persistent application data.

**Tester checks:** Correct record saved/updated, duplicate record, data
consistency---only when authorized access/evidence is available.

## 9.4 Complete flow

``` text
User clicks "Place Order"
          |
          v
PRESENTATION LAYER
Captures user action and form data
          |
          v
HTTP / API REQUEST
          |
          v
APPLICATION LAYER
Validates request and applies business rules
          |
          v
DATA LAYER
Stores or retrieves order information
          |
          v
APPLICATION LAYER
Prepares response
          |
          v
PRESENTATION LAYER
Shows success or error to user
```

### Interview answer

"A typical web application can be understood through three layers. The
presentation layer displays the user interface and captures actions. The
application layer processes requests and applies business logic. The
data layer stores and retrieves persistent information. These layers
work together to complete user operations."

🟢 **Difficulty:** Easy--Medium \| ⏱️ 45--60 minutes

------------------------------------------------------------------------

## 10. Browser Developer Tools --- Tester ka investigation toolkit

### Pehle apni language mein samjho

Maan lo login button click kiya, lekin user login nahi hua.

Kya problem button mein hai? API mein? Server mein? Database mein? Sirf
screen dekhkar pata nahi chalega.

Browser DevTools tumhe evidence deta hai: - UI ke HTML elements. -
Browser console errors. - Network requests. - Server responses. -
Application storage/cookies.

### English definition

**Browser Developer Tools:** Built-in browser utilities used to inspect
and debug web pages, JavaScript, network activity, storage, and
rendering behavior.

### DevTools kaise open karein?

-   `F12`
-   `Ctrl + Shift + I`
-   Right-click an element → Inspect

### Important tabs

  Tab           Use
  ------------- -----------------------------------------
  Elements      DOM/HTML inspect
  Console       JavaScript errors and logs
  Network       Browser-server requests/responses
  Application   Cookies, local storage, session storage
  Sources       Loaded scripts and debugging

## 10.1 Elements tab

Example:

``` html
<button type="submit" class="btn btn-primary">
  Sign in
</button>
```

Tum inspect kar sakte ho: - Tag: `button` - Type: `submit` - Class:
`btn btn-primary` - Visible text: `Sign in`

Automation note: Locator ke liye accessible role/name/label ko
preference do jab available ho. CSS class hamesha stable locator nahi
hoti.

## 10.2 Network tab

Steps: 1. DevTools open karo. 2. Network tab select karo. 3. Fetch/XHR
filter choose karo. 4. Preserve log zaroorat par enable karo. 5. Request
list clear karo. 6. Application mein action perform karo. 7. New request
select karo. 8. Headers, Payload, Response aur Timing inspect karo.

### Request mein kya dekhna hai?

  Field         Meaning
  ------------- --------------------------------
  Request URL   Request kis endpoint par gayi
  Method        GET, POST, PUT, PATCH, DELETE
  Status        Server/network response status
  Payload       Client ne kya data bheja
  Response      Server ne kya return kiya
  Timing        Request mein kitna time laga

## 10.3 Common HTTP methods

  Method   Common purpose                 Example
  -------- ------------------------------ ----------------------------
  GET      Data retrieve                  `GET /api/courses`
  POST     Create/submit action           `POST /api/cart/items`
  PUT      Full resource update/replace   `PUT /api/users/12`
  PATCH    Partial resource update        `PATCH /api/users/12`
  DELETE   Delete resource                `DELETE /api/cart/items/5`

Actual API design project ke conventions ke hisaab se vary kar sakta
hai.

## 10.4 Common HTTP status codes

    Code General meaning
  ------ ---------------------------------------------------
     200 OK
     201 Created
     204 No Content
     400 Bad Request
     401 Unauthorized / authentication required or invalid
     403 Forbidden
     404 Not Found
     409 Conflict
     422 Unprocessable Content
     500 Internal Server Error

> [!WARNING] Sirf status code dekhkar final conclusion mat nikalo.
> Request, response body, requirement aur application behavior bhi
> inspect karo. Different applications validation errors ke liye
> different status codes use kar sakti hain.

## 10.5 UI error vs backend error

Suppose screen par "Something went wrong" show hota hai.

Possible causes: - Frontend JavaScript error. - Request send nahi hui. -
API ne 400/401/403/404 return kiya. - Server ne 500 return kiya. -
Network timeout. - Response successful tha, lekin UI ne wrong handling
ki.

Investigation: 1. Console error? 2. Network request bani? 3. URL/method
correct? 4. Status kya hai? 5. Response body kya hai? 6. UI response ko
correctly display kar rahi hai?

**Evidence ke bina frontend/backend ko blame mat karo.**

## 10.6 Security note

Real credentials, access tokens, cookies, personal data ya payment
information screenshots/logs mein expose mat karo. Evidence share karne
se pehle sensitive values redact karo.

🟡 **Difficulty:** Medium \| ⏱️ 60--90 minutes

------------------------------------------------------------------------

## 11. Mapping testing activities to web layers

Course lab mein MindBridge ke actions ko three layers par map kiya gaya
hai.

  ------------------------------------------------------------------------------
  User action   Presentation   Application/API                     Data layer
  ------------- -------------- ----------------------------------- -------------
  Load          Course grid    `GET /api/courses`                  Course rows
  catalogue     appears                                            read

  View course   Course details `GET /api/courses/{id}`             One course
                appear                                             read

  Filter by     Filtered       `GET /api/courses?level=beginner`   Matching rows
  level         results appear                                     read

  Search title  Search results `GET /api/courses?search=python`    Matching rows
                appear                                             read

  Add to cart   Cart count     `POST /api/cart/items`              Cart item
                changes                                            written

  Submit        Error message  `POST /api/checkout` returns 500    Lab mapping
  payment with                                                     says data
  seeded                                                           layer not
  special                                                          reached
  character                                                        
  ------------------------------------------------------------------------------

### Payment example --- source-specific detail

Uploaded lab ke mutabik card number mein `$` (aur described examples
`<`, `>`, `&`, `(`, `)`) use karne par checkout POST request 500 return
karti hai. Lab expected mapping ke mutabik failure application layer par
hota hai, data layer tak nahi pahunchta.

**Important:** Lab specifically kuch characters ko crash trigger batata
hai. Isko "all special characters fail" generalization mat banao.

### Better bug observation

Weak: "Payment page broken."

Better: "When the seeded special character `$` is entered in the
card-number field and Place Order is selected, `POST /api/checkout`
returns HTTP 500 and the UI displays an error. According to the lab's
expected layer mapping, the request fails in the application layer
before data-layer access."

------------------------------------------------------------------------

# 🟠 MODULE 03 --- STATIC, DYNAMIC TESTING & TEST LEVELS

## 12. Static Testing

### Pehle apni language mein samjho

Socho tum ghar banwa rahe ho. Construction start hone se pehle architect
ka blueprint check karte ho.

Blueprint mein likha hai: - Bedroom mein door hona chahiye. - Ek doosri
line mein likha hai bedroom ka entrance permanently closed rahega.

Ghar banne se pehle document mein ye conflict mil gaya. Abhi software ya
building execute/run nahi hui, lekin problem identify ho gayi.

Software mein bhi tester requirements, design, documents ya code ko
execute kiye bina review kar sakta hai.

### English definition

**Static Testing:** A testing approach in which work products such as
requirements, designs, documents, or source code are examined without
executing the software.

### Static testing ke examples

-   Requirement review.
-   Design review.
-   Test case review.
-   Code review.
-   Static code analysis.

### Static testing kya find kar sakti hai?

-   Ambiguous requirement.
-   Contradictory requirements.
-   Missing requirement.
-   Incorrect calculation in a specification.
-   Coding standard violation.
-   Potential code issue identified by static analysis.

### MindBridge example --- password requirement

Uploaded course video mein: - Requirement UR-04: password minimum 8
characters. - Requirement UR-09: password minimum 10 characters and at
least one special character.

Course video ise direct contradiction ke roop mein present karta hai.
More precisely, dono statements different rules/thresholds specify karte
hain; team ko single unambiguous acceptance rule clarify karna chahiye.
Agar 10 characters wala rule final hai, woh 8-character minimum ko
satisfy bhi karta hai, lekin requirement set phir bhi
inconsistent/ambiguous hai because exact intended rule clear nahi.

Static finding example:

  ---------------------------------------------------------------------
  Field                              Finding
  ---------------------------------- ----------------------------------
  ID                                 ST-01

  Type                               Static

  Action                             Review password length
                                     requirements

  Finding                            UR-04 says minimum 8; UR-09 says
                                     minimum 10 and special character

  Recommendation                     Clarify and update requirements
                                     before implementation
  ---------------------------------------------------------------------

### Extra practical knowledge

Static testing ka matlab sirf manual document reading nahi. Static
analysis tools code ko execute kiye bina inspect kar sakte hain---for
example, code quality, style, type or security issue detection.

------------------------------------------------------------------------

## 13. Dynamic Testing

### Pehle apni language mein samjho

Ab ghar ban chuka hai. Tum actual door open karte ho, lights on karte
ho, taps run karte ho. Yaani ab system ko use karke check kar rahe ho.

Software mein application run karke: - Button click karna. - Form submit
karna. - Search karna. - API call execute karna. - Expected vs actual
result compare karna.

Ye dynamic testing hai.

### English definition

**Dynamic Testing:** A testing approach in which software is executed
with test data to evaluate its actual behavior and compare results with
expected behavior.

### MindBridge example

Course video ke final clarified requirement ke according password: - At
least 10 characters. - At least one special character.

A valid test password use karne par application error show karti hai:
"Password must not contain special characters."

Expected: Account should be created successfully.\
Actual: System displays an error.

Ye dynamic testing mein discovered functional defect hai.

> [!IMPORTANT] Transcript mein password example ka text extraction
> ambiguous hai: spoken text "password 123!" jaisa capture hua hai,
> jabki speaker kehta hai ki value 10 characters se zyada hai. `123!`
> akela 4 characters hota hai, isliye use valid example nahi maana ja
> sakta. Practice ke liye mentor-created value `Welcome123!` (11
> characters) use karo. Ye source ka exact test input hone ka claim nahi
> hai.

### Dynamic finding example

  ---------------------------------------------------------------------
  Field                              Finding
  ---------------------------------- ----------------------------------
  ID                                 DT-01

  Type                               Dynamic

  Action                             Create account with a valid
                                     password containing a special
                                     character

  Expected                           Account should be created
                                     successfully

  Actual                             Application displays an error
                                     rejecting special characters
  ---------------------------------------------------------------------

------------------------------------------------------------------------

## 14. Static vs Dynamic Testing --- Difference

  -----------------------------------------------------------------------
  Point                   Static Testing          Dynamic Testing
  ----------------------- ----------------------- -----------------------
  Software execute hota   No                      Yes
  hai?                                            

  Kya inspect hota hai?   Documents,              Running software
                          requirements, design,   
                          code                    

  Main focus              Defects before          Runtime behavior
                          execution               

  Example                 Requirement conflict    Registration form
                          review                  submit

  Output                  Review findings, static Test results, runtime
                          analysis findings       defects

  Benefit                 Early issue detection   Actual behavior
                                                  validation
  -----------------------------------------------------------------------

### Dono mein se better kaunsa?

Dono important hain. Static testing requirement/design/code mein issues
identify kar sakti hai. Dynamic testing actual execution behavior check
karti hai. Ek doosre ka replacement nahi hain.

### English interview answer

"Static testing examines work products such as requirements, design
documents, and source code without executing the software. Dynamic
testing executes the application with test data to verify its actual
behavior. Static testing can identify issues early, while dynamic
testing validates runtime behavior. Both are complementary."

🟡 **Difficulty:** Medium \| ⏱️ 45--60 minutes

------------------------------------------------------------------------

## 15. Shift-Left Testing

### Pehle apni language mein samjho

Maan lo tumhare ghar ki construction complete ho gayi. Tab pata chala ki
staircase ki design hi wrong thi.

Ab usko fix karne mein walls todni padengi, cost aur time dono badhenge.

Agar blueprint review ke time hi staircase issue mil jata, to ek
document change se solve ho sakta tha.

Software mein bhi bug jitna late discover hota hai, uska fix kabhi-kabhi
zyada expensive, risky aur disruptive ho sakta hai.

### English definition

**Shift-Left Testing:** An approach that moves testing and quality
activities earlier in the software development lifecycle, rather than
waiting until late development or pre-release stages.

### Course video ka Urban Wear example

-   Retailer Black Friday sale launch kar raha hai.
-   Customers discount code apply karke checkout kar rahe hain.
-   Payment button freeze ho jata hai.
-   Customer service overload, social media complaints aur revenue
    impact hota hai.
-   Course scenario ke mutabik root cause checkout logic mein undetected
    bug hai.

Alternative timeline: - Design phase mein QA tester checkout design
review karta hai. - Tester poochta hai: "What happens if a user applies
a discount code after shipping has been calculated?" - Team missing
logic early identify kar sakti hai.

### Shift-left flow

``` text
DESIGN / REQUIREMENTS
        |
        v
BUILD / DEVELOPMENT
        |
        v
TEST
        |
        v
RELEASE
```

Shift-left ka matlab quality activities ko timeline mein earlier stages
par lana.

### QA tester early stage par kya kar sakta hai?

-   Requirement review.
-   Acceptance criteria clarification.
-   Risk identification.
-   Test scenario planning.
-   Design review.
-   Test data needs identify karna.

### English interview answer

"Shift-left testing means involving testing and quality activities
earlier in the SDLC. Instead of waiting until the software is fully
developed, testers review requirements, identify risks, and plan tests
early. This helps detect issues sooner and can reduce rework and
late-stage failures."

🟡 **Difficulty:** Medium \| ⏱️ 30--45 minutes

------------------------------------------------------------------------

## 16. Testing Levels --- Unit, Integration, System, Acceptance

### Pehle apni language mein samjho

Car banane ka example lo:

1.  Pehle ek bolt check karo ki correct size ka hai.
2.  Phir wheel aur axle ko connect karke check karo.
3.  Phir poori assembled car test karo.
4.  Finally customer car drive karke confirm kare ki uski need meet ho
    rahi hai.

Software testing bhi different scopes par hoti hai. Isi ko testing
levels kehte hain.

### English definition

**Test Levels:** Different stages or scopes of testing used to evaluate
software components, their interactions, the complete system, and
whether the product meets user/business acceptance needs.

## 16.1 Unit Testing

### Hinglish explanation

Application ke smallest testable piece ko independently check karna.
Usually ek function, method ya class.

Example: `calculate_tax()` function: - Price = 1000 - Tax rate = 10% -
Expected tax = 100

Function ka result independently verify kiya jata hai.

### English definition

**Unit Testing:** Testing individual software units, such as functions,
methods, or classes, in isolation to verify that each unit behaves as
expected.

**Who performs it?** Course reading ke according primarily developers.

**What does it find?** - Incorrect calculation. - Wrong conditional
logic. - Unexpected return value. - Edge-case handling issue.

**Course example:** `calculateTax()` function different inputs ke saath
test hota hai.

### Mentor note

Unit tests mein dependencies ko mocks/stubs se replace kiya ja sakta
hai, taaki isolated unit ki logic verify ho. Ye course reading mein bhi
explain hai.

## 16.2 Integration Testing

### Hinglish explanation

Ab individual parts sahi hain. Lekin kya wo ek doosre ke saath sahi
communicate karte hain?

Example: - Registration form user data submit karta hai. - Backend
service request process karti hai. - Database mein user record create
hota hai.

Integration test verify karega ki components ke beech data flow aur
interaction correct hai.

### English definition

**Integration Testing:** Testing interactions and data flow between two
or more integrated software components to identify defects in their
interfaces and connections.

**Who performs it?** Course reading ke according developers and QA
engineers.

**What does it find?** - Wrong API contract. - Incorrect data mapping. -
Interface mismatch. - Component communication failure. - Integration
configuration issues.

## 16.3 System Testing

### Hinglish explanation

Ab application ke components integrate ho chuke hain. Ab poore system ko
ek complete product ki tarah test karna hai.

E-commerce flow: 1. Product search. 2. Product details open. 3. Add to
cart. 4. Discount apply. 5. Shipping information. 6. Checkout. 7. Order
confirmation.

Yahan focus complete end-to-end behavior par hai.

### English definition

**System Testing:** Testing the fully integrated software system as a
whole against specified functional and non-functional requirements.

**Who performs it?** Course reading ke according QA team.

**What does it find?** - End-to-end workflow defects. - Requirement
failures. - Cross-feature interaction issues. - System-level behavior
issues.

## 16.4 Acceptance Testing

### Hinglish explanation

Application technically work kar rahi hai. Lekin kya customer/business
ke actual kaam ke liye acceptable hai?

Example: Accounting team new invoicing software use karti hai: - Invoice
create. - Tax calculate. - Payment record. - Month-end report.

Business user confirm karta hai ki software real workflow support karta
hai.

### English definition

**Acceptance Testing:** Testing performed to determine whether a system
meets business needs and acceptance criteria and is acceptable to its
intended users or customers.

**Who performs it?** Course reading ke according client, end users or
product stakeholders.

**What does it validate?** - Business workflow. - User expectations. -
Acceptance criteria. - Product fitness for intended purpose.

## 16.5 Four levels --- comparison

  -----------------------------------------------------------------------------
  Level           Scope                   Main question    Course reading:
                                                           typical performer
  --------------- ----------------------- ---------------- --------------------
  Unit            Single                  Is this small    Developers
                  function/method/class   unit correct?    

  Integration     Connected components    Do components    Developers + QA
                                          communicate      engineers
                                          correctly?       

  System          Complete integrated     Does the whole   QA team
                  product                 system meet      
                                          requirements?    

  Acceptance      Business/user needs     Is this          Client/end
                                          acceptable to    users/stakeholders
                                          the              
                                          user/business?   
  -----------------------------------------------------------------------------

### Increasing scope

``` text
        ACCEPTANCE
       Business fit
      -------------
          SYSTEM
      Whole product
     ---------------
        INTEGRATION
     Component links
    -----------------
           UNIT
      Small code unit
```

Scope generally increases as we move from Unit to Acceptance.

> [!NOTE] Course reading roles ko is tarah map karta hai. Real
> organizations mein developers, QA engineers aur business users ki
> involvement overlap kar sakti hai. Responsibility project structure
> par depend karti hai.

### Interview answer

"The four main test levels are Unit, Integration, System, and Acceptance
testing. Unit testing checks individual code units. Integration testing
checks interactions between components. System testing validates the
complete integrated application against requirements. Acceptance testing
confirms whether the product meets business and user needs."

🟡 **Difficulty:** Medium \| ⏱️ 60--75 minutes

------------------------------------------------------------------------

## 17. Test Levels vs Static/Dynamic Testing --- Dono alag concepts hain

Ye distinction bahut important hai.

### Hinglish explanation

-   **Testing level** batata hai: kitne scope par test kar rahe ho? Ek
    function, connected components, complete system, ya business
    acceptance?
-   **Static/Dynamic approach** batata hai: work product ko execute kiye
    bina inspect kar rahe ho ya running software execute karke behavior
    check kar rahe ho?

  ---------------------------------------------------------------------
  Concept                            Answers which question?
  ---------------------------------- ----------------------------------
  Test level                         What scope are we testing?

  Static/Dynamic                     Are we executing the software or
                                     examining a work product without
                                     execution?
  ---------------------------------------------------------------------

Example: - Function run karke result check karna = dynamic unit test. -
Requirement document review karna = static testing. - Full checkout flow
execute karna = dynamic system-level test. - Business user workflow
validate karta hai = acceptance testing (typically dynamic execution).

**Mentor clarification:** Static/dynamic techniques aur test levels ko
ek hi classification samajhna mistake hai.

------------------------------------------------------------------------

# 🧪 MODULE 01--03 --- PRACTICAL REVISION & ASSESSMENT

## Exercise 1 --- QA, QC or UAT?

Classify karo aur reason bhi likho:

1.  Requirement ambiguity review karna.
2.  Login test cases execute karna.
3.  Business user invoice workflow accept karta hai.
4.  Team-wide quality standard define karna.
5.  Checkout API response inspect karna.
6.  Product Owner final business acceptance deta hai.

## Exercise 2 --- Seven principles

Checkout ZIP field ke liye: 1. Har possible ZIP value test kyun nahi kar
sakte? 2. Five useful test inputs choose karo. 3. Test suite ko next
release mein kaise refresh karoge? 4. Requirement stage par kaunse
questions poochoge?

## Exercise 3 --- Web layers

Login flow ke liye: 1. Presentation layer ke components. 2. Application
layer ki responsibility. 3. Data layer ki responsibility. 4. Invalid
password par expected UI behavior. 5. Network tab mein kya inspect
karoge?

## Exercise 4 --- Static vs Dynamic

MindBridge registration requirement: - UR-04: password minimum 8
characters. - UR-09: password minimum 10 characters and at least one
special character.

Questions: 1. Document review se kya issue identify hota hai? 2. Ye
static hai ya dynamic? 3. Clarification ke baad final requirement 10+
characters and special character ho. 4. Valid password `Welcome123!`
submit karne par app special characters reject kare to expected vs
actual kya hoga? 5. Ye static finding hai ya dynamic finding?

## Exercise 5 --- Test levels

E-commerce application ke examples ko classify karo:

1.  `calculate_total()` function test.
2.  Checkout service ka payment API ke saath interaction.
3.  Search se order confirmation tak full workflow.
4.  Business team confirms order and refund process meets their business
    needs.

------------------------------------------------------------------------

# 🎤 INTERVIEW QUICK REVISION

## Important definitions

  ---------------------------------------------------------------------
  Term                               One-line explanation
  ---------------------------------- ----------------------------------
  Software Quality                   Software meets requirements and
                                     user needs in its intended context

  Software Testing                   Evaluating software to identify
                                     defects and assess
                                     behavior/quality

  QA                                 Process-oriented quality
                                     activities

  QC                                 Product-oriented quality checking

  UAT                                Business/user acceptance
                                     validation

  RACI                               Responsible, Accountable,
                                     Consulted, Informed

  Static Testing                     Examine work products without
                                     executing software

  Dynamic Testing                    Execute software and evaluate
                                     actual behavior

  Shift-Left                         Move quality/testing activities
                                     earlier in SDLC

  Unit Testing                       Test an individual code unit

  Integration Testing                Test interactions between
                                     components

  System Testing                     Test the complete integrated
                                     system

  Acceptance Testing                 Validate business/user acceptance
                                     needs

  Presentation Layer                 User interface

  Application Layer                  Business logic and request
                                     processing

  Data Layer                         Persistent data storage/retrieval
  ---------------------------------------------------------------------

## 15 questions to practice aloud

1.  What is software testing?
2.  What is the difference between QA and QC?
3.  What is UAT?
4.  Explain verification vs validation.
5.  What is RACI?
6.  Explain the seven testing principles.
7.  What is risk-based testing?
8.  Explain the three layers of a web application.
9.  How do you inspect an API request in Chrome DevTools?
10. What is the difference between HTTP 404 and 500?
11. What is static testing?
12. What is dynamic testing?
13. What is shift-left testing?
14. Explain the four testing levels.
15. What is the difference between a test level and a testing approach?

------------------------------------------------------------------------

# 📊 YOUR PROGRESS TRACKER

Confidence score: - 1 = Concept clear nahi. - 2 = Definition yaad,
example difficult. - 3 = Apne words mein explain kar sakta hoon. - 4 =
Scenario par apply kar sakta hoon. - 5 = Interview mein confidently
explain aur practical use kar sakta hoon.

  Topic                          Status          Confidence (1--5)
  ------------------------------ ------------- -------------------
  Software quality and testing   Not started                   ---
  QA vs QC                       Not started                   ---
  UAT                            Not started                   ---
  Verification vs validation     Not started                   ---
  RACI                           Not started                   ---
  Seven testing principles       Not started                   ---
  Bug reporting                  Not started                   ---
  Three web layers               Not started                   ---
  Browser DevTools               Not started                   ---
  HTTP methods/status codes      Not started                   ---
  Static testing                 Not started                   ---
  Dynamic testing                Not started                   ---
  Shift-left testing             Not started                   ---
  Unit testing                   Not started                   ---
  Integration testing            Not started                   ---
  System testing                 Not started                   ---
  Acceptance testing             Not started                   ---

## 🏁 Module completion standard

Module 1--3 tab complete maanenge jab tum:

-   QA, QC, UAT ko examples ke saath explain kar sako.
-   Seven testing principles ko checkout scenario par apply kar sako.
-   Browser action se API aur data flow explain kar sako.
-   Network tab mein URL, method, status, payload aur response identify
    kar sako.
-   Static aur dynamic testing ka difference confidently bata sako.
-   Shift-left ka real business impact explain kar sako.
-   Unit, Integration, System aur Acceptance testing ke examples de
    sako.
-   Test level aur static/dynamic approach ko confuse na karo.

> [!TIP] **Next step:** Is guide ko ek saath ratne ki koshish mat
> karna. Module 1 ke Session 1 se start karenge. Tum apne words mein
> answer doge; main tumhe review, correction, follow-up scenarios aur
> interview practice dunga. Jab Module 1--3 ki understanding verify ho
> jayegi, tab hum next uploaded module par move karenge.

------------------------------------------------------------------------

## 📚 Source and learning note

This guide is based on the three uploaded course-resource ZIPs: - Module
1: QA/QC/UAT, RACI, seven testing principles, MindBridge testing mindset
and bug reporting. - Module 2: Web application layers, tracing browser
data flow, DevTools and mapping QA activities to layers. - Module 3:
Static vs dynamic testing, applying both techniques, shift-left testing,
and Unit/Integration/System/Acceptance test levels.

Examples marked as mentor-created are additional teaching examples, not
claims about exact Coursera source wording. Where extracted transcripts
were ambiguous, the guide calls that out instead of presenting an
uncertain detail as fact.
