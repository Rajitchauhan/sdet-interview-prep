# SQL + MySQL Interview Master Notes

## Aggregates • GROUP BY • HAVING • Calculations • CASE • JOINs • Story-based problem solving

> **Goal:** Long interview/HackerRank/LeetCode story ko small
> requirements mein todna, correct tables/joins/filters/grouping
> identify karna, aur independently query likhna.

------------------------------------------------------------------------

# 1. SQL vs MySQL

-   **SQL** relational databases se baat karne ki language/standard hai.
-   **MySQL** database management system hai jo SQL dialect support
    karta hai.
-   `SELECT`, `WHERE`, `JOIN`, `GROUP BY`, `HAVING`, `CASE` largely
    common SQL hain.
-   MySQL-specific syntax ka example: `LIMIT`, `IFNULL()`, `CURDATE()`,
    `NOW()`.
-   MySQL direct `FULL OUTER JOIN` support nahi karta; `LEFT JOIN` +
    unmatched right rows + `UNION ALL` se emulate karte hain.

  Task                 MySQL syntax
  -------------------- -------------------------------------------------
  First 10 rows        `LIMIT 10`
  Skip 20, return 10   `LIMIT 10 OFFSET 20`
  NULL fallback        `IFNULL(col, 0)` or portable `COALESCE(col, 0)`
  Current date/time    `CURDATE()`, `NOW()`
  Join strings         `CONCAT(first_name, ' ', last_name)`
  Full outer join      LEFT JOIN + unmatched rows + UNION ALL

Interview mein "SQL" bola ho to core SQL likho. Platform MySQL ho to
dialect ke differences dhyan mein rakho.

------------------------------------------------------------------------

# 2. Aggregate functions

Aggregate function multiple rows ko summarize karke ek value deta hai.

Example `employees`:

    employee_id employee_name     department_id   salary
  ------------- --------------- --------------- --------
              1 Suman                        10    60000
              2 Amit                         20    70000
              3 Ravi                         10    60000
              4 Pooja                        10    65000
              5 Karan                        20    70000
              6 Mohan                        30    45000
              7 Priya                        10    50000
              8 Neeraj                     NULL    40000

## COUNT

``` sql
SELECT COUNT(*) AS total_rows FROM employees;
SELECT COUNT(department_id) AS assigned_department_count FROM employees;
SELECT COUNT(DISTINCT department_id) AS unique_department_count FROM employees;
```

-   `COUNT(*)`: all rows count karta hai, NULL values hone par bhi.
-   `COUNT(column)`: sirf non-NULL values count karta hai.
-   `COUNT(DISTINCT column)`: unique non-NULL values count karta hai.

**LEFT JOIN tip:** Parent ke child records count karne ke liye child
table ka non-NULL primary key count karo, e.g. `COUNT(e.employee_id)`.
`COUNT(*)` unmatched parent row ko bhi 1 count kar sakta hai.

## SUM, AVG, MIN, MAX

``` sql
SELECT SUM(salary) AS total_salary,
       AVG(salary) AS average_salary,
       MIN(salary) AS min_salary,
       MAX(salary) AS max_salary
FROM employees;
```

-   `SUM`: total.
-   `AVG`: average of non-NULL values.
-   `MIN`/`MAX`: lowest/highest non-NULL value.
-   NULL values generally aggregate calculations mein ignore hoti hain.
-   `AVG(salary)` ko `SUM(salary)/COUNT(*)` se blindly replace mat karo;
    NULL salary ke case mein denominator galat ho sakta hai.

------------------------------------------------------------------------

# 3. GROUP BY

`GROUP BY` same value/combination wali rows ko groups mein divide karta
hai, phir har group ka aggregate calculate hota hai.

Question: department-wise employee count.

``` sql
SELECT department_id,
       COUNT(*) AS employee_count
FROM employees
GROUP BY department_id;
```

Multiple grouping columns:

``` sql
SELECT department_id, city, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id, city;
```

Har unique `(department_id, city)` pair ek group hai.

## GROUP BY + SELECT rule

SELECT mein: - grouping columns allowed, - aggregate expressions
allowed, - arbitrary non-grouped columns avoid karo.

