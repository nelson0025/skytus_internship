CREATE DATABASE BANK;
USE BANK;
CREATE TABLE ACCOUNT(ID INT PRIMARY KEY,NAME VARCHAR(50),BALANCE INT);
INSERT INTO ACCOUNT(ID,NAME,BALANCE)VALUE 
(1,'NELSON',10000),
(2,'JON SNOW',5000);

SELECT * FROM ACCOUNT;
#---------------------------------------------------------------------------------------
#6.1 Start a transaction
START TRANSACTION;

UPDATE ACCOUNT
SET BALANCE = BALANCE -1000
WHERE ID = 1;

UPDATE ACCOUNT 
SET BALANCE = BALANCE + 1000
WHERE ID = 2;
	
COMMIT;

SELECT*FROM ACCOUNT;
#---------------------------------------------------------------------------------------
#6.2 Insert record into accounts
START TRANSACTION;
INSERT INTO ACCOUNT (ID,NAME,BALANCE)
VALUE 
(3,'TOM',12500);

COMMIT;

SELECT * FROM ACCOUNT;
#---------------------------------------------------------------------------------------
#6.3 Rollback changes
START TRANSACTION;

UPDATE  ACCOUNT
SET BALANCE = BALANCE -2000
WHERE ID=1;

UPDATE ACCOUNT
SET BALANCE =BALANCE + 2000
WHERE ID =3;

SELECT * FROM ACCOUNT;
ROLLBACK;


SELECT * FROM ACCOUNT;
#---------------------------------------------------------------------------------------
#6.4 Commit valid transactions
START TRANSACTION;

UPDATE ACCOUNT
SET BALANCE = BALANCE - 2000
WHERE ID = 3;

UPDATE ACCOUNT
SET BALANCE = BALANCE + 2000
WHERE ID =1;

SELECT * FROM ACCOUNT;
COMMIT;
SELECT * FROM ACCOUNT;

#---------------------------------------------------------------------------------------
#6.5 Demonstrate transfer of money using transaction
START TRANSACTION;

UPDATE ACCOUNT
SET BALANCE=BALANCE - 2000
WHERE ID = 3;

UPDATE ACCOUNT
SET BALANCE=BALANCE + 2000
WHERE ID =2;

COMMIT;

SELECT * FROM ACCOUNT;