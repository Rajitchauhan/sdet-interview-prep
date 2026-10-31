# Module 12 — Running Local LLMs with Ollama
## Ollama Installation, Model Selection, Claude Code & GitHub Copilot Integration
### Complete Hinglish Study Guide | QA Automation / SDET | Local AI Workflows

> **Module ka central idea:** Cloud-based AI assistant ke alawa tum apne computer par Large Language Model (LLM) download karke locally run kar sakte ho. Course mein Ollama ke through local model install kiya gaya, phir us model ko Claude Code aur VS Code + GitHub Copilot ke saath integrate karke use kiya gaya.

---

## 0. ZIP inspection and source coverage

Uploaded ZIP mein:
- 5 transcript `.txt` files.
- 5 matching English subtitle `.vtt` files.
- Transcript/subtitle pairs same lecture content ko represent karte hain; duplicate content ko consolidate kiya gaya.

### Lessons covered in source

| Lesson | Course source mein covered |
|---|---|
| 1 | Local LLMs ka introduction; privacy, offline use, cost and hardware trade-off |
| 2 | Ollama download/install; terminal verification; `ollama list` |
| 3 | Ollama model library; model features/variants; hardware-based model selection; pull and run a Qwen model |
| 4 | Ollama ke through Claude Code mein local model use karna |
| 5 | Ollama ke through VS Code + GitHub Copilot mein local model use karna |

**Source boundary / important caveats:**
- Intro lecture mein Ollama aur LM Studio dono ka naam aata hai, lekin practical walkthrough Ollama ka hai. LM Studio installation/use ka hands-on is ZIP mein nahi hai.
- Transcript speech-to-text mein product names kuch jagah “Olama”, “Cloud Code”, “Quen” likhe gaye hain. Context ke hisaab se guide standard product spellings **Ollama**, **Claude Code**, aur **Qwen** use karti hai. Ye transcription normalization hai, extra course feature nahi.
- Course demonstration mein Qwen 3.5 family aur 9B variant ka example hai. Model availability, tags, sizes, features aur compatibility time ke saath change hote hain.
- Course instructor kehta hai ki local model private/offline ho sakta hai aur free to run, lekin actual hardware, electricity, storage, licensing and setup costs ko bhi consider karna chahiye. “Free” ka matlab zero total cost nahi.
- Exact commands current Ollama documentation ke against verify karna; course recording-time instructions ko universal/current guarantee mat samajhna.

---

# Part 1 — Local LLM kya hai?

## 1.1 WHY: Local LLM ki zaroorat kyun?

Normally jab tum cloud AI assistant use karte ho, tumhara prompt/context internet ke through provider ke service infrastructure tak ja sakta hai.

Agar tum sensitive QA work kar rahe ho, jaise:
- Internal application code.
- Private API specifications.
- Customer-related test data.
- Internal logs.
- Unreleased product requirements.
- Proprietary test framework.

Toh data handling aur privacy important concern hai.

Local LLM ka idea hai model ko apne computer par run karna, taaki inference tumhari local machine par ho sake.

## 1.2 WHAT: Local LLM

**Simple definition:** Local LLM ek large language model hai jo remote hosted AI service ke bajay tumhare local computer par execute hota hai.

Course ke mutabik local model ke main advantages:

1. **Privacy:** Prompt/context ko remote model API par bhejne ki zaroorat nahi hoti, jab workflow fully local ho.
2. **Offline access:** Model download hone ke baad local inference internet ke bina bhi possible ho sakta hai.
3. **Subscription cost avoidance:** Local model run karne ke liye per-prompt cloud subscription ki requirement nahi hoti.
4. **Control:** User apne hardware par model choose/download/run kar sakta hai.

### Important nuance: local ka matlab automatically secure nahi

Local model ka use privacy improve kar sakta hai, lekin:
- Local files aur prompts tumhare computer par stored ho sakte hain.
- Extensions/IDE plugins alag se network access kar sakte hain.
- Logs ya telemetry settings matter kar sakti hain.
- Model license/usage terms still apply.
- Malware/unsafe downloaded model files ka risk ho sakta hai.