Risky/invalid:

``` sql
SELECT department_id, employee_name, AVG(salary)
FROM employees
GROUP BY department_id;
```

Ek department mein multiple names ho sakte hain. Kaunsa name show hoga?
MySQL ke `ONLY_FULL_GROUP_BY` mode mein query reject ho sakti hai.
Random result par depend mat karo.

JOIN ke saath grouping karte waqt ID aur name dono group karna robust
hai:

``` sql
GROUP BY d.department_id, d.department_name
```

------------------------------------------------------------------------

# 4. WHERE vs HAVING

  WHERE                              HAVING
  ---------------------------------- ----------------------------
  Individual rows filter karta hai   Groups filter karta hai
  GROUP BY se pehle logically        GROUP BY ke baad logically
  `salary > 50000`                   `COUNT(*) > 2`

Only employees with salary above 50000, then department count:

``` sql
SELECT department_id, COUNT(*) AS employee_count
FROM employees
WHERE salary > 50000
GROUP BY department_id;
```

Departments having more than 2 employees:

``` sql
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 2;
```

Dono saath:

``` sql
SELECT department_id, COUNT(*) AS qualifying_count
FROM employees
WHERE salary > 50000
GROUP BY department_id
HAVING COUNT(*) >= 2;
```

**Trick:** "Employees whose..." usually WHERE. "Departments having more
than..." usually HAVING. "At least 5" = `>= 5`; "more than 5" = `> 5`.

Aggregate ko same query level ke WHERE mein directly use nahi karte,
kyunki WHERE grouping se pehle apply hota hai.

------------------------------------------------------------------------

# 5. SQL logical execution order

Query likhne ka order aur logical processing order alag hain.

``` sql
SELECT department_id, COUNT(*) AS employee_count
FROM employees
WHERE salary > 50000
GROUP BY department_id
HAVING COUNT(*) >= 2
ORDER BY employee_count DESC
LIMIT 5;
```

Logical order: 1. FROM 2. JOIN / ON 3. WHERE 4. GROUP BY 5. HAVING 6.
SELECT 7. DISTINCT 8. ORDER BY 9. LIMIT

Optimizer physical execution ko reorder kar sakta hai; ye logical
understanding ke liye hai.

MySQL mein SELECT alias ko ORDER BY mein use kar sakte ho:

``` sql
SELECT COUNT(*) AS employee_count
FROM employees
ORDER BY employee_count;
```

Same SELECT level ke WHERE mein alias par rely mat karo. Original
expression use karo.

------------------------------------------------------------------------

# 6. Calculations

Arithmetic operators: `+`, `-`, `*`, `/`, `%`.

Annual salary:

``` sql
SELECT employee_name, salary, salary * 12 AS annual_salary
FROM employees;
```

Percentage formula:

`percentage = (part / total) * 100`

QA pass percentage:

``` sql
SELECT
  100.0 * SUM(CASE WHEN status = 'PASS' THEN 1 ELSE 0 END)
  / NULLIF(COUNT(*), 0) AS pass_percentage
FROM test_executions;
```

Failure rate:

``` sql
SELECT
  100.0 * SUM(CASE WHEN status = 'FAIL' THEN 1 ELSE 0 END)
  / NULLIF(COUNT(*), 0) AS failure_rate
FROM test_executions;
```

-   `100.0` decimal calculation encourage karta hai; integer
    division/truncation se bachne mein help.
-   `NULLIF(denominator, 0)` zero ko NULL bana deta hai, divide-by-zero
    avoid hota hai.
-   Empty input par percentage NULL ho sakti hai; requirement ke hisaab
    se handle karo.

Calculation solve karne se pehle identify: 1. Numerator kya hai? 2.
Denominator kya hai? 3. Unit kya hai? 4. NULL values ka effect? 5.
Denominator zero ho sakta hai? 6. Decimal precision chahiye?

------------------------------------------------------------------------

# 7. CASE WHEN ... THEN ... ELSE ... END

`CASE` SQL ka if/else expression hai.

