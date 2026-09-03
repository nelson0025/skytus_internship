# ------------------------------------------------------------------------------------
# 6.1 - Function to check if a number is prime.

def check_number():
    number=int(input("enter the number : "))
    if number<=1:
        print("number is not prime..")
    else:
          for i in range (2,number):
           if number%i==0:
               print("number is not prime..")
               break
          else:
               print("number is prime..")

check_number()

# ------------------------------------------------------------------------------------
# 6.2 - Function to reverse a string.
def reverse():
    txt=input("enter text : ")
    print("reverse a string. : ",txt[::-1])

reverse()

# ------------------------------------------------------------------------------------
# 6.3 - Function to find factorial.

def factorial():
    num = int(input("Enter a number: "))
    result = 1

    for i in range(1, num + 1):
        result = result * i

    print("Factorial:", result)

factorial()

# ------------------------------------------------------------------------------------
# 6.4 - Function to calculate simple interest.

p = float(input("enter the Principal : "))
r=  float(input("enter the Rate of Interest : "))
t = float(input("enter the Time : "))

si=(p*r*t)/100
print("Simple Interest :", si)

# ------------------------------------------------------------------------------------
# 6.5 - Function to check if a word is palindrome.

def palindrome():
    text=input("\nenter the text : ")
    rever=text[::-1]
    if text==rever:
        print(text,"is palindrome")
    else:
        print(text,"is not palindrome")

palindrome()

# ------------------------------------------------------------------------------------
# 6.6 - Function to count vowels in a string.

def vowels():
     text=input("\nenter the text : ")
     count=0

     mach=["a","e","i","o","u"]

     for i in text:
          if i in mach:
               count=count+1
     print("total vowels ",count)

vowels()

# ------------------------------------------------------------------------------------
# 6.7 - Function to merge two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]


def merge():

    list1.extend(list2)

    print(list1)

merge()

# ------------------------------------------------------------------------------------
# 6.8 - Function to find GCD of two numbers.

def gcd():
    num1=int(input("enter the frist value  : "))
    num2=int(input("enter the second value : "))
    gcd=1
    for i in range(1,min(num1,num2)+1):
        if num1%i==0 and num2==0:
           gcd=i
    print("GCD is :",gcd)

gcd()

# ------------------------------------------------------------------------------------
# 6.9 - Function to find area of rectangle.
def rectangle():
    length=int(input("enter the lenth : "))
    width=int(input("enter the width  : "))

    multi=length * width
    print(multi)

rectangle()

# ------------------------------------------------------------------------------------
# 6.10 - Function to check Armstrong number.

def armstrong():
    number = int(input("enter the numner       : "))

    original = number
    digits = len(str(number))
    total = 0
    while number > 0:
          digit = number % 10
          total = total + digit ** digits
          number = number//10
    if total == original:
        print("Armstrong number")
    else:
        print("not an Armstrong number")


armstrong()
