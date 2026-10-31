# QA Automation / SDET — Debugging Mastery & AI-Assisted Engineering
## Manual Python + Pytest + Playwright Debugging se Production-Grade AI Workflow tak
### Deep Learning Roadmap | Hinglish | Step-by-Step Mentor Program

> **Mission:** Sirf automated tests likhna nahi. Aisa QA Automation / SDET engineer banna jo failure ko systematically investigate kare, root cause prove kare, safe fix kare, flaky tests reduce kare, reliable CI pipelines maintain kare aur AI ko genuinely time-saving engineering assistant ki tarah use kare.

---

# 0. Sabse pehle: hamara learning contract

Course ke Modules 1–13 ne tumhe testing foundations, Agile/Scrum, test strategy, AI tooling, MCP, authenticated testing, local LLMs aur CI/CD ka exposure diya. Ab hum course consumption mode se engineering practice mode mein enter kar rahe hain.

Ab se hum kisi feature ko tab tak complete nahi maanenge jab tak tum:
1. Uska purpose explain na kar sako.
2. Khud code likh/modify na kar sako.
3. Failure intentionally reproduce na kar sako.
4. Debugger/logs/trace se evidence collect na kar sako.
5. Root cause aur symptom ka difference na bata sako.
6. Fix ke baad regression verify na kar sako.
7. AI ke bina basic investigation na kar sako.
8. AI use karne par uske output ko independently validate na kar sako.

## 0.1 Manual-first, AI-second rule

**Stage A — Manual engineering:** Pehle tum khud problem ko samajhna aur debug karna seekhoge.

**Stage B — AI-assisted engineering:** Uske baad AI ko use karoge, lekin:
- AI ko complete project context doge.
- AI se pehle diagnosis aur evidence maangoge, direct code rewrite nahi.
- Minimal patch prefer karoge.
- Tests run karoge.
- Diff inspect karoge.
- Side effects aur regression check karoge.
- Wrong suggestion ko reject karna seekhoge.

AI ka purpose tumhari engineering judgement replace karna nahi; repetitive work reduce karna aur investigation ko accelerate karna hai.

## 0.2 “100% working AI” ke baare mein honest expectation

Koi AI model, prompt, agent ya automation workflow 100% correct output guarantee nahi karta. AI:
- Context miss kar sakta hai.
- Wrong root cause infer kar sakta hai.
- Outdated API suggest kar sakta hai.
- Existing test intent ko weaken kar sakta hai.
- Tests pass karwane ke liye assertion hata sakta hai.
- Flaky test ko retry se hide kar sakta hai.
- Secrets ya sensitive data expose karne ka risk create kar sakta hai.

Hamari definition of effective AI:

**Useful AI result = grounded context + specific task + evidence + minimal change + independent execution + review.**

Agar AI ne 10 minute mein code generate kiya, lekin usko verify karne mein 2 ghante lag gaye aur result unreliable hai, toh woh time-saving workflow nahi hai.

---

# 1. End goal: tum kya independently kar paoge?

Roadmap complete karne ke baad target capabilities:

## Python debugging
- Python traceback read karna.
- Exception ka exact origin locate karna.
- VS Code/Python debugger use karna.
- Breakpoints, conditional breakpoints, step over/into/out, watch, call stack.
- Variables, object state, scope, references aur mutation inspect karna.
- `pdb` / `breakpoint()` use karna.
- Logging levels, structured logs aur exception logging.
- Async code, API requests, file/config/import issues debug karna.
- Reproducible minimal example banana.

## Pytest debugging
- Test discovery aur collection failures debug karna.
- Fixture setup/teardown failures samajhna.
- Fixture scope, dependency graph aur parametrization inspect karna.
- `pytest -vv -s -x --lf --tb=long` jaise options ka correct use.
- `--setup-show`, `--collect-only`, `--fixtures`, `--markers` use karna.
- Assertion introspection aur custom assertion messages.
- Mock/patch failures, incorrect patch target, call assertions.
- Test isolation, shared state, order dependency aur flaky tests diagnose karna.
- Parallel execution failures aur worker-specific issues investigate karna.

## Playwright debugging
- Locator resolution, strict mode, timeout aur actionability errors debug karna.
- Auto-waiting ka actual behaviour samajhna.
- DOM, accessibility tree, locator count aur element state inspect karna.
- Browser DevTools Console, Network, Application/Storage, Elements use karna.
- Playwright Inspector, debug mode, trace viewer, screenshots, video, console/page errors.
- Frames, popups, downloads, uploads, dialogs aur authentication debug karna.
- API request failures aur UI/API state mismatch investigate karna.
- Test data, environment, browser version, viewport aur timing issues isolate karna.
- Flaky test ka root cause fix karna—blind retries nahi.

## AI-assisted engineering
- AI se logs explain, test review, test generation aur refactoring karwana.
- AI ko evidence-based debugging prompt dena.
- AI output ke claims verify karna.
- AI se minimal patch aur regression tests mangna.
- AI-generated tests ki quality judge karna.
- AI agents, CLI, MCP aur IDE workflows ka appropriate use select karna.
- Sensitive data, credentials, permissions aur generated code ke risks control karna.
- Measure karna ki AI ne actual time save kiya ya extra rework create kiya.

---

# 2. Learning structure and rules

## 2.1 Two-stage learning model

| Stage | Focus | AI usage |
|---|---|---|
| Stage 1 | Manual debugging mastery | AI debugging solution nahi dega; docs/notes allowed after attempt |
| Stage 2 | AI-assisted engineering | AI use allowed, but diagnosis and changes verified |

**Manual-first ka matlab AI ko forever ban karna nahi.** Pehle tum apne dimaag se investigation karoge. Phir same problem AI ke saath solve karke compare karoge.

## 2.2 Har lesson ka fixed format

Har topic hum is sequence mein padhenge:

1. WHY — production mein ye skill kyun chahiye?
2. WHAT — concept and terminology.
3. HOW — actual workflow.
4. Tool demonstration — VS Code / terminal / browser / Pytest / Playwright.
5. Small code example.
6. Line-by-line explanation.
7. Real-world bug scenario.
8. Intentional failure — hum bug create karenge.
9. Debugging investigation — evidence collect karenge.
10. Root cause — prove karenge.
11. Fix — smallest safe change.
12. Regression test — ensure old behaviour remains correct.
13. Common mistakes.
14. Interview answer — simple English + stronger answer + keywords.
15. Homework and review rubric.

