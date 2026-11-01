# 🧪 MODULE 2 — TESTING FOUNDATIONS & PRINCIPLES
## Hinglish Mentor Notes | University of Minnesota

> 🎯 **Module ka goal:** Is module mein hum “testing kaise karni chahiye?” ko systematic tarike se samjhenge. Dependability, testing principles, programmer mistakes ke hotspots, V-Model, Verification/Validation, Structural Testing aur Mutation Testing cover honge.

> 🧭 **Reading rule:** `🎓 COURSE STORY` lecture ka original example simple Hinglish mein explain karta hai. `🧠 MENTOR EXPLAINS` concept ko practical banata hai. `💼 SDET CONNECTION` automation work se jodta hai. `⭐ INTERVIEW` interview answer deta hai. **Overlap ke naam par koi topic remove nahi kiya gaya.**

---

# 🗺️ Module 2 ka lecture map

| Lecture | Core topic | Main question |
|---|---|---|
| 1 | Dependability | Software par bharosa kaise measure/achieve karte hain? |
| 2 | Testing Principles & Quality Process | Testing ka objective kya hai? |
| 3 | Where Programmers Make Mistakes | Testing effort kahan focus karein? |
| 4 | How We Test — Principles | Effective testing kaise organize karein? |
| 5 | V-Model | Development phases ke saath testing ka relation kya hai? |
| 6 | V&V in V-Model | Verification aur validation practical level par kaise differ karte hain? |
| 7 | Structural Testing | Code execution/coverage ko kaise measure karte hain? |
| 8 | Mutation Testing | Hamare tests khud kitne effective hain? |

🎯 **Difficulty:** Medium → Hard  |  **Interview relevance:** High

---

# 1. 🎓 LECTURE 1 — Dependability: Can We Rely on Software?

## 1.1 Dependability kya hai?

Instructor lecture ki shuruaat terminology clear karne se karte hain.

**Dependability** ka matlab: kya software aisi service deliver karta hai jis par hum rely kar sakein?

**Service** = system ka woh behaviour jo user ko perceive hota hai.

Example:
- Airplane ki service: passengers ko ek destination se doosre destination tak le jana.
- Shopping website ki service: user ko products buy karne dena.

Agar user website par purchase karna chahta hai aur system error de deta hai, toh delivered service expected service se deviate hui.

## 1.2 Fault → Error → Failure — most important chain

### 🎓 COURSE SOURCE

Instructor teen terms distinguish karte hain:

| Term | Meaning |
|---|---|
| **Fault** | Root cause; programmer mistake, misunderstanding, design mistake ya physical defect |
| **Error** | System ke andar wrong state jo failure cause kar sakti hai |
| **Failure** | User ko delivered service specification se different milti hai |

Lecture ka sequence:

```text
Programmer mistake / Fault
          ↓
Latent error in code/state
          ↓ (faulty code path execute hua)
Effective error
          ↓ (fault tolerance ne hide nahi kiya)
Failure visible to user
```

### 🧠 MENTOR STORY — shopping checkout

Maan lo developer ne discount calculation mein wrong condition likh di.

1. **Fault:** Developer ne business rule galat implement kiya.
2. **Latent error:** Wrong condition code mein present hai, lekin abhi tak execute nahi hui.
3. **Effective error:** Specific cart value par faulty condition execute hui aur wrong total calculate hua.
4. **Failure:** User ko wrong amount charge/display hua.

**Key difference:** Fault root cause hai; error internal incorrect state hai; failure externally visible service problem hai.

## 1.3 Latent error vs Effective error

- **Latent:** Defect/code issue present hai, lekin execution mein abhi trigger nahi hua.
- **Effective:** Faulty code path execute hua aur system state wrong ho gayi.

Har effective error user ko failure ke roop mein dikhe, zaroori nahi. Fault tolerance error ko contain kar sakta hai.

## 1.4 Dependability achieve karne ke 4 approaches

### A. Fault Avoidance

Faults ko by-construction prevent karna.

Instructor examples:
- C mein array boundary cross karke buffer overflow ho sakta hai.
- Java array bounds checking provide karta hai.
- Haskell ka rich type system compile time par kuch problems detect kar sakta hai.

**Simple:** Aisi language, design ya coding rule use karo jo kuch classes of mistakes ko hone hi na de.

### B. Fault Tolerance

Agar ek component fail ho, toh system ke remaining parts service continue kar sakein.

Instructor examples:
- Aircraft mein multiple actuators; ek fail ho toh doosra control maintain kar sake.
- Large websites mein redundant servers; ek server crash ho toh doosre load handle karein.