``` sql
SELECT employee_name, salary,
       CASE
         WHEN salary >= 60000 THEN 'High'
         WHEN salary >= 45000 THEN 'Medium'
         ELSE 'Low'
       END AS salary_category
FROM employees;
```

Conditions top-to-bottom check hoti hain. Pehli TRUE condition ka result
return hota hai. Isliye higher/specific threshold pehle rakho.

Simple CASE exact value match ke liye:

``` sql
SELECT status,
       CASE status
         WHEN 'PASS' THEN 'Successful'
         WHEN 'FAIL' THEN 'Failed'
         WHEN 'SKIPPED' THEN 'Not executed'
         ELSE 'Unknown'
       END AS status_label
FROM test_executions;
```

## Conditional aggregation

Har module ke PASS/FAIL counts:

``` sql
SELECT tc.module,
       COUNT(*) AS total_executions,
       SUM(CASE WHEN te.status = 'PASS' THEN 1 ELSE 0 END) AS pass_count,
       SUM(CASE WHEN te.status = 'FAIL' THEN 1 ELSE 0 END) AS fail_count,
       SUM(CASE WHEN te.status = 'SKIPPED' THEN 1 ELSE 0 END) AS skipped_count
FROM test_cases tc
INNER JOIN test_executions te
  ON tc.test_case_id = te.test_case_id
GROUP BY tc.module;
```

Kaise kaam karta hai: - CASE har row par condition check karta hai. -
Matching row ko 1, non-matching ko 0. - SUM saare 1 add karta hai. -
GROUP BY har module ke liye separate result banata hai.

Ek hi result mein multiple categories ke counts chahiye → conditional
aggregation. Sirf FAIL rows count karni hain → simple
`WHERE status='FAIL'` + `COUNT(*)` bhi sufficient.

MySQL shortcut `SUM(status = 'PASS')` bhi possible hai because boolean
expression 1/0 deta hai, lekin portable/readable interview answer ke
liye `SUM(CASE...)` prefer karo.

CASE ko SUM/AVG ke saath use kar sakte ho:

``` sql
SELECT department_id,
       SUM(CASE WHEN salary >= 60000 THEN salary ELSE 0 END) AS high_salary_total,
       AVG(CASE WHEN salary >= 60000 THEN salary END) AS avg_high_salary
FROM employees
GROUP BY department_id;
```

AVG mein ELSE omitted hai to non-matching rows NULL hongi, aur AVG NULL
ignore karta hai.

------------------------------------------------------------------------

# 8. NULL handling

NULL unknown/missing value hai. `= NULL` nahi likhte.

``` sql
WHERE department_id IS NULL
WHERE department_id IS NOT NULL
```

NULL fallback:

``` sql
SELECT COALESCE(department_id, 0) FROM employees;
```

MySQL:

``` sql
SELECT IFNULL(department_id, 0) FROM employees;
```

`COALESCE` standard SQL; `IFNULL` MySQL function. NULL ko 0 tabhi banao
jab business meaning valid ho. Missing department aur department ID 0
same cheez nahi zaroori.

------------------------------------------------------------------------

# 9. JOIN fundamentals

Example `departments`:

    department_id department_name
  --------------- -----------------
               10 QA
               20 HR
               30 Development
               40 Support
               50 Finance

Employees table upar diya hai.

## INNER JOIN

Sirf matching rows:

``` sql
SELECT e.employee_name, d.department_name
FROM employees e
INNER JOIN departments d
  ON e.department_id = d.department_id;
```

Neeraj (NULL department) aur empty departments result mein nahi aayenge.

## LEFT JOIN

Left table ki all rows preserve:

``` sql
SELECT e.employee_name, d.department_name
FROM employees e
LEFT JOIN departments d
  ON e.department_id = d.department_id;
```

All employees chahiye → employees left side. No match par right-side
columns NULL.

## RIGHT JOIN

Right table ki all rows preserve:

``` sql
SELECT d.department_name, e.employee_name
FROM employees e
RIGHT JOIN departments d
  ON e.department_id = d.department_id;
```

All departments chahiye. Equivalent readable LEFT JOIN:

``` sql
SELECT d.department_name, e.employee_name
FROM departments d
LEFT JOIN employees e
  ON d.department_id = e.department_id;
```