Isliye “local = completely secure” assume nahi karna.

## 1.3 Local LLM ka major disadvantage: hardware

Course instructor ka central warning:
- Powerful models ko run karne ke liye significant computing resources chahiye.
- RAM important hai.
- GPU/video card especially important ho sakta hai.
- Model download ho jana aur smoothly run hona do different things hain.
- Weak hardware par response slow ho sakta hai; ek prompt ka response minutes le sakta hai.

### Course ka trade-off

| Local LLM | Cloud AI |
|---|---|
| Data local process ho sakta hai | Prompt/context provider infrastructure tak ja sakta hai |
| Offline use possible | Internet/service access usually required |
| Model download/storage required | Local model download generally required nahi |
| Hardware performance par depend | Provider-side compute use hota hai |
| Subscription avoid ho sakti hai | Subscription/API cost ho sakti hai |
| Setup/model selection user manage karta hai | Provider model infrastructure manage karta hai |

**Source nuance:** Ye broad conceptual comparison hai. Har cloud provider ki data policy aur har local setup ka behaviour different ho sakta hai.

## 1.4 QA/SDET mein local LLM ka use

Local model se tum experiment kar sakte ho:
- Python test code explain karwana.
- Test case drafts banwana.
- Local repository ka code summarize karwana.
- Test logs ko analyze karwana.
- API request/response examples explain karwana.
- Playwright locator suggestions lena.

Lekin model ki coding/reasoning quality, context window, speed aur tool integration model/hardware par depend karegi.

---

# Part 2 — Ollama kya hai?

## 2.1 Course ka explanation

Course Ollama ko ek tool/platform ke roop mein introduce karta hai jisse:
- Models download/pull kar sakte hain.
- Local machine par models run kar sakte hain.
- Terminal se model manage kar sakte hain.
- Ollama app ke through model select karke chat kar sakte hain.
- Supported integrations ke through Claude Code, VS Code and other coding tools se connect kar sakte hain.

Course intro mein LM Studio ka bhi naam hai, lekin actual practical lessons Ollama par focus karte hain.

## 2.2 Ollama install karna — course workflow

Instructor:
1. Ollama website ke download section par jaata hai.
2. Windows/Linux/Mac platform select karta hai.
3. Windows installer download karta hai.
4. Installer run karta hai.
5. Installation ke baad terminal open karta hai.
6. `ollama` command run karke check karta hai ki command recognized hai ya nahi.
7. `ollama list` se downloaded models verify karta hai.

Course recording mein Windows installer roughly 2 GB ka bataya gaya tha. Ye recording-time observation hai; current installer size change ho sakta hai.

### Course commands

```bash
ollama
```

Purpose: CLI command available hai ya nahi verify/help entry point check karna.

```bash
ollama list
```

Purpose: Locally available/downloaded models list karna.

### Agar command not found aaye

Course instructor suggest karta hai:
- Terminal restart karo.
- Zaroorat pade toh computer restart karo.
- Phir command retry karo.

**Mentor addition:** Installation path/PATH environment variable aur installer completion bhi verify karo. Error message ke exact output ko inspect karo; har command-not-found issue ka reason restart hi nahi hota.

---

# Part 3 — Model choose karna

## 3.1 WHY: Sabse bada model download karna best kyun nahi?

Model size aur capability ke beech trade-off hota hai:
- Larger parameter count generally more compute/storage demand karta hai.
- Model family ke different variants different hardware needs rakhte hain.
- Tumhara GPU/RAM sufficient na ho toh response slow ya unusable ho sakta hai.

Course ka key message: **Model select karne se pehle apne hardware ko consider karo.**

## 3.2 Model library mein kya dekhna hai?

Course instructor Ollama model library open karta hai aur model page par:
- Model family.
- Variants/parameter sizes.
- Supported features.
- Model download size/variant.
- Cloud availability indicator.

Transcript mein Qwen 3.5 family ka example hai. Course recording ke waqt instructor ne approximately 5.7 million downloads ka mention kiya; ye historical recording-time figure hai, current popularity count nahi.

