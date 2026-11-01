# Module 1 — Introduction to Software Testing
## Complete Hinglish Study Guide | University of Minnesota course material

> **Source policy:** This guide is based on the uploaded `module_1.zip`. Course-derived explanations preserve the instructor's sequence and terminology. Extra explanations and practical SDET connections are explicitly labelled. No topic has been removed because it overlaps with previously studied material.

---

# 0. Module inventory and source audit

## What was present in the ZIP

| Resource | Finding | How it is handled |
|---|---|---|
| `subtitles-en.vtt` | Lecture transcript: course introduction, why testing matters, V&V and analysis techniques | Primary source |
| `subtitles-en (1).vtt` | Lecture transcript: why software testing is hard | Primary source |
| `subtitles-en (2).vtt` | Lecture transcript: what exactly is a test; test data, oracle, setup/invocation/assessment/teardown | Primary source |
| `subtitles-en (3).vtt` | Lecture transcript: JUnit/Eclipse demo with triangle example | Primary source |
| `subtitles-en (4).vtt` | Lecture transcript: writing unit tests using TDD and a circle program | Primary source |
| `subtitle.txt`, `subtitle (1).txt`, `subtitle (2).txt`, `subtitle (3).txt` | Plain-text transcript versions / alternate transcript files | Read and compared with the VTT material; unique details are retained |
| `README.md` and `README1.md` | Same assignment instructions duplicated | Content retained once; duplicate file is not repeated |
| `Demo.java` | Triangle program supplied as System Under Test (SUT) | Code explained below |
| `DemoTest.java` | Empty starter test class | Assignment deliverable is to write tests here |
| `build.gradle`, Gradle wrapper files | Java 8 + JUnit 4.12 Gradle setup | Setup notes included |

**Important source observation:** the ZIP contains five VTT lecture transcripts. The first is the course introduction, followed by four focused lecture transcripts. The plain-text transcript files are not a perfect one-to-one duplicate set of the VTT files; therefore, unique transcript details have been retained rather than assuming every TXT file is redundant.

## Module learning path

1. Why software testing matters; Verification and Validation (V&V); testing among other analysis techniques.
2. Why testing is inherently hard; sampling, discontinuous software behaviour, state space, Zune leap-year failure, black-box and white-box testing, testing dimensions.
3. What a test is; SUT, unit, test data, actual output, expected output, oracle, test case, setup, invocation, assessment and teardown.
4. Automated unit testing with JUnit; Eclipse demo; testing a triangle method and a `main()` method.
5. Test-Driven Development (TDD); writing tests before implementation; circle calculator example; expected-output precision; negative input; why methods are easier to test than console-driven `main()` methods.
6. Assignment: create `DemoTest.java` for `Demo.isTriangle()` and `Demo.main()`. The assignment evaluates test adequacy using mutation analysis.

---

# 1. Lecture: Course introduction — Why do we test?

## 1.1 Why software testing matters

### COURSE SOURCE

The instructor begins with the fact that writing software is difficult and programmers make mistakes. If software is not adequately tested, failures can have consequences far beyond a small bug.

The lecture gives historical examples from 2016:
- Yahoo: a major user-information leak.
- British Airways: a scheduling-system problem associated with cancelled reservations and flights.
- Jeep: a security issue that could allow remote compromise of vehicle functions.
- Democratic National Committee: email-server compromise.
- Bangladesh Bank: a large financial loss due to software/security weaknesses.
- Nest thermostat: a software update that disrupted heating control.
- Therac-25: a radiation-treatment machine associated with deaths due to software-related failures.

The instructor's central point is not to memorize the figures in those historical examples. It is to understand that software failures can affect:
- Money and business continuity.
- Privacy and security.
- Critical infrastructure.
- Physical safety and human life.
- Customer trust and product acceptance.

### MENTOR EXPLANATION

Testing is not just about checking whether a button works. Imagine:
- A payment succeeds in the UI but the account is charged twice.
- A booking system displays a confirmed booking but does not persist it.
- A deployment works for one user but fails for a particular date, timezone, or account state.
- A medical or industrial system gives an unsafe output.

A visible UI success message is only one observation. A tester has to ask whether the whole expected behaviour is correct.

### PROJECT APPLICATION

For a retail application, a checkout test should not stop at “Order placed” appearing on screen. Depending on the requirements, you may also need to verify:
- An order record was created.
- The correct customer owns the order.
- The correct amount was charged.
- Inventory was updated correctly.
- The order is visible in order history.
- A retry does not create a duplicate order.

These are examples of the broader consequences that motivate testing; they are practical extensions, not additional examples quoted from the lecture.

## 1.2 Verification and Validation

### COURSE SOURCE

The instructor distinguishes two questions:

| Term | Question | What is being checked? |
|---|---|---|
| **Verification** | “Are we building the software right?” | Does the software conform to its requirements/specification? |
| **Validation** | “Are we building the right product?” | Does the resulting product meet the user's/customer's actual needs? |

The lecture emphasizes that requirements themselves can be wrong or incomplete. A product can conform to a written requirement and still fail to solve the customer's real problem.

Both verification and validation are needed.

### MENTOR EXPLANATION

Suppose a requirement says: “The search page must show 10 products.”

- Verification: does the page show 10 products according to the written requirement?
- Validation: is showing only 10 products actually what users need? Perhaps users need pagination, filters, or a way to see all matching products.

A tester should not blindly assume that every written requirement represents the correct user need. Requirement clarification is part of quality work.

### Interview answer — simple English

“Verification checks whether we are building the product according to the specified requirements. Validation checks whether we are building the right product for the user's needs.”

### Interview answer — stronger version

“Verification is conformance-oriented: we check whether the implementation satisfies the specification. Validation is user-need-oriented: we check whether the product solves the intended problem. A system can pass verification against an incorrect requirement and still fail validation, so both activities are important throughout development.”

**Keywords:** specification, conformance, user needs, right product, right implementation.

## 1.3 Verification and Validation techniques mentioned in the lecture

### COURSE SOURCE

The instructor says that testing is one part of a broader V&V toolbox. The lecture names these techniques:

1. **Requirements understanding and validation** — before creating tests, understand what the software does and should do.
2. **Inspections** — other people examine the work/code.
3. **Design discussions / walkthroughs** — discuss whether the planned design will meet requirements such as performance and security.
4. **Static analysis** — examine a program without relying on executing it, looking for issues such as integer overflow or null-pointer dereferences.
5. **Testing** — execute the software and observe whether it behaves as expected.
6. **Runtime verification** — observe behaviour while the software is running; if anomalous behaviour is detected, the system may be shut down or inspected.

The instructor explains why testing receives special attention: testing can examine the whole system in its intended execution environment, including interactions with the operating system, processor, compiler, devices, network, linker, loader and other software. Testing is also useful for assessing behaviours such as performance, and customers may require a test suite as evidence that a product behaves as expected. Tests can also document expected behaviour.

### MENTOR EXPLANATION

Do not confuse these techniques:

- **Static analysis:** inspect code without running the application.
- **Dynamic testing:** run the software with inputs and observe behaviour.
- **Inspection/review:** a human examines requirements, design, code or test artefacts.
- **Runtime monitoring/verification:** observe a live system while it operates.

No single technique catches every defect. A mature quality strategy combines techniques.

## 1.4 Testing is incomplete — the objective is effective testing

### COURSE SOURCE

The lecture emphasizes that even simple software may have an enormous number of possible tests. Exhaustive testing is generally not feasible. The course's goal is to make testing effective despite its incompleteness.

This is a key idea to carry into the rest of the course:

> We cannot test every possible behaviour, so we need techniques that help us select useful tests.

### MENTOR EXPLANATION

A form may accept:
- Many possible names.
- Thousands of email addresses.
- Different passwords.
- Different account states.
- Different browsers and devices.
- Different network conditions.

Trying every combination is usually impossible. The tester must select test data intelligently. Later lectures and modules introduce techniques for doing that.

## 1.5 The instructor's analysis-technique “square”

### COURSE SOURCE

The instructor introduces a conceptual space with two dimensions:

- **Accuracy tendency:** pessimistic versus optimistic.
- **Property complexity:** simple properties versus complex properties.

The lecture uses these terms:

- **Optimistic technique:** may say the program is correct when it is actually wrong.
- **Pessimistic technique:** may report a problem even though the program is actually correct.
- Moving toward the centre of the diagram represents more accurate results.
- Along the vertical dimension, the techniques differ in how complex a property they can examine.

Examples and ideas discussed:

| Technique | Lecture's explanation |
|---|---|
| Typical testing | A few tests pass, so a developer may optimistically conclude the code works, even though untested cases may fail |
| Simple program analysis / Lint-like tools | Can warn about possible issues such as overflow or null-pointer dereference; may be pessimistic and produce false warnings |
| Type checking | Checks relatively simple properties accurately; the lecture compares language type systems |
| Static analysis | Checks program properties without executing the program; the lecture distinguishes sound and unsound tools |
| Coverage testing | Adds explicit coverage objectives/metrics to make testing more rigorous |
| Model checking | Described in the lecture as equivalent to exhaustive testing for certain kinds of systems/properties |
| Automated testing | Allows many more tests to be run efficiently |
| Theorem proving | Uses mathematical reasoning to prove complex properties, but requires substantial effort |

The instructor also mentions the **halting problem**: it is not theoretically possible to build a general method that decides whether every arbitrary program will eventually halt. The lecture uses this to explain why perfect verification of every property of every program is not achievable.

### Important nuance

The course's diagram is a teaching model. Do not turn it into an oversimplified claim that one tool is always “better” than another. The instructor's conclusion is that we need multiple techniques and should choose an appropriate tool for the problem.

### Sound vs unsound static analysis — as described in the lecture

- **Sound static analysis:** will not claim that a wrong program is right, but may produce false warnings.
- **Unsound static analysis:** may allow an incorrect program to pass, but tends to avoid some false warnings.
- The instructor notes that practitioners may prefer tools with fewer false alarms because excessive warnings are costly to investigate.

### MENTOR EXPLANATION

A false positive means a tool reports a problem that is not actually a defect. A false negative means a real defect is not reported.

Example:
- A static analyser warns that a value could be null. If the code path guarantees it is never null, that warning may be a false positive.
- A tool misses a real null dereference on a path it does not analyse. That is a false negative.

Be careful: “sound” and “unsound” have formal meanings in program analysis. Use the instructor's definitions when discussing this particular lecture, and study the formal definitions more deeply when the course reaches static analysis.

### INTERVIEW ANSWER

“Testing is one technique within verification and validation. Other techniques include inspections, design reviews, static analysis and runtime verification. Since exhaustive testing is not feasible, we combine techniques to improve confidence and choose techniques according to the properties we need to check.”

---

# 2. Lecture: Why is software testing hard?

## 2.1 Testing samples possible behaviour

### COURSE SOURCE

The instructor compares software testing with testing physical systems such as bridges or steel girders. In physical testing, engineers can test increasing loads and often infer behaviour between sampled points because the system behaves relatively continuously.

Software is different. It is often **discontinuous**: a tiny change in an input or state can lead to a very different outcome. Passing one test does not necessarily tell us that nearby inputs will also pass.

The lecture uses a wall analogy:
- The wall represents all possible behaviours of the system.
- The tester can only look through small openings.
- Each test is like looking through one small opening.
- The tester cannot directly see every possible behaviour.

### MENTOR EXPLANATION

Suppose an age field accepts values 18 through 60.

Testing age 30 successfully does not prove that:
- 17 is rejected.
- 18 is accepted.
- 60 is accepted.
- 61 is rejected.
- 18.5 is handled correctly.
- A blank value is handled correctly.
- A very large integer is handled correctly.

One successful point gives limited evidence. Software behaviour can change sharply at boundaries.

## 2.2 State space

### COURSE SOURCE

The instructor describes the **state space** as the large collection of possible values/states in which the system may exist. Bugs may occur at different points in this space. Testing checks selected points, but those checks do not automatically tell us what happens at nearby points.