**Rule:** "All X" bola hai to X ko usually FROM ke baad left side rakho
and LEFT JOIN use karo.

## JOIN cardinality / duplicate rows

-   One-to-one: one matching row each side.
-   One-to-many: one department → many employees.
-   Many-to-many: bridge table ke through multiple matches.

JOIN mein duplicates hamesha error nahi. Ek parent ke 5 children hon to
parent 5 result rows mein aa sakta hai. "Each parent once" requirement
ho to EXISTS, DISTINCT ya GROUP BY consider karo.

------------------------------------------------------------------------

# 10. ON vs WHERE --- critical LEFT JOIN concept

`ON` batata hai right-side row kis condition par match hogi. `WHERE`
final joined rows filter karta hai.

INNER JOIN mein simple filters ON/WHERE mein often same result de sakte
hain. LEFT JOIN mein difference critical hai.

Requirement: every department show karo, but employee details only if
salary \> 55000.

Correct:

``` sql
SELECT d.department_name, e.employee_name, e.salary
FROM departments d
LEFT JOIN employees e
  ON d.department_id = e.department_id
 AND e.salary > 55000;
```

Agar salary condition WHERE mein hogi:

``` sql
SELECT d.department_name, e.employee_name, e.salary
FROM departments d
LEFT JOIN employees e
  ON d.department_id = e.department_id
WHERE e.salary > 55000;
```

To unmatched department rows mein `e.salary` NULL hoga; WHERE unhe
remove kar dega. Support/Finance disappear ho jayenge.

**Memory trick:** - ON = matching rule. - WHERE = final rows filter. -
All left rows preserve karne hain aur right table par qualifying
condition hai → condition ON mein rakhne par غور karo.

------------------------------------------------------------------------

# 11. JOIN + GROUP BY + aggregates

All departments including zero employee count:

``` sql
SELECT d.department_id,
       d.department_name,
       COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e
  ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
ORDER BY employee_count DESC;
```

Why `COUNT(e.employee_id)`? Empty department ke liye LEFT JOIN ek row
deta hai jahan employee columns NULL. `COUNT(*)` 1 count kar sakta hai;
`COUNT(e.employee_id)` 0 dega.

Average and max salary:

``` sql
SELECT d.department_name,
       AVG(e.salary) AS avg_salary,
       MAX(e.salary) AS max_salary
FROM departments d
LEFT JOIN employees e
  ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name;
```

Empty department ke liye AVG/MAX NULL expected hai.

------------------------------------------------------------------------

# 12. Multiple JOINs

QA tables: - `test_cases(test_case_id, test_case_name, module)` -
`test_executions(execution_id, test_case_id, status, executed_by)` -
`employees(employee_id, employee_name, ...)`

Execution + test case + executor:

``` sql
SELECT te.execution_id, tc.test_case_name, te.status,
       e.employee_name AS executed_by
FROM test_executions te
INNER JOIN test_cases tc
  ON te.test_case_id = tc.test_case_id
INNER JOIN employees e
  ON te.executed_by = e.employee_id;
```

Har JOIN condition separately identify karo: foreign key → referenced
primary key.

------------------------------------------------------------------------

# 13. SELF JOIN

Same table ko different roles mein join karna.

Employee-manager:

``` sql
SELECT e.employee_name AS employee,
       m.employee_name AS manager
FROM employees e
LEFT JOIN employees m
  ON e.manager_id = m.employee_id;
```

**Tumhari direction confusion ka fix:** `e` employee hai, `m` manager
hai. Employee row ka `manager_id`, manager row ke `employee_id` ko point
karta hai. Correct condition: `e.manager_id = m.employee_id`. Reverse
condition alag relationship check karegi.

Only employees with a manager:

``` sql
SELECT e.employee_name, m.employee_name AS manager
FROM employees e
INNER JOIN employees m
  ON e.manager_id = m.employee_id;
```

Same department unique pairs:

``` sql
SELECT e1.employee_name AS employee_1,
       e2.employee_name AS employee_2,
       e1.department_id
FROM employees e1
INNER JOIN employees e2
  ON e1.department_id = e2.department_id
 AND e1.employee_id < e2.employee_id;
```