**Simple:** Failure ko tolerate karne ki capacity.

### C. Error Removal

Existing errors ko identify aur remove karna. Instructor ke according verification/testing latent errors remove karne mein help karte hain.

**Testing ka relation:** Testing error removal approach ka part hai.

### D. Error Forecasting

System ke behaviour ke basis par estimate karna ki future failures kitne likely hain. Ye errors remove karna nahi, dependability ka assessment/measurement hai.

### ⭐ INTERVIEW TABLE

| Approach | One-line answer |
|---|---|
| Fault avoidance | Faults ko introduce hone se prevent karna |
| Fault tolerance | Fault ke baad bhi service continue rakhna |
| Error removal | Existing errors detect/remove karna |
| Error forecasting | Failure likelihood estimate karna |

## 1.5 Dependability metrics — Reliability, Availability, Safety, Integrity, Maintainability

### Reliability

**Correct service ki continuity.** System kitne time tak continuously correct service provide karta hai?

Instructor metric: **MTBF — Mean Time Between Failures**.

### Availability

**User request ke liye system ready/available hone ki probability/readiness.**

Instructor kehte hain reliability aur availability same nahi. System unreliable ho sakta hai, lekin agar failure ke baad bahut quickly reboot/recover ho jata hai, toh availability phir bhi high ho sakti hai.

### Recoverability

Failure ke baad system kitni jaldi correct operation mein restore hota hai.

Instructor metric: **MTTR — Mean Time To Repair**.

### Availability formula

\[
Availability = \frac{MTBF}{MTBF + MTTR}
\]

Example:
- MTBF = 99 hours
- MTTR = 1 hour

\[
Availability = \frac{99}{99+1}=0.99=99\%
\]

**Interpretation:** Long operating time + short recovery time → higher availability.

### Safety

Software failure ke kaaran catastrophic consequences ka absence.

Instructor ka car example:
- Car jo kabhi start hi nahi hoti: unreliable, lekin driveway mein khadi rahe toh safe ho sakti hai.
- Car jo mostly theek chalti hai lekin kabhi unintended acceleration kar deti hai: reliability generally high ho sakti hai, lekin safety risk serious hai.

**Reliability ≠ Safety.**

### Integrity

Improper system alteration ka absence. Security compromise/buffer overflow ke through attacker data ya software change kar de, toh integrity fail hui.

### Maintainability

Software ko modify, repair aur upgrade karne ki ability. Poor maintainability se changes slow/risky ho sakte hain; maintenance ke liye system long time offline rakhna availability ko affect kar sakta hai.

## 1.6 Critical systems & plan for failure

Instructor ka point: critical environment mein sirf expected inputs ke liye correct behaviour enough nahi. System ko unexpected/unreliable inputs, sensors, hardware aur external systems ke failures ke against robust hona chahiye.

Testing environment mein:
- Inputs unreliable simulate karo.
- Stress testing karo.
- Hardware/software components deliberately disconnect/fail karke response observe karo.

### 🎓 COURSE STORY — Netflix Chaos Monkey

Instructor Netflix ka **Chaos Monkey** example dete hain. Ye tool deliberately kuch software/hardware components ko disrupt karta hai, phir measure kiya jata hai ki system kitna well respond karta hai.

**Lesson:** Resilience ko sirf paper par assume nahi karte; failure simulate karke observe karte hain.

## 1.7 DO-178B criticality levels

Lecture aviation guidance ke context mein software failure ke worst consequence ke basis par five levels batata hai:

| Level | Meaning in lecture |
|---|---|
| Catastrophic | Software failure se plane crash ho sakta hai |
| Hazardous | Crew ke liye aircraft fly karna extremely difficult ho sakta hai |
| Major | Crew workload significantly increase |
| Minor | Annoyance/minor effect |
| No Effect | No safety effect |

Criticality jitni high, testing/verification objectives utne rigorous. Lecture Level A catastrophic software ke liye high rigor aur robustness expectations discuss karta hai.

> ⚠️ Course-source note: Ye lecture ka DO-178B framing hai. Is guide mein regulatory standard ko independently update/interpret nahi kiya gaya.

### ⭐ INTERVIEW ANSWER — Dependability

“Dependability is the ability of software to deliver a service that users can rely on. A fault is the root cause, an error is an incorrect internal state, and a failure occurs when the delivered service deviates from the specification. Dependability can be improved through fault avoidance, fault tolerance, error removal and error forecasting. It can be discussed using reliability, availability, safety, integrity and maintainability.”

**Keywords:** fault, error, failure, latent, effective, fault tolerance, MTBF, MTTR, availability, reliability.