## 2.3 Topic difficulty and time

Har lesson par:
- Difficulty: Easy / Medium / Hard.
- Estimated focused time.
- Prerequisites.
- Completion criteria.
- Practical assignment.

Time estimates learning estimates hain, deadline guarantee nahi.

## 2.4 Definition of Done

Koi topic tab complete hoga jab tum:
- Concept ko apne words mein explain kar sako.
- Code/tool khud use kar sako.
- Ek intentional failure debug kar sako.
- Evidence ke saath root cause bata sako.
- Fix aur regression test dikha sako.
- Interview mein answer de sako.

---

# 3. Stage 1 — Manual Debugging Mastery (AI solution ke bina)

# Phase 1 — Python Debugging Foundation

## 1. Python traceback ko read karna

**Difficulty:** Easy–Medium  
**Estimated time:** 2–3 hours

### WHY
Debugging ka first step error ko samajhna hai, error se darna nahi. Traceback tumhe batata hai:
- Kaunsi exception raise hui.
- Kis file/line par hui.
- Call chain mein kaunse functions execute hue.
- Failure ka final location kya hai.

### WHAT
Exception traceback ek call stack report hai. Last lines often exception type/message show karti hain, aur stack frames batate hain code kaise us point tak pahucha.

### HOW
1. Exception type identify karo.
2. Error message padho.
3. Apne code ka first relevant frame locate karo.
4. Us line ke input values inspect karo.
5. Caller function tak trace karo.
6. Determine karo incorrect value kahan introduce hui.

### Practice errors
- `NameError`
- `TypeError`
- `ValueError`
- `KeyError`
- `IndexError`
- `AttributeError`
- `ImportError` / `ModuleNotFoundError`
- `FileNotFoundError`
- `AssertionError`
- `TimeoutError`

Example:

```python
def calculate_total(price, quantity):
    return price * quantity

def create_order():
    price = "100"
    quantity = 2
    return calculate_total(price, quantity)

print(create_order())
```

Is code mein Python string repetition karega, numeric multiplication nahi. Debugging question: function ko kis type ka input milna chahiye tha? Validation kis layer par honi chahiye?

### Completion test
Traceback dekhkar exception type, failing line, incorrect value aur likely source identify kar pao.

## 2. VS Code Python debugger

**Difficulty:** Medium  
**Estimated time:** 3–4 hours

### Core controls
- Breakpoint: execution ko selected line par pause karna.
- Continue: next breakpoint tak run.
- Step Over: current line execute karke next line par jaana; function ke andar enter nahi karna.
- Step Into: called function ke andar jaana.
- Step Out: current function complete karke caller par return.
- Restart: debugging session restart.
- Stop: session terminate.
- Variables panel: current local/global values inspect.
- Watch: selected expression monitor.
- Call Stack: function call sequence inspect.
- Debug Console: paused execution context mein expressions evaluate.

### Practice scenario
Ek function unexpected `None` return kar raha hai:
1. Function call par breakpoint lagao.
2. Input inspect karo.
3. Step Into.
4. Branch conditions inspect karo.
5. Return statement tak jao.
6. Caller mein returned value inspect karo.

### Conditional breakpoint
Breakpoint ko condition ke saath trigger karna, e.g. `order_id == 105`.

Large loop mein har iteration pause karne ke bajay specific record par pause karna useful hai.

### Logpoint
Execution pause kiye bina diagnostic message output karna. Temporary debugging ke liye useful; production logs ka replacement nahi.

## 3. `pdb` and `breakpoint()`

**Difficulty:** Medium  
**Estimated time:** 2 hours

```python
def apply_discount(amount, discount):
    breakpoint()
    final_amount = amount - (amount * discount / 100)
    return final_amount
```

Useful PDB commands:
- `n` — next line.
- `s` — step into.
- `c` — continue.
- `l` — list source.
- `p expression` — print expression.
- `pp expression` — pretty-print.
- `w` — stack.
- `u` / `d` — move up/down stack.
- `q` — quit debugger.

Practice:
- Breakpoint inside function.
- Inspect parameters.
- Move through call stack.
- Inspect returned values.
- Remove debugger before committing.

## 4. Variables, scope, references and mutation

**Difficulty:** Medium  
**Estimated time:** 2–3 hours

Debugging mein sirf value nahi, object identity aur mutation bhi important hai.

Topics:
- Local vs global scope.
- Mutable vs immutable objects.
- List/dict shared references.
- Shallow vs deep copy.
- Default mutable argument bug.
- Closure-captured values.
- Class instance state.

Example:

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("A"))
print(add_item("B"))
```

Investigate why second call contains first call's value.

Safe alternative:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## 5. Python logging for debugging

**Difficulty:** Medium  
**Estimated time:** 2–3 hours

### WHY
`print()` quick experiment ke liye useful hai, lekin maintainable application/test suite mein structured logging better hai.

### Levels
- DEBUG — detailed diagnostic information.
- INFO — normal execution milestones.
- WARNING — unexpected but recoverable situation.
- ERROR — operation failed.
- CRITICAL — severe failure.

Example:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

logger = logging.getLogger(__name__)

def fetch_order(order_id):
    logger.info("Fetching order_id=%s", order_id)
    try:
        # API/database operation
        return {"id": order_id}
    except Exception:
        logger.exception("Failed to fetch order_id=%s", order_id)
        raise
```

Rules:
- `logger.exception()` exception traceback include karta hai; exception handler ke andar use karo.
- Password, access token, cookies, PII log mat karo.
- Log message mein useful identifiers rakho, secrets nahi.
- Bare `except: pass` debugging ko destroy karta hai.

## 6. Python async and API debugging

**Difficulty:** Hard  
**Estimated time:** 3–4 hours

Topics:
- Sync vs async call.
- `await` missing.
- Coroutine created but never awaited.
- Exception propagation.
- Timeout.
- Connection refused.
- DNS failure.
- TLS/certificate issue.
- Response status vs transport error.
- JSON parsing error.
- Request payload and headers.

Practice with `requests` and `httpx` (if used):
- Request URL.
- Method.
- Safe headers.
- Status code.
- Response time.
- Response body.
- Correlation/request ID.

Never log authorization headers or full secrets.

---

# Phase 2 — Pytest Debugging Mastery

## 7. Pytest execution and discovery

**Difficulty:** Easy–Medium  
**Estimated time:** 2 hours

