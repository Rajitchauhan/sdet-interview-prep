# Module 08 — Agentic AI, MCP, Chrome DevTools MCP & Playwright MCP
## Complete Hinglish Study Guide | QA Automation / SDET | Python + Pytest + Playwright

> **Module ka central idea:** AI assistant ko sirf code suggest karne tak limited na rakhkar, controlled tools ke through browser inspect/operate karne, test generate karne aur debugging mein assist karne ki capability dena.
>
> **Important distinction:** AI-generated output ko automatically correct ya production-ready nahi maana ja sakta. QA engineer ki responsibility requirements, assertions, test data, security, execution aur review ki hi rahegi.

---

## 0. Is guide ko kaise use karna hai

Har topic ko is order mein samjho:

1. **WHY** — QA engineer ko iski zaroorat kyun?
2. **WHAT** — concept kya hai?
3. **HOW** — practical workflow kaise chalta hai?
4. **Example** — QA / Playwright context mein example.
5. **Common mistakes** — real-world mein kya galat hota hai?
6. **Interview answer** — simple English + detailed English answer.
7. **Practice** — khud karke verify karo.

### Source coverage and limitations

ZIP mein 9 transcript `.txt` files aur 9 English subtitle `.vtt` files mile. Transcript aur subtitle pairs largely same lecture content ko represent karte hain; guide mein duplicate material ko repeat nahi kiya gaya.

| Lesson | Course source mein covered |
|---|---|
| 1 | Agentic AI vs traditional chat AI; tool use; MCP ki need |
| 2 | MCP servers kahan milte hain; server selection and safety |
| 3 | Node.js, `npx`, Python, `uv`, `uvx` requirements |
| 4 | Claude Desktop mein MCP configuration; Airbnb MCP example |
| 5 | VS Code + GitHub Copilot mein MCP configuration; project vs user config |
| 6 | Chrome DevTools MCP; browser interaction, network, console, Lighthouse |
| 7 | Playwright MCP; natural-language browser interaction and test generation |
| 8 | Optional AWS MCP; AWS documentation MCP via `uvx` |

**Source boundary:** Course ka hands-on app example pizza store (`localhost:3000`) hai. Course VS Code/GitHub Copilot aur Claude Desktop configuration dikhata hai. Python examples aur QA safeguards jo neeche clearly “Mentor addition” ke naam se hain, woh course transcript ka verbatim hands-on nahi hain.

---

# Part 1 — Agentic AI

## 1.1 WHY: Normal chat AI se aage kyun jaana pada?

Socho tumhara Playwright test fail ho gaya.

### Traditional / non-agentic workflow

1. Tum failing test ka code copy karte ho.
2. AI chat mein paste karke solution poochte ho.
3. AI suggested code deta hai.
4. Tum IDE mein code update karte ho.
5. Tum khud test run karte ho.
6. Agar phir fail hua, error dobara AI ko dete ho.

Is workflow mein **human continuously loop mein hota hai**. AI suggestion deta hai, lekin environment mein action aur verification tum karte ho.

### Agentic workflow

Agentic AI workflow mein AI application, allowed tools ke through, multiple steps kar sakti hai:

1. Project files inspect karna.
2. Failing test aur related code samajhna.
3. Relevant documentation search karna.
4. Candidate fix propose/apply karna.
5. Test command execute karna.
6. Result inspect karna.
7. Findings aur changes report karna.

Course ka analogy: **LLM is the brain; tools are the hands.**

Lekin practical QA mein human oversight remove nahi hota. High-impact actions, code changes, credentials, deployments aur test data mutation ke liye approval/review important hai.

## 1.2 WHAT: Agentic AI kya hai?

**Simple definition:** Agentic AI ek aisa AI-based system hai jo goal ko achieve karne ke liye context samajhkar, tools use karke, multiple actions aur feedback steps perform kar sakta hai.

| Traditional chat AI | Agentic workflow |
|---|---|
| Mostly prompt → response | Goal → plan/actions → feedback → result |
| User manually code copy/run karta hai | System permitted tools se files/run/tests inspect kar sakta hai |
| Har step ke liye user ko prompt dena pad sakta hai | Multiple connected steps execute ho sakte hain |
| Tool access limited ya absent ho sakta hai | Tool use workflow ka important part hai |

