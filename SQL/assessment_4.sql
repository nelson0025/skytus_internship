#---------------------------------------------------------------------------------------
#4.1 Find employees earning more than average salary
SELECT * FROM EMPLOYEES
WHERE SALARY > (SELECT AVG(SALARY) FROM EMPLOYEES);

#---------------------------------------------------------------------------------------
#4.2 Find department with highest total salary

SELECT DEPT_ID,SUM(SALARY) AS TOTAL_SALARY
FROM EMPLOYEES
GROUP BY DEPT_ID
ORDER BY TOTAL_SALARY  DESC
LIMIT 1;

#---------------------------------------------------------------------------------------
#4.3 Display employee with second highest salary
SELECT * FROM EMPLOYEES  WHERE SALARY = (
SELECT MAX(SALARY)
FROM EMPLOYEES WHERE SALARY<(SELECT MAX(SALARY) FROM EMPLOYEES));
#---------------------------------------------------------------------------------------
#4.4 Display employees working in same department as "Amit"
SELECT *
FROM EMPLOYEES
WHERE DEPT_ID = (
    SELECT DEPT_ID
    FROM EMPLOYEES
    WHERE EMP_NAME = 'NELSON'
);