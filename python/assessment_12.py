# -------------------------------------------------------------------------------------------------------
# 12.1 - Print numbers from 1 to 10.

for i in range (1,11):
    print (i)

# -------------------------------------------------------------------------------------------------------
# 12.2 - Display multiplication table for a given number.

a=int(input("A : "))
for i in range(1,11):
    print(a," X ",i," = ",a*i)

# -------------------------------------------------------------------------------------------------------
# 12.3 - Find factorial of a number.

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial:", factorial)

# -------------------------------------------------------------------------------------------------------
# 12.4 - Find factorial of a number.

z = int(input("Enter number : "))

a = 0
b = 1

for i in range(z):
    print(a, end=" ")

    c = a + b
    a = b
    b = c

# -------------------------------------------------------------------------------------------------------
# 12.5 - Check if a number is prime.

number=int(input("enter the number : "))
if number>1:
     for i in range(2,number):
          if number%i==0:
              print(number ," number is not prime")
              break
     else:
          print(number,"is prime")    
else:
    print("not prime")             

# -------------------------------------------------------------------------------------------------------
# 12.6 - Reverse a number (e.g., 123 → 321).

number=int(input("number : "))

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reverse number:", reverse)

# -------------------------------------------------------------------------------------------------------
# 12.7 - Count digits in a number.

while True:
    number=int(input("\nnumber       : "))
    if len(str(number))==0:
        print("please enter a number")
        break
    else:   
        print("total degits : ",len(str(number)))
        break

# -------------------------------------------------------------------------------------------------------
# 12.8 - Find sum of even numbers between 1–100.

sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum += i

print("sum of even numbers :", sum)

# -------------------------------------------------------------------------------------------------------
# # 12.9 - Print a pyramid pattern.

for i in range(1,6):
    print(" " * (5-i) +" * "*i)

# -------------------------------------------------------------------------------------------------------
# # 12.10 - Find all divisors of a number.

number = int(input("Number : "))

for i in range(1, number + 1):
    if number % i == 0:
        print(i)