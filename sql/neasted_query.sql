1 - select employee_id , employee_name , salary from employees where salary >
    (select avg(salary) from employees) order by salary DESC;

2 - select employee_name , salary from employees where salary =
(select max(salary) from employees) ;

3 -   select e.employee_id , e.employee_name , d.department_id
      from employees as inner join departments as d
      on e.department_id = d.department_id
      where d.department_name = 'HR' ;

      OR 


3 - select employee_id , employee_name department_id
      from employees where department_id = 
      (select department_id from departments where department_name = 'QA') ;

4 - select employee_name , salary from employees 
    where salary > any
    (select e.salary
    from employees as e inner join deparments as d 
    on e.department_id = d.department_id
    where d.department_name = 'HR') 
    order by salary ASC;

5 - select tc.test_case_id , tc.test_case_name , tc.module
    from test_executions as te left join test_cases as tc 
    on tc.test_case_id = te.test_case_id 
    where te.execution_id is null 
    order by tc.test_case_id ASC ;

6 - select tc.test_case_id,
    tc.test_case_name,
    tc.module
    from test_cases as tc 
    where EXISTS (select 1 from test_executions as te where tc.test_case_id = te.test_case_id) ;

7 - select e.employee_name , e.department_id , e.salary 
    from employees as e where e.salary >
    (select AVG(e2.salary)  from employees as e2 where e.department_id = e2.department_id)  
    order by e.department_id ASC , e.salary DESC ;

8 - select e1.department_id , AVG(e1.salary) as average_salary
    from employees as e1 group by department_id
    having AVG(e1.salary) > (
        select avg(e2.salary) from employees as e2 
    ) 
    order by average_salary DESC;

9 - select employee_name , salary 
    from employees 
    where salary >
    (select MAX(e.salary) from employees as e inner join departments as d on 
    e.department_id = d.department_id where d.department_name = 'QA');

10 - select employee_name , salary 
    from employees 
    where salary >
    (select MIN(e.salary) from employees as e inner join departments as d on 
    e.department_id = d.department_id where d.department_name = 'QA')
    order by salary DESC;

11 - SELECT 
    department_id, 
    AVG(salary) AS average_salary
FROM 
    employees 
GROUP BY 
    department_id 
HAVING 
    AVG(salary) > 55000
order by average_salary DESC;