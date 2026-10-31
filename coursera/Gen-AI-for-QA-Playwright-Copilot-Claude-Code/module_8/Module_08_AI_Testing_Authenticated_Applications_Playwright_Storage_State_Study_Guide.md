# Module 11 — AI Testing for Authenticated Applications
## Browser Extensions, Browser Authentication, Playwright Storage State & Protected Routes
### Complete Hinglish Study Guide | Python + Pytest + Playwright | QA Automation / SDET

> **Module ka central problem:** Public web page ko AI se inspect karwana relatively simple hai. Lekin jab application ke important features login ke peeche hon — username/password, tokens, MFA, protected routes — tab AI ko authenticated browser context kaise milega?
>
> Is module ka practical answer: browser extension / AI-powered browser se already authenticated browser use karna, aur Playwright mein authentication state save karke reuse karna.

---

## 0. ZIP inspection — kya mila?

Uploaded ZIP mein 4 transcript `.txt` files aur 4 matching English `.vtt` subtitle files mile. Inke alawa ek nested `AiPoweredTesting.zip` practical resource archive tha. Nested archive mein 115 files the, including:
- Awesome Pizza application source code.
- Playwright Test Agents ke Planner, Generator aur Healer agent definitions.
- Playwright CLI skill and reference files.
- Authentication setup and protected-route tests.
- Generated test plans.
- Multiple TypeScript Playwright project examples.
- A mock Jira ticket and application log.

### Course lesson coverage

| Lesson | Source mein covered |
|---|---|
| 1 | Public vs private/protected website; browser login; local/session storage ka concept; auth token |
| 2 | Claude Chrome extension se already authenticated website access; protected page inspect karna; AI se Playwright test generate karwana |
| 3 | Advanced Playwright authentication; login setup test; `storageState`; JSON auth file; Git ignore; subsequent tests mein state reuse |
| 4 | Project source available vs source unavailable; AI assistant project code inspect karke test likh sakta hai; browser extension se protected page explore karke test generate karne ka alternative |

### Resource archive inspection

| Resource | Actual files / content |
|---|---|
| `awesome-pizza/` | Express + TypeScript app, login/protected UI, Playwright config, `tests/auth/auth-setup.spec.ts`, `tests/auth/auth-test.spec.ts` |
| `.github/agents/` | Planner, Generator, Healer agent instructions |
| `.claude/agents/` | Claude-side versions of the same agent instructions |
| `.github/skills/playwright-cli/` | Playwright CLI skill and reference docs |
| `Claude-Pizza-Test/` | `CLAUDE.md`, testing plan, API/UI specs, POM |
| `AwesomePizza-PL/` | Separate TypeScript Playwright project with tests and POM |
| `Skills/` | Previous module skills: hello, hello-name, count-tests, test-from-ticket |
| `Files/jira_ticket_mockup.html` | Mock Jira ticket |
| `Files/application.log` | Application log file |

**Source boundary:** Course lectures are about authenticated browser access and Playwright storage state. The nested project contains additional supporting agent/CLI/skill examples from previous modules. This guide uses them to explain the supplied resources, but does not claim that every nested file was demonstrated in Module 11 lectures.

---

# Part 1 — WHY: AI ko authenticated application access kyun chahiye?

## 1.1 Public website vs protected website

Public page:
- URL AI assistant ko de sakte ho.
- Assistant/browser tool page open karke inspect kar sakta hai.
- Login ki requirement nahi.

Protected page:
- Login required.
- Authentication token/cookie/browser state ke bina user-specific page accessible nahi hota.
- AI assistant ko sirf URL dene se access nahi milta.

### Real-world examples

- Banking dashboard.
- E-commerce order history.
- Admin portal.
- HR employee portal.
- SaaS customer dashboard.
- Internal CRM.
- Staff-only application.

**QA perspective:** Production applications ke important flows aksar login ke peeche hote hain. Isliye authenticated test setup SDET ke liye essential hai.

## 1.2 Course ka example

Course ne Awesome Pizza app mein login functionality add ki:
- Login page.
- Username/password form.
- Protected page.
- Logout button.
- Protected data.

Course ka dummy credential example `user` / `pass` hai. Ye sirf supplied demo app ke liye hai; real applications mein credentials hard-code ya share nahi karne.