Commands to understand and practice:

```bash
pytest
pytest -v
pytest -vv
pytest -q
pytest -s
pytest -x
pytest --maxfail=1
pytest --lf
pytest --ff
pytest --collect-only
pytest --tb=short
pytest --tb=long
pytest --tb=no
```

Meaning:
- `-v` / `-vv`: verbose test output.
- `-s`: capture disable; print output visible.
- `-x`: first failure ke baad stop.
- `--maxfail=1`: one failure ke baad stop.
- `--lf`: last-failed tests run.
- `--ff`: last-failed tests first.
- `--collect-only`: tests collect karo, execute mat karo.
- `--tb`: traceback format.

Practice:
- Wrong test filename.
- Wrong function prefix.
- Missing test function.
- Syntax error during collection.
- Import error in `conftest.py`.
- Incorrect pytest root/configuration.

## 8. Fixture debugging

**Difficulty:** Medium–Hard  
**Estimated time:** 4–5 hours

You have already studied fixtures; now debug their behaviour deeply.

Investigate:
- Fixture not found.
- Wrong fixture name.
- Fixture dependency chain.
- Scope mismatch.
- Setup failure.
- Teardown failure.
- `yield` placement.
- Autouse fixture side effects.
- Shared mutable state.
- Parametrized fixture value.
- `request.param`.
- Fixture finalizer.
- Fixture execution order.

Useful commands:

```bash
pytest --setup-show -v
pytest --fixtures
pytest --fixtures-per-test
```

Practice:
1. Create function-scoped fixture.
2. Convert to module scope.
3. Observe setup/teardown.
4. Introduce scope mismatch.
5. Debug it.
6. Introduce shared list mutation.
7. Prove test-order dependency.
8. Fix with isolated test data.

## 9. Assertion and test failure analysis

**Difficulty:** Medium  
**Estimated time:** 2–3 hours

Topics:
- Expected vs actual.
- Assertion introspection.
- Custom assertion message.
- Floating-point comparison.
- String whitespace/case mismatch.
- List order vs set equality.
- Date/time and timezone mismatch.
- Decimal vs float.
- `None` vs missing field.
- API response schema mismatch.

Rule: Assertion ko weak mat karo sirf test pass karne ke liye. Business requirement confirm karo, then expected result fix karo.

## 10. Mocking and patch debugging

**Difficulty:** Hard  
**Estimated time:** 3–4 hours

Topics:
- `Mock`, `MagicMock`.
- `return_value`.
- `side_effect`.
- `patch`.
- `patch.object`.
- Patch where dependency is looked up, not necessarily where defined.
- Call count/args assertions.
- Mock too much vs integration test.
- Leaked mock state.
- Incorrect mock return type.

Practice:
- API call mocked in wrong module.
- Mock returns dict but code expects response object.
- `side_effect` exception.
- Expected call mismatch.
- Test passes with mock but real integration fails.

## 11. Isolation, order dependency and flaky tests

**Difficulty:** Hard  
**Estimated time:** 4 hours

Investigate:
- Global mutable state.
- Shared test data.
- Fixed usernames/emails.
- Database leftovers.
- Test order dependency.
- Time-based assumptions.
- Random data without seed/recording.
- Parallel worker collisions.
- External service instability.

Repeat a suspicious test:
```bash
pytest path/to/test_file.py::test_name -v --count=10
```

`pytest-repeat` plugin is required for `--count`; it is not built into pytest.

Do not automatically add retries as the first fix. Repetition helps reveal flakiness; root cause still needs investigation.

---

# Phase 3 — Playwright Debugging Mastery (manual)

## 12. Playwright error taxonomy

**Difficulty:** Medium  
**Estimated time:** 3 hours

Learn to classify failure before changing code.

| Error family | What it usually means | First investigation |
|---|---|---|
| Locator timeout | Target did not reach expected condition | Locator, DOM, visibility, state |
| Strict mode violation | Locator matched multiple elements | Scope/refine locator |
| Element not visible | Hidden/covered/wrong state | DOM/CSS/layout |
| Not enabled | Control disabled | Business/UI state |
| Not stable | Element moving/animating | Animation/layout |
| Detached from DOM | Element rerendered/replaced | Re-render timing and locator strategy |
| Navigation timeout | Navigation did not complete as expected | URL, network, app response |
| Browser closed | Context/browser lifecycle issue | Fixture teardown/crash |
| Target closed | Page/context closed before operation | Popup/page lifecycle |
| Frame not found | Wrong frame locator/iframe lifecycle | DOM and frame tree |
| Download timeout | Download did not start | Trigger, event wait, app response |

Do not assume every timeout means “increase timeout”. Timeout is often a symptom, not root cause.

## 13. Locator debugging

**Difficulty:** Medium  
**Estimated time:** 4 hours

Tools and methods:
- `locator.count()`
- `locator.first`
- `locator.last`
- `locator.nth()` only when index is meaningful/stable.
- `locator.is_visible()`
- `locator.is_enabled()`
- `locator.is_checked()`
- `locator.get_attribute()`
- `locator.text_content()`
- `locator.inner_text()`
- `locator.input_value()`
- `locator.evaluate()` for targeted DOM inspection.
- `page.locator("body").inner_text()` for quick page text inspection.
- `page.url`
- `page.title()`

Preferred locator hierarchy:
1. `get_by_role()` with accessible name.
2. `get_by_label()`.
3. `get_by_placeholder()`.
4. `get_by_text()` where text is stable and meaningful.
5. `get_by_test_id()` when application exposes stable test IDs.
6. CSS locator when needed.
7. XPath only when there is a clear reason.

Example:

```python
button = page.get_by_role("button", name="Place order")
print("matches:", button.count())
print("visible:", button.is_visible())
print("enabled:", button.is_enabled())
```

Remember:
- `count()` immediate snapshot deta hai; it is not an auto-wait assertion.
- `is_visible()` immediate state check hai.
- For test assertions, prefer Playwright `expect()` assertions that auto-wait.

## 14. Playwright Inspector and debug mode

**Difficulty:** Medium  
**Estimated time:** 2 hours

Python CLI examples (verify command syntax against installed Playwright version):

```bash
PWDEBUG=1 pytest -s
```

On Windows PowerShell:

```powershell
$env:PWDEBUG="1"
pytest -s
```

