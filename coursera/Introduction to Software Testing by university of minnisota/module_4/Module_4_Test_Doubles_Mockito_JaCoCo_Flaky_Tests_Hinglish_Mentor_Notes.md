# Module 4 — Unit Testing Ecosystem: Test Doubles, Mockito, JaCoCo & Flaky Tests
## Complete Hinglish Mentor Notes | Introduction to Software Testing

> **Learning mode:** Paid-mentor style, concept-first, practical, interview-ready.  
> **Source basis:** Module 4 ZIP ke 5 lecture transcripts + CoffeeMaker assignment projects + CoffeeMaker requirements PDF + Gradle setup PDF + supplied Java source files.  
> **Important:** `COURSE SOURCE` labels ka matlab instructor/source material mein directly covered content. `MENTOR EXPLANATION` aur `SDET CONNECTION` labels extra teaching hain, taaki concept practical QA/SDET work se connect ho. Source mein jo cheez nahi di gayi, use course fact bana kar present nahi kiya gaya.

---

# 0. Module 4 ka complete overview

## Is module ka central idea kya hai?

Unit testing ka matlab sirf kisi method ko call karke expected output assert kar dena nahi hai. Real applications mein ek class akeli kaam nahi karti. Woh database, file system, external API, payment service, email service, message queue, ya kisi doosri class par depend kar sakti hai.

Agar hum unit test ke time har real dependency ko use karenge, to tests:

- slow ho sakte hain;
- external service down hone par fail ho sakte hain;
- shared database ke data change hone se inconsistent ho sakte hain;
- real side effects create kar sakte hain;
- dependencies abhi develop na hui hon to likhe hi nahi ja sakte;
- aur kabhi-kabhi flaky ban sakte hain.

Isliye hum **Test Doubles** use karte hain — real dependency ke lightweight substitutes.

Module 4 ka flow:

| Lesson | Topic | Aap kya seekhenge |
|---|---|---|
| 1 | Test Doubles overview | Dependency ko replace/observe karne ki need |
| 2 | Input Test Doubles | Dummy, Stub, Fake aur Mockito se stubbing |
| 3 | Output Test Doubles | Mock, Spy, `verify()`, call count, `InOrder` |
| 4 | Test Suite Adequacy | JaCoCo, instruction/line/branch coverage |
| 5 | Flaky Tests | Non-determinism, concurrency, environment, robust assertions |

## Difficulty aur estimated time

| Topic | Difficulty | Focused learning time |
|---|---:|---:|
| Test Doubles overview | Easy–Medium | 35–45 min |
| Dummy / Stub / Fake | Medium | 60–75 min |
| Mockito stubbing | Medium | 60–90 min |
| Mock / Spy / verify / InOrder | Medium–Hard | 75–90 min |
| JaCoCo coverage | Medium | 60–75 min |
| Flaky tests | Hard | 75–90 min |
| CoffeeMaker assignment analysis | Hard | 2–4 hours |
| Revision + interview practice | Medium | 60 min |

**Total suggested learning effort:** approximately 8–11 focused hours, assignment implementation ke time ko alag rakhein.

---

# 1. Unit Testing Ecosystem aur Test Doubles

<badge label="COURSE SOURCE" color="success"/> <badge label="Difficulty: Easy–Medium" />

## 1.1 WHY — Test Doubles ki zarurat kyun padti hai?

Imagine karo hum ek `EmployeeTravelScheduler` class test kar rahe hain. Iska kaam employee ke liye flights find karna aur company rules ke according suitable flight select karna hai.

Lekin flight find karne ke liye class ko `AirlineTravelService` chahiye. Ye external service ho sakti hai.

Ab problems dekho:

1. Real airline service available na ho.
2. Service abhi doosri team develop kar rahi ho.
3. Real API call expensive ho ya rate-limited ho.
4. Test ke time actual flight book ho gayi to unwanted side effect ho sakta hai.
5. External service down ho to hamara unit test bhi fail ho jayega.
6. Shared database/API data kisi aur process se change ho sakta hai.

**Mentor explanation:** Hum jis class ka behaviour test karna chahte hain, uski correctness ko uske external dependency ke health/status se unnecessarily tie nahi karna chahte.

Agar `EmployeeTravelScheduler` ki logic correct hai, lekin airline API down hai, to unit test ko fail nahi hona chahiye. Unit test mein airline service ka controlled substitute dena better hai.

## 1.2 WHAT — Test Double kya hota hai?

**COURSE SOURCE:** Test Double ek lightweight version/substitute hota hai us component ka jiske saath System Under Test (SUT) interact karta hai.

Movie example: Indiana Jones ke dangerous scene mein actor ke badle stunt double action karta hai. Test Double bhi testing mein real dependency ki jagah leta hai.

### Important terminology

| Term | Simple meaning | Main role |
|---|---|---|
| SUT (System Under Test) | Jis class/component ko test kar rahe hain | Target |
| Dependency / Collaborator | Jis doosre component ko SUT use karta hai | External collaborator |
| Test Double | Dependency ka test-time substitute | Isolation/control |
| Test Stub | Controlled input/response deta hai | Input provide karna |
| Mock Object | Interactions verify karne mein help karta hai | Interaction observation |
| Spy Object | Real object ko wrap karke interactions observe karta hai | Real object monitoring |

## 1.3 Test Doubles banane ke reasons

**COURSE SOURCE ke reasons:**

- Real component incomplete ya unavailable ho sakta hai.
- Real component ko construct karna expensive ho sakta hai.
- Component kisi doosri team/company ke ownership mein ho sakta hai.
- Tests ke side effects avoid karne hote hain.
- Flaky tests ka risk kam karna hota hai.
- Sirf output nahi, SUT aur collaborator ke beech interactions bhi inspect karne hote hain.

### Real-world SDET example

Suppose `OrderService` order place karte waqt ye kaam karta hai:

1. Inventory service se stock check.
2. Payment service se payment charge.
3. Email service se confirmation send.

Unit test mein real payment charge karna dangerous hai. Real email bhejna bhi unnecessary hai.

Hum controlled test doubles use karke verify kar sakte hain:

- Stock available ho to payment method call hua?
- Payment successful ho to email send method call hua?
- Payment failed ho to confirmation email send nahi hua?
- Payment service ko correct amount/order ID pass hua?

**Important:** Test Double ka objective real production service ko fully reproduce karna nahi hota. Objective hai SUT ko controlled conditions mein test karna.

---

# 2. Input Test Doubles — Dummy, Stub aur Fake

<badge label="COURSE SOURCE" color="success"/> <badge label="Difficulty: Medium" />

## 2.1 Three input doubles ka difference

Instructor in teen types ko functionality aur implementation effort ke perspective se explain karte hain.

| Type | Kya karta hai? | Kab use karenge? |
|---|---|---|
| Dummy Object | Required parameter ke liye placeholder | Object chahiye, lekin test mein uska role irrelevant hai |
| Test Stub | Specific input par predefined response deta hai | SUT ko controlled data/response chahiye |
| Fake Object | Real dependency ka lightweight working implementation | Real dependency expensive ho, e.g. in-memory DB |