Even small software systems can have trillions of possible states. Therefore, exhaustive testing is not realistic.

### MENTOR EXPLANATION

A state is not just one input field. It can include:
- Current user/account state.
- Current database records.
- Cart contents.
- Authentication state.
- Current date/time.
- Network status.
- Feature flags.
- Browser/device configuration.

The combinations can grow extremely quickly.

## 2.3 Zune media player — leap-year example

### COURSE SOURCE

The lecture discusses a Microsoft Zune media-player failure on New Year's Eve in 2008. The device used a date representation based on the number of days since 1980. A loop converted that day count into a year/day representation.

The failure occurred on the last day of a leap year: day 366.

The relevant logic, as explained by the instructor, had a condition equivalent to:
- Continue while `days > 365`.
- If it is a leap year, handle the leap-year case only when `days > 366`.
- For exactly day 366 in a leap year, the condition does not take the expected branch.
- The loop repeats without changing the day count.
- The result is an **infinite loop**.

The comparison should have handled the boundary using `>= 366`, not only `> 366`.

### Why this is a powerful testing example

To expose the defect, the test needed to select exactly the right condition:
- A leap year.
- The last day of that leap year.
- Day number 366.

A random ordinary date would probably not reveal the bug.

### MENTOR EXPLANATION — boundary thinking

When a rule contains a comparison such as:
- `> 365`
- `>= 18`
- `< 100`
- `<= 10`

ask what happens:
1. Just below the boundary.
2. Exactly at the boundary.
3. Just above the boundary.

For the Zune example, the critical value was exactly 366. The defect was not exposed by testing only day 365 or day 367.

### PROJECT APPLICATION

For an e-commerce discount:
- Discount applies for cart total greater than ₹1,000.

Do not test only ₹1,500. Consider:
- ₹999.99
- ₹1,000.00
- ₹1,000.01

Whether equality should qualify depends on the exact requirement. The tester must not guess.

## 2.4 Think like a helpful adversary

### COURSE SOURCE

The instructor says a good tester needs knowledge of the system and must think like a **helpful adversary**. The tester should ask: “What can I do to break this?”

The lecture highlights:
- Boundary conditions.
- Unexpected values.
- Negative values.
- Very large values.
- Values that may trigger loops or unusual control flow.

The instructor's point is not to attack the system maliciously. It is to deliberately choose inputs that reveal weaknesses.

### MENTOR EXPLANATION

A tester should combine two mindsets:
- Understand what the product is supposed to do.
- Challenge assumptions that could cause it to fail.

“Happy path only” testing is insufficient. Try valid, invalid, boundary, unexpected and state-dependent conditions.

## 2.5 Black-box and white-box testing

### COURSE SOURCE

The instructor distinguishes:

- **Black-box testing:** testing from the requirements; the tester focuses on what the system should do, without needing to inspect the internal code.
- **White-box testing:** examining the code to identify areas where programmers may have made mistakes, such as boundary conditions.

The Zune example can be approached from both perspectives:
- Requirements might tell us how dates should be handled.
- Code inspection can reveal the loop and comparison that create the boundary defect.

### MENTOR EXPLANATION

Example: Login feature.

**Black-box perspective**
- Valid username/password should log in.
- Invalid password should be rejected.
- Locked account should follow the specified behaviour.
- Password reset should follow the requirements.

**White-box perspective**
- Inspect branches for successful and failed authentication.
- Check whether lockout counters update correctly.
- Check whether a token is generated only after successful authentication.
- Identify untested conditional paths.

Black-box and white-box are perspectives, not mutually exclusive job titles. A tester can use both.

## 2.6 Three dimensions for thinking about testing

### COURSE SOURCE

The instructor introduces three axes/dimensions:

1. **Scale**
   - Unit testing: small units, usually a method or class-level unit in the lecture's Java framing.
   - Integration testing: larger pieces/subsystems and their interactions.
   - System testing: the whole system, often evaluated against customer use cases.

2. **Process**
   - Test-driven development: tests are written before implementation.
   - Test-after / conventional process: tests are written while or after the software is developed.
   - In either approach, iteration and re-testing are expected.

3. **Purpose**
   - Functionality.
   - Performance.
   - Security.
   - Usability.
   - Availability.

The lecture mentions Netflix's **Chaos Monkey** as an availability/resilience example: it deliberately disrupts hardware or software processes to observe how the system responds.

### MENTOR EXPLANATION

These dimensions answer different questions:

- Scale: “How much of the system am I testing?”
- Process: “When am I creating/running tests relative to implementation?”
- Purpose: “What quality or behaviour am I trying to evaluate?”

Do not confuse them. A unit test can be written test-first or test-after. A system test can focus on performance or functionality. These are separate dimensions.

### Interview answer — simple English

“Software testing is hard because we can execute only a sample of all possible inputs and system states. Software can behave discontinuously, so passing one test does not guarantee nearby cases will pass. We use risk, boundary knowledge, black-box and white-box techniques to select effective tests.”

### Interview answer — stronger version

“Testing is inherently incomplete because the state space of even a relatively small program can be enormous. Unlike many physical systems, software behaviour is often discontinuous, so a successful test at one input does not establish correctness for nearby inputs. The Zune leap-year failure is a good example: a very specific boundary value, day 366 in a leap year, triggered an infinite loop. Effective testing therefore requires domain knowledge, boundary-focused test selection, requirements-based black-box testing and code-informed white-box testing.”

**Keywords:** sampling, state space, discontinuous behaviour, boundary condition, helpful adversary, black box, white box, unit/integration/system, TDD, purpose.

---

# 3. Lecture: What exactly is a test?

## 3.1 Software Under Test (SUT)

### COURSE SOURCE

The lecture starts with **Software Under Test (SUT)**. The SUT does not have to be the entire finished product. It can be a completed part or subset of a program whose behaviour can be exercised.

A unit may be:
- A method.
- A function.
- A subroutine.
- A procedure.
- A small, defined set of steps/tasks with expected behaviour.

This is the context in which the lecture introduces unit testing.

### MENTOR EXPLANATION

