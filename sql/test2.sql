Table: test_executions

execution_id	    Unique execution record ID
test_case_name	    Name of the test case
module	            Application module
status	            PASS, FAIL, or SKIPPED
duration_seconds	Execution duration in seconds
executed_by	        Name of the person or automation agent
environment	        QA, STAGING, or PRODUCTION
defect_id	        Associated defect ID; may be NULL
executed_at	        Execution timestamp


1 - select test_case_name , module , duration_seconds ,executed_at  from test_executions
 where status = 'FAIL' AND environment =  ='QA' ;

2 - select test_case_name , module , duration_seconds from test_executions 
order by duration_seconds DESC  LMIT 10;

3 - select status  , count(status) as total_number_excution  from test_executions
 where environment = 'STAGING' group by status ;

-- 4 - select status count(fail)  , count(execution_id) as total_number_excution 
-- from test_executions group bu status having count() order by module 
-- #  samjh hi nhi aya bss itna hi hua , kya count mai fail de sakte ? 
-- 2 - kyuki mujhe ye samjh aya hai stsus ka group bana ke pass fail vale ko count karna and 
-- jisme having mai condition hai 3 se jyada fail nhi hone chahiye

4 - select module count(*) as total_excution , 
sum(case when status = 'Fail' then 1 ELSE 0 END) as Fail_excution 
from test_executions group by module having sum(case when status = 'Fail' then 1 ELSE 0 END) > 3
 order by module # iss question ko mai group by status kar rha tha mujhe ye clear hi nhi ho pa rha tha ki module se group by karnn hai but order wise mene module kiya tha isko solve karne ke liye merne code bhi dekha


5 - select module , count(*) as total_excution , sum(case when status = 'fail' then 1 else 0 end)  from test_executions where
 status = round( sum(case when status = 'Fail' then 1 else 0 END) / count(status) ) * 100 as Failure_rate

5 - select module , count(*) as total_excution ,
 sum(case when status = 'Fail' then 1 else 0 end) as Fail_excution , 
 (sum(case when status = 'Fail' then 1 else 0 end) * 100.0) / count(*) as Failure_rate 
 from test_executions group by module having (sum(case when status = 'Fail' then 1 else 0 end) * 100.0) / count(*) > 20  
 
6 - select SUM(case when status = 'Fail' and defect_id is not NULL then 1 ELSE 0 END) 
,SUM(case when status = 'Fail' and defect_id is NULL then 1 ELSE 0 END)  from test_executions ; 

7 - SELECT 
    environment,
    AVG(duration_seconds) AS avg_duration_seconds
FROM 
    test_executions
GROUP BY 
    environment
HAVING 
    AVG(duration_seconds) > 30
ORDER BY 
    avg_duration_seconds DESC;



