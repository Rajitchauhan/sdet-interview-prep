employees
employee_id	employee_name	department_id	salary	manager_id
        1	        Suman	            10	60000	  NULL
        2	        Amit	            20	70000	  1
        3	        Ravi	            10	60000	  1
        4	        Pooja	            10	65000	  2
        5	        Karan	            20	70000	  2
        6	        Mohan	            30	45000	  NULL
        7	        Priya	            10	50000	  1
        8	        Neeraj	          NULL	40000	  2



departments
department_id	department_name
            10	    QA
            20	    HR
            30	    Development
            40	    Support
            50	    Finance



Table: test_cases
test_case_id	test_case_name	    module
        101	        Login Test	    Authentication
        102	        Logout Test	    Authentication
        103	        Payment Test	Payment
        104	        Search Test	    Product
        105	        Cart Test	    Product
        106	        Profile Test	User

Table: test_executions
execution_id	test_case_id	status	executed_by
            1	    101	        PASS	1
            2	    101	        FAIL	2
            3	    102	        PASS	1
            4	    103	        FAIL	3
            5	    103	        PASS	2
            6	    104	        PASS	1
            7	    104	        FAIL	3
            8	    999	        FAIL	2



1 - select e.employee_id , e.employee_name , d.department_name 
    from employees as e left join deparments as d
    on e.department_id = d.department_id
    order by e.employee_name ASC ;

2 - select d.department_name , e.employee_name , e.salary
    from departments (isme ye samjh nih aya current employee ka means kya hai sirf matching chaiye to inner  nhi to right join use karunga pahle doubts clear hone do and mene questions english mai bola tha jaise interview puche jate hai)

2 - select d.department_name , e.employee_name , e.salary 
    from employees as e inner join departments as d 
    on e.department_id = d.department_id
    order by d.department_name ASC ;

3 - select d.department_name , count(e.employee_id) as total_emp
    from deparments as d left join employees as e
    on d.department_id = e.department_id
    group by d.department_name
    order by total_emp DESC ;

4 - select e.employee_id , e.employee_name , d.department_name 
    from employees as e left join deparments as d
    on e.department_id = d.department_id
    where e.department_id IS NULL ;

4 - SELECT
    e.employee_id,
    e.employee_name,
    e.department_id
    FROM employees AS e
    LEFT JOIN departments AS d
        ON e.department_id = d.department_id
    WHERE d.department_id IS NULL;

5 - select emp.employee_name  as  employee_name , mgr.employee_name as manager_name
    from employees as emp left join employees mgr 
    on emp.manager_id = mgr.employee_id


6 - select d.department_id , d.department_name
    from departments as d left join employees as e 
    on d.department_id = e.department_id 
    where d.employee_name iS NULL; (mujhe ek doubts hai yaha d.employee_name , e.employee_name same hai agar mene tables join kiya hai ? and mujhe employee chahiye jo null hai to e.employee_name ya d.employee_name sahi hai and kyu ye abhi thoda aur bhi confused)

6 - select d.department_id , d.department_name
    from departments as d left join employees as e 
    on d.department_id = e.department_id 
    where e.employee_name iS NULL;

7 - select tc.test_case_id , tc.test_case_name , tc.module
    from test_cases as tc left join test_executions as te 
    on tc.test_case_id = te.test_case_id
    where te.execution_id is NULL ;
 OR
    select tc.test_case_id , tc.test_case_name , tc.module
    from test_cases as tc
    where NOT EXISTS (
        select 1 from test_executions as te 
        where tc.test_case_id = te.test_case_id
     ) ;


8 - select tc.test_case_id , tc.test_case_name , tc.module
    from test_cases as tc
      where EXISTS (
        select 1 from test_executions as te 
        where tc.test_case_id = te.test_case_id
     ) ;
    // isme simple inner join nlagane ki soch rha hu mai , plz batana agar mai kuch miss kar rha hu to .
   

9 - select  d.department_name , e.employee_name , e.salary 
    from departments as d left join employees as e 
    on d.department_id = e.department_id
    and e.salary > 55000
    order by d.department_name ASC ; 

10 - select e.employee_name , d.employee_name , d.department_id
     from employees as e inner join employees as d
     on e.department_id = d.department_id
     and e.employee_id < d.employee_id

11 - SELECT
    d.department_name,
    COUNT(e.employee_id) AS total_emp,
    AVG(e.salary) AS avg_salary,
    MAX(e.salary) AS max_salary
FROM departments AS d
LEFT JOIN employees AS e
    ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
ORDER BY avg_salary DESC;

12 - select e1.employee_name , e1.salary  , e2.employee_name , e2.salary
     from employees as e1 inner join employees e2
     on e1.salary = e2.salary 
     and e1.employee_id < e2.employee_id
13 - full join use hoga bss  , mysql mai left join + right join with union all koi specific conditions nhi hai sirf match vali tab tum mujhe dikhna puri query

14 - ab aage mujhe nhi pata lagat hai revision karna padega ya dobara dekhna padega 