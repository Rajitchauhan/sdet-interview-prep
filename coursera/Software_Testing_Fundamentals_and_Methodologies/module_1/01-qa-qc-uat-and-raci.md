# Lesson 1 --- QA, QC, UAT and RACI

`<small>`{=html}Source-based lesson \| Difficulty: Easy → Medium \|
Estimated study time: 60--90 minutes`</small>`{=html}

## 1. WHY --- Ye topic kyun padhna hai?

Software quality sirf tester ke test cases run karne se nahi aati.
Product banne se pehle team ko quality ke rules aur process define karne
hote hain; product banne ke baad usko test karna hota hai; aur business
ko confirm karna hota hai ki product actual need solve karta hai.

Is lesson ka central idea:

-   QA: quality build karne ke liye process aur standards establish
    karna.
-   QC: actual product ko check karke defects identify karna.
-   UAT: business/user perspective se validate karna ki product expected
    value deliver karta hai.

Agar ye roles clear nahi honge, to team mein responsibility overlap ya
gaps ho sakte hain.

## 2. WHAT --- Quality Assurance (QA)

### Course Source

Uploaded course video QA ko **proactive and process-oriented** approach
batata hai. QA ka focus defects hone ki likelihood kam karne ke liye
SDLC ke across standards, practices, processes aur guidelines establish
karna hai.

Course ke according QA activities:

-   Requirements review karna.
-   Test strategy create karna.
-   Coding aur quality standards define karna.
-   Risks identify karna.
-   Development ke dauran required testing activities map karna.
-   Check karna ki agreed processes follow ho rahe hain.

QA ka central question:

> "Have we set up the right conditions and processes to build a quality
> product from the start?"

### Mentor Explanation --- Simple Hinglish

QA ka matlab sirf "testing karna" nahi hai. QA ka focus hai **process ko
aisa banana ki defects introduce hone ke chances kam hon**.

Example: Team ek new checkout feature bana rahi hai. QA-oriented
activities ho sakti hain:

-   Requirement clear hai ya ambiguous, ye review karna.
-   Team ke liye code review process define karna.
-   Accessibility standards agree karna.
-   Decide karna ki feature ke liye kaunse testing activities required
    hongi.
-   Ensure karna ki agreed process follow ho raha hai.

QA ka focus hai: "Hum quality product banane ke liye sahi process follow
kar rahe hain ya nahi?"

## 3. WHAT --- Quality Control (QC)

### Course Source

Uploaded course QC ko **reactive and product-oriented** approach batata
hai. QC actual product par focus karta hai aur defects identify karta
hai.

Course mein QC activities:

-   Test cases execute karna.
-   Product ko requirements ke against review karna.
-   Outputs inspect karna.
-   Defects identify karna.
-   Verify karna ki product expected behavior show karta hai.

### Mentor Explanation --- Simple Hinglish

QC mein tester actual application ko use/check karta hai. Jaise checkout
page par:

-   Valid ZIP code accept hota hai?
-   Alphabetic ZIP code reject hota hai?
-   Special characters ka behavior kya hai?
-   Place Order click karne par correct response aata hai?
-   Different browsers mein feature ka behavior consistent hai?

QC ka focus hai: "Jo product bana hai, kya woh requirements ke according
kaam kar raha hai?"

## 4. QA vs QC --- Side-by-side

  -----------------------------------------------------------------------
  Point                   QA                      QC
  ----------------------- ----------------------- -----------------------
  Main focus              Process                 Product

  Course framing          Proactive               Reactive

  Main objective          Defects prevent karne   Existing defects
                          ki likelihood reduce    identify karna
                          karna                   

  Typical work            Requirements review,    Test execution, output
                          standards, test         inspection, defect
                          strategy, risk          reporting
                          identification          

  Core question           Kya quality build karne Kya actual product
                          ka process sahi hai?    expected behavior de
                                                  raha hai?
  -----------------------------------------------------------------------

**Important:** Course QA aur QC ko alag focus ke roop mein explain karta
hai. Iska matlab ye nahi ki quality sirf ek QA Lead ya QC Engineer ki
responsibility hai. Course ka QA-vs-QC practical video quality ko team
effort batata hai.