---

# 2. 🎓 LECTURE 2 — Testing Principles & The Quality Process

## 2.1 Principles → Methods/Techniques → Methodologies → Tools

Instructor testing ko layers mein organize karte hain:

```text
Principles
   ↓
Methods & Techniques
   ↓
Methodologies
   ↓
Tools
```

- **Principles:** Sochne ke fundamental rules — hum testing ko kis nazariye se approach karein?
- **Methods/Techniques:** Specific testing approaches.
- **Methodologies:** Methods ko systematically apply karne ka organized way.
- **Tools:** Automation/efficiency ke liye software tools.

**Mentor example:** “Risk important hai” ek principle ho sakta hai; risk-based testing technique/method hai; team ka risk-based test planning process methodology ka part hai; test management tool execution/management mein help kar sakta hai.

## 2.2 Five questions: What, Where, When, Who, How

Lecture testing principles ko five questions mein frame karta hai:

| Question | Meaning |
|---|---|
| **What** | Testing se achieve kya karna hai? |
| **Where** | Code/system ke kis area par focus karna hai? |
| **When** | Testing kab aur kitni baar karni hai? |
| **Who** | Testing kaun karega — developer, independent tester, separate team? |
| **How** | Individual test cases likhte waqt effective strategy kya hogi? |

Is lecture mein instructor primarily **WHAT — Quality Process** par focus karte hain.

## 2.3 Quality Process — testing ka objective

Quality process ka matlab:
- Software ke quality goals identify karo.
- Un goals ko achieve karne ke liye testing/verification plan karo.
- Available time aur money ko cost-effectively use karo.
- Process ko sufficiently rigorous rakho.

### 🧠 MENTOR EXPLAINS

Testing ka objective “jitne zyada test cases utna better” nahi. Pehle define karo ki product ke liye important quality goals kya hain:
- Functional correctness?
- Security?
- Performance?
- Availability?
- Usability?
- Reliability?

Phir decide karo kaunsi testing activity un goals ka evidence degi.

### ⭐ INTERVIEW

“Testing principles provide a systematic foundation for deciding what quality goals to achieve, where to focus testing, when and by whom testing should be performed, and how effective test cases should be designed.”

---

# 3. 🎓 LECTURE 3 — Where Are Programmers Likely to Make Mistakes?

## 3.1 Mistakes ke reasons

Instructor reasons list karte hain:
- Time pressure.
- Complex existing code.
- Complex infrastructure.
- Complex system interactions.
- Requirement misunderstanding.
- Incorrect requirements.
- Unexpected physical/environmental conditions.

Lecture Steve McConnell ki *Code Complete* ke reference se average 15–50 bugs per 1,000 lines of code ka figure mention karta hai. Is figure ko universal guarantee nahi samajhna; lecture ka point hai ki defects normal engineering reality hain.

## 3.2 Error-prone language constructs — testing hotspots

### A. Floating-point numbers

Real numbers infinite hain, lekin computer floating-point representation finite hoti hai. Isliye floating-point numbers approximate hote hain.

Problems:
- Direct equality comparisons unreliable ho sakti hain.
- Very large/small values par precision behaviour change hota hai.
- Repeated calculations error accumulate kar sakti hain.

### 🎓 COURSE STORY — Patriot missile

Lecture Patriot missile system ka example deta hai. Small floating-point timing error system ko days tak run karne par accumulate hua, aur incoming missile track karne mein failure hua; loss of life ka impact mention hota hai.

**Lesson:** Small precision error long-running system mein serious ban sakta hai.

**Testing ideas:** Boundary magnitudes, repeated calculations, precision tolerance, long-duration behaviour.

### B. Pointers and memory management

C/C++ mein:
- `malloc()` se memory allocate.
- `free()` se memory release.

Potential problems:
- Memory ownership wrong handle karna.
- Dangling pointer — pointer invalid/released memory ko refer kare.
- Memory free na karna — memory leak; application memory consume karti rahe.

Java mein manual `malloc/free` same way nahi, lekin unused objects ke references retain karne se memory usage grow ho sakta hai.

### C. Parallelism / concurrency

Multiple threads logically/physically concurrent execute karte hain. Shared memory access ka order timing ke hisaab se vary ho sakta hai.

**Race condition:** Different execution order se result change ho sakta hai.

**Deadlock:** Thread A resource B ka wait kar raha, Thread B resource A ka — dono progress nahi kar paate.

Instructor note: concurrency bugs rare timing conditions mein appear ho sakte hain, isliye repeated runs aur careful test design important.

### D. Numeric limits and boundaries