**Important nuance:** “Agentic” ka matlab fully autonomous, always-correct, ya human-free nahi hai. Actual autonomy configured tools, permissions, policies aur user approvals par depend karti hai.

## 1.3 QA engineer ke use cases

- Existing test failure ka context collect karna.
- Test strategy ka first draft banana.
- Natural-language scenarios se test skeleton generate karna.
- Browser console/network information inspect karna.
- API documentation aur request collections draft karna.
- Test run ke logs summarize karna.
- Repetitive project setup tasks mein help lena.

## 1.4 Common mistakes

- AI ke generated test ko bina review ke merge kar dena.
- AI ke “test passed” claim ko actual test report samajh lena.
- Agent ko unnecessary terminal, filesystem, network ya production access dena.
- Prompt mein credentials, customer data ya secrets paste kar dena.
- AI se test generate karwana, lekin expected result independently define na karna.

## 1.5 Interview answers

**Simple English:**

“Traditional AI mainly responds to prompts. Agentic AI can use tools to inspect context and perform a sequence of actions toward a goal. In QA, it can help inspect failures, interact with browsers, generate tests and analyze results. I still review the changes and verify the test results.”

**Stronger answer:**

“An agentic workflow combines an LLM with tools and an execution loop. Instead of only suggesting a code change, the system may inspect the repository, gather relevant context, make a proposed change, execute tests and evaluate the feedback. In QA automation, this can accelerate test creation and debugging. However, generated tests can contain incorrect assumptions, weak assertions or unsafe actions, so I treat AI output as a draft and retain human review, access control and independent verification.”

**Keywords:** LLM, tools, context, execution loop, feedback, human oversight, verification.

---

# Part 2 — Model Context Protocol (MCP)

## 2.1 WHY: MCP ki zaroorat kyun?

Imagine Chrome browser ke developers ek browser-control tool banana chahte hain. Agar har AI application ke liye alag integration likhni pade — ek ChatGPT ke liye, ek Claude ke liye, ek GitHub Copilot ke liye — to same functionality baar-baar implement karni padegi.

MCP ka purpose hai ek standardized way provide karna jisse AI applications external tools/systems se connect ho saken.

## 2.2 WHAT: MCP kya hai?

Course ke mutabik, **Model Context Protocol (MCP) ek open standard hai jo AI applications ko external systems se connect karne mein help karta hai.**

Course analogy: **MCP is like USB-C for AI applications.**

USB-C analogy ka meaning:
- Standard connector/interface.
- Different compatible devices ek common interface use kar sakte hain.
- Har pairing ke liye completely custom connector design karne ki zaroorat kam hoti hai.

MCP context mein:
- AI client: jaise VS Code/GitHub Copilot ya Claude Desktop.
- MCP server: tools/resources expose karne wala server.
- Tools: defined actions, jaise browser navigate karna, network requests read karna, documentation search karna.
- Client: available tools discover karke supported workflow mein invoke karta hai.

> **Terminology note:** MCP ek protocol/standard hai; MCP server us protocol ko implement karne wala component hai. Dono same cheez nahi hain.

## 2.3 Example: Pizza application MCP

Course instructor ne pizza web store/API ke upar MCP example banaya. AI assistant se natural language mein pooch sakte hain:
- Aaj ka pizza menu kya hai?
- Pizza order karo.
- Mera order check karo.

Iska purpose ye dikhana hai ki assistant website khole bina, connected MCP tools ke through backend functionality use kar sakta hai.

**QA connection:** Isi pattern se test-data setup, test environment status, ya approved internal QA utilities expose ki ja sakti hain — lekin tool permissions carefully design honi chahiye.

## 2.4 MCP server kahan mil sakte hain?

Course mein sources:
- Awesome MCP Servers GitHub collection.
- Claude Code ki MCP documentation/list.
- VS Code Marketplace ka MCP Servers section.

Course ka safety message:
- Third-party MCP server ko blindly trust mat karo.
- Official/maintainer-published source ko preference do.
- GitHub stars ek popularity signal ho sakte hain, **security guarantee nahi**.
- Code, maintainer, recent activity, permissions, dependencies aur issue history review karo.