---

# Part 2 — Browser authentication kaise work karta hai?

## 2.1 Course demonstration

Instructor browser DevTools ke Application/Storage tab mein local storage inspect karta hai.

Initial state:
- Website mein `theme` key stored ho sakti hai.
- Login nahi hua, isliye auth token absent hai.

Login ke baad:
- Application successful authentication response leti hai.
- Browser storage mein `auth_token` set hota hai.
- Protected page token ki presence/use ke basis par content load karta hai.

Logout:
- Application `auth_token` remove karti hai.
- User protected access lose kar deta hai.

### Simple flow

```text
User enters credentials
        |
        v
Frontend sends login request
        |
        v
Backend validates credentials
        |
        v
Backend returns authentication data
        |
        v
Frontend stores token/cookie
        |
        v
Browser sends authentication data
        |
        v
Protected API/page becomes accessible
```

## 2.2 Supplied app ka actual implementation

Resource archive ke `ui/login.js` mein:
- `POST /api/login` request bheji jaati hai.
- JSON body mein `username` aur `password` hote hain.
- Success par `localStorage.setItem('auth_token', data.token)` call hota hai.
- Browser `/protected.html` par redirect hota hai.

`ui/protected.js` mein:
- `localStorage.getItem('auth_token')` se token read hota hai.
- Token absent ho toh auth-required message display hota hai.
- Token present ho toh `/api/protected` ko `Authorization: Bearer <token>` header ke saath request bheji jaati hai.
- API response se protected data render hota hai.
- `401` response par token remove karke login page par redirect hota hai.
- Logout par token remove hota hai aur `/login.html` open hota hai.

### Important distinction

Browser storage mein token ki presence aur backend authorization do separate checks hain.

- Frontend protected page hide/show kar sakta hai.
- Backend ko har protected API request par token validate karna chahiye.
- Sirf UI hide kar dena real security boundary nahi hai.

**QA test idea:** Direct protected API call without token bhi unauthorized honi chahiye; sirf UI-level check enough nahi.

## 2.3 Local storage vs session storage vs cookies

| Storage | General behaviour | Testing implication |
|---|---|---|
| `localStorage` | Origin ke liye persistent browser storage; reload/restart ke baad bhi reh sakta hai | Auth token/theme jaise values store ho sakte hain |
| `sessionStorage` | Tab/session scoped; tab close hone par generally clear | New tab/context behaviour alag ho sakta hai |
| Cookies | Browser request ke saath server ko bhej sakti hain; expiry, domain, path, Secure, HttpOnly, SameSite attributes ho sakte hain | Server-side sessions and cookie auth common hain |

Course instructor broadly browser storage explain karta hai. Actual application code ka auth example specifically `localStorage` mein `auth_token` use karta hai.

**Security nuance:**
- `localStorage` JavaScript se accessible hota hai; XSS ke case mein token exposure risk hota hai.
- `HttpOnly` cookies JavaScript se read nahi ki ja sakti, although browser automatically send kar sakta hai.
- Secure authentication design application architecture par depend karta hai; ek universal storage method sabke liye best nahi.

## 2.4 Common mistakes

- Assume karna ki har website auth token localStorage mein hi rakhti hai.
- Cookie-based authentication ko localStorage token samajhna.
- Browser mein token visible hone ko successful authorization ka complete proof samajhna.
- Logout ke baad sirf UI check karna, protected API access test na karna.
- Real credentials/token screenshots, logs ya Git repo mein commit kar dena.

---

# Part 3 — Browser extension se protected page ko AI se inspect karna

## 3.1 WHY

Agar AI assistant apne isolated browser se website open karta hai, toh uske paas tumhare normal Chrome session ka authentication state automatically nahi hota.

Course ka approach: browser extension / AI-powered browser ko already logged-in browser ke saath use karna.

## 3.2 Course demonstration — Claude Chrome extension

Course flow:

1. Chrome Web Store se Claude extension install ki.
2. Extension mein Claude account se sign in kiya.
3. Chrome browser mein Awesome Pizza app open ki.
4. Website mein dummy credentials se login kiya.
5. Protected area open kiya.
6. Claude application mein prompt diya ki Chrome extension use karke protected website open/inspect karo.
7. Pehle assistant ne URL direct open karne ki koshish ki aur access nahi mila.
8. Prompt mein explicitly “using the Chrome extension” add kiya.
9. Ab extension ke authenticated browser context se protected page inspect hua.
10. Instructor ne kaha ki AI page scrape/inspect kar sakta hai aur Playwright tests generate karne mein help kar sakta hai.

Course mein direct extension panel se interact karna bhi dikhaya gaya; instructor ko main Claude app se extension invoke karna zyada convenient laga.

### Course ke mentioned alternatives

- Claude Chrome extension.
- ChatGPT Atlas.
- Google Gemini Chrome extension.
- Browser Use.

**Availability caveat:** Transcript ke waqt Claude extension ke liye paid plan required bataya gaya tha. Browser extensions, AI browser features aur plan requirements time ke saath change ho sakti hain. Isko current subscription guarantee mat samajhna.

## 3.3 Protected browser access ka QA workflow

```text
Human logs in through browser
          |
          v
Browser holds authenticated state
          |
          v
AI extension is allowed to inspect that browser
          |
          v
AI explores protected UI
          |
          v
AI drafts test scenarios/code
          |
          v
QA reviews and runs tests independently
```

## 3.4 Safety: “Allow always” ka risk

Course demo mein extension tool actions ke liye permission prompt dikhata hai, including “Allow” and “Always allow actions on this site”.

Real QA work mein:
- Har permission ko blindly approve mat karo.
- Read-only inspection aur destructive actions alag rakho.
- Test environment prefer karo.
- Payment/order/delete/admin actions ke liye approval boundaries rakho.
- Browser session mein personal/customer data ho toh AI access carefully control karo.
- Shared workstation par logged-in session expose mat chhodo.

**Important:** Browser extension ko authenticated session ka access dena powerful permission hai. Ye normal public-page browsing se zyada sensitive hai.

---

# Part 4 — Playwright authentication and Storage State

<badge color="success">Module ka most important Playwright topic</badge>

## 4.1 WHY: Har test mein login repeat kyun na karein?

Suppose tumhare paas 30 tests hain jo protected dashboard verify karte hain.

Naive approach:
- Har test login page open kare.
- Username/password fill kare.
- Login click kare.
- Redirect wait kare.
- Protected feature test kare.

Problems:
- Repeated login overhead.
- Test execution slow.
- Login flow itself frequently run hone se unrelated tests fail ho sakte hain.
- Authentication logic aur feature tests tightly coupled ho jaate hain.

Better approach:
1. Dedicated setup test login perform kare.
2. Successful authentication ke baad browser state save kare.
3. Protected tests saved state reuse karein.
4. Har test apne isolated browser context mein authenticated start ho sakta hai.

## 4.2 WHAT: Playwright Storage State

Playwright browser context ka relevant authentication state file mein save kar sakta hai.

Course example:
- File path: `playwright/.auth/user.json`
- Save operation: `page.context().storageState({ path: ... })`
- Reuse: `test.use({ storageState: ... })` in Playwright Test (TypeScript).

Storage state file mein application origin ke against local storage values aur cookies jaise authentication-related data ho sakte hain. Modern Playwright versions IndexedDB storage state support bhi provide karte hain when explicitly requested.

**Important correction/nuance:** Playwright storage state ko sessionStorage ka automatic complete backup mat samajhna. SessionStorage ko separately handle karne ki zaroorat ho sakti hai. Course ke demo mein token localStorage mein hai, isliye storageState approach us example ke liye fit hai.

## 4.3 Course ke actual auth setup test

Supplied archive: `awesome-pizza/tests/auth/auth-setup.spec.ts`

```typescript
import { test, expect } from '@playwright/test'

test('authenticate', async ({ page }) => {

    const dummyUser = 'user';
    const dummyPass = 'pass';

    await page.goto('http://localhost:3000/login.html')

    await page.fill('#login-username', dummyUser);
    await page.fill('#login-password', dummyPass);
    await page.click('#login-btn');

    await expect(page).toHaveURL('http://localhost:3000/protected.html');

    await page.context().storageState({
        path: 'playwright/.auth/user.json'
    })
})
```

### Line-by-line explanation