`<` self-pair aur reverse duplicate pair dono rokta hai.

Same salary pairs:

``` sql
SELECT e1.employee_name, e2.employee_name,
       e1.salary, e2.salary
FROM employees e1
INNER JOIN employees e2
  ON e1.salary = e2.salary
 AND e1.employee_id < e2.employee_id;
```

------------------------------------------------------------------------

# 14. ANTI JOIN --- no matching record

Employees jinka matching department record nahi:

``` sql
SELECT e.employee_id, e.employee_name, e.department_id
FROM employees e
LEFT JOIN departments d
  ON e.department_id = d.department_id
WHERE d.department_id IS NULL;
```

Important distinction: - `e.department_id IS NULL` = employee ke paas
department ID missing. - `d.department_id IS NULL` after LEFT JOIN =
department table mein matching row nahi mili.

`NOT EXISTS` alternative:

``` sql
SELECT e.employee_id, e.employee_name
FROM employees e
WHERE NOT EXISTS (
  SELECT 1
  FROM departments d
  WHERE d.department_id = e.department_id
);
```

------------------------------------------------------------------------

# 15. SEMI JOIN / EXISTS

Question: test cases with at least one execution, each test case once.

``` sql
SELECT tc.test_case_id, tc.test_case_name, tc.module
FROM test_cases tc
WHERE EXISTS (
  SELECT 1
  FROM test_executions te
  WHERE te.test_case_id = tc.test_case_id
);
```

EXISTS check karta hai ki subquery at least one row return karti hai ya
nahi. `SELECT 1` convention hai; selected value important nahi.

-   Related table ke columns output chahiye → JOIN.
-   Sirf related row exists check karna hai → EXISTS.
-   Parent once chahiye → EXISTS naturally child matches ki wajah se
    parent duplicate nahi karta.
-   INNER JOIN multiple child rows ke liye parent repeat kar sakta hai.

------------------------------------------------------------------------

# 16. NON-EQUI JOIN / range join

Equality ke bajay range condition par matching.

`salary_grades(grade, min_salary, max_salary)`:

  grade     min_salary   max_salary
  ------- ------------ ------------
  A              60000       100000
  B              40000        59999
  C              20000        39999

``` sql
SELECT e.employee_name, e.salary, g.grade
FROM employees e
INNER JOIN salary_grades g
  ON e.salary BETWEEN g.min_salary AND g.max_salary;
```

`BETWEEN` inclusive hai, lower aur upper bound dono include. Salary
ranges overlap nahi karni chahiye aur gaps nahi hone chahiye.

Question clue: "falls within range", "salary band", "between minimum and
maximum", "effective date range" → non-equi/range JOIN socho.

------------------------------------------------------------------------

# 17. CROSS JOIN

Har left row ko har right row ke saath combine karta hai.

``` sql
SELECT b.browser_name, env.environment_name
FROM browsers b
CROSS JOIN environments env;
```

3 browsers × 3 environments = 9 rows. Use case: browser-environment test
matrix, all products × all dates. Missing JOIN condition accidentally
Cartesian product create kar sakti hai; CROSS JOIN intentional hona
chahiye.

------------------------------------------------------------------------

# 18. FULL OUTER JOIN in MySQL

FULL OUTER JOIN conceptually both tables ke all rows preserve karta hai:
matches + unmatched left + unmatched right.

MySQL direct FULL OUTER JOIN support nahi karta. Workaround:

``` sql
-- All employees and matching departments
SELECT e.employee_id, e.employee_name,
       e.department_id, d.department_name
FROM employees e
LEFT JOIN departments d
  ON e.department_id = d.department_id

UNION ALL

-- Only departments with no employee
SELECT e.employee_id, e.employee_name,
       d.department_id, d.department_name
FROM employees e
RIGHT JOIN departments d
  ON e.department_id = d.department_id
WHERE e.employee_id IS NULL;
```

First half: all employees + matches. Second half: only unmatched
departments. `UNION ALL` duplicates remove nahi karta, but second half
anti-match hone ke kaaran matched rows repeat nahi hoti.