In a Python project, the SUT might be:
- A function that calculates tax.
- A Django service method that creates an order.
- A serializer validation method.
- An API endpoint.
- A small component that formats a response.

The test target should be clearly identified. “Test the application” is broad; “test the order-total calculation for discounts and tax” is a more precise target.

## 3.2 Test data / input

### COURSE SOURCE

A test needs information on which the SUT will act. This is the **input** or **test data**.

The instructor describes different ways to select/generate test data:
- Based on a profile of expected user behaviour.
- Based on probability or user studies.
- Deliberately chosen values that often expose errors, such as zero, values larger than expected, or words where numbers are expected.

### MENTOR EXPLANATION

Test data should be selected for a reason. It is not just “some sample values”.

For a quantity field:
- Typical valid value: 5.
- Zero: 0.
- Negative: -1.
- Large value: 1,000,000.
- Wrong data type: `"five"`.
- Empty value: `""` or `None`, depending on the interface.

The correct expected behaviour must come from requirements or a trusted oracle, not from guessing.

## 3.3 Actual output and expected output

### COURSE SOURCE

After providing test data, the tester executes the SUT and observes its behaviour/output.

The tester then asks: “Is this correct?”

The lecture distinguishes:
- **Actual output:** what the software really produced when executed.
- **Expected output:** what should have happened according to the test's expectation.

A comparison is needed to decide whether the actual result is acceptable.

## 3.4 Test oracle

### COURSE SOURCE

The component/person/process that decides whether the actual behaviour matches the expected behaviour is called the **Oracle**.

Historically, the oracle may be the human tester/developer who runs the test and judges the result. The lecture explains that humans can be unreliable when comparing outputs, so automated oracles are increasingly important.

JUnit for Java and PyUnit for Python are given as examples of frameworks that can compare expected values/conditions with actual results and report pass/fail.

### MENTOR EXPLANATION

An oracle is not simply the test framework. The framework executes assertions, but the expected result must come from somewhere trustworthy:
- A requirement.
- A business rule.
- A mathematical calculation.
- A specification.
- A known-good reference.
- A second implementation or consistency check.

Example:
```python
def calculate_total(price, quantity):
    return price * quantity

def test_calculate_total():
    actual = calculate_total(100, 3)
    expected = 300
    assert actual == expected
```

Here, the assertion performs the comparison. The expected value `300` is the oracle value supplied by the test author based on the intended rule.

**Important:** A test can pass and still be wrong if its expected result is wrong. A weak oracle can make a weak test suite look healthy.

## 3.5 Test case

### COURSE SOURCE

The lecture explains that test data and the expected output together form the essential content of a **test case**.

A test case is not merely an input value. It includes the expected behaviour/result against which the actual output is assessed.

### MENTOR EXPLANATION

A practical test case often also records:
- Test case ID.
- Requirement/reference.
- Preconditions.
- Test steps.
- Test data.
- Expected result.
- Actual result.
- Status.
- Notes/evidence.

The lecture's conceptual definition focuses on input/test data and expected output. The additional fields above are a practical test-management format.

## 3.6 Four parts of a test: Setup, Invocation, Assessment, Teardown

### COURSE SOURCE

The lecture identifies four parts:

| Part | Meaning in the lecture |
|---|---|
| **Setup** | Put the SUT into the state/conditions in which the test input makes sense |
| **Invocation** | Execute the SUT using the provided input/test data |
| **Assessment** | Observe behaviour and compare actual behaviour with expected behaviour |
| **Teardown** | Clean up or restore the system after the test |

The instructor gives examples:
- To test deleting a product, the product must already exist.
- A user may need to be logged in before performing an action.
- A shared setup can be reused across multiple test cases.
- Teardown may close database connections/file handles, delete created data, or restore deleted data.

### MENTOR EXPLANATION — map to Pytest

```python
import pytest

@pytest.fixture
def product():
    # SETUP: create a product needed by the test
    item = {"id": 101, "name": "Keyboard", "stock": 5}

    yield item

    # TEARDOWN: cleanup after the test
    item.clear()


def test_product_exists(product):
    # INVOCATION: in this simple example, the fixture supplies the SUT data
    actual_name = product["name"]

    # ASSESSMENT
    assert actual_name == "Keyboard"
```

Line-by-line:
- `@pytest.fixture` defines reusable setup.
- The code before `yield` prepares the test state.
- `yield item` provides the prepared object to the test.
- The test body performs the action/observation and assertion.
- Code after `yield` performs teardown.

This is a mentor-created illustration of the lecture's four parts. It is not code shown in the uploaded course transcript.

### Real-world Playwright connection

For a UI test that deletes a product:
- Setup: create a product through API or a fixture; log in as an authorized user.
- Invocation: open the product page and click Delete.
- Assessment: verify the product is no longer present and the expected success behaviour occurred.
- Teardown: remove any remaining test data or reset state.

A reusable setup is valuable because many tests may need the same login or baseline data. However, avoid shared mutable state that makes tests depend on execution order.

## 3.7 Common mistakes

1. Treating test data alone as the complete test case.
2. Writing assertions without knowing the correct expected result.
3. Forgetting preconditions, such as login or required records.
4. Letting one test leave data that changes the next test's result.
5. Doing all setup repeatedly inside every test instead of reusing suitable fixtures.
6. Skipping teardown when tests create persistent data or open resources.
7. Assuming a green test report proves the product is correct; it proves only that the executed checks passed.

### Interview answer — simple English

“A test includes test data, execution of the software under test, and comparison of actual behaviour with expected behaviour using an oracle. A test also has setup, invocation, assessment and teardown stages.”

### Interview answer — stronger version

“A test is a controlled execution of a software unit or system using selected test data, followed by assessment of the observed behaviour against an expected result. The oracle determines whether the actual result is correct. A complete test also needs setup to establish preconditions and teardown to clean up or restore state. Reusable setup and reliable teardown make test suites more consistent and easier to maintain.”

**Keywords:** SUT, unit, test data, actual output, expected output, oracle, test case, setup, invocation, assessment, teardown.

---

