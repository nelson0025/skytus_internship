#---------------------------------------------------------------------------------------
#8.1 Add index to improve search on orders.customer_id
CREATE INDEX IND_ID
ON ORDERS(ID);

SELECT * FROM ORDERS
WHERE ID=1;
#---------------------------------------------------------------------------------------
#8.2 Use EXPLAIN to analyze query
EXPLAIN 
SELECT * FROM ORDERS 
WHERE ID =1;
#---------------------------------------------------------------------------------------
#8.3 Optimize a slow JOIN query
SELECT C.NAME,C.CITY,
COUNT(O.ORDER_ID) AS TOTAL_ORDER,
SUM(O.AMOUNT) AS TOTAL_AMOUNT
FROM CUSTOMBERS AS C
JOIN ORDERS AS O
ON C.ID=O.ID
GROUP BY C.NAME,C.CITY;

EXPLAIN
SELECT C.NAME,C.CITY,
COUNT(O.ORDER_ID) AS TOTAL_ORDER,
SUM(O.AMOUNT) AS TOTAL_AMOUNT
FROM CUSTOMBERS AS C
JOIN ORDERS AS O
ON C.ID=O.ID
GROUP BY C.NAME,C.CITY;
#---------------------------------------------------------------------------------------
#8.4 Explain when index should not be used
SELECT * FROM CUSTOMBERS ;

EXPLAIN 
SELECT * FROM CUSTOMBERS;