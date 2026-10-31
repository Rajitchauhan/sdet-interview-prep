# Lesson 3 --- Adopting the Testing Mindset: MindBridge Lab

`<small>`{=html}Based on the uploaded DOCX lab instructions and supplied
bug-report files \| Difficulty: Easy → Medium \| Estimated study time:
45--75 minutes`</small>`{=html}

## 1. WHY --- Testing mindset ka matlab kya hai?

Tester ka kaam sirf happy path par click karna nahi. Tester ko sochna
hota hai:

-   Normal user flow kaise work karega?
-   Invalid input dene par system kya karega?
-   Boundary values par behavior kya hoga?
-   Application unexpected input ko safely reject karti hai?
-   Defect ko koi doosra person reproduce kar sakta hai?

Is lab ka objective ZIP-code validation defect identify karna aur uska
clear bug report likhna hai.

## 2. Course Source --- Lab overview

Uploaded lab instructions ke mutabik:

-   App: MindBridge
-   Local URL: `http://localhost:3000`
-   Activity type: Ungraded
-   Approximate duration: 15 minutes
-   Scenario: Checkout ke ZIP code field mein invalid alphabetic text
    accept ho raha hai.

### Important limitation

Lab instructions ek Coursera-provided lab desktop aur supporting files
folder assume karti hain. Tumhare ZIP mein instructions, template aur
completed bug report example available hain, lekin actual runnable
MindBridge application aur separate solution key included nahi hain.

Isliye: - Agar tumhare paas lab environment access hai, to instructions
ke according app run karke exercise execute kar sakte ho. - Agar app
access nahi hai, to is lesson ko scenario-based exercise ki tarah
complete karo. Main actual app execute karne ka claim nahi kar raha. -
Solution key ZIP mein missing hai; supplied completed bug report ko
reference example ke roop mein use karo.

## 3. Course Source --- Lab steps

### Step 1: Happy path

Lab instructions mein normal flow:

1.  MindBridge open karo.
2.  Login karo.
3.  Catalog open karo.
4.  Koi course open karo.
5.  Add to cart select karo.
6.  Cart open karo.
7.  Checkout select karo.
8.  Pre-filled valid ZIP `94105` ko unchanged chhodo.
9.  Place order select karo.
10. Confirm karo ki order success page open hota hai.

**Expected working behavior:** Valid sample ZIP ke saath order success
page tak pahunchna.

### Step 2: Edge cases brainstorm karo

Lab instructions ye ZIP values suggest karti hain:

  Test data      Why try it?
  -------------- --------------------
  `testing`      Alphabetic input
  `12`           Too short
  `1234567890`   Too long
  `@#%`          Special characters
  Blank          Missing value

Ye supplied lab ke suggested test inputs hain. Inke expected behavior ko
application requirement ke against validate karna chahiye.

### Step 3: Seeded defect reproduce karo

Lab instructions ke mutabik: 1. Dobara course cart mein add karo. 2.
Checkout par jao. 3. ZIP field mein `testing` enter karo. 4. Place order
select karo. 5. Observe karo ki order accept ho jata hai aur success
page aa jata hai.

**Course-provided expected behavior:** Invalid non-numeric ZIP ko reject
hona chahiye aur clear message dikhna chahiye, jaise "Zip code must
contain only numbers."

**Observed seeded defect (as described by lab):** `testing` ZIP code ke
saath order accept ho jata hai.

## 4. WHAT --- Bug report kya hota hai?

Bug report ek structured record hai jisme defect ko itni clarity se
describe kiya jata hai ki doosra team member issue ko samajh aur
reproduce kar sake.

Uploaded template mein ye sections hain:

-   Bug title
-   Environment details
-   Severity and priority
-   Prerequisites / pre-conditions
-   Steps to reproduce
-   Expected result
-   Actual result
-   Test data / edge case notes
-   Attachments / console logs

## 5. HOW --- Strong bug report kaise likhen?

### 5.1 Title

Title short, specific aur behavior-focused hona chahiye.

Weak: `Checkout bug`

Better: `Checkout accepts alphabetic text in ZIP code field`

### 5.2 Environment details

Record karo: - Application - Environment - Browser - Date/time -
Relevant build/version, if known

Environment detail missing ho to bug reproduce karna difficult ho sakta
hai.

### 5.3 Severity vs Priority

**Uploaded source:** Completed example Severity ko Major aur Priority ko
High set karta hai. Reason: invalid ZIP data order processing database
mein enter ho sakta hai aur shipping/billing fulfillment impact ho sakta
hai.

**Mentor Explanation:** - Severity: defect ka impact/seriousness kitna
hai? - Priority: team ko ise kitni jaldi fix karna chahiye?

Ye simple distinction hai. Actual severity/priority scale company ke
process ke according define hoti hai.

### 5.4 Preconditions

Bug reproduce karne se pehle required conditions: - Application running
ho. - User logged in ho. - Cart mein at least one course ho.

### 5.5 Steps to reproduce