# 4. Lecture: Automated unit testing framework demo — JUnit and triangle example

## 4.1 What the instructor demonstrates

### COURSE SOURCE

The instructor uses:
- Eclipse, an Integrated Development Environment (IDE).
- Java.
- JUnit, an automated unit testing framework.
- A simple `Demo` class that reads three side lengths and calls `isTriangle()`.

The lecture says Eclipse is the IDE used for the demonstration, but other IDEs can also support JUnit. The key concept is the automated testing framework, not Eclipse itself.

## 4.2 The supplied `Demo.java`

The uploaded assignment contains this code:

```java
import java.util.Scanner;

public class Demo {

    public static void main(String[] args) {
        // Reading from System.in
        Scanner reader = new Scanner(System.in);

        System.out.println("Enter side 1: ");
        int side_1 = reader.nextInt();

        System.out.println("Enter side 2: ");
        int side_2 = reader.nextInt();

        System.out.println("Enter side 3: ");
        int side_3 = reader.nextInt();

        if (isTriangle(side_1, side_2, side_3)) {
            System.out.println("This is a triangle.");
        }
        else {
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

### Line-by-line explanation

- `import java.util.Scanner;` — imports a class used to read console input.
- `public class Demo` — declares the class being tested.
- `main(String[] args)` — program entry point.
- `new Scanner(System.in)` — reads input from standard input.
- `nextInt()` — reads integer input for each side.
- `isTriangle(...)` — calls the business-logic method.
- The `if/else` prints one of two messages.
- `reader.close()` closes the scanner.
- `isTriangle(double a, double b, double c)` — checks the triangle inequality.
- A valid triangle requires all three conditions to be true:
  - `a + b > c`
  - `a + c > b`
  - `b + c > a`
- The method returns `true` only if all conditions pass; otherwise it returns `false`.

### MENTOR EXPLANATION

The important testing design distinction is that this class has two different kinds of behaviour:
1. A method with a direct return value: `isTriangle()`.
2. A console-driven entry point: `main()`.

The first is relatively easy to test because the test can call the method and compare a Boolean result. The second requires input/output handling, which is more involved.

## 4.3 Why use an automated framework?

### COURSE SOURCE

The lecture explains that JUnit:
- Identifies test methods using annotations such as `@Test`.
- Executes tests.
- Uses assertions to determine whether conditions are true/false or values are equal.
- Produces a report indicating which tests passed or failed.
- Helps remove the human element from repetitive comparisons.
- Makes it practical to rerun a suite after code changes.

The instructor notes that similar testing frameworks exist for other languages, including Python.

### MENTOR EXPLANATION — JUnit to Pytest mapping

| JUnit concept | Pytest equivalent / related idea |
|---|---|
| `@Test` annotation | Test function discovered by naming convention, e.g. `test_...` |
| `assertEquals(expected, actual)` | `assert actual == expected` |
| `assertTrue(condition)` | `assert condition` |
| `assertFalse(condition)` | `assert not condition` |
| Test class/method structure | Pytest test module and test functions/classes |
| JUnit test runner/report | `pytest` runner and its output/plugins |

This mapping is to help a Python/Pytest learner understand the Java demonstration. It does not mean JUnit and Pytest are identical in every feature.

## 4.4 Testing `isTriangle()` directly

Example JUnit 4 test:

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

Explanation:
- `@Test` marks a method as a test.
- `assertTrue(...)` checks that the method returns `true`.
- `assertFalse(...)` checks that the method returns `false`.
- `Demo.isTriangle(...)` is called directly; no console interaction is needed.

**Note:** This is a mentor-created minimal illustration consistent with the JUnit 4.12 dependency in the uploaded assignment. The uploaded starter `DemoTest.java` itself is empty.

## 4.5 Testing `main()` and console input/output

### COURSE SOURCE

The lecture demonstrates that testing `main()` requires redirecting standard input and output:
- Provide test input through a byte input stream.
- Capture console output through a byte output stream.
- Invoke `main()`.
- Compare the captured output with the expected output.

The lecture calls some of this setup boilerplate. It is more complicated than calling a method that returns a Boolean or number.

### MENTOR EXPLANATION

A simplified JUnit 4 style illustration:

```java
import org.junit.Test;
import static org.junit.Assert.*;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class DemoMainTest {

    @Test
    public void main_printsTriangleMessage() {
        String input = "3\n4\n5\n";
        ByteArrayInputStream in =
            new ByteArrayInputStream(input.getBytes());

        ByteArrayOutputStream out = new ByteArrayOutputStream();

        System.setIn(in);
        System.setOut(new PrintStream(out));

        Demo.main(new String[]{});

        String actual = out.toString();
        assertTrue(actual.contains("This is a triangle."));
    }
}
```

This is an illustrative pattern, not a complete production-ready test. A robust test should also restore the original `System.in` and `System.out` in a `finally` block so that global process state does not leak into other tests.

### Why console tests are more complicated

- The test must provide input in the exact expected format.
- The test must capture output.
- Output includes prompts, spaces and line separators.
- Newline conventions can differ between Windows, macOS and Unix-like systems.
- Exact floating-point output can be sensitive to precision.
- Global `System.in` and `System.out` state must be restored.

### Instructor's design lesson

Methods are easier to test because a test can compare return values directly, such as:
- Boolean values.
- Numbers.
- Strings.

This is one reason methods are useful: they isolate behaviour and reduce the complexity of testing the whole console interaction.

---

# 5. Lecture: Writing unit tests and Test-Driven Development (TDD)

## 5.1 What is TDD?

### COURSE SOURCE

The instructor describes **Test-Driven Development (TDD)** as an approach where, when given a problem, the first step is not to write the solution code. Instead, create test cases that describe how to prove the solution is correct.

The reason given:
- If code is written first, developers may unconsciously write tests that merely confirm the code they already produced.
- If tests are written first, they are more likely to represent the intended solution rather than the implementation.
- Tests are created while the problem and expected behaviour are being considered.
- The implementation is then developed to satisfy those tests.

The lecture contrasts test-first with test-after and explains that iteration is still necessary: code changes, tests are rerun, and failures are investigated.

### MENTOR EXPLANATION

A simple TDD cycle is often expressed as:

1. Write a test for a behaviour that does not exist yet.
2. Run it and observe failure.
3. Write the minimum implementation needed to satisfy the test.
4. Run the test again.
5. Refactor while keeping tests green.
6. Repeat for the next behaviour.

The uploaded transcript emphasizes writing tests first and then building code to meet them. The familiar Red-Green-Refactor wording is a helpful extension, not necessarily the exact wording used in the supplied transcript.

## 5.2 Circle calculator example

### COURSE SOURCE

The instructor's TDD example is a program that:
- Asks the user for the radius of a circle.
- Echoes the input/radius.
- Reports the circle's area.
- Reports the circle's circumference.

The class first considers the test cases and expected output, then develops the code and runs the tests.

The instructor explains that the test cases should represent the intended solution before the implementation influences the test author's thinking.

## 5.3 Expected output must be accurate

### COURSE SOURCE

During the demonstration, a test fails because the expected output does not exactly match the program's actual output.

The instructor investigates the failure trace and finds that the expected numerical values were copied from an online calculator that rounded the result. Java produced more decimal precision. The test's expected output was therefore incomplete.

The instructor updates the expected values to match the required precision, reruns the suite, and gets passing tests.

### MENTOR EXPLANATION

A failing test does not automatically mean the application code is wrong. Possible causes include:
- The application behaviour is wrong.
- The expected value is wrong.
- The test data is wrong.
- The assertion is too strict or too loose.
- The output formatting differs.
- The test setup is incorrect.

When a test fails, compare expected and actual carefully before changing either the test or the application.

**Important testing discipline:** Never blindly change the expected result to whatever the application currently returns. First establish which result is correct from the requirement or a reliable independent calculation. In the course demo, the instructor discovers the expected value had been rounded by the external calculator.

## 5.4 Negative radius — a requirement gap exposed by test-first thinking

### COURSE SOURCE

The instructor then points out that the program does not validate the radius. If a negative radius is entered, the current implementation does not produce the expected error message.

This reveals a gap between the intended behaviour and the code supplied by the developers.

The lecture's key lesson:
- A test may fail because the implementation does not meet the intended requirement.
- The tester should communicate that gap to the development team.
- If the code is written first and the tests are derived only from the code, the missing negative-radius behaviour may never be considered.

The instructor also mentions a non-numeric radius such as `"abc"` and an expected error message like “radius must be a number”. The transcript notes that try/catch constructs can be used to handle such cases and that JUnit can capture/test them.

### MENTOR EXPLANATION

Separate these questions:
1. What should happen for a negative radius?
2. What should happen for text input instead of a number?
3. What does the current code actually do?
4. Is the expected behaviour documented or agreed with the product owner/developer?

A tester should report the requirement gap rather than silently inventing product behaviour.

## 5.5 Assertions discussed in the lecture

The instructor mentions different assertion styles, including:
- `assertEqual`
- `assertTrue`
- `assertFalse`

These represent different ways to express expected conditions.

### Pytest equivalents

```python
assert actual == expected
assert condition
assert not condition
```

Pytest uses Python's `assert` statement, while JUnit provides assertion methods such as `assertEquals`, `assertTrue` and `assertFalse`.

## 5.6 Why methods are easier to test than `main()`

### COURSE SOURCE

The instructor concludes that testing methods is generally easier than testing a console-driven `main()` method:
- Method return values can be compared directly.
- Testing `main()` may require redirecting standard input/output.
- Output can include formatting and platform-specific line separators.
- Windows, macOS and Unix-like systems may use different newline characters.
- These complications make main-method testing more involved.

### MENTOR EXPLANATION

This is a design-for-testability lesson. Keep business logic in methods/services and keep the entry point thin.

Instead of placing all logic inside:
```python
def main():
    # read input
    # calculate total
    # validate
    # print everything
    ...