Interview answer: "MySQL does not support FULL OUTER JOIN directly. I
emulate it with a LEFT JOIN plus unmatched rows from the other table
using UNION ALL."

## UNION vs UNION ALL

-   `UNION` duplicates remove karta hai.
-   `UNION ALL` duplicates preserve karta hai; generally
    duplicate-elimination work nahi.
-   Both SELECTs mein same number of columns and compatible types/order
    hone chahiye.
-   Output column names first SELECT se aate hain.

------------------------------------------------------------------------

# 19. Story-based SQL question decoding method

Long question ko ek baar mein solve karne ki koshish mat karo. Seven
steps follow karo.

## Step 1 --- One-line requirement

Paragraph ko apni language mein short karo: - Har department ka employee
count. - Aise test cases jinki execution nahi hui. - Har employee aur
manager ka naam. - Har browser-environment combination.

## Step 2 --- Output columns identify karo

Question ke "return/display/show" part se exact output list banao. Ye
SELECT list hai.

## Step 3 --- Main entity identify karo

Question kis entity ki list maang raha hai: employees, departments, test
cases, executions, pairs, combinations?

"All", "every", "including those with no..." words preserve-all clue
hain.

## Step 4 --- Relationships map karo

Examples: - `employees.department_id = departments.department_id` -
`test_executions.test_case_id = test_cases.test_case_id` -
`test_executions.executed_by = employees.employee_id` -
employee-manager: `e.manager_id = m.employee_id`

Foreign key → referenced key likh lo before JOIN.

## Step 5 --- Story phrase ko SQL operation mein translate karo

  Phrase                      SQL thought
  --------------------------- --------------------------------------------
  total/how many              COUNT
  total amount                SUM
  average                     AVG
  highest/lowest              MAX/MIN
  for each/per                GROUP BY
  groups having more than     HAVING
  only rows where             WHERE
  including zero/no child     LEFT JOIN preserve parent
  without/never/no matching   ANTI JOIN / NOT EXISTS
  at least one                EXISTS
  each once                   duplicates check; EXISTS/DISTINCT/GROUP BY
  between min and max         BETWEEN / range JOIN
  all combinations            CROSS JOIN
  same table relationship     SELF JOIN
  percentage/rate             numerator / denominator × 100
  top N                       ORDER BY + LIMIT

## Step 6 --- Query skeleton

``` sql
SELECT ...
FROM ...
JOIN ...
  ON ...
WHERE ...
GROUP BY ...
HAVING ...
ORDER BY ...
LIMIT ...;
```

Har clause mandatory nahi. Sirf requirement ke hisaab se use karo.

## Step 7 --- Edge-case verification

-   unmatched rows aani chahiye?
-   one-to-many join duplicates dega?
-   aggregate correct group par hai?
-   WHERE ne NULL-extended rows delete to nahi ki?
-   "at least" inclusive hai?
-   NULL compare kaise ho raha?
-   exact requested columns hain?

------------------------------------------------------------------------

# 20. Story ko decode karne ka worked example

Prompt:

"Report every department and the number of employees assigned to it.
Departments with no employees must also appear. Sort from highest
employee count to lowest."

Decode: - Tables: departments + employees - Output: department name +
count - "Every department" → all departments preserve - "Number" →
COUNT - "No employees must also appear" → LEFT JOIN - "Per department" →
GROUP BY - Highest to lowest → ORDER BY DESC

``` sql
SELECT d.department_name,
       COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e
  ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
ORDER BY employee_count DESC;
```

Paragraph ko 6 clues mein tod diya. Isi tarah har story solve karni hai.

------------------------------------------------------------------------

# 21. Boundary words --- exact interpretation

  English phrase          SQL
  ----------------------- ---------------------------------
  At least 5              `>= 5`
  More than 5             `> 5`
  At most 5               `<= 5`
  Less than 5             `< 5`
  Exactly 5               `= 5`
  Between 10 and 20       `BETWEEN 10 AND 20` (inclusive)
  Not equal               `<>` or `!=`
  No more than            `<=`
  Greater than or equal   `>=`

