# 🧪 MODULE 1 — INTRODUCTION TO SOFTWARE TESTING
## Hinglish Mentor Notes | University of Minnesota

> 🎯 **Is module ka goal:** Testing ki definitions ratna nahi. Tumhe samajhna hai ki software testing kyun zaroori hai, testing difficult kyun hai, ek test actually hota kya hai, aur tests ko systematically kaise likhte hain.

> 🧭 **Reading rule:** `🎓 COURSE STORY` instructor ki lecture/story ko simple Hinglish mein samjhata hai. `🧠 MENTOR EXPLAINS` concept ko todkar samjhata hai. `💼 SDET CONNECTION` tumhare automation/testing work se connect karta hai. `⭐ INTERVIEW` interview-ready answer deta hai. Koi topic overlap ke naam par remove nahi kiya gaya.

---

# 🗺️ Module ka route — pehle samajh lo hum kahan ja rahe hain

| Lecture | Main sawaal | Tum kya seekhoge |
|---|---|---|
| 1. Welcome & Why Test? | Testing kyun karte hain? | Real failures, V&V, analysis techniques |
| 2. Why Testing Is Hard | Testing karna itna difficult kyun hai? | Sampling, state space, discontinuity, Zune story, black/white box |
| 3. What Is a Test? | Test ki actual definition kya hai? | SUT, test data, oracle, test case, 4 stages |
| 4. JUnit Demo | Automated unit test practically kaise chalta hai? | JUnit, assertions, triangle method, console I/O |
| 5. Writing Unit Tests / TDD | Test pehle likhne ka benefit kya hai? | Circle story, expected output, invalid input, TDD |

🎯 **Difficulty:** Easy → Hard  |  **Focus:** Concepts + practical test thinking

---

# 1. 🎓 LECTURE 1 — Welcome: Why Do We Test?

## 1.1 Testing kyun zaroori hai?

### 🎓 COURSE STORY — instructor ke real-world examples

Instructor Mike Whalen lecture ki shuruaat ek simple baat se karte hain: **software likhna difficult hai, aur programmers mistakes karte hain.** Agar hum software ko adequately test nahi karte, toh bug sirf screen par chhota error nahi hota; woh real world mein financial loss, privacy breach, security risk, ya human safety issue ban sakta hai.

Lecture mein 2016 ke kuch examples diye gaye:

- **Yahoo:** users ki personal information leak hui.
- **British Airways:** scheduling-system problem ki wajah se reservations/flights cancel hue aur business ko bada impact hua.
- **Jeep:** remote security vulnerability se vehicle functions ko affect karne ka risk tha.
- **Democratic National Committee:** email server compromise hua.
- **Bangladesh Bank:** financial system se related large loss ka example diya gaya.
- **Nest thermostat:** software update ke baad heating control disrupt hua.
- **Therac-25:** radiation-treatment machine se related software failures ne human life ko affect kiya.

> 🔴 **Story ka lesson:** Software failure ka impact application ke type par depend karta hai. Shopping website mein wrong total financial loss de sakta hai; banking software mein wrong transaction; medical/aviation system mein safety risk.

### 🧠 MENTOR EXPLAINS — tester ko is story se kya seekhna chahiye?

Socho tum ek e-commerce application test kar rahe ho. UI par `Order placed successfully` aa gaya. Kya test pass ho gaya?

**Nahi, abhi nahi.** Tumhe requirements ke hisaab se aur cheezein verify karni pad sakti hain:

1. Order database mein create hua?
2. Correct user ke naam par create hua?
3. Product quantity/inventory correct update hui?
4. Payment amount correct hai?
5. User order history mein order dekh sakta hai?
6. Retry karne par duplicate order toh create nahi hua?

Ek green toast message poore business transaction ka proof nahi hai.

### ⭐ INTERVIEW — Why is software testing important?

**Simple English:**  
“Software testing is important because developers can make mistakes, and defects can affect functionality, security, money, customer trust and even human safety. Testing helps us find defects before software reaches users.”

**Stronger answer:**  
“Software is used in business-critical and safety-critical environments. A defect can cause anything from a poor user experience to financial loss, security compromise or physical harm. Testing provides evidence about whether the system behaves as expected and helps reduce the risk of releasing defective software. Testing cannot prove that no defects exist, but it can expose defects and increase confidence in the product.”