## 3.3 Parameters ka basic concept

Course examples:
- 0.8B parameters.
- 2B parameters.
- 9B parameters.

`B` means billion parameters.

**Basic intuition:** Parameter count model ke learned weights ki quantity ko describe karta hai. Larger parameter model often more compute and memory demand kar sakta hai, but parameter count alone model quality ka complete measure nahi.

Model selection mein ye bhi matter karte hain:
- Quantization.
- Context length.
- Model architecture.
- Supported capabilities.
- Runtime/hardware compatibility.
- Task performance.

Ye additional technical context hai; course lecture ka main focus hardware vs model size tha.

## 3.4 Course ka hardware-based selection approach

Instructor unsure hai ki apne computer par kaunsa model run kar sakta hai.

Woh apne system specifications AI assistant ko deta hai aur poochta hai:

> “What Ollama models can I run with these specifications?”

Assistant:
- Suitable models ki list suggest karta hai.
- General-purpose model vs coding/reasoning model compare karta hai.
- Hardware ke according options batata hai.

**Important:** AI recommendation ko starting point samjho, benchmark nahi. Actual local performance test karke verify karo.

### Hardware assessment checklist — mentor addition

Model download se pehle note karo:
- Operating system.
- CPU.
- Total RAM.
- GPU model.
- Dedicated GPU VRAM.
- Available disk space.
- Intended task: chat, code generation, reasoning, tool use.
- Acceptable response latency.

Agar GPU available nahi hai, toh smaller/quantized model try karna practical ho sakta hai; exact performance machine par depend karegi.

## 3.5 Course example: Qwen 3.5 9B

Instructor:
1. Qwen 3.5 family choose karta hai.
2. 9 billion parameter variant select karta hai.
3. Model ka exact identifier copy karta hai.
4. Terminal mein `ollama pull` ke saath model identifier run karta hai.
5. Download complete hone ka wait karta hai.
6. `ollama list` se verify karta hai.
7. `ollama run` se model start karta hai.
8. `hello how are you` prompt deta hai.
9. Local model response receive hota hai.

### Commands — course example

```bash
ollama pull qwen3.5:9b
```

```bash
ollama list
```

```bash
ollama run qwen3.5:9b
```

**Command caveat:** Ye course transcript se normalized illustrative tag hai. Current Ollama library mein exact model name/tag verify karo; model tags update/retire ho sakte hain.

Interactive session exit karne ke liye course instructor `Ctrl+C` ya `/bye` use karta hai.

## 3.6 Ollama desktop app

Course instructor:
- Ollama app open karta hai.
- Model select karta hai.
- Chat interface mein prompt enter karta hai.
- Downloaded local Qwen model se response receive karta hai.

Course note: App mein cloud models bhi listed ho sakte hain. Agar goal local/offline inference hai, toh confirm karo ki selected model local downloaded model hai, cloud-hosted option nahi.

---

# Part 4 — Claude Code ke saath local Ollama model

## 4.1 WHY

Tum Claude Code ko terminal-based coding assistant ke roop mein use karte ho. Course dikhata hai ki Ollama ke integration ke through Claude Code ko local model ke saath launch kiya ja sakta hai.

## 4.2 Course prerequisites

- Ollama installed.
- Desired model locally pulled/downloaded.
- Claude Code installed.
- Terminal available.

## 4.3 Course workflow

1. Ollama documentation ka integrations section open karo.
2. Claude Code integration instructions read karo.
3. VS Code embedded terminal open karo.
4. `ollama launch claude` command run karo.
5. Available/recommended models list mein se downloaded local model select karo.
6. Qwen 3.5 local model choose karo.
7. Claude Code terminal session start hota hai.
8. Prompt example: `Explain package.json`.
9. Local model project file ka explanation deta hai.

### Course ka important limitation

Recording ke waqt:
- Local model Claude Code ke terminal workflow se accessible tha.
- VS Code ke Claude Code extension/chat interface ke model selector mein local model visible nahi tha.
- Instructor kehta hai ki future implementation mein ye change ho sakta hai.