Use Inspector to:
- Pause and resume execution.
- Step through actions.
- Inspect locator behaviour.
- Use locator picker where available.
- Understand which action is waiting.

Also learn:
- `page.pause()` for temporary interactive debugging.
- Remove debug pauses before CI/commit.
- Avoid leaving debug mode enabled in shared environments.

## 15. Playwright Trace Viewer

**Difficulty:** Medium–Hard  
**Estimated time:** 3 hours

Trace can provide:
- Action timeline.
- Locator/action details.
- DOM snapshots.
- Screenshots.
- Network activity.
- Console/log information, depending on trace configuration.

Pytest Playwright configuration commonly supports tracing through plugin options/fixtures; exact config depends on installed plugin/version.

Example command often used with pytest-playwright:

```bash
pytest --tracing=retain-on-failure
```

Check the installed plugin's current help (`pytest --help`) because supported options may differ by version.

Trace debugging workflow:
1. Reproduce failure.
2. Preserve trace on failure.
3. Open trace viewer.
4. Locate failed action.
5. Inspect before/after DOM snapshot.
6. Check action wait reason.
7. Inspect network/console evidence.
8. Identify root cause.
9. Fix and rerun.

Trace may contain sensitive application data. Do not upload/share traces publicly without review.

## 16. Screenshots, video and browser lifecycle

**Difficulty:** Medium  
**Estimated time:** 2–3 hours

Learn:
- Screenshot at failure.
- Full-page screenshot.
- Video recording configuration.
- Browser context lifecycle.
- Page lifecycle.
- Test teardown.
- Context isolation.
- Browser crash vs page close.
- Artifact naming and retention.

Pytest plugin options vary; inspect `pytest --help` and installed package documentation.

## 17. Browser DevTools debugging

**Difficulty:** Medium–Hard  
**Estimated time:** 4 hours

### Elements panel
- DOM structure.
- Attributes.
- CSS rules.
- Computed styles.
- Visibility/layout.
- Overlay and z-index.
- Event listeners where useful.

### Console
- JavaScript exceptions.
- Failed resource messages.
- CORS errors.
- Unhandled promise rejections.
- Application logs.

### Network
- Request URL/method.
- Status code.
- Request headers.
- Request payload.
- Response headers/body.
- Timing.
- Initiator.
- Redirects.
- Failed requests.

### Application/Storage
- Cookies.
- Local Storage.
- Session Storage.
- IndexedDB.
- Service worker state.

Practice:
1. Login button click.
2. Observe request.
3. Verify payload.
4. Verify response.
5. Inspect token/cookie storage.
6. Reload page.
7. Verify session persistence.
8. Logout and confirm session removal.

## 18. Playwright event and browser error monitoring

**Difficulty:** Hard  
**Estimated time:** 3 hours

Learn to capture:
- Console messages.
- Page errors.
- Failed requests.
- Request failures vs HTTP error responses.
- Responses with 4xx/5xx.
- Page crash.
- Dialog events.
- Popup events.
- Download events.

Conceptual Python example:

```python
page.on("console", lambda message: print("CONSOLE:", message.type, message.text))
page.on("pageerror", lambda error: print("PAGE ERROR:", error))
page.on("requestfailed", lambda request: print(
    "REQUEST FAILED:", request.method, request.url, request.failure
))
```

Be careful:
- A request returning HTTP 404/500 is not necessarily a `requestfailed` event; transport failure and HTTP error response are different.
- Event listeners can produce noisy output; filter relevant requests.
- Do not print secrets from headers or payloads.

## 19. API + UI combined debugging

**Difficulty:** Hard  
**Estimated time:** 4 hours

Scenario: UI says “Order placed” but order is absent in order history.

Investigate layers in order:
1. UI click/action.
2. Request sent?
3. Correct URL/method?
4. Payload correct?
5. Response status/body?
6. Backend persisted record?
7. Database state?
8. UI refreshed/refetched?
9. Cache/stale response?
10. Test assertion correct?

Learn difference:
- API transport failure.
- HTTP error.
- Business validation error.
- Database persistence failure.
- Frontend state update failure.
- Eventual consistency delay.
- Test data collision.

## 20. Authentication, storage state and session debugging

**Difficulty:** Hard  
**Estimated time:** 3–4 hours

Investigate:
- Cookie vs localStorage vs sessionStorage.
- Token missing/expired.
- Wrong role/permissions.
- 401 vs 403.
- Storage state generated before login completes.
- Context uses wrong storage state.
- Test uses stale auth state.
- Logout invalidation.
- CSRF and same-site cookie considerations.

Security:
- Never commit `.auth` state or tokens.
- Keep auth files in `.gitignore`.
- Treat traces/screenshots as potentially sensitive.
- Use test accounts and least privilege.

## 21. Frames, popups, dialogs, upload/download

**Difficulty:** Hard  
**Estimated time:** 4 hours

Practice debugging:
- Wrong iframe selector.
- Nested iframe.
- Frame navigation/reload.
- Popup opened in a new page.
- Alert/confirm/prompt handler timing.
- Download event listener timing.
- File path wrong.
- Upload input not available.
- File chooser event vs input element.

For each:
1. Reproduce.
2. Inspect browser event/page/frame.
3. Verify event subscription timing.
4. Check file path/permissions.
5. Confirm final application state.

## 22. Flaky Playwright tests: root-cause engineering

**Difficulty:** Hard  
**Estimated time:** 5–6 hours

Flakiness categories:
- Timing/race condition.
- Weak locator.
- Animation/layout instability.
- Network dependency.
- Shared test data.
- Test order dependency.
- Browser/environment difference.
- App defect.
- Third-party service.
- Timezone/locale.
- Parallel execution conflict.
- Incomplete cleanup.

Investigation:
1. Run once and capture evidence.
2. Repeat same test.
3. Run in isolation.
4. Run full suite.
5. Run headed/headless where relevant.
6. Compare trace and logs.
7. Inspect data setup and cleanup.
8. Identify nondeterministic dependency.
9. Fix cause.
10. Repeat multiple times and in CI.

Bad fixes:
- Add arbitrary `time.sleep()`.
- Increase all timeouts.
- Use `force=True` without understanding actionability.
- Add retries and declare fixed.
- Remove assertion.
- Use `nth()` to hide ambiguous locator.
- Skip failing test indefinitely.

---

# Phase 4 — End-to-end debugging workflow

## 23. The 12-step debugging protocol

Every failure par same disciplined method follow karo.