## 5. WHAT --- User Acceptance Testing (UAT)

### Course Source

Uploaded video ke according UAT primarily in logon ke through perform
hota hai:

-   Business stakeholders
-   Product owners
-   Customer representatives
-   Selected end users

Development aur QA teams UAT support kar sakti hain, lekin final
acceptance decision generally unka nahi hota.

UAT ka goal:

-   Business requirements validate karna.
-   Real user workflows support hote hain ya nahi check karna.
-   Expected business value mil rahi hai ya nahi confirm karna.

UAT ka central question:

> "Does this product deliver the value we expected?"

### Mentor Explanation --- Simple Hinglish

Maan lo team ne students ke liye AI Practice Generator banaya.

QC tester check kar sakta hai: - Generate button click karne par
questions generate hote hain? - Special characters handle hote hain? -
Browser compatibility sahi hai?

Lekin student ya Product Owner ye evaluate karega: - Kya generated
questions useful hain? - Kya feature student ko study karne mein help
karta hai? - Kya feature actual business/user need solve karta hai?

Yahi UAT perspective hai.

### QA, QC, UAT --- Simple analogy

Course video apartment analogy deta hai:

-   Architect plans banata hai --- QA ke process/standards jaisa.
-   Inspector building check karta hai --- QC jaisa.
-   Tenant final walkthrough karta hai --- UAT jaisa.

Analogy perfect one-to-one mapping nahi hai, lekin basic distinction
yaad rakhne mein help karti hai.

## 6. QA, QC, UAT --- One feature lifecycle example

MindBridge mein AI Practice Generator feature add ho raha hai:

``` text
Requirements and design
        |
        v
QA: requirements review, standards, test strategy, risks
        |
        v
Development
        |
        v
QA: agreed process and checks followed?
        |
        v
Feature built
        |
        v
QC: execute tests, inspect behavior, report defects
        |
        v
Business / user validation
        |
        v
UAT: does it solve the user's real need?
```

### Video-specific QC checks

Uploaded transcript mein AI Practice Generator ke examples:

-   Special characters correctly handle karta hai?
-   Different web browsers par work karta hai?
-   Generate button multiple times click karne par expected response
    deta hai?

Ye examples course source se liye gaye hain.

## 7. RACI Matrix

### Course Source

RACI ek tool hai jo major tasks ke liye team responsibilities clear
karta hai.

  Letter   Full form     Simple meaning
  -------- ------------- -------------------------------------------------------
  R        Responsible   Kaam perform karta hai
  A        Accountable   Final ownership/decision leta hai
  C        Consulted     Input/advice deta hai
  I        Informed      Progress/decision ke baare mein update rakha jata hai

### Course video ka acceptance-criteria example

  Task                         Product Owner   QA Lead       Developers
  ---------------------------- --------------- ------------- ------------
  Define acceptance criteria   Accountable     Responsible   Consulted

Course narration ke mutabik Product Owner final decision own karta hai,
QA Lead work karta hai aur developers input dete hain.

### "Write test cases" example --- source discrepancy

Video narration ke mutabik: - QC Engineer hands-on test execution ke
liye Responsible hai. - QA Lead overall test quality ke liye Responsible
hai. - Developer ko Informed rakha jata hai.

Lekin detailed visual transcript mein "Write test cases" ke visual par
QA Lead ko Responsible aur Developer ko Informed dikhaya gaya hai; QC
Engineer ki assignment visual mein clearly represented nahi hai.

**Isliye source ka exact RACI row fully unambiguous nahi hai.** Is
course mein hum narration ko as spoken record kar rahe hain, lekin ise
ek perfectly verified RACI table nahi maan rahe.

### Mentor's Additional Knowledge

RACI banate waqt har task ke liye ye check karna useful hota hai: - Kaun
actual kaam karega? - Final approval/ownership kiski hai? - Kis se input
lena zaroori hai? - Kisko sirf update dena hai?

Ek task mein Responsible aur Accountable roles ka practical assignment
organization ke process ke hisaab se vary kar sakta hai. Team ko pehle
agree karna chahiye.

## 8. Practical example --- Checkout feature

