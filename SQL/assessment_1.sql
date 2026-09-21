CREATE DATABASE STUDENTS;
USE STUDENTS;

CREATE TABLE STUDENT(STUDENT_ID INT PRIMARY KEY,STUDENT_NAME VARCHAR(50),DEPARTMENT VARCHAR (30),
STUDENT_YEAR INT,MARK INT);

INSERT INTO STUDENT
(STUDENT_ID,STUDENT_NAME,DEPARTMENT,STUDENT_YEAR,MARK) 
VALUES
(1,'NELSON','COMPUTER',2023,70),
(2,'JON SNOW','CIVIL',2024,78),
(3,'SPIDY','COMPUTER',2026,50);

INSERT INTO STUDENT(STUDENT_ID,STUDENT_NAME,DEPARTMENT,STUDENT_YEAR,MARK)
VALUES
(4,'MAX','CSE',2022,90),
(5,'YUKI','CSE',2021,91);


#---------------------------------------------------------------------------------------
#1.1 Display all student records
SELECT * FROM STUDENT;

#---------------------------------------------------------------------------------------
#1.2 Display only _name_ & department
SELECT STUDENT_NAME ,DEPARTMENT FROM STUDENT;

#---------------------------------------------------------------------------------------
#1.3 Find students _with marks greater than 75
SELECT * FROM STUDENT WHERE MARK>75;

#---------------------------------------------------------------------------------------
#1.4 Display students _from CSE department
SELECT * FROM STUDENT WHERE DEPARTMENT='CSE';

#---------------------------------------------------------------------------------------
#1.5 Sort students _by marks (descending)
SELECT * FROM STUDENT ORDER BY MARK DESC;

#---------------------------------------------------------------------------------------
#1.6 Display _top 3 scorers
SELECT * FROM STUDENT ORDER BY MARK DESC LIMIT 3;