**Do not generalize this limitation to current versions.** Current Ollama/Claude Code integration docs check karo; support may have changed.

## 4.4 QA use case

Example prompts:
- “Explain this pytest fixture.”
- “Review this Playwright locator strategy.”
- “Summarize this test failure log.”
- “Suggest edge cases for this API schema.”

Local model ko project context dene se pehle:
- Sensitive files exclude/avoid karo if unnecessary.
- Secrets `.env`/credentials expose mat karo.
- Model output independently verify karo.

---

# Part 5 — VS Code + GitHub Copilot ke saath local Ollama model

## 5.1 Course prerequisites

Course ke mutabik:
- Ollama installed.
- VS Code installed.
- GitHub Copilot extension.
- GitHub Copilot Chat extension.
- Desired local model downloaded.

## 5.2 Course workflow

1. Ollama integrations documentation open karo.
2. VS Code + GitHub Copilot section select karo.
3. Terminal open karo.
4. `ollama launch vscode` command run karo.
5. Ollama downloaded model select karta hai / model choose karne deta hai.
6. VS Code launch hota hai.
7. GitHub Copilot Chat model selector open karo.
8. Local Qwen model ek new model option ke roop mein visible hota hai.
9. Project file open karo.
10. Prompt: “Tell me about this file.”
11. Copilot Chat local model se file explanation receive karta hai.

### Course commands

```bash
ollama launch vscode
```

**Caveat:** Exact launch command and support depend on current Ollama integration version. Current official documentation verify karo before running.

## 5.3 Course ka key takeaway

Course demonstration mein local model:
- VS Code ke GitHub Copilot Chat model selector mein available hota hai.
- Project file ka context le sakta hai.
- Structured explanation generate karta hai.

## 5.4 QA workflow example

Open a local test file, then ask:
- Explain this test.
- Identify missing assertions.
- Suggest negative test cases.
- Explain this fixture scope.
- Summarize the failure output.

**Mentor addition:** Generated code ko blindly accept mat karo. Local model ki quality selected model/quantization/hardware par depend karegi; especially complex reasoning and test architecture mein output review karo.

---

# Part 6 — Ollama, Claude Code and Copilot: course comparison

| Area | Ollama + Claude Code | Ollama + VS Code/GitHub Copilot |
|---|---|---|
| Launch flow in course | `ollama launch claude` | `ollama launch vscode` |
| Interface demonstrated | Terminal-based Claude Code | VS Code Copilot Chat |
| Model selection | Terminal launch/model selection | VS Code model selector |
| Demo prompt | Explain `package.json` | Explain an open project file |
| Course limitation | Local model not shown in Claude Code extension selector at recording time | Local model appeared in Copilot Chat selector |

These are recording-time observations, not a permanent product comparison.

---

# Part 7 — QA/SDET practical applications

This module is about running local LLMs and integrating them with coding assistants. The following are mentor-suggested QA applications, not separate course demonstrations.

## 7.1 Python code explanation

Prompt:
```text
Explain this Python test file.
Describe:
1. Fixtures used.
2. Test setup and teardown.
3. Assertions.
4. External dependencies.
5. Potential test isolation problems.
Do not modify the code.
```

## 7.2 Playwright test review

```text
Review this Playwright test for:
- Locator stability
- Assertion quality
- Fixed waits
- Test independence
- Test data
- Cleanup

Do not rewrite the test unless I ask.
Separate confirmed issues from suggestions.
```

## 7.3 API test design

```text
Review this API endpoint schema and suggest:
- Positive cases
- Missing required fields
- Invalid data types
- Boundary values
- Authentication/authorization cases

Do not invent undocumented business rules.
```

## 7.4 Test log summary

```text
Summarize this pytest failure log.
Return:
1. Failed test name
2. Exception/assertion
3. Relevant stack trace
4. Confirmed observations
5. Possible causes (label as hypotheses)
6. Next debugging steps
Do not claim the root cause unless the evidence supports it.
```

---

# Part 8 — Common mistakes and troubleshooting