### Step 1 — State the symptom
Example: “Checkout test times out while clicking Place order.”

### Step 2 — Preserve evidence
- Full traceback.
- Failed test name.
- Browser/OS/version.
- Screenshot/trace.
- Relevant console/network logs.
- Test data and environment.

### Step 3 — Reproduce
- Same test.
- Same environment.
- Same data if possible.

### Step 4 — Reduce noise
- Run single test.
- Disable unrelated parallelism if needed.
- Remove unrelated setup only if safe.

### Step 5 — Classify the layer
- Test code?
- Python?
- Pytest fixture?
- Playwright locator/action?
- Browser?
- Frontend?
- API?
- Backend/database?
- Environment/CI?

### Step 6 — Form a hypothesis
Example: “The button is disabled because payment validation has not completed.”

### Step 7 — Gather evidence
Do not change code yet. Inspect actual state.

### Step 8 — Prove/disprove hypothesis
Check DOM, state, request, response, fixture, logs.

### Step 9 — Find root cause
Explain why the failure happens, not just where it appears.

### Step 10 — Apply smallest safe fix
Avoid unrelated refactors during debugging.

### Step 11 — Verify
- Re-run failing test.
- Run related tests.
- Run relevant suite.
- Check no assertion was weakened.

### Step 12 — Record learning
Write:
- Symptom.
- Root cause.
- Evidence.
- Fix.
- Regression test.
- Prevention.

## 23.1 Debugging journal template

```markdown
# Debugging Record

## Context
- Project:
- Environment:
- Browser:
- Python:
- Playwright:
- Pytest:

## Symptom
What failed?

## Reproduction
Exact command and steps:

## Evidence
- Traceback:
- Screenshot/trace:
- Console:
- Network:
- Test data:

## Hypotheses
1.
2.
3.

## Root cause
What actually caused the issue?

## Fix
Smallest safe change:

## Verification
- Failing test:
- Related tests:
- Full suite:
- CI:

## Prevention
What should change to prevent recurrence?
```

---

# 4. Stage 2 — AI-Assisted QA Engineering

Manual debugging foundation ke baad hi ye stage start karna hai.

# Phase 5 — AI ko engineering workflow mein use karna

## 24. AI usage maturity ladder

| Level | Usage | Risk |
|---|---|---|
| 0 | AI not used | Manual effort higher |
| 1 | Error explanation | Low, if evidence reviewed |
| 2 | Hypothesis generation | Medium |
| 3 | Test/code review | Medium |
| 4 | Minimal patch proposal | Medium–High |
| 5 | Test generation/refactoring | High without review |
| 6 | Agent edits/runs multiple files | High; needs controls |
| 7 | Autonomous CI/PR workflow | Very high; strict permissions and review |

Goal: Level 4–6 responsibly use karna. Level 7 ko carefully controlled workflow ke bina adopt nahi karna.

## 25. The evidence-first AI debugging workflow

**Never start with:** “Fix my code.”

Use this sequence:

1. Give exact task and expected behaviour.
2. Give actual behaviour.
3. Give smallest relevant code.
4. Give exact command.
5. Give full relevant error/log.
6. Give environment/version.
7. Ask AI to summarize facts only.
8. Ask it to list hypotheses with confidence and evidence needed.
9. Verify evidence manually.
10. Ask for minimal patch only after root cause is supported.
11. Ask for regression test.
12. Review diff.
13. Run tests.
14. Ask AI to review test output, not to claim success.
15. Independently verify final behaviour.

## 26. Master prompt — debugging diagnosis (no code changes)

```text
Act as a senior Python, Pytest and Playwright debugging engineer.

IMPORTANT:
Do not edit files.
Do not suggest a code rewrite yet.
Do not guess beyond the evidence.

Context:
- Project:
- Expected behaviour:
- Actual behaviour:
- Exact command:
- Python version:
- Pytest version:
- Playwright version:
- OS/browser:
- Relevant code:
- Full error/log:

Tasks:
1. Restate the failure in one sentence.
2. Separate confirmed facts from assumptions.
3. Identify the first meaningful failure, not just cascading errors.
4. Classify the likely failing layer.
5. Give up to 3 hypotheses, ranked by likelihood.
6. For each hypothesis, state evidence supporting it and evidence still missing.
7. Tell me the smallest manual check to confirm or reject each hypothesis.
8. Do not recommend sleep(), arbitrary timeout increases, force=True, retries, skipping tests or weakening assertions without evidence.
9. If version-specific behaviour matters, say so and request current official documentation/version details.
10. Stop after diagnosis. Wait for my evidence before proposing a fix.
```

## 27. Master prompt — minimal safe fix

Use only after root cause is established.

```text
The root cause has been verified:

[ROOT CAUSE + EVIDENCE]

Propose the smallest safe fix.

Requirements:
1. Preserve the original business requirement.
2. Do not delete or weaken assertions.
3. Do not skip tests or add retries as a substitute for fixing the cause.
4. Do not introduce arbitrary sleeps.
5. Avoid unrelated refactoring.
6. Explain every changed line.
7. Add or update a regression test.
8. List possible side effects.
9. Show the expected diff before applying it.
10. If any required context is missing, ask instead of inventing it.
```

## 28. Master prompt — AI-generated test review

```text
Review these Python/Pytest/Playwright tests as a strict senior SDET.

Review:
- Does each test verify a meaningful requirement?
- Are assertions strong enough?
- Can the test pass when the feature is broken?
- Are locators stable and accessible?
- Are fixtures scoped correctly?
- Is test data isolated?
- Is cleanup reliable?
- Are waits based on observable conditions?
- Are exceptions swallowed?
- Are retries/sleeps/force clicks hiding problems?
- Can tests run independently and in parallel?
- Is sensitive data exposed?
- Are failure diagnostics useful?

For every finding:
- Severity: Critical / High / Medium / Low.
- File and line.
- Evidence.
- Why it matters.
- Suggested minimal change.
- Regression test.

Do not rewrite the whole test suite. Review first and wait for approval.
```

## 29. Master prompt — Playwright locator investigation

