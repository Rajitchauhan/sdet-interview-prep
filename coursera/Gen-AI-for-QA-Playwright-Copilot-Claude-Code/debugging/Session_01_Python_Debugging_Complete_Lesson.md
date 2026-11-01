# Session 01 — Python Debugging: Tracebacks, Exceptions & Root-Cause Analysis
## Complete Hands-on Lesson | Hinglish | QA Automation / SDET

> **Is lesson ka goal:** Python program fail hone par random changes nahi karne. Tum traceback read karoge, exact failing line identify karoge, bad value ko uske source tak trace karoge, debugger se hypothesis prove karoge aur regression test likhoge.

**Difficulty:** Easy → Medium  
**Estimated focused time:** 3–4 hours  
**Prerequisite:** Basic Python functions, variables, lists/dicts, conditions, exceptions.  
**AI rule:** Is lesson mein AI se direct solution nahi lena. Pehle khud investigate karna hai.

---

# 1. Debugging kya hoti hai?

Suppose tumhare paas ek order application hai. User cart mein 2 products add karta hai. Checkout par application crash ho jaati hai.

Developer kehta hai: “Checkout broken hai.”

QA Automation Engineer ke roop mein tumhara kaam sirf error message forward karna nahi. Tumhe determine karna hai:

- Kya input galat tha?
- Kya application ne input validate nahi kiya?
- Kya function ko wrong data type mila?
- Kya function ne wrong value return ki?
- Kya test setup/fixture ne invalid state create ki?
- Kya actual defect application mein hai ya test mein?

**Debugging = failure ko systematically investigate karke actual cause identify karna.**

Testing defect expose kar sakti hai. Debugging us defect/failure ka reason locate karne mein help karti hai.

## Symptom, error aur root cause ka difference

| Term | Meaning | Example |
|---|---|---|
| Symptom | Jo externally observe hua | Checkout test failed |
| Error/exception | Runtime ne kya report kiya | `TypeError` |
| Failure location | Jis line par execution fail hua | `total = price * quantity` |
| Root cause | Wrong condition/value introduce kahan hui | API se price string aayi aur validation nahi hui |
| Fix | Cause ko correct karna | Input validation/conversion at correct boundary |
| Regression test | Future mein same bug detect karna | String price input validation test |

Important: Exception ki line hamesha root cause nahi hoti. Ho sakta hai bad data usse pehle kisi API, fixture ya caller function se aaya ho.

---

# 2. Python exception aur traceback

## 2.1 Exception kya hai?

Exception runtime par aane wali abnormal condition ko represent karti hai. Example:
- Invalid type ke saath operation.
- Dictionary mein missing key.
- List ka invalid index.
- File missing.
- Module import failure.
- Explicit `raise`.

Python exception raise hone par normal execution current path par stop hota hai, jab tak exception handle na ho.

## 2.2 First debugging example

File: `debug_01.py`

```python
def calculate_total(price, quantity):
    total = price * quantity
    return total


def create_order():
    price = 100
    quantity = "2"
    total = calculate_total(price, quantity)
    return total


print(create_order())
```

Run:

```bash
python debug_01.py
```

Expected output:

```text
200
```

Surprise: Python integer ko string se multiply karne par string repetition karta hai. Isliye `100 * "2"` numeric multiplication nahi, string repetition ke liye invalid operand combination hai? Actually Python `int * str` supported hai: result `"2"` repeated 100 times. Is example ka result 200 nahi hoga; long repeated string milegi.

### Investigation

1. `calculate_total()` ko kaunse arguments mile?
2. `price` ka type kya hai?
3. `quantity` ka type kya hai?
4. Business rule ke mutabik quantity integer honi chahiye ya string?
5. Validation kis boundary par honi chahiye?

Inspect types:

```python
def calculate_total(price, quantity):
    print("price:", repr(price), type(price))
    print("quantity:", repr(quantity), type(quantity))

    total = price * quantity
    return total
```

`repr()` useful hai kyunki string ka representation quotes ke saath dikhata hai.

### Corrected version

```python
def calculate_total(price, quantity):
    if not isinstance(price, (int, float)):
        raise TypeError("price must be numeric")

    if not isinstance(quantity, int):
        raise TypeError("quantity must be an integer")

    return price * quantity
```

But production mein `bool` Python mein `int` ka subclass hai. Agar boolean quantity reject karni hai, use:

```python
if isinstance(quantity, bool) or not isinstance(quantity, int):
    raise TypeError("quantity must be an integer")
```