### A. Dummy Object

**COURSE SOURCE:** Dummy object aisi value hai jo method ko parameter ke roop mein deni zaruri hai, lekin test ke liye uski actual functionality matter nahi karti.

Example: Kisi method ka signature hai:

```java
public boolean schedule(Employee employee, String region)
```

Aap kisi particular branch ko test kar rahe ho jahan employee ki details use hi nahi ho rahi, lekin method null accept nahi karta. Aap ek dummy `Employee` pass kar sakte ho.

Mockito example:

```java
Employee employee = mock(Employee.class);
```

Course ke example mein Mockito se create kiya gaya mock object dummy role play kar raha hai.

**Important distinction:** Mockito ka `mock()` method object create karta hai. Us object ka *testing role* dummy, stub, ya mock ho sakta hai. Role aur creation mechanism alag concepts hain.

### B. Test Stub

**COURSE SOURCE:** Stub ek lightweight/special-purpose object hai jo kuch selected inputs ke liye predefined outputs return karta hai.

Example:

```java
when(airlineService.findFlights(any(Date.class)))
    .thenReturn(flights);
```

Ab SUT jab `findFlights()` call karega, to real airline API hit nahi hogi. Stub controlled `flights` list return karega.

Stub se hum test kar sakte hain:

- flights available hain;
- flights empty hain;
- service specific date par result deti hai;
- SUT returned flights ko price ke order mein sort karta hai.

### C. Fake Object

**COURSE SOURCE:** Fake object real dependency ka lightweight implementation hota hai.

Instructor ka example: External database ke badle in-memory database use karna.

- Production DB: external server, network, credentials, setup.
- Fake/in-memory DB: test process ke andar lightweight data store.

Fake object kuch real functionality provide karta hai, lekin simplified form mein.

**Mentor distinction:** Fake aur Stub ko mix mat karna.

- Stub ka focus: predefined response.
- Fake ka focus: simplified but working implementation.

Example:
- Stub: `getUser(10)` hamesha fixed user return kare.
- Fake repository: `save()` aur `findById()` actual in-memory map par kaam karein.

## 2.2 Course story — Employee Travel Scheduler

**COURSE SOURCE:** Instructor employee travel scheduler ka example use karte hain.

SUT: `EmployeeTravelScheduler`

Dependency: `AirlineTravelService`

Scheduler ka rule:
- Airline service se flights fetch karo.
- Flights ko price ke basis par sort karo.
- $2,000 se expensive flights ko remove karo.

Testing challenge: Real airline service use nahi karni. Humein controlled flight data chahiye.

Isliye stub service create karte hain aur predefined flight list return karwate hain.

### Story ko samjho

Original list:

| Flight | Price |
|---|---:|
| Flight A | $2,500 |
| Flight B | $1,200 |
| Flight C | $1,800 |

Expected scheduler output:
1. Flight B — $1,200
2. Flight C — $1,800

Flight A exclude ho jayegi kyunki price $2,000 se zyada hai.

Is test mein do cheezein verify hongi:
- sorting correct hai;
- expensive flight filter ho gayi.

## 2.3 Mockito se dummy object banana

**COURSE SOURCE:** Mockito Java unit testing ke liye mocking framework hai. Course mein Gradle dependency management ke through Mockito use hota hai.

Example:

```java
Employee employee = mock(Employee.class);
```

Mockito object create karta hai. Course explanation ke according unconfigured dummy object ke fields default/zero-like values lete hain:

| Field type | Default-like value described in lesson |
|---|---|
| Object reference / String | `null` |
| Integer / int | `0` |
| Floating point | `0.0` |

**Caution:** Ye simplified course explanation hai. Mockito mocks ko normal POJO objects ki tarah fields initialized hone ki assumption se use mat karo. Mock ke method calls ka behaviour Mockito control karta hai.

## 2.4 Mockito stubbing — `when()` aur `thenReturn()`

Basic pattern:

```java
when(mockObject.methodName(arguments))
    .thenReturn(expectedValue);
```

Meaning:
- `when(...)`: kis method invocation ko configure karna hai.
- `thenReturn(...)`: us invocation par kya response milega.

### Example: Airline service stub

```java
AirlineTravelService stubService =
    mock(AirlineTravelService.class);

List<Flight> flights = new ArrayList<>();
flights.add(expensiveFlight);
flights.add(cheapFlight);

when(stubService.findFlights(any(Date.class)))
    .thenReturn(flights);
```

**Line-by-line:**

1. `mock(...)` — real airline service ki jagah Mockito mock create.
2. `flights` — controlled test data.
3. `when(...)` — service ke `findFlights()` call ko configure karna.
4. `any(Date.class)` — kisi bhi Date argument ke liye match.
5. `thenReturn(flights)` — matching call par predefined list return.

### Consecutive responses

Course mein same method ke repeated calls par different responses return karne ka example diya gaya:

```java
when(stubService.findFlights(any(Date.class)))
    .thenReturn(flights)
    .thenReturn(new ArrayList<Flight>());
```

Expected behaviour:
- First matching call → `flights`.
- Second matching call → empty list.

Use case: First request par flights available, next request par no flights.

### Specific argument matching

Course mein `any(Date.class)` aur particular date/time ke saath matching ka contrast dikhaya gaya.

Concept:
- Broad matcher: any Date.
- Specific argument: selected date/time.
- Agar test different date pass kare aur stub sirf ek specific date ke liye configured ho, expected stub response match nahi karega.

**Important:** Mockito argument matching ke advanced patterns ke liye instructor Hamcrest ka reference dete hain. Transcript mein matcher language ka detailed tutorial nahi hai; isliye yahan uska deep syntax course content ke roop mein add nahi kiya gaya.

## 2.5 Static imports — Course ka additional concept

Instructor `import static` ka meaning bhi explain karte hain.

Without static import:

```java
org.mockito.Mockito.mock(Employee.class);
```

With static import:

```java
import static org.mockito.Mockito.*;

Employee employee = mock(Employee.class);
```

Static import se static methods ko class prefix ke bina call kar sakte hain.

JUnit assertions mein bhi same idea:

```java
import static org.junit.Assert.assertTrue;
```

Then:

```java
assertTrue(condition);
```

**Common mistake:** Static import ka matlab object create karna nahi hota. Ye sirf static method ko shorter syntax mein access karne deta hai.

---

# 3. Output Test Doubles — Mocks aur Spies

<badge label="COURSE SOURCE" color="success"/> <badge label="Difficulty: Medium–Hard" />

## 3.1 WHY — Sirf return value test karna enough nahi hota

Har method useful return value nahi deta. Kuch methods `void` return karte hain.

Example:

```java
paymentService.charge(amount);
emailService.sendConfirmation(orderId);
auditService.recordEvent(event);
```