**Keywords:** defect, risk, reliability, security, customer trust, safety, confidence.

---

## 1.2 Verification vs Validation — sabse important difference

### 🎓 COURSE SOURCE

Instructor do questions introduce karte hain:

| Concept | Question | Simple meaning |
|---|---|---|
| **Verification** | Are we building the software right? | Jo specification/requirement likhi hai, kya implementation uske according hai? |
| **Validation** | Are we building the right product? | Kya product actual user ki need solve kar raha hai? |

### 🧠 MENTOR EXPLAINS — ek relatable example

Customer kehta hai: “Mujhe online food order karne ke liye simple app chahiye.”

Team requirement likhti hai:
- User restaurant list dekh sake.
- Food cart mein add kar sake.
- Payment kar sake.
- Order track kar sake.

**Verification:**  
Requirement ke against check karo: restaurant list aa rahi hai? Cart kaam kar raha hai? Payment flow specified behaviour follow kar raha hai? Order tracking correct hai?

**Validation:**  
Real user ko app use karwao. Kya user easily restaurant find kar pa raha hai? Kya checkout confusing hai? Kya app uski actual need solve kar rahi hai?

Aisa ho sakta hai ki tumne 100% written requirements implement kar di, lekin user ko app use karna hi difficult lag raha ho. Verification pass ho sakti hai, validation fail.

> ⭐ **Golden line:** Verification = product specification ke according bana? Validation = product user ke liye sahi bana?

### 💼 SDET CONNECTION

Automation tests aksar verification mein strong hote hain, kyunki hum defined expected behaviour ko repeatably check karte hain. Lekin user satisfaction, usability aur real-world usefulness ko sirf automated assertions se fully prove nahi kar sakte. Iske liye user feedback, acceptance testing aur usability evaluation bhi important hain.

### ⭐ INTERVIEW ANSWER

**Simple:**  
“Verification checks whether we are building the product right according to specifications. Validation checks whether we are building the right product for the user's needs.”

**Strong:**  
“Verification is specification-oriented and checks conformance between implementation and documented requirements. Validation is user-oriented and checks whether the delivered product solves the intended problem. A product may conform to an incorrect or incomplete specification, so passing verification alone does not guarantee user satisfaction.”

**Keywords:** specification, conformance, user needs, acceptance, usability.

---

## 1.3 V&V ke alawa quality check karne ke methods

### 🎓 COURSE SOURCE — lecture mein named techniques

1. **Requirements understanding/validation:** Pehle samjho ki software ko karna kya hai. Requirement hi unclear hai toh test ka expected result bhi unclear hoga.
2. **Inspection:** Kisi aur person/team se requirements, design ya code examine karwana.
3. **Design discussion / walkthrough:** Team design discuss kare — kya design performance, security aur required behaviour meet karega?
4. **Static analysis:** Program ko execute kiye bina code analyse karna. Example: possible null-pointer dereference ya integer overflow ka warning.
5. **Testing:** Software execute karo, input do aur actual behaviour observe karo.
6. **Runtime verification:** Program chal raha ho tab uske behaviour ko monitor karna; anomaly dikhe toh investigation ya shutdown action ho sakta hai.

Instructor batate hain ki testing useful isliye hai kyunki actual execution environment mein OS, processor, compiler, devices, network, linker/loader aur doosre components ke saath system ka behaviour dekha ja sakta hai. Performance jaise behaviour ko assess karne mein bhi testing useful hai.

### 🧠 MENTOR EXPLAINS — simple comparison

| Method | Application run hoti hai? | Example |
|---|---|---|
| Code inspection | Zaroori nahi | Developer code review |
| Static analysis | Nahi | Linter/static analyser warning |
| Dynamic testing | Haan | Pytest test function run karna |
| Runtime monitoring | Haan, running system | Logs/metrics/alerts observe karna |

**Yaad rakho:** Static analysis aur testing ek hi cheez nahi. Static analysis code ko bina execute kiye examine karta hai; dynamic testing actual execution karti hai.

---

## 1.4 Testing incomplete hai — exhaustive testing kyun nahi?

### 🎓 COURSE SOURCE

Instructor ka point: simple software ke liye bhi possible tests ki count bahut badi ho sakti hai. Har possible input aur har possible state test karna practical nahi. Isliye objective **perfectly complete testing** nahi, balki **effective testing** hai.