```text
Investigate this Playwright locator failure.

Do not replace the locator immediately.

Expected target:
[EXPECTED ELEMENT]

Current locator:
[LOCATOR]

Error:
[ERROR]

DOM/accessibility evidence:
[SNIPPET OR TRACE DETAILS]

Please:
1. Explain what the locator matches and why.
2. Identify whether the issue is zero matches, multiple matches, hidden state, disabled state, detachment or timing.
3. Suggest inspection commands I can run.
4. Rank locator options by semantic stability.
5. Prefer role/label/test-id where appropriate.
6. Explain why each proposed locator is stable or fragile.
7. Do not suggest nth() unless index is a meaningful part of the requirement.
8. Do not use force=True to bypass an unexplained failure.
```

## 30. Master prompt — CI failure diagnosis

```text
Act as a senior CI/CD and test automation engineer.

Analyze the workflow and failed GitHub Actions logs.

Do not edit files yet.

Check:
- Trigger and branch filters.
- Runner OS.
- Runtime setup.
- Dependency lockfile/install.
- Python/Node version.
- Playwright version.
- Browser binaries vs configured projects.
- Environment variables/secrets.
- Test command.
- Report/trace artifact paths.
- Permissions.
- Cache keys and invalidation.
- First meaningful error vs cascading errors.

For each finding, classify:
- Confirmed issue
- Likely issue
- Improvement suggestion

Cite the exact log/YAML evidence.
Do not remove tests or reduce browser coverage just to get a green build.
Do not invent current action versions. Ask for official docs or verify current official references.
```

## 31. AI tools ka role — tool-first, hype nahi

Different tools different jobs ke liye useful hain:

| Tool category | Best use | Caution |
|---|---|---|
| IDE assistant | Explain code, small edits, review | Review every diff |
| Chat assistant | Reasoning, learning, debugging hypotheses | It may lack repository context |
| CLI coding agent | Multi-file changes, running commands | Scope permissions and inspect commands |
| Browser agent | Inspect UI and reproduce workflows | Verify actions and environment |
| Playwright MCP | Browser interaction/inspection through tools | Tool actions are not a replacement for assertions |
| Chrome DevTools MCP | Network/console/browser evidence | Review data exposure |
| Local LLM | Private/local experimentation, offline tasks | Model capability and hardware vary |
| GitHub Copilot / Claude Code etc. | Repository-aware workflows depending on setup | Product features/pricing/availability change |

**Selection rule:** Simple question ke liye full agent launch mat karo. Small task = small tool. Multi-file investigation = agent only when context and permissions are controlled.

## 32. AI ko project context kaise dena hai?

Create and maintain project guidance files such as:
- `README.md` — setup and commands.
- `CONTRIBUTING.md` — coding/test conventions.
- `AGENTS.md` or tool-specific project instructions — project rules, if supported by your tool.
- `pytest.ini` / `pyproject.toml` — test configuration.
- `requirements.txt` or lockfile — dependencies.
- `docs/test-strategy.md` — test scope and risk.
- `docs/debugging-playbook.md` — common investigation steps.

Guidance file mein:
- Project structure.
- How to run tests.
- Naming conventions.
- Fixture policy.
- Locator policy.
- Test data strategy.
- Reporting/trace setup.
- Security rules.
- Definition of Done.

Do not place passwords, tokens, private URLs or production data in guidance files.

## 33. AI context packet — reusable template

```markdown
# Project Context

## Purpose
What application does this project test?

## Stack
- Python:
- Pytest:
- Playwright:
- Browser:
- OS:
- CI:

## Structure
Relevant folders/files:

## How to run
Exact setup and test commands:

## Test architecture
Fixtures, POM, API helpers, auth setup:

## Conventions
Locator strategy, assertions, test naming:

## Current task
What needs to be investigated?

## Expected behaviour

## Actual behaviour

## Evidence
Logs, trace, screenshot, network details:

## Constraints
Files not to change, security rules, required browser coverage:
```

## 34. AI time-saving measurement

AI use ko feelings se judge mat karo. Measure karo.

Track:
- Manual investigation time.
- AI-assisted investigation time.
- Number of AI suggestions rejected.
- Number of regressions introduced.
- Rework time.
- Tests generated vs tests accepted.
- Defects found by generated tests.
- False positives/false negatives.
- Final verification time.

Example:

| Metric | Manual baseline | AI-assisted |
|---|---:|---:|
| Investigation | 35 min | 18 min |
| Fix/review | 20 min | 25 min |
| Rework | 5 min | 2 min |
| Total | 60 min | 45 min |

This is only an illustrative example. AI saves time only if total verified effort decreases without quality loss.

---

# 5. Stage 3 — Advanced debugging and engineering quality

## 35. Test observability

**Difficulty:** Hard

A production-grade test should tell the team:
- What failed?
- Where?
- Under what data?
- In which browser/environment?
- What was the last successful action?
- What request failed?
- What did the page look like?
- Can failure be reproduced?

Build useful diagnostics:
- Test name and parameters.
- Correlation ID / test run ID.
- Safe request/response metadata.
- Screenshot and trace on failure.
- Browser/OS/version.
- Application build/version.
- Environment and test data ID.

Never include secrets, session tokens, passwords or unnecessary personal data.

## 36. Test architecture debugging

Topics:
- Page Object Model boundaries.
- Business action vs assertion responsibility.
- Fixtures vs page objects.
- API helper design.
- Test data factories.
- Environment configuration.
- Auth state lifecycle.
- Shared utilities.
- Dependency injection patterns.
- Avoiding giant base classes.
- Avoiding hidden test side effects.

Practice:
- Debug a POM method returning wrong page/context.
- Debug stale page reference.
- Debug fixture that creates a new context unexpectedly.
- Debug helper that swallows assertion errors.

## 37. Parallel execution and resource contention

Topics:
- Pytest-xdist worker model.
- Per-worker test data.
- Shared account collision.
- Database cleanup.
- File path collisions.
- Port conflicts.
- Rate limits.
- Browser resource limits.
- Test ordering.
- Worker-specific logs.

Do not enable parallel execution before tests are isolated and deterministic.

## 38. CI pipeline quality gates

Topics:
- Smoke vs regression.
- Pull request checks.
- Nightly full suite.
- Browser matrix.
- Sharding.
- Retry policy with reporting.
- Artifact retention.
- Test duration budget.
- Flaky test quarantine policy.
- Required checks and branch protection.
- Secret handling and least privilege.

A green pipeline is meaningful only when required tests actually ran.

## 39. Security-aware debugging

Never:
- Paste real secrets into public AI tools.
- Upload production customer data unnecessarily.
- Commit `.auth` state.
- Share traces without inspecting them.
- Give an agent unrestricted shell/repository permissions without need.
- Run unknown scripts/actions without review.
- Let AI silently change permissions or deployment configuration.