In methods ka return value nahi bhi ho sakta. Lekin humein verify karna hai ki:
- method call hua ya nahi;
- correct arguments ke saath call hua;
- kitni baar call hua;
- calls correct order mein hue ya nahi.

**COURSE SOURCE:** Testing sirf function output check karna nahi hai. Kabhi-kabhi interactions check karna bhi zaruri hota hai.

## 3.2 Mock Object

Mock object fake object hota hai jise Mockito se construct karke interactions observe kiye ja sakte hain.

Mock se questions:
- `confirmFlight()` call hua?
- `bookFlight()` call hua?
- `bookFlight()` kitni baar call hua?
- Correct flight object pass hua?
- Confirm hone se pehle booking attempt to nahi hui?

## 3.3 Spy Object

**COURSE SOURCE:** Spy real object ko wrap karta hai, taaki us object ke saath SUT ke interactions observe kiye ja sakein.

Example: Real `ArrayList` create karo, spy se wrap karo, normal list operations perform karo, phir verify karo `add()` kitni baar call hua.

### Mock vs Spy

| Point | Mock | Spy |
|---|---|---|
| Underlying object | Mockito-created fake/mock | Existing real object wrapped |
| Real behaviour | Usually default/mock behaviour unless stubbed | By default real object behaviour |
| Primary use | Dependency interactions isolate/verify | Real object interactions monitor |
| Example | Mock `AirlineTravelService` | Spy on `ArrayList` |

**Mentor note:** Spy ke saath real methods execute ho sakte hain. Isliye spy use karte waqt side effects aur object state ko samajhna zaruri hai.

## 3.4 Course story — Airline booking interaction

Instructor ka example:

`EmployeeTravelScheduler` airline service ke saath interact karta hai.

Expected flow:
1. Flight availability confirm karo.
2. Agar flight available hai, tab book karo.
3. Agar flight unavailable hai, booking mat karo.

Do flights:
- Flight 1 → confirmation returns `true`.
- Flight 2 → confirmation returns `false`.

Expected calls:
- `confirmFlight()` → 2 times.
- `bookFlight()` → 1 time.

Is example se output aur interaction testing ka difference samajh aata hai.

### Mockito `verify()`

Basic syntax:

```java
verify(mockObject).methodName(arguments);
```

Example:

```java
verify(stubService, times(2))
    .confirmFlight(any(Flight.class));

verify(stubService, times(1))
    .bookFlight(any(Flight.class), any(PaymentMethod.class));
```

**Meaning:**
- `verify(...)` interaction check karta hai.
- `times(2)` expected invocation count.
- `any(Flight.class)` kisi bhi Flight argument ko accept karta hai.
- Agar actual calls expected count se kam/zyada hue, verification fail hoti hai.

### Course failure example

Instructor expected `confirmFlight()` 3 times, lekin SUT ne sirf 2 baar call kiya. Test failure ka message `TooLittleActualInvocations` tha.

Is failure ka meaning:
- Expected invocations: 3.
- Actual invocations: 2.
- Required interaction missing hai.

**SDET lesson:** Verification failure ko blindly product bug mat samjho. Pehle test expectation aur actual business flow compare karo.

## 3.5 `InOrder` — Call order verify karna

Kabhi invocation count correct hona enough nahi hota.

Example:
- `confirmFlight()` 1 time.
- `bookFlight()` 1 time.

Count correct hai. Lekin agar booking pehle ho gayi aur confirmation baad mein, business rule violate hua.

Mockito `InOrder`:

```java
InOrder inOrder = inOrder(stubService);

inOrder.verify(stubService)
    .confirmFlight(any(Flight.class));

inOrder.verify(stubService)
    .bookFlight(any(Flight.class), any(PaymentMethod.class));
```

Meaning:
1. First verify confirmation call.
2. Then verify booking call.
3. Order wrong hua to verification fail.

**Important:** `InOrder` sirf tab use karo jab sequence business requirement ka part ho. Har test mein exact order assert karna over-specification ho sakta hai.

## 3.6 Spy example — Real ArrayList

Conceptual example:

```java
List<Flight> realFlights = new ArrayList<>();
List<Flight> flightSpy = spy(realFlights);

flightSpy.add(flight1);
flightSpy.add(flight2);

verify(flightSpy, times(2)).add(any(Flight.class));
```

Yahan:
- Real `ArrayList` behaviour available hai.
- `add()` actual list mein elements add karta hai.
- Spy interaction record karta hai.
- `verify()` calls count check karta hai.

## 3.7 Course ka important nuance — One object multiple roles play kar sakta hai

Instructor explain karte hain ki same Mockito-created object:
- Stub role play kar sakta hai: predefined flights return karna.
- Mock role play kar sakta hai: `confirmFlight()` aur `bookFlight()` calls verify karna.

Mockito object ka construction method same ho sakta hai; uska role test ke purpose par depend karta hai.

### Common mistakes

1. **Mock ko real implementation samajhna:** Unstubbed method se real service behaviour expect mat karo.
2. **Only output assert karna:** `void` method ka interaction miss ho sakta hai.
3. **Wrong call count:** Expected count business flow se derive karo.
4. **Unnecessary order verification:** Jab order requirement nahi hai, `InOrder` se brittle test mat banao.
5. **Spy ko harmless samajhna:** Real methods execute hone se real side effects ho sakte hain.
6. **Every dependency mock kar dena:** Jahan real lightweight object suitable hai, wahan unnecessary mocks test ko over-coupled bana sakte hain.

---

# 4. Test Suite Adequacy aur JaCoCo Coverage

<badge label="COURSE SOURCE" color="success"/> <badge label="Difficulty: Medium" />

## 4.1 WHY — Test pass ho rahe hain, par kya testing sufficient hai?

Suppose class mein 100 lines code hain aur aapne 3 test cases likhe. Teeno pass ho gaye.

Kya iska matlab class thoroughly tested hai?

**Nahi.** Ho sakta hai tests sirf happy path execute kar rahe hon. Important conditions, alternate branches, exception paths untouched hon.

Course ka question: **How do we assess the adequacy of a test suite?**

Instructor code structures execute hone ko measure karne ka approach introduce karte hain.

## 4.2 Coverage kya hoti hai?

Coverage ka broad meaning: test suite ke run hone par code ka kitna hissa execute hua.

Course mein focus metrics:

| Metric | Kya measure karta hai? |
|---|---|
| Instruction coverage | Bytecode instructions mein kitne execute hue |
| Line coverage | Source code ki kitni lines execute hui |
| Branch coverage | Conditional branches ke kitne outcomes execute hue |

### A. Instruction coverage

JaCoCo Java bytecode instrument karta hai aur instructions ke execution ka report deta hai.

Simple idea: Compiled code ke kitne instructions tests ke through execute hue?

### B. Line coverage

Source file ki kitni executable lines tests ke through execute hui.

Example:

```java
if (price > 2000) {
    rejectFlight();
}
```

Agar test mein `price > 2000` true nahi hua, to `rejectFlight()` wali line execute nahi hui.

### C. Branch coverage

