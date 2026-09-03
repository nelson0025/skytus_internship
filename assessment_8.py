# ------------------------------------------------------------------------------------
# 8.1 - Write a program to handle division by zero error.

try:
     num=int(input("enter the number : "))
     print(1/num)
except ZeroDivisionError:
     print("Can not divide by zero")

# ------------------------------------------------------------------------------------
# 8.2 - Write a program to handle invalid integer input.

try:
     num=int(input("enter the number : "))
     print(num)
except ValueError:
     print("number must be integer")

# ------------------------------------------------------------------------------------
# 8.3 - Write a program to open a file and handle the "file not found" error.

try:
    with open ("handling.txt","r") as file:
        data=file.read()
        print(data)
except FileNotFoundError:
    print("file not found")

# ------------------------------------------------------------------------------------
# 8.4 - Write a program to demonstrate multiple exception blocks.

try:
     num=int(input("enter the number : "))
     print(1/num)
except ZeroDivisionError:
     print("Cannot divide by zero")

except ValueError:
     print("number must be integer")

# ------------------------------------------------------------------------------------
# 8.5 - Write a program to use finally for resource cleanup.

try:
    with open("handling.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("file not found")

finally:
    print("resource clean up succsessfully..")

# ------------------------------------------------------------------------------------
# 8.6 - Write a program to create a custom exception for invalid age (<18).

class invalidageerror(Exception):
    pass
try:
    age=int(input("enter the age : "))
    if age<18:
        print("age must greter then 18..")
except invalidageerror as e:
    print(e)        

# ------------------------------------------------------------------------------------
# 8.7 - Write a program to handle IndexError when accessing a list.

try:
       list1=[10,20,30,40,50]
       user=int(input("enter the index number : "))
       print(list1[user])
except IndexError:
       print("indax number and value not found ")

# ------------------------------------------------------------------------------------
# 8.8 - Write a program that takes two numbers and handles all possible errors.

class nagativenumbererror(Exception):
     pass

try:
     num1=int(input("enter the frist number  : "))
     num2=int(input("enter the second number : "))
     if num1 < 0 or num2 < 0:
          raise nagativenumbererror

     result = num1 / num2
     print("Result :", result)
except ValueError:
     print("input must be number")     
     
except nagativenumbererror:
     print("number can't be in nagative")
     
except ZeroDivisionError:
     print("number can't be divide by zero")     

except Exception:
     print("other error")

# ------------------------------------------------------------------------------------
# 8.9 -Write a program to log errors to a file instead of printing them.

try:
    user=input("enter text : ")
    with open("text.log","a") as file:
         file.write(user)

except Exception as e:
    with open("error.log", "a") as file:
        file.write(str(e) + "\n")

# -----------------------------------------------------------------------------------------------
# 8.10 - Write a program that validates an email format and raises an exception for invalid ones.

class invalidemailerror(Exception):
    pass
try:
    user=input("enter Email : ")
    if "@" not in user or "." not in user :

        raise invalidemailerror("invalid email formate")
    print("valid email")
except invalidemailerror as e:
  print(e)