Use:
- Synthetic test data.
- Least privilege.
- Secret manager / GitHub Secrets.
- Redacted logs.
- `.gitignore`.
- Reviewed tool permissions.
- Protected branches and human review.

---

# 6. Step-by-step training schedule

This is a **topic-based plan**, not a rigid calendar. We will not jump ahead just because a day number has arrived.

## Stage 1 — Manual debugging

| Session | Topic | Difficulty | Estimated time | Practical outcome |
|---:|---|---|---:|---|
| 1 | Traceback reading and exception taxonomy | Easy–Medium | 2–3h | Diagnose Python exceptions |
| 2 | VS Code debugger controls | Medium | 3–4h | Debug function line by line |
| 3 | Breakpoints, conditional breakpoints, watch, call stack | Medium | 2–3h | Inspect runtime state |
| 4 | `pdb`, `breakpoint()` | Medium | 2h | Debug without IDE |
| 5 | Scope, references, mutation, copies | Medium | 2–3h | Find state bugs |
| 6 | Logging and exception logging | Medium | 2–3h | Build useful diagnostic logs |
| 7 | Async/API/network Python debugging | Hard | 3–4h | Diagnose request failures |
| 8 | Pytest discovery and command-line debugging | Easy–Medium | 2h | Diagnose collection/execution |
| 9 | Fixture setup/teardown and scope | Medium–Hard | 4–5h | Diagnose fixture failures |
| 10 | Assertions and failure analysis | Medium | 2–3h | Improve test diagnostics |
| 11 | Mock/patch debugging | Hard | 3–4h | Diagnose isolated unit tests |
| 12 | Isolation, order dependence, flaky tests | Hard | 4h | Stabilize Pytest suite |
| 13 | Playwright error taxonomy | Medium | 3h | Classify browser failures |
| 14 | Locator debugging and DOM inspection | Medium | 4h | Fix locator issues correctly |
| 15 | Playwright Inspector/debug mode | Medium | 2h | Step through browser tests |
| 16 | Trace Viewer | Medium–Hard | 3h | Diagnose failed actions |
| 17 | Screenshots/video/lifecycle | Medium | 2–3h | Preserve useful evidence |
| 18 | Browser DevTools: Elements/Console | Medium | 2h | Inspect UI/client issues |
| 19 | Network and Storage panels | Hard | 3h | Debug API/auth issues |
| 20 | Playwright events and browser errors | Hard | 3h | Capture console/request failures |
| 21 | API + UI + DB investigation | Hard | 4h | Trace end-to-end failure |
| 22 | Auth/storage state debugging | Hard | 3–4h | Diagnose session failures |
| 23 | Frames/popups/dialogs/files | Hard | 4h | Debug advanced browser flows |
| 24 | Flaky test root-cause analysis | Hard | 5–6h | Fix nondeterminism |
| 25 | Full debugging protocol and capstone | Hard | 5–6h | Own a failure end to end |

## Stage 2 — AI-assisted workflow

| Session | Topic | Difficulty | Estimated time | Practical outcome |
|---:|---|---|---:|---|
| 26 | AI diagnosis without code edits | Medium | 2h | Evidence-based diagnosis |
| 27 | AI hypothesis ranking and verification | Medium | 2h | Reject weak hypotheses |
| 28 | AI minimal patch workflow | Hard | 3h | Reviewable fix |
| 29 | AI test/code review | Medium–Hard | 3h | Find test quality gaps |
| 30 | AI test generation and validation | Hard | 4h | Accept/reject generated tests |
| 31 | Repository context and instruction files | Medium | 2h | Better project-aware output |
| 32 | CLI coding agent safety and permissions | Hard | 3h | Controlled agent use |
| 33 | MCP/browser/DevTools agent workflow | Hard | 3–4h | Tool-assisted investigation |
| 34 | CI log diagnosis with AI | Medium–Hard | 3h | Faster pipeline debugging |
| 35 | AI hallucination/version verification | Medium | 2h | Verify claims against docs |
| 36 | AI efficiency measurement and capstone | Hard | 4–5h | Prove time saved without quality loss |

**Total:** 36 focused sessions. Actual duration depends on practice quality and how many topics need repetition.

---

# 7. Capstone projects

## Capstone A — Python debugging lab

Build a small Python order service with intentional defects:
- Wrong type.
- Missing key.
- Mutable default.
- Incorrect exception handling.
- Wrong API response handling.
- Logging that leaks sensitive data (identify and fix safely).

Deliver:
- Reproduction steps.
- Traceback analysis.
- Debugger screenshots/notes.
- Root cause.
- Fix.
- Regression tests.

## Capstone B — Pytest debugging lab

Build a test suite with:
- Fixture scope mismatch.
- Setup/teardown defect.
- Shared mutable fixture.
- Wrong patch target.
- Order dependency.
- Weak assertion.
- Test collection issue.

Deliver:
- Each failure classified.
- Evidence.
- Corrected test architecture.
- Full suite result.

## Capstone C — Playwright debugging lab

Use a demo application with:
- Login.
- Search.
- Product detail.
- Add to cart.
- Checkout.
- Order history.

Introduce defects:
- Duplicate button names.
- Hidden element.
- Disabled control.
- Delayed API.
- 401 response.
- Stale auth state.
- Broken iframe.
- Popup timing issue.
- Failed image/API request.
- Flaky animation.

Deliver:
- Locator investigation.
- Inspector/trace.
- DevTools Network/Console evidence.
- Root-cause record.
- Stable regression test.

## Capstone D — AI-assisted QA engineering

Use the same failures from A/B/C.

For every bug:
1. Solve manually first.
2. Record manual time and diagnosis.
3. Give AI only the evidence packet.
4. Compare AI hypotheses with your diagnosis.
5. Ask for minimal patch only after root cause is verified.
6. Review diff.
7. Run regression tests.
8. Record accepted/rejected AI suggestions.
9. Measure total time and quality.

**Success condition:** AI-assisted process reduces total verified effort or improves diagnostic quality without weakening tests, introducing security risk or increasing rework.

## Capstone E — Production-style CI

Create GitHub Actions pipeline for Python + Pytest + Playwright:
- Pull request trigger.
- Python setup.
- Reproducible dependencies.
- Browser installation.
- Smoke tests.
- Report/trace artifact.
- Safe secrets handling.
- Failure diagnostics.
- Optional browser matrix.
- Cache with correct invalidation.
- AI-assisted log diagnosis with human approval.