**Learning:** Sirf crash fix nahi karna; input contract define karna hai.

---

# 3. Traceback ko kaise read karein?

File: `debug_02.py`

```python
def divide_amount(amount, people):
    return amount / people


def split_bill():
    amount = 900
    people = 0
    return divide_amount(amount, people)


def checkout():
    return split_bill()


print(checkout())
```

Run:

```bash
python debug_02.py
```

Expected exception:

```text
ZeroDivisionError: division by zero
```

Traceback ka shape roughly:

```text
Traceback (most recent call last):
  File "...debug_02.py", line 14, in <module>
    print(checkout())
  File "...debug_02.py", line 11, in checkout
    return split_bill()
  File "...debug_02.py", line 7, in split_bill
    return divide_amount(amount, people)
  File "...debug_02.py", line 2, in divide_amount
    return amount / people
ZeroDivisionError: division by zero
```

Exact line numbers tumhare file ke hisaab se differ karenge.

## 3.1 Read karne ka reliable order

**Step A — Last line padho**

`ZeroDivisionError: division by zero`

Isse exception type aur message milta hai.

**Step B — Bottom-most application frame dekho**

`return amount / people`

Yahan actual exception raise hui.

**Step C — Us function ke inputs inspect karo**

`amount = 900`, `people = 0`.

**Step D — Caller chain follow karo**

`divide_amount()` ko `split_bill()` call karta hai. `people` ki value wahan set hui.

**Step E — Root cause identify karo**

Bill split karne ke liye people count zero nahi hona chahiye. Function boundary par validation missing hai, ya upstream business flow invalid count bhej raha hai.

## 3.2 Traceback bottom-to-top kyun investigate karte hain?

Traceback call chain ko show karta hai. Last application frame generally failure location hota hai. Uske upar caller frames batate hain execution wahan tak kaise aaya.

Practical rule:
1. Last line: exception type/message.
2. Bottom relevant frame: failing operation.
3. Caller frames: input kahan se aaya.
4. Business rule: expected state kya thi?

---

# 4. Common Python exceptions — practical examples

Har example ko alag file mein run karo. Pehle error predict karo, phir execute karo.

## 4.1 `NameError`

```python
print(total_price)
```

Cause: `total_price` naam ka variable current scope mein define nahi.

Debug:
- Variable spelling check.
- Assignment execute hui ya nahi?
- Variable local scope mein toh nahi?
- Branch ke andar define karke branch skip toh nahi hui?

## 4.2 `TypeError`

```python
price = 100
discount = "10"
print(price - discount)
```

Cause: incompatible types ke beech subtraction.

Debug:
```python
print(repr(price), type(price))
print(repr(discount), type(discount))
```

Blind conversion mat karo. Confirm karo input contract kya hai.

## 4.3 `ValueError`

```python
age = int("twenty")
```

Cause: string present hai, lekin valid integer representation nahi.

`TypeError` vs `ValueError`:
- TypeError: operation ke liye type inappropriate.
- ValueError: type acceptable ho sakta hai, value acceptable nahi.

## 4.4 `KeyError`

```python
user = {"name": "Aman", "role": "tester"}
print(user["email"])
```

Cause: dictionary mein `email` key nahi.

Possible investigation:
```python
print(user.keys())
print("email" in user)
```

`user.get("email")` use karna tabhi correct hai jab missing email valid state ho. Agar email mandatory hai, missing key ko silently ignore karna bug hide kar sakta hai.

## 4.5 `IndexError`

```python
products = ["Laptop", "Phone"]
print(products[2])
```

Cause: valid indices 0 and 1 hain.

Debug:
```python
print("length:", len(products))
print("requested index:", 2)
```

## 4.6 `AttributeError`

```python
user = None
print(user.name)
```

Cause: `None` par `.name` attribute access.

Root-cause questions:
- User object `None` kyun hai?
- Lookup failed?
- Fixture returned `None`?
- Function return statement missing?
- API response parsing wrong?

## 4.7 `ModuleNotFoundError`

```python
import some_missing_package
```

Check:
```bash
python --version
python -m pip --version
python -m pip show some_missing_package
```

Common issue: package ek interpreter/environment mein install hai, test doosre interpreter se run ho raha hai.

Prefer:
```bash
python -m pip install package_name
```

Isse pip current `python` interpreter se associate hota hai.

## 4.8 `FileNotFoundError`

```python
with open("data/users.json", encoding="utf-8") as file:
    content = file.read()
```