Instructor ise extremely common mistake area batate hain.

Examples:
- Buffer 32 ka hona tha, 31 bana.
- Loop 99 par stop hona tha, 100 tak chala gaya.
- Requirement `above 10,000` thi, code `at or above 10,000` kar gaya.
- Integer maximum value ke paas arithmetic overflow/failure.

**Off-by-one error** = boundary/position ek unit se wrong.

### E. Interrupts

Embedded software mein external hardware event program ke normal flow ko interrupt kar sakta hai. Interrupt ke baad jab execution resume hota hai, environment/state change ho chuka ho sakta hai. Wrong handling se bugs aa sakte hain.

### F. Complex Boolean expressions

Example:
```text
(a AND b) OR (c AND d AND e)
```

Complex conditions mein true/false combinations mentally reason karna difficult ho sakta hai. Wrong branch execute ho sakta hai.

### G. Type conversions / casts

Integer ↔ floating-point conversion mein:
- Decimal precision lose ho sakti hai.
- Value truncate/round ho sakti hai.
- Large floating-point value integer range se bahar ja sakti hai.
- Overflow/failure ho sakta hai.

## 3.3 Module-level hotspot — 80/20 rule

Instructor testing/debugging ke liye 80/20 rule ka reference dete hain: roughly 20% modules mein 80% bugs ho sakte hain. Ye rule of thumb hai, fixed mathematical law nahi.

Possible reasons:
- Module system ke liye central/critical ho.
- Logic complex ho.
- New/junior developers ne likha ho.
- Module frequent changes se guzarta ho.

**Practical lesson:** Initial testing aur production defects ka feedback use karke identify karo ki kaunse modules repeatedly problem de rahe hain. Maintenance cycle mein un areas par extra attention do.

### ⭐ INTERVIEW ANSWER — Where should testing focus?

“Testing should focus on areas where defects are more likely. Common risk areas include floating-point calculations, memory management, concurrency, numeric boundaries, interrupts, complex Boolean expressions and type conversions. At system level, defect history can reveal that a small subset of modules contains a large proportion of defects, so testing effort should adapt based on evidence.”

---

# 4. 🎓 LECTURE 4 — How We Test: Systematic Principles

Instructor five questions mein se **HOW** par focus karte hain. Lecture six important principles discuss karta hai.

## 4.1 Divide and Conquer

Everything ek saath test karna difficult hai. Testing ko multiple abstraction levels mein divide karo:
- Unit.
- Integration.
- System.

Test purpose ke hisaab se bhi divide karo:
- Well-formedness/memory safety.
- Performance.
- Conformance to requirements.
- Scalability.

Aur testing techniques bhi purpose ke hisaab se select karo. Ek technique jo memory-safety bug find karti hai, zaroori nahi ki requirement conformance bhi prove kare.

**Mentor example:** API unit tests response transformation verify kar sakte hain; integration tests database/API interaction; system tests complete user journey.

## 4.2 Visibility

Test input system mein execute ho gaya, lekin kya hum uska effect observe kar pa rahe hain?

Instructor ka concern:
- Input code path execute kar sakta hai.
- Statement coverage mark ho sakti hai.
- Lekin input internal state mein store hokar output tak propagate hi na ho.
- Tester ko result visible nahi hota.

Visibility improve karne ke liye:
- Observable outputs.
- Useful logs.
- State inspection/test hooks where appropriate.
- Distributed systems mein correlation IDs/tracing.

**Important:** Sirf code execute hona enough nahi; meaningful outcome observe aur assess karna bhi zaroori hai.

## 4.3 Repeatability

Ideal tests consistently pass ya fail hone chahiye. Flaky tests woh hain jo kabhi pass, kabhi fail karte hain without a meaningful code change.

Instructor examples:
- Java `Set` ka iteration order deterministic nahi ho sakta; test order assume kar le toh kabhi fail.
- Database/filesystem inconsistent state.
- Parallel execution/timing.
- Environment differences.

Nuance:
- Kabhi test flaky hota hai.
- Kabhi underlying program mein genuine concurrency defect hota hai jo intermittent failure produce karta hai.
- Dono ko same cheez nahi samajhna chahiye.

**SDET checklist:**
- Test data isolated?
- Order dependency?
- Shared mutable state?
- Time/sleep dependency?
- Network/environment dependency?
- Cleanup reliable?
- Randomness controlled?

## 4.4 Redundancy / Defense in Depth

Verification methods imperfect hain; har technique kuch errors miss kar sakti hai. Isliye multiple complementary techniques use karo.