Steps exact aur numbered hone chahiye. Har step mein ek clear action
rakho.

### 5.6 Expected vs Actual

-   Expected: requirement ke mutabik kya hona chahiye tha?
-   Actual: execution ke time kya hua?

Dono ko mix mat karo.

## 6. Course-provided completed bug report --- summarized

Uploaded completed bug report ka core content:

  Field              Supplied example
  ------------------ --------------------------------------------------------------
  Title              Order accepted with invalid text as ZIP code during checkout
  Application        MindBridge
  Environment        Localhost
  Browser            Chrome
  Severity           Major
  Priority           High
  Main input         `testing`
  Expected           Invalid ZIP reject ho aur validation message aaye
  Actual             Order accept ho gaya
  Other edge cases   `12`, `1234567890`, `@#%`, blank

Completed example mein reason diya gaya hai ki invalid ZIP
order-processing data mein enter ho sakta hai aur production
shipping/billing fulfillment ko affect kar sakta hai.

## 7. Practice --- Write your own bug report

Neeche template copy karke apni Markdown file mein fill karo. Ye
uploaded template ke fields ko readable practice format mein arrange
karta hai.

``` markdown
# Bug Report: Checkout accepts alphabetic text in ZIP code field

## Environment Details
- Application: MindBridge
- Environment: Localhost
- Browser: Chrome
- Date/Time: [Add if known]

## Severity & Priority
- Severity: [Your assessment]
- Priority: [Your assessment]
- Reason: [Explain impact and urgency]

## Preconditions
1. Application is running.
2. User is logged in.
3. At least one course is in the cart.

## Steps to Reproduce
1. Open the application.
2. Log in.
3. Open Catalog and add a course to the cart.
4. Open the cart and select Checkout.
5. Enter `testing` in the ZIP code field.
6. Select Place order.

## Expected Result
The application rejects the invalid ZIP code and displays a clear validation message.

## Actual Result
[Write what you observed. If you did not run the app, label this as the behavior described in the supplied lab instructions.]

## Test Data
- testing
- 12
- 1234567890
- @#%
- blank

## Evidence
- Screenshot/video: [Attach if available]
- Console/network logs: [Add only if captured]
```

**Important honesty rule:** Agar tumne app khud run nahi ki, Actual
Result ko apna observed result mat likhna. Clearly mention karo: "As
described in the supplied lab instructions." Real defect report mein
observed facts aur assumptions alag hone chahiye.

## 8. Common mistakes

1.  Title vague rakhna: "Bug in checkout".
2.  Reproduction steps skip karna.
3.  Expected aur Actual result ko combine karna.
4.  Severity ko business impact explain kiye bina assign karna.
5.  Evidence capture nahi karna, jab available ho.
6.  Aisa claim karna ki issue reproduce kiya, jab app run hi nahi ki.
7.  Test data mention na karna.

## 9. Mentor's Additional Knowledge --- Bug report quality checklist

Professional bug report ke liye ye additional checks useful hain:

-   Kya title issue ko identify karta hai?
-   Kya steps kisi new tester ko reproduce karne denge?
-   Kya exact input value record hai?
-   Kya expected behavior requirement se grounded hai?
-   Kya actual behavior observed hai?
-   Kya environment enough detail mein hai?
-   Kya severity ka reason diya hai?
-   Kya screenshot/logs relevant hain, aur kya woh actually capture kiye
    gaye hain?

Ye checklist mentor addition hai; uploaded template ka exact extra
section nahi.

## 10. Interview understanding

### Simple English answer

"A bug report documents a defect with details such as environment, steps
to reproduce, expected result, actual result, severity, priority, and
evidence. A good bug report should be clear and reproducible."

### Stronger answer

"A good defect report helps developers and other team members understand
and reproduce an issue without depending on the original tester. I
include a concise title, environment details, preconditions, exact
reproduction steps, expected and actual results, test data, severity and
priority, and supporting evidence where available. I also make sure that
observed behavior is separated from assumptions."

### Keywords

`Reproducibility` · `Preconditions` · `Steps to reproduce` ·
`Expected result` · `Actual result` · `Severity` · `Priority` ·
`Evidence`

## 11. Practice questions

1.  Happy path aur edge case mein kya difference hai?
2.  ZIP value `testing` kyun useful test data hai?
3.  Expected result aur actual result alag kyun likhte hain?
4.  Severity Major aur Priority High ka reason supplied example mein kya
    hai?
5.  Agar tumne application execute nahi ki, to report mein actual result
    kaise label karoge?
6.  Bug report developer ke liye useful kaise banti hai?

## 12. Lesson completion checklist

-   [ ] Main happy path describe kar sakta hoon.
-   [ ] Main at least 4 ZIP edge cases explain kar sakta hoon.
-   [ ] Main bug report ke major fields explain kar sakta hoon.
-   [ ] Main Expected aur Actual result separate likh sakta hoon.
-   [ ] Main severity aur priority ka difference samajhta hoon.
-   [ ] Main observed result aur source-described result mein difference
    maintain karta hoon.
