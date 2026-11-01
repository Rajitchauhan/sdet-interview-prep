# Focused Debugging Syllabus for QA Automation / SDET

**Approach:** 80/20 — learn the debugging methods that are most useful in day-to-day Python, Pytest, and Playwright automation work. Avoid rare/advanced techniques until they are actually needed.

**Scope:** 27 core topics + one repeatable real-world debugging process. This is the focused syllabus, not the full lesson material. Each topic will be taught with runnable examples, line-by-line explanation, a deliberately introduced bug, investigation steps, root-cause proof, a minimal fix, and a regression test.

---

## 1. Python Debugging — 6 topics

| # | Method / technique | What you should be able to do |
|---|---|---|
| 1 | `print()`, `type()`, `repr()` | Inspect values, data types, whitespace, and unexpected representations. |
| 2 | Traceback and exception reading | Find where an error occurred and follow the call chain to its cause. |
| 3 | `breakpoint()` and `pdb` | Pause execution and inspect program state interactively. |
| 4 | VS Code Debugger | Use breakpoints, step over/into/out, continue, variables, and call stack. |
| 5 | `try-except` and `logging` | Handle expected failures and record useful diagnostic information. |
| 6 | Variables, scope, and call stack | Understand which values exist at a particular execution point and how a function was reached. |

## 2. Pytest Debugging — 7 topics

| # | Method / technique | What you should be able to do |
|---|---|---|
| 1 | `pytest -v`, `-s`, `-x` | Read verbose output, display print output, and stop at the first failure. |
| 2 | `pytest --lf`, `--ff`, `-k` | Rerun failed tests, run failures first, and select tests by expression. |
| 3 | `pytest --tb=short`, `--tb=long` | Control traceback detail and identify the failing assertion. |
| 4 | `pytest --pdb` and `pytest.set_trace()` | Enter the debugger when a test fails or at a chosen line. |
| 5 | Fixture setup/teardown debugging | Investigate fixture order, scope, yielded resources, and cleanup failures. |
| 6 | Mocking and `monkeypatch` debugging | Diagnose incorrect mocks, patch targets, return values, and patched environment/state. |
| 7 | Flaky tests and test isolation | Investigate order dependence, shared state, timing, test data, and cleanup issues. |

## 3. Playwright Debugging — 9 topics

| # | Method / tool | What you should be able to do |
|---|---|---|
| 1 | `page.pause()` and Playwright Inspector | Pause a test, inspect the page, and investigate locators/actions interactively. |
| 2 | Locator debugging: `count()`, `highlight()` | Check how many elements match and visually inspect the target. |
| 3 | Actionability and timeout debugging | Diagnose why an element is not visible, enabled, stable, or actionable in time. |
| 4 | Strict-mode and locator errors | Find ambiguous or incorrect locators and make them uniquely identify the intended element. |
| 5 | Screenshots and videos | Capture visual evidence of failures and compare the browser state. |
| 6 | Playwright Trace Viewer | Inspect actions, snapshots, timing, errors, and network activity around a failure. |
| 7 | Browser console and JavaScript errors | Capture console messages and uncaught page errors. |
| 8 | Network request/response debugging | Inspect requests, responses, status codes, failed requests, and API-related UI failures. |
| 9 | Browser DevTools | Use Elements, Network, Console, and Storage/Application panels for investigation. |

## 4. Repeatable Real-world Debugging Process — 5 steps

1. **Reproduce:** Make the failure happen reliably, using the same inputs and conditions.
2. **Investigate:** Read the error and inspect execution, variables, browser state, logs, or network evidence.
3. **Prove the root cause:** Form a hypothesis and verify it with evidence instead of guessing.
4. **Apply a minimal fix:** Change only what is needed; avoid hiding the symptom.
5. **Regression test:** Rerun the failing test and relevant nearby tests to check that the fix works and did not break existing behavior.

---

## Suggested learning sequence

1. Python debugging foundations
2. VS Code debugger hands-on practice
3. Pytest command-line and failure investigation
4. Fixtures, mocks, isolation, and flaky tests
5. Playwright Inspector and locator failures
6. Actionability, timeout, and strict-mode failures
7. Screenshots, videos, Trace Viewer, console, and network
8. Browser DevTools practice
9. End-to-end debugging exercises using realistic failures

**Estimated duration:** 12–15 focused study sessions, depending on practice time and how independently the exercises are solved.

## What is intentionally out of scope for now

To keep the learning focused, do not study these upfront: advanced profiling, rare Python introspection APIs, complex async internals, deep memory analysis, and specialist observability tooling. Add them later only when a real problem requires them.

## Completion standard

A topic is complete only when you can:

- Explain when and why to use the method.
- Use it on a runnable example without copying blindly.
- Diagnose an intentionally broken example.
- Show evidence for the root cause.
- Apply a minimal fix.
- Add or run a regression test.
- Explain the investigation clearly in an interview or code review.

---

**Important:** This file is the final focused syllabus. It is not a claim that all 27 topics have already been taught. The detailed lessons and exercises should be created and completed one session at a time.
