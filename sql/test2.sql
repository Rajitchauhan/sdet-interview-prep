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


1 - select test_case_name , module , duration_seconds ,executed_at  from test_executions where status = 'FAIL' AND environment =  ='QA' ;

2 - select test_case_name , module , duration_seconds from test_executions order by duration_seconds DESC  LMIT 10;

3 - select status  , count(status) as total_number_excution  from test_executions where environment = 'STAGING' group by status ;

4 - select status count(fail)  , count(execution_id) as total_number_excution 
from test_executions group bu status having count() order by module #  samjh hi nhi aya bss itna hi hua , kya count mai fail de sakte ? 2 - kyuki mujhe ye samjh aya hai stsus ka group bana ke pass fail vale ko count karna and jisme having mai condition hai 3 se jyada fail nhi hone chahiye