| Mistake | Why it happens | What to check |
|---|---|---|
| `ollama` command not found | Installation/PATH/terminal issue | Installer, PATH, restart terminal |
| `ollama list` empty | No model downloaded | Pull a model |
| Model download succeeds but inference is slow | Hardware/model size mismatch | RAM, GPU/VRAM, model variant |
| Disk space runs out | Model files are large | Available storage and model size |
| Wrong model selected in app | Cloud and local options mixed | Confirm selected model is local |
| Claude Code local model not available | Integration/client version or launch flow | Current Ollama integration docs |
| Copilot model selector doesn't show local model | Extension/version/configuration mismatch | VS Code, Copilot Chat and Ollama versions |
| Model gives weak code | Model capability/context limits | Try smaller task, stronger suitable model, verify manually |
| Local model still sends data externally | Other extension/tool may use network | Inspect integration architecture/settings |
| Sensitive secrets appear in prompts | Project context includes secret files | Exclude `.env`, tokens, credentials |

---

# Part 9 — Practical lab

## Lab A — Ollama installation verification

1. Install Ollama using the current official installer.
2. Open a fresh terminal.
3. Run `ollama`.
4. Run `ollama list`.
5. Record the output.
6. Note current version and available disk space.

## Lab B — Model selection

Record your hardware:

| Hardware item | Your machine |
|---|---|
| OS | |
| CPU | |
| RAM | |
| GPU | |
| VRAM | |
| Free disk space | |

Then:
1. Select a model suitable for your hardware.
2. Pull it.
3. Run it locally.
4. Ask a simple question.
5. Ask it to explain a small Python file.
6. Record response time and quality.

## Lab C — Claude Code integration

If current supported integration is available:
1. Confirm Claude Code is installed.
2. Follow current Ollama integration instructions.
3. Launch local model.
4. Ask it to explain a `pytest` test file.
5. Verify whether the answer reflects the actual source.

## Lab D — VS Code + Copilot integration

If current supported integration is available:
1. Install/update required extensions.
2. Follow current Ollama VS Code integration instructions.
3. Launch VS Code through the documented flow.
4. Check model selector.
5. Select local model.
6. Ask it to explain an open Python test file.
7. Compare with cloud model output if you have access.

## Lab E — Local vs cloud model comparison

Use the same task and prompt for both models.

| Metric | Local model | Cloud model |
|---|---|---|
| Response time | | |
| Correctness | | |
| Code quality | | |
| Test coverage suggestions | | |
| Context handling | | |
| Privacy/data path | | |
| Cost | | |

Don't assume the local model is better simply because it is private, or that the cloud model is better simply because it is larger. Evaluate the task outcome.

---

# Part 10 — Interview preparation

## Q1. What is a local LLM?

**Simple English:**

“A local LLM is a language model that runs on a user's own computer instead of relying entirely on a remotely hosted AI service.”

**Stronger answer:**

“A local LLM can process prompts and project context on local hardware, which can help with privacy and offline access. The trade-off is that performance depends on local CPU, RAM and GPU resources. Model size and quantization also affect speed and memory requirements. I would choose a model based on the task and hardware, then validate its output rather than assuming local models perform like hosted models.”

## Q2. What is Ollama?

“Ollama is a tool used in the course to download, manage and run language models locally, and to integrate those models with supported coding tools.”

## Q3. What are the advantages of local LLMs?

- Local processing can improve privacy.
- Offline use may be possible.
- Can avoid recurring hosted-model subscription charges.
- User can choose and manage models.

## Q4. What are the limitations?

- Hardware requirements.
- RAM/GPU/VRAM constraints.
- Storage for model downloads.
- Slower inference on weaker machines.
- Model quality/capabilities vary.
- Setup and maintenance responsibility.

## Q5. How did the course use Ollama with Claude Code?

“The course used the Ollama launch integration to start Claude Code with a locally downloaded model. The instructor selected a local Qwen model and asked it to explain a project file.”

## Q6. How did the course use Ollama with GitHub Copilot?