Conditional decision ke outcomes cover hue ya nahi.

```java
if (isAvailable) {
    bookFlight();
} else {
    rejectBooking();
}
```

Is decision ke two branches:
- True branch.
- False branch.

Agar test sirf `isAvailable = true` test karta hai, branch coverage incomplete hai.

**Important:** 100% line coverage ka matlab 100% branch coverage zaruri nahi. Ek line par multiple decision outcomes ho sakte hain.

## 4.3 JaCoCo kya hai?

**COURSE SOURCE:** JaCoCo Java code coverage tool hai. Tests run karne ke baad report deta hai ki kitni lines, instructions aur branches cover hui hain.

Course mein JaCoCo ko Gradle build ke saath configure kiya gaya.

### Gradle setup — Course example

```gradle
apply plugin: 'jacoco'

check.dependsOn jacocoTestReport
```

- `apply plugin: 'jacoco'` — Gradle project mein JaCoCo plugin apply.
- `check.dependsOn jacocoTestReport` — `check` task ke saath JaCoCo test report task dependency.

Course ke sample project mein report path:

```text
build/reports/jacoco/test/html/index.html
```

JUnit test report ka path:

```text
build/reports/tests/test/index.html
```

**Version note:** ZIP ke Gradle examples purane Java 8, Gradle aur JaCoCo versions par based hain. Ye course project ka historical setup hai, modern production project ke liye version recommendation nahi. Current environment mein dependency/plugin compatibility separately verify karni hogi.

## 4.4 Course story — EmployeeTravelScheduler coverage

Instructor JaCoCo se `EmployeeTravelScheduler` test suite inspect karte hain.

Report mein:
- Green = relevant code fully covered.
- Yellow = partial coverage / branch ka kuch outcome execute nahi hua.
- Red = code not covered (report presentation ke context mein).

Ek method `sortAndExcludeNonconformingFlights()` flights ko price se sort karta hai aur $2,000 se expensive flights ko remove karta hai.

Coverage report ne show kiya:
- Filter ka normal path execute hua.
- Lekin `flight > $2,000` wala branch execute nahi hua.

Iska matlab existing tests expensive flight scenario ko exercise nahi kar rahe the.

### Coverage report se test gap kaise identify hua?

1. JaCoCo report open.
2. `EmployeeTravelScheduler` class open.
3. Relevant method inspect.
4. Yellow branch identify.
5. Requirement read: $2,000 se expensive flights exclude honi chahiye.
6. New test add: stub airline service ek expensive flight return kare.
7. Scheduler call karo.
8. Assert karo returned list mein expensive flight nahi hai.
9. JaCoCo report dobara run karo.
10. Branch coverage re-check karo.

**Main lesson:** Coverage report test cases likhne ka replacement nahi. Ye missing execution paths dhoondhne ka diagnostic tool hai.

## 4.5 100% coverage ka matlab bug-free software nahi

Ye interview aur practical dono ke liye critical hai.

Suppose:

```java
int discount(int amount) {
    if (amount > 1000) {
        return amount * 10 / 100;
    }
    return 0;
}
```

Tests:
- amount = 1500 → branch true.
- amount = 500 → branch false.

100% branch coverage possible hai. Lekin test expected result galat assert kare ya requirement incomplete ho, to bug bach sakta hai.

Coverage batati hai **code execute hua ya nahi**. Ye prove nahi karti ki:
- assertions meaningful hain;
- expected behaviour correct hai;
- all requirements covered hain;
- all boundary values tested hain;
- hidden defects absent hain.

### Coverage ko kaise use karna chahiye?

- Coverage low hai → unexecuted paths identify karo.
- Coverage high hai → assertions aur requirements ki quality inspect karo.
- Branch missed hai → condition ke opposite outcome ka test socho.
- Method covered hai → zaruri nahi har input combination covered ho.

---

# 5. Flaky Tests aur Non-Determinism

<badge label="COURSE SOURCE" color="success"/> <badge label="Difficulty: Hard" />

## 5.1 WHY — Flaky test dangerous kyun hai?

**COURSE SOURCE definition:** Flaky test woh test hai jiska outcome non-deterministic hota hai. Same SUT ke liye kabhi pass, kabhi fail.

Example:
- Run 1 → Pass.
- Run 2 → Fail.
- Run 3 → Pass.
- Run 4 → Pass.
- Run 5 → Fail.

Aise test par team trust lose kar deti hai.

### Instructor ke lecture mein diye gaye statistics

Transcript mein instructor historical examples cite karte hain:
- Google TAP ke 1.6 million daily tests mein approx. 73,000 failures ko flakiness se associated bataya gaya.
- Ek study ka reference diya gaya jisme OS, Java version aur timing change se GUI-related tests ke fail hone ki baat thi.
- Google blog ke reference se test lifecycle mein 16% tests ke kisi stage par flaky banne ka example diya gaya.

**Source caution:** Ye lecture ke historical statistics hain, current industry metrics nahi. Inhe present-day universal rate ke roop mein quote mat karna.

## 5.2 Flaky test ke main causes

### A. Concurrency

Multiple threads/processes simultaneously execute karte hain. Execution order aur timing har run mein same nahi hoti.

Possible issues:
- race condition;
- shared mutable state;
- thread scheduling differences;
- output order variation.

### B. Timing

Test timeout ya operation completion time par depend karta hai.

Example:
- Local machine par operation 100 ms mein complete.
- CI machine par 2 seconds.
- Test 500 ms timeout use kar raha hai.
- Local pass, CI fail.

### C. Environment changes

Course examples:
- Operating system differences.
- File system differences.
- Network stack.
- GUI framework/control positions.
- Available memory.
- Processor, network, disk speed.
- Date/time synchronization.
- JVM version and memory allocation.

### D. External shared data/services

Lecture ke initial discussion ke according database ya external service kabhi available aur kabhi unavailable ho sakti hai; shared data bhi doosre users/processes update kar sakte hain.

Test Doubles aise dependencies ko isolate karne mein help karte hain.

## 5.3 Course demo 1 — Multi-threaded log test

Instructor do threads use karte hain:
- Thread A.
- Thread B.

Har thread 10 times computation execute karta hai aur log mein apna ID append karta hai.

Test expectation ek exact interleaved string thi, jaise:

```text
babababababababababa
```

Lekin actual execution kabhi:

```text
abababababababababab
```

bhi produce kar sakta hai.

Problem:
- Test exact order assume kar raha tha.
- Program ka actual requirement sirf ye tha ki A ne 10 baar aur B ne 10 baar computation ki.
- Thread execution order guaranteed nahi tha.

### Program bug aur test bug mein difference

Instructor explicitly kehte hain ki flaky result aane par pehle decide karo:

**Kya SUT flaky hai, ya test flaky hai?**

Is example mein shared log access synchronized tha. Program shared variable ko protect kar raha tha. Test ne unnecessary exact ordering assume kar li thi.

### Correct test strategy

Exact sequence assert karne ke badle meaningful invariant assert karo:

- A count = 10.
- B count = 10.

Instructor log ko sort karke all A aur all B group karte hain, phir expected count-based string se compare karte hain.

**Mentor explanation:** Assertion ko business requirement ke according rakho. Agar order requirement ka part hi nahi hai, to order assert karke test brittle mat banao.

## 5.4 Course demo 2 — HashSet order aur hashCode

Instructor `ClassWithoutHashcode` ke objects ko `HashSet` mein store karke output order inspect karte hain.

Important idea:
- HashSet insertion order guarantee nahi karta.
- Default `Object.hashCode()` implementation ki value execution/memory allocation conditions ke saath vary kar sakti hai.
- Different JVM/platform/run par iteration order change ho sakta hai.
- Isliye set se list/array banane ke baad insertion order expect karna unreliable hai.

Instructor ka demonstration:
- Ek machine par test repeatedly pass hota raha.
- Different machine/JVM par output order change ho sakta tha.
- Test flaky ya environment-dependent lag sakta hai.

**Critical correction/mentor clarification:** HashSet ko insertion-ordered collection samajhna hi incorrect assumption hai. Java mein insertion order chahiye to appropriate ordered collection use karna hota hai, jaise `LinkedHashSet`. Course ka point test ki fragile assumption ko expose karna hai; har hash code ko literally memory pointer samajhna modern JVM implementations ke liye oversimplification hoga.

## 5.5 Mocks aur concurrency

Instructor ye bhi batate hain ki mock verification bhi order-sensitive ho sakti hai.

- `InOrder` exact sequence enforce karta hai.
- Count-based verification order-independent ho sakta hai.
- Multi-threaded environment mein agar business requirement exact order nahi demand karti, count-based checks zyada robust ho sakte hain.

Example:

```java
verify(mockService, times(10)).process(any());
```

Iska focus invocation count par hai, exact interleaving par nahi.

**Important:** Agar business rule kehta hai “payment authorize hone ke baad hi capture karo”, tab order meaningful hai. Wahan `InOrder`/sequence verification valid hai.

## 5.6 Practical flaky-test debugging checklist

1. Test ko multiple times run karo.
2. Failure pattern observe karo — random, environment-specific, timing-specific?
3. SUT aur test assertion ko separately inspect karo.
4. Shared state identify karo.
5. External dependencies identify karo.
6. Date/time/timezone assumptions inspect karo.
7. Fixed sleep/fragile timeout assumptions inspect karo.
8. Ordering assumption requirement se justified hai ya nahi?
9. Test data isolated aur deterministic hai?
10. CI aur local environment differences compare karo.

### Playwright / Python SDET connection — Mentor extension

Course examples Java unit testing par hain. Lekin flaky-test principles Playwright automation mein bhi directly apply hote hain.

| Java unit test concept | Playwright example |
|---|---|
| Timing dependency | Fixed `time.sleep(5)` |
| Concurrency/shared state | Parallel tests same account/data modify karna |
| Environment dependency | Local vs CI browser/viewport differences |
| External service dependency | Live API test data unstable |
| Exact order assumption | Unnecessary strict event sequence assertion |
| Non-deterministic data | Random test data without controlled seed |

Playwright mein:
- fixed sleeps avoid karo;
- auto-waiting aur web-first assertions prefer karo;
- test data isolate karo;
- independent tests design karo;
- external systems ko API/UI test strategy ke according control karo;
- retries ko root-cause fix ka replacement mat banao.

---

# 6. CoffeeMaker Assignment — ZIP ke practical resources

<badge label="ASSIGNMENT SOURCE" color="success"/> <badge label="Difficulty: Hard" />

ZIP mein CoffeeMaker ke multiple variants diye gaye hain. Inko ek hi project samajh kar mix nahi karna.

## 6.1 ZIP inventory — kya-kya mila?

Module 4 ZIP mein 80 files hain. Important resource groups:

| Resource | Purpose |
|---|---|
| `CoffeeMaker_JUnit_Assign` | Buggy CoffeeMaker ko JUnit tests se test karna |
| `CoffeeMaker_Mock_Assign` | RecipeBook dependency ko stub/mock karna |
| `CoffeeMaker_JaCoCo_Assign` | Coverage report exercise |
| `Golden/CoffeeMaker_JUnit_Golden` | Reference/golden implementation |
| CoffeeMaker requirements PDF | User stories aur use cases |
| Class diagram PDF | Classes/relationships visual |
| Sequence diagram PDF | Object interaction visual |
| Gradle setup PDF | Eclipse/Gradle project import |

## 6.2 CoffeeMaker requirements — source-derived summary

CoffeeMaker command-line based educational application hai. Hardware control scope mein nahi hai; focus logic par hai.

### User stories

1. Waiting State — user ko six options show.
2. Add Recipe — maximum three recipes; unique name; integer price/ingredients.
3. Delete Recipe — existing recipe delete.
4. Edit Recipe — existing recipe details update; recipe name change nahi.
5. Add Inventory — coffee, milk, sugar, chocolate add.
6. Check Inventory — current quantities display.
7. Purchase Beverage — selected recipe, payment, inventory check, beverage purchase/change.

### Important requirement rules

**Add Recipe:**
- Maximum 3 recipes.
- Recipe name unique.
- Price integer.
- Ingredient amounts integer.
- Price/ingredients negative nahi hone chahiye.
- Duplicate recipe name reject.

**Delete Recipe:**
- Valid existing recipe delete.
- Out-of-range index reject.
- Alphabetic input reject.
- Empty recipe delete nahi.

**Edit Recipe:**
- Existing recipe select.
- Name change allowed nahi.
- Invalid index/empty slot reject.
- Price/ingredients integer and non-negative.

**Add Inventory:**
- Coffee, milk, sugar, chocolate quantities.
- Negative/non-integer input reject or reprompt according to use case.
- Inventory current amount mein add hoti hai.

**Purchase Beverage:**
- Recipe exist honi chahiye.
- User ne sufficient money deposit kiya ho.
- Inventory sufficient ho.
- Successful purchase par ingredients deduct aur change return.
- Insufficient money/inventory par user ka money return.

## 6.3 JUnit Buggy Assignment — deliverable

`CoffeeMaker_JUnit_Assign/README.md` ke according:

- `CoffeeMakerTest.java` develop/update karna hai.
- Existing functional code ko modify nahi karna.
- At least 5 bugs detect karne ke liye sufficient unit tests likhne hain.
- Assignment testing par focused hai, code fix karne par nahi.

### Provided starter tests

- `testAddInventory()`
- `testAddInventoryException()`
- `testMakeCoffee()`

Starter tests complete suite nahi hain. Ye sirf starting point hain.

### High-value test ideas from requirements

