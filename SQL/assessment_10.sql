#==============================================================================================================
-- 10.1 Design database for Mess Management System

CREATE DATABASE MESS_MANAGEMENT;
USE MESS_MANAGEMENT;
#==============================================================================================================
-- 10.2 Create tables

CREATE TABLE STUDENTS
(STD_ID INT PRIMARY KEY,
STD_NAME VARCHAR(50),
ROOM_ID INT,PHONE INT);

CREATE TABLE MEALS
(MEAL_ID INT PRIMARY KEY,MEAL_DATE DATE,
MEAL_TYPE VARCHAR(50),MENU VARCHAR(50));

CREATE TABLE ATTENDANCE
(ATTENDANCE_ID INT PRIMARY KEY ,STD_ID INT,
MEAL_ID INT,STATUS VARCHAR(50)
);

CREATE TABLE PAYMENTS
(PAYMENT_ID INT PRIMARY KEY,STD_ID INT,AMOUNT INT,
PAYMENT_DATE DATE,PAYMENT_STATUS VARCHAR(50)
);
#==============================================================================================================
-- 10.3 Create relationships

ALTER TABLE ATTENDANCE
ADD FOREIGN KEY(STD_ID) REFERENCES STUDENTS(STD_ID),
ADD FOREIGN KEY(MEAL_ID) REFERENCES MEALS(MEAL_ID);

ALTER TABLE PAYMENTS
ADD FOREIGN KEY(STD_ID) REFERENCES STUDENTS(STD_ID);
#==============================================================================================================
-- 10.4 Create sample data
INSERT INTO STUDENTS(STD_ID,STD_NAME,ROOM_ID ,PHONE) VALUE
(1, 'NELSON', 101, 9876543210),
(2, 'JON SNOW', 102, 9876543211),
(3, 'TOM', 103, 9876543212),
(4, 'MJ', 104, 9876543213),
(5, 'SCOUT', 105, 9876543214),
(6, 'TONY', 106, 9876543215),
(7, 'MAX', 107, 9876543216),
(8, 'HAL JORDAN', 108, 9876543217);

INSERT INTO MEALS(MEAL_ID,MEAL_DATE,MEAL_TYPE,MENU )VALUE
(1, '2026-10-01', 'BREAKFAST', 'POHA'),
(2, '2026-10-01', 'LUNCH', 'DAL RICE'),
(3, '2026-10-01', 'DINNER', 'ROTI SABJI'),

(4, '2026-10-02', 'BREAKFAST', 'UPMA'),
(5, '2026-10-02', 'LUNCH', 'RAJMA RICE'),
(6, '2026-10-02', 'DINNER', 'PANEER ROTI'),

(7, '2026-10-03', 'BREAKFAST', 'PARATHA'),
(8, '2026-10-03', 'LUNCH', 'DAL ROTI'),
(9, '2026-10-03', 'DINNER', 'KHICHDI');

INSERT INTO ATTENDANCE(ATTENDANCE_ID, STD_ID, MEAL_ID, STATUS) VALUE
(1, 1, 1, 'PRESENT'),
(2, 1, 2, 'PRESENT'),
(3, 1, 3, 'ABSENT'),

(4, 2, 1, 'PRESENT'),
(5, 2, 2, 'ABSENT'),
(6, 2, 3, 'PRESENT'),

(7, 3, 1, 'PRESENT'),
(8, 3, 2, 'PRESENT'),
(9, 3, 3, 'PRESENT'),

(10, 4, 1, 'ABSENT'),
(11, 4, 2, 'PRESENT'),
(12, 4, 3, 'PRESENT'),

(13, 5, 1, 'PRESENT'),
(14, 5, 2, 'PRESENT'),
(15, 5, 3, 'ABSENT'),

(16, 6, 1, 'PRESENT'),
(17, 6, 2, 'ABSENT'),
(18, 6, 3, 'PRESENT'),