Example:
- Unit tests.
- API/integration tests.
- UI/system tests.
- Static analysis.
- Code review.
- Security/performance checks.

Same exact check ko blindly duplicate karna goal nahi. Different techniques different failure classes expose kar sakti hain.

## 4.5 Feedback

Initial testing se learn karo:
- Kaunse modules defect-prone hain?
- Kaunsi bug classes repeat hoti hain?
- Kaunsi test techniques useful rahi?
- Kaunse tests unreliable hain?

Phir testing strategy update karo. Scientific software mein precision issues; highly concurrent software mein concurrency errors par focus badh sakta hai.

## 4.6 Logging — visibility ka practical partner

Large systems mein input multiple services se pass hota hai. Tester har internal component directly observe nahi kar sakta. Logging se information flow aur expected behaviour trace karna easier hota hai.

**SDET example:** Request ID/correlation ID ke through UI request ko API logs aur downstream service logs se trace karna.

### ⭐ INTERVIEW ANSWER — Testing principles

“The lecture highlights divide and conquer, visibility, repeatability, redundancy and feedback. We break testing into appropriate levels and purposes, ensure test outcomes are observable, keep tests deterministic, use complementary verification techniques, and improve the test strategy using defect and execution feedback.”

---

# 5. 🎓 LECTURE 5 — V-Model of Software Development

## 5.1 V-Model ka basic idea

V-Model software development phases aur corresponding testing phases ko pair karta hai. Left side par requirements/design progressively detailed hote hain; right side par corresponding tests execute hote hain.

### V-Model map

```text
USER REQUIREMENTS  --------------------> VALIDATION / ACCEPTANCE TESTING
       ↓                                           ↑
SYSTEM SPECIFICATION --------------------> VERIFICATION / SYSTEM TESTING
       ↓                                           ↑
ARCHITECTURE / HIGH-LEVEL DESIGN --------> SYSTEM INTEGRATION TESTING
       ↓                                           ↑
DETAILED DESIGN -------------------------> MODULE / MODULE INTEGRATION TESTING
       ↓                                           ↑
IMPLEMENTATION / CODE -------------------> UNIT TESTING
```

## 5.2 Left side ke phases

### User Requirements
User ko system se kya chahiye — natural language mein documented.

### Specification / System Specification
System user requirements meet karne ke liye exactly kya karega — recorded technical understanding.

### Architecture / Architectural Design
High-level decisions:
- Build vs buy?
- Client-server ya another architecture?
- Existing enterprise systems ke saath integration?
- Team/resources/expertise available?
- System ko subsystems/components mein kaise divide karna?

### Detailed Design
Subsystems/modules/classes organize karna. Lecture class diagrams aur sequence diagrams ka reference deta hai. Is stage par design implementation developers ko handoff kiya ja sakta hai.

### Implementation
Actual code likhna.

## 5.3 Right side ke corresponding test levels

| Development phase | Corresponding test |
|---|---|
| User requirements | Validation / Acceptance testing |
| System specification | Verification / System testing |
| Architecture | System integration testing |
| Detailed design | Module testing / Module integration testing |
| Implementation | Unit testing |

**Core idea:** Left side ka har phase right side par test planning ko inform karta hai. Testing sirf coding complete hone ke baad start nahi hoti; test planning early development se shuru hoti hai.

## 5.4 V-Model criticism and modern use

Instructor kehte hain V-Model relatively simple hai, lekin useful model hai. Agile methodologies mein small Vs repeatedly use ho sakte hain: small increments, frequent testing, testing at every phase.

> 🔵 **Clarification:** V-Model ka matlab ye nahi ki project ke end tak testing wait karti hai. Early phases mein test planning/design hoti hai; execution corresponding stage par hoti hai.

### ⭐ INTERVIEW ANSWER

“V-Model pairs each development phase with a corresponding testing phase. Requirements map to acceptance/validation testing, system specification to system verification, architecture to system integration testing, detailed design to module testing, and implementation to unit testing. Its key benefit is that testing is planned early rather than treated as an activity that starts only after coding.”

---

# 6. 🎓 LECTURE 6 — Verification and Validation inside the V-Model

## 6.1 Validation — user's perspective

Validation asks:
- Does the user like the product?
- Does it solve the user's need?
- Is it usable?
- Is performance acceptable?
- Is it secure enough for the intended use?

## 6.2 Verification — written standard/specification

Verification checks whether the system conforms to:
- User requirements as documented.
- System specification that constrains the implementation.

Simple framing:
- Validation: Are we building the right product?
- Verification: Are we building the product right?

## 6.3 🎓 COURSE STORY — Boat on a car rack

Instructor ek boat example dete hain.