```

Prefer:
```python
def calculate_total(price, quantity):
    return price * quantity

def main():
    # collect input
    # call calculate_total()
    # display result
    ...
```

Now the calculation can be tested directly with normal inputs and expected return values. This is a general design illustration, not code from the course.

## 5.7 Common mistakes

1. Writing tests after implementation and deriving expectations from the code instead of requirements.
2. Writing only happy-path tests.
3. Using rounded expected values for precise numerical output.
4. Changing expected values simply to make a failing test pass.
5. Forgetting invalid input such as negative or non-numeric values.
6. Testing only the console entry point when the core logic can be tested directly.
7. Not rerunning the full relevant test suite after code changes.
8. Treating a green test run as proof that every possible behaviour is correct.

### Interview answer — simple English

“TDD means writing test cases before implementing the functionality. We first define the expected behaviour, then write code to satisfy those tests, and rerun the tests as the code changes.”

### Interview answer — stronger version

“In Test-Driven Development, tests are created from the expected behaviour before the implementation is written. This helps reduce implementation bias because the tests are not simply derived from the code that already exists. The developer then implements the functionality, runs the tests, investigates failures and iterates. TDD does not eliminate the need for exploratory testing or broader integration and system testing, but it gives a clear feedback loop for the behaviour covered by the tests.”

**Keywords:** test-first, expected behaviour, implementation bias, iteration, regression, assertions, invalid input, testability.

---

# 6. Assignment — Building Unit Tests with JUnit

## 6.1 Assignment brief from the uploaded README

### COURSE SOURCE

The assignment is titled **Building Unit Tests with JUnit**.

The task:
- Create `DemoTest.java`.
- Test the supplied `Demo` class.
- Test both `isTriangle()` and `main()`.
- Do not modify the supplied `Demo.java`.
- Submit `DemoTest.java`.

The README says the assignment measures test adequacy using **mutation analysis**. The course has generated variations of `Demo.java`, each with one fault introduced. Examples mentioned:
- Replacing a binary operator with another operator, such as `+` instead of `-`.
- Replacing one variable with another variable of the same type, such as substituting `a` for `b`.

Your test suite is evaluated on whether it detects these mutated versions.

## 6.2 Project structure from the ZIP

```text
IntroToUnitTesting/
├── build.gradle
├── settings.gradle
├── gradlew
├── gradlew.bat
├── gradle/
│   └── wrapper/
├── README.md
├── README1.md
└── src/
    ├── main/
    │   └── java/
    │       └── Demo.java
    └── test/
        └── java/
            └── DemoTest.java