(19, 7, 1, 'PRESENT'),
(20, 7, 2, 'PRESENT'),
(21, 7, 3, 'PRESENT'),

(22, 8, 1, 'ABSENT'),
(23, 8, 2, 'PRESENT'),
(24, 8, 3, 'ABSENT');

INSERT INTO PAYMENTS(PAYMENT_ID, STD_ID, AMOUNT, PAYMENT_DATE, PAYMENT_STATUS) VALUE
(1, 1, 3000, '2026-10-01', 'PAID'),
(2, 2, 3000, '2026-10-01', 'PAID'),
(3, 3, 3000, '2026-10-01', 'PAID'),
(4, 4, 3000, '2026-10-02', 'PENDING'),
(5, 5, 3000, '2026-10-02', 'PAID'),
(6, 6, 3000, '2026-10-02', 'PENDING'),
(7, 7, 3000, '2026-10-03', 'PAID'),
(8, 8, 3000, '2026-10-03', 'PAID');
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
SELECT * FROM STUDENTS;
SELECT * FROM MEALS;
SELECT * FROM ATTENDANCE;
SELECT * FROM PAYMENTS;
DROP TABLE ATTENDANCE;
#---------------------------------------------------------------------------------------
#==============================================================================================================
-- 10.5 Write 15 business queries
#--------------------------------------------------------------------------------------------------------------
-- 10.5.1 Find the total number of students currently registered in the mess.

SELECT COUNT(STD_ID ) AS TOTAL_STUDENT FROM STUDENTS;
#--------------------------------------------------------------------------------------------------------------
-- 10.5.2 Find the total mess revenue collected from all students.

SELECT SUM(AMOUNT) AS TOTAL_REVENUE FROM PAYMENTS;
#--------------------------------------------------------------------------------------------------------------
-- 10.5.3 Find the total revenue collected only from PAID payments.

SELECT SUM(AMOUNT) AS TOTAL_REVENUE FROM PAYMENTS
WHERE  PAYMENT_STATUS='PAID';

#--------------------------------------------------------------------------------------------------------------
-- 10.5.4 Find all students who have not yet paid their mess fees.

SELECT S.STD_ID AS ID ,
S.STD_NAME AS NAME,
S.ROOM_ID,S.PHONE ,P.PAYMENT_STATUS 
FROM STUDENTS AS S
JOIN  PAYMENTS AS P
ON S.STD_ID = P.STD_ID
WHERE PAYMENT_STATUS = 'PENDING';
#--------------------------------------------------------------------------------------------------------------
-- 10.5.5 Find the total amount pending from students.

SELECT SUM(AMOUNT) AS TOTAL_PENDING_AMOUNT FROM PAYMENTS
WHERE PAYMENT_STATUS = 'PENDING';
#--------------------------------------------------------------------------------------------------------------
-- 10.5.6 Find the student who has attended the most meals.

SELECT S.STD_ID AS ID,
S.STD_NAME AS NAME ,COUNT(A.MEAL_ID) AS TOTAL_MEAL
FROM STUDENTS AS S
JOIN ATTENDANCE AS A
ON S.STD_ID = A.STD_ID
WHERE STATUS = 'PRESENT'
GROUP BY S.STD_ID,S.STD_NAME
ORDER BY TOTAL_MEAL DESC
LIMIT 1; 
#--------------------------------------------------------------------------------------------------------------
-- 10.5.7 Find the student with the highest number of absences

