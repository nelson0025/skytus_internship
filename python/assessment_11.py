# -------------------------------------------------------------------------------------------------------
# 11.1 - Create a custom math module and import it in another file.

import Test
a= int(input(" A  : "))
b=int(input(" B  : "))

print("\nAddition       : ",Test.add(a,b))
print("Subtraction    : ",Test.sub(a,b))
print("Multiplication : ",Test.multi(a,b))
print("Division       : ",Test.div(a,b))

# -------------------------------------------------------------------------------------------------------
# 11.2 - Create a module to perform string operations

import Test

text=input("\n Text      :  ")

print("\nUppercase  : ",Test.upper_text(text))
print("Lowercase  : ",Test.lower_text(text))
print("Reverse    : ",Test.revers(text))
print("Length     : ",Test.length(text))

# -------------------------------------------------------------------------------------------------------
# 11.3 - Use random module to generate 5 random integers.

import random

for i in range(5):
    print(random.randint(1,100))

# -------------------------------------------------------------------------------------------------------
# 11.4 - Use datetime module to display current date and time.

import datetime

x=datetime.datetime.today()
print(x)

# -------------------------------------------------------------------------------------------------------
# 11.5 - Use math module to find factorial of a number.

import math

a=int(input("\n A : "))

print("\nfactorial :  ",math.factorial(a))

# -------------------------------------------------------------------------------------------------------
# 11.6 - Create a package shapes with modules for circle and rectangle.

from red import Circlefile
from red import Rectanglefile



Radius=int(input("\nRadius : "))
Length=int(input("Length : "))
Width=int(input("Width  : "))

print("\n area         : ",Circlefile.circle(Radius))
print("Circumference : ",Circlefile.Circumference(Radius))

print("\n area         : ",Rectanglefile.Rectangle(Length,Width))
print("Perimeter     : ",Rectanglefile.Circumference(Length,Width))

# -------------------------------------------------------------------------------------------------------
# 11.7 - Import multiple functions from one module and use them.

from Test import add ,sub,multi,div
a= int(input(" A  : "))
b=int(input(" B  : "))

print("\nAddition       : ",add(a,b))
print("Subtraction    : ",sub(a,b))
print("Multiplication : ",multi(a,b))
print("Division       : ",div(a,b))

# -------------------------------------------------------------------------------------------------------
# 11.8 - Write a program to shuffle a list using random module.


import random
list1=["bettleship","spidermen","pacific RIM","Top Gun","interstellar"]
x=random.shuffle(list1)
print(list1)

# -------------------------------------------------------------------------------------------------------
# 11.9 - Write a program to calculate the difference between two dates.

import datetime

date1=input("frist date  :")
date2=input("second date : ")
a=datetime.datetime.strptime(date1,"%d-%m-%Y")
b=datetime.datetime.strptime(date2,"%d-%m-%Y")
c = abs( a - b)
print("difference between two dates is : ",c)

# -------------------------------------------------------------------------------------------------------
# # 11.10 - Use os module to list files in a directory.

import os
o=os.listdir()
print(o)