### Mentor addition — safer MCP selection checklist

MCP install karne se pehle:
- [ ] Official repository/maintainer verify kiya?
- [ ] Source code aur package identity match karte hain?
- [ ] Required permissions samjhe?
- [ ] Kya server filesystem, shell, browser, network ya secrets access maangta hai?
- [ ] Dependencies aur release history check ki?
- [ ] Local/test environment mein try kiya?
- [ ] Production credentials aur customer data se isolate rakha?
- [ ] Unnecessary tools disable kiye?

**Remember:** GitHub stars, marketplace listing ya official-looking name akela safety proof nahi hai.

---

# Part 3 — MCP runtimes and package managers

## 3.1 WHY

MCP server ek executable process hota hai. Usko start karne ke liye relevant runtime/package manager available hona chahiye.

## 3.2 Course ke key associations

| MCP implementation | Course mein mentioned runtime/launcher | Tumhe kya chahiye |
|---|---|---|
| TypeScript / Node.js based | `npx` | Node.js |
| Python based | `uvx` (recommended in course example) or `pip` | Python + uv/uvx for that workflow |

Course explain karta hai:
- `npx` Node.js ecosystem ka package execution tool hai.
- `uv` Python package/environment manager hai.
- `uvx` Python CLI tools ko execute karne ke liye use hota hai.
- Har MCP server ki own documentation check karni hoti hai; command and arguments server-specific hote hain.

### Basic mental model

```text
MCP client
   |
   | starts/connects to
   v
MCP server process
   |
   | exposes tools
   v
External system (browser, docs, API, etc.)
```

## 3.3 Course examples

- Playwright MCP: Node.js / `npx` based setup.
- AWS documentation MCP: Python tooling / `uvx` based setup.

**Caution:** Course mein shown package tags/commands time ke saath change ho sakte hain. Install karte waqt official MCP repository ki current instructions follow karo. Transcript ka command blindly copy mat karo.

## 3.4 Common mistakes

- `npx` command chalana jab Node.js installed nahi hai.
- `uvx` command chalana jab uv available nahi hai.
- Server-specific arguments miss kar dena.
- JSON config mein comma/bracket mistake.
- Config update ke baad server restart na karna.
- Wrong project ke config file ko edit karna.

## 3.5 Interview answer

“Different MCP servers can use different runtimes. The course demonstrates Node-based servers launched through npx and Python-based servers launched through uvx. I check the server’s official installation instructions because the exact command and arguments depend on that server.”

---

# Part 4 — MCP configuration: Claude Desktop and VS Code

## 4.1 Claude Desktop — course workflow

Course demonstration ka sequence:

1. Claude Desktop open karo.
2. File → Settings → Developer Settings.
3. Claude configuration file edit/open karo.
4. JSON ke andar `mcpServers` entry add karo.
5. Server ka configuration object add karo.
6. JSON valid hai ya nahi verify karo.
7. Claude Desktop ko completely exit karo.
8. Application dobara start karo.
9. Connectors/tools area mein server visible hai ya nahi check karo.
10. Natural-language prompt se server test karo.

Course example: Airbnb MCP server, Rome ke liye apartment search.

**Important:** Ye Airbnb MCP ka demonstration hai; tumhare QA automation workflow ke liye install karna mandatory nahi.

## 4.2 VS Code + GitHub Copilot — course workflow

Course demonstration:

1. VS Code project open karo.
2. Project ke andar `.vscode` folder banao, agar absent ho.
3. `.vscode/mcp.json` file create karo.
4. MCP configuration mein `servers` entry add karo.
5. JSON save karo.
6. Server start karo.
7. GitHub Copilot Agent chat ke Configure Tools section mein server/tools verify karo.
8. Prompt se tool invoke karke test karo.

Course example: Airbnb MCP server.

### Project-level vs user-level configuration

| Configuration | Scope | Kab use karein |
|---|---|---|
| Project `.vscode/mcp.json` | Particular project | Project-specific tools/config |
| VS Code user MCP configuration | User's VS Code environment | Aisa MCP jo multiple projects mein use karna ho |