### 🧠 MENTOR EXPLAINS

Login form mein combinations socho:
- Username ki possible values.
- Password ki possible values.
- Locked/unlocked account.
- Active/inactive user.
- Network slow/down.
- Different browser/device.
- Existing session/no session.
- Password expired/not expired.

Har combination try karna possible nahi. Isliye test selection intelligent hona chahiye: boundaries, risk, important business flows, previous defects aur likely failure areas ko priority do.

> 🔴 **Important:** 100% testing ka matlab har possible input test karna nahi hota. Practical projects mein hum risk aur defined adequacy criteria ke basis par coverage decide karte hain.

---

## 1.5 Instructor ka analysis-technique diagram: Optimistic vs Pessimistic

### 🎓 COURSE SOURCE

Instructor analysis techniques ko do dimensions par explain karte hain:

- **Optimistic vs Pessimistic:** Technique galat program ko correct maan sakti hai ya correct program par warning de sakti hai.
- **Simple vs Complex properties:** Technique kis complexity ke property ko check kar sakti hai.

Lecture mein ye approaches discuss hoti hain:

| Technique | Instructor ka central point |
|---|---|
| Typical testing | Kuch tests pass hue toh developer galti se maan sakta hai ki program correct hai — optimistic conclusion |
| Simple program analysis / lint-like tools | Possible overflow/null issue flag kar sakte hain; kabhi false warning bhi |
| Type checking | Relatively simple properties ko accurately check kar sakta hai |
| Static analysis | Execution ke bina program properties analyse karta hai; sound/unsound distinction aati hai |
| Coverage testing | Tests ke execution/coverage objectives define karta hai |
| Model checking | Certain systems/properties ke liye exhaustive-style state exploration ka concept |
| Automated testing | Bahut saare tests efficiently execute karne mein help |
| Theorem proving | Mathematical reasoning se complex properties prove karne ki approach; effort high |

Instructor **halting problem** ka bhi reference dete hain: arbitrary program ke liye ek universal method banana jo har case mein decide kar de ki program halt karega ya nahi — theoretically possible nahi. Isse samajh aata hai ki har arbitrary program property ko perfectly verify karna possible nahi.

### 🧠 MENTOR EXPLAINS — false positive/false negative

- **False positive:** Tool defect report kare, lekin actual mein defect na ho.
- **False negative:** Real defect ho, lekin tool detect na kare.

Example: static analyser warning deta hai ki variable `None` ho sakta hai. Agar actual code path mein woh kabhi `None` ho hi nahi sakta, warning false positive ho sakti hai. Agar real null path tool miss kar de, false negative.

> ⚠️ Sound/unsound ke formal definitions nuanced hain. Is lecture ke diagram mein instructor inhe false alarms aur missed errors ke trade-off ko samjhane ke liye use karte hain. Interview mein definition ko context ke saath explain karna.

### ⭐ INTERVIEW TOPIC

**Question:** Can testing prove that software has no bugs?  
**Answer:** “No. Testing can reveal the presence of defects, but it cannot prove their complete absence for a non-trivial system because we cannot execute every possible input and state. We use multiple verification techniques to increase confidence.”

---

# 2. 🎓 LECTURE 2 — Why Is Software Testing Hard?

## 2.1 Wall story — testing is sampling

### 🎓 COURSE STORY

Instructor ek wall ka example dete hain. Wall ke peeche system ke saare possible behaviours hain. Tum wall ke through sirf kuch chhote openings se dekh sakte ho. Har opening ek test ki tarah hai. Tum kuch selected behaviours observe karte ho, lekin poori wall ke peeche kya hai, sab nahi dekh sakte.

### 🧠 MENTOR EXPLAINS

Test execute karna = system ke behaviour ka ek sample observe karna.

Agar tumne `age = 30` test kiya aur pass hua, toh tum ye conclude nahi kar sakte ki age field correct hai. `17`, `18`, `60`, `61`, blank, negative, text aur very large values ka behaviour alag ho sakta hai.

## 2.2 Physical systems vs software — discontinuity

Instructor physical systems (jaise bridge/steel girder) aur software ke testing behaviour ka contrast dete hain. Physical system mein load badhane par behaviour kabhi-kabhi relatively continuous hota hai; software mein chhoti input change se output sharply change ho sakta hai.

