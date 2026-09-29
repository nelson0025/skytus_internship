#---------------------------------------------------------------------------------------
#5.1 Primary key
CREATE TABLE CUSTOMER (CUSTOMER_ID INT PRIMARY KEY);

#---------------------------------------------------------------------------------------
#5.2 Unique email
 
CREATE TABLE CUSTOMER (
    CUSTOMER_ID INT,
    CUSTOMER_EMAIL VARCHAR(100) UNIQUE
);

#---------------------------------------------------------------------------------------
#5.3 Unique email
CREATE TABLE CUSTOMER (CUSTOMER_ID INT PRIMARY KEY,
EMAIL VARCHAR(30),
PASSWORD VARCHAR(30) NOT NULL
);                   

#---------------------------------------------------------------------------------------
#5.4 Add foreign key between orders and users
CREATE TABLE CUSTOMBER (
    USER_ID INT PRIMARY KEY,
    USER_NAME VARCHAR(50)
);

CREATE TABLE ORDERS (
    ORDER_ID INT PRIMARY KEY,
    USER_ID INT,
    FOREIGN KEY (USER_ID) REFERENCES CUSTOMBER(USER_ID)         

#---------------------------------------------------------------------------------------
#5.5 Create index on email column
CREATE INDEX IDX_EMAIL
ON CUSTOMBER(EMAIL);

#---------------------------------------------------------------------------------------
#5.6 Create view to display user order summary
CREATE VIEW USER_ORDER_SUMMARY AS
SELECT 
    U.USER_ID,
    U.USER_NAME,
    COUNT(O.ORDER_ID) AS TOTAL_ORDERS,
    SUM(O.AMOUNT) AS TOTAL_AMOUNT
FROM USERS AS U
JOIN ORDERS AS O
ON U.USER_ID = O.USER_ID
GROUP BY U.USER_ID, U.USER_NAME;