| Feature | Test idea | Expected behaviour |
|---|---|---|
| Add recipe | First recipe add | Success |
| Add recipe | Duplicate name | Reject |
| Add recipe | Capacity reached | Additional recipe reject |
| Delete recipe | Valid index | Correct recipe name |
| Delete recipe | Empty slot | Null/failure |
| Delete recipe | Negative/out-of-range index | Safe rejection |
| Edit recipe | Existing recipe | Name retained, other values updated |
| Edit recipe | Empty slot | Safe rejection |
| Add inventory | Valid positive quantities | Inventory increases |
| Add inventory | Negative/non-numeric input | Inventory exception |
| Purchase | Exact payment | Change 0 |
| Purchase | Extra payment | Correct change |
| Purchase | Insufficient payment | Money returned |
| Purchase | Insufficient ingredient | Money returned; no incorrect deduction |
| Purchase | Invalid recipe index | Safe handling |

## 6.4 Source code inspection — mentor analysis, not lecture claims

ZIP ke buggy `CoffeeMaker_JUnit_Assign` source mein kuch suspicious implementation points visible hain. Ye observations source code se nikle hain; assignment ka exact bug list README mein disclose nahi kiya gaya.

### Observation A — `makeCoffee()` index validation

Buggy source mein:

```java
if (getRecipes()[recipeToPurchase] == null) {
    change = amtPaid;
}
```

Is line se pehle negative ya array length se bada index validate nahi hota.

Test ideas:
- `makeCoffee(-1, 100)`
- `makeCoffee(arrayLength, 100)`

Expected requirement-based behaviour: invalid recipe selection safely reject ho aur money return ho. Actual buggy code `ArrayIndexOutOfBoundsException` throw kar sakta hai.

### Observation B — Inventory coffee deduction

Buggy `Inventory.useIngredients()` source mein coffee ke liye:

```java
Inventory.coffee += r.getAmtCoffee();
```

Recipe banate waqt coffee inventory reduce honi chahiye, lekin source coffee quantity increase kar raha hai.

Test:
1. Initial coffee quantity record karo.
2. Known recipe with coffee amount 3 prepare karo.
3. Expected coffee quantity = initial - 3.
4. Actual behaviour compare karo.

### Observation C — Sugar inventory addition

Buggy `Inventory.addSugar()` mein condition:

```java
if (amtSugar <= 0) {
    Inventory.sugar += amtSugar;
} else {
    throw new InventoryException(...);
}
```

Positive quantity add karni chahiye, lekin code positive value ko reject aur zero/negative ko accept karta hua dikh raha hai.

Test ideas:
- Add `"5"` → expected inventory increase.
- Add `"0"` → requirement/source interpretation ke hisaab se zero accepted or no-op; verify carefully.
- Add `"-2"` → exception expected.

### Observation D — RecipeBook capacity mismatch

Requirements PDF ke according maximum 3 recipes. Lekin buggy JUnit assignment ke `RecipeBook.java` mein:

```java
private final int NUM_RECIPES = 4;
```

Golden version mein 3 slots hain. Isliye assignment requirements aur buggy source ke beech mismatch hai.

**Mentor instruction:** Test expected behaviour requirements se derive karo, buggy implementation ko expected behaviour mat banao. Is discrepancy ko notes mein record karo. Test likhte waqt three-recipe limit verify karna meaningful hai.

### Observation E — Delete/edit index validation

Buggy `RecipeBook.deleteRecipe()` aur `editRecipe()` directly array index access karte hain. Negative/out-of-range values safe handle nahi karte. Requirements invalid selection ko reject karne ko kehti hain.

Test invalid indices for both operations.

**Note:** Ye source inspection observations hain; inhe course lecture mein instructor ke identified bug list ke roop mein present nahi kiya gaya. Assignment mein apne tests run karke actual failures verify karna hoga.

## 6.5 CoffeeMaker Mock Assignment

`CoffeeMaker_Mock_Assign` mein `CoffeeMaker` constructor dependencies receive karta hai:

```java
public CoffeeMaker(RecipeBook recipeBook, Inventory inventory)
```

Yahan `RecipeBook` interface hai. Assignment ka goal RecipeBook ko stub karke CoffeeMaker test karna hai.

### Test setup concept

```java
recipeBookStub = mock(RecipeBook.class);
coffeeMaker = new CoffeeMaker(recipeBookStub, new Inventory());
```

Then:
- `when(recipeBookStub.getRecipes()).thenReturn(recipes);`
- `when(recipeBookStub.addRecipe(recipe)).thenReturn(true);`
- `verify(recipeBookStub).addRecipe(recipe);`

**Important:** `CoffeeMaker_Mock_Assign` mein `RecipeBook` interface hai, jabki JUnit assignment variant mein concrete `RecipeBook` class hai. Dono project variants ko ek saath merge mat karna.

### Assignment practice checklist

- RecipeBook mock create.
- `getRecipes()` stub.
- `addRecipe()` stub.
- `deleteRecipe()` stub.
- `editRecipe()` stub.
- `verify()` se interactions verify.
- `makeCoffee()` ke recipe lookup behaviour test.
- Dependency call count/order only when requirement demands.

## 6.6 JaCoCo Assignment

`CoffeeMaker_JaCoCo_Assign` project mein JaCoCo plugin configured hai. Project README ke according:
- Build/test run karo.
- JUnit report inspect karo.
- JaCoCo HTML report inspect karo.
- Missed lines/branches identify karo.
- Missing tests add karo.

Coverage report location:

```text
build/reports/jacoco/test/html/index.html
```

### Suggested workflow

1. Project ko correct folder se open/import karo.
2. Existing Gradle setup inspect karo.
3. Baseline build run karo.
4. JUnit tests ka result dekho.
5. JaCoCo report open karo.
6. Missed branch identify karo.
7. Requirement ke according test design karo.
8. Test run karo.
9. Coverage report dobara inspect karo.
10. Coverage increase ke saath assertion quality bhi check karo.

## 6.7 Course project setup — Gradle/Eclipse

Source ZIP mein Gradle project import PDF aur README instructions included hain.

Course setup flow:
1. ZIP extract.
2. Eclipse open.
3. `File > Import`.
4. `Gradle > Existing Gradle Project`.
5. Project root directory select.
6. Finish.
7. Gradle Tasks view open.
8. `build` task run.
9. Test reports inspect.

Command line (project README):

```bash
./gradlew build
```

Windows:

```bat
gradlew.bat build
```

**Historical compatibility warning:** Assignment README Java 8 require karta hai aur old Gradle/JUnit/Mockito/JaCoCo dependencies use karta hai. Aapke current machine par installed Java/Python/Gradle versions alag ho sakte hain. Isliye is legacy project ko run karne se pehle compatibility check karna hoga. Current Playwright/Python environment ko is Java assignment ke liye blindly change mat karna.

---

# 7. Course concepts ko Python / Pytest / Playwright SDET work se connect karna

<badge label="MENTOR EXTENSION" color="info"/> <badge label="Not a lecture transcript" />

Course Java + JUnit + Mockito + JaCoCo par based hai. Lekin underlying testing principles Python automation mein bhi apply hote hain.

## 7.1 Test Doubles in Python