Course ke mutabik, project configuration doosre project mein automatically available nahi hoti. Global/user configuration machine ke VS Code instances mein reusable ho sakti hai.

**Security note:** Global config convenient hai, lekin powerful MCP tools ko har project mein available karna risk bhi badha sakta hai. Least privilege follow karo.

### Illustrative JSON shape — not a copy-paste server command

Actual `command`, `args` aur environment values official server documentation se aayenge.

```json
{
  "servers": {
    "example-server": {
      "command": "REPLACE_WITH_DOCUMENTED_COMMAND",
      "args": [
        "REPLACE_WITH_DOCUMENTED_ARGUMENTS"
      ]
    }
  }
}
```

Ye sirf configuration structure samjhane ke liye hai. Placeholder values ko executable command mat samajhna.

## 4.3 Common mistakes

- `mcpServers` aur VS Code `servers` naming ko clients ke across mix karna.
- JSON mein trailing comma/invalid syntax.
- Wrong nesting level par server object paste karna.
- Project config ko global samajhna.
- Server restart na karna.
- Tool list mein multiple overlapping browser tools enabled rakhna.
- Unnecessary tools enable karna.

---

# Part 5 — Chrome DevTools MCP

## 5.1 WHY

QA engineer ko browser test karte waqt sirf visible UI nahi dekhna hota. Browser ke paas aur bhi useful evidence hota hai:
- Network requests/responses.
- Console messages/errors.
- Browser state.
- Performance audit information.

Traditional flow mein tester DevTools kholta, errors copy karta, phir AI chat mein paste karta. Chrome DevTools MCP connected AI client ko browser inspection tools provide kar sakta hai.

## 5.2 WHAT: Course ke mutabik

Course mein Chrome DevTools MCP:
- Live Chrome browser ko interact/control/inspect karta hai.
- Puppeteer library ka use karta hai.
- Browser actions perform kar sakta hai.
- Console messages inspect kar sakta hai.
- Network requests read kar sakta hai.
- Performance insights/audits, including Lighthouse audit, run kar sakta hai.

Course setup requirements:
- Chrome browser.
- Node.js.
- Chrome DevTools MCP server configuration.
- AI client mein MCP tools enabled.

## 5.3 Course demonstration — pizza store

Instructor ka flow:

1. VS Code/GitHub Copilot mein Chrome DevTools MCP configure.
2. Configure Tools mein Chrome DevTools tools verify.
3. Built-in browser/Playwright MCP ko temporarily disable kiya, taaki demonstration mein tool conflict na ho.
4. Prompt: Chrome open karke `localhost:3000` par jao.
5. Natural language se theme change karwaya.
6. Website par order place karwaya.
7. Browser ke network requests ka overview manga.
8. Console errors ke baare mein poocha.
9. Lighthouse audit run karwaya.

### QA engineer ko isse kya seekhna chahiye?

| Browser evidence | QA use |
|---|---|
| Network request | UI action ne expected API call ki ya nahi |
| HTTP status | Request successful, client error, server error? |
| Request payload | Correct data backend ko bheja? |
| Response body | API ne expected data diya? |
| Console error | JavaScript/runtime issue? |
| Lighthouse audit | Performance/accessibility/SEO-related signals |

**Important:** Lighthouse audit full QA sign-off nahi hota. Ye specific audit categories ka signal deta hai; functional correctness, security, business rules aur cross-browser testing separately validate karne honge.

## 5.4 Mentor addition — Chrome DevTools MCP ka responsible QA workflow

Suppose checkout button click karne par order create nahi hota.

AI se focused request do:

```text
Inspect the currently open checkout page using the Chrome DevTools tools.

1. Identify the request triggered when I click Place Order.
2. Report the request method, URL, status code and payload fields.
3. Inspect the response body.
4. Check whether the browser console contains relevant errors.
5. Do not retry the order or modify application data.
6. Summarize observations separately from assumptions.
```

Is prompt mein useful controls hain:
- Specific task.
- Evidence requested.
- Side-effect boundary.
- Observations vs assumptions separation.

### Common mistakes