"At least five" ko `> 5` likhne se exactly 5 wale records miss ho jaate
hain. Tumhari practice mein ye boundary mistake hui thi.

------------------------------------------------------------------------

# 22. HackerRank / LeetCode workflow

1.  **First read:** broad task samjho.
2.  **Second read:** output columns identify karo.
3.  **Third read:** constraints, NULLs, duplicates, sorting, ties.
4.  Schema padho: primary key, foreign key, nullable columns.
5.  Sample input/output dekho.
6.  One-line requirement likho.
7.  Query skeleton banao.
8.  Edge cases test karo.

Sample output clues: - Same ID multiple times → one-to-many join
possible. - Every parent with NULL child → outer join. - Parent once
despite multiple child records → EXISTS/DISTINCT/GROUP BY. - One row per
category → GROUP BY. - No child rows → anti-join. - All combinations →
CROSS JOIN.

## Mind blank ho to ye likho

``` text
1. Output kya hai?
2. Main table kaunsi hai?
3. Relationship/foreign key kya hai?
4. All rows, only matches, ya missing matches?
5. Row filter hai ya group filter?
6. Calculation kya hai?
7. Duplicates/NULL ka risk?
8. Sort/limit?
```

------------------------------------------------------------------------

# 23. Tumhari observed mistakes/confusions --- targeted fixes

## A. "All employees" vs "all departments"

Tumne kabhi all departments ke liye RIGHT JOIN use kiya, jabki easier
approach departments ko left rakhna tha.

-   All employees → `FROM employees e LEFT JOIN departments d`
-   All departments → `FROM departments d LEFT JOIN employees e`

## B. "No matching department" mein wrong NULL check

Wrong for unmatched department record:

``` sql
WHERE e.department_id IS NULL
```

Correct:

``` sql
WHERE d.department_id IS NULL
```

Left side NULL means employee ID missing; right side key NULL after LEFT
JOIN means no matching department row.

## C. SELF JOIN direction reverse

Correct:

``` sql
ON e.manager_id = m.employee_id
```

Employee row ka manager_id manager ki employee_id ko refer karta hai.

## D. LEFT JOIN condition WHERE mein rakh dena

All departments retain karne hain, only qualifying employees match karne
hain:

``` sql
ON d.department_id = e.department_id
AND e.salary > 55000
```

## E. GROUP BY miss karna

"Department-wise count/average" → GROUP BY department. Aggregate plus
non-aggregate output columns ka grouping rule follow karo.

## F. COUNT(\*) vs COUNT(child_id)

LEFT JOIN empty department ke liye `COUNT(*)` 1 ho sakta hai. Use
`COUNT(e.employee_id)`.

## G. "At least" vs "more than"

At least = `>=`; more than = `>`.

## H. EXISTS vs JOIN

Related columns output chahiye → JOIN. Sirf existence check → EXISTS.
"Each test case once" mein JOIN multiplication check karo.

## I. Naming and syntax slips

Practice mein table/column spelling (`departments`, `joining_date`),
singular/plural, alias spelling aur ORDER BY/GROUP BY miss hue. Final
schema scan zaroor karo.

------------------------------------------------------------------------

# 24. Interview answers --- explain your reasoning

**GROUP BY:** "I use GROUP BY when the requirement asks for an aggregate
at a particular level, such as department-wise employee count. WHERE
filters rows before grouping, while HAVING filters aggregated groups."

**WHERE vs HAVING:** "WHERE filters individual rows before aggregation.
HAVING filters groups after GROUP BY, for example groups whose COUNT is
greater than five."

**LEFT JOIN:** "LEFT JOIN preserves every row from the left table and
returns matching right-side data. If there is no match, right-side
columns are NULL."

**ON vs WHERE:** "ON defines matching conditions. WHERE filters the
final joined result. Moving a right-table filter from ON to WHERE can
remove unmatched left-side rows."

\*\*COUNT(\*) vs COUNT(column):\*\* "COUNT(\*) counts rows.
COUNT(column) counts non-NULL values. After a LEFT JOIN, I count the
child table's non-null primary key to get zero for parents without
children."