**Example:**  
`age >= 18` mein:
- 17 → reject
- 18 → accept
- 19 → accept

17 se 18 ka one-unit difference result ko flip kar deta hai. Ek successful test nearby values ke pass hone ka proof nahi.

## 2.3 State space — system kitni states mein ho sakta hai?

### 🎓 COURSE SOURCE

**State space** = possible values/states ka large collection jisme system operate kar sakta hai. Defects state space ke specific points par trigger ho sakte hain. Small application mein bhi combinations bahut large ho sakte hain; isliye exhaustive testing practical nahi.

### 💼 SDET EXAMPLE

Cart application ki state sirf cart total nahi hai. State mein ho sakta hai:
- Logged-in/logged-out user.
- Cart empty/one item/multiple items.
- Stock available/out of stock.
- Coupon valid/expired.
- Payment success/failure/pending.
- Network online/offline.
- Existing order/new order.

In sabka combination state space badha deta hai.

## 2.4 🔥 Zune leap-year story — boundary testing ka classic example

### 🎓 COURSE STORY

Microsoft Zune media player New Year's Eve 2008 par fail hua. Lecture explain karta hai ki device 1980 se days count karta tha, phir loop se us day count ko year aur day representation mein convert karta tha.

Bug leap year ke last day par trigger hua:
- Leap year mein 366 days hote hain.
- Logic mein condition `days > 366` thi.
- Jab `days == 366` hua, leap-year branch expected tarah execute nahi hui.
- Loop day count ko reduce/update nahi kar paaya.
- Same condition repeat hoti rahi.
- Result: **infinite loop**.

### 🧠 MENTOR EXPLAINS — bug exactly kahan tha?

Agar logic ko simple form mein dekhein:

```python
# Conceptual illustration only
if leap_year and days > 366:
    days -= 366
```

Agar input exactly 366 hai, `366 > 366` false hai. Lekin agar requirement ke hisaab se 366th day ko bhi handle karna tha, condition wrong hai. Boundary par `>` vs `>=` ka difference important ban gaya.

### 🔥 Is story se tester ki learning

1. Normal date test karna enough nahi.
2. Leap year test karna zaroori.
3. Last day (366) specifically test karna zaroori.
4. Loop condition aur boundary comparison inspect karna helpful.
5. Ek exact boundary input system ko hang kar sakta hai.

**Real-world boundary example:** Discount rule: cart total `> ₹1,000` hai ya `>= ₹1,000`? ₹999, ₹1,000, ₹1,001 test karo. Expected result requirement se decide hoga.

## 2.5 Helpful Adversary — tester ka mindset

Instructor kehte hain tester ko system samajhna chahiye aur helpful adversary ki tarah sochna chahiye: “Main kaise input doon jisse system fail ho sakta hai?”

Try:
- Boundary values.
- Negative values.
- Very large values.
- Unexpected values.
- Rare states.
- Wrong sequence of actions.

Ye malicious attack nahi; quality improve karne ke liye deliberate challenge hai.

## 2.6 Black-box vs White-box testing

| Black-box | White-box |
|---|---|
| Requirements/expected behaviour ke basis par | Internal code structure ki knowledge ke basis par |
| Code dekhna required nahi | Code/branches/paths dekh sakte hain |
| “System kya karta hai?” | “Code ke andar kaunsa path execute hua?” |
| Example: invalid password reject hota hai? | Example: failed-login branch aur lockout counter path execute hua? |

Dono useful hain. Black-box se requirement behaviour check hota hai; white-box se internal structure aur missed paths par attention milti hai.

## 2.7 Testing ke 3 dimensions

Instructor testing ko teen alag axes par explain karte hain:

### A. Scale — kitna system test kar rahe ho?
- **Unit testing:** small unit/method/function.
- **Integration testing:** components/subsystems ka interaction.
- **System testing:** whole system/customer use cases.

### B. Process — tests kab likhte/run karte ho?
- **Test-first / TDD:** implementation se pehle tests.
- **Test-after:** code develop hone ke baad tests.
- Dono approaches mein iteration aur re-testing ho sakti hai.

### C. Purpose — kis quality ko check kar rahe ho?
- Functionality.
- Performance.
- Security.
- Usability.
- Availability.

Instructor **Netflix Chaos Monkey** ka example dete hain: system ke kuch hardware/software processes ko deliberately disrupt karke dekhna ki service available/reliable rehti hai ya nahi.