Investigate:
```python
from pathlib import Path

print("Current directory:", Path.cwd())
print("Exists:", Path("data/users.json").exists())
```

Relative path current working directory se resolve hota hai, necessarily script file ke folder se nahi.

---

# 5. Debugging ka first professional habit: values inspect karo

Guess karne se pehle actual runtime state inspect karo.

Useful functions:

```python
print(value)
print(repr(value))
print(type(value))
print(id(value))
```

- `print(value)`: human-readable value.
- `repr(value)`: unambiguous representation, strings ke quotes visible.
- `type(value)`: runtime type.
- `id(value)`: object identity during its lifetime; reference/mutation investigations mein useful.

Example:

```python
email = " user@example.com "
print(repr(email))
print(type(email))
```

Output:
```text
' user@example.com '
<class 'str'>
```

Ab whitespace issue visible ho gaya.

**Caution:** Sensitive values (passwords, tokens, personal data) logs/terminal screenshots mein expose mat karo.

---

# 6. VS Code debugger — step by step

## 6.1 Debugger ka purpose

Debugger program ko pause karke current execution state inspect karne deta hai. Isse tumhe har jagah `print()` add karne ki zaroorat nahi.

## 6.2 Setup

1. VS Code open karo.
2. Python project folder open karo.
3. Correct Python interpreter select karo.
4. Python extension installed/active confirm karo.
5. Buggy `.py` file open karo.
6. Left gutter mein line number ke paas click karke breakpoint set karo.
7. Run and Debug view open karo.
8. Python file/debug configuration select karke start karo.

UI labels VS Code version ke hisaab se slightly change ho sakte hain.

## 6.3 Breakpoint kahan lagana hai?

Example:

```python
def calculate_discount(price, percentage):
    discount = price * percentage / 100
    final_price = price - discount
    return final_price


def checkout():
    price = 1000
    percentage = 20
    return calculate_discount(price, percentage)


print(checkout())
```

Breakpoints:
- `calculate_discount()` ke first line par.
- `checkout()` ke return call par.

## 6.4 Debug controls

| Control | Meaning | Kab use karein |
|---|---|---|
| Continue | Next breakpoint tak run | Jab current state inspect ho chuki |
| Step Over | Current line execute, called function mein enter nahi | Function implementation abhi inspect nahi karni |
| Step Into | Called function ke andar enter | Function ke internal logic ko inspect karna |
| Step Out | Current function se return | Function ka internal flow complete karke caller par jana |
| Restart | Debug session restart | Fresh reproduction |
| Stop | Debug session end | Investigation finish |

## 6.5 Variables panel

Pause hone par inspect:
- `price`
- `percentage`
- `discount`
- `final_price`

Watch panel mein expression add kar sakte ho:
- `price * percentage / 100`
- `type(price)`
- `percentage > 100`

Watch expressions current paused frame ke scope par depend karte hain.

## 6.6 Call Stack

Call Stack batata hai kaunse functions ek doosre ko call karke current line tak aaye.

Example:
```text
<module>
  checkout()
    calculate_discount()
```

Caller frame select karne par us frame ke local variables inspect kar sakte ho.

## 6.7 Conditional breakpoint

Loop mein 500 records hain, lekin tumhe sirf `order_id == 105` par pause karna hai.

Loop line par breakpoint set karo, condition add karo:

```python
order_id == 105
```

Condition true hone par hi pause hoga.

## 6.8 Logpoint

Logpoint execution pause nahi karta; selected line par diagnostic output print karta hai.

Example message:
```text
order_id={order_id}, status={status}
```

Temporary debugging ke liye useful. Production-quality logs ke liye Python logging use karo.

---

# 7. Same problem ko `pdb` se debug karna

VS Code debugger available na ho toh Python built-in debugger `pdb` use kar sakte ho.

File:

```python
def calculate_discount(price, percentage):
    breakpoint()
    discount = price * percentage / 100
    return price - discount


print(calculate_discount(1000, 20))
```

Run:
```bash
python debug_pdb.py
```

Useful commands:

| Command | Meaning |
|---|---|
| `n` | Next line |
| `s` | Step into |
| `c` | Continue |
| `l` | Source listing |
| `p price` | Expression print |
| `pp locals()` | Local variables pretty-print |
| `w` | Stack |
| `u` | Caller frame |
| `d` | Callee frame |
| `q` | Quit debugger |

Try:
```text
p price
p percentage
p price * percentage / 100
n
p discount
```

Debugging ke baad `breakpoint()` remove karo. Unwanted breakpoint CI mein tests ko hang kar sakta hai.

