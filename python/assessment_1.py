#---------------------------------------------------------------------------------------
# 1.1 - Write a program to print your name, age, and city in one line.

name="nelson"
age=24
city="maliyadhara"
print(f"my name is {name},my age is {age} and i am living at {city}")

#---------------------------------------------------------------------------------------
# 1.2 - Take user input for two numbers and print their sum.

a=int(input("\nenter frist number  : "))
b=int(input("enter second number : "))

sum=a+b
print("------------------")
print("total sum : ",sum)

#---------------------------------------------------------------------------------------
# 1.3 - Write a program to convert temperature from Celsius to Fahrenheit.

Celsius = float(input("enter the Celsius : "))
fahrenheit = (Celsius * 9/5) + 32

print(f"Fahrenheit = {fahrenheit} F")

#---------------------------------------------------------------------------------------
# 1.4 - Store your name in a variable and print it in uppercase.

name=input("enter your name : ")
print(name.upper())

#---------------------------------------------------------------------------------------
# 1.5 - Ask the user for their birth year and calculate their current age.

user=int(input("enter your birth year : "))
current=2026
total=current - user
print("current age : ",total)

#---------------------------------------------------------------------------------------
# 1.6 - Write a program to swap the values of two variables.

a=int(input("\nenter the frist number   : "))
b=int(input("enter the second number  : "))

a,b=b,a
print("a = ",a)
print("b = ",b)

#---------------------------------------------------------------------------------------
# 1.7 - Create a program to calculate the area. of a rectangle from user inputs.

length=float(input("\nenter length   : "))
width=float(input("enter width    : "))

reactangle=length*width
print("rectangle area : ",reactangle)

#---------------------------------------------------------------------------------------
# 1.8 - Write a program to check if a number is positive or negative.

number=float(input("\nenter number : "))
if number<0 :
    print("number is negative.")
elif number>0:
    print("number is psitive")    
else:
    print("input is Zero")   

#---------------------------------------------------------------------------------------
# 1.9 - Ask for two numbers and print their average.

num1=int(input("enter frist number  : "))
num2=int(input("enter second number : "))

avg=(num1+num2)/2
print("average : ",avg)