- Network request dekhkar assume karna ki backend data persist ho gaya.
- Sirf status code check karna, response body/business result ignore karna.
- Console warnings ko automatically application bug declare kar dena.
- Lighthouse score ko complete quality measure samajhna.
- MCP ko production environment mein destructive actions karne dena.

## 5.5 Interview answer

**Simple English:**

“Chrome DevTools MCP allows an AI client to interact with and inspect a live Chrome browser. The course demonstrates browser actions, network request inspection, console inspection and Lighthouse audits.”

**Stronger answer:**

“For QA, browser automation is only one part of investigation. Chrome DevTools MCP can help an AI client inspect browser-side evidence such as network requests, console messages and performance audit results. For example, when checkout fails, I can inspect the triggered API request, status, payload and response, then correlate it with console errors. I would still verify the backend state and reproduce the issue independently before reporting a defect.”

**Keywords:** Chrome, Puppeteer, network, console, Lighthouse, browser evidence, investigation.

---

# Part 6 — Playwright MCP

## 6.1 WHY

Agar tum already Playwright test codebase use kar rahe ho, toh natural-language browser interaction ke saath Playwright-specific test generation bhi useful ho sakti hai.

## 6.2 WHAT: Course ka main distinction

Course ke comparison ke mutabik:

| Chrome DevTools MCP | Playwright MCP |
|---|---|
| Live Chrome inspection/control par focus | Browser automation workflow par focus |
| Network, console, performance/Lighthouse insights highlight kiye | Playwright tests generate karna key selling point |
| Specific Playwright test environment required nahi | Playwright ecosystem/codebase mein zyada relevant |
| General browser debugging/investigation | Playwright test creation and execution workflow |

Course ka recommendation:
- Agar Playwright environment/test codebase mein kaam kar rahe ho, Playwright MCP consider karo.
- Agar main requirement general browser interaction/inspection hai, Chrome DevTools MCP useful ho sakta hai.

**Nuance:** Ye course ke demonstrated use cases ka comparison hai, complete feature-by-feature benchmark nahi. Actual capabilities server version ke saath change ho sakti hain.

## 6.3 Course demonstration — natural language to Playwright test

Prerequisite:
- Existing Playwright-configured project.
- Pizza demo app running at `localhost:3000`.
- Playwright MCP configured in VS Code.
- GitHub Copilot tools configuration mein Playwright MCP enabled.

Instructor workflow:

1. Copilot ko Playwright MCP use karke `localhost:3000` open karne ko kaha.
2. AI ne navigation tool invoke kiya.
3. Website open hui.
4. Natural language se theme change karwaya.
5. AI ne browser interaction perform kiya.
6. Prompt diya: “Generate a Playwright test with this workflow.”
7. AI ne Playwright test generate kiya aur execute kiya.
8. Instructor ne assertions add karne ko kaha.
9. AI ne assertions include/uncomment kiye.
10. Test green/pass hua.

**Core takeaway:** Natural-language workflow ko Playwright test code mein convert karna.

## 6.4 Mentor addition — Python + Pytest + Playwright example

Course demonstration Playwright test generation dikhata hai; neeche Python version tumhari stack ke liye mentor adaptation hai.

Suppose natural-language test definition:

```text
Scenario: Change website theme
Given the pizza store home page is open
When the user selects the light theme
Then the page should show the light theme
And the theme toggle should indicate the selected state
```

Possible Python + Pytest + Playwright test skeleton:

```python
from playwright.sync_api import Page, expect


def test_user_can_change_theme(page: Page):
    page.goto("http://localhost:3000")

    theme_button = page.get_by_role(
        "button",
        name="Change theme"
    )

    theme_button.click()

    expect(page.locator("body")).to_have_class("light-theme")
```

**Important:** Ye illustrative adaptation hai. Actual locator name, CSS class, expected theme value tumhare application ke DOM aur implementation par depend karenge. Agar app `data-theme="light"` use karti hai, toh assertion us actual contract ke against honi chahiye. AI ko guessed selectors/assertions blindly accept nahi karne.

### Better test generation prompt