### ⭐ INTERVIEW ANSWER — Why is testing hard?

**Simple:**  
“Testing is hard because we cannot test every possible input and state. Software can behave differently even when an input changes slightly, so we need to select test cases carefully.”

**Strong:**  
“Software testing is inherently incomplete because the state space can be enormous. Software behaviour is often discontinuous, so a passing test does not guarantee that nearby inputs will pass. The Zune leap-year incident illustrates how a specific boundary value, day 366, triggered an infinite loop. Effective testing requires domain knowledge, boundary-focused test selection, black-box and white-box techniques, and risk-based prioritisation.”

**Keywords:** sampling, state space, discontinuity, boundary, helpful adversary, black-box, white-box.

---

# 3. 🎓 LECTURE 3 — What Exactly Is a Test?

## 3.1 SUT — Software Under Test

SUT ka full form **Software Under Test** hai. Iska matlab hamesha poori application nahi hota. Ye program ka koi completed part/subset bhi ho sakta hai jiska behaviour execute karke check kar sakte hain.

Unit examples:
- Method.
- Function.
- Subroutine.
- Procedure.
- Small defined task/operation.

**Python examples:** `calculate_tax()`, Django service method, serializer validation, API endpoint.

## 3.2 Test data / input

Test data woh input hai jo SUT ko diya jata hai. Instructor batate hain ki data:
- Expected user behaviour/profile ke basis par select ho sakta hai.
- Probability/user studies se aa sakta hai.
- Deliberately unusual values se aa sakta hai, jaise zero, very large number, ya number ki jagah word.

**Example — quantity field:**
- Normal: `5`
- Zero: `0`
- Negative: `-1`
- Very large: `1000000`
- Wrong type: `"five"`
- Empty: `""` / `None` (interface ke hisaab se)

## 3.3 Actual output vs Expected output

- **Actual output:** program execute karne par jo result mila.
- **Expected output:** requirement/rule ke according jo result aana chahiye.

Test ka kaam dono ko compare karna hai.

## 3.4 Test Oracle — extremely important term

### 🎓 COURSE SOURCE

**Oracle** woh person, component ya process hai jo decide karta hai ki actual behaviour correct hai ya nahi. Historically human tester actual aur expected compare karta tha. Lekin humans repetitive comparison mein unreliable ho sakte hain, isliye automated oracles useful hain. Lecture JUnit (Java) aur PyUnit (Python) ko examples ke roop mein mention karta hai.

### 🧠 MENTOR EXPLAINS

Test framework assertion execute kar sakta hai, lekin expected result kahan se aaya? Requirement, business rule, mathematical calculation, specification ya trusted reference se.

```python
def calculate_total(price, quantity):
    return price * quantity

def test_calculate_total():
    actual = calculate_total(100, 3)
    expected = 300
    assert actual == expected
```

Yahan assertion comparison karta hai. `expected = 300` oracle value hai jo intended rule ke basis par choose hui.

> 🔴 **Important:** Agar expected result hi wrong hai, test green aakar bhi misleading ho sakta hai. Green test ka matlab sirf itna hai ki assertion pass hui — ye nahi ki expected value sach mein correct thi.

## 3.5 Test Case — sirf input nahi hota

Lecture ke according test data aur expected output test case ke essential parts hain.

Practical test case document mein aur fields bhi ho sakte hain:

| Field | Purpose |
|---|---|
| Test Case ID | Unique reference |
| Requirement | Kis requirement ko verify kar raha hai |
| Preconditions | Test se pehle required state |
| Steps | Kya actions perform honge |
| Test data | Kaunse inputs |
| Expected result | Kya hona chahiye |
| Actual result | Kya hua |
| Status | Pass/Fail/Blocked |

Ye expanded template mentor addition hai; lecture ka core point input + expected output hai.

## 3.6 Test ke 4 stages — Setup, Invocation, Assessment, Teardown

| Stage | Meaning | Product delete example |
|---|---|---|
| **Setup** | Test ke liye required state create karo | Product pehle create karo; user login ho |
| **Invocation** | SUT/action execute karo | Delete action perform karo |
| **Assessment** | Actual vs expected compare karo | Product list se remove hua? |
| **Teardown** | Cleanup/restore | Remaining test data delete karo |

### 🧠 PYTEST MAPPING

