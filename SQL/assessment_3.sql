CREATE DATABASE COMPANY_DB;
USE COMPANY_DB;

CREATE TABLE EMPLOYEES(EMP_ID INT PRIMARY key,EMP_NAME VARCHAR(50),DEPT_ID INT ,SALARY INT);
CREATE TABLE DEPARTMENTS(DEPT_ID INT,DEPT_NAME VARCHAR(50));

INSERT INTO EMPLOYEES(EMP_ID,EMP_NAME,DEPT_ID,SALARY) value
(1,'NELSON',101,100000),
(2,'JON SNOW',102,90000),
(3,'SCOUT',103,65000),
(4,'JONATHAN',104,3000);

INSERT INTO DEPARTMENTS(DEPT_ID,DEPT_NAME) value
(101,'IT'),
(102,'HR'),
(103,'SALES'),
(104,'MARKETING'),
(105,'FINANCE');

UPDATE EMPLOYEES
SET SALARY =100000
WHERE EMP_ID =1;

UPDATE EMPLOYEES
SET SALARY =90000
WHERE EMP_ID=2;

UPDATE EMPLOYEES
SET SALARY=65000
WHERE EMP_ID=3;

UPDATE EMPLOYEES
SET SALARY =30000
WHERE EMP_ID=4;

DROP TABLE IF EXISTS DEPARTMENTS_BACKUP;
DROP TABLE IF EXISTS DEPARTMENTS_NEW;

SELECT * FROM DEPARTMENTS;
select* FROM EMPLOYEES;

#---------------------------------------------------------------------------------------
#3.1 Display employee name with department name

SELECT E.EMP_NAME,D.DEPT_NAME FROM EMPLOYEES E
INNER JOIN DEPARTMENTS D ON E.DEPT_ID=D.DEPT_ID;

#---------------------------------------------------------------------------------------
#3.2 Display employees earning more than 50,000
SELECT * FROM EMPLOYEES WHERE SALARY > 50000;

#---------------------------------------------------------------------------------------
#3.3 Display department-wise total salary
SELECT DEPT_ID,SUM(SALARY) AS TOTAL_SALARY
FROM EMPLOYEES
GROUP BY DEPT_ID;

#---------------------------------------------------------------------------------------
#3.4 Display departments with more than 2 employees

SELECT DEPT_ID,COUNT(*) AS TOTAL_EMPLOYEES	
FROM  EMPLOYEES
GROUP BY DEPT_ID
HAVING COUNT(*)>2;

#---------------------------------------------------------------------------------------
#3.5 Display employees without a department

SELECT * FROM EMPLOYEES WHERE DEPT_ID IS NULL;