User requirement: **Ek person boat ko car rack par rakh sake.**

Possible solution: Har boat ke saath ek crane de do jo boat ko car par lift kar de. Technically ek person boat load kar sakta hai, lekin user ki need ke liye ye practical/acceptable solution shayad nahi.

Solution specifications define ki jaati hain:
- Boat itni light ho ki one person lift kar sake.
- Handles diye jaayein.
- Car rack easy placement ke liye designed ho.

Lekin specification mein word **“easily”** tricky hai. “Easily” ko quantitatively define kaise karoge? User se validation mein pooch sakte ho, lekin verification ke liye measurable criterion banana hoga.

Final validation: Boat real users ko do aur observe karo ki average one person actually boat ko rack par load kar pata hai ya nahi.

### 🧠 MENTOR EXPLAINS — software example

User says: “Mujhe easy checkout chahiye.”

Specification:
- Checkout 3 steps se zyada nahi.
- Payment form clear validation show kare.
- User order summary review kar sake.

Verification: Steps count, validation behaviour, summary correctness check.

Validation: Real users checkout complete kar pa rahe hain? Confused toh nahi? “Easy” feel hota hai?

**Lesson:** Written requirements meet karna zaroori hai, lekin user need/satisfaction alag se validate karni hoti hai.

### ⭐ INTERVIEW ANSWER

“Verification checks conformance to documented specifications, while validation evaluates the product from the user's perspective. The boat example shows that a solution can technically satisfy a requirement but still be impractical for the user. Vague words such as ‘easy’ need measurable acceptance criteria, and real user evaluation may still be required.”

---

# 7. 🎓 LECTURE 7 — Structural Testing / Code Coverage

## 7.1 Black-box vs White-box recap

- **Black-box:** code internals ki knowledge ke bina expected behaviour/requirements test karna.
- **White-box:** code structure ko dekhkar tests design karna.

Code review, inspection aur pair programming bhi lecture ke framing mein white-box activities ho sakti hain.

## 7.2 Structural Testing kya hai?

Structural Testing white-box testing ka form hai. Lecture is video mein **Code Coverage** par focus karta hai.

Question:
- Kya har line execute hui?
- If statement true bhi hua aur false bhi?
- Kya test cases code structure ko sufficiently exercise karte hain?

## 7.3 Statement Coverage

**Statement coverage:** test execution ke dauran har executable statement at least once run hona chahiye.

Example:

```python
def discount(price, is_member):
    if is_member:
        price = price * 0.9
    return price
```

Test:
```python
def test_member_discount():
    assert discount(100, True) == 90
```

Ye `if` body execute karta hai. Lekin `is_member=False` branch test nahi hui.

### Important

Statement coverage high hone ka matlab logic fully correct prove nahi hota. Sirf statements execute hue hain. Wrong expected result, missing scenario ya incorrect business rule still ho sakta hai.

## 7.4 Decision/Branch Coverage — lecture ka next-step idea

Instructor `if` condition true aur false dono taraf execute karne ka question uthate hain. Branch/decision coverage ka idea hai decision outcomes ko exercise karna.

Example:
- `is_member=True`
- `is_member=False`

Dono outcomes test karna.

## 7.5 Safety-critical standards example — DO-178B

Lecture aviation standard DO-178B ka reference deta hai. Software criticality ke basis par statement, decision aur modified condition/decision coverage tak requirements ho sakti hain. Exact rigor software criticality par depend karti hai.

## 7.6 Structural coverage ke challenges

Instructor challenges list karte hain:
- Modules ke across procedure calls.
- Inter-procedural data flow.
- Object-oriented behaviour.
- Polymorphism se program flow complex ho sakta hai.
- Regression testing mein code structure change hone par prior coverage tests invalid/insufficient ho sakte hain.

## 7.7 Regression testing and coverage

Regression testing = modified program par existing test suite rerun karna taaki ensure ho ki old behaviour break nahi hua.

White-box tests code structure par based hote hain; structure change hone par old coverage evidence re-evaluate karna pad sakta hai.

## 7.8 100% coverage always possible/practical nahi

Lecture kehta hai:
- Kuch statements rare/random events par depend karte hain.
- Kuch paths practically unreachable ya difficult to simulate ho sakte hain.
- Har uncovered statement ka formal explanation banana impractical ho sakta hai.
- Isliye adequacy metrics/scores use ho sakte hain; lecture 95% statement coverage ko possible example ke roop mein discuss karta hai.

> 🔴 **Critical interview point:** 100% code coverage ≠ 100% bug-free software. Coverage tells you what code was executed, not whether assertions were meaningful or requirements fully correct.