```text
You are assisting with a Python + Pytest + Playwright project.

First inspect the existing project structure, pytest configuration,
fixtures, page objects and locator conventions.

Create a test for this scenario:
[PASTE THE TEST SCENARIO]

Rules:
1. Use the existing project conventions.
2. Reuse existing fixtures and page objects where appropriate.
3. Prefer role/label/test-id locators over brittle XPath.
4. Do not invent selectors or expected values.
5. If required UI details are missing, inspect the page or ask me.
6. Add meaningful assertions for the business outcome.
7. Do not change application code just to make the test pass.
8. Run the focused test and report the exact command and result.
9. Explain every changed file.
```

## 6.5 Generated test ko review kaise karna hai?

| Review area | Questions |
|---|---|
| Requirement | Kya test actual acceptance criteria verify karta hai? |
| Locator | Semantic/stable locator hai? |
| Assertion | Sirf click hua ya actual outcome verify hua? |
| Test isolation | Test independent hai? |
| Test data | Hard-coded data safe/stable hai? |
| Wait strategy | Fixed sleep use toh nahi hua? |
| POM/fixtures | Existing project conventions follow ki? |
| Failure output | Failure par useful evidence milega? |
| Side effects | Test real order/payment/data create toh nahi kar raha? |
| Maintainability | Duplicate logic ya unnecessary complexity toh nahi? |

### Weak vs strong assertion

Weak:

```python
theme_button.click()
```

Ye sirf action perform karta hai; result verify nahi karta.

Stronger (actual app contract ke mutabik):

```python
theme_button.click()
expect(page.locator("body")).to_have_attribute(
    "data-theme",
    "light"
)
```

Assertion ko actual DOM contract ke saath match karna zaroori hai.

## 6.6 Common mistakes

- AI-generated test ko bina read kiye commit kar dena.
- Test pass hone ko test quality ka proof samajhna.
- Generated assertion ka expected value guess kar lena.
- `wait_for_timeout()` se timing problem hide karna.
- Test ko application ke internal implementation se unnecessarily couple karna.
- Har test mein duplicate browser setup karna, existing fixtures ignore karna.
- AI ko application code change karne dena jab requirement sirf test create karna ho.

## 6.7 Interview answer

**Simple English:**

“Playwright MCP lets an AI client interact with a browser and, in the course demonstration, generate Playwright tests from a natural-language workflow. It is especially useful when the project already uses Playwright.”

**Stronger answer:**

“Playwright MCP can bridge natural-language test descriptions and executable Playwright automation. For example, I can describe a user workflow, let the MCP interact with the application, and ask the AI client to generate a Playwright test. In my Python automation work, I would review the generated code against the project’s fixtures, POM structure, locator strategy and acceptance criteria. I would also verify that the assertions validate the business outcome, not merely that an action was performed.”

**Keywords:** Playwright MCP, natural language, browser automation, test generation, assertions, review, Python, Pytest.

---

# Part 7 — AWS Documentation MCP (Optional lesson)

## 7.1 Course coverage

Ye optional lecture un learners ke liye hai jo AWS resources ke saath kaam karte hain.

Course mein:
- AWS MCP servers collection/repository introduce ki gayi.
- AWS documentation MCP server demonstrate kiya.
- AWS MCP configuration mein `uvx` use hota hai.
- `uv`/`uvx` installed hona chahiye.
- MCP server ko VS Code/GitHub Copilot configuration mein add kiya.
- Tools list mein AWS documentation tools verify kiye.
- Example prompt: AWS Lambda ke latest managed runtimes kya hain?
- AI assistant ne AWS documentation search tool use karke response diya.

Course mention karta hai ki AWS ecosystem mein documentation, infrastructure, deployment, CloudFormation etc. ke liye MCP tools available ho sakte hain.

## 7.2 QA/SDET relevance

AWS MCP tumhare liye tab useful hoga jab:
- Test environment AWS par hosted ho.
- Lambda-based backend test karna ho.
- S3, API Gateway, CloudWatch ya deployment configuration samajhni ho.
- Official AWS documentation se current behaviour verify karna ho.

**Mentor addition:** AWS documentation MCP ko pehle read-only documentation lookup ke liye use karo. Infrastructure modification/deployment permissions alag risk category hain.