```python
import pytest

@pytest.fixture
def product():
    # SETUP
    item = {"id": 101, "name": "Keyboard"}

    yield item

    # TEARDOWN
    item.clear()


def test_product_name(product):
    # INVOCATION / observation
    actual = product["name"]

    # ASSESSMENT
    assert actual == "Keyboard"
```

- Fixture ke `yield` se pehle setup.
- `yield` fixture data test ko deta hai.
- Test body mein action/observation aur assertion.
- `yield` ke baad teardown.

### 💼 PLAYWRIGHT CONNECTION

Product delete UI test:
1. Setup: API/fixture se product create + authorized login.
2. Invocation: product page open karke Delete click.
3. Assessment: product absent + expected confirmation.
4. Teardown: agar data bacha hai toh cleanup.

### ⚠️ Common mistakes

- Test data ko complete test case samajhna.
- Expected result ka source confirm na karna.
- Preconditions bhool jana.
- Tests ke beech shared state leak hona.
- Teardown na karna.
- Green report ko “no bugs” ka proof samajhna.

### ⭐ INTERVIEW ANSWER

“A test is a controlled execution of a software unit or system using selected test data, followed by assessment of the observed behaviour against an expected result. An oracle determines whether the actual result is correct. A complete test also includes setup, invocation, assessment and teardown.”

**Keywords:** SUT, test data, actual output, expected output, oracle, test case, setup, invocation, assessment, teardown.

---

# 4. 🎓 LECTURE 4 — Automated Unit Testing Framework Demo (JUnit)

## 4.1 Instructor kya demonstrate karte hain?

Instructor **Eclipse IDE + Java + JUnit** use karte hain. Eclipse sirf demonstration ka IDE hai; important concept JUnit automated testing framework hai. Lecture mein triangle program diya gaya hai jo console se 3 sides leta hai aur `isTriangle()` call karta hai.

## 4.2 Uploaded assignment ka `Demo.java`

```java
import java.util.Scanner;

public class Demo {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);

        System.out.println("Enter side 1: ");
        int side_1 = reader.nextInt();

        System.out.println("Enter side 2: ");
        int side_2 = reader.nextInt();

        System.out.println("Enter side 3: ");
        int side_3 = reader.nextInt();

        if (isTriangle(side_1, side_2, side_3)) {
            System.out.println("This is a triangle.");
        } else {
            System.out.println("This is not a triangle.");
        }

        reader.close();
    }

    public static boolean isTriangle(double a, double b, double c) {
        if ((a + b > c) &&
            (a + c > b) &&
            (b + c > a)) {
            return true;
        }
        return false;
    }
}
```

### Code ka meaning

- `Scanner` console se input read karta hai.
- `main()` three side lengths leta hai.
- `isTriangle()` ko three values pass hoti hain.
- Triangle inequality ki teen conditions check hoti hain:
  - `a + b > c`
  - `a + c > b`
  - `b + c > a`
- Teeno true hain toh triangle valid; warna false.

## 4.3 Automated framework kyun?

JUnit:
- `@Test` annotation se test methods identify karta hai.
- Test methods execute karta hai.
- Assertions se expected condition compare karta hai.
- Pass/fail report deta hai.
- Same tests code changes ke baad dobara run karne deta hai.
- Manual repetitive comparison kam karta hai.

### JUnit vs Pytest mapping

| JUnit | Pytest |
|---|---|
| `@Test` | `test_...` naming convention |
| `assertEquals(expected, actual)` | `assert actual == expected` |
| `assertTrue(condition)` | `assert condition` |
| `assertFalse(condition)` | `assert not condition` |
| JUnit runner | `pytest` runner |

Ye conceptual mapping hai; frameworks ke saare features identical nahi.

## 4.4 Method ko direct test karna

```java
import org.junit.Test;
import static org.junit.Assert.*;

public class DemoTest {

    @Test
    public void validTriangle_returnsTrue() {
        assertTrue(Demo.isTriangle(3, 4, 5));
    }

    @Test
    public void invalidTriangle_returnsFalse() {
        assertFalse(Demo.isTriangle(1, 2, 3));
    }
}
```

Method direct call hota hai. Console input dene ki zaroorat nahi.

## 4.5 `main()` ko test karna — extra complexity

