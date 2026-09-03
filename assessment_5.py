# ------------------------------------------------------------------------------------
# 5.1 - Check if a person is eligible to vote (age ≥ 18).

age=int(input("enter the age : "))

if age>=18:
    print("you are eligible for vote..")
else:
    print("you are not eligible for voteing..")

# ------------------------------------------------------------------------------------
# 5.2 -  Grade calculator based on marks: 90+ = A, 80+ = B, else C.

mark=float(input("enter student mark : "))

if mark>=90:
       print("grade : A ")
elif mark>=80 :
       print("grade : B ")
else:
       print("grade : C ")

# ------------------------------------------------------------------------------------
# 5.3 - Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.

light=input("light color : ").lower()

if light=="red":
        print("------------")
        print("STOP")
elif light=="yellow":
        print("------------")
        print("WAIT")
elif light == "green":
        print("------------")
        print("GO")
else:
        print("------------")
        print("invalid input..")

# ------------------------------------------------------------------------------------
# 5.4 - ATM withdrawal check: sufficient balance or not.

balance=1000

amount= float(input("enter withdrawal amount : ₹ "))

if amount<=balance:
    balance-=amount
    print("------------------------------------")
    print(f"{amount}₹ withdrawal successfully...")
    print(f"\ntotal balance : {balance}₹")
else:
    print("insufficient balance")

# ------------------------------------------------------------------------------------
# 5.5 - Check if a number is positive, negative, or zero.

number=int(input("\nentre the number : "))

if number>0:
        print(f"{number} number is positive..")

elif number<0:
       print(f"{number} number is negative..")

elif number==0:
       print("number is ZERO..")

else:
       print("invalid input")

# ------------------------------------------------------------------------------------
# 5.6 - Check if a number lies within a given range.

number=int(input("enter the number : "))

if number>=0 and number<=50:
    print(f"{number} number lies within a given range..")
else:
    print(f"{number} number not lies within a given range..")

# ------------------------------------------------------------------------------------
# 5.7 - Username & password verification.

name = "nelson"
password = 12345678

username = input("enter the user name : ")
pass_word = int(input("enter the password : "))

if username != name:
    print("invalid username..")

if pass_word != password:
    print("invalid password")

if username == name and pass_word == password:
    print("login successfully..")

# ------------------------------------------------------------------------------------
# 5.8 - Electricity bill calculator based on units consumed.

print("\n----------unit price table----------")
print("------------------------------------")
print("1. 0 to 50 units    : 3.05 per unit ")
print("2. 51 to 100 units  : 3.50 per unit ")
print("3. 101 to 250 units : 4.15 per unit ")
print("4. above 250 units  : 5.20 per unit ")
print("------------------------------------")
consumer = int(input("enter units : "))

if consumer <= 50:
    data = consumer*3.05
    print(f"Electricity bill is : {data} ₹")
elif consumer <= 100:
    data = consumer*3.50
    print(f"Electricity bill is : {data} ₹")
elif consumer <= 250:
    data = consumer*4.15
    print(f"Electricity bill is : {data} ₹")
else:
    data = consumer*5.20
    print(f"Electricity bill is : {data} ₹")

# ------------------------------------------------------------------------------------
# 5.9 - Simple calculator (add, subtract, multiply, divide).

print("\n--------calculator--------")
print("1. ADD ")
print("2. subtract ")
print("3. multiply ")
print("4. divide ")
print("----------------------------")

choice = int(input("select option : "))

if choice == 1:
    a = float(input("\nA : "))
    b = float(input("B : "))
    data = a+b
    print("total : ", data)
elif choice == 2:
    a = float(input("\nA : "))
    b = float(input("B : "))
    data = a-b
    print("total : ", data)
elif choice == 3:
    a = float(input("\nA : "))
    b = float(input("B : "))
    data = a*b
    print("total : ", data)
elif choice == 4:
    a = float(input("\nA : "))
    b = float(input("B : "))
    data = a/b
    print("total : ", data)
else:
    print("invalid input.")

# ------------------------------------------------------------------------------------
# 5.10 - Check type of triangle (equilateral, isosceles, scalene).

a = int(input("enter the side A : "))
b = int(input("enter the side B : "))
c = int(input("enter the side C : "))

if a == b and b == c:
    print("equilateral")
elif a == b or b == c or c == a:
    print("isosceles")
else:
    print("scalene")