### ⭐ INTERVIEW ANSWER — Code coverage

“Structural testing is a white-box approach that uses program structure to guide testing. Statement coverage checks whether every statement executes at least once. Decision or branch coverage checks decision outcomes. Coverage helps identify unexecuted code, but it does not prove correctness because tests may execute code without checking the right behaviour.”

---

# 8. 🎓 LECTURE 8 — Mutation Testing

## 8.1 Mutation testing kyun chahiye?

Instructor ka opening thought:
“All tests passed? Great — but are the tests actually good?”

Dijkstra ka idea lecture mein quote hota hai: program testing bugs ki presence show kar sakti hai, absence prove nahi kar sakti.

Toh question hai: **Hamare test suite ki quality/adequacy kaise evaluate karein?**

Mutation testing isi question ko address karta hai.

## 8.2 Mutation testing ka process

1. Original program lo.
2. Code mein ek small artificial fault introduce karo.
3. Modified program ko **mutant** kehte hain.
4. Existing test suite mutant par run karo.
5. Agar test fail hota hai, mutant **killed**.
6. Agar all tests pass, mutant **survived**.
7. Surviving mutant ke location par review karo — shayad missing test case hai.

## 8.3 🎓 COURSE STORY — arithmetic operator mutation

Instructor example:
```text
delta = newGuess - sqrt
```

Mutation operator subtraction ko addition se replace kar sakta hai. Agar test suite ka output is change se different hota hai aur koi test fail hota hai, mutant killed.

Other mutation ideas:
- Arithmetic operator swap.
- Boolean condition swap.
- Off-by-one condition change.
- Same type ke variables swap.

Mutation aisa hona chahiye ki code compile/run kar sake; syntax error create karna useful mutant nahi.

## 8.4 Triangle example se samjho

Original:
```java
a + b > c
```

Mutant:
```java
a + b >= c
```

Only normal valid case `3,4,5` test karoge toh both pass. Test suite mutant ko detect nahi karegi.

Boundary case `1,2,3`:
- Original returns false.
- Mutant returns true.

Assertion fail hui → mutant killed.

## 8.5 Mutation adequacy score

Lecture formula ka idea:

\[
Mutation\ Score =
\frac{Killed\ Mutants}{Total\ Mutants - Equivalent\ Mutants}
\times 100
\]

- **Killed mutants:** At least one test failed against mutant.
- **Equivalent mutants:** Mutant code change ke bawajood observable behaviour original jaisa hi hai.
- **Survived mutants:** Tests ne mutant ko detect nahi kiya.

Equivalent mutants ko denominator se exclude karte hain, kyunki unhe behavioural difference ke through kill karna possible nahi ho sakta.

## 8.6 Mutation testing ki interpretation

High mutation score indicate kar sakta hai ki tests plausible code changes ke against sensitive hain. Lekin:
- High score absolute correctness proof nahi.
- Mutant quality matters.
- Equivalent mutants handling matters.
- Mutation tools ke generated changes meaningful hone chahiye.

### ⭐ INTERVIEW ANSWER — Mutation testing

“Mutation testing evaluates the adequacy of a test suite by making small changes to the program, called mutations, and running the tests against those modified versions. If a test fails, the mutant is killed. If all tests pass, the mutant survives and may indicate a gap in the test suite. Mutation score is calculated using killed mutants while excluding equivalent mutants from the denominator.”

**Keywords:** mutant, mutation operator, killed mutant, survived mutant, equivalent mutant, mutation score, test adequacy.

---

# 9. 🔗 Module 2 — Concepts ko ek saath connect karo

| Concept | Tumhe kya question poochna chahiye? |
|---|---|
| Dependability | Kya user software ki service par rely kar sakta hai? |
| Fault/Error/Failure | Root cause, internal wrong state aur visible failure kya hain? |
| Testing principles | Hum quality goals aur testing strategy kaise decide karte hain? |
| Error-prone constructs | Code mein likely mistake areas kaunse hain? |
| Divide and conquer | Testing ko levels/purposes mein kaise divide karein? |
| Visibility | Test ka effect observe kar pa rahe hain? |
| Repeatability | Test har run mein predictable hai? |
| Redundancy | Different techniques se defence in depth hai? |
| Feedback | Past defects se strategy improve ho rahi hai? |
| V-Model | Development phase ke saath corresponding testing kya hai? |
| Structural testing | Code statements/decisions execute hue? |
| Mutation testing | Tests wrong code change ko detect kar paate hain? |

---

# 10. ⭐ Module 2 — High-priority interview questions