Lecture mein standard input/output redirect karna demonstrate hota hai:
- `System.in` ko test input se replace karo.
- `System.out` ko output-capture stream par redirect karo.
- `main()` invoke karo.
- Captured output expected output se compare karo.

**Why difficult?**
- Prompts bhi output ka part hain.
- Exact spaces/newlines matter kar sakte hain.
- Windows aur Unix-like systems mein line separator different ho sakta hai.
- Global `System.in`/`System.out` restore karne chahiye.
- Console input format maintain karna padta hai.

### 🧠 MENTOR DESIGN LESSON

Business logic ko console input/output ke saath tightly mix mat karo. Calculation/validation ko separate method mein rakho, taaki direct return value test kar sako. `main()`/UI layer ko thin rakho.

---

# 5. 🎓 LECTURE 5 — Writing Unit Tests & TDD

## 5.1 TDD kya hai?

### 🎓 COURSE SOURCE

**Test-Driven Development (TDD)** mein problem milne par pehla step solution code likhna nahi hota. Pehle test cases create karte hain jo define karte hain ki solution correct kab maana jayega. Phir implementation likhte hain.

Instructor kehte hain ki agar pehle code likh diya aur baad mein tests banaye, toh developer anjaane mein tests ko existing code ke according likh sakta hai — solution ke according nahi.

### 🧠 MENTOR EXPLAINS — TDD cycle

1. Expected behaviour samjho.
2. Test likho.
3. Test run karo — implementation na hone par fail expected hai.
4. Minimum code likho.
5. Test dobara run karo.
6. Code improve/refactor karo, tests green rakho.
7. Next behaviour ke liye repeat.

Red-Green-Refactor TDD ka popular framing hai; lecture ka central idea test-first hai.

## 5.2 🎓 COURSE STORY — Circle calculator

Instructor ek program ka example lete hain jo:
- User se circle ka radius leta hai.
- Radius echo/display karta hai.
- Circle ka area calculate karta hai.
- Circumference calculate karta hai.

Instructor pehle test cases aur expected outputs decide karte hain, phir implementation build karte hain. Maksad hai tests ko implementation bias se bachana.

## 5.3 Expected output precision — test fail hone ka matlab hamesha code bug nahi

Lecture demo mein test fail hota hai. Instructor failure trace dekhte hain aur discover karte hain ki expected numerical values online calculator se copy hui thi, jahan result round off tha. Java output zyada decimal precision de raha tha.

### 🧠 MENTOR EXPLAINS

Test fail hone ke possible reasons:
- Application wrong.
- Expected value wrong.
- Test data wrong.
- Assertion overly strict/loose.
- Output formatting difference.
- Setup issue.

**Correct debugging habit:** Actual result ko blindly expected mat bana do. Pehle requirement ya independent reliable calculation se decide karo ki correct result kya hai.

## 5.4 Negative radius — hidden requirement gap

Instructor observe karte hain ki negative radius validate nahi ho raha. Program negative radius par required error message nahi deta. Lecture non-numeric input jaise `"abc"` ka example bhi discuss karta hai aur “radius must be a number” jaisa error response mention karta hai. Try/catch handling aur JUnit se exception/invalid behaviour test karne ka reference aata hai.

**Lesson:** Happy path ke saath invalid input bhi consider karo. Agar requirement unclear hai, expected behaviour khud invent mat karo — developer/product owner se clarify karo.

## 5.5 Methods `main()` se easier to test kyun?

Method return value direct compare kar sakte hain. Console-driven `main()` mein input/output redirect karna, prompts, whitespace aur OS-specific newline handle karna padta hai. Isliye business logic ko methods/services mein isolate karna testability improve karta hai.

### ⭐ INTERVIEW ANSWER — TDD

“TDD is a development approach in which we write tests before implementing the functionality. The tests define the expected behaviour, then we write code to satisfy them and repeat the cycle as requirements or behaviour are added. This reduces the risk of writing tests that merely confirm the existing implementation.”

---

# 6. 🧩 ASSIGNMENT — Building Unit Tests with JUnit

## 6.1 ZIP mein actual kya diya gaya hai?

Uploaded Module 1 ZIP ke assignment folder mein:
- `Demo.java` — triangle logic.
- `DemoTest.java` — starter test class, initially empty.
- `build.gradle`, `settings.gradle`, Gradle wrapper.
- `README.md` aur `README1.md` — duplicate assignment instructions.