SELECT S.STD_ID AS ID,
S.STD_NAME AS NAME ,COUNT(A.MEAL_ID) AS TOTAL_MEAL
FROM STUDENTS AS S
JOIN ATTENDANCE AS A
ON S.STD_ID = A.STD_ID
WHERE STATUS = 'ABSENT'
GROUP BY S.STD_ID,S.STD_NAME
ORDER BY TOTAL_MEAL DESC
LIMIT 1; 
#--------------------------------------------------------------------------------------------------------------
-- 10.5.8 Find the attendance percentage of each student.
SELECT S.STD_ID,S.STD_NAME ,
COUNT(CASE WHEN A.STATUS='PRESENT' THEN 1 END) AS PRESENT_MEAL,
COUNT(A.ATTENDANCE_ID) AS TOTAL_MEAL,
ROUND(COUNT(CASE WHEN A.STATUS='PRESENT' THEN 1 END)
*100/COUNT(a.ATTENDANCE_ID),2) AS ATTENDANCE_PERCENTAGE
FROM STUDENTS AS S
JOIN ATTENDANCE AS A
ON S.STD_ID=A.STD_ID
GROUP BY S.STD_ID,S.STD_NAME;
 
#--------------------------------------------------------------------------------------------------------------
-- 10.5.9 Find students whose attendance percentage is below 75%
SELECT S.STD_ID,S.STD_NAME ,
COUNT(CASE WHEN A.STATUS='PRESENT' THEN 1 END) AS PRESENT_MEAL,
COUNT(a.ATTENDANCE_ID) AS TOTAL_MEAL,
ROUND(COUNT(CASE WHEN A.STATUS='PRESENT' THEN 1 END)
*100/COUNT(a.ATTENDANCE_ID),2) AS ATTENDANCE_PERCENTAGE
FROM STUDENTS AS S
JOIN ATTENDANCE AS A
ON S.STD_ID=A.STD_ID
GROUP BY S.STD_ID,S.STD_NAME
HAVING ROUND(COUNT(CASE WHEN A.STATUS='PRESENT' THEN 1 END)
*100/COUNT(a.ATTENDANCE_ID),2)> 75;

#--------------------------------------------------------------------------------------------------------------
-- 10.5.10 Find the most popular meal based on the number of students who attended it.
SELECT M.MEAL_ID,M.MEAL_TYPE,M.MENU, COUNT(*) AS TOTAL_STUDENT FROM MEALS AS M
JOIN ATTENDANCE AS A
ON M.MEAL_ID = A.MEAL_ID
WHERE A.STATUS='PRESENT'
GROUP BY M.MEAL_ID,M.MEAL_TYPE,M.MENU
ORDER BY TOTAL_STUDENT DESC
LIMIT 1;

#--------------------------------------------------------------------------------------------------------------
-- 10.5.11 Find the number of students present for each meal type (Breakfast, Lunch, Dinner).
SELECT    M.MEAL_TYPE, COUNT(*) AS TOTAL_STUDENTS FROM MEALS AS M
JOIN ATTENDANCE AS A
ON M.MEAL_ID = A.MEAL_ID
WHERE A.STATUS='PRESENT'
GROUP BY  M.MEAL_TYPE ;
#--------------------------------------------------------------------------------------------------------------
-- 10.5.12 Find the total number of meals consumed by each student.
SELECT S.STD_ID AS ID,S.STD_NAME AS NAME,COUNT(A.MEAL_ID) AS TOTAL_MEAL
 FROM STUDENTS AS S
JOIN ATTENDANCE AS A
ON S.STD_ID = A.STD_ID
WHERE A.STATUS='PRESENT'
GROUP BY S.STD_ID,S.STD_NAME;