Python testing mein common tools:
- `unittest.mock.Mock`
- `unittest.mock.MagicMock`
- `unittest.mock.patch`
- `pytest` fixtures
- Fake in-memory repositories/services

Example:

```python
from unittest.mock import Mock

payment_gateway = Mock()
payment_gateway.charge.return_value = True

result = payment_gateway.charge(500)

assert result is True
payment_gateway.charge.assert_called_once_with(500)
```

Mapping:

| Java / Mockito | Python equivalent |
|---|---|
| `mock(Class.class)` | `Mock()` / `patch()` |
| `when(...).thenReturn(...)` | `.return_value = ...` |
| `verify(mock, times(2))` | `.assert_called...` / `call_count` |
| `InOrder` | `mock_calls` / `assert_has_calls` |
| Stub | Mock with configured return value |
| Fake | Small working fake implementation |

## 7.2 Example — Order Service

Imagine:

```python
class OrderService:
    def __init__(self, payment_gateway, email_service):
        self.payment_gateway = payment_gateway
        self.email_service = email_service

    def place_order(self, order):
        paid = self.payment_gateway.charge(order.total)
        if paid:
            self.email_service.send_confirmation(order.id)
            return "SUCCESS"
        return "PAYMENT_FAILED"
```

Unit test mein:
- Payment gateway mock.
- Email service mock.
- Payment success return configure.
- Email call verify.
- Payment failure return configure.
- Ensure email send nahi hui.

Example:

```python
from unittest.mock import Mock

def test_email_sent_after_successful_payment():
    payment = Mock()
    email = Mock()

    payment.charge.return_value = True

    service = OrderService(payment, email)
    order = Order(id=101, total=500)

    result = service.place_order(order)

    assert result == "SUCCESS"
    payment.charge.assert_called_once_with(500)
    email.send_confirmation.assert_called_once_with(101)
```

**SDET insight:** Is test mein hum UI test nahi kar rahe. Hum service ki business logic aur dependency interactions isolate karke test kar rahe hain.

## 7.3 Playwright automation mein flaky test prevention

Example of fragile test:

```python
page.click("#submit")
time.sleep(5)
assert page.locator(".success").is_visible()
```

Better direction:

```python
page.get_by_role("button", name="Submit").click()
expect(page.get_by_text("Order created")).to_be_visible()
```

Why better:
- Fixed sleep par depend nahi.
- Locator semantic hai.
- Assertion condition ke complete hone ka wait karti hai.
- Unnecessary timing assumption kam hota hai.

Parallel tests ke liye:
- Har test ka independent data.
- Unique user/order IDs.
- Shared mutable state avoid.
- Cleanup strategy.
- External services ko controlled test environment mein use karna.

---

# 8. Interview Preparation

## 8.1 What is a Test Double?

**Simple English answer:**

A test double is a lightweight replacement of a real dependency used during testing. It helps isolate the system under test and control the dependency's behaviour.

**Professional answer (1–2 minutes):**

In unit testing, a class often depends on external collaborators such as databases, APIs, file systems, or other services. Using real dependencies can make tests slow, unreliable, expensive, or difficult to execute. A test double replaces the real collaborator during testing. Depending on its role, it can provide predefined responses or help verify interactions. Common types include dummy objects, stubs, fakes, mocks, and spies. Test doubles help us isolate the unit, control test data, avoid side effects, and improve test reliability.

**Keywords:** SUT, dependency, isolation, controlled behaviour, side effects, reliability.

## 8.2 Dummy vs Stub vs Fake

**Simple answer:**
- Dummy: required placeholder.
- Stub: returns predefined responses.
- Fake: lightweight working implementation.

**Professional answer:**

A dummy object is passed to the system under test when the parameter is required but its behaviour is irrelevant. A stub provides predefined responses for selected method calls so the SUT can be tested under controlled conditions. A fake is a simplified working implementation of a real dependency, such as an in-memory repository replacing an external database. The correct choice depends on whether the test needs only a placeholder, a controlled response, or a lightweight functional implementation.

**Keywords:** placeholder, predefined response, simplified implementation, input double.

## 8.3 Mock vs Spy

**Simple answer:**
A mock is generally a test-created object used to control and verify interactions. A spy wraps a real object and records interactions while real behaviour can still execute.

**Professional answer:**

Mocks and spies are useful when output assertions alone are insufficient, especially for void methods or collaborator interactions. A mock is a fake collaborator whose behaviour can be configured and whose method calls can be verified. A spy wraps a real object and allows us to observe how it is used while retaining real object behaviour by default. I use mocks when I need to isolate an external dependency and spies when I need to monitor interactions with an existing real object. I avoid unnecessary interaction assertions because they can couple tests too tightly to implementation details.

**Keywords:** interaction testing, `verify`, real object, invocation count, coupling.

## 8.4 What is stubbing in Mockito?

**Simple answer:**
Stubbing means configuring a mock to return a predefined value when a specific method is called.

**Professional answer:**

In Mockito, stubbing is commonly configured using `when(...).thenReturn(...)`. It allows a test to control the response of a dependency. For example, I can configure an airline service mock to return a known list of flights, so the scheduler can be tested without calling the real airline API. I can also configure different responses for consecutive calls or match specific arguments. This makes unit tests deterministic and independent of external services.

**Keywords:** `when`, `thenReturn`, controlled response, argument matching, deterministic.

## 8.5 What is JaCoCo?

**Simple answer:**
JaCoCo is a Java code coverage tool that generates reports about executed instructions, lines, and branches during tests.

**Professional answer:**

JaCoCo instruments Java bytecode and collects coverage information while tests execute. It provides reports for metrics such as instruction, line, and branch coverage. I use these reports to identify unexecuted code paths and design additional tests. However, coverage is not proof of correctness. High coverage does not guarantee meaningful assertions or defect-free software, so I use coverage together with requirement-based test design and boundary/negative testing.

**Keywords:** instrumentation, instruction coverage, line coverage, branch coverage, test adequacy.

## 8.6 What is a flaky test?

**Simple answer:**
A flaky test is a test that sometimes passes and sometimes fails for the same system and test conditions.

**Professional answer:**

A flaky test has a non-deterministic outcome. Common causes include concurrency, race conditions, timing assumptions, shared test data, environment differences, and unstable external dependencies. I investigate whether the failure is caused by the application or by the test itself. Then I remove unnecessary ordering assumptions, isolate test data, control dependencies, replace fixed sleeps with condition-based waits, and ensure assertions validate only behaviour required by the specification.

**Keywords:** non-deterministic, concurrency, timing, environment, isolation, robust assertions.

## 8.7 What is branch coverage?

**Simple answer:**
Branch coverage measures whether each possible outcome of a decision, such as true and false, has been executed by tests.

**Professional answer:**

Branch coverage focuses on decision outcomes rather than only whether a line was executed. For an `if/else` condition, tests should exercise both the true and false outcomes. It helps identify missing paths that line coverage may not reveal. However, even 100% branch coverage does not guarantee that all requirements or input combinations are tested.