README ke according tumhe `DemoTest.java` likhna hai, `Demo.java` modify nahi karna. Dono `isTriangle()` aur `main()` test karne hain.

## 6.2 Mutation analysis se evaluation

Assignment ka important twist: test suite ko **mutation analysis** se assess kiya jayega.

README mutation examples deta hai:
- Binary operator change karna, jaise `+` ko `-` banana.
- Same type ke variable ko doosre variable se replace karna.

Matlab tumhare tests sirf original code par pass na hon; plausible mistakes introduce hone par fail bhi hone chahiye.

### 🔥 Example — `>` vs `>=`

Correct:
```java
a + b > c
```

Mutant:
```java
a + b >= c
```

Test `3,4,5` dono versions mein true dega — mutant survive kar sakta hai.

Test `1,2,3`:
- Correct: `1 + 2 > 3` → false.
- Mutant: `1 + 2 >= 3` → true.

Ye boundary test mutant ko detect kar sakta hai.

## 6.3 Triangle test ideas

| Input | Expected | Reason |
|---|---|---|
| 3, 4, 5 | true | Valid scalene |
| 2, 2, 3 | true | Valid isosceles |
| 4, 4, 4 | true | Equilateral |
| 1, 2, 3 | false | Equality boundary |
| 2, 3, 6 | false | One side too large |
| 0, 2, 2 | false | Zero side |
| -1, 2, 2 | false | Negative side |
| 1, 3, 2 | false | Permutation/boundary |
| 2, 1, 3 | false | Permutation/boundary |

Ye mentor-suggested candidate cases hain; README exact list prescribe nahi karta.

## 6.4 Assignment ko kaise approach karna hai?

1. Triangle inequality ko apni language mein likho.
2. Har condition ko independently fail karne wale cases socho.
3. Valid triangle ke multiple shapes cover karo.
4. Equality boundary test karo.
5. Variables ki permutations consider karo.
6. `main()` ke liye input supply aur output capture test karo.
7. Console streams redirect karo toh original streams restore karo.
8. Mutants jo survive karte hain, unke liye additional test identify karo.

> 🟠 **Environment note:** Uploaded README Java 8 aur old Gradle setup ka reference deta hai. Modern Java/Gradle par build issue aaye toh pehle environment compatibility check karna; usse test logic ka bug mat samajhna.

---

# 7. 📌 Module 1 — Interview Revision Sheet

| Question | Must-say answer |
|---|---|
| Why testing? | Defects expose karna, risk reduce karna, confidence increase karna |
| Verification vs validation? | Specification conformance vs user need |
| Exhaustive testing possible? | Generally no; state/input space too large |
| State space? | Possible system states ka collection |
| Zune failure? | Leap-year day 366 boundary caused infinite loop |
| Black-box? | Requirements/behaviour based |
| White-box? | Code structure based |
| SUT? | Software/module currently being tested |
| Oracle? | Decides expected correctness |
| Test case? | Input/test data + expected behaviour |
| Four test stages? | Setup, invocation, assessment, teardown |
| TDD? | Test first, then implement |
| Why methods easier? | Direct return value; no console I/O redirection |

## 7.1 Practice — answer aloud

1. Ek example do jahan verification pass but validation fail ho.
2. Wall analogy se testing ki limitation explain karo.
3. Zune bug ka exact boundary explain karo.
4. Test oracle aur assertion mein difference kya hai?
5. Setup aur teardown mein difference?
6. Agar test fail ho toh kaise determine karoge ki code wrong hai ya expected value?
7. TDD implementation bias kaise reduce karta hai?
8. `>` se `>=` mutation ko kaunsa test catch karega?

## 7.2 Module completion criteria

Module tab complete maanenge jab tum:
- Verification/validation ko apne example se explain kar sako.
- Zune story bina notes ke samjha sako.
- State space aur sampling explain kar sako.
- Black-box/white-box distinguish kar sako.
- SUT, oracle, test case aur four stages explain kar sako.
- JUnit assignment ke triangle tests design kar sako.
- Mutation testing ka purpose explain kar sako.

> 💚 **Mentor reminder:** Video English mein hai; notes ka kaam tumhe concept apni Hinglish mein samjhana hai. Agar tum notes padhkar concept apne words mein explain kar pa rahe ho, toh notes apna kaam kar rahe hain.