---

# 8. Real QA Automation scenario — API response se wrong value

Suppose API response:

```python
response_data = {
    "product": "Keyboard",
    "price": "1499",
    "quantity": 2
}
```

Code:

```python
def calculate_order_total(data):
    price = data["price"]
    quantity = data["quantity"]
    return price * quantity


total = calculate_order_total(response_data)
print(total)
```

Observed output:
```text
14991499
```

## 8.1 Symptom
Expected total `2998`, actual string `"14991499"`.

## 8.2 First hypothesis
Price string aa raha hai, so string repetition ho rahi hai.

## 8.3 Evidence
```python
print(repr(price), type(price))
print(repr(quantity), type(quantity))
```

## 8.4 Root cause
API response price string hai, lekin calculation code numeric value assume kar raha hai.

## 8.5 Safe fix decision

Do not blindly cast every string. Confirm API contract:
- Kya API price string intentionally return karti hai?
- Currency precision kya hai?
- Decimal use karna chahiye?
- Invalid price format ka expected behaviour kya hai?

For money, binary floating point rounding concerns ke karan `Decimal` often more suitable hai.

Example:

```python
from decimal import Decimal, InvalidOperation

def calculate_order_total(data):
    try:
        price = Decimal(str(data["price"]))
    except (KeyError, InvalidOperation) as exc:
        raise ValueError("A valid product price is required") from exc

    quantity = data.get("quantity")

    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError("quantity must be an integer")

    if quantity < 0:
        raise ValueError("quantity cannot be negative")

    return price * quantity
```

**Mentor point:** Validation policy business rules se derive karo. Example mein negative quantity reject ki gayi hai; real product ke rules verify karne honge.

---

# 9. Exception handling — error ko hide nahi karna

Bad example:

```python
def get_user(user_id):
    try:
        return database_lookup(user_id)
    except Exception:
        return None
```

Problem:
- Any exception becomes `None`.
- Actual DB failure, coding bug, connection error sab hide ho sakte hain.
- Caller ko pata nahi chalta lookup failed kyun.

Better pattern (when adding context):

```python
def get_user(user_id):
    try:
        return database_lookup(user_id)
    except DatabaseError as exc:
        raise UserLookupError(
            f"Could not load user_id={user_id}"
        ) from exc
```

This preserves the original exception as the cause.

Rules:
1. Expected exception types catch karo.
2. Exception ko silently swallow mat karo.
3. Useful context add karo.
4. Original cause preserve karo with `raise ... from exc`.
5. Logs mein secrets mat rakho.

---

# 10. Debugging assignment — tumhari practical test

## Exercise A — Find the exception

```python
def get_discount(user):
    return user["membership"]["discount"]


def checkout(user):
    discount = get_discount(user)
    return 1000 - discount


user = {
    "name": "Aman",
    "membership": None
}

print(checkout(user))
```

Tasks:
1. Predict exception.
2. Run code.
3. Traceback mein failing line locate karo.
4. Caller chain identify karo.
5. `membership` ki actual value/type inspect karo.
6. Root cause explain karo.
7. Decide karo missing membership valid state hai ya invalid.
8. Safe fix implement karo.
9. At least 2 tests likho: valid membership and no membership.

## Exercise B — Wrong output, no exception

```python
def calculate_total(price, quantity):
    return price * quantity


print(calculate_total("250", 3))
```

Tasks:
1. Output predict karo.
2. Run.
3. `repr()` and `type()` use karo.
4. Explain why no exception occurred.
5. Define input contract.
6. Implement validation.
7. Test valid and invalid inputs.

## Exercise C — Trace the caller

```python
def apply_tax(amount, tax_rate):
    return amount + amount * tax_rate


def create_invoice():
    amount = 500
    tax_rate = 18
    return apply_tax(amount, tax_rate)


def export_invoice():
    return create_invoice()


print(export_invoice())
```

Tasks:
1. Is code ka output kya hai?
2. Business requirement agar tax rate 18 percent hai toh code correct hai?
3. Expected total kya hona chahiye?
4. Bug exception nahi, logic error hai. Debugging kaise karoge?
5. Fix and regression test likho.

Hint: Tax rate `18` ko fraction mein convert karna hoga. Lekin solution likhne se pehle expected business calculation explain karo.

---

# 11. Regression test kaise likhein?

Bug fix karne ke baad same bug dobara introduce na ho, isliye regression test add karo.

Example:

```python
import pytest

def calculate_total(price, quantity):
    if not isinstance(price, (int, float)):
        raise TypeError("price must be numeric")
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError("quantity must be an integer")
    return price * quantity


def test_calculate_total_valid_values():
    assert calculate_total(100, 2) == 200


def test_calculate_total_rejects_string_price():
    with pytest.raises(TypeError, match="price must be numeric"):
        calculate_total("100", 2)


def test_calculate_total_rejects_string_quantity():
    with pytest.raises(TypeError, match="quantity must be an integer"):
        calculate_total(100, "2")
```

Run:
```bash
pytest -v
```

Why these tests?
- Valid behaviour preserved.
- String price rejected.
- String quantity rejected.
- Exception message contract checked.

Note: This is a teaching example. Real code may use `Decimal` for money and domain-specific validation.

---

# 12. Common debugging mistakes

1. **Only last error line read karna:** Caller chain ignore ho jaati hai.
2. **Failing line ko root cause maan lena:** Bad value upstream create hui ho sakti hai.
3. **Random print statements add karna:** Focused state inspection better hai.
4. **Type check nahi karna:** Value dekhne mein correct lag sakti hai, type wrong ho sakta hai.
5. **Exception catch karke `None` return karna:** Original failure hide ho sakta hai.
6. **Input contract define na karna:** Fix arbitrary conversion ban sakta hai.
7. **Debugger mein pause chhod dena:** CI hang ho sakta hai.
8. **Fix ke baad test na likhna:** Same defect return ho sakta hai.
9. **Sensitive values print karna:** Credentials expose ho sakte hain.
10. **AI se direct fix lena:** Tum root cause samajhne ka skill develop nahi kar paoge.

---

# 13. Interview preparation

## Q1. What is debugging?

**Simple answer:**
“Debugging is the systematic process of investigating a failure, identifying its root cause, applying a fix and verifying that the issue is resolved.”

**Stronger answer:**
“When a test or application fails, I first reproduce the issue and preserve evidence such as the traceback, logs and input data. I identify the failing layer, inspect runtime values and trace the call stack to understand where the incorrect state originated. After confirming the root cause, I apply the smallest safe fix and add regression coverage. I then rerun the failing test and related suite to ensure the fix has not introduced side effects.”

**Keywords:** Reproduction, traceback, call stack, runtime state, hypothesis, evidence, root cause, minimal fix, regression test.

## Q2. Is the line shown in a traceback always the root cause?

“No. It identifies where the exception was raised, but the invalid value or state may have been introduced earlier by a caller, fixture, API response or another component. I trace the call stack and inspect inputs to locate the origin.”

## Q3. Difference between `TypeError` and `ValueError`?

“TypeError generally means an operation received an inappropriate type. ValueError means the type may be acceptable, but the supplied value is invalid for that operation.”

## Q4. What is a breakpoint?

“A breakpoint pauses program execution at a selected line so I can inspect variables, call stack and runtime state.”

## Q5. Difference between Step Over and Step Into?

“Step Over executes the current line without entering a called function. Step Into enters the function so I can inspect its internal execution.”

## Q6. Why is regression testing required after a fix?

“To confirm the original defect is resolved and existing behaviour has not been broken by the change.”

---

# 14. Session 01 completion checklist

Mark only after demonstrating the skill:

- [ ] I can explain symptom vs exception vs root cause.
- [ ] I can read the final exception line.
- [ ] I can locate the failing application frame.
- [ ] I can follow caller frames.
- [ ] I can inspect `repr()` and `type()`.
- [ ] I can use VS Code breakpoints.
- [ ] I can use Step Over / Into / Out.
- [ ] I can inspect Variables and Call Stack.
- [ ] I can use a conditional breakpoint.
- [ ] I can use `pdb` basics.
- [ ] I can explain why catching every exception is dangerous.
- [ ] I can fix a bug without weakening expected behaviour.
- [ ] I can write a regression test.

**Session 01 is not complete merely by reading this file. Complete Exercises A, B and C and share your diagnosis for review.**

---

# 15. Next lesson

**Session 02 — VS Code Debugger Deep Practice**

We will take a multi-function Python program with:
- Wrong input introduced in one function.
- Incorrect transformation in another.
- Conditional branch bug.
- Unexpected return value.
- Shared mutable object.

You will debug it using:
- Breakpoints.
- Conditional breakpoints.
- Step Over / Into / Out.
- Variables.
- Watch expressions.
- Call Stack.
- Debug Console.

AI-assisted debugging will remain locked until the manual debugging foundation is demonstrated.