**Keywords:** decision outcomes, true/false, control flow, coverage gap.

---

# 9. Practice Exercises — Concept mastery

## Exercise 1 — Identify the correct Test Double

Har case ke liye Dummy, Stub, Fake, Mock ya Spy select karo.

1. Method ko `Employee` parameter chahiye, lekin test mein employee details use nahi hoti.
2. Payment service ko fixed `true` response dena hai.
3. External DB ke badle in-memory repository use karni hai.
4. Verify karna hai ki `sendEmail()` exactly once call hua.
5. Real list par operations perform karke `add()` invocation count verify karna hai.

**Answers:**
1. Dummy
2. Stub
3. Fake
4. Mock
5. Spy

## Exercise 2 — Mockito stubbing

Requirement:
- `getUser(10)` → user object return.
- `getUser(20)` → null return.

Write a Mockito-style stub configuration.

**Expected concept:**

```java
when(userService.getUser(10)).thenReturn(user10);
when(userService.getUser(20)).thenReturn(null);
```

## Exercise 3 — Invocation count

A service flow:
- `validate()` 1 time.
- `charge()` 1 time.
- `sendReceipt()` 1 time.

Write verification statements.

**Expected concept:**

```java
verify(service, times(1)).validate();
verify(service, times(1)).charge();
verify(service, times(1)).sendReceipt();
```

Actual class/method signatures ke according arguments add karna.

## Exercise 4 — Order verification

Business rule: `authorize()` ke baad hi `capture()` call hona chahiye.

**Expected concept:** `InOrder` use karo. Pehle authorize verify, phir capture.

## Exercise 5 — Coverage gap

Code:

```java
if (balance >= amount) {
    debit();
} else {
    reject();
}
```

Existing test sirf sufficient balance test karta hai.

Questions:
1. Kaunsa branch missing hai?
2. Kaunsa test add karoge?

**Answer:**
- False branch missing.
- `balance < amount` test add karo; verify reject behaviour.

## Exercise 6 — Flaky assertion

Two worker threads log their IDs. Requirement says each thread must complete 10 tasks. Existing test exact output order compare karta hai.

Question: Better assertion kya hogi?

**Answer:**
- A aur B ke occurrence counts verify karo.
- Exact interleaving order assert mat karo unless order requirement ka part hai.

## Exercise 7 — CoffeeMaker test design

At least 5 requirement-based tests identify karo jo buggy CoffeeMaker source ke suspicious paths catch kar sakte hain.

Suggested answer:
1. Negative recipe index.
2. Out-of-range recipe index.
3. Coffee quantity purchase ke baad decrease.
4. Positive sugar inventory add.
5. Negative sugar inventory reject.
6. Delete invalid recipe index.
7. Edit invalid recipe index.
8. More than 3 recipes add karna reject.

---

# 10. Common mistakes — Revision table

| Mistake | Correct thinking |
|---|---|
| Mock, Stub, Fake ko same samajhna | Roles alag hain |
| Mockito `mock()` ko sirf Mock role ke liye samajhna | Same created object stub/dummy/mock role play kar sakta hai |
| Stub se interaction verification expect karna | Stub response deta hai; mock interaction verify karta hai |
| Spy ko pure fake samajhna | Spy real object wrap karta hai |
| Har call ka order verify karna | Order only when requirement needs it |
| 100% coverage = bug-free | Coverage execution measure hai, correctness proof nahi |
| Flaky failure ko immediately product bug bolna | Test-vs-SUT cause isolate karo |
| HashSet ko insertion ordered samajhna | HashSet insertion order guarantee nahi karta |
| Fixed sleep se timing issue solve karna | Condition-based wait/assertion use karo |
| Test doubles ko production integration tests ka replacement samajhna | Unit tests aur integration tests different purposes serve karte hain |
| Buggy assignment source ko expected behaviour banana | Requirements expected behaviour define karti hain |
| CoffeeMaker project variants mix karna | JUnit, Mock, JaCoCo projects separate variants hain |

---

# 11. Module 4 ka final revision map

```text
UNIT TESTING ECOSYSTEM
        |
        +-- Test Doubles
        |     |
        |     +-- Input doubles
        |     |     +-- Dummy
        |     |     +-- Stub
        |     |     +-- Fake
        |     |
        |     +-- Interaction doubles
        |           +-- Mock
        |           +-- Spy
        |
        +-- Mockito
        |     +-- mock()
        |     +-- when().thenReturn()
        |     +-- any() / argument matching
        |     +-- verify()
        |     +-- times()
        |     +-- InOrder
        |
        +-- Test Suite Adequacy
        |     +-- Instruction coverage
        |     +-- Line coverage
        |     +-- Branch coverage
        |     +-- JaCoCo reports
        |
        +-- Flaky Tests
              +-- Concurrency
              +-- Timing
              +-- Environment
              +-- Non-deterministic order
              +-- Robust assertions
```

## Completion checklist

- [ ] Main SUT aur dependency ka difference samjha sakta hoon.
- [ ] Dummy, Stub aur Fake ko examples ke saath differentiate kar sakta hoon.
- [ ] Mockito `mock()` aur `when().thenReturn()` likh sakta hoon.
- [ ] Consecutive return values configure kar sakta hoon.
- [ ] Mock aur Spy ka difference explain kar sakta hoon.
- [ ] `verify()` aur `times()` use kar sakta hoon.
- [ ] `InOrder` kab use karna chahiye samajhta hoon.
- [ ] Instruction, line aur branch coverage explain kar sakta hoon.
- [ ] JaCoCo report se missed branch identify kar sakta hoon.
- [ ] 100% coverage bug-free hone ka proof nahi hai — explain kar sakta hoon.
- [ ] Flaky test ke causes identify kar sakta hoon.
- [ ] Test bug aur product bug mein distinction kar sakta hoon.
- [ ] CoffeeMaker requirements se test cases derive kar sakta hoon.
- [ ] Assignment ke alag project variants ko mix nahi karta.

## Mentor's final guidance

Module 4 ka sabse important shift ye hai:

**Testing sirf output compare karna nahi hai.** Kabhi dependency ko controlled input dena hota hai, kabhi interaction verify karna hota hai, kabhi coverage report se missing execution path dhoondhna hota hai, aur kabhi test ke apne assumptions ko challenge karna hota hai.

Ek strong SDET:
1. Requirement se expected behaviour derive karta hai.
2. SUT ko dependencies se isolate karna jaanta hai.
3. Correct test double choose karta hai.
4. Output ke saath meaningful interactions verify karta hai.
5. Coverage ko diagnostic tool ki tarah use karta hai.
6. Flaky tests ko retries se hide nahi karta — root cause identify karta hai.

**Module 4 complete tab maana jayega jab aap CoffeeMaker assignment ke liye requirement-based tests design kar sako, Mockito se dependencies stub/verify kar sako, JaCoCo report se missing branch identify kar sako, aur flaky test ka root cause explain karke robust assertion likh sako.**