1. Explain fault, error and failure with a real example.
2. What is the difference between reliability and availability?
3. What is MTBF and MTTR?
4. Differentiate safety and reliability.
5. Explain fault avoidance, fault tolerance, error removal and error forecasting.
6. What is the difference between principles, techniques, methodologies and tools?
7. What are the five testing analysis questions: What, Where, When, Who and How?
8. Why are floating-point calculations error-prone?
9. What is a race condition? What is deadlock?
10. What is an off-by-one error?
11. Explain the 80/20 rule in defect distribution.
12. Explain divide and conquer in testing.
13. What makes a test observable?
14. What is a flaky test? Give causes.
15. What is defense in depth in testing?
16. Explain V-Model and its phase mappings.
17. Verification vs validation in the V-Model?
18. What is structural testing?
19. Difference between statement and branch coverage?
20. Does 100% code coverage mean bug-free software?
21. What is regression testing?
22. What is mutation testing?
23. What are killed, survived and equivalent mutants?
24. How is mutation score calculated?

---

# 11. 🧠 Practice scenarios

## Scenario A — Checkout sometimes charges twice

A payment request is retried when network response is delayed. Sometimes duplicate charge happens.

- Dependability chain mein fault/error/failure identify karo.
- Which testing purpose is relevant?
- What state/timing conditions should be exercised?

## Scenario B — Test passes 9 times and fails once

A test sometimes fails because list items appear in a different order.

- Is this likely product defect or test design issue?
- Which testing principle is being violated?
- How will you make the test deterministic?

## Scenario C — 100% statement coverage

A team reports 100% statement coverage, but a discount calculation bug reaches production.

- How can this happen?
- What does statement coverage not prove?
- Which additional test strategy could assess test adequacy?

## Scenario D — Vague requirement

Requirement says: “Search should be fast and easy.”

- What should be clarified?
- Which parts can be verified quantitatively?
- Which parts need validation with users?

## Scenario E — Surviving mutant

A mutation changes `>` to `>=`, but all tests pass.

- What type of test case might be missing?
- Why is the boundary input useful?

---

# 12. ✅ Answer guide

- **A:** Fault may be missing idempotency/incorrect retry handling; internal duplicate state is error; user charged twice is failure. Test retries, timeouts, duplicate requests and payment state transitions.
- **B:** If ordering is unspecified, test may be incorrectly assuming order. Repeatability issue. Sort expected/actual or assert order-independent membership, depending on requirement.
- **C:** Statement execution doesn't prove assertions are meaningful or all decision outcomes/requirements are checked. Mutation testing can evaluate whether tests detect injected faults.
- **D:** Define measurable response-time threshold, search-result correctness and usability acceptance criteria. Performance can be verified against thresholds; ease-of-use needs user validation.
- **E:** Equality boundary test. `x == boundary` distinguishes `>` from `>=`.

---

# 13. 📊 Module 2 — Study priority & completion criteria

| Topic | Difficulty | Suggested study time | Priority |
|---|---|---:|---|
| Dependability + fault/error/failure | Medium | 45–60 min | Must know |
| Four dependability approaches | Medium | 30–40 min | Must know |
| Reliability/availability/safety etc. | Medium | 45–60 min | Must know |
| Five testing questions + quality process | Easy–Medium | 30–40 min | Must know |
| Error-prone constructs | Hard | 60–90 min | Must know |
| Testing principles (How) | Medium | 45–60 min | Must know |
| V-Model | Medium | 35–45 min | Must know |
| V&V boat story | Easy–Medium | 30–40 min | Must know |
| Structural testing/coverage | Hard | 60–75 min | Must know |
| Mutation testing | Hard | 60–75 min | Must know |

**Estimated focused study:** 8–11 hours, excluding additional coding practice.

## Module completion criteria

Module 2 complete tab hoga jab tum:
- Fault → error → failure chain apne example se explain kar sako.
- Reliability, availability, safety, integrity aur maintainability differentiate kar sako.
- MTBF/MTTR se availability calculate kar sako.
- Five testing questions explain kar sako.
- Common error-prone code constructs identify kar sako.
- Divide and conquer, visibility, repeatability, redundancy aur feedback explain kar sako.
- V-Model ke phase pairs draw kar sako.
- Boat story se verification/validation explain kar sako.
- Statement coverage vs branch coverage distinguish kar sako.
- Mutation score, killed/survived/equivalent mutants explain kar sako.

> 💚 **Mentor rule:** Sirf definitions yaad nahi karni. Har concept ke saath ek real scenario sochna hai. Interview mein definition + example + practical implication doge, tab answer strong lagega.