## 7.3 Interview answer

“The course demonstrates an AWS documentation MCP server that can search AWS documentation through an AI client. It is optional for QA engineers and is useful when testing applications hosted on AWS or investigating AWS service behaviour.”

---

# Part 8 — Chrome DevTools MCP vs Playwright MCP: decision guide

| Situation | Better starting point | Why |
|---|---|---|
| Browser console/network issue investigate karna | Chrome DevTools MCP | Browser inspection evidence |
| Lighthouse audit run karna | Chrome DevTools MCP | Course demonstration includes Lighthouse |
| Existing Playwright test project mein kaam | Playwright MCP | Playwright-oriented workflow |
| Natural-language flow se Playwright test draft | Playwright MCP | Course ka main demonstrated advantage |
| General browser interaction, Playwright codebase nahi | Chrome DevTools MCP | Course recommendation |
| AWS docs lookup | AWS Documentation MCP | AWS documentation tools |

**Remember:** MCP tools ek doosre ka replacement nahi hote. Tumhare task ke hisaab se tool select karo. Ek hi time par multiple browser MCPs enable karne par tool selection/conflict confusing ho sakta hai; course instructor ne demo ke liye overlapping tools disable kiye the.

---

# Part 9 — Practical lab for your Python + Playwright journey

## Lab A — MCP concepts ko explain karna

**Task:** Apne words mein explain karo:
1. Agentic AI.
2. MCP.
3. MCP client.
4. MCP server.
5. Tool.
6. MCP vs normal browser automation.

**Expected outcome:** Tum 2 minutes mein architecture aur use case explain kar sako.

## Lab B — Chrome DevTools investigation

Test app: apna local demo app ya approved test environment.

Scenario:
1. Home page open karo.
2. Ek user action perform karo.
3. Relevant network request identify karo.
4. Method, URL, status, payload aur response note karo.
5. Console errors check karo.
6. Observation aur assumption separate likho.

**Evidence template:**

| Field | Your observation |
|---|---|
| User action | |
| Request method | |
| Endpoint | |
| Status code | |
| Payload | |
| Response | |
| Console error | |
| Expected behaviour | |
| Actual behaviour | |
| Conclusion | |

## Lab C — Playwright MCP se test draft

Natural-language scenario likho:

```text
Scenario: User can search for a pizza

Given the pizza store is open
When the user searches for a valid pizza name
Then matching pizza results should be displayed
And unrelated results should not be displayed
```

AI se test generate karwao, phir manually review karo:
- Locator correct?
- Search action correct?
- Result assertion meaningful?
- No fixed sleep?
- Existing fixtures reused?
- Test data deterministic?
- Test cleanup required?

## Lab D — AI-generated test quality challenge

AI ko deliberately incomplete scenario do:

```text
User clicks Add to Cart.
```

Check karo AI kya missing poochta hai:
- Which product?
- Initial cart state?
- Expected quantity?
- Expected price?
- Cart badge or cart page?
- Duplicate click behaviour?
- Inventory/availability?
- Persistence after reload?

**Learning:** Weak requirements se reliable test nahi ban sakta. AI bhi missing business rules ko magically know nahi karta.

## Lab E — MCP safety review

Kisi MCP server ko install karne se pehle uski documentation/repository inspect karo. Report banao:
- Maintainer.
- Runtime.
- Install command.
- Permissions/tools.
- External systems touched.
- Secrets/environment variables.
- Read-only vs write actions.
- Risks and mitigations.

---

# Part 10 — Module 8 quick revision

## One-line definitions

| Term | Revision |
|---|---|
| Agentic AI | AI workflow that can use tools and perform multi-step actions toward a goal |
| MCP | Open standard for connecting AI applications to external systems |
| MCP server | Component exposing tools/resources through MCP |
| MCP client | AI application that connects to MCP servers |
| `npx` | Node.js package execution tool used by some MCP servers |
| `uvx` | Python tool runner used by some Python MCP servers |
| Chrome DevTools MCP | Browser interaction/inspection; course shows network, console and Lighthouse |
| Playwright MCP | Playwright-oriented browser automation and natural-language test generation |
| AWS Docs MCP | AWS documentation lookup through an AI client |

