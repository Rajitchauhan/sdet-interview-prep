1 - select e.employee_name, d.department_name from employees AS e inner join departments AS d on e.department_id  = d.department_id ;

2 - select e.employee_name , e.salary , d.department_name from employees AS e inner join departments AS d
  on e.department_id = d.department_id where d.department_name = 'QA' ; 

3 - select e.employee_name , e.salary , d.department_name from employees AS e inner join departments AS d
  on e.department_id = d.department_id where e.salary > 55000 order by salary DESC; 

4 - select e.employee_name , e.salary , d.department_name from employees AS e inner join departments AS d
  on e.department_id = d.department_id order by e,employee_name ASC e.salary DESC; (doubts kya group by use hoga but QA ke group karne pe name maange hai to sayad nhi use hoga)

5 - select e.employee_id , e.employee_name , e.salary , d.department_name from employees AS e inner join departments AS d
  on e.department_id = d.department_id where d.department_name = 'QA' OR d.department_name = "Development" ;

6 - select d.department_name , count(e.employee_name) AS total_emp_in_dprt , AVG(e.salary) AS avg_salary 
from employees AS e inner join departments AS d
  on e.department_id = d.department_id 
  group by d.department_name having AVG(e.salary) > 55000 
  order by avg_salary DESC ;

-- LEFT JOIN

1 - select e.employee_name , e.salary , d.department_name from employees AS e left join deparments AS d
     on e.department_id = d.department_id  order by e.employee_name ASC ;

2 - select   d.department_name, e.employee_name from deparments AS d left join employees AS e
     on e.department_id = d.department_id  order by d.department_name ASC ;

3 - SELECT e.employee_id, e.employee_name, d.department_name
FROM employees AS e
LEFT JOIN departments AS d
ON e.department_id = d.department_id
WHERE d.department_name IS NULL;

4 - select  d.department_name, count(e.employee_id) as total_emp  from deparments AS d left join employees AS e
     on e.department_id = d.department_id group by d.department_name  order by total_emp DESC;

5 - select  d.department_name, e.employee_name  , e.salary from deparments AS d left join employees AS e
     on e.department_id = d.department_id and e.salary > 55000  order by d.department_name ASC;

6 - select d.department_name , count(e.employee_id) AS total_emp , AVG(e.salary) AS avg_salary from deparments AS d left join employees AS e
     on e.department_id = d.department_id 
     GROUP BY 
    d.department_name
ORDER BY 
    avg_salary DESC;


-- Right JOIN

1 - select  d.department_name , e.employee_name from employees as e right join deparments as d on 
     e.department_id = d.department_id order by d.department_name ASC;

2 - select  d.department_name , e.employee_name , e.salary  from employees as e right join deparments as d on 
    e.department_id = d.department_id order by e.salary DESC;

3 - select d.department_id  , d.department_name  from employees as e right join deparments as d on 
    e.department_id = d.department_id  where e.employee_id is NULL;

4 - select  d.department_name , count(e.employee_id) as total_emp from employees as e right join deparments as d on 
     e.department_id = d.department_id group by d.department_name order by total_emp DESC;

5 - select  d.department_name , e.employee_name , e.salary from employees as e right join deparments as d on 
     e.department_id = d.department_id AND e.salary > 55000 order by d.department_name ASC ;

6 - select  d.department_name , count(e.employee_id) as total_emp  , AVG(e.salary) as avg_salary from employees as e right join deparments as d 
on e.department_id = d.department_id  group by d.department_name order by avg_salary DESC ;


-- Self join

Table: employees
employee_id	employee_name	department_id	salary	manager_id
1	Suman	10	60000	NULL
2	Amit	20	70000	1
3	Ravi	10	60000	1
4	Pooja	10	65000	2
5	Karan	20	70000	2
6	Mohan	30	45000	NULL
7	Priya	10	50000	


My corrected SELF JOIN queries:

Q1:
SELECT e.employee_name AS employee, m.employee_name AS manager
FROM employees AS e
LEFT JOIN employees AS m
ON m.employee_id = e.employee_id
ORDER BY employee ASC;

Q2:
SELECT e.employee_name AS employee, m.employee_name AS manager
FROM employee AS e
INNER JOIN employee AS m
ON e.manager_id = m.employee_id
ORDER BY manager;

Q5:
SELECT e1.employee_name AS emp1, e2.employee_name AS emp2,
e1.department_id AS departments, e1.salary AS salary
FROM employees AS e1
INNER JOIN employees AS e2
ON e1.department_id = e2.department_id AND e1.salary > e2.salary
ORDER BY departments ASC;

Q6:
SELECT e.employee_name AS manager, e.manager_id AS manager_id,
m.employee_name AS employee, m.employee_id AS employee_id
FROM employees AS e
INNER JOIN employees AS m
ON e.manager_id = m.employee_id
AND e.employee_id < m.employee_id
ORDER BY manager_id ASC, employee_id ASC;

    