---

# 8. Practical debugging command reference

## Python

```bash
python --version
python -m pip --version
python -m pip show playwright
python -m pip show pytest
python -m pip freeze
```

## Pytest

```bash
pytest -v
pytest -vv -s
pytest --collect-only
pytest --setup-show -v
pytest --fixtures
pytest --fixtures-per-test
pytest -x
pytest --lf
pytest --ff
pytest --tb=long
pytest --durations=10
pytest -k "login"
pytest path/to/test_file.py::test_name -vv -s
```

## Playwright / environment

```bash
python -m playwright --version
python -m playwright install
python -m playwright install chromium
pytest --help
```

Check installed plugin help for tracing, video, screenshot and browser options; exact CLI switches depend on package/version.

## Git

```bash
git status
git diff
git diff --staged
git log --oneline -5
git show --stat
```

Before accepting AI edits, inspect `git diff`.

---

# 9. Debugging anti-patterns — never make these habits

| Anti-pattern | Why it is dangerous | Better approach |
|---|---|---|
| Immediately increase timeout | Hides slow/wrong state | Inspect what condition never became true |
| Add `time.sleep()` | Timing-dependent and slow | Wait for observable state |
| Use `force=True` quickly | Bypasses actionability checks | Find overlay/disabled/hidden cause |
| Add retries first | Hides flaky root cause | Reproduce and investigate nondeterminism |
| Remove assertion | Test becomes weaker | Confirm requirement and correct expected value |
| Skip failing test forever | Defect escapes coverage | Track owner/reason/expiry |
| Catch all exceptions and pass | Hides failures | Catch expected exceptions and log/re-raise |
| Ask AI “fix everything” | Large uncontrolled changes | Diagnose first, minimal patch |
| Accept all AI edits | Regression/security risk | Review diff and run tests |
| Trust green CI blindly | Tests may not have run | Check collected/executed test counts |
| Log secrets | Security incident | Redact sensitive values |
| Run agent with broad permissions | Unintended destructive actions | Least privilege and approval |

---

# 10. Personal progress tracker

Update this after each session. Status:
- `Not started`
- `Learning`
- `Practicing`
- `Needs revision`
- `Completed`

| Session | Topic | Status | Confidence (1–5) | Evidence / notes |
|---:|---|---|---:|---|
| 1 | Traceback and exceptions | Not started | — | |
| 2 | VS Code debugger | Not started | — | |
| 3 | Breakpoints and call stack | Not started | — | |
| 4 | pdb | Not started | — | |
| 5 | State and mutation | Not started | — | |
| 6 | Logging | Not started | — | |
| 7 | Async/API debugging | Not started | — | |
| 8 | Pytest discovery | Not started | — | |
| 9 | Fixture debugging | Not started | — | |
| 10 | Assertion debugging | Not started | — | |
| 11 | Mock/patch debugging | Not started | — | |
| 12 | Isolation/flakiness | Not started | — | |
| 13 | Playwright error taxonomy | Not started | — | |
| 14 | Locator debugging | Not started | — | |
| 15 | Inspector/debug mode | Not started | — | |
| 16 | Trace Viewer | Not started | — | |
| 17 | Screenshot/video/lifecycle | Not started | — | |
| 18 | DevTools Elements/Console | Not started | — | |
| 19 | DevTools Network/Storage | Not started | — | |
| 20 | Browser events | Not started | — | |
| 21 | API/UI/DB debugging | Not started | — | |
| 22 | Auth debugging | Not started | — | |
| 23 | Frames/popups/files | Not started | — | |
| 24 | Flaky tests | Not started | — | |
| 25 | Manual debugging capstone | Not started | — | |
| 26 | AI diagnosis | Not started | — | |
| 27 | AI hypotheses | Not started | — | |
| 28 | AI minimal patch | Not started | — | |
| 29 | AI review | Not started | — | |
| 30 | AI test generation | Not started | — | |
| 31 | Project context files | Not started | — | |
| 32 | CLI agent safety | Not started | — | |
| 33 | MCP/browser agents | Not started | — | |
| 34 | AI CI debugging | Not started | — | |
| 35 | AI verification | Not started | — | |
| 36 | AI capstone | Not started | — | |

## Skill scorecard

Score each from 1 to 5 after practical assessment:

| Skill | Initial score | Target |
|---|---:|---:|
| Read Python traceback | — | 5 |
| Use VS Code debugger | — | 5 |
| Debug Pytest fixtures | — | 5 |
| Diagnose Playwright locator failures | — | 5 |
| Use Trace Viewer | — | 4 |
| Use DevTools Network/Console | — | 5 |
| Diagnose auth/API/UI mismatch | — | 4 |
| Fix flaky tests | — | 4 |
| Debug CI pipeline | — | 4 |
| Validate AI suggestions | — | 5 |
| Measure AI time savings | — | 4 |

---

# 11. How our interactive mentoring will work

We will not dump all 36 sessions in one sitting. This file is the master roadmap; actual teaching will be step-by-step.

For each session:
1. I explain one concept in Hinglish.
2. I give a small runnable example.
3. We intentionally introduce a bug.
4. You run it locally.
5. You share the exact output/error or describe what happened.
6. I ask you to investigate before revealing the solution.
7. We use debugger/logs/trace step by step.
8. You propose the root cause.
9. I review your reasoning strictly.
10. We fix and add regression coverage.
11. I give an assignment.
12. I update the progress tracker based on demonstrated work.

### Strict mentor rules
- I will not mark a topic complete just because you say “understood”.
- I will not jump to AI before manual debugging foundations.
- I will not give you a fake guarantee that AI output is always correct.
- If your diagnosis is weak, I will ask for evidence.
- If code is incorrect, I will explain exactly why.
- If a shortcut is unsafe, I will say so.
- We will focus on transferable engineering skills, not memorizing tool buttons.

### Your first lesson

**Session 1: Python traceback reading and exception debugging.**

We will start with a small Python program containing multiple functions and one intentional defect. You will learn to:
- Read traceback top-to-bottom and bottom-to-top.
- Identify the actual failing line.
- Track the bad value back to its source.
- Use VS Code debugger to prove the cause.
- Fix the code and write a regression test.

**Do not start with AI. First learn to see the bug yourself.**