“The course launched VS Code through Ollama, then selected the local model from the GitHub Copilot Chat model selector and asked it to explain an open project file.”

## Q7. Would you use a local LLM for QA automation?

“Yes, for tasks such as explaining local test code, drafting test scenarios or summarizing logs, provided the model is capable enough. I would verify its suggestions with actual requirements and test execution. I would also ensure that the surrounding tools do not unexpectedly transmit sensitive data externally.”

---

# Part 11 — Module 12 quick revision

| Concept | One-line revision |
|---|---|
| Local LLM | Model runs on local computer |
| Ollama | Tool to download/manage/run local models |
| `ollama list` | Lists locally available models |
| `ollama pull` | Downloads a model |
| `ollama run` | Starts a model session |
| Model parameters | Learned weights count; larger models can require more compute |
| Hardware | RAM, GPU/VRAM, CPU and disk affect local inference |
| Claude Code integration | Course uses `ollama launch claude` |
| VS Code integration | Course uses `ollama launch vscode` |
| Local model advantage | Privacy/offline potential |
| Local model trade-off | Hardware and performance constraints |
| LM Studio | Mentioned in intro; no detailed practical demo in this module |

## 12 questions — notes band karke answer karo

1. Local LLM kya hai?
2. Local LLM ka privacy advantage kya hai?
3. Local model ke major hardware requirements kya hain?
4. Ollama ka role kya hai?
5. `ollama list`, `ollama pull`, `ollama run` mein difference?
6. Model parameters mein 9B ka kya meaning hai?
7. Largest model download karna hamesha best kyun nahi?
8. Hardware specifications ke basis par model kaise select karoge?
9. Course ne Claude Code ko local model se kaise launch kiya?
10. Course ne GitHub Copilot ko local model se kaise connect kiya?
11. Local model run hone ka matlab complete system offline hai, kya ye always true hai?
12. QA engineer local LLM ka use kaise kar sakta hai, aur output verify kaise karega?

---

# Part 12 — Module progress tracker

| Topic | Status |
|---|---|
| Local LLM concept | ⬜ |
| Privacy/offline/cost advantages | ⬜ |
| Hardware trade-offs | ⬜ |
| Ollama installation | ⬜ |
| Terminal verification | ⬜ |
| `ollama list` | ⬜ |
| Model library and variants | ⬜ |
| Hardware-based model selection | ⬜ |
| Pull and run a local model | ⬜ |
| Ollama desktop app | ⬜ |
| Claude Code integration | ⬜ |
| VS Code + Copilot integration | ⬜ |
| Local model QA use cases | ⬜ |
| Local vs cloud comparison | ⬜ |
| Practical labs | ⬜ |
| Interview answers | ⬜ |

### Mentor scoring rubric

- **0 — Unknown:** Local LLM/Ollama explain nahi kar pa rahe.
- **1 — Basic:** Advantages/disadvantages aur commands samajh aate hain.
- **2 — Working:** Model install/run karke coding assistant se use kar sakte ho.
- **3 — Strong:** Hardware selection, privacy boundaries, integration trade-offs aur QA use cases evaluate kar sakte ho.

**Module complete tab maana jayega jab tum Ollama par suitable model run kar sako, ek supported coding tool ke saath integrate kar sako, aur local model ke output ko independently evaluate kar sako.**

---

# Final mentor note

Module 12 ka lesson ye nahi ki local model cloud AI ko completely replace kar dega.

Actual takeaway:
1. Local LLM privacy/offline workflows ke liye useful ho sakta hai.
2. Model selection hardware ke according honi chahiye.
3. Ollama model download/run/manage karne ka tool hai.
4. Course ne Claude Code aur VS Code + GitHub Copilot integrations demonstrate ki.
5. Local model ki coding/reasoning quality verify karni hoti hai.
6. Local inference ka matlab automatically every connected tool offline/private nahi hota.

**QA/SDET ke liye:** Local LLM ko ek optional productivity tool samjho. Tumhari core value requirements samajhna, test design karna, reliable automation likhna aur evidence ke basis par defects identify karna hi rahegi.