| Code | Meaning |
|---|---|
| `import { test, expect }` | Playwright Test runner and assertion API import |
| `test('authenticate', ...)` | Authentication setup test define |
| `dummyUser`, `dummyPass` | Demo app ke credentials |
| `page.goto(...)` | Login page open |
| `page.fill(...)` | Username/password fields fill |
| `page.click(...)` | Login button click |
| `expect(page).toHaveURL(...)` | Confirm redirect to protected page |
| `page.context().storageState(...)` | Current context ka storage state JSON file mein save |

### Is test mein kya good hai?

- Login operation explicit hai.
- Redirect verify hota hai.
- State save karne se pehle successful URL assert hai.
- Auth state ek reusable file mein save hoti hai.

### Is test mein kya improve kar sakte hain?

- Credentials hard-coded hain — real project mein environment variables/secrets use karo.
- `baseURL` config use kar sakte ho.
- Protected page par actual authenticated content/assertion bhi verify karo.
- Setup test execution order/configuration properly define karo.
- Auth file ko Git ignore mein rakho.
- File path create/permissions ensure karo.

## 4.4 Auth file ko Git se protect karna

Course ka strong warning:

`playwright/.auth/` folder ko `.gitignore` mein add karo.

Example:

```gitignore
playwright/.auth/
```

Kyun?
- `user.json` mein cookies/token/local storage values ho sakti hain.
- Ye values kisi ko logged-in session reuse karne de sakti hain.
- Git commit/push hone par credentials/session leak ho sakta hai.

**Rule:** Auth state file ko source code ki tarah treat mat karo; ye sensitive session material hai.

---

# Part 5 — Saved state ko tests mein reuse karna

## 5.1 Course ka TypeScript example

Supplied archive: `awesome-pizza/tests/auth/auth-test.spec.ts`

```typescript
import { test, expect } from '@playwright/test'

test.use({ storageState: 'playwright/.auth/user.json' })

test('protected routes', async ({ page }) => {

    await page.goto('http://localhost:3000/protected.html')

})
```

### Explanation

- `test.use(...)` current test file ke tests ke liye storage state configure karta hai.
- Test start hone par Playwright context saved authentication state load karta hai.
- `page.goto('/protected.html')` protected page open karta hai.
- Har protected test ko login form dobara fill karne ki zaroorat nahi.

**Source nuance:** Supplied `auth-test.spec.ts` example page open karta hai, lekin explicit assertion add nahi karta. Production-quality test mein protected content/identity-specific element assert karna chahiye.

## 5.2 Setup project dependency — stronger Playwright Test pattern

Course lecture setup test concept explain karta hai. Practical project mein Playwright Test ke documented setup project/dependency pattern se setup test ko dependent tests se pehle run karwana more reliable hai.

Illustrative TypeScript configuration:

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',

  projects: [
    {
      name: 'setup',
      testMatch: /.*auth-setup\.spec\.ts/,
    },
    {
      name: 'chromium',
      use: {
        ...devices['Desktop Chrome'],
        storageState: 'playwright/.auth/user.json',
      },
      dependencies: ['setup'],
    },
  ],
});
```

Ye mentor addition hai; supplied project config mein ye exact setup-project dependency configured nahi thi.

### Why this pattern matters?

Agar setup test state file generate karne se pehle protected tests start ho gaye, toh tests fail honge. Dependency ordering is risk ko address karti hai.

**Additional note:** Parallel execution, multiple roles, token expiry aur cleanup ke liye setup architecture carefully design karna padta hai. Different roles ke liye separate auth state files rakho.

---

# Part 6 — Python + Pytest + Playwright adaptation

Course code TypeScript Playwright Test mein hai. Tumhari Python stack ke liye equivalent workflow neeche hai. Ye mentor adaptation hai, course ka exact code nahi.

## 6.1 Python setup script/test: login and save storage state

```python
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

AUTH_DIR = Path("playwright/.auth")
AUTH_FILE = AUTH_DIR / "user.json"


def main():
    AUTH_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        context = browser.new_context()
        page = context.new_page()

        page.goto("http://localhost:3000/login.html")

        page.get_by_label("Username:").fill("user")
        page.get_by_label("Password:").fill("pass")
        page.get_by_role("button", name="Login").click()

        expect(page).to_have_url(
            "http://localhost:3000/protected.html"
        )

        expect(
            page.get_by_role("heading", name="Protected Area")
        ).to_be_visible()

        context.storage_state(path=str(AUTH_FILE))

        context.close()
        browser.close()


