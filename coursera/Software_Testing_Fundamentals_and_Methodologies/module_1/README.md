# Module 1 --- Testing Foundations

> **A Hinglish study course built from the Coursera resources you
> uploaded, with clearly separated mentor explanations and practical
> application.**

## Welcome

Ye repository tumhari personal QA / Software Testing study course hai.
Iska goal sirf definitions ya interview answers yaad karna nahi hai.
Goal hai tester ki tarah sochna, product ko systematically evaluate
karna, defects identify karna aur unhe clearly communicate karna.

### Source boundary --- please read

Maine tumhare ZIP ke available resources inspect kiye. Is ZIP mein ye
topics/materials hain:

-   Quality Assurance (QA), Quality Control (QC), User Acceptance
    Testing (UAT)
-   QA vs QC practical scenario
-   RACI matrix
-   ISTQB ke seven fundamental testing principles
-   MindBridge checkout testing mindset lab
-   Bug report template aur completed bug report example
-   Videos ke subtitles aur detailed transcripts, jinmein slide/visual
    descriptions bhi hain

**Important gap:** ZIP ke naam mein "map testing and web layers" likha
hai, lekin actual files mein Web Application Layers ka dedicated
lesson/reading nahi mila. Isliye is repository mein Web Application
Layers ko completed course content nahi bataya gaya. Jab tak source nahi
milta, us topic ko pending rakhenge.

**Assignment limitation:** Lab instructions mein
`Bug_Report_Solution_Key.md` compare karne ko kaha gaya hai, lekin
solution key ZIP mein included nahi hai. Tumne bataya hai ki assignment
download nahi kar sakte. Koi problem nahi---hum available lab
instructions aur supplied completed bug-report example se exercise
karenge. Missing solution key ko pretend karke reproduce nahi kiya gaya
hai.

## How to study this repository

Recommended order:

1.  `01-qa-qc-uat-and-raci.md` --- QA, QC, UAT aur RACI samjho.
2.  `02-seven-fundamental-testing-principles.md` --- seven principles ko
    examples ke saath deeply samjho.
3.  `03-testing-mindset-lab-and-bug-report.md` --- MindBridge lab ko
    available instructions ke basis par mentally/practically complete
    karo.
4.  `04-module-1-study-plan-and-progress.md` --- tasks, revision aur
    progress track karo.

Har topic mein ye distinction maintain kiya gaya hai:

-   **Course Source:** Uploaded course material kya kehta hai.
-   **Mentor Explanation:** Wahi idea simple Hinglish mein.
-   **Project Application:** Tum apne testing/Playwright practice mein
    kaise apply karoge.
-   **Mentor's Additional Knowledge:** Relevant extra explanation jo
    uploaded source ka direct claim nahi hai.

## Lesson format

Har lesson ko is flow mein padho:

1.  WHY --- ye concept kyun zaroori hai?
2.  WHAT --- concept ka meaning kya hai?
3.  HOW --- real work mein kaise use hota hai?
4.  Example --- simple example.
5.  Practical application --- MindBridge ya apne automation project mein
    use.
6.  Common mistakes --- beginners kahan confuse hote hain?
7.  Interview understanding --- short answer aur key points.
8.  Practice --- khud se answer ya task complete karo.

## Suggested GitHub repository structure

``` text
qa-engineering-learning/
├── README.md
└── Module-01-Testing-Foundations/
    ├── README.md
    ├── 01-qa-qc-uat-and-raci.md
    ├── 02-seven-fundamental-testing-principles.md
    ├── 03-testing-mindset-lab-and-bug-report.md
    └── 04-module-1-study-plan-and-progress.md
```

Tum in files ko isi structure mein GitHub par upload kar sakte ho. Abhi
ye Module 1 ka available-material version hai; baad mein next modules ke
notes isi style mein add honge.

## Source inventory and audit

  -----------------------------------------------------------------------
  Uploaded resource                   Use in this course
  ----------------------------------- -----------------------------------
  Fundamental testing principles.txt  Seven principles lesson

  Two subtitle TXT files              QA/QC/UAT and QA-vs-QC video
                                      content

  Two VTT subtitle files              Timing and spoken-content
                                      cross-check

  Two detailed-transcript PDFs        Video visuals, slide text and
                                      diagrams

  Adopting the Testing Mindset DOCX   MindBridge lab steps and success
                                      checklist

  Bug Report Template (two copies)    Bug report format; files are
                                      duplicates

  Completed Bug Report Markdown       Reference example for expected
                                      report quality
  -----------------------------------------------------------------------

### Source notes and limitations

-   The two bug-report template files are duplicates; one template is
    enough.
-   The lab instructions refer to a separate solution-key file, but it
    was not included in the ZIP.
-   The RACI video transcript has an ambiguity in the "Write test cases"
    example. The spoken narration says the QC engineer is responsible
    for hands-on execution and the QA Lead is responsible for overall
    test quality. The visual transcript lists the QA Lead as Responsible
    and the Developer as Informed, without clearly showing all role
    assignments. This discrepancy is flagged in Lesson 1 rather than
    silently resolved.
-   The UAT video calls UAT the last phase before go-live. That is the
    course's simplified framing. In real projects, UAT timing and
    release workflows can vary; see the clearly marked mentor note in
    Lesson 1.

## Completion standard

Module 1 tab complete mark karne se pehle tumhe bina notes dekhe:

-   QA, QC aur UAT ka difference explain karna aana chahiye.
-   RACI ke R, A, C, I ka meaning aur ek example dena aana chahiye.
-   Seven testing principles ko apne words mein explain karna aana
    chahiye.
-   MindBridge ZIP-code defect ke reproducible bug report likhni aani
    chahiye.
-   Ye samajhna chahiye ki passing tests ka matlab defect-free ya
    user-satisfied product prove hona nahi hai.

**Mentor rule:** Agar concept samajh nahi aaya, hum next topic par rush
nahi karenge. Pehle example, discussion aur practice se clarity build
karenge.
