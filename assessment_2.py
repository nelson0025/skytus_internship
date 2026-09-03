#---------------------------------------------------------------------------------------
# 2.1 - Calculate the remainder of two numbers.

num1=int(input("\nenter frist number  : "))
num2=int(input("enter second number : "))

reminder=num1%num2
print("-------------------------------")
print("reminder            :",reminder)

#---------------------------------------------------------------------------------------
# # 2.2 - Check if a number is even or odd.

num=float(input("enter the number : "))

if num %2==0:
    print("number is even")
else:
    print("number is odd")    

#---------------------------------------------------------------------------------------
# 2.3 - Compare two numbers and print the larger one.

num1=int(input("\nenter frist number   : "))
num2=int(input("enter secound number : "))


if num1 > num2:
    print("Larger number:", num1)
else:
    print("Larger number:", num2)   


#---------------------------------------------------------------------------------------
# 2.4 - write a program to calculate the square and cube of a number

num=int(input("enter the number : "))

square=num**2
cube=num**3
print("square is : ",square)
print("cube is : ",cube)

#---------------------------------------------------------------------------------------
#2.5 - Check if two entered numbers are equal.

num1=int(input("\nenter frist number   : "))
num2=int(input("enter secound number : "))

if num1==num2:
     print("both number are equal")
else:
     print("both number are not equal")     

#---------------------------------------------------------------------------------------
# 2.6 - Take two numbers and print True if both are positive, else False.

num1=int(input("\nenter frist number   : "))
num2=int(input("enter secound number : "))

print(num1 > 0 and num2 > 0) 

#---------------------------------------------------------------------------------------
# 2.7 - Write a program to convert float to integer.

num=float(input("enter the number : "))

int_num=int(num)
print( int_num)

#---------------------------------------------------------------------------------------
# 2.8 - Take a number as string, convert to int, and multiply by 10.

num=input("enter the number : ")

num=int(num)
total=num*10
print(total)

#---------------------------------------------------------------------------------------
# 2.9 - Write a program that uses and & or operators to check multiple conditions.

#for and
age=int(input("enter the age : "))

if age>18 and age< 60:
 print('your are aligable')
else:
  print("your not alegebal")

# for OR

num1=int(input("enter the frist number : "))
num2=int(input("enter the second number : "))
if num1==20 or num2==10: 
  print("true")
else:   
  print("false")

#---------------------------------------------------------------------------------------
# 2.10 - Divide two numbers and print the quotient and remainder separately.

#for divide
num1=int(input("enter the frist number  : "))
num2=int(input("enter the second number : "))
 
divide=num1/num2
print("------------------")
print("divistion is : ",divide)

#for quotient
num1=int(input("enter the frist number  : "))
num2=int(input("enter the second number : "))

quotient=num1//num2

print("------------------")
print("quotient is : ",quotient)

#for remainder
num1=int(input("enter the frist number  : "))
num2=int(input("enter the second number : "))

remainder=num1%num2

print("------------------")
print("remainder is : ",remainder)