## 10 questions you should be able to answer

1. Agentic AI aur normal chat AI mein kya difference hai?
2. MCP ko USB-C analogy se kaise explain karoge?
3. MCP client aur MCP server mein kya difference hai?
4. MCP server install karte waqt security checks kya karoge?
5. `npx` aur `uvx` kis ecosystem se related hain?
6. VS Code project MCP config aur user MCP config mein kya difference hai?
7. Chrome DevTools MCP se QA engineer ko kya evidence mil sakta hai?
8. Chrome DevTools MCP aur Playwright MCP ka course-level difference kya hai?
9. Natural-language generated Playwright test ko merge karne se pehle kya review karoge?
10. AWS Documentation MCP QA engineer ke liye kab useful hoga?

---

# Part 11 — Interview practice: answer yourself first

**Q1. What is MCP and why is it useful?**

Expected points:
- Open standard.
- AI application ↔ external systems.
- Reusable standardized integration.
- Tools/resources.
- USB-C analogy.
- Security and permission review.

**Q2. How can AI help in browser testing through MCP?**

Expected points:
- Natural-language browser interaction.
- Browser inspection.
- Network and console evidence.
- Playwright test generation.
- Human review and independent verification.

**Q3. Would you trust an AI-generated Playwright test?**

Expected points:
- Treat as draft.
- Validate requirements.
- Review locators/assertions.
- Check isolation and data.
- Run repeatedly.
- Review code before merge.

**Q4. When would you choose Chrome DevTools MCP over Playwright MCP?**

Expected points:
- General browser investigation.
- Network/console/performance evidence.
- Not necessarily tied to Playwright codebase.
- Playwright MCP for Playwright-centric workflow and test generation.

**Q5. What are the risks of third-party MCP servers?**

Expected points:
- Untrusted code.
- Excessive tool permissions.
- Filesystem/network/secrets access.
- Data exfiltration or unintended changes.
- Verify maintainer/source and permissions.
- Least privilege, isolated environment, approval.

---

# Part 12 — Module progress tracker

| Topic | Status |
|---|---|
| Agentic AI vs non-agentic AI | ⬜ Not started |
| Tool use and AI workflow | ⬜ Not started |
| MCP definition and architecture | ⬜ Not started |
| MCP server discovery and safety | ⬜ Not started |
| Node.js / `npx` / Python / `uvx` | ⬜ Not started |
| Claude Desktop MCP configuration | ⬜ Not started |
| VS Code project/user MCP configuration | ⬜ Not started |
| Chrome DevTools MCP | ⬜ Not started |
| Network/console/Lighthouse investigation | ⬜ Not started |
| Playwright MCP | ⬜ Not started |
| Natural language → Playwright test | ⬜ Not started |
| AWS Documentation MCP (optional) | ⬜ Not started |
| Python adaptation lab | ⬜ Not started |
| Interview answers | ⬜ Not started |

## Mentor assessment rubric

Har topic ko 0–3 score do:

- **0 — Unknown:** concept explain nahi kar pa rahe.
- **1 — Basic:** definition yaad hai, example weak hai.
- **2 — Working:** practical use case explain/perform kar sakte ho.
- **3 — Strong:** trade-offs, risks, debugging aur interview follow-ups handle kar sakte ho.

**Module complete tab maana jayega jab:**
- MCP architecture bina notes explain kar sako.
- Chrome DevTools aur Playwright MCP ka use case choose kar sako.
- AI-generated test ka critical review kar sako.
- MCP permissions/security risks identify kar sako.
- Ek practical investigation ya test-generation lab complete ho.

---

# Final mentor note

Module 8 ka most valuable takeaway “AI se test generate karwana” bhar nahi hai. Real SDET skill ye hai ki tum samjho:

1. AI ko kaunsa context diya ja raha hai.
2. AI ke paas kaunse tools aur permissions hain.
3. Tool se kaunsa evidence mil raha hai.
4. Generated test actual requirement ko verify karta hai ya nahi.
5. Result independently kaise validate karna hai.

**AI tumhari speed badha sakta hai; testing judgement tumhe develop karni hai.**
