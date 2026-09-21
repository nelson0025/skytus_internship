#---------------------------------------------------------------------------------------
#2.1 Count total _number of students
SELECT COUNT(*)AS TOTAL_STUDENT FROM STUDENT;

#---------------------------------------------------------------------------------------
#2.2 Find average marks of students
SELECT AVG(MARK) AS AVRAGE_MARK FROM STUDENT;

#---------------------------------------------------------------------------------------
#2.3 Find highest & lowest marks

SELECT MAX(MARK), MIN(MARK) FROM STUDENT;

#---------------------------------------------------------------------------------------
#2.4 Find department-wise average marks

SELECT DEPARTMENT ,AVG(MARK) AS AVRAGE_MARK FROM STUDENT
GROUP BY DEPARTMENT;

#---------------------------------------------------------------------------------------
#2.5 Display departments where average marks > 70

SELECT DEPARTMENT ,AVG(MARK) AS AVRAGE_MARK FROM STUDENT 
GROUP BY DEPARTMENT
HAVING AVG(MARK)>70;