if __name__ == "__main__":
    main()
```

### Key points

- `Path.mkdir(...)` auth directory create karta hai.
- `browser.new_context()` isolated browser context create karta hai.
- Login complete hota hai.
- Redirect assertion authentication success verify karti hai.
- Protected heading assertion stronger evidence provide karti hai.
- `context.storage_state(...)` JSON file save karta hai.
- Browser/context cleanly close hote hain.

**Credential warning:** Demo credentials example ke liye hain. Real app mein environment variables/secret manager use karo. Credentials source file mein commit mat karo.

## 6.2 Python test mein saved state reuse

```python
from pathlib import Path
import pytest
from playwright.sync_api import Page, expect

AUTH_FILE = Path("playwright/.auth/user.json")


@pytest.fixture(scope="session")
def require_auth_state():
    if not AUTH_FILE.exists():
        pytest.fail(
            "Auth state not found. Run the authentication setup first."
        )


def test_protected_page_is_accessible(
    page: Page,
    require_auth_state
):
    # This example assumes the browser context is created
    # with the saved storage state by the fixture/configuration.
    page.goto("http://localhost:3000/protected.html")

    expect(
        page.get_by_role("heading", name="Protected Area")
    ).to_be_visible()
```

Upar wala test tabhi authenticated hoga jab `page` fixture ke context mein `storage_state` load kiya gaya ho. Sirf file exist hone se Playwright automatically usko use nahi karta.

### Correct reusable pytest fixture approach

A simple approach is to create a dedicated context using the saved state:

```python
import pytest
from pathlib import Path
from playwright.sync_api import Browser, BrowserContext, Page

AUTH_FILE = Path("playwright/.auth/user.json")


@pytest.fixture
def authenticated_context(browser: Browser) -> BrowserContext:
    if not AUTH_FILE.exists():
        pytest.fail("Auth state missing. Run auth setup first.")

    context = browser.new_context(
        storage_state=str(AUTH_FILE)
    )
    yield context
    context.close()


@pytest.fixture
def authenticated_page(
    authenticated_context: BrowserContext
) -> Page:
    page = authenticated_context.new_page()
    return page
```

Test:

```python
from playwright.sync_api import expect


def test_protected_page(authenticated_page):
    authenticated_page.goto(
        "http://localhost:3000/protected.html"
    )

    expect(
        authenticated_page.get_by_role(
            "heading",
            name="Protected Area"
        )
    ).to_be_visible()
