<!--
PYTHON MASTERY NOTES — SOURCE-PRESERVING EDITION

The original DOCX content is preserved. Formatting below is an added Markdown
presentation layer: headings, code fences, tables, navigation, callouts, and
optional visual/animation helpers. No source paragraph or table content is
intentionally omitted.
-->

# 🐍 Python Mastery Notes

> **Complete Source-Preserving Markdown Edition**  
> Phase 1 → Phase 4 · 20 Topics

<div align="center">

**📚 Learn → 🧠 Understand → 💻 Practice → 🎤 Interview**

</div>

---

## 🧭 Quick Navigation


- [Phase 1 · Topic 1: Python Memory Model](#phase-1--topic-1-python-memory-model)
- [Phase 1 · Topic 2: Namespaces and Scope (LEGB Rule)](#phase-1--topic-2-namespaces-and-scope-legb-rule)
- [Phase 1 · Topic 3: Functions in Depth](#phase-1--topic-3-functions-in-depth)
- [Phase 1 · Topic 4: Comprehensions (List, Dict, Set, Generator)](#phase-1--topic-4-comprehensions-list-dict-set-generator)
- [Phase 2 · Topic 5: Class Anatomy](#phase-2--topic-5-class-anatomy)
- [Phase 2 · Topic 6: self in Depth](#phase-2--topic-6-self-in-depth)
- [Phase 2 · Topic 7: __init__ vs __new__](#phase-2--topic-7-init-vs-new)
- [Phase 2 · Topic 8: All Dunder Methods (Gaps Filled)](#phase-2--topic-8-all-dunder-methods-gaps-filled)
- [1. Problem Definition (Problem kya thi?)](#1-problem-definition-problem-kya-thi)
- [Phase 2 · Topic 10: Inheritance, MRO, super() Internals](#phase-2--topic-10-inheritance-mro-super-internals)
- [Phase 2 · Topic 11: Class Methods vs Static Methods vs Instance Methods](#phase-2--topic-11-class-methods-vs-static-methods-vs-instance-methods)
- [Phase 2 · Topic 12: Abstract Classes (abc module)](#phase-2--topic-12-abstract-classes-abc-module)
- [Phase 2 · Topic 13: Dataclasses (Phase 2 Final Topic)](#phase-2--topic-13-dataclasses-phase-2-final-topic)
- [Phase 3 · Topic 15: Generators and Iterators (Deeper Dive)](#phase-3--topic-15-generators-and-iterators-deeper-dive)
- [Phase 3 · Topic 16: Context Managers (Deeper Dive)](#phase-3--topic-16-context-managers-deeper-dive)
- [Phase 3 · Topic 17: Exception Handling](#phase-3--topic-17-exception-handling)
- [Phase 3 · Topic 18: Type Hints](#phase-3--topic-18-type-hints)
- [Phase 3 · Topic 19: Modules and Packages (Phase 3 Final Topic)](#phase-3--topic-19-modules-and-packages-phase-3-final-topic)
- [Phase 4 · Topic 20: Logging (Not print)](#phase-4--topic-20-logging-not-print)

---

> 💡 **How to use these notes**
>
> - Use the navigation above to jump between topics.
> - `<details>` sections, Mermaid diagrams, and CSS animation examples are
>   supported by many Markdown viewers, but exact rendering depends on the
>   viewer (GitHub, VS Code, Obsidian, MkDocs, etc.).
> - The source notes themselves are kept intact; visual elements are an
>   additional presentation layer.



---

# 📘 Topic 01


## 🐍 Python Mastery Notes

### Phase 1 · Topic 1: Python Memory Model

## 1. Core Mental Model — Variables Are Not Boxes

Beginner (galat) mental model: x ek 'box' hai jisme value rakhi hoti hai. Ye C/Java wali soch hai.

Python ka asli mental model:

Object — memory (heap) mein banta hai, e.g. 10, [1,2,3], "hello"

Naam (variable) — sirf ek label/sticky-note hai jo object ko point karta hai

```python
x = 10
 
Memory:  [ 10 ]   <- object banaya gaya
              ^
              x    <- naam ne object ko point kiya
```

Jab likhte ho y = x, naya object NAHI banta. Ek naya naam ("y") usi purane object pe chipak jaata hai:

```python
y = x
 
Memory:  [ 10 ]
          ^    ^
          x    y
```

💡 Dono naam same object ko point kar rahe hain — koi copy nahi hui.

## 2. Mutation vs Reassignment (core distinction)

Ye sabse important distinction hai poore Python OOP aur function-passing ke liye.

### append() — Mutation

Existing object ke andar change karta hai. Object ka id() SAME rehta hai.

```python
a = [1, 2, 3]
print(id(a))     # 140234567890
a.append(4)
print(id(a))     # 140234567890  -- SAME address
```

### + (concatenation) — Reassignment

Naya object banata hai. Purana object untouched rehta hai.

```python
a = [1, 2, 3]
b = a
b = b + [4]      # naya object [1,2,3,4] banta hai
print(a)          # [1, 2, 3]      -- untouched
print(b)          # [1, 2, 3, 4]   -- naya object
```

```python
append() case:
a -> [1,2,3] -> mutate -> a -> [1,2,3,4]   (SAME object)
 
+ case:
a -> [1,2,3]      (untouched)
b -> [1,2,3,4]    (NAYA object)
```

## 3. Mutable vs Immutable Types

| Mutable (andar se change ho sakta hai) | Immutable (kabhi andar se change nahi hota) |
| --- | --- |
| list, dict, set, custom objects (default) | int, float, str, tuple, bool, frozenset |

String bhi immutable hai — isliye s = s + " world" naya object banata hai, purana "hello" untouched rehta hai.

## 4. Function Argument Passing — 'Pass by Object Reference'

Ye Python ka official behavior hai: reassignment andar se caller ko kabhi affect nahi karta, but mutation affect karta hai.

### Case A: Immutable (int) — Reassignment, no effect on caller

```python
x = 5
def change(n):
    n = n + 1     # naya object banta hai, sirf local naam 'n' reassign hota hai
    return n
 
change(x)       # return value kahin store nahi hua!
print(x)        # 5  -- x completely unaffected
```

💡 Common mistake: change(x) call karke return value ignore karna. print(x) seedha x print karta hai, function ka result nahi.

### Case B: Mutable (list) — Mutation, DOES affect caller

```python
lst = [1, 2, 3]
def change(n):
    n.append(4)    # SAME object mutate hua
 
change(lst)
print(lst)       # [1, 2, 3, 4]  -- lst affected, kyunki n aur lst same object point karte the
```

✅ Reassignment (n = ...) andar se caller ko kabhi affect nahi karta. Mutation (.append(), .sort(), etc.) affect karta hai — kyunki dono naam same object share karte hain.

## 5. is vs == — Identity vs Value

| Operator | Kya compare karta hai |
| --- | --- |
| == | VALUE — kya dono cheez barabar hain |
| is | IDENTITY — kya dono same memory object hain |

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a
 
print(a == b)   # True   -- values same hain
print(a is b)   # False  -- alag objects, chahe values same dikhein
print(a is c)   # True   -- c = a, same object
```

```python
a -> [1,2,3]  (object #1)
b -> [1,2,3]  (object #2)   <- alag object, same value
c ---'  (c bhi object #1 ko point karta hai)
```

## 6. CPython Integer Caching (reference)

CPython -5 se 256 tak ke integers ko startup pe cache kar leta hai. Isi range ke andar is True dega, bahar False.

```python
a = 256
b = 256
print(a is b)   # True  -- cached object
 
a = 257
b = 257
print(a is b)   # False -- alag objects, cache range ke bahar
```

💡 Rule: is sirf None, True, False check karne ke liye use karo. Values compare karne ke liye hamesha == use karo.

## Effective Python — Reference

Item 1 aur Item 4 dekh lo parallel mein (Python version/str-bytes basics). Memory model / mutation-vs-reassignment ka dedicated item nahi hai — ye CPython internals hai jo book directly assume karti hai.

## Summary — Topic 1 in one line

✅ Variables naam hain, objects nahi. Reassignment naya object bana ke naam ko wahan point karata hai; mutation existing object ko andar se badalta hai. Ye distinction hi function-argument-passing, mutable/immutable, aur is-vs-== sab ka base hai.


---

# 📘 Topic 02


## 🐍 Python Mastery Notes

### Phase 1 · Topic 2: Namespaces and Scope (LEGB Rule)

## 1. LEGB Rule — WHAT

Jab Python kisi naam (variable) ko dhundta hai, ek fixed order mein 4 jagah check karta hai:

L — Local (current function ke andar)

E — Enclosing (outer function, agar nested function hai)

G — Global (module/file level)

B — Built-in (Python ke apne functions: len, print, range)

```python
Search order:  L -> E -> G -> B
(jahan pehle mil jaye, wahi use hota hai)
```

### Basic Example

```python
x = "global"
 
def outer():
    x = "enclosing"
    def inner():
        print(x)   # local nahi hai, enclosing mein milta hai
    inner()
 
outer()   # Output: enclosing
```

## 2. CORE RULE — Assignment vs Read (sabse important part)

✅ READ karna hai -> LEGB chalta hai (search karta hai upar tak).  ASSIGN karna hai -> LEGB nahi chalta, seedha us function ka LOCAL ban jaata hai (jab tak global/nonlocal na likha ho).

Python jab function ko compile karta hai (execute se pehle), pura function body scan karta hai. Agar kahin bhi us naam ko '=' ke left side pe dekhta hai, to us naam ko PURE FUNCTION ke liye local ghoshit kar deta hai — chahe assignment neeche kisi line pe ho, aur chahe outer/global scope mein same naam pehle se exist karta ho.

### Trap Example — UnboundLocalError

```python
counter = 0
 
def increment():
    counter = counter + 1   # ERROR yahan
    print(counter)
 
increment()
 
# UnboundLocalError: cannot access local variable 'counter'
# where it is not associated with a value
```

WHY: 'counter = ...' dikhte hi Python 'counter' ko poore function ke liye LOCAL bana deta hai (compile time pe). Jab 'counter + 1' evaluate hota hai, local 'counter' ki koi value abhi assign nahi hui (assignment isi line mein ho rahi thi) -> error.

```python
Function scan (compile time):
  "counter = ..." dikha  ->  counter ab LOCAL hai poore function mein
 
Execution:
  counter + 1   ->  local counter ki value chahiye
                ->  abhi tak assigned nahi hua
                ->  UnboundLocalError!
 
Global counter (0) ko check hone ka mauka hi nahi mila,
kyunki local hone ka decision pehle hi lock ho gaya tha.
```

## 3. Fix — global keyword

```python
counter = 0
 
def increment():
    global counter          # bata do: module-level wala counter use karo
    counter = counter + 1
    print(counter)
 
increment()   # 1
increment()   # 2  -- global state persist hota hai calls ke beech
```

## 4. Fix — nonlocal keyword (nested functions ke liye)

```python
def outer():
    count = 0
    def inner():
        nonlocal count      # "outer" ka count target karo
        count = count + 1
        return count
    return inner()
 
outer()   # 1
```

### global vs nonlocal — exact farak

| Keyword | Kis scope ko target karta hai |
| --- | --- |
| global | Seedha module-level (global) scope — chahe function kitna bhi nested ho, hamesha sabse bahar wale global tak jaata hai |
| nonlocal | Sirf immediate enclosing (outer) function ka scope — GLOBAL tak kabhi nahi jaata |

```python
count = 0   # global
 
def outer():
    count = 5   # enclosing (outer ka apna local)
    def inner():
        nonlocal count   # 'outer' ka count target karega, GLOBAL wala NAHI
        count = count + 1
        return count
    return inner()
 
print(outer())   # 6  (5+1, outer ka count update hua)
print(count)     # 0  (global count bilkul untouched!)
```

💡 nonlocal sirf tab kaam karta hai jab ek function ke andar nested function ho, aur beech wale (enclosing) function ka variable modify karna ho. Global variable ke liye kaam nahi karta.

## 5. Effective Python — Item 21 (Full Coverage)

📘 EFFECTIVE PYTHON — Item 21: Know How Closures Interact with Variable Scope

Book ek REAL-WORLD case deti hai jahan same scoping bug 'silently galat result' deta hai — error nahi aata, jo actually zyada dangerous hai.

### Scenario: Priority Sort (closures + first-class functions)

Numbers sort karne hain, lekin ek priority group ke numbers pehle aane chahiye. Iske liye 'key=' parameter mein ek closure (nested helper function) diya jaata hai.

```python
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)
 
numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)
# [2, 3, 5, 7, 1, 4, 6, 8]
```

Ye 3 Python features milke possible banate hain (book ke exact points):

Closures — helper() bina parameter ke 'group' ko access kar pata hai, kyunki wo enclosing scope se aaya hai

Functions first-class objects hain — isliye function ko key=helper jaisa VALUE ki tarah pass kiya ja sakta hai (bina call kiye, bina brackets ke)

Tuple comparison — Python tuples ko element-by-element compare karta hai. (0,x) vs (1,x) mein pehla element hi decide kar deta hai order, isliye priority group hamesha pehle aata hai

### Dry Run — key= function har element pe kaise chalta hai

| number (x) | x in group? | helper(x) return |
| --- | --- | --- |
| 8 | No | (1, 8) |
| 3 | Yes | (0, 3) |
| 1 | No | (1, 1) |
| 2 | Yes | (0, 2) |
| 5 | Yes | (0, 5) |
| 4 | No | (1, 4) |
| 7 | Yes | (0, 7) |
| 6 | No | (1, 6) |

sort() in tuples ko compare karta hai, asli numbers ko nahi. Saare (0,x) tuples (group members) pehle aate hain, unke andar bhi number ke hisaab se sorted. Phir saare (1,x), unke andar bhi sorted.

### The Bug — found flag add karne ki koshish

```python
def sort_priority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True   # Seems simple -- but BUG!
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found
 
found = sort_priority2(numbers, group)
print('Found:', found)   # False !! (galat, priority items mile the)
print(numbers)            # [2, 3, 5, 7, 1, 4, 6, 8]  (sorting sahi hai)
```

⚠️ Sorting sahi hui, lekin 'found' False print hua jabki priority items clearly mile. Root cause: 'found = True' helper() ke andar assignment hai, isliye Python 'found' ko helper ka NAYA LOCAL variable bana deta hai. sort_priority2 ka asli 'found' kabhi touch nahi hota — sirf naam match karta hai, cheez alag hai.

```python
sort_priority2 ka found = False     <- ye box kabhi touch nahi hota
 
helper() chalta hai har number pe:
  jab x in group (3,2,5,7 ke liye):
     found = True    <- ye helper ka APNA ALAG local "found" hai
                         set hota hai, use hota hai, helper khatam
                         hote hi GAYAB ho jaata hai
 
helper() poora complete hone ke baad:
  return found   <- ye sort_priority2 ka ASLI found hai, hamesha False raha
```

### The Fix — nonlocal

```python
def sort_priority3(numbers, group):
    found = False
    def helper(x):
        nonlocal found       # Added
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found
 
found = sort_priority3(numbers, group)
print('Found:', found)   # True  -- ab sahi!
```

Book ka exact point: is scoping bug ka intended purpose hai — ye local variables ko containing module mein 'pollute' hone se rokta hai. Agar aisa na hota, to function ke andar har assignment global scope mein 'garbage' daal deta, aur obscure bugs create karta.

### Book ki Important Warning

⚠️ nonlocal ko sirf CHHOTI, SIMPLE functions mein use karo. Bade/complex functions mein nonlocal ke side-effects track karna mushkil ho jaata hai (assignment aur usage door door ho sakte hain code mein). Agar state management complex ho raha hai, ek CLASS banao (__call__ method ke saath) instead of nonlocal — zyada readable hota hai.

## 6. Kab Dhyan Dena Hai — Practical Debugging Guide

### Red flag pattern (bug hone se PEHLE pehchano)

💡 Jab bhi nested function ho, aur uske andar outer function ka koi variable ASSIGN/MODIFY karne ki koshish ho ('=' use ho) — ruk ke socho: 'Main isko sirf READ kar raha hun, ya ASSIGN kar raha hun?' Sirf read -> koi problem nahi. Assign/modify -> nonlocal (outer function ka var) ya global (module-level var) explicitly likhna ZAROORI hai.

### Jab bug ho jaye (debug process)

Step 1: Dekho error UnboundLocalError hai, ya silently galat value aa rahi hai

Step 2: UnboundLocalError -> seedha pata chal jaata hai, jaha '=' use hua hai wahi culprit line hai

Step 3: Silent wrong value (jaisa 'found' case) -> ZYADA DANGEROUS, error nahi aata. Jis variable ki value expected se different aa rahi ho, check karo: kya wo kisi nested function ke andar assign ho raha hai?

Step 4: Fix -> nonlocal/global add karo. Agar function complex ho raha hai, class bana do taki state ek jagah (self.found) clearly rahe

## Summary — Topic 2 in one line

✅ READ operation LEGB follow karta hai (upar tak search karta hai). ASSIGNMENT LEGB follow nahi karta — turant local ban jaata hai jahan likha gaya hai, jab tak global/nonlocal explicitly na bola jaye. Yahi rule UnboundLocalError aur silent closure bugs, dono ka root cause hai.


---

# 📘 Topic 03


## 🐍 Python Mastery Notes

### Phase 1 · Topic 3: Functions in Depth

## 1. Functions Are First-Class Objects

Functions Python mein normal OBJECTS hain — int, list, str jaisa. Inko variable mein assign kar sakte ho, dusre function ko argument bana sakte ho, dict/list mein daal sakte ho — bina call kiye, sirf VALUE ki tarah.

```python
def greet(name):
    return f"Hello {name}"
 
my_func = greet          # function ko VALUE ki tarah assign kiya, CALL nahi kiya
print(my_func("RK"))     # Hello RK
```

### Practical Pattern — Dictionary of Functions

```python
def add(a, b):
    return a + b
 
def subtract(a, b):
    return a - b
 
operations = {"+": add, "-": subtract}
 
result = operations["+"](5, 3)   # dict se function FETCH kiya, phir CALL kiya
print(result)   # 8
```

💡 operations['+'] function object return karta hai (call nahi karta). Turant baad (5, 3) lagane se wo function CALL ho jaata hai. Ye pattern production mein command dispatchers, strategy pattern, API route handlers mein use hota hai.

## 2. *args aur **kwargs

| Syntax | Kya karta hai | Type |
| --- | --- | --- |
| *args | Jitne bhi POSITIONAL arguments aayein, ek saath pack kar deta hai | tuple |
| **kwargs | Jitne bhi KEYWORD arguments aayein, ek saath pack kar deta hai | dict |

```python
def mystery(*args, **kwargs):
    print(args)
    print(kwargs)
 
mystery(1, 2, name="RK", age=25)
 
# Output:
# (1, 2)                        <- tuple
# {'name': 'RK', 'age': 25}      <- dict
```

💡 args hamesha TUPLE hota hai (as-is print hota hai parentheses ke saath), kwargs hamesha DICT. Interview mein 'args ka type kya hai' common question hai.

## 3. Default Argument Trap (famous Python gotcha)

⚠️ CORE FACT: Default argument value sirf EK BAAR create hoti hai — function DEFINITION ke time pe (jab 'def' line execute hoti hai) — HAR CALL pe nahi.

```python
def add_item(item, cart=[]):   # [] YAHIN, EK HI BAAR banta hai
                                #  jab Python function define karta hai
    cart.append(item)
    return cart
 
print(add_item("apple"))    # ['apple']
print(add_item("banana"))   # ['apple', 'banana']         <- BUG!
print(add_item("orange"))   # ['apple', 'banana', 'orange']  <- BUG!
```

WHY: Sabhi calls jo 'cart' explicitly pass NAHI karte, EK HI shared default list object use karte hain. .append() ek MUTATION hai (Topic 1 yaad karo) — isliye har call pehle wali list ko hi modify karti hai.

```python
def add_item(item, cart=[]):
                     ^
        Ye [] object EK BAAR banta hai, function definition ke time
        Sabhi calls jo cart pass NAHI karte, isi EK object ko SHARE karte hain
 
id(default cart) - Call 1: 140234...
id(default cart) - Call 2: 140234...  <- SAME id, har baar
id(default cart) - Call 3: 140234...  <- SAME id
```

### Fix — production pattern

```python
def add_item(item, cart=None):
    if cart is None:
        cart = []          # NAYA object har us call pe banta hai jaha cart pass nahi hua
    cart.append(item)
    return cart
```

✅ Mutable default arguments (list, dict, set) kabhi direct use mat karo. Hamesha 'None' default rakho, function ke andar check karke naya object banao.

## 4. return vs Implicit None

Agar function ke andar explicit 'return' statement NAHI hai, Python khud implicitly function ke end mein 'return None' add kar deta hai.

```python
def do_something():
    x = 5 + 5
    # koi return nahi
 
result = do_something()
print(result)   # None
```

## 5. Effective Python — Item 20 (Full Coverage)

📘 EFFECTIVE PYTHON — Item 20: Prefer Raising Exceptions to Returning None

### The Bug — None aur Falsy Values ka Confusion

```python
def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
 
x, y = 0, 5
result = careful_divide(x, y)
if not result:
    print('Invalid inputs')
else:
    print('Result:', result)
 
# Output: Invalid inputs   <- GALAT! 0/5 = 0.0 ek VALID answer tha
```

⚠️ x=0, y=5 -> 0/5 = 0.0, koi error nahi tha, function ne valid result return kiya. Lekin 'if not result' ne ise galat treat kiya, kyunki 0.0 bhi FALSY hai.

### Falsy Values — Python Core Concept

Python 'if' condition kisi bhi value ko boolean context mein convert kar leta hai. Ye sab values FALSY hain (if mein False jaisa behave karti hain):

```python
False
None
0        # integer zero
0.0      # float zero
""       # empty string
[]       # empty list
{}       # empty dict
()       # empty tuple
set()    # empty set
 
# Baaki SAB truthy hai (0.0001, "a", [0], etc.)
```

Root problem: function ka 'None' (error signal) aur function ka legitimate '0.0' (valid answer) — dono 'if not result' check mein INDISTINGUISHABLE ho gaye.

### Fix 1 — Explicit 'is None' check

```python
result = careful_divide(x, y)
if result is None:      # sirf identity check, 0.0 ko False nahi maanega
    print('Invalid inputs')
else:
    print('Result:', result)
 
# Output: Result: 0.0   <- Ab sahi!
```

💡 'is None' identity check karta hai (Topic 1 yaad hai), value check nahi. Isliye 0.0 falsy hone ke bawajood None se confuse nahi hota.

### Fix 2 — BETTER: None return hi mat karo, Exception raise karo

```python
def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('Invalid inputs')
 
x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)
 
# Output: Result is 2.5
```

✅ Function jab kisi SPECIAL SITUATION (error, missing case) ko batana chahe, None return mat karo — kyunki None aur genuine falsy values (0, "", []) ko caller confuse kar sakta hai. Exception raise karo, caller ko explicitly try/except se handle karne do.

Book ka additional point: type annotations (-> float) use karke bhi ye clear kiya ja sakta hai ki function kabhi None nahi degа — lekin Python typing exceptions ko interface mein directly represent nahi karti, isliye docstring mein exception-raising behavior document karna zaroori hai.

## Summary — Topic 3 in one line

✅ Functions objects hain (assign/pass kiye ja sakte hain). *args=tuple, **kwargs=dict. Mutable default arguments EK BAAR bante hain (definition time) — None + check use karo. Function 'special case' batane ke liye None mat return karo, Exception raise karo — warna falsy values (0, "", []) se confusion ho sakta hai.


---

# 📘 Topic 04


## 🐍 Python Mastery Notes

### Phase 1 · Topic 4: Comprehensions (List, Dict, Set, Generator)

## 1. List Comprehension — WHAT

Normal for-loop pattern:

```python
squares = []
for n in range(10):
    squares.append(n ** 2)
```

Isi ko ek line mein — List Comprehension:

```python
squares = [n ** 2 for n in range(10)]
```

Padhne ka tarika: RESULT pehle, LOOP baad mein -> "n**2, har n ke liye, jo range(10) mein hai"

## 2. WHY — sirf shortcut nahi hai

Performance — comprehensions normal for-loop se thodi FAST hoti hain (optimized bytecode, .append() baar-baar call nahi hota)

Intent clarity — turant pata chalta hai 'naya list/dict/set ban raha hai transform/filter karke', poora block padhna nahi padta

### Filter ke saath (if condition)

```python
even_squares = [n ** 2 for n in range(10) if n % 2 == 0]
```

```python
names = ["rahul", "amit", "sneha", "raj"]
result = [name.upper() for name in names if len(name) > 3]
print(result)
# ['RAHUL', 'AMIT', 'SNEHA']   -- "raj" filter hua (length 3)
```

💡 Comprehension mein 2 kaam ho rahe hain: TRANSFORM (name.upper()) aur FILTER (if len(name) > 3). Dono alag purpose hain — filter decide karta hai kaun aage jaayega, transform decide karta hai kaise convert hoga.

## 3. Set aur Dict Comprehensions

```python
# List  -> []
squares_list = [n**2 for n in range(5)]        # [0, 1, 4, 9, 16]
 
# Set   -> {}  (bina colon ke)
squares_set = {n**2 for n in range(5)}          # {0, 1, 4, 9, 16} -- duplicates auto-remove
 
# Dict  -> {key: value}
squares_dict = {n: n**2 for n in range(5)}      # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Important Gotchas

```python
words = ["apple", "banana", "apple", "cherry", "banana"]
 
result1 = {word for word in words}
result2 = {word: len(word) for word in words}
 
print(result1)
# {'cherry', 'banana', 'apple'}   -- duplicates removed, ORDER GUARANTEED NAHI
print(result2)
# {'apple': 5, 'banana': 6, 'cherry': 6}  -- duplicate key OVERWRITE hoti hai, error nahi
```

⚠️ Sets UNORDERED hote hain — insertion order preserve nahi hoti (list ke opposite). Kabhi assume mat karo set ka output kisi specific order mein aayega.

## 4. Generator Expression — Lazy Evaluation (core WHY)

```python
# List comprehension — pura list EK SAATH memory mein banta hai
squares_list = [n**2 for n in range(1000000)]
 
# Generator expression — sirf () use hota hai, [] nahi
squares_gen = (n**2 for n in range(1000000))
```

```python
import sys
print(sys.getsizeof(squares_list))   # 8,448,728 bytes  (~8.4 MB)
print(sys.getsizeof(squares_gen))    # 200 bytes
```

⚠️ List: turant saari 1 million values calculate karta hai, memory mein EK SAATH store. Generator: koi value calculate NAHI karta jab tak maango — sirf ek 'recipe' (instructions) store karta hai.

```python
List:      [0, 1, 4, 9, 16, 25, ...., 999998000001]
           <- SAARI values EK SAATH memory mein, ready
 
Generator: (recipe: "n**2 do, phir next n ke liye ruk jao")
           <- KOI value abhi nahi bani, sirf plan hai
```

### Generator se values nikalna — next()

```python
squares_gen = (n**2 for n in range(5))
 
print(next(squares_gen))   # 0
print(next(squares_gen))   # 1
print(next(squares_gen))   # 4
 
# for loop WAHI SE continue karega jaha generator ruka tha:
for val in squares_gen:
    print(val)
# 9
# 16   (SHURU se nahi, jaha chhoda wahi se)
```

⚠️ Generator EK BAAR consume ho jaye to KHATAM ho jaata hai — dobara use nahi kar sakte (list ke opposite, jise jitni baar chahe loop kar sakte ho).

## 5. Kab Kya Use Karna Hai — Decision Table

| Situation | Use Karo |
| --- | --- |
| Result multiple baar use karna hai, ya index se access (result[5]) | List comprehension |
| Sirf EK BAAR iterate karna hai, data bahut bada hai | Generator expression |
| Duplicates nahi chahiye, order matter nahi karta | Set comprehension |
| Key-value mapping banana hai | Dict comprehension |

```python
# GALAT -- pura file memory mein load ho jaayega
lines = [line.strip() for line in open('huge_log.txt')]
 
# SAHI -- ek time pe ek line hi memory mein aati hai
lines = (line.strip() for line in open('huge_log.txt'))
for line in lines:
    process(line)
```

### Combined Example — sum() + generator (interleaved execution)

```python
data = [1, -2, 3, -4, 5, -6]
result = sum(n for n in data if n > 0)
print(result)   # 9
```

sum() poori list PEHLE nahi banata. Har element ke liye filter-check aur add EK SAATH, INTERLEAVED hota hai:

```python
n=1  -> n>0? Yes -> yield 1  -> sum: 1
n=-2 -> n>0? No  -> skip
n=3  -> n>0? Yes -> yield 3  -> sum: 1+3=4
n=-4 -> n>0? No  -> skip
n=5  -> n>0? Yes -> yield 5  -> sum: 4+5=9
n=-6 -> n>0? No  -> skip
Final: 9
```

💡 Memory mein kisi bhi time pe sirf EK number hota hai — chahe data mein 6 numbers hon ya 60 lakh, memory usage SAME rahega.

## 6. Effective Python — Item 30 (Full Coverage)

📘 EFFECTIVE PYTHON — Item 30: Consider Generators Instead of Returning Lists

Ye Item comprehension ka FUNCTION-LEVEL version hai — jab function results collect karta hai, yield use karna append()-based list return karne se BEHTAR hai.

### Purana style — list + append

```python
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result
 
address = 'Four score and seven years ago...'
print(index_words(address)[:5])
# [0, 5, 11, 15, 21]
```

### Naya style — yield / generator function

```python
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1
 
it = index_words_iter(address)
print(next(it))   # 0
print(next(it))   # 5
 
# Poori list chahiye to convert kar sakte ho:
result = list(index_words_iter(address))
```

### WHY yield behtar hai (book ke exact 2 points)

Cleaner code — result.append(...) baar-baar likhna noise create karta hai. yield sidha value emit karta hai, koi list-management overhead nahi

Memory — REAL production case: file processing (10 lakh line ki log file). List-based version poori file ka result memory mein rakhega -- crash ho sakta hai. Generator version sirf EK LINE jitni memory use karta hai, file kitni bhi badi ho

```python
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset
# Working memory limited to MAX LENGTH OF ONE LINE, chahe file kitni bhi badi ho
```

⚠️ Book ki warning: Generator se return hui values STATEFUL hoti hain — ek baar consume karne ke baad dobara use NAHI kar sakte (generator wahi se continue hota hai jaha ruka, restart nahi hota).

## Summary — Topic 4 in one line

✅ Comprehensions [list]/{set}/{dict} turant PURA result memory mein banate hain — clarity aur speed ke liye best jab result multiple baar use karna ho. Generator expressions () aur generator functions (yield) LAZY hote hain — ek time pe ek value, memory-efficient jab data bada ho ya sirf ek baar iterate karna ho. Generators EK BAAR consume hone ke baad khatam ho jaate hain.


---

# 📘 Topic 05


## 🐍 Python Mastery Notes

### Phase 2 · Topic 5: Class Anatomy

## 1. Teen Tarah Ke Variables — WHAT

```python
class Employee:
    company = "TechCorp"        # CLASS variable
 
    def __init__(self, name, salary):
        self.name = name         # INSTANCE variable
        self.salary = salary     # INSTANCE variable
 
    def show_bonus(self):
        bonus = self.salary * 0.1   # LOCAL variable
        return bonus
```

| Type | Kaha Define Hota Hai | Scope |
| --- | --- | --- |
| Class variable | Class ke andar, method ke BAHAR | SABHI instances ke beech SHARED (single object) |
| Instance variable | self. ke saath, method ke andar | HAR object ka apna ALAG copy |
| Local variable | Method ke andar, bina self. ke | Method khatam hote hi GAYAB (Topic 2 scope) |

## 2. Memory Level Pe Kya Ho Raha Hai

Class variable EK HI JAGAH memory mein banta hai — class object ke andar. Attribute access karte time Python object ke andar dhundta hai, nahi milta to CLASS ke andar dhundta hai (attribute lookup chain).

```python
Employee class object:
   company = "TechCorp"    <- YAHIN, ek hi jagah
 
emp1 object:               emp2 object:
   name = "Rahul"             name = "Priya"
   salary = 50000             salary = 60000
   (company yahan NAHI hai, class se milta hai)
```

## 3. Class Variable Modify Karna — Sabko Affect Karta Hai

```python
class Employee:
    company = "TechCorp"
    def __init__(self, name):
        self.name = name
 
e1 = Employee("Rahul")
e2 = Employee("Priya")
 
print(e1.company)   # TechCorp
print(e2.company)   # TechCorp
 
Employee.company = "NewCorp"   # CLASS variable modify hua
 
print(e1.company)   # NewCorp  -- dono affected
print(e2.company)   # NewCorp
```

💡 Jab instance ke paas apna khud ka attribute nahi hota, Python class ke paas jaake dhundta hai. Employee.company badalne se, sabhi instances jo apna khud ka company nahi rakhte, turant naya value dekhte hain — same shared object ko point karte hain.

## 4. TRAP — Shadowing (instance attribute class ko chhupa deta hai)

```python
e1.company = "StartupXYZ"     # DHYAN DO - ye Employee.company NAHI hai!
 
print(e1.company)        # StartupXYZ
print(e2.company)        # TechCorp   -- unaffected
print(Employee.company)  # TechCorp   -- unaffected
```

⚠️ e1.company = ... class variable ko MODIFY nahi karta — ye ek NAYA instance variable create kar deta hai, sirf e1 ke upar. Class aur baaki instances UNTOUCHED rehte hain.

### Attribute Lookup Rule

Jab e1.company access hota hai, Python order follow karta hai:

1. Pehle instance ke apne __dict__ mein dhundta hai — kya e1 ke paas apna khud ka company hai?

2. Agar nahi milta, class ke __dict__ mein dhundta hai

```python
PEHLE (e1.company = ... se pehle):
Employee class:  company = "TechCorp"
e1 object:        (company yahan NAHI hai) -> class se milta -> "TechCorp"
e2 object:        (company yahan NAHI hai) -> class se milta -> "TechCorp"
 
BAAD (e1.company = "StartupXYZ" ke baad):
Employee class:  company = "TechCorp"        <- UNTOUCHED
e1 object:        company = "StartupXYZ"     <- NAYA instance attribute, e1 pe
e2 object:        (company yahan NAHI hai)   -> class se milta -> "TechCorp" (unaffected)
```

Yehi Topic 1 ka assignment-vs-mutation pattern hai, class attributes ke context mein: assignment (e1.company = ...) naya object bana ke instance pe attach karta hai, class ko kabhi touch nahi karta (jab tak explicitly ClassName.attr likha na jaye).

## 5. DANGEROUS TRAP — Mutable Class Variable

```python
class Employee:
    skills = []      # class variable, ek MUTABLE list hai
 
    def __init__(self, name):
        self.name = name
 
    def add_skill(self, skill):
        self.skills.append(skill)   # koi assignment nahi, sirf MUTATION
 
e1 = Employee("Rahul")
e2 = Employee("Priya")
 
e1.add_skill("Python")
e2.add_skill("Django")
 
print(e1.skills)   # ['Python', 'Django']  <- BUG! dono mila ke
print(e2.skills)   # ['Python', 'Django']  <- SAME list, dono mein
```

⚠️ self.skills.append(...) mein koi '=' nahi hai, sirf mutation hai. self.skills access hote waqt instance mein nahi milta, class mein milta hai (SAME shared list object). .append() us SHARED object ko directly modify kar deta hai — sabhi instances affected.

```python
Employee class:  skills = []  --> ye EK object hai, SHARED
 
e1.add_skill("Python"):
   self.skills -> instance mein nahi mila -> class ka skills mila (same object)
   .append("Python") -> class ka skills MUTATE hua -> ['Python']
 
e2.add_skill("Django"):
   self.skills -> instance mein nahi mila -> class ka skills mila (SAME object)
   .append("Django") -> SAME object mutate hua -> ['Python', 'Django']
 
Ab e1.skills aur e2.skills DONO isi EK object ko point karte hain
```

Ye EXACTLY wahi bug hai jo Topic 3 mein tha (mutable default argument trap) — sirf yahan trigger function default argument nahi, CLASS VARIABLE hai. Root cause same: mutable object sabke beech shared ho gaya, mutation sabko affect karta hai.

### Fix — Production Pattern

```python
class Employee:
    def __init__(self, name):
        self.name = name
        self.skills = []      # INSTANCE variable, har object ka apna alag
 
    def add_skill(self, skill):
        self.skills.append(skill)
 
e1 = Employee("Rahul")
e2 = Employee("Priya")
 
e1.add_skill("Python")
e2.add_skill("Django")
 
print(e1.skills)   # ['Python']
print(e2.skills)   # ['Django']
```

✅ Mutable defaults (list, dict, set) ko KABHI class variable ki tarah define mat karo. __init__ ke andar self. se banao, taki har instance ka apna alag object ho.

## 6. Class Variable Directly Modify Karna — __init__ ke andar bhi

```python
class Counter:
    total_count = 0
 
    def __init__(self):
        Counter.total_count += 1   # DHYAN DO - self.total_count NAHI hai
 
    def show(self):
        message = f"Total counters: {Counter.total_count}"  # LOCAL variable
        return message
 
c1 = Counter()
c2 = Counter()
c3 = Counter()
 
print(c1.show())         # Total counters: 3
print(Counter.total_count)  # 3
```

✅ Rule: jahan bhi 'ClassName.var' (class naam se) likha ho — chahe kahin se bhi likha ho (__init__ ke andar bhi) — wo CLASS variable ko target karta hai. Jahan 'self.var' likha ho — wo INSTANCE variable ko target karta hai. Ye purely 'kis naam se access kiya' pe depend karta hai, na ki 'kaha likha hai' pe.

```python
Counter class: total_count = 0
 
c1 = Counter()  -> Counter.total_count += 1 -> class ka total_count = 1
c2 = Counter()  -> Counter.total_count += 1 -> class ka total_count = 2
c3 = Counter()  -> Counter.total_count += 1 -> class ka total_count = 3
 
Teeno objects ne SAME class variable ko increment kiya
(koi instance variable bana hi nahi, kyunki self. use nahi hua)
```

message variable show() ke andar hai, bina self. ke -> LOCAL variable. Method khatam hote hi gayab ho jaata hai, lekin Counter.total_count (class variable) persist karta hai. Yehi asli 'object counter' pattern hai — production mein instances count karne ke liye use hota hai (e.g. active database connections).

## Effective Python — Reference

Is topic (class vs instance vs local variable scoping) pe book mein koi dedicated Item nahi hai — ye core Python semantics hai jo book already assume karti hai. Closest related Item hai Item 42: 'Prefer Public Attributes Over Private Ones' — lekin wo attribute-privacy (_var vs __var naming convention) ke baare mein hai, alag topic hai.

## Summary — Topic 5 in one line

✅ Class variable = 1 shared object, ClassName.var se ya self.var (agar instance override nahi hai) se access hota hai. Instance variable = self.var se banta hai, har object ka apna alag. Assignment (instance.var = x) naya instance attribute banata hai (shadowing) — class untouched. Mutation (self.var.append()) agar variable class ka hai, SABKO affect karta hai — mutable class variables isliye dangerous hain.


---

# 📘 Topic 06


## 🐍 Python Mastery Notes

### Phase 2 · Topic 6: self in Depth

## 1. self Actually Kya Hai — WHAT

Jab d.bark() likha jaata hai, Python internally isko convert kar deta hai:

```python
d.bark()              # ye jo hum likhte hain
Dog.bark(d)           # Python isko INTERNALLY isme convert karta hai
```

self koi magic keyword nahi hai — ye sirf method ka PEHLA PARAMETER hai. Python object ko automatically pehla argument bana ke pass kar deta hai jab '.' (dot) se method call kiya jaata hai.

```python
class Dog:
    def bark(self):
        return f"{self.name} says Woof!"
 
d = Dog()
d.name = "Tommy"
 
d.bark()              # ye...
Dog.bark(d)           # ...aur ye — DONO SAME kaam karte hain
```

## 2. Test 1 — d.bark() vs Dog.bark(d)

🧠 MERA JAWAB THA: Dono ka output same aayega: Tommy says Woof! Ye do ways hain class ke function ko call karne ke — d.bark() usually use karte hain, ek aur Dog.bark(d) hai jisme object explicitly pass karna padta hai. Python khud bhi ye default kar leta hai.

👍 Ye reasoning bilkul CORRECT tha. d.bark() = 'bound method call' (Python automatically object ko self mein bind karta hai). Dog.bark(d) = manually wahi kaam karna jo Python automatically karta hai.

```python
d.bark()      -> Output: Tommy says Woof!
Dog.bark(d)   -> Output: Tommy says Woof!   (SAME)
```

## 3. Test 2 — Alag Instances, Same Method Code

```python
class Dog:
    def bark(self):
        return f"{self.name} says Woof!"
 
d1 = Dog(); d1.name = "Tommy"
d2 = Dog(); d2.name = "Rocky"
 
print(d1.bark())   # ?
print(d2.bark())   # ?
```

🧠 MERA JAWAB THA: Tommy, Rocky ayega. Do instances d1 aur d2 hain, same class template hai but dono ka apna khud ka space hai, ids alag hai.

✅ ASLI SAHI REASONING: Output sahi tha (Tommy, Rocky). id/space wala concept bhi sahi connect kiya (Topic 1 se). Lekin exact MECHANISM missing tha: d1.bark() internally Dog.bark(d1) banta hai, matlab self=d1 TEMPORARILY bind hota hai sirf uss call ke liye. self.name is call ke duration ke liye d1.name ke barabar ho jaata hai.

🔧 CORRECTION / GAP: Method ka CODE class mein sirf EK BAAR exist karta hai (shared, jaise class variable). self ek fixed cheez nahi hai — har call pe DYNAMICALLY decide hota hai based on kis object se method call hua.

```python
Dog class:
   bark() ka code  <- YAHI EK JAGAH hai, SHARED
 
d1.bark() call: self -> d1  (temporary binding, sirf iss call ke liye)
d2.bark() call: self -> d2  (temporary binding, sirf iss call ke liye)
```

## 4. Test 3 — Bound Method (interview-favorite trap)

```python
d = Dog(); d.name = "Tommy"
 
method = d.bark      # DHYAN DO - bina () ke!
print(method())
```

🧠 MERA JAWAB THA: Tommy says Woof! aayega. method mein d.bark liya hai, baad mein () add kar diya hai — isse koi farak nahi aayega.

✅ ASLI SAHI REASONING: Output sahi tha, lekin reasoning INCOMPLETE thi. Actual mechanism: 'd.bark' (bina call kiye) ek NORMAL FUNCTION return nahi karta — ye ek BOUND METHOD OBJECT return karta hai. print(method) dikhata hai: <bound method Dog.bark of <Dog object at 0x...>> — matlab self=d PEHLE HI is line mein fix/lock ho gaya tha, function call se bhi pehle.

🔧 CORRECTION / GAP: 'Koi farak nahi' kehna technically output ke liye sahi hai, lekin ye HIDE kar deta hai ki d.bark ek special object (bound method) hai jisme self already permanently attached hota hai — plain function nahi hai. Ye interview mein direct pucha jaata hai.

```python
d.bark          -> BOUND METHOD banta hai (self=d already fixed)
method = d.bark -> "method" is bound-method-object ko point karta hai
method()        -> self=d already pata hai, name="Tommy" use hota hai
 
# Compare -- class se access (object ke bina):
Dog.bark        -> <function Dog.bark at 0x...>   PLAIN FUNCTION, self attached NAHI
```

### Core Rule Table

| Access Karne Ka Tarika | Kya Milta Hai |
| --- | --- |
| instance.method | BOUND METHOD — self already object se jud gaya hai |
| ClassName.method | PLAIN FUNCTION — self khud pass karna hoga |

## Effective Python — Reference

self ki internal mechanics (bound method vs plain function) pe book mein koi dedicated Item nahi hai — ye core Python semantics hai jo book directly assume karti hai (jaise Topic 1 aur Topic 5 mein bhi tha).

## Summary — Topic 6 in one line

✅ instance.method() Python internally ClassName.method(instance) mein convert karta hai. Method ka code class mein ek baar hi shared hota hai, self har call pe dynamically decide hota hai. instance.method (bina call kiye) ek BOUND METHOD object hai jisme self already permanently attach ho chuka hota hai — plain function nahi.


---

# 📘 Topic 07


## 🐍 Python Mastery Notes

### Phase 2 · Topic 7: __init__ vs __new__

## 1. Do Alag Steps — WHAT

Jab Employee('Rahul') likha jaata hai, object banane ka DO-STEP process hota hai:

__new__ — object ko BANATA hai (memory allocate karta hai, khaali object return karta hai)

__init__ — us ALREADY-BANE object ko INITIALIZE karta hai (attributes set karta hai)

```python
class Employee:
    def __new__(cls, name):
        print("Step 1: __new__ - object BAN raha hai")
        instance = super().__new__(cls)
        return instance
 
    def __init__(self, name):
        print("Step 2: __init__ - object INITIALIZE ho raha hai")
        self.name = name
 
e = Employee("Rahul")
```

## 2. Test — Order Kya Hoga

🧠 MERA JAWAB THA: First __new__ hi chalega. Isme super() bhi use hua hai jo parent class ke __new__ jo memory allocate karega AND parent class ka __init__ use karega, vo first chalega, then Employee class ka __init__ chalega.

✅ ASLI SAHI REASONING: Order sahi tha: __new__ pehle, __init__ baad mein. Output: 'Step 1: __new__...' phir 'Step 2: __init__...'

🔧 CORRECTION / GAP: BADA MISCONCEPTION: super().__new__(cls) sirf parent (object class) ka __new__ call karta hai, TAAKI memory allocate ho jaye. Ye __init__ ko BILKUL TOUCH nahi karta. __init__ jo baad mein chalta hai, wo PARENT ka nahi hai — wo EMPLOYEE class ka apna khud ka __init__ hai jo humne khud likha hai. __new__ aur __init__ dono INDEPENDENT steps hain jo Python sequentially khud call karta hai.

```python
Exact sequence jab Employee('Rahul') likha jaata hai:
 
1. Python 'Employee(...)' dekhta hai
2. Python khud __new__(cls, 'Rahul') call karta hai
   -> super().__new__(cls) se object ki MEMORY allocate hoti hai
   -> __new__ khaali/naya object RETURN karta hai
3. Python check karta hai: __new__ ne Employee type ka object return kiya?
   -> Haan, isliye Python aage badhta hai
4. Python khud is NAYE object pe __init__(self, 'Rahul') call karta hai
   -> __init__ attributes set karta hai (self.name = name)
5. Final object 'e' ready hai
```

## 3. Kab __new__ Override Karna Padta Hai (99% Cases Mein Nahi)

💡 99% cases mein __new__ kabhi override nahi karna padta — __init__ hi kaafi hota hai. __new__ sirf SPECIAL cases mein use hota hai.

Immutable types (str, int, tuple) ko subclass karna — kyunki immutable objects __init__ mein modify nahi ho sakte (Topic 1: immutable = andar se change nahi hota), value ko OBJECT BANATE WAQT hi (__new__ mein) set karna padta hai

Singleton pattern — jaha class ka SIRF EK instance kabhi bane, chahe kitni baar call karo

## 4. Singleton Pattern — Practical Example

```python
class Singleton:
    _instance = None
 
    def __new__(cls):
        if cls._instance is None:
            print('Naya object banaya!')
            cls._instance = super().__new__(cls)
        else:
            print('Purana object hi return kar raha hun')
        return cls._instance
 
s1 = Singleton()
s2 = Singleton()
 
print(s1 is s2)   # True
```

### Test — cls._instance Kya Hai, aur is None Check Kyun

🧠 MERA JAWAB THA: cls. Ye class variable hai, 'is None' ka reason nahi pata.

👍 cls._instance class variable hai — sahi (Topic 5 se connect: Counter.total_count jaisa concept, class-level pe stored, sabhi calls ke beech PERSIST karta hai).

✅ ASLI SAHI REASONING: 'is None' check ka purpose: 'Kya humne PEHLE kabhi object banaya hai?' Pehli baar Singleton() call hone pe cls._instance abhi None hai (class define hote waqt set kiya tha) -> condition True -> NAYA object banao, cls._instance mein STORE karo. Doosri baar call hone pe cls._instance ab None NAHI hai (pehli call ne store kar diya tha) -> condition False -> NAYA object mat banao, jo already stored hai WAHI return karo.

```python
Pehli call: Singleton()
   cls._instance == None?  -> YES (kabhi bana nahi)
   -> naya object banao, cls._instance mein STORE karo
 
Doosri call: Singleton()
   cls._instance == None?  -> NO (pehli call ne store kiya tha)
   -> naya object MAT banao
   -> jo cls._instance mein hai, WAHI return karo
```

💡 Agar 'is None' check na hota, to har baar Singleton() call karne pe NAYA object ban jaata — Singleton pattern ka pura purpose FAIL ho jaata.

## 5. WHY Ye Matter Karta Hai — Practical Use Cases

🔧 REAL USE CASE: Singleton — Database connection pool, application config object. Nahi chahte ki poore program mein alag-alag jagah 10 baar DatabaseConnection() call karne se 10 ALAG connections khul jayein. Singleton guarantee deta hai: jitni baar call karo, WAHI EK connection object milega.

🔧 REAL USE CASE: Immutable subclassing — jab tu str/int/tuple ko subclass karke koi custom validation ya extra behavior add karna chahta hai, value SET karne ka mauka sirf __new__ mein hota hai, kyunki __init__ chalne tak object already immutable/frozen ho chuka hota hai.

## Effective Python — Reference

__new__ ki mechanics pe book mein koi dedicated Item nahi hai. Closest related hai Item 39: 'Use @classmethod Polymorphism to Construct Objects' — lekin wo ALTERNATE CONSTRUCTORS banane ke baare mein hai (@classmethod se object create karna, jaise different data sources se), __new__ mechanism ke baare mein nahi. Alag topic hai, directly applicable nahi.

## Summary — Topic 7 in one line

✅ __new__ object BANATA hai (memory allocate), __init__ us object ko INITIALIZE karta hai (attributes set). Python khud dono ko sequentially call karta hai — __new__ pehle, phir __init__. 99% cases mein __new__ override karne ki zaroorat nahi; sirf Singleton pattern aur immutable-type subclassing jaise special cases mein use hota hai.


---

# 📘 Topic 08


## 🐍 Python Mastery Notes

### Phase 2 · Topic 8: All Dunder Methods (Gaps Filled)

💡 Base coverage (__len__, __getitem__, __setitem__, __contains__, __iter__, __call__, __enter__/__exit__, __bool__) already cover ho chuka tha Library example ke reference notes mein. Ye doc sirf GAPS fill karta hai: __str__ vs __repr__, __eq__/__hash__ connection, aur __iter__/__next__ ka real mechanism.

## 1. Default Object Representation — Problem

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
 
b = Book("Atomic Habits", "James Clear")
print(b)
# <__main__.Book object at 0x7f22909fef90>   -- USELESS for debugging
```

## 2. __str__ vs __repr__ — Exact Farak

| Method | Kiske Liye | Purpose |
| --- | --- | --- |
| __repr__ | Developer ke liye | Debugging, logs, Python shell. Ideally object RECREATE karne jitna precise |
| __str__ | End-user ke liye | Human-readable, print()/str() ke time |

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
 
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"
 
    def __str__(self):
        return f"{self.title} by {self.author}"
 
b = Book("Atomic Habits", "James Clear")
print(b)          # __str__ use hota hai
print(str(b))     # __str__ use hota hai
print(repr(b))    # __repr__ use hota hai
```

### Test — Collections Ke Andar Kaunsa Method Use Hota Hai

```python
books = [Book("Atomic Habits", "James Clear")]
print(books)
# [Book(title='Atomic Habits', author='James Clear')]   -- __repr__ output, CHAHE __str__ bhi defined ho
```

🧠 MERA JAWAB THA: Repr wala output hi show karega chahe str na likha ho.

🔧 CORRECTION / GAP: Test mein __str__ BHI defined tha, phir bhi list print karne pe __repr__ wala format aaya. Real rule zyada deep hai: jab kisi COLLECTION (list, dict, tuple, set) ko print/str karte ho, Python us collection ke ANDAR ke har element ke liye HAMESHA __repr__ use karta hai — chahe __str__ defined ho ya na ho. __str__ SIRF tab use hota hai jab object ko DIRECTLY print() karo (print(b)), list ke andar nahi.

```python
print(b)                -> __str__ use hota hai (agar defined hai)
print(books)  (list)    -> HAMESHA __repr__ use hota hai, har element ke liye
                            (chahe __str__ ho ya na ho)
```

✅ GOLDEN RULE: __repr__ HAMESHA define karo (kam se kam), __str__ optional hai. Agar __str__ nahi likha, Python __repr__ ko print(obj) ke liye bhi fallback ki tarah use karta hai.

## 3. __eq__ aur __hash__ Ka Hidden Connection

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
 
p1 = Point(1, 2)
p2 = Point(1, 2)
 
print(p1 == p2)          # True
points_set = {p1, p2}    # ???
```

🧠 MERA JAWAB THA: Bss itna pata hai eq compare ke liye use hota hai.

📖 NAYA CONCEPT (pehli baar dekha): points_set = {p1, p2} line CRASH karti hai: TypeError: unhashable type: 'Point'. Jab kisi class mein __eq__ CUSTOM define karte ho, Python AUTOMATICALLY us class ka __hash__ ko None set kar deta hai (agar khud __hash__ explicitly nahi diya).

```python
print(Point.__hash__)   # None  -- Python ne automatically disable kar diya
```

WHY: hash() aur == ka ek CONTRACT hai — 'agar do objects == se equal hain, to unka hash() bhi SAME hona chahiye.' Custom __eq__ (value-based) ke saath default __hash__ (memory-address-based) rakhne se ye contract TOOT jaata — isliye Python precaution ki tarah __hash__ ko None kar deta hai, taaki silent bug na bane, turant crash ho jaye.

```python
Normal case (koi __eq__ custom nahi):
   __eq__ = identity based (is jaisa)
   __hash__ = memory address based
   -> Contract maintained automatically
 
Custom __eq__ (values compare karta hai):
   __eq__ = value based (x, y compare)
   __hash__ = Python isko None kar deta hai (SAFETY)
   -> "Tu decide kar ki hash kaise banega, warna set/dict mein use nahi kar sakta"
```

### Fix — __hash__ Explicitly Define Karo

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
 
    def __hash__(self):
        return hash((self.x, self.y))   # tuple ka hash use karo
 
p1 = Point(1, 2)
p2 = Point(1, 2)
points_set = {p1, p2}
print(len(points_set))   # 1  -- duplicate maana gaya (equal + same hash)
```

✅ Agar __eq__ define karte ho, __hash__ bhi define karna ZAROORI hai (set/dict mein use karna hai to). Dono CONSISTENT hone chahiye: jo attributes __eq__ mein compare karte ho, wahi (ya unka combination) __hash__ mein use karo.

## 4. __iter__ / __next__ — Real Iterator Protocol

```python
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
 
c = Countdown(3)
for num in c:
    print(num)
# 3
# 2
# 1
```

📖 NAYA CONCEPT (pehli baar dekha): for loop internally 'iter(c)' EK BAAR call karta hai (shuru mein), phir 'next(iterator)' HAR iteration pe call karta hai, jab tak StopIteration exception na aaye — jo loop ko GRACEFULLY rok deta hai (error nahi dikhta).

```python
for num in c:  ye Python internally is tarah expand karta hai:
 
iterator = iter(c)        # __iter__ EK BAAR call hota hai
while True:
    try:
        num = next(iterator)   # __next__ HAR iteration pe call hota hai
        print(num)
    except StopIteration:      # loop RUK jaata hai
        break
```

```python
Step-by-step trace (Countdown(3)):
 
1. iter(c) -> c.__iter__() -> 'return self' -> c KHUD apna iterator hai
2. next(iterator) -> c.__next__() -> current=3 -> value=3, current=2 -> print(3)
3. next(iterator) -> c.__next__() -> current=2 -> value=2, current=1 -> print(2)
4. next(iterator) -> c.__next__() -> current=1 -> value=1, current=0 -> print(1)
5. next(iterator) -> c.__next__() -> current=0 -> raise StopIteration
6. Python is exception ko CATCH karta hai internally -> loop RUK jaata hai
```

💡 StopIteration ek NORMAL exception hai (jaise ZeroDivisionError, Topic 3 se), lekin for loop ne ise SPECIAL meaning di hai — 'error mat treat karo, loop ko gracefully rok do.' Ye Python ka built-in convention hai.

### __getitem__ vs __iter__/__next__ — Kab Kya Use Karo

|  | __getitem__-based | __iter__/__next__-based |
| --- | --- | --- |
| Indexing (obj[0]) | Automatically milta hai | Nahi milta (alag se define karna padta) |
| Stop condition | IndexError pe rukta hai | StopIteration pe rukta hai, tu control karta hai |
| State management | Simple, index-based | Explicit (self.current jaisa state rakhna padta) |
| Kab use karo | Data sequence-like ho (index se access ho sake) | Data generate/compute ho raha ho on-the-fly |

## 5. Effective Python — Item 43 (Full Coverage)

📘 EFFECTIVE PYTHON — Item 43: Inherit from collections.abc for Custom Container Types

Real problem: __getitem__ implement karna KAAFI NAHI hai poori 'sequence' jaisi behavior ke liye.

```python
class IndexableNode(BinaryNode):
    def _traverse(self):
        if self.left is not None:
            yield from self.left._traverse()
        yield self
        if self.right is not None:
            yield from self.right._traverse()
 
    def __getitem__(self, index):
        for i, item in enumerate(self._traverse()):
            if i == index:
                return item.value
        raise IndexError(f'Index {index} is out of range')
 
tree = IndexableNode(10, left=IndexableNode(5, left=IndexableNode(2)))
 
print(tree[0])    # 2   -- works!
print(tree[1])    # 5   -- works!
print(11 in tree) # False -- works!
 
len(tree)   # CRASH: TypeError: object of type 'IndexableNode' has no len()
```

⚠️ Har dunder method INDEPENDENT hai — ek implement karne se doosre AUTOMATICALLY nahi aate. __getitem__ se indexing/iteration/'in' mila, lekin len() ke liye ALAG SE __len__ chahiye. .count()/.index() jaise methods ke liye aur bhi zyada kaam.

### Solution — collections.abc Module

```python
from collections.abc import Sequence
 
class BadType(Sequence):
    pass
 
foo = BadType()
# TypeError: Can't instantiate abstract class BadType without
# an implementation for abstract methods '__getitem__', '__len__'
```

✅ collections.abc.Sequence se inherit karne pe, Python TURANT bata deta hai kaunse dunder methods ZAROORI hain — object banane se pehle hi error deta hai agar bhool jao. Aur agar __getitem__ + __len__ dono implement kar do, .count()/.index() jaise methods AUTOMATICALLY FREE milte hain (jaise @total_ordering se __eq__+__lt__ se baaki comparisons free milte hain).

🔧 REAL USE CASE: Custom container class banate waqt (Library, tree, custom collection) — collections.abc.Sequence (list jaisi classes ke liye) ya Mapping (dict jaisi classes ke liye) se inherit karo, manually sab dunder methods likhne ke bajaye. Sirf __getitem__ + __len__ do, baaki free milega.

## Summary — Topic 8 in one line

✅ __repr__ (developer) hamesha define karo, collections isi ko use karte hain andar; __str__ (user) optional hai. Custom __eq__ define karne se Python __hash__ ko None kar deta hai — set/dict use karna hai to __hash__ explicitly consistent tarike se define karo. __iter__ ek baar, __next__ har step pe, StopIteration loop-stop signal hai. Har dunder method independent hai — collections.abc use karo taaki poori container semantics (len, count, index) automatically मिले.


---

# 📘 Topic 09


Python @property Decorator

Complete Reference Guide, Concepts, Code & Best Practices

Object Oriented Programming Encapsulation Effective Python

Core Concept (Ek Line Me Memory Trick)

"Code baahar se Variable / Attribute jaisa dikhega ( obj.attr ), lekin andar se Function / Method execute

hoga."

1. Overview & Core Syntax

Python me @property ek built-in decorator hai jo kisi method ko variable ki tarah access karne ki permission deta

hai. Isse Getter, Setter, aur Deleter create kiye jaate hain.

2. Major Problems & Solutions

Problem 1: Dependent Data Update Na Hona (Computed Attributes)

Jab ek attribute doosre attribute par depend karta hai (jaise first_name + last_name = email ), toh

first_name change hone par email purana hi reh jata hai.

Solution: email ko method banakar @property decorator laga do. Ab har baar access karne par fresh data

milta hai bina () lagaye.

Problem 2: Data Bypass (Validation Na Hona)

Normal public variables ( obj.salary = -5000 ) me koi bhi invalid value set kar sakta hai.

Wrong Attempt: Java-style manual setter function ( set_salary(val) ) banana.

Flaw: Developer direct obj.salary = -5000 likh kar aapke setter function ko bypass kar sakta hai.

Solution: @salary.setter use karo. Syntax attribute wahi rehta hai, lekin backend par validation function

automatically trigger hota hai.

Problem 3: Breaking Changes Avoid Karna

Pahle se bane codebase me jab direct attributes use ho rahe ho, toh baad me validation add karne ke liye code

break kiye bina @property me migrate kiya ja sakta hai.

Component Decorator Syntax Trigger Condition

Getter @property Value read karne par ( print(obj.attr) )

Setter @<attr>.setter New value assign karne par ( obj.attr = val )

Deleter @<attr>.deleter Attribute delete karne par ( del obj.attr )

•

•

•

•

Python Mastery Notes · @property Decorator

Haan bilkul, iss video (https://www.youtube.com/watch?v=7wua7EBC-xA) ke aadhar par pure topic ke detailed notes, theory aur code bilkul simple Hinglish/Hindi mai neeche diye gaye hain:

## Python @property Decorator - Complete Notes

@property ek built-in Python decorator hai jo kisi class ke method ko ek variable / attribute ki tarah access karne ki permission deta hai.

### 1. Problem Definition (Problem kya thi?)

Jab hum kisi class me do attributes ke aadhar par teesra attribute banate hain, toh data update hone par dikkat aati hai.

#### Without @property Code (Problem Example):

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # Email initial initialization par hi ban jata hai
        self.email = f"{first}.{last}@email.com"

e1 = Employee("Shantanu", "Khasne")

# First name change kiya
e1.first = "Jay"

print(e1.first) # Output: Jay
print(e1.email) # Output: Shantanu.Khasne@email.com (EMAIL UPDATE NAHI HUA!)
```

Problem: first_name change karne par bhi email purana hi raha kyunki email ek static instance variable ban chuka tha.

### 2. Solution: @property Decorator (Getter)

Is problem ko solve karne ke liye hum email ko method banakar uspar @property lagate hain. Iss se hume method ko e1.email() ki jagah direct e1.email ki tarah access karne ka mauka milta hai.

#### Code with @property:

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # @property lagane se ye method variable ki tarah access hoga
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

e1 = Employee("Shantanu", "Khasne")
e1.first = "Jay"

# Ab email automatic update ho jayega aur () lagane ki zaroorat nahi padegi
print(e1.email) # Output: Jay.Khasne@email.com
```

### 3. Advanced Features: Setter and Deleter

Agar hum direct e1.fullname = "Virat Kohli" jaisa assignment karna chahte hain, toh Python AttributeError deta hai. Iske liye hume Setter aur Deleter ka use karna padta hai.

#### Complete Working Code (Getter, Setter & Deleter):

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # 1. GETTER (Read attribute)
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    # 2. SETTER (Modify/Assign new value)
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    # 3. DELETER (Delete attribute)
    @fullname.deleter
    def fullname(self):
        print("Name Deleted!")
        self.first = None
        self.last = None

# Testing the code
e1 = Employee("Rajendra", "Jaiswal")

# Getter access
print(e1.fullname) # Output: Rajendra Jaiswal

# Setter trigger (Updating full name directly)
e1.fullname = "Virat Kohli"
print(e1.first)    # Output: Virat
print(e1.last)     # Output: Kohli
print(e1.fullname) # Output: Virat Kohli

# Deleter trigger
del e1.fullname    # Output: Name Deleted!
print(e1.first)    # Output: None
```

### Main Summary Points:

Getter (@property): Method ko bina () ke attribute ki tarah call/read karne ke liye.

Setter (@<method_name>.setter): Attribute me nayi value set/assign karne par internal variables ko change karne ke liye.

Deleter (@<method_name>.deleter): del command chalaney par variables ko reset/delete karne ke liye.

## 🐍 Python Mastery Notes

### Phase 2 · Topic 9: Properties (@property, @setter, @deleter)

## 1. Problem — Plain Public Attributes Ka Limitation

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
 
e = Employee("Rahul", 50000)
e.salary = -5000    # koi validation nahi, negative salary allowed!
print(e.salary)     # -5000
```

### Test — Manual Setter Function Ka Problem

🧠 MERA JAWAB THA: Validation ke liye alag se function banata jaha salary >= 0 hoti, salary jaise attributes outside of class access ho rahe hain ye dangerous hai, isko private member banana padega.

✅ ASLI SAHI REASONING: Direction sahi thi — validation aur privacy dono zaroori concerns hain. Lekin ek REAL problem hai jo manual setter function (jaise set_salary()) se solve nahi hota:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.set_salary(salary)
 
    def set_salary(self, value):
        if value < 0:
            raise ValueError("Salary negative nahi ho sakti")
        self.salary = value
 
e = Employee("Rahul", 50000)
e.salary = -5000    # DHYAN DO - ye line ABHI BHI kaam karegi!
```

🔧 CORRECTION / GAP: set_salary() function banane se koi GUARANTEE nahi milti ki log usi function ka use karenge — koi bhi seedha 'e.salary = -5000' likh ke set_salary() ko COMPLETELY BYPASS kar sakta hai. Python attribute access ko rok nahi sakta. Doosra problem: agar codebase mein 50 jagah 'e.salary' direct access ho raha hai, set_salary() introduce karne se saari 50 jagah code CHANGE karna padega — BREAKING CHANGE hai.

## 2. Solution — @property

@property ka magic: syntax 'e.salary = -5000' jaisa hi rehta hai (attribute jaisa dikhta hai), lekin peeche se ek function (jisme validation ho sakti hai) chal jaata hai.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary   # ye ab property setter ko call karega
 
    @property
    def salary(self):
        return self._salary
 
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary negative nahi ho sakti")
        self._salary = value
 
e = Employee("Rahul", 50000)
print(e.salary)     # 50000  -- normal attribute jaisa
 
e.salary = -5000
# ValueError: Salary negative nahi ho sakti  -- ab BYPASS NAHI ho sakta!
```

```python
e.salary          -> @property wala "salary" method call hota hai (getter)
e.salary = value  -> @salary.setter wala "salary" method call hota hai (setter, validation yahan)
 
Actual storage: self._salary  (underscore wala, "internal" convention)
```

## 3. @deleter — Cleanup Logic

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
 
    @property
    def salary(self):
        return self._salary
 
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary negative nahi ho sakti")
        self._salary = value
 
    @salary.deleter
    def salary(self):
        print("Salary record delete ho raha hai!")
        del self._salary
 
e = Employee("Rahul", 50000)
del e.salary
# Salary record delete ho raha hai!
print(e.salary)
# AttributeError: 'Employee' object has no attribute '_salary'
```

```python
del e.salary          -> @salary.deleter wala function call hota hai
                         -> print(...) chalta hai
                         -> del self._salary  -> _salary object se HATA diya gaya
 
print(e.salary)        -> @property wala getter call hota hai
                         -> return self._salary  -> _salary EXIST NAHI karta
                         -> AttributeError!
```

🔧 REAL USE CASE: @deleter cleanup logic ke liye use hota hai — file handle close karna, cache clear karna, log entry banana jab koi resource 'delete' ho raha ho. Simple 'del obj.attr' syntax rakh sakte ho, peeche se proper cleanup bhi ho jaata hai.

## 4. Effective Python — Item 44 (Full Coverage)

📘 EFFECTIVE PYTHON — Item 44: Use Plain Attributes Instead of Setter and Getter Methods

### Anti-Pattern — Java-Style Getters/Setters

Programmers jo Java/C++ se aate hain, wo explicit getter/setter methods likhte hain — YE PYTHONIC NAHI HAI:

```python
class OldResistor:
    def __init__(self, ohms):
        self._ohms = ohms
    def get_ohms(self):
        return self._ohms
    def set_ohms(self, ohms):
        self._ohms = ohms
 
r0 = OldResistor(50e3)
r0.set_ohms(r0.get_ohms() - 4e3)   # clumsy, especially increment jaisa operation ke liye
```

⚠️ Book ka clear recommendation: Python mein HAMESHA simple public attributes se shuru karo (self.ohms = ohms), explicit getter/setter methods KABHI mat likho. Sirf jab zaroorat pade (validation, computed value), tab @property mein MIGRATE karo — bina purane calling code ko tode, kyunki syntax obj.attr hi rehta hai.

### Subtlety — Validation __init__ Mein Bhi Chalta Hai

```python
class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
 
    @property
    def ohms(self):
        return self._ohms
 
    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'ohms must be > 0; got {ohms}')
        self._ohms = ohms
 
BoundedResistance(-5)
# ValueError: ohms must be > 0; got -5
```

💡 -5 object banate waqt hi fail ho jaata hai, kyunki parent Resistor.__init__ 'self.ohms = -5' likhta hai — aur ye line TURANT @ohms.setter ko trigger kar deti hai, object construction COMPLETE hone se pehle. Ye Employee.__init__ mein 'self.salary = salary' wale pattern se EXACTLY match karta hai — same mechanism.

### CRITICAL WARNING — Rule of Least Surprise

```python
class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current   # GETTER mein DUSRA attribute set!
        return self._ohms
 
    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms
 
r7 = MysteriousResistor(10)
r7.current = 0.01
print(f'Before: {r7.voltage:.2f}')   # 0.00
r7.ohms                               # sirf READ kiya
print(f'After: {r7.voltage:.2f}')    # 0.10  -- BIZARRE! sirf padhne se change ho gaya
```

⚠️ GOLDEN RULE: property ka GETTER sirf value RETURN karna chahiye — kabhi bhi dusre attributes modify NAHI karna chahiye. Isse 'bizarre behavior' hota hai jo koi bhi expect nahi karega. Property methods FAST aur SIDE-EFFECT-FREE honi chahiye — koi slow computation, database query, ya unrelated attribute modification nahi. Kuch complex/slow karna hai to NORMAL METHOD use karo, property nahi.

### Bonus — Immutable Attribute Trick

```python
class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
 
    @property
    def ohms(self):
        return self._ohms
 
    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Ohms is immutable")
        self._ohms = ohms
 
r4 = FixedResistance(1e3)
r4.ohms = 2e3
# AttributeError: Ohms is immutable
```

💡 hasattr(self, '_ohms') check karta hai ki attribute PEHLE SE set hai ya nahi — agar haan, to dobara set karne ki koshish pe error. Ye pattern object ko 'construction ke baad immutable' banane ke liye use hota hai.

### Biggest Limitation of @property

Book ka honest point: @property ke methods sirf SUBCLASSES ke beech share ho sakte hain (inheritance se). UNRELATED classes isi implementation ko share nahi kar sakti. Iske liye Python 'descriptors' support karta hai (Item 46 — advanced topic, curriculum mein aage nahi hai abhi).

## Summary — Topic 9 in one line

✅ HAMESHA plain public attributes se shuru karo. Jab validation/computed-value ki zaroorat pade, @property + @x.setter mein migrate karo — syntax same rehta hai (obj.attr), calling code todta nahi. Getter FAST aur side-effect-free rakho (koi unrelated attribute modify na ho, koi slow I/O na ho). @deleter cleanup logic ke liye hai.


---

# 📘 Topic 10


## 🐍 Python Mastery Notes

### Phase 2 · Topic 10: Inheritance, MRO, super() Internals

## 1. super().__init__() Explicit Call Zaroori Hai

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal init: {name}")
 
class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed          # super().__init__(name) MISSING hai
        print(f"Dog init: {breed}")
 
d = Dog("Tommy", "Labrador")
print(d.name)
```

🧠 MERA JAWAB THA: Error aayega, name variable ko search karega jo use milega nahi.

👍 Bilkul sahi tha! Output: 'Dog init: Labrador' phir AttributeError: 'Dog' object has no attribute 'name'.

⚠️ BADA MISCONCEPTION jo clear karna zaroori hai: Python AUTOMATICALLY parent ka __init__ KABHI call nahi karta jab child class apna __init__ DEFINE kar leti hai. Agar child apna khud __init__ likhta hai, parent ka __init__ SIRF tab chalega jab explicitly super().__init__(...) likha jaye.

```python
Dog("Tommy", "Labrador") call hota hai
   -> Python Dog.__init__ dhundta hai -> milta hai -> WAHI chalta hai
   -> Dog.__init__ ke andar: self.breed set hua, print hua
   -> KOI super().__init__() call nahi hua
   -> Animal.__init__ KABHI CHALA HI NAHI
   -> isliye self.name KABHI SET HUA HI NAHI
   -> d.name access karne pe -> AttributeError
```

💡 Agar child class __init__ define NAHI karti (bilkul chhodh deti hai), Python automatically PARENT ka __init__ use kar leta hai (normal attribute lookup, Topic 5 jaisa). Lekin jaise hi child apna __init__ likhta hai, ye COMPLETELY OVERRIDE ho jaata hai — merge NAHI hota, jab tak super() se bulaya na jaye.

## 2. Simple Multiple Inheritance — Left-to-Right

```python
class A:
    def show(self):
        print("A ka show")
 
class B:
    def show(self):
        print("B ka show")
 
class C(A, B):
    pass
 
c = C()
c.show()          # A ka show
print(C.__mro__)  # (C, A, B, object)
```

🧠 MERA JAWAB THA: B, A ko override kar dega, order matter karta hai.

🔧 CORRECTION / GAP: Order matter karta hai — SAHI. Lekin kaunsa jeetega, wahi galat tha. class C(A, B) mein A PEHLE likha hai, isliye A ko PRIORITY milti hai — 'A jeeta, B nahi'. Rule: 'jaisa likha hai, waisa hi priority' — LEFT-TO-RIGHT.

```python
C -> A -> B -> object   (search order)
 
Rule: koi bhi method/attribute access karte time, Python ISI ORDER mein dhundta hai.
```

## 3. Diamond Problem — C3 Linearization

```python
class A:
    def show(self):
        print("A ka show")
 
class B(A):
    def show(self):
        print("B ka show")
 
class C(A):
    def show(self):
        print("C ka show")
 
class D(B, C):
    pass
 
d = D()
d.show()
print(D.__mro__)
```

Structure:

```python
        A
       / \
      B   C
       \ /
        D
```

🧠 MERA JAWAB THA: A output hoga, same left-to-right pattern use hoga.

🔧 CORRECTION / GAP: Output actually 'B ka show' aaya, A NAHI. MRO: D -> B -> C -> A -> object. Simple left-to-right (jo class C(A,B) case mein sahi tha) yahan DIRECTLY apply nahi hota diamond shape ki wajah se.

✅ ASLI SAHI REASONING: A sabse LAST mein hai MRO mein, chahe wo diagram mein 'sabse upar' hai. C3 LINEARIZATION rule: koi bhi PARENT class apne kisi bhi CHILD se PEHLE MRO mein kabhi nahi aa sakta. A dono B aur C ka common parent hai, isliye A dono ke BAAD hi aayega.

```python
D(B, C)  ->  MRO order:  D, B, C, A, object
 
Rule: Koi bhi class apne SAARE subclasses ke baad aati hai MRO mein.
      A, B aur C dono ka parent hai, isliye A, B/C se PEHLE kabhi nahi aa sakta.
```

## 4. super() MRO Chain Follow Karta Hai (Sirf Immediate Parent Nahi)

```python
class A:
    def show(self):
        print("A ka show")
 
class B(A):
    def show(self):
        print("B ka show, ab super() call karunga")
        super().show()
 
class C(A):
    def show(self):
        print("C ka show, ab super() call karunga")
        super().show()
 
class D(B, C):
    def show(self):
        print("D ka show, ab super() call karunga")
        super().show()
 
d = D()
d.show()
 
# Output:
# D ka show, ab super() call karunga
# B ka show, ab super() call karunga
# C ka show, ab super() call karunga
# A ka show
```

✅ super() MRO mein 'is class ke BAAD kaun hai' dekh ke usko call karta hai — sirf immediate parent nahi. D->B->C->A poori chain sequentially chali, kisi ko manually har parent ka naam likhne ki zaroorat nahi padi.

🔧 REAL USE CASE: Django Class-Based Views mein multiple Mixins use hote hain (LoginRequiredMixin, PermissionRequiredMixin, etc.), aur har mixin apna super().dispatch(...) call karta hai — isse saari mixins EK CHAIN mein sequentially execute hoti hain, MRO ke hisaab se.

## 5. Effective Python — Item 40 (Full Coverage)

📘 EFFECTIVE PYTHON — Item 40: Initialize Parent Classes with super

### The Bug — Diamond Inheritance Bina super() Ke

```python
class MyBaseClass:
    def __init__(self, value):
        self.value = value
 
class TimesSeven(MyBaseClass):      # GALAT tarika
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 7
 
class PlusNine(MyBaseClass):        # GALAT tarika
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 9
 
class ThisWay(TimesSeven, PlusNine):
    def __init__(self, value):
        TimesSeven.__init__(self, value)
        PlusNine.__init__(self, value)
 
foo = ThisWay(5)
print('Should be (5*7)+9 = 44 but is', foo.value)
# Should be (5 * 7) + 9 = 44 but is 14   <- BUG!
```

⚠️ MyBaseClass.__init__ DO BAAR chalta hai (ek TimesSeven se, ek PlusNine se). Har baar self.value RESET ho jaata hai original value pe — pehla calculation (35) COMPLETELY LOST ho jaata hai.

```python
TimesSeven.__init__(self, 5):
   MyBaseClass.__init__(self, 5)  -> self.value = 5
   self.value *= 7                 -> self.value = 35
 
PlusNine.__init__(self, 5):
   MyBaseClass.__init__(self, 5)  -> self.value = 5   <- RESET! 35 wala kaam GAYA
   self.value += 9                 -> self.value = 14
 
Final: self.value = 14  (TimesSeven ka kaam completely IGNORE ho gaya)
```

### The Fix — super()

```python
class TimesSevenCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 7
 
class PlusNineCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 9
 
class GoodWay(TimesSevenCorrect, PlusNineCorrect):
    def __init__(self, value):
        super().__init__(value)
 
foo = GoodWay(5)
print('Should be 7*(5+9) = 98 and is', foo.value)
# Should be 7 * (5 + 9) = 98 and is 98   <- SAHI!
 
print(GoodWay.__mro__)
# (GoodWay, TimesSevenCorrect, PlusNineCorrect, MyBaseClass, object)
```

✅ super() ensure karta hai common superclass (diamond ke top pe) SIRF EK BAAR chale, chahe kितनè bhi paths se accessible ho. MyBaseClass.__init__ ab sirf EK BAAR chalta hai.

### WHY Order 'Ulta' Lagta Hai

super().__init__() chain CALLS karta hai top tak (GoodWay -> TimesSevenCorrect -> PlusNineCorrect -> MyBaseClass), lekin ACTUAL KAAM (multiplication/addition) REVERSE order mein hota hai — jab calls UNWIND hoti hain (jaise recursion):

```python
GoodWay(5) call:
   -> TimesSevenCorrect.__init__ chalu -> super().__init__() call (aage badhta)
      -> PlusNineCorrect.__init__ chalu -> super().__init__() call (aage badhta)
         -> MyBaseClass.__init__ chalu -> self.value = 5   <- YAHIN SET, EK BAAR
      <- PlusNineCorrect wapas aata -> self.value += 9  -> 14
   <- TimesSevenCorrect wapas aata -> self.value *= 7   -> 98
```

💡 MyBaseClass.__init__ sirf EK BAAR chala (super() MRO follow karta hai, duplicate calls nahi hoti), aur actual computation UNWINDING phase mein hoti hai — innermost se outermost ki taraf.

## Summary — Topic 10 in one line

✅ super().__init__() explicitly call karna ZAROORI hai jab child apna __init__ define kare. Simple inheritance mein MRO left-to-right hai. Diamond problem mein C3 Linearization guarantee deta hai ki koi parent apne child se PEHLE MRO mein nahi aa sakta. super() MRO CHAIN follow karta hai (sirf immediate parent nahi), aur common superclass ko duplicate-call se bachata hai — isliye multiple inheritance/mixins (jaise Django) mein super() use karna correctness ke liye ZAROORI hai, sirf best-practice nahi.


---

# 📘 Topic 11


## 🐍 Python Mastery Notes

### Phase 2 · Topic 11: Class Methods vs Static Methods vs Instance Methods

## 1. Teen Tarah Ke Methods — WHAT

```python
class Employee:
    company = "TechCorp"
 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
 
    def show(self):                        # INSTANCE method
        return f"{self.name} works at {Employee.company}"
 
    @classmethod
    def from_string(cls, data_string):     # CLASS method
        name, salary = data_string.split("-")
        return cls(name, int(salary))
 
    @staticmethod
    def is_valid_salary(salary):           # STATIC method
        return salary > 0
```

|  | Instance Method | Class Method | Static Method |
| --- | --- | --- | --- |
| Decorator | (koi nahi) | @classmethod | @staticmethod |
| Pehla parameter | self (object) | cls (class) | Koi extra nahi |
| Access | Object + Class dono | Sirf class | Kuch bhi nahi |
| Kab use karo | Object ke data pe kaam | Alternate constructor | Utility function |

## 2. Class Method — Alternate Constructor Pattern

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
 
    @classmethod
    def from_string(cls, data_string):
        name, salary = data_string.split("-")
        return cls(name, int(salary))
 
e = Employee.from_string("Rahul-50000")
print(e.name, e.salary)   # Rahul 50000
```

🧠 MERA JAWAB THA: Output Rahul 50000 sahi tha, lekin samajh nahi aaya cls() kyu kiya gaya, kya ye class method mein aise hi karte hain? Statics/class method pe bahut kam kaam kiya hai.

🔧 CORRECTION / GAP: cls hamesha CLASS METHOD ke andar us CLASS ko point karta hai jisse method call hua (yahan cls=Employee). Isliye 'cls(name, int(salary))' EXACTLY 'Employee(name, int(salary))' jaisa hi hai — naya object banata hai, __init__ ko call karke. cls(...) sirf ek GENERIC way hai class ka naam likhne ka, bina hardcode kiye.

### WHY cls() Likhte Hain, ClassName() Kyun Nahi Directly

```python
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.role = "Manager"
 
m = Manager.from_string("Priya-80000")
print(type(m))          # <class 'Manager'>
print(m.name, m.salary, m.role)   # Priya 80000 Manager
```

📖 NAYA CONCEPT: Manager.from_string(...) call karne pe type(m) 'Manager' aata hai, 'Employee' NAHI — kyunki cls automatically 'Manager' ban jaata hai (jis class se method call hua), bilkul jaise self wahi object hota hai jisse method call hua (Topic 6).

```python
cls(...) use karo:
   Employee.from_string(...) -> cls=Employee -> Employee object banta hai
   Manager.from_string(...)  -> cls=Manager  -> Manager object banta hai
   (SAHI behavior, jis class se call hua wahi object banta hai)
 
ClassName(...) hardcode karo (GALAT tarika):
   Manager.from_string(...)  -> hamesha Employee object banta hai  <- GALAT!
```

🔧 REAL USE CASE: Django models/ORMs mein @classmethod se alternate constructors banaye jaate hain — jaise User.from_json(data), User.from_csv_row(row) — jo bhi subclass ho, cls(...) ki wajah se sahi type ka object banega, bina extra code likhe har subclass ke liye.

## 3. Static Method — Organization, Not Access

```python
class Employee:
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0
 
print(Employee.is_valid_salary(50000))   # True
print(Employee.is_valid_salary(-5000))   # False
```

🧠 MERA JAWAB THA: Salary ko as a argument send kiya gaya hai, isliye static method use access kar sakte hain.

🔧 CORRECTION / GAP: Direction galat thi. Static method ka point 'access karna' NAHI hai — balki ye KUCH BHI access NAHI karta (na self, na cls). Real WHY: ORGANIZATION. Function logically Employee se related hai (salary validation), isliye Employee ke namespace ke andar rakhna sense banata hai, bina object ki zaroorat ke bhi.

```python
# Agar standalone function hota (class ke bahar):
def is_valid_salary(salary):
    return salary > 0
# Kaam to karega, lekin agar Product, Invoice, Order jaisi
# alag classes ke apne is_valid_price, is_valid_amount functions bhi hon,
# SAB global namespace mein bikhre honge, koi organization nahi
 
# @staticmethod se:
Employee.is_valid_salary(50000)    # clearly Employee se related hai
Product.is_valid_price(100)        # clearly Product se related hai
```

✅ @staticmethod ka fayda GROUPING/NAMESPACING hai — function logically kis cheez se related hai, code padhte hi pata chalta hai, bina object banaye bhi call ho sakta hai.

## 4. Final Combined Test

```python
class Circle:
    pi = 3.14159
 
    def __init__(self, radius):
        self.radius = radius
 
    def area(self):
        return Circle.pi * self.radius ** 2
 
    @classmethod
    def unit_circle(cls):
        return cls(1)
 
    @staticmethod
    def is_valid_radius(radius):
        return radius > 0
 
c1 = Circle.unit_circle()
print(c1.radius)              # 1
print(Circle.is_valid_radius(5))  # True
print(c1.area())              # 3.14159
```

👍 Pehle do outputs (1, True) sahi the. Teesra (3.14159 = pi * 1**2) calculate nahi kiya tha, lekin verify karne pe wahi mila.

Categorization: area(self) = INSTANCE method (self.radius object-specific data use karta hai). unit_circle(cls) = CLASS method (@classmethod decorator, alternate constructor, naya object cls(1) se banata hai). is_valid_radius(radius) = STATIC method (@staticmethod, na self na cls, standalone utility check).

## 5. Effective Python — Item 39 (Full Coverage)

📘 EFFECTIVE PYTHON — Item 39: Use @classmethod Polymorphism to Construct Objects

Core insight: Python sirf EK constructor allow karta hai per class (__init__). Agar kai SUBCLASSES hain, aur generic helper code unhe SABKO ek jaisa treat kare (bina har subclass ke liye alag code likhe), @classmethod se alternate constructor pattern yehi solve karta hai.

```python
class GenericInputData:
    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError
 
class PathInputData(GenericInputData):
    def __init__(self, path):
        self.path = path
 
    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))   # cls() - generic constructor
```

✅ Helper function (jaise create_workers) 'input_class.generate_inputs(config)' call kar sakta hai BINA JAANE ki input_class exactly kaunsi subclass hai. cls() ki wajah se GENERIC glue code likha ja sakta hai jo kisi bhi subclass ke saath kaam kare, bina har naye subclass ke liye alag helper function likhne ke.

💡 Yehi principle hai jo Manager/Employee example mein dekha — book isko poore SYSTEM-DESIGN level pe le jaata hai: agar from_string(), from_json() jaise alternate constructors cls() use karte hain, naya subclass add karna BINA existing helper code todhe possible hota hai.

## Summary — Topic 11 in one line

✅ Instance method (self) object ke data pe kaam karta hai. Class method (cls) alternate constructor banata hai — cls(...) use karo, hardcoded class name nahi, taaki subclasses correctly kaam karein. Static method (na self na cls) sirf ORGANIZATIONAL grouping ke liye hai, standalone utility function jaisa. @classmethod polymorphism generic helper code likhne deta hai jo kisi bhi subclass ke saath kaam kare.


---

# 📘 Topic 12


## 🐍 Python Mastery Notes

### Phase 2 · Topic 12: Abstract Classes (abc module)

## 1. Problem — Plain NotImplementedError Ka Limitation

```python
class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError
 
class UpiPayment(PaymentMethod):
    pass   # process_payment implement karna BHOOL gaye!
 
upi = UpiPayment()          # Object BAN GAYA, koi error nahi
upi.process_payment(500)    # Error YAHIN aati hai - bahut DER se
```

### Test — Error Kab Aati Hai

🧠 MERA JAWAB THA: Not implemented error output ayega (unclear jawab, exact timing specify nahi kiya).

🔧 CORRECTION / GAP: Precise timing important thi: 'upi = UpiPayment()' line BINA KISI ERROR ke successfully chal jaati hai — object ban jaata hai. Error SIRF tab aati hai jab 'upi.process_payment(500)' CALL kiya jaata hai — bahut DER se.

```python
Object banate waqt (UpiPayment()):  KOI ERROR NAHI - object successfully ban gaya
Method call karte waqt (process_payment()):  YAHIN error aati hai - bahut DER se
```

⚠️ Production scenario mein danger: UpiPayment object 10 jagah bana liya gaya (koi problem nahi dikhi), system mein pass ho gaya, aur SIRF jab actual payment process hota hai (shayad live users ke saath), tab NotImplementedError crash karta hai. Bahut LATE hai — pehle hi pata chalna chahiye tha object banate waqt.

## 2. Solution — abc Module

```python
from abc import ABC, abstractmethod
 
class PaymentMethod(ABC):           # ABC se inherit karo
    @abstractmethod                  # method ko "MANDATORY" bana deta hai
    def process_payment(self, amount):
        pass
 
class UpiPayment(PaymentMethod):
    pass   # process_payment implement nahi kiya
 
upi = UpiPayment()
# TypeError: Can't instantiate abstract class UpiPayment
# without an implementation for abstract method 'process_payment'
# <- ERROR YAHIN AATI HAI, object banate waqt HI!
```

✅ ABC + @abstractmethod se error TURANT aati hai object creation ke time — method call hone ka wait nahi karta. Bahut JALDI pakda jaata hai, production mein jaane se pehle.

```python
Normal class + NotImplementedError:
   Object BAN sakta hai (koi check nahi)
   Error sirf METHOD CALL hone pe aati hai (bahut der se)
 
ABC + @abstractmethod:
   Object BANNE HI NAHI DETA agar method missing hai
   Error TURANT aati hai, object creation ke time (bahut jaldi, safe)
```

## 3. Rule Parent Class Pe Bhi Apply Hota Hai

```python
from abc import ABC, abstractmethod
 
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
 
    def show_receipt(self, amount):     # NORMAL method, abstract nahi
        return f"Receipt: ₹{amount} paid"
 
payment = PaymentMethod()   # DIRECTLY khud PaymentMethod ka object banane ki koshish
# TypeError: Can't instantiate abstract class PaymentMethod
# without an implementation for abstract method 'process_payment'
```

🧠 MERA JAWAB THA: Methods mein sirf 'pass' likha hai, vo implement nahi kiya gaya, aur abstract ki wajah se.

✅ ASLI SAHI REASONING: Direction sahi thi. Precise mechanism: ABC + @abstractmethod ka rule KISI BHI class pe apply hota hai jisme koi @abstractmethod PROPERLY implement (real code ke saath) nahi hai — chahe wo class khud PARENT ho ya koi subclass. PaymentMethod mein process_payment sirf 'pass' hai, isliye PaymentMethod KHUD BHI 'incomplete' class maani jaati hai.

show_receipt() (normal, non-abstract method) ka is rule pe koi asar nahi padta — sirf @abstractmethod wale methods hi 'mandatory' hote hain. PaymentMethod is liye block hui kyunki uska EK abstract method (process_payment) incomplete tha, show_receipt hone ya na hone se farak nahi padta.

### Conceptual WHY — Design Decision, Bug Nahi

Real duniya mein socho: kya koi 'generic payment method' exist karta hai jo credit card bhi nahi, UPI bhi nahi, kuch bhi specific nahi? NAHI. PaymentMethod sirf ek TEMPLATE/BLUEPRINT hai, jo batata hai 'kaisi classes banani hain' (process_payment zaroor hona chahiye), lekin KHUD USABLE NAHI HAI.

✅ 'Abstract' ka asli matlab: class sirf STRUCTURE define karti hai, khud kaam nahi karti. Python jaan-boojh kar isko directly banne nahi deta — taaki koi galti se PaymentMethod() object bana ke use na kare (jo conceptually meaningless hota, kyunki process_payment() call karte hi crash hota).

🔧 REAL USE CASE: Real production analogy: Shape class jisme area() abstract method ho — koi 'generic shape' nahi banata, sirf Circle, Square, Triangle jaisi CONCRETE shapes banate hain. Shape sirf ek CONTRACT hai jo batata hai 'har shape ka area() hona chahiye.'

## 4. Kab Use Karo Abstract Classes

Jab ek COMMON INTERFACE define karna ho jo saari subclasses ko follow karna ZAROORI ho (jaise PaymentMethod, Shape, DatabaseConnector)

Jab tu chahta ho ki INCOMPLETE implementation JALDI pakdi jaye (object creation time pe), na ki production mein method-call time pe

Jab tu API/framework design kar raha ho jisme dusre developers subclasses banayenge — abstract class unhe FORCE karti hai zaroori methods implement karne ke liye

## Effective Python — Reference

💡 Ye topic (abc module, @abstractmethod) Effective Python mein COVER NAHI hai — poori book mein search karne pe 'abstractmethod' ka koi mention nahi mila. Ye ek genuinely book-ke-bahar ka core Python OOP feature hai.

## Summary — Topic 12 in one line

✅ Plain 'raise NotImplementedError' ka bug bahut DER se pakda jaata hai (method call hone pe). ABC + @abstractmethod se error object CREATION ke time hi aati hai — bahut jaldi, safe. Rule parent aur subclass dono pe apply hota hai. Abstract class sirf TEMPLATE/CONTRACT hai, khud usable nahi — real production APIs/frameworks mein common interface enforce karne ke liye use hota hai.


---

# 📘 Topic 13


## 🐍 Python Mastery Notes

### Phase 2 · Topic 13: Dataclasses (Phase 2 Final Topic)

## 1. Problem — Boilerplate Code

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
 
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
 
p1 = Point(1, 2)
p2 = Point(1, 2)
```

💡 Simple data-holder class ke liye bhi __init__, __repr__, __eq__ manually likhna padta hai (Topic 8 se yaad karo — __eq__ custom karne se __hash__ bhi affect hota hai). Har simple data class ke liye ye saara code BAAR-BAAR likhna padta hai.

## 2. Solution — @dataclass

```python
from dataclasses import dataclass
 
@dataclass
class Point:
    x: int
    y: int
 
p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1)          # Point(x=1, y=2)
print(p1 == p2)     # True
```

🧠 MERA JAWAB THA: Output '1 2' aur True hoga — same vaisa hi kaam karega jaise humne dunder method bana kar kiya tha.

🔧 CORRECTION / GAP: Core concept (dataclass wahi kaam karta hai jo manual dunder methods karte) SAHI tha. Lekin exact output 'Point(x=1, y=2)' hai, '1 2' nahi — kyunki @dataclass ne automatically __repr__ generate kar diya, bilkul wahi format jo Topic 8 mein manually likha tha.

x: int, y: int — ye TYPE HINT/ANNOTATION hai (Phase 3 mein detail mein aayega). @dataclass in annotations ko dekh kar decide karta hai kaunse fields __init__/__repr__/__eq__ mein include karne hain.

```python
Sirf 'x: int' aur 'y: int' likhne se, Python AUTOMATICALLY generate karta hai:
 
1. __init__  — self.x = x, self.y = y wala constructor
2. __repr__  — Point(x=1, y=2) jaisa readable format
3. __eq__    — values compare karta hai (field-by-field)
```

## 3. Mutable Default Trap — Design-Level Pe Blocked (Topic 3 Connect)

```python
from dataclasses import dataclass
 
@dataclass
class Employee:
    name: str
    skills: list = []      # DANGER - mutable default
 
e = Employee("Rahul")
# ValueError: mutable default <class 'list'> for field skills
# is not allowed: use default_factory
```

🧠 MERA JAWAB THA: Pata nahi, shayad allow karega — yaha ek immutable hai (name: str) aur ek mutable (skills: list).

🔧 CORRECTION / GAP: Python ise ALLOW nahi karta — TURANT crash ho jaata hai, class DEFINE hote hi (object banane se pehle bhi). Ye EXACTLY Topic 3 ka mutable default argument trap hai. Farak: normal function (def foo(cart=[])) mein Python ye silently ALLOW kar deta hai (bug bante hi rehta hai). @dataclass mein Python ne is problem ko itna dangerous maana ki COMPLETELY DISALLOW kar diya.

💡 Agar allow hota, to saare Employee objects EK HI shared list use karte — ek employee ka skill add karna SABKE skills mein add ho jaata (jaise Topic 5 ka mutable class variable trap).

### Fix — default_factory

```python
from dataclasses import dataclass, field
 
@dataclass
class Employee:
    name: str
    skills: list = field(default_factory=list)
 
e1 = Employee("Rahul")
e2 = Employee("Priya")
 
e1.skills.append("Python")
e2.skills.append("Django")
 
print(e1.skills)   # ['Python']
print(e2.skills)   # ['Django']   -- ALAG lists, koi sharing nahi
```

✅ field(default_factory=list) ka matlab: har naye object ke liye ek NAYA, FRESH list() call karo — purana object share mat karo. Ye bilkul Topic 3 wala manual fix (if cart is None: cart = []) hai, bas @dataclass ne isko BUILT-IN syntax de diya hai.

## 4. frozen=True — Immutability (Topic 1 Connect)

```python
from dataclasses import dataclass
 
@dataclass(frozen=True)
class Point:
    x: int
    y: int
 
p = Point(1, 2)
print(p)     # Point(x=1, y=2)
p.x = 100
# dataclasses.FrozenInstanceError: cannot assign to field 'x'
```

📖 NAYA CONCEPT: frozen=True object ko IMMUTABLE bana deta hai (jaise tuple, str — Topic 1 ki category). Object banane ke baad, KOI bhi attribute change nahi kar sakta. Python __setattr__ method ko override kar deta hai — attribute assign karne ki koshish automatically BLOCK ho jaati hai, error raise karke.

```python
Normal @dataclass:            p.x = 100  -> kaam kar jaata hai (mutable, jaise list)
@dataclass(frozen=True):      p.x = 100  -> FrozenInstanceError (immutable, jaise tuple)
```

🔧 REAL USE CASE: Configuration objects, ya koi bhi data jo banne ke baad KABHI change nahi hona chahiye — jaise API response ka parsed data, ya settings object. frozen=True guarantee deta hai ki koi accidentally us data ko modify na kare kahin bhi codebase mein.

💡 BONUS: frozen=True classes ka __hash__ bhi AUTOMATICALLY generate hota hai (Topic 8 ka __eq__/__hash__ connection yaad hai?) — kyunki immutable objects SAFELY hash-able hote hain (values kabhi change nahi hongi, hash bhi kabhi invalid nahi hoga).

## Effective Python — Reference

💡 Book mein dataclasses ke liye koi dedicated Item nahi hai. Ek useful mention mila Item 37 ke context mein (namedtuple ki limitations discuss karte waqt): agar tere paas BAHUT ZYADA optional attributes hain, dataclasses module namedtuple se BETTER CHOICE hai — namedtuple mein default values specify nahi kar sakte, aur numerical index se access bhi ho jaata hai jo unintentional usage create kar sakta hai.

## Summary — Topic 13 in one line

✅ @dataclass type hints (x: int) se automatically __init__, __repr__, __eq__ generate karta hai — boilerplate khatam. Mutable defaults (list, dict) DESIGN-LEVEL pe block hote hain (ValueError class define hote hi) — field(default_factory=list) use karo. frozen=True object ko immutable banata hai (FrozenInstanceError modify karne pe) — config/settings objects ke liye ideal.

🎉 PHASE 2 (OOP FROM GROUND UP) — COMPLETE! Topics 5-13 sab cover ho gaye: Class Anatomy, self, __init__/__new__, Dunder Methods, Properties, Inheritance/MRO/super(), Class/Static/Instance Methods, Abstract Classes, Dataclasses. Ab Phase 3 (Advanced Python) shuru hoga: Decorators, Generators/Iterators, Context Managers, Exception Handling, Type Hints, Modules/Packages.


---

# 📘 Topic 15


## 🐍 Python Mastery Notes

### Phase 3 · Topic 15: Generators and Iterators (Deeper Dive)

💡 Basics (generator expressions, memory efficiency, __iter__/__next__ protocol) already cover ho chuke Topics 4 aur 8 mein. Ye doc DEEPER mechanism, yield from, aur ek real production trap cover karta hai.

## 1. yield Ka Exact Pause/Resume Mechanism

```python
def counter():
    print("Start hua")
    yield 1
    print("Beech mein")
    yield 2
    print("End ke pass")
    yield 3
    print("Khatam")
 
gen = counter()
print("Generator bana, lekin abhi tak kuch print nahi hua")
 
print(next(gen))
print("---")
print(next(gen))
```

🧠 MERA JAWAB THA: Pura function nahi chalega, yield aate hi pause ho jayega, next() hi use next tak le jayega.

👍 Core intuition CORRECT thi. Verified output: 'Generator bana...' PEHLE print hua, 'Start hua' BAAD mein (jab next() call hua). counter() call karna sirf generator OBJECT create karta hai — koi code abhi execute nahi hota.

```python
gen = counter()          -> KUCH NAHI hota, sirf generator OBJECT banta hai
                             (function body NAHI chalta)
 
next(gen) [1st call]:
   -> function SHURU se chalna start hota hai
   -> print("Start hua")
   -> yield 1  <- YAHIN RUK JAATA HAI, "1" return hota hai
 
next(gen) [2nd call]:
   -> function WAHI SE resume hota hai (yield 1 ke turant baad)
   -> print("Beech mein")
   -> yield 2  <- YAHIN RUK JAATA HAI, "2" return hota hai
```

✅ Generator function ka LOCAL STATE (variables, execution position) FREEZE ho jaata hai har yield pe, aur EXACTLY wahi se resume hota hai jab agla next() call hota hai. Normal function call hote hi POORA chal jaata hai — generator PAUSE/RESUME kar sakta hai.

## 2. yield from — Generator Delegation

```python
def inner_gen():
    yield 1
    yield 2
    yield 3
 
def outer_gen():
    yield "start"
    yield from inner_gen()
    yield "end"
 
for value in outer_gen():
    print(value)
# start
# 1
# 2
# 3
# end
```

🧠 MERA JAWAB THA: Yield from ke baare mein honestly pata nahi tha, lekin code dekh kar laga: start, phir 1 2 3, phir end aayega kyunki for loop unko print karega.

👍 Output guess sahi tha, aur honestly bata dena ki mechanism pata nahi — yehi sahi approach hai naye concepts ke liye.

yield from inner_gen() EXACTLY equivalent hai isse:

```python
for value in inner_gen():
    yield value
```

💡 yield from ka matlab: inner_gen() ke SAARE values ko, ek-ek karke, outer_gen() KHUD yield karta hai — jaise outer_gen() khud un values ko produce kar raha ho.

### Agar yield from Na Ho — Kya Hota Hai

```python
def outer_gen_WRONG():
    yield "start"
    inner_gen()          # yield from NAHI use kiya, sirf CALL kiya
    yield "end"
 
for value in outer_gen_WRONG():
    print(value)
# start
# end          <- 1, 2, 3 COMPLETELY GAYAB!
```

⚠️ inner_gen() (bina yield from) sirf ek generator OBJECT banata hai, use KAHIN USE nahi karta — na iterate karta hai, na values yield karta hai. Wo generator object TURANT discard ho jaata hai, bina kabhi consume hue.

```python
inner_gen()               -> generator OBJECT banta hai, koi value NIKALI NAHI jaati,
                              object turant IGNORE ho jaata hai
 
yield from inner_gen()    -> generator ko ITERATE karta hai
                              (jaise "for value in inner_gen(): yield value")
                              HAR value ko outer generator KHUD yield karta hai
```

🔧 REAL USE CASE: yield from tab zaroori hota hai jab ek generator, doosre generator ke SAARE values 'pass through' karna chahta ho — manually for+yield loop likhne ke bajaye ek line mein. Library/tree traversal jaise recursive structures mein common hai (jaise left subtree ke saare nodes ko pass through karna).

## 3. DANGEROUS Trap — Generator Exhaustion (Production Bug)

```python
def read_data():
    yield 1
    yield 2
    yield 3
 
def process(gen):
    total = sum(gen)
    count = sum(1 for _ in gen)  # kitne items the, count karne ki koshish
    return total, count
 
data = read_data()
result = process(data)
print(result)   # (6, 0)
```

🧠 MERA JAWAB THA: Output 6 nahi hai (simple loop use karte to hota) — generator pause hone ke baad WAHI SE start hota hai, beginning se nahi. Bas yaha tak samajh aaya hai.

✅ ASLI SAHI REASONING: Core principle 'generator wahi se resume hota hai jaha ruka, beginning se nahi' bilkul CORRECT tha. Precise application: total=6 SAHI hai (sum(gen) ne 1,2,3 saari values le lin). count=0 iska WOHI reason hai — pehli sum() ke baad generator 'END' state pe pahunch chuka hai (saari values consumed). Doosri baar 'for _ in gen' chalne ki koshish karta hai, generator wahi se resume karta hai jaha ruka tha (END se) — koi naya value nahi milti, loop turant khatam, count=0.

```python
Generator ki "position" pehli sum() ke baad:
   1, 2, 3 saari yield ho chuki hain
   generator "END" pe pahunch chuka hai (StopIteration wali state)
 
Doosri baar "for _ in gen" chalne ki koshish:
   generator "wahi se start" karta hai jaha ruka tha -> matlab END se
   koi naya value nahi milti -> loop turant khatam ho jaata hai
   count = 0
```

⚠️ REAL PRODUCTION DANGER: File reading, ya API response streaming jaise cases mein generator ko DO function ko pass kar diya (jaise process() mein), DOOSRA function KUCH BHI nahi paayega — SILENT bug, koi error nahi aata, bas 0 ya khaali result milta hai.

✅ Fix: agar tujhe MULTIPLE baar data chahiye, list() mein CONVERT karo pehle (data = list(read_data())), phir list ko jitni baar chahe use karo — list, generator ke opposite, dobara-dobara iterate ho sakti hai.

## Summary — Topic 15 in one line

✅ Generator function CALL karna sirf object banata hai, code EXECUTE nahi hota — code sirf next() call hone pe chalta hai, aur har yield pe FREEZE hokar wahi se RESUME hota hai agli call pe. yield from ek generator ke saare values doosre generator ke through 'pass through' karta hai (delegation). Generator EK BAAR consume hone ke baad EXHAUSTED ho jaata hai — dobara iterate karne pe KHAALI milta hai, silent bug ban sakta hai — multiple use ke liye list() mein convert karo.


---

# 📘 Topic 16


## 🐍 Python Mastery Notes

### Phase 3 · Topic 16: Context Managers (Deeper Dive)

💡 Basic __enter__/__exit__ (Library example) already cover ho chuka Topic 8 mein. Ye doc exception handling ka exact mechanism aur contextlib.contextmanager shortcut cover karta hai.

## 1. __exit__ Exception Ke Bawajood Bhi Call Hota Hai

```python
class Resource:
    def __enter__(self):
        print("Open")
        return self
 
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Close")
        print(f"exc_type: {exc_type}")
 
with Resource() as r:
    print("Kaam kar rahe hain")
    raise ValueError("Kuch galat hua")
 
# Output:
# Open
# Kaam kar rahe hain
# Close
# exc_type: <class 'ValueError'>
# (exception phir WAAPAS raise hoti hai, bahar propagate)
```

✅ __exit__ HAMESHA call hota hai — chahe with block successfully complete ho ya exception aaye beech mein. Ye try/finally jaisa AUTOMATIC hai, bina explicitly finally likhe. Yehi with ka core WHY hai: cleanup (file close, connection close, lock release) GUARANTEE hota hai.

```python
with Resource() as r:
    print("Kaam kar rahe hain")     -> chal gaya
    raise ValueError(...)            -> exception create hui
 
   YAHIN PYTHON RUK KAR __exit__ CALL KARTA HAI, EXCEPTION KE BAAWJOOD:
   __exit__(exc_type=ValueError, exc_val=..., exc_tb=...) chalta hai
 
   __exit__ complete hone ke baad, EXCEPTION WAPAS RAISE hoti hai
   (jab tak __exit__ explicitly "suppress" na kare)
```

💡 exc_type/exc_val/exc_tb parameters — Python automatically batata hai exception hui thi ya nahi. Normal completion pe teeno None hote hain. Exception hone pe: exc_type = exception ka type, exc_val = actual exception object, exc_tb = traceback info.

## 2. __exit__ Ka Return Value — Suppress vs Propagate

```python
class Resource:
    def __enter__(self):
        return self
 
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exception aayi: {exc_val}")
        return True   # DHYAN DO
 
with Resource() as r:
    raise ValueError("Kuch galat hua")
 
print("Is line tak pahunch gaye!")   # YE CHALTI HAI, bina kisi crash ke!
```

🧠 MERA JAWAB THA: Ye line try se bahar thi (jawab unclear/galat tha, mechanism samajh nahi aaya).

🔧 CORRECTION / GAP: Is code mein koi try/except tha hi nahi. Asal mechanism: return True hone se Python samajh leta hai 'is exception ko __exit__ ne handle kar liya, aage propagate karne ki zaroorat nahi.' Isliye exception WAHI KHATAM ho jaati hai, with block ke BAAHAR normal code chalta rehta hai, jaise kuch hua hi na ho.

```python
__exit__ return None/False (ya kuch return na karna):
   -> exception PROPAGATE hoti hai (normal behavior)
 
__exit__ return True:
   -> exception SUPPRESS ho jaati hai (silently "eaten")
```

⚠️ DANGER: Agar __exit__ BLINDLY hamesha True return kare (chahe exception type kuch bhi ho), SABHI errors silently swallow ho jayenge — including genuine bugs (TypeError, KeyError jo batate hain code mein galti hai). Ye debugging ko NIGHTMARE bana deta hai.

```python
# PRODUCTION-SAFE pattern:
def __exit__(self, exc_type, exc_val, exc_tb):
    if exc_type is SpecificExpectedError:
        return True   # sirf ISI specific error ko suppress karo
    return False       # baaki SAB errors ko propagate hone do
```

## 3. contextlib.contextmanager — Generator-Based Shortcut

```python
from contextlib import contextmanager
 
@contextmanager
def my_resource():
    print("Open ho raha hai")    # <- __enter__ ke equivalent
    yield "resource_object"       # <- yield VALUE hi "as r" wala r banta hai
    print("Close ho raha hai")    # <- __exit__ ke equivalent
 
with my_resource() as r:
    print(f"Kaam kar rahe hain: {r}")
```

🧠 MERA JAWAB THA: Open ho raha hai, resource_object print hoga, aur with wali chalegi vo khud close kar degi (partial - exact mapping specify nahi hui thi).

🔧 CORRECTION / GAP: Output/flow ka intuition sahi tha. Precise mapping: yield SE PEHLE ka code = __enter__ ke equivalent (with block shuru hone se pehle chalta hai). yield ki VALUE = 'as r' mein jo milta hai. yield KE BAAD ka code = __exit__ ke equivalent (with block khatam hone ke baad chalta hai).

```python
Exact execution trace:
1. my_resource() call -> generator object banta hai (Topic 15: koi code abhi nahi chalta)
2. "with" statement generator ko "start" karta hai (jaise next() call kiya)
   -> "Open ho raha hai" print hota hai
   -> yield tak pahunchta hai, RUK JAATA HAI (Topic 15 pause mechanism)
   -> yield ki value "r" mein store hoti hai
3. with block ke andar code chalta hai
4. with block KHATAM hote hi, generator RESUME hota hai (jaise next() phir call hua)
   -> "Close ho raha hai" print hota hai
```

💡 Ye Topic 15 (generator pause/resume) ka DIRECT real-world application hai — @contextmanager poore __enter__/__exit__ class-writing ko ek simple generator function mein convert kar deta hai.

## 4. CRITICAL GAP — try/finally Zaroori Hai contextmanager Mein

⚠️ Class-based __enter__/__exit__ mein cleanup GUARANTEED hota hai (Python khud __exit__ call karta hai, exception ke bawajood). Lekin @contextmanager (generator-based) mein, agar yield ko try/finally mein wrap NAHI kiya, cleanup SKIP ho sakta hai exception ki wajah se!

```python
# GALAT tarika - try/finally ke bina
@contextmanager
def my_resource_risky():
    print("Open ho raha hai")
    yield "resource"
    print("Close ho raha hai")   # exception aayi to ye LINE KABHI NAHI CHALEGI
 
with my_resource_risky() as r:
    raise ValueError("Kuch galat hua")
# Output: "Open ho raha hai", "Kaam kar rahe hain"
# "Close ho raha hai" KABHI PRINT NAHI HUA! Cleanup SKIP ho gaya.
```

```python
# SAHI tarika - try/finally ke saath
@contextmanager
def my_resource_safe():
    print("Open ho raha hai")
    try:
        yield "resource"
    finally:
        print("Close ho raha hai (GUARANTEED)")
 
with my_resource_safe() as r:
    raise ValueError("Kuch galat hua")
# "Close ho raha hai (GUARANTEED)" ab HAMESHA chalta hai, exception ke bawajood
```

✅ GOLDEN RULE: @contextmanager likhte waqt, yield ko HAMESHA try/finally mein wrap karo — warna cleanup code exception ki wajah se skip ho sakta hai. Class-based approach mein ye automatically guaranteed tha, generator-based mein MANUALLY ensure karna padta hai.

## 5. Effective Python — Item 66 (Full Coverage)

📘 EFFECTIVE PYTHON — Item 66: Consider contextlib and with Statements

Book ka core point: with statement try/finally ka reusable, less-noisy version hai:

```python
# with version:
with lock:
    # kaam karo
    ...
 
# EQUIVALENT try/finally version:
lock.acquire()
try:
    # kaam karo
    ...
finally:
    lock.release()
```

💡 with statement BEHTAR hai kyunki: repetitive try/finally code khatam karta hai, aur guarantee deta hai ki har acquire ka corresponding release call bhulega nahi — chahe kितनè bhi complex control flow ho.

### Book Ka Real Example — Temporary Logging Level

```python
from contextlib import contextmanager
import logging
 
@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)   # <- GUARANTEED restore, exception ho ya na ho
 
with debug_logging(logging.DEBUG):
    print('* Inside:')
    my_function()   # debug messages bhi print honge
print('* After:')
my_function()   # sirf error messages (normal level restore ho gaya)
```

🔧 REAL USE CASE: Temporary state change (log level, feature flag, config override) ke liye ideal pattern — with block ke andar naya state active hai, bahar automatically PURANA state restore ho jaata hai, chahe exception aaye ya na aaye.

### with...as Target — Value Directly Access Karna

```python
with open('my_output.txt', 'w') as handle:
    handle.write('This is some data!')
# handle automatically CLOSE ho jaata hai with block khatam hote hi
```

Book ka point: 'as' target ke through with block ka code directly context ke object se interact kar sakta hai — jaise file handle, ya humara logger instance.

## Summary — Topic 16 in one line

✅ __exit__ HAMESHA call hota hai exception ke bawajood — cleanup guarantee karta hai, try/finally jaisa automatic. __exit__ ka return value (True/False) decide karta hai exception SUPPRESS hogi ya PROPAGATE. @contextmanager generator-based shortcut hai (yield se pehle=__enter__, baad=__exit__), lekin yield ko MANUALLY try/finally mein wrap karna zaroori hai warna cleanup exception ki wajah se skip ho sakta hai.


---

# 📘 Topic 17


## 🐍 Python Mastery Notes

### Phase 3 · Topic 17: Exception Handling

## 1. Exception Hierarchy — Order Matters

```python
try:
    result = 10 / 0
except Exception:
    print("Exception pakda")
except ZeroDivisionError:
    print("ZeroDivisionError pakda")
 
# Output: "Exception pakda"  <- ZeroDivisionError wala block KABHI NAHI CHALA!
```

🧠 MERA JAWAB THA: Zero division error wala output aayega.

🔧 CORRECTION / GAP: Output actually 'Exception pakda' tha. Rule: Python except blocks ko TOP SE BOTTOM, order mein check karta hai, aur JO PEHLA MATCH mile usi ko use karta hai — chahe niche koi ZYADA SPECIFIC except block ho. ZeroDivisionError, Exception ka hi SUBCLASS hai (Topic 10 inheritance), isliye except Exception: bhi ise catch kar leta hai. Python pehle match pe hi ruk jaata hai.

```python
try:
    10 / 0 -> ZeroDivisionError raise hui
 
except Exception:          <- YE PEHLE CHECK HOTA HAI
   kya ZeroDivisionError, Exception ka instance hai? -> HAAN (subclass hai)
   -> YAHIN MATCH HO GAYA, block chal gaya
 
except ZeroDivisionError:  <- KABHI CHECK HI NAHI HUA
```

⚠️ GOLDEN RULE: Hamesha SPECIFIC exceptions ko PEHLE likho, GENERIC ko BAAD mein. Ulta order galat hai — specific except blocks kabhi trigger nahi honge, ye silent code smell hai.

```python
try:
    result = 10 / 0
except ZeroDivisionError:      # SPECIFIC pehle
    print("ZeroDivisionError pakda")
except Exception:               # GENERIC baad mein (fallback)
    print("Exception pakda")
```

## 2. Multiple Exceptions Ek Saath — except (Type1, Type2)

```python
def process(value):
    try:
        result = 100 / value
        data = {"a": 1}
        return data[result]
    except (ZeroDivisionError, KeyError) as e:
        print(f"Error hua: {type(e).__name__}")
        return None
 
process(0)   # ZeroDivisionError -> "Error hua: ZeroDivisionError"
process(5)   # 100/5=20.0, data[20.0] not found -> "Error hua: KeyError"
```

🧠 MERA JAWAB THA: Dono baar ZeroDivisionError aayega, kyunki order to vahi hai.

🔧 CORRECTION / GAP: Order yahan matter NAHI karta — ye DO ALAG calls hain, DO ALAG inputs ke saath. process(0): 100/0 khud ek ZeroDivisionError create karta hai. process(5): 100/5 SUCCESSFULLY chal jaata hai (20.0), lekin AGLI line (data[result]) pe ek BILKUL ALAG problem hoti hai (20.0 key dict mein nahi hai) — isliye KeyError aati hai.

except (Type1, Type2) as e: ka matlab: agar Type1 YA Type2 (inme se koi bhi) aaye, dono ko isi EK block mein pakdo — OR logic. Tuple mein jitni chaho utni exception types daal sakte ho.

✅ type(e).__name__ se pata chalta hai EXACTLY kaunsi exception thi — ek hi handler kai tarah ki exceptions ko same tareeke se handle kar sakta hai.

## 3. Custom Exceptions — WHY Zaroori Hain

```python
def process_payment(amount, balance):
    if amount <= 0:
        raise ValueError("Amount positive hona chahiye")
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount
```

⚠️ Dono errors 'ValueError' hi hain. Agar caller ko 'insufficient balance' ka case ALAG SE handle karna ho, usko ERROR MESSAGE KA TEXT PARSE karna padega — FRAGILE approach (message badalte hi code toot jaayega).

### Solution — Custom Exception Classes

```python
class InsufficientBalanceError(Exception):
    pass
 
class InvalidAmountError(Exception):
    pass
 
def process_payment(amount, balance):
    if amount <= 0:
        raise InvalidAmountError("Amount positive hona chahiye")
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")
    return balance - amount
 
try:
    process_payment(1000, 500)
except InsufficientBalanceError:
    print("Balance kam hai — retry logic dikhao")
except InvalidAmountError:
    print("Galat amount — user ko turant bata do")
```

### Test — pass Se Kaam Kaise Chalta Hai

🧠 MERA JAWAB THA: Jab child class ke paas khud ka init na ho to vo parent class ka use kar leta hai.

👍 Bilkul correct! InsufficientBalanceError apna khud __init__ define nahi karta, isliye Python normal attribute lookup follow karta hai (Topic 5/10) — parent (Exception) ka __init__ use ho jaata hai, jo automatically message store kar leta hai.

```python
InsufficientBalanceError(Exception):
    pass    <- koi __init__ nahi
 
raise InsufficientBalanceError("Insufficient balance")
   -> InsufficientBalanceError ka apna __init__ dhunda -> NAHI MILA
   -> parent Exception ka __init__ use hua (jo message store karta hai)
```

## 4. Custom Exception Mein Extra Data — __init__ Override

```python
class InsufficientBalanceError(Exception):
    def __init__(self, required, available):
        self.required = required
        self.available = available
        message = f"Need ₹{required}, but only ₹{available} available"
        super().__init__(message)
 
try:
    raise InsufficientBalanceError(1000, 500)
except InsufficientBalanceError as e:
    print(f"Error message: {e}")       # Need ₹1000, but only ₹500 available
    print(f"Shortfall: {e.required - e.available}")   # 500
```

### CRITICAL — super().__init__(message) Kyun Zaroori Hai

🧠 MERA JAWAB THA: Yaad nahi raha, tum hi batao.

📖 NAYA CONCEPT: BaseException.__new__ (Topic 7 level pe) OBJECT BANATE WAQT hi automatically self.args = constructor arguments set kar deta hai — __init__ chalne se PEHLE. Agar super().__init__(message) NAHI likhte, self.args wahi RAW constructor arguments (1000, 500) rakh leta hai — humara formatted message kahin store hi nahi hota. str(e) tab RAW tuple '(1000, 500)' dikhata hai, formatted message nahi!

```python
__new__ level (Topic 7):
   self.args automatically (1000, 500) set ho jaata hai <- RAW args
 
__init__ level (humara custom code):
   message = "Need ₹1000..."   <- ye variable bana, but...
   super().__init__(message) NAHI likha
   -> self.args ko humara formatted message OVERRIDE nahi karta
   -> str(e) abhi bhi RAW (1000, 500) dikhata hai
```

✅ super().__init__(message) call karne se Exception.__init__ chalta hai, jo self.args ko humare diye gaye message se OVERWRITE kar deta hai. Yehi Topic 10 wala pattern hai — super() na likhne se parent ka initialization properly nahi hota, yahan specifically message-storage logic skip ho jaata hai.

## 5. Effective Python — Item 65 (try/except/else/finally)

📘 EFFECTIVE PYTHON — Item 65: Take Advantage of Each Block in try/except/else/finally

```python
UNDEFINED = object()
def divide_json(path):
    handle = open(path, 'r+')          # May raise OSError
    try:
        data = handle.read()            # May raise UnicodeDecodeError
        op = json.loads(data)           # May raise ValueError
        value = (op['numerator'] / op['denominator'])  # May raise ZeroDivisionError
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)
        return value
    finally:
        handle.close()   # Always runs
```

| Block | Kab Chalta Hai |
| --- | --- |
| try | Main code jo exception raise kar sakta hai |
| except | SIRF agar try mein specified exception aayi |
| else | SIRF agar try SUCCESSFULLY complete hua (koi exception nahi) |
| finally | HAMESHA chalta hai — success ho, exception ho, ya except ke andar bhi |

💡 else block ka WHY: try/except ke turant baad jo code hai use VISUALLY ALAG dikhata hai except block se. Ye exception-propagation behavior CLEAR karta hai — else mein jo exceptions aayen, wo INTENTIONALLY unhandled hain (upar propagate hongi), jabki try mein jo hain wo DELIBERATELY handle ki ja rahi hain.

🔧 REAL USE CASE: File read + process + write + cleanup jaise multi-step operations mein ye pattern perfect hai: try=risky read/parse, except=expected errors handle karo, else=safe write/update karo (sirf jab parsing successful thi), finally=file handle GUARANTEED close karo.

## 6. Effective Python — Item 87 (Root Exception Pattern)

📘 EFFECTIVE PYTHON — Item 87: Define a Root Exception to Insulate Callers from APIs

Agar module/library banate ho jo kai custom exceptions raise karta hai, ek COMMON ROOT exception banao, aur saari specific exceptions usi se INHERIT karayen.

```python
class Error(Exception):
    """Base-class for all exceptions raised by this module."""
 
class InvalidDensityError(Error):
    """Density value mein problem hai."""
 
class InvalidVolumeError(Error):
    """Volume value mein problem hai."""
 
def determine_weight(volume, density):
    if density < 0:
        raise InvalidDensityError('Density must be positive')
    if volume < 0:
        raise InvalidVolumeError('Volume must be positive')
    return volume * density
 
# Consumer - saari specific exceptions ek saath pakad sakta hai:
try:
    weight = determine_weight(1, -1)
except Error:   # ROOT exception - sab yahin catch
    print("Kisi bhi module-specific error aayi")
```

```python
Error (root, sabka common parent)
 ├── InvalidDensityError
 └── InvalidVolumeError
 
Consumer options:
   except InvalidDensityError:  -> sirf specific case
   except Error:                 -> saari module-specific errors ek saath
```

✅ WHY POWERFUL: (1) Caller FLEXIBILITY — specific ya generic, dono tarike se catch kar sakte hain. (2) BUG DETECTION — agar module kabhi aisi exception raise kare jo Error se inherit NAHI karti, consumer ka 'except Error:' use catch NAHI karega — turant pata chal jaayega ki ye ACTUAL BUG hai, intentional error nahi.

🔧 REAL USE CASE: Django/FastAPI projects mein common pattern: class APIError(Exception), phir ValidationError(APIError), AuthenticationError(APIError), etc. — middleware saari API errors ko ek jagah handle kar sakta hai (except APIError:), lekin specific error types bhi individually differentiate ho sakte hain.

## Summary — Topic 17 in one line

✅ except blocks TOP-TO-BOTTOM order mein check hote hain — specific PEHLE, generic BAAD mein likho. except (Type1, Type2) multiple exceptions OR logic se ek block mein catch karta hai. Custom exceptions specific error-handling enable karte hain (Exception se inherit, __init__ auto-inherit hota hai). super().__init__(message) zaroori hai taaki str(e) formatted message dikhaye, raw args nahi. else block try ke SAFE-SUCCESS code ko except se visually alag karta hai. Root Exception pattern (module-level base class) API design mein caller flexibility aur bug detection dono deta hai.


---

# 📘 Topic 18


## 🐍 Python Mastery Notes

### Phase 3 · Topic 18: Type Hints

## 1. Problem — Silent Type Bugs

```python
def calculate_total(price, quantity):
    return price * quantity
 
result = calculate_total("100", 5)
print(result)          # '100100100100100'  (STRING repetition!)
print(type(result))    # <class 'str'>
```

🧠 MERA JAWAB THA: Ye 100 ko 5 baar print kar dega.

🔧 CORRECTION / GAP: Concept (repetition) sahi tha, but exact behavior: "100" * 5 ek STRING repetition/concatenation hai ("100100100100100"), print nahi ho raha 5 baar — EK hi combined string return ho rahi hai.

⚠️ SABSE BADA PROBLEM: "100" * 5 ERROR NAHI deta — Python str*int ko VALID operation maanta hai. Koi crash nahi hota, code SILENTLY galat result deta hai. Bina type hints ke, Python KABHI bataega nahi ki galat type pass hui hai.

## 2. Solution Syntax — Type Hints

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
```

price: float = price float hona chahiye. quantity: int = quantity int hona chahiye. -> float = function float return karega.

### CRITICAL TEST — Kya Ye Runtime Pe Enforce Hote Hain?

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
 
result = calculate_total("100", 5)
print(result)   # '100100100100100'  <- SAME BUG, koi error nahi!
```

🧠 MERA JAWAB THA: Ek Python dev inka use karke decide kar leta hai ki value type kya hona chahiye, jisse type error se bach sake.

🔧 CORRECTION / GAP: Direction sahi thi (developer guidance), lekin ASLI power miss hui: Python KHUD runtime pe kabhi check nahi karta type hints ko — sirf METADATA hain. Asli value ek SEPARATE TOOL se aati hai: mypy (static type checker) — jo code BINA RUN KIYE padhta hai aur type hints ke against verify karta hai.

```python
Python runtime:        Type hints ko IGNORE karta hai, kuch enforce nahi karta
mypy (static checker):  Type hints ko PADHTA hai, code RUN kiye bina check karta hai
 
calculate_total("100", 5)   -> mypy turant flag karega:
   "Argument 'price' has type 'str', expected 'float'"
   (ERROR CODE RUN HONE SE PEHLE, editor mein hi dikh jaata hai)
```

✅ Type hints ka asli value: (1) Documentation — function padhte hi pata chalta hai kya expect hai. (2) IDE support — autocomplete, inline errors. (3) mypy/static analysis — bugs CODE REVIEW/CI mein catch hote hain, production se pehle. (4) Team collaboration — dusre developers turant samajh jate hain.

## 3. Optional aur Union — Advanced Type Hints

```python
from typing import Optional, Union
 
def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Rahul"
    return None
 
def process_id(value: Union[int, str]) -> str:
    return str(value)
```

### Optional[str] — Exact Matlab

🧠 MERA JAWAB THA: Optional int ke alava str bhi de sakte hai.

🔧 CORRECTION / GAP: Optional[str] ka int se koi lena-dena nahi hai. Optional[str] = Union[str, None] ka SHORTCUT hai — matlab 'ya to str return hoga, ya None return hoga', koi third option nahi.

Connect Topic 3 (Item 20) se: function jab 'special case/error' batana chahta hai, None return karta hai. Problem ye thi ki function signature dekh ke pata hi nahi chalta tha ki function kabhi None bhi de sakta hai. Optional[str] ye EXPLICITLY declare kar deta hai.

```python
def find_user(user_id: int) -> str:      # BINA Optional ke
    if user_id == 1:
        return "Rahul"
    return None   # SILENTLY galat — signature ne bola tha sirf "str" aayega!
 
def find_user(user_id: int) -> Optional[str]:   # Optional SAAF SAAF bata raha hai
    if user_id == 1:
        return "Rahul"
    return None   # ab EXPECTED hai, signature already declare kar chuka tha
 
result = find_user(2)
if result is None:          # mypy caller ko REMIND karega ye check karne ke liye
    print("User nahi mila")
else:
    result.upper()           # yahan mypy jaanta hai result definitely str hai
```

✅ mypy ka real fayda: agar Optional[str] return karne wale function ka result BINA None check kiye directly use karo (result.upper() bina check ke), mypy TURANT warning dega — Item 20 wala bug class, ab TOOL LEVEL pe catch ho raha hai.

### Union[int, str] — Custom Combination

Union[Type1, Type2, ...] ka matlab: 'in mein se KOI BHI ek type ho sakta hai' — tu KHUD decide karta hai kaunse types allowed hain.

|  | Optional[str] | Union[int, str] |
| --- | --- | --- |
| Kya represent karta hai | str YA None (dusra option HAMESHA None) | int YA str (tu KHUD choose karta hai types) |
| Equivalent to | Union[str, None] | (khud complete hai) |
| Kab use karo | Function kabhi None return/accept kar sakta ho | Parameter genuinely multiple concrete types accept karta ho |

```python
process_id(123)      # valid - int hai
process_id("abc123") # valid - str hai
process_id(3.14)     # mypy ERROR - float allowed nahi hai Union[int, str] mein
```

## 4. Effective Python — Item 90 (Full Coverage)

📘 EFFECTIVE PYTHON — Item 90: Consider Static Analysis via typing to Obviate Bugs

Book ka core point: typing module KHUD koi type-checking implement nahi karta — ye sirf ek COMMON LIBRARY hai types define karne ke liye, jo SEPARATE tools (mypy, pytype, pyright, pyre) consume karte hain.

### Simple Example — Type Mismatch

```python
def subtract(a: int, b: int) -> int:
    return a - b
 
subtract(10, '5')   # Oops: passed string value
 
$ python3 -m mypy --strict example.py
.../example.py:4: error: Argument 2 to "subtract" has
incompatible type "str"; expected "int"
```

### POWERFUL Example — mypy Tere Pichle Sikhe Bugs Pakadta Hai!

```python
class Counter:
    def __init__(self) -> None:
        self.value: int = 0        # field annotation
 
    def add(self, offset: int) -> None:
        value += offset            # BUG: "self." bhool gaye
 
    def get(self) -> int:
        self.value                 # BUG: "return" bhool gaye
 
counter = Counter()
counter.add(5)
 
$ python3 -m mypy --strict example.py
.../example.py:6: error: Name 'value' is not defined
.../example.py:8: error: Missing return statement
```

⚠️ Bina type hints ke: counter.add(5) call karne pe RUNTIME UnboundLocalError crash (Topic 2 ka scoping bug — self. bhool gaye). counter.get() call karne pe None milta jabki int expected tha (Topic 3 ka implicit-None bug — return bhool gaye).

✅ mypy --strict CHALANE PE, dono bugs CODE RUN KIYE BINA hi pakde jate hain! Ye book ka core message hai: Type hints + mypy = tere pehle se sikhe hue SAARE bugs (LEGB scoping mistakes, missing returns, wrong types) ko production mein jaane se PEHLE hi pakad lo, bina test cases likhe bhi.

### Gradual Typing

💡 Type hints OPTIONAL hain — poora codebase ek saath type-annotate karne ki zaroorat nahi. 'Gradual typing' ka matlab: codebase INCREMENTALLY update kiya ja sakta hai types specify karne ke liye, jaha-jaha zaroorat ho waha se shuru karo.

## Summary — Topic 18 in one line

✅ Type hints (param: type, -> type) Python RUNTIME pe enforce NAHI hote — sirf metadata hain. Real value mypy jaisa STATIC ANALYSIS tool deta hai, jo code run kiye bina bugs pakadta hai (type mismatches, Topic 2 ke UnboundLocalError jaise scoping bugs, Topic 3 ke missing-return bugs). Optional[X] = Union[X, None] — function ke None-return-karne-wale-behavior ko explicitly document karta hai (Item 20 se connect). Union[X, Y] custom multiple types allow karta hai.


---

# 📘 Topic 19


## 🐍 Python Mastery Notes

### Phase 3 · Topic 19: Modules and Packages (Phase 3 Final Topic)

## 1. Module vs Package — WHAT

Module — koi bhi single .py file (jaise utils.py)

Package — ek FOLDER jisme .py files hon, aur usme (traditionally) ek __init__.py ho

```python
myproject/
├── main.py
└── mypackage/
    ├── __init__.py
    ├── helpers.py
    └── models.py
```

## 2. Test — __init__.py Mandatory Hai Kya?

```python
# mypackage/helpers.py (bina __init__.py ke folder mein)
def greet(name):
    return f"Hello {name}"
 
# main.py
from mypackage.helpers import greet
print(greet("RK"))
```

🧠 MERA JAWAB THA: Ye option hai ya nahi, but ye import ho jayegi aur run bhi ho jayegi without error.

👍 Bilkul sahi! Verified — bina __init__.py ke bhi 'Hello RK' successfully print hua, koi error nahi. Python 3.3+ mein ye 'namespace packages' concept ki wajah se possible hai — Python __init__.py ke bina bhi folder ko package ki tarah treat kar leta hai.

💡 BUT IMPORTANT: Namespace packages sirf 'from mypackage.helpers import greet' (poora path) ke liye kaam karte hain. 'from mypackage import greet' (directly package se) BINA __init__.py ke KAAM NAHI karega — us case mein __init__.py zaroori hai.

## 3. __init__.py Ka Role — Package Ka Entry Point

```python
# mypackage/__init__.py
from .helpers import greet
from .models import CONFIG
 
# main.py
from mypackage import greet, CONFIG   # AB YE KAAM KARTA HAI, directly package se!
print(greet("RK"))
print(CONFIG)
```

### Test — . (Dot) Relative Import Ka Matlab

🧠 MERA JAWAB THA: Dot(.) current folder se import kar rahe hain (same folders se).

🔧 CORRECTION / GAP: Direction sahi thi, precise matlab: '.' = 'isi PACKAGE ke andar se, module dhoondo' — relative to jaha __init__.py KHUD hai. from .helpers = mypackage.helpers, relative import. Absolute import (from mypackage.helpers import greet) bhi kaam karta, lekin relative import BETTER PRACTICE hai — agar package ka naam badal jaye (mypackage -> myapp), relative imports automatically kaam karte rehte hain kyunki wo naam pe depend nahi karte, sirf structure pe.

```python
mypackage/
├── __init__.py     <- YAHAN se "from .helpers import greet" likha hai
├── helpers.py       <- "." isi FOLDER ke andar wale "helpers.py" ko point karta hai
└── models.py
```

### WHY Ye Lines 'Expose' Karti Hain

Bina __init__.py mein import kiye, greet sirf mypackage.helpers.greet (poora path) se accessible hota — kyunki greet, helpers.py MODULE ke andar define hai, mypackage package DIRECTLY nahi jaanta us naam ko.

```python
BINA __init__.py imports ke:
   from mypackage import greet          -> ERROR! mypackage seedha "greet" nahi jaanta
   from mypackage.helpers import greet  -> Ye chalega (poora path specify kiya)
 
__init__.py mein "from .helpers import greet" likhne SE:
   greet naam __init__.py ke NAMESPACE mein "aa jaata hai"
   -> from mypackage import greet  -> AB KAAM KAREGA
```

✅ __init__.py package ka 'ENTRY POINT' hai — jo bhi is file mein import ho jaata hai, wo PACKAGE-LEVEL pe directly accessible ban jaata hai, caller ko internal file-structure ka pata hone ki zaroorat nahi rehti.

## 4. __all__ — Sirf Wildcard (*) Imports Ko Control Karta Hai

```python
# mypackage/__init__.py
from .helpers import greet
from .models import CONFIG
INTERNAL_SECRET = "should not be exposed"
__all__ = ['greet']
 
# main.py
from mypackage import *
print(greet("RK"))       # works - 'greet' hai __all__ mein
print(CONFIG)             # NameError! CONFIG __all__ mein nahi hai
print(INTERNAL_SECRET)   # NameError!
```

🧠 MERA JAWAB THA: __all__ ke jariye hum ye likhte hain ki * lagane pe kaun kaun si file import hongi.

👍 Concept sahi tha — __all__ control karta hai * ke through kya import hota hai. Ek precision zaroori thi: kya ye EXPLICIT imports ko bhi block karta hai?

```python
from mypackage import CONFIG   # EXPLICIT import, bina * ke
print(CONFIG)   # WORKS! __all__ mein na hone ke bawajood
```

🔧 CORRECTION / GAP: __all__ KISI CHEEZ KO 'PRIVATE' NAHI banata — ye SIRF from module import * ka behavior control karta hai. Explicit naam se import (from mypackage import CONFIG) __all__ se COMPLETELY UNAFFECTED hai — chahe wo naam __all__ mein ho ya na ho.

```python
__all__ = ['greet']
 
from mypackage import *          -> SIRF "greet" milega
from mypackage import CONFIG      -> KAAM KAREGA (explicit, __all__ isko block nahi karta)
from mypackage import greet       -> KAAM KAREGA (explicit, aur __all__ mein bhi hai)
```

✅ Rule: __all__ documentation ki tarah kaam karta hai — batata hai package ka 'official public API' jab koi import * kare. Python enforcement level pe ye SIRF * ko affect karta hai, explicit imports ko kabhi nahi rokta.

## 5. __all__ Ki Absence Mein Default Rule (Underscore Convention)

```python
# __all__ define NAHI kiya:
from .helpers import greet
from .models import CONFIG
_internal_var = "hidden"
 
# main.py
from mypackage import *
print(greet("RK"))       # works
print(CONFIG)             # works
print(_internal_var)      # NameError! underscore se shuru hone wale naam import * se NAHI aate
```

💡 Agar __all__ PRESENT NAHI hai, import * SIRF 'public' attributes import karta hai — matlab jo naam UNDERSCORE (_) se start NAHI hote. Topic 9 ka '_salary' jaisa 'internal' naming convention yahan import * behavior ko bhi affect karta hai, sirf documentation nahi hai.

## 6. Effective Python — Item 85 (Full Coverage)

📘 EFFECTIVE PYTHON — Item 85: Use Packages to Organize Modules and Provide Stable APIs

Book ke do primary purposes for packages:

### Purpose 1 — Namespaces (Naming Conflicts Avoid Karna)

```python
# Problem: dono modules mein 'inspect' function hai
from analysis.utils import inspect
from frontend.utils import inspect   # OVERWRITES! pehla wala GAYAB
 
# Fix 1 - 'as' clause se rename karo:
from analysis.utils import inspect as analysis_inspect
from frontend.utils import inspect as frontend_inspect
 
# Fix 2 - highest unique module name se access karo:
import analysis.utils
import frontend.utils
analysis.utils.inspect(value)
frontend.utils.inspect(value)
```

🔧 REAL USE CASE: Bade codebases mein alag teams ke same-naam wale functions/classes clash kar sakte hain — packages namespace provide karte hain taaki 'as' rename ya full-path access se conflict resolve ho sake.

### Purpose 2 — Stable APIs (Production-Critical Pattern)

```python
# models.py
__all__ = ['Projectile']
class Projectile:
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity
 
# utils.py
from .models import Projectile
__all__ = ['simulate_collision']
def _dot_product(a, b):   # underscore = internal helper
    ...
def simulate_collision(a, b):
    ...
 
# __init__.py — explicit API build karna
__all__ = []
from .models import *
__all__ += models.__all__
from .utils import *
__all__ += utils.__all__
```

✅ WHY: Consumers HAMESHA 'from mypackage import X' use karenge, kabhi 'mypackage.models.X' ya 'mypackage.utils.X' directly nahi. Isse internal files REORGANIZE/RENAME/DELETE kiye ja sakte hain (jaise models.py delete karna) BINA consumers ka code todhe — unhone hamesha sirf mypackage se import kiya tha.

🔧 REAL USE CASE: Open-source packages ya large team codebases mein: __init__.py mein explicitly saare internal modules se import karke __all__ build karna ek STABLE API CONTRACT deta hai — internal reorganization se external consumers safe rehte hain.

## Summary — Topic 19 in one line

✅ Python 3.3+ mein __init__.py OPTIONAL hai poore path imports ke liye (namespace packages), lekin package-level direct imports (from mypackage import x) ke liye __init__.py mein explicit import ZAROORI hai. Relative imports (.) package-structure-relative hain, naam-independent. __all__ SIRF import * ko control karta hai, explicit imports ko kabhi nahi rokta — bina __all__ ke, underscore-prefixed naam automatically import * se exclude ho jate hain. Packages ka real production use: namespace conflicts avoid karna, aur STABLE API provide karna (internal refactoring, external consumers ko affect kiye bina).

🎉 PHASE 3 (ADVANCED PYTHON) — COMPLETE! Topics 14-19 sab cover ho gaye: Decorators, Generators/Iterators, Context Managers, Exception Handling, Type Hints, Modules/Packages. Ab Phase 4 (Production Patterns) shuru hoga: Logging, Configuration Management, Design Patterns (Singleton, Factory, Observer, Strategy), SOLID Principles, Testing Mindset, Code Quality.


---

# 📘 Topic 20


## 🐍 Python Mastery Notes

### Phase 4 · Topic 20: Logging (Not print)

## 1. Problem — print() Ki Limitations Production Mein

```python
def process_order(order_id, amount):
    print(f"Processing order {order_id} with amount {amount}")
    if amount < 0:
        print(f"ERROR: Invalid amount for order {order_id}")
        return None
    print(f"Order {order_id} processed successfully")
    return amount
```

🧠 MERA JAWAB THA: Print zyada help nahi kar payega, na hi vo timestamp dikha payega na ki error/info/warning file mein likh payega.

👍 Bilkul sahi — 3 core limitations of print(): (1) koi TIMESTAMP nahi, (2) koi LEVEL filtering nahi (INFO/ERROR/WARNING sab same treat hote), (3) koi FILE persistence nahi — server background mein chal raha ho to output dikhta hi nahi.

## 2. Solution — logging Module

```python
import logging
 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
 
def process_order(order_id, amount):
    logging.info(f"Processing order {order_id} with amount {amount}")
    if amount < 0:
        logging.error(f"Invalid amount for order {order_id}")
        return None
    logging.info(f"Order {order_id} processed successfully")
    return amount
 
# Output:
# 2026-07-18 11:48:22,686 - INFO - Processing order 101 with amount -50
# 2026-07-18 11:48:22,689 - ERROR - Invalid amount for order 101
```

✅ logging automatically TIMESTAMP deta hai, LEVEL (INFO/ERROR) clearly labeled karta hai, aur file mein bhi likha ja sakta hai (handler configure karke) — teeno print() ki limitations solve ho jaati hain.

## 3. Log Levels — Hierarchy Aur Threshold Filtering

```python
DEBUG    < INFO    < WARNING    < ERROR    < CRITICAL
(sabse kam important)              (sabse zyada critical)
```

```python
import logging
 
logging.basicConfig(level=logging.WARNING, format='%(levelname)s - %(message)s')
 
logging.debug("Ye debug message hai")
logging.info("Ye info message hai")
logging.warning("Ye warning message hai")
logging.error("Ye error message hai")
```

🧠 MERA JAWAB THA: First time seekh raha hoon, mujhe nahi pata.

📖 NAYA CONCEPT: level=logging.WARNING set karne ka matlab hai: 'SIRF ye level aur usse zyada critical (ERROR, CRITICAL) DIKHAO'. Verified output: sirf WARNING aur ERROR print hue, DEBUG aur INFO COMPLETELY SILENT rahe.

```python
Hierarchy: DEBUG < INFO < WARNING < ERROR < CRITICAL
 
level=WARNING set kiya:
   DEBUG    -> IGNORE (WARNING se neeche hai)
   INFO     -> IGNORE (WARNING se neeche hai)
   WARNING  -> DIKHEGA (threshold hai ye)
   ERROR    -> DIKHEGA (WARNING se upar hai)
   CRITICAL -> DIKHEGA (WARNING se upar hai)
```

🔧 REAL USE CASE: Development mein level=DEBUG set karo (sab dikhega, detailed tracing). Production mein deploy karte waqt SIRF level config badlo (level=WARNING ya ERROR) — poore codebase mein jo bhi logging.debug()/logging.info() calls hain, wo AUTOMATICALLY silent ho jaate hain, bina ek bhi line code se hataye!

## 4. logging.exception() — Automatic Traceback Capture

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.exception("Division fail hui")
        return None
 
divide(10, 0)
 
# Output:
# ERROR - Division fail hui
# Traceback (most recent call last):
#   File "...", line 7, in divide
# ZeroDivisionError: division by zero
```

🧠 MERA JAWAB THA: Humne yahan exception lagayi wahan se, ye sach mein interesting hai, hum exception bhi use kar sakte hain.

📖 NAYA CONCEPT: logging.exception() SIRF except block ke andar se call hone ke liye designed hai. Ye AUTOMATICALLY current exception ki poori TRACEBACK information capture karke apne message ke saath attach kar deta hai — koi manual print nahi karna padta.

```python
logging.error("message")      -> sirf message print hota hai
 
logging.exception("message")  -> message + PURI TRACEBACK print hoti hai
                                   (kaunsi exception, kaunsi line, kaunsa function)
```

💡 PRODUCTION SCENARIO: App crash hua, sirf log file hai, koi live terminal nahi. Agar log sirf 'Division fail hui' kahe, pata NAHI chalega kis line pe, kaunsi exact exception type, kaunsa function chain tha. logging.exception() ye SAARI information automatically capture kar leta hai.

✅ GOLDEN RULE: Jab bhi except block ke andar logging karo, aur exception details zaroori hon debugging ke liye, logging.exception() use karo (na ki logging.error()) — automatically poori traceback milti hai.

## Effective Python — Reference

💡 Book mein logging module pe koi dedicated Item nahi hai. Closest related content Item 89 (warnings module) mein hai, jaha logging.captureWarnings ka mention tha — but wo deprecation-warnings ke context mein hai, alag topic.

## Summary — Topic 20 in one line

✅ print() production mein insufficient hai — no timestamp, no level filtering, no persistence. logging module ye teeno solve karta hai. Log levels (DEBUG<INFO<WARNING<ERROR<CRITICAL) threshold-based filtering dete hain — production mein sirf config-level pe verbosity control hoti hai, code touch kiye bina. logging.exception() except block ke andar automatic traceback capture karta hai — production debugging ke liye essential.


---

# ✨ Optional Visual / Animation Layer

> **This section does not replace or alter the notes above.**  
> It is a small toolkit you can use if you render these notes with a Markdown
> engine that permits HTML/CSS. GitHub's Markdown sanitization may limit CSS.

## 🎬 Animated Heading

```html
<h2 class="python-animated-title">🐍 Python Mastery</h2>

<style>
.python-animated-title {
  animation: floatTitle 2.5s ease-in-out infinite;
}

@keyframes floatTitle {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-6px); }
}
</style>
```

## 🪄 Animated Progress Bar

```html
<div style="width:100%;background:#eee;border-radius:12px;overflow:hidden;">
  <div style="width:75%;padding:6px 0;text-align:center;animation:pulse 1.5s infinite;">
    Python Progress — 75%
  </div>
</div>
```

> ⚠️ CSS/HTML support varies by Markdown platform. For GitHub, prefer
> Mermaid diagrams, GIFs, and the platform's supported Markdown features.

---

# 🏁 End of Python Mastery Notes

**20 Topics · Source content preserved · Markdown presentation enhanced**