```

The supplied `DemoTest.java` is currently an empty class with a comment telling you to test both methods.

## 6.3 Build configuration from the uploaded project

The uploaded `build.gradle`:
- Applies the Java plugin.
- Requires Java 8.
- Sets source and target compatibility to Java 8.
- Uses the `jcenter()` repository.
- Declares `junit:junit:4.12` as a test dependency.

The README says Java 8 JDK is required and warns that the project does not support Java 9 in its original configuration. This is the course assignment's historical setup, not a claim that modern Java projects should use Java 8.

### Important environment note

Do not assume this old project will run unchanged with a modern Java/Gradle environment. The README explicitly describes a Java 8 requirement and an older Gradle setup. If the project fails on a modern machine, first distinguish:
- A problem in the assignment/test code.
- A compatibility problem in the historical build configuration.
- A dependency/repository availability problem.

The uploaded files do not establish which Java/Gradle versions are currently installed on your computer.

## 6.4 Triangle behaviour to test

For three side lengths `a`, `b`, and `c`, the supplied method returns true only if all three conditions hold:

```text
a + b > c
a + c > b
b + c > a
```

Think about categories, not just a few random examples.

| Category | Example input | Expected result | Why it matters |
|---|---:|---|---|
| Valid scalene triangle | 3, 4, 5 | `true` | Ordinary valid case |
| Valid isosceles triangle | 2, 2, 3 | `true` | Equal sides |
| Valid equilateral triangle | 4, 4, 4 | `true` | All sides equal |
| One boundary equality | 1, 2, 3 | `false` | Triangle inequality is strict |
| One side too large | 2, 3, 6 | `false` | Detects invalid combination |
| Zero side | 0, 2, 2 | `false` | Invalid/edge input |
| Negative side | -1, 2, 2 | `false` | Unexpected input |
| Different invalid permutations | 1, 3, 2; 2, 1, 3 | `false` | Helps detect variable/operator mistakes |

These are mentor-selected candidate cases derived from the supplied triangle rule. The course README does not prescribe this exact test list.

## 6.5 Mutation analysis — understand the purpose

### COURSE SOURCE

Mutation analysis introduces small faults into the original program. A good test suite should fail when a mutation changes behaviour in a way that the tests should detect.

The README gives examples of mutations:
- Change an operator.
- Substitute one same-typed variable for another.

### MENTOR EXPLANATION

Imagine the correct code has:
```java
a + b > c
```

A mutant might change it to:
```java
a + b >= c
```

If your tests contain only `3, 4, 5`, both versions return true. Your test does not distinguish the original from this mutant.

But for `1, 2, 3`:
- Correct strict comparison: `1 + 2 > 3` is false.
- Mutated inclusive comparison: `1 + 2 >= 3` is true.

That boundary test can detect the mutation.

This is the central mindset of mutation testing: ask whether the tests are sensitive to plausible implementation mistakes.

## 6.6 Your assignment approach

Do not begin by writing a large random list. Work systematically:

1. Read the method and translate each condition into a rule.
2. Identify each condition independently.
3. Create at least one valid case.
4. Create cases that make each inequality fail.
5. Include equality boundaries because the operator is strict `>`.
6. Include permutations to check whether the method uses the correct variables.
7. Test `main()` separately by providing input and checking the printed behaviour.
8. Keep tests independent; restore global input/output streams if you redirect them.
9. Run the suite.
10. Inspect failures; do not change expected values without confirming the rule.

### Suggested test names

- `returnsTrue_forValidScaleneTriangle`
- `returnsTrue_forValidIsoscelesTriangle`
- `returnsTrue_forValidEquilateralTriangle`
- `returnsFalse_whenFirstTwoSidesEqualThird`
- `returnsFalse_whenOneSideIsTooLarge`
- `returnsFalse_forZeroSide`
- `returnsFalse_forNegativeSide`
- `main_printsValidTriangleMessage`
- `main_printsInvalidTriangleMessage`

These are suggested names, not names required by the course.

## 6.7 Assignment deliverable checklist

- [ ] `Demo.java` remains unchanged.
- [ ] `DemoTest.java` contains JUnit tests.
- [ ] Tests cover `isTriangle()`.
- [ ] Tests cover `main()`.
- [ ] Expected results come from the triangle rule and program requirements.
- [ ] Boundary equality is tested.
- [ ] Invalid inputs are considered.
- [ ] Tests are independent and repeatable.
- [ ] The test suite can detect plausible operator/variable mutations.
- [ ] The final test report has been inspected.

---

# 7. Course source vs mentor additions — clear boundary

## Directly supported by the uploaded course material

- Reasons software testing matters and real-world failure examples.
- Verification vs validation.
- Requirements understanding, inspections, design discussions, static analysis, testing and runtime verification.
- Testing is incomplete; exhaustive testing is impractical.
- Optimistic and pessimistic analysis techniques.
- Sound and unsound static analysis as presented in the lecture.
- Type checking, coverage testing, model checking, theorem proving and the halting problem.
- Sampling, discontinuous behaviour and state space.
- Zune leap-year/day-366 infinite-loop example.
- Helpful-adversary mindset.
- Black-box and white-box testing.
- Unit, integration and system testing.
- Test-first/TDD and test-after process.
- Testing purposes: functionality, performance, security, usability and availability.
- Chaos Monkey as an availability example.
- SUT, test data, actual output, expected output, oracle and test case.
- Setup, invocation, assessment and teardown.
- JUnit/Eclipse demonstration, triangle method and console testing.
- Circle-calculator TDD example, expected-output precision and negative-radius gap.
- Why methods are easier to test than console-driven main methods.
- Assignment requirements and mutation-analysis evaluation.

## Mentor explanation / practical extensions in this guide

- Retail, login, checkout and Playwright examples.
- Python/Pytest mapping for JUnit concepts.
- Example Pytest fixture illustrating setup/teardown.
- Example JUnit test snippets.
- Practical test-case fields and test naming suggestions.
- Expanded triangle test-data suggestions.
- Explanation of mutation detection using a strict-vs-inclusive comparison.
- Advice about restoring `System.in`/`System.out`.
- Design-for-testability example separating business logic from console input/output.

These additions are deliberately labelled. They are not presented as verbatim course content.

---

# 8. Topic tracker — Module 1

| Topic | Difficulty | Suggested focused study time | Priority |
|---|---|---:|---|
| Why testing matters | Easy | 20–30 min | Must know |
| Verification vs validation | Easy | 25–35 min | Must know |
| V&V techniques | Medium | 35–45 min | Must know |
| Optimistic/pessimistic analysis square | Hard | 45–60 min | Understand carefully |
| Why testing is hard / sampling | Medium | 30–40 min | Must know |
| State space and discontinuity | Medium | 30–40 min | Must know |
| Zune leap-year example | Medium | 25–35 min | Must know |
| Black-box vs white-box | Easy | 20–30 min | Must know |
| Scale/process/purpose dimensions | Medium | 30–40 min | Must know |
| SUT, test data, oracle, test case | Medium | 35–45 min | Must know |
| Setup/invocation/assessment/teardown | Medium | 35–45 min | Must know |
| JUnit framework demo | Medium | 45–60 min | Must know for course assignment |
| Testing console `main()` | Hard | 45–60 min | Must know for assignment |
| TDD | Medium | 35–45 min | Must know |
| Expected-output precision | Medium | 25–35 min | Must know |
| Mutation analysis | Hard | 45–60 min | Must know for assignment |

**Estimated focused learning time:** approximately 9–12 hours, excluding the time needed to complete and debug the assignment.

## Completion criteria

Module 1 is not complete just because the videos have been watched. You should be able to:

1. Explain verification and validation with your own example.
2. Explain why passing tests do not prove the absence of defects.
3. Describe state space, sampling and discontinuous software behaviour.
4. Explain the Zune day-366 defect without looking at notes.
5. Distinguish black-box and white-box testing.
6. Explain unit, integration and system testing.
7. Define SUT, test data, actual output, expected output and oracle.
8. Explain the four parts of a test.
9. Explain why a wrong expected result can cause a false test failure.
10. Describe TDD and why tests-first can reduce implementation bias.
11. Explain why testing a method is easier than testing console-driven `main()`.
12. Write tests for the supplied triangle method.
13. Explain how a mutation can survive a weak test suite and how a boundary test can kill it.

---

# 9. Practice questions

Try answering before checking your notes.

## Concept checks

1. What is the difference between verification and validation?
2. Why can software testing not usually be exhaustive?
3. What does the wall analogy represent?
4. What is meant by discontinuous software behaviour?
5. Why did the Zune fail on day 366 of a leap year?
6. What is a helpful adversary?
7. Explain black-box and white-box testing.
8. What are the three dimensions of testing described in the lecture?
9. What is the difference between actual output and expected output?
10. What is a test oracle?
11. What is the purpose of setup?
12. What is the difference between assessment and teardown?
13. Why is a method generally easier to test than a console-driven `main()`?
14. What is TDD?
15. Why should a tester not blindly update expected output to match actual output?
16. What is mutation analysis?
17. Why is `1, 2, 3` a valuable triangle test case?

## Scenario questions

### Scenario A — booking date

A booking application works for ordinary dates but fails on December 31 in a leap year.

- What testing concept should come to mind?
- Which test data would you select?
- Would you use black-box testing, white-box testing, or both?

### Scenario B — payment setup

A test tries to refund an order, but the order does not exist.

- Which part of the test lifecycle is missing or incorrect?
- How could reusable setup help?

### Scenario C — expected amount

The application returns `19.999999`, but the expected value is `20.00`.

- Is the application necessarily wrong?
- What should you inspect before changing the assertion?

### Scenario D — weak triangle tests

Your suite tests only `3, 4, 5` and `4, 5, 6`.

- Could a mutation changing `>` to `>=` survive?
- What additional input would help detect it?

---

# 10. Answer key

1. Verification checks conformance to requirements; validation checks whether the product meets user needs.
2. The possible inputs and states are too numerous; testing samples behaviour.
3. It represents all possible system behaviours, of which tests can inspect only selected points.
4. A small change in input/state can cause a sharply different outcome; nearby successful tests do not guarantee correctness.
5. The loop failed to handle exactly day 366 in a leap year, so the value did not change and the loop continued indefinitely.
6. A tester who deliberately thinks about how to expose weaknesses while understanding the intended behaviour.
7. Black-box tests from requirements; white-box tests informed by internal code structure.
8. Scale, process and purpose.
9. Actual output is what the program produced; expected output is what the test says should happen.
10. The mechanism/person/process that determines whether actual behaviour matches expected behaviour.
11. To establish the state/preconditions required for the test.
12. Assessment compares observed behaviour with expectations; teardown cleans up or restores state after execution.
13. Methods can return values directly; `main()` may require input/output redirection and exact formatting checks.
14. TDD creates tests before implementation and then develops code to satisfy them.
15. Because the test expectation may be correct and the implementation may be defective; expected values must be checked against requirements or a reliable oracle.
16. It introduces small faults into a program to see whether the test suite detects them.
17. The strict triangle inequality rejects equality; `1 + 2` is not greater than `3`, so this can detect `>` changed to `>=`.

---

# 11. Suggested study sequence

1. Watch the course lecture.
2. Read the corresponding section in this guide.
3. Explain the concept aloud in your own words.
4. Write one real-world example.
5. Attempt the practice questions without notes.
6. Complete the JUnit assignment.
7. Review every surviving mutation/failing test report if the course platform provides it.
8. Only then move to the next module.

**Mentor rule:** We are not skipping a concept just because it looks familiar. First understand the instructor's framing; then connect it to Python, Pytest, Playwright and real SDET work.