```

**Note:** Ye example `pytest-playwright` plugin ke `browser` fixture par based hai. Ensure plugin installed hai aur fixtures available hain. Agar tum `sync_playwright()` manually manage kar rahe ho, toh browser/context lifecycle manually manage karna hoga.

## 6.3 Session scope vs test isolation

Common mistake: Authenticated `BrowserContext` ko session scope mein create karke saare tests share kara dena.

Potential problems:
- Cookies/local storage mutations leak ho sakti hain.
- One test logout kare toh doosre tests fail ho sakte hain.
- Parallel tests same state mutate kar sakte hain.

Safer default:
- Auth state file session-level reuse.
- Each test gets its own new browser context loaded from that state.
- Each test remains isolated.

---

# Part 7 — AI ko authenticated page access dene ke two approaches

Course lecture explicitly two scenarios explain karta hai.

## Approach A — Application source code available

Example: Tumhare paas local project/repository hai, jisme:
- Frontend code.
- Backend code.
- Test code.
- Requirements/config.

AI coding assistant repository inspect kar sakta hai.

Course workflow:
1. Auth setup test run karke `user.json` create.
2. Protected test file mein storage state use.
3. AI assistant ko test file open/context mein do.
4. Prompt: “Complete this test.”
5. Assistant source code inspect karke protected page ke DOM, selectors, API calls aur behaviour samajh sakta hai.
6. Test generate/complete hota hai.
7. Human test run karke verify karta hai.

**Benefit:** AI ko app ka source code aur test project dono milte hain.

**Risk:** Source code inspect karna actual runtime authentication proof ka substitute nahi. Test ko authenticated browser context mein execute karna phir bhi zaroori hai.

## Approach B — Application source code unavailable

Example:
- Third-party SaaS.
- Client-owned application.
- Black-box testing.
- Source repository access nahi.

Course workflow:
1. Chrome browser mein user manually login karta hai.
2. Claude Chrome extension already authenticated browser access use karti hai.
3. AI ko protected URL diya jata hai.
4. Prompt explicitly says “using the Chrome extension”.
5. AI protected page inspect karta hai.
6. User tool actions allow karta hai.
7. AI observed page ke basis par Playwright test draft kar sakta hai.

**Course limitation:** Instructor recording ke waqt is approach ko apna available workaround batata hai. Ye universal “only solution” nahi hai. Other approved browser automation, test accounts, staging access, documented APIs, or test hooks may be available depending on the environment.

## Comparison

| Factor | Source code available | Source code unavailable |
|---|---|---|
| AI context | Repository + app source + test code | Authenticated browser UI |
| Requirement understanding | Source + ticket/docs | UI observation + provided requirements |
| Locator discovery | Source/DOM/runtime | Browser-visible DOM/UI |
| Hidden business logic | Source may reveal implementation | Usually not visible |
| Test generation | Project conventions can be reused | Must infer more from UI |
| Risk | AI may overfit implementation | AI may invent hidden rules |
| Best use | White-box-informed automation | Black-box UI exploration |

---

# Part 8 — Supplied project archive: what to inspect

Nested archive mein actual files diye gaye hain. Ye tumhare liye practical reference hai.

## 8.1 Authentication-related files

| File | Purpose |
|---|---|
| `awesome-pizza/ui/login.html` | Login form; username/password labels and button |
| `awesome-pizza/ui/login.js` | POST login request, store `auth_token`, redirect |
| `awesome-pizza/ui/protected.html` | Protected area page |
| `awesome-pizza/ui/protected.js` | Read token, request protected API, logout/remove token |
| `awesome-pizza/tests/auth/auth-setup.spec.ts` | Login and save `playwright/.auth/user.json` |
| `awesome-pizza/tests/auth/auth-test.spec.ts` | Load saved state for protected route test |
| `awesome-pizza/playwright.config.ts` | Playwright test configuration |
| `awesome-pizza/.gitignore` | Project ignore rules |

## 8.2 Agent files included

The archive includes:
- `.github/agents/playwright-test-planner.agent.md`
- `.github/agents/playwright-test-generator.agent.md`
- `.github/agents/playwright-test-healer.agent.md`
- Claude equivalents under `.claude/agents/`

These files specify:
- Agent name/description.
- Tool permissions.
- Model setting in the course sample.
- MCP server configuration.
- Workflow instructions.

### Planner file highlights

- `planner_setup_page` once before other browser tools.
- Explore snapshots.
- Screenshots only if needed.
- Identify interactive elements, forms and navigation.
- Cover happy path, edge/boundary, error handling.
- Save plan using `planner_save_plan`.
- Each scenario needs title, steps, expected outcomes and starting-state assumptions.
- Aim for independent scenarios.

### Generator file highlights

- Obtain test plan scenario.
- Run `generator_setup_page`.
- Execute scenario steps through browser tools.
- Read generator log.
- Write one test file for one test.
- Include step comments.
- Match test title and describe group to plan.
- Use assertions, not snapshot testing (course sample instruction).

### Healer file highlights

- Run tests to identify failures.
- Debug each failure.
- Inspect error, snapshot, selector, timing, assertion.
- Determine likely root cause.
- Edit and rerun.
- Fix one issue at a time.
- Avoid `networkidle` and discouraged APIs.
- Course sample says if failure persists and test is believed correct, mark `test.fixme()` with comment.

**Mentor review:** The last instruction is risky if followed mechanically. Marking a test `fixme` can hide an unresolved product/test issue. A QA engineer should first classify the failure, record evidence and get an explicit decision. Do not turn a genuine product defect into a skipped test merely to achieve a green run.

---

# Part 9 — Real-life risks with storage state

## 9.1 Expired token

Saved `user.json` token may expire.

Symptoms:
- Protected page redirects to login.
- API returns 401.
- Test fails even though selector is correct.

Solution:
- Regenerate auth state through setup.
- Use short-lived test credentials designed for automation.
- Avoid hard-coding static tokens.
- Make setup failure message clear.

## 9.2 Role-based authentication

Suppose application has:
- Admin.
- Manager.
- Staff.

Create separate auth states:

```text
playwright/.auth/
├── admin.json
├── manager.json
└── staff.json
```

Each test should use the role it is intended to validate.

Do not use admin state for every test — that can hide authorization defects.

## 9.3 Logout behaviour

Logout should be tested at multiple levels:
1. UI returns to login.
2. Auth token/cookie cleared or invalidated as designed.
3. Protected API request without auth returns 401/403.
4. Back navigation does not reveal protected data.
5. Old token reuse is rejected if server-side invalidation is expected.

## 9.4 Session state and sensitive data

- Auth JSON should be ignored by Git.
- CI secrets and generated state need restricted access.
- Don't upload auth state to tickets/chat.
- Delete stale local state when no longer needed.
- Use dedicated test accounts, not personal accounts.
- Avoid production accounts for automation.

---

# Part 10 — Common mistakes and debugging

| Mistake | Why it fails | Better approach |
|---|---|---|
| Save state before login completes | Token/cookie not yet stored | Assert authenticated redirect/content before saving |
| Use wrong origin | Storage state tied to origin | Use same base URL/domain |
| Forget `.gitignore` | Session token leak | Ignore auth directory and verify Git status |
| Assume sessionStorage is included | State may not restore | Handle sessionStorage separately if app uses it |
| Reuse expired token | 401/login redirect | Regenerate state |
| Share mutable context across tests | State leaks | New context per test using same state file |
| Use admin state for staff test | Authorization bug hidden | Separate role states |
| Test only protected UI | Backend may still be exposed | Test API authorization too |
| Let AI “fix” 401 by changing assertions | Real auth defect hidden | Inspect token, request, response and backend rules |
| Store real password in test file | Credential exposure | Environment variables/secret manager |

---

# Part 11 — Practical lab using the supplied Awesome Pizza app

## Lab A — Understand login mechanism

Open:
- `ui/login.js`
- `ui/protected.js`

Answer:
1. Which endpoint receives login request?
2. Which HTTP method?
3. Which fields are sent?
4. Where is the token stored?
5. Which header is sent to protected API?
6. What happens on 401?
7. What does logout remove?

## Lab B — Run auth setup

Course resource is TypeScript Playwright.

1. Install project dependencies using its package instructions.
2. Start the Awesome Pizza server.
3. Run auth setup spec.
4. Verify redirect to `/protected.html`.
5. Inspect generated `playwright/.auth/user.json`.
6. Confirm `.gitignore` covers the auth folder.
7. Do not share/commit the generated token.

## Lab C — Verify protected route

1. Run the protected test with storage state.
2. Add an assertion for protected heading or protected data.
3. Delete/rename the auth JSON and rerun.
4. Observe expected failure.
5. Re-run setup and verify recovery.

## Lab D — Logout and authorization

1. Load protected page with auth state.
2. Click logout.
3. Verify redirect to login.
4. Attempt to open protected page again.
5. Verify protected content is not available.
6. Inspect protected API without auth and verify unauthorized response.

## Lab E — Python adaptation

Implement:
- Python login setup.
- Save storage state.
- Pytest fixture that creates a context with saved state.
- Protected page assertion.
- Logout test.
- Missing/expired state handling.

---

# Part 12 — Interview answers

## Q1. What is Playwright storage state?

**Simple English:**

“Storage state lets Playwright save browser authentication-related state, such as cookies and local storage, to a file and reuse it in another browser context.”

**Stronger answer:**

“After a successful login, I can save the browser context storage state to a JSON file. Subsequent tests can create a new browser context using that file, so they start authenticated without repeating the login UI flow. I keep the file out of source control because it may contain reusable session credentials. I also handle token expiry, different user roles and test isolation.”

## Q2. Why use a separate authentication setup test?

“To avoid repeating the login flow in every protected test. A setup step authenticates once and saves the reusable state. Feature tests can then focus on the protected functionality.”

## Q3. Why add the auth folder to `.gitignore`?

“Because the state file can contain cookies or tokens that allow access to an authenticated session. Committing it could expose credentials or private application data.”

## Q4. How can AI inspect a protected website?

“If an AI browser extension is connected to a browser where the user has already authenticated, the AI may inspect the protected page through that browser session, subject to permissions. For a local project, an AI coding assistant can also inspect the source code and use Playwright storage state in generated tests.”

## Q5. What if you do not have source code access?

“I can use an approved authenticated browser session to explore the UI, document observed behaviour and draft black-box tests. I would still need acceptance criteria or stakeholder clarification for business rules that are not visible in the UI.”

## Q6. Does storage state automatically include sessionStorage?

“No. I would not assume that. Playwright storage state supports cookies and local storage, and can include IndexedDB when configured. SessionStorage generally needs a separate handling approach.”

## Q7. What happens if the saved token expires?

“The protected request may return 401 or redirect to login. I would regenerate the state through the authentication setup and ensure the test environment uses valid automation credentials.”

## Q8. How do you test role-based access?

“I maintain separate authenticated states for each role and verify both allowed and forbidden actions. I avoid using an administrator state for all tests because that can hide authorization defects.”

---

# Part 13 — Module 11 revision questions

Notes band karke answer karo:

1. Public website aur protected website mein difference kya hai?
2. Course app mein login ke baad token kahan store hota hai?
3. Frontend token check aur backend authorization mein difference?
4. LocalStorage, sessionStorage aur cookies mein difference?
5. AI browser extension protected page ko kaise access karti hai?
6. Extension permissions ko carefully handle kyun karna chahiye?
7. Playwright `storageState` ka purpose kya hai?
8. `playwright/.auth/user.json` mein sensitive data kyun ho sakta hai?
9. Auth setup test mein redirect assertion kyun important hai?
10. `test.use({ storageState: ... })` kya karta hai in Playwright Test?
11. Python Playwright mein storage state kaise load karoge?
12. SessionStorage automatically included kyun assume nahi karna chahiye?
13. Different roles ke liye separate state files kyun?
14. Expired auth state kaise diagnose karoge?
15. AI-generated protected-page test ko kaise validate karoge?

---

# Part 14 — Module progress tracker

| Topic | Status |
|---|---|
| Public vs protected website | ⬜ |
| Browser authentication flow | ⬜ |
| LocalStorage/sessionStorage/cookies | ⬜ |
| Supplied app login implementation | ⬜ |
| Browser extension authenticated access | ⬜ |
| Extension permission/security | ⬜ |
| Playwright storage state | ⬜ |
| Auth setup test | ⬜ |
| `.auth` folder and `.gitignore` | ⬜ |
| Reuse state in Playwright Test | ⬜ |
| Python storage state setup | ⬜ |
| Pytest authenticated context fixture | ⬜ |
| Source available vs unavailable workflow | ⬜ |
| Role-based auth and token expiry | ⬜ |
| Practical labs | ⬜ |
| Interview answers | ⬜ |

## Mentor scoring rubric

- **0 — Unknown:** Authentication and storage state explain nahi kar pa rahe.
- **1 — Basic:** Token and JSON file ka concept samajh aaya.
- **2 — Working:** Login state save/reuse karke protected test chala sakte ho.
- **3 — Strong:** Python fixture design, role isolation, expiry, security, API authorization aur AI access limitations explain kar sakte ho.

**Module complete tab hoga jab tum ek authenticated test setup independently implement kar sako, protected UI/API verify kar sako aur auth state ko securely manage kar sako.**

---

# Final mentor note

Module 11 ka sabse important practical takeaway:

**Authentication ko har feature test ke andar repeat mat karo. Authentication setup ko separate rakho, state securely save karo, aur isolated contexts mein reuse karo.**

AI ke liye bhi same principle apply hota hai:
- Public URL dena aur authenticated browser access dena different hai.
- Source code access aur browser session access different types of context hain.
- AI ka protected page inspect kar lena security validation ka substitute nahi.
- Generated test ka pass hona correct authorization prove nahi karta.
- Auth state file sensitive hoti hai — Git, logs aur shared chats se protect karo.

**Strong SDET woh hai jo happy-path login ke saath expired token, logout, role permissions, unauthorized API calls aur test isolation bhi verify karta hai.**