**EXISTS:** "I use EXISTS when I only need to check whether a related
row exists and don't need columns from that table. It avoids duplicate
parent rows from multiple child matches."

**MySQL FULL OUTER JOIN:** "MySQL doesn't support FULL OUTER JOIN
directly. I emulate it using LEFT JOIN and unmatched rows from the other
table with UNION ALL."

------------------------------------------------------------------------

# 25. Debugging checklist

  -----------------------------------------------------------------------
  Symptom                             Check
  ----------------------------------- -----------------------------------
  Too many rows                       One-to-many multiplication? Missing
                                      join condition?

  Too few rows                        INNER instead of LEFT? WHERE
                                      removed NULL rows? Wrong key?

  Wrong count                         COUNT(\*) vs COUNT(child_id)?
                                      Duplicate join rows?

  Wrong average                       Wrong denominator? NULLs? Join
                                      duplicates?

  Missing categories                  Parent table preserved? Filter
                                      accidentally in WHERE?

  Duplicate pairs                     SELF JOIN mein `id1 < id2` missing?

  No rows                             Wrong key direction? Wrong literal?
                                      NULL comparison with `=`?

  Unexpected NULL                     No match, or aggregate had no
                                      non-NULL values?

  Syntax error                        Column/table spelling, comma,
                                      alias, parentheses, clause order?
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 26. One-page cheat sheet

  ----------------------------------------------------------------------------------
  Requirement                         Pattern
  ----------------------------------- ----------------------------------------------
  All rows count                      `COUNT(*)`

  Non-NULL count                      `COUNT(col)`

  Unique count                        `COUNT(DISTINCT col)`

  Total / average                     `SUM()` / `AVG()`

  Highest / lowest                    `MAX()` / `MIN()`

  Per group                           `GROUP BY`

  Filter rows                         `WHERE`

  Filter groups                       `HAVING`

  If/else                             `CASE WHEN ... THEN ... ELSE ... END`

  Conditional category count          `SUM(CASE WHEN ... THEN 1 ELSE 0 END)`

  Only matching                       `INNER JOIN`

  Preserve left                       `LEFT JOIN`

  No matching                         `LEFT JOIN ... WHERE right_pk IS NULL` /
                                      `NOT EXISTS`

  At least one                        `EXISTS`

  Same table relationship             SELF JOIN

  Range match                         `BETWEEN`

  All combinations                    `CROSS JOIN`

  MySQL full outer equivalent         LEFT JOIN + unmatched right rows + UNION ALL

  Percentage                          `100.0 * numerator / NULLIF(denominator, 0)`

  Top N in MySQL                      `ORDER BY ... LIMIT N`
  ----------------------------------------------------------------------------------

------------------------------------------------------------------------

# 27. Practice kaise karni hai --- independent solving ladder

**Round 1: Decode only.** Query mat likho. Output, main table,
relationships, all-vs-match-vs-missing, aggregate, filters identify
karo.

**Round 2: Skeleton.** FROM/JOIN/ON/WHERE/GROUP BY/HAVING likho.

**Round 3: Full query.** SELECT expressions, aliases, sorting, limit
complete karo.

**Round 4: Explain aloud.** 60 seconds mein batao JOIN kyun, ON kyun,
GROUP BY kis level par, WHERE/HAVING kyun, duplicates/NULL kaise handle
hue.

**Round 5: Edge cases.** Zero child rows, multiple child rows, NULL
foreign key, exact threshold, empty input, duplicate values test karo.

Mastery tab mark karo jab bina hint ke query likho, result shape explain
karo aur edge cases reason kar sako. Hint ke baad corrected query
learning hai, lekin independent mastery ka proof nahi.

------------------------------------------------------------------------

## Final reminder

Tumhara repeated challenge sirf SQL syntax nahi tha; long requirement se
important clues extract karna, preserved table choose karna, NULL kis
side check karna, SELF JOIN direction, ON vs WHERE aur aggregate ke
saath GROUP BY lagana tha. Ye sab repeatable patterns hain. Har question
ko ek saath solve karne ki zaroorat nahi---pehle output, main entity,
relationship, filters, grouping/calculation aur edge cases identify
karo. Phir query build karo.