Ye example mentor practice ke liye hai, course ke original RACI example
ka replacement nahi.

  --------------------------------------------------------------------------
  Task           Product Owner  QA Lead        Developer      QC Tester
  -------------- -------------- -------------- -------------- --------------
  Business       A              R/C            C              C
  acceptance                                                  
  rules agree                                                 
  karna                                                       

  Code review    I              A/R (team      R              I
  standard                      process ke                    
  follow karna                  mutabik)                      

  Checkout test  I              A (test        I              R
  execute karna                 quality)                      

  Defect fix     I              C              R              C
  karna                                                       

  Business       A/R            C              I              C
  workflow                                                    
  accept karna                                                
  --------------------------------------------------------------------------

**Note:** Ye illustrative mentor-created matrix hai, uploaded Coursera
source ka official answer nahi. Actual team mein roles aur ownership
change ho sakte hain.

## 9. Common beginner mistakes

1.  **QA = testing, QC = testing** --- dono ko sirf test execution
    samajhna. Course ka key distinction process vs product focus hai.
2.  **UAT ko normal scripted testing samajhna** --- course UAT ko
    business/user workflow aur value validation ke perspective se
    explain karta hai.
3.  **QA sirf release se pehle hota hai** --- source QA ko SDLC ke
    across describe karta hai.
4.  **Tester hi quality ka sole owner hai** --- course video quality ko
    team effort ke roop mein frame karta hai.
5.  **RACI mein R aur A confuse karna** --- Responsible work karta hai;
    Accountable final ownership/decision leta hai.

## 10. Interview understanding

### Simple English answer

"Quality Assurance focuses on improving processes and standards to
prevent defects. Quality Control focuses on checking the actual product
by executing tests and identifying defects. User Acceptance Testing
validates whether the product meets business needs and delivers value to
users."

### Stronger answer (practice version)

"Quality Assurance is a proactive, process-oriented approach applied
throughout the software development lifecycle. It includes activities
such as reviewing requirements, defining quality standards, identifying
risks, and establishing a test strategy. Quality Control is
product-oriented and focuses on evaluating the actual application
through test execution, output inspection, and defect reporting. User
Acceptance Testing is primarily performed by business stakeholders or
representative users to confirm that real workflows and business
expectations are satisfied. These activities complement each other and
contribute to product quality."

### Keywords

`Proactive` · `Process-oriented` · `Product-oriented` ·
`Defect prevention` · `Defect detection` · `Business requirements` ·
`User workflow` · `Business value` · `RACI`

## 11. Mentor's Additional Knowledge --- UAT timing nuance

Course video UAT ko "last phase before go-live" kehta hai. Ye course ka
simplified teaching model hai. Real-world teams mein UAT ka timing
delivery model, release process aur business availability par depend kar
sakta hai. Isliye interview mein UAT ka **purpose and participants**
explain karna zyada important hai; har organization mein ek fixed
calendar position claim mat karna.

## 12. Practice --- Answer without notes

1.  QA aur QC mein main difference kya hai?
2.  QA activities coding start hone se pehle kaise help kar sakti hain?
3.  QC tester checkout page par kaunse checks perform kar sakta hai?
4.  UAT mein business stakeholder kya validate karega jo normal
    functional test se different ho sakta hai?
5.  RACI mein Responsible aur Accountable ka difference kya hai?
6.  Agar test execution ho chuka hai lekin business ko feature useful
    nahi lagta, to kaunsa validation perspective missing ho sakta hai?

### Mini task

MindBridge checkout feature ke liye 4 tasks likho aur har task ke liye
R, A, C, I assign karne ki koshish karo. Ye tumhara own practice matrix
hoga, official course answer nahi.

## 13. Lesson completion checklist

-   [ ] Main QA ko process-oriented approach ke roop mein explain kar
    sakta hoon.
-   [ ] Main QC ko product-oriented checking ke roop mein explain kar
    sakta hoon.
-   [ ] Main UAT ka purpose aur participants bata sakta hoon.
-   [ ] Main RACI ke four letters explain kar sakta hoon.
-   [ ] Main checkout feature ka ek simple RACI example bana sakta hoon.
-   [ ] Main source video ki RACI ambiguity identify kar sakta hoon.