#--------------------------------------------------------------------------------------------------------------
-- 10.5.13 Find the students who have paid their fees but have poor attendance (attendance below 75%).
SELECT S.STD_ID AS ID,S.STD_NAME AS NAME ,P.PAYMENT_STATUS AS STATUS ,
COUNT(CASE WHEN A.STATUS = 'PRESENT' THEN 1 END) AS PRESENT_MEALS,
COUNT(A.ATTENDANCE_ID) AS TOTAL_MEAL,
ROUND(COUNT(CASE WHEN A.STATUS='PRESENT' THEN 1 END)
*100/COUNT(a.ATTENDANCE_ID),2) AS ATTENDANCE_PERCENTAGE
FROM STUDENTS AS S
JOIN ATTENDANCE AS A
ON S.STD_ID = A.STD_ID
JOIN PAYMENTS AS P
ON S.STD_ID = P.STD_ID
WHERE P.PAYMENT_STATUS = 'PAID'
GROUP BY S.STD_ID,S.STD_NAME,P.PAYMENT_STATUS
HAVING ROUND(COUNT(CASE WHEN A.STATUS='PRESENT' THEN 1 END)
*100/COUNT(A.ATTENDANCE_ID),2)< 75;
#--------------------------------------------------------------------------------------------------------------
-- 10.5.14 Find the total number of meals served on each date and identify the date with the highest attendance.
SELECT M.MEAL_DATE ,COUNT(A.ATTENDANCE_ID) AS TOTAL_RECORD,
COUNT(CASE WHEN A.STATUS = 'PRESENT' THEN 1 END) AS TOTAL_ATTENDANCE
 FROM MEALS AS M
JOIN ATTENDANCE AS A
ON M.MEAL_ID = A.MEAL_ID
GROUP BY M.MEAL_DATE;
#--------------------------------------------------------------------------------------------------------------
-- 10.5.15 Generate a mess performance report showing each student's name, room number, total meals attended,
-- attendance percentage, payment amount, and payment status.
SELECT STD_NAME,ROOM_ID, 
COALESCE(A.TOTAL_MEALS_ATTENDED, 0) AS TOTAL_MEALS_ATTENDED,
COALESCE(A.ATTENDANCE_PERCENTAGE, 0) AS ATTENDANCE_PERCENTAGE,
P.AMOUNT AS PAYMENT_AMOUNT,
P.PAYMENT_STATUS
FROM STUDENTS AS S
LEFT JOIN 
(  SELECT
STD_ID,COUNT(CASE WHEN STATUS = 'PRESENT' THEN 1 END) AS TOTAL_MEALS_ATTENDED,
ROUND(COUNT(CASE WHEN STATUS = 'PRESENT' THEN 1 END)
* 100.0 / COUNT(*),2) AS ATTENDANCE_PERCENTAGE
    FROM ATTENDANCE
    GROUP BY STD_ID) AS A
ON S.STD_ID = A.STD_ID
LEFT JOIN PAYMENTS AS P
ON S.STD_ID = P.STD_ID
ORDER BY S.STD_ID;
#==============================================================================================================
-- 10.6 Optimize at least 3 queries
#--------------------------------------------------------------------------------------------------------------
#10.6.1

CREATE INDEX IND_STD_ID
ON ATTENDANCE(STD_ID);

SELECT * FROM ATTENDANCE
WHERE STD_ID=1;
#--------------------------------------------------------------------------------------------------------------
#10.6.2

SELECT S.STD_NAME,S.ROOM_ID,S.PHONE,COUNT(A.MEAL_ID) AS TOTAL_MEAL FROM STUDENTS AS S
JOIN ATTENDANCE AS A
ON S.STD_ID=A.STD_ID
GROUP BY  S.STD_NAME,S.ROOM_ID,S.PHONE;

EXPLAIN
SELECT S.STD_NAME,S.ROOM_ID,S.PHONE,COUNT(A.MEAL_ID)FROM STUDENTS AS S
JOIN ATTENDANCE AS A
ON S.STD_ID=A.STD_ID
GROUP BY  S.STD_NAME,S.ROOM_ID,S.PHONE;
#--------------------------------------------------------------------------------------------------------------
#10.6.3

SELECT SUM(AMOUNT) AS TOTAL_REVENUE FROM PAYMENTS
WHERE  PAYMENT_STATUS='PAID';

EXPLAIN
SELECT SUM(AMOUNT) AS TOTAL_REVENUE FROM PAYMENTS
WHERE  PAYMENT_STATUS='PAID';

