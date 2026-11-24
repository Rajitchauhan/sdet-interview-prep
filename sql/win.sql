Tables and schemas
1. monthly_sales
Column	           	Data type
employee_id	   	    INT
month_start	   	    DATE
sales	           	DECIMAL(10,2)

2. employees
Column	        	 Data type
employee_id	 	     INT
employee_name	 	 VARCHAR(100)
department_id	 	 INT
salary	         	 DECIMAL(10,2)

3. users
Column	         	Data type
user_id	         	INT
name	         	VARCHAR(100)
email	         	VARCHAR(150)

4. test_executions
Column	          	Data type
execution_id	  	INT
test_case_id	  	INT
status	          	VARCHAR(20)
duration_seconds	DECIMAL(8,2)
executed_at	   	    DATETIME

Q1. Previous Month Sales

Write a query to display each employee's monthly sales along with 
their previous month's sales.

Requirements:
- Compare records separately for each employee.
- Sort records chronologically.
- Display employee_id, month_start, sales, previous_sales.

sol  - select employee_id, month_start, sales ,
       LAG(sales) OVER(partition by employee_id  order by month_start)
       as previous_sales 
       from monthly_sales

2 - Next Execution Duration

2 - Write a query to display each test execution along with 
the duration of the next execution of the same test case.

Requirements:
- Compare executions separately for each test case.
- Use executed_at to determine execution order.
- Display execution_id, test_case_id, duration_seconds, next_duration.

sol - select execution_id, test_case_id, duration_seconds,
      LEAD(duration_seconds) OVER(partition by test_case_id order by executed_at ) as next_duration
      from test_executions;


Q3. Highest-Paid Employee in Each Department

Write a query to display every employee along with the name
of the highest-paid employee in their department.

Requirements:
- Preserve all employee records.
- Display employee_name, department_id, salary, highest_paid_employee.

sol - select employee_name, department_id, salary,
      first_value(employee_name,) over(partition by department_id order by salary DESC)
       as highest_paid_employee
       from employees ;
      
Lowest-Paid Employee in Each Department

Q4. Write a query to display every employee along with the 
name of the lowest-paid employee in their department.

Requirements:
- Preserve all employee records.
- Display employee_name, department_id, salary, lowest_paid_employee.

sol - select employee_name, department_id, salary,
      first_value(employee_name) over(partition by department_id order by salary ASC)
       as lowest_paid_employee
       from employees ;

Q5. Write a query to find the top 2 highest-paid employees
 from every department.

Requirements:
- Return exactly 2 employees per department wherever possible.
- If salaries are equal, use employee_id as a tie-breaker.
- Display employee_name, department_id, salary.


sol - with rank_employee as (
       select employee_name, department_id, salary , 
       row_number() over(partition by department_id order by salary DESC  
       , employee_id ASC)
      as rnk
     from employees
     )

 select employee_name, department_id, salary 
  from rank_employee 
   where rnk <= 2;


Top 2 Salary Ranks in Each Department

Q6. Write a query to find employees belonging to the 
top 2 salary ranks in each department.

Requirements:
- Employees with equal salaries must receive the same rank.
- Include all employees who fall within the top 2 ranks.
- Display employee_name, department_id, salary, salary_rank.
     
    
sol : WITH ranked_emp AS (
    SELECT 
        employee_name, 
        department_id, 
        salary, 
        DENSE_RANK() OVER(
            PARTITION BY department_id 
            ORDER BY salary DESC
        ) AS salary_rank
    FROM 
        employees
)
SELECT 
    employee_name, 
    department_id, 
    salary, 
    salary_rank
FROM 
    ranked_emp 
WHERE 
    salary_rank <= 2;



Q7. Find Duplicate Email Records

Write a query to identify duplicate email records in the users table.

Requirements:
- Keep the first record based on the lowest user_id.
- Display only subsequent duplicate records.
- Display user_id, name, email.

sol : WITH ranked_users AS (
    SELECT 
        user_id,
        name,
        email,
        ROW_NUMBER() OVER(
            PARTITION BY email 
            ORDER BY user_id ASC
        ) AS rn
    FROM 
        users
)
SELECT 
    user_id, 
    name, 
    email
FROM 
    ranked_users
WHERE 
    rn > 1;