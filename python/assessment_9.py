# -------------------------------------------------------------------------------------------------------
# 9.1 - Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.

class car:

    def __init__(self, brand, model, speed):

        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        accel = int(input("enter the speed to accelrate : "))
        self.speed += accel
        print("speed   : ", self.speed)

    def brake(self):
        br = int(input("enter the speed to brake     : "))
        self.speed -= br
        if self.speed < 0:
            self.speed = 0
        print("speed   : ", self.speed)

brand = input("enter the brand name : ")
model = input("enter the model name : ")
speed = int(input("enter the speed      : "))
car1 = car(brand, model, speed)

print("----------------------")
print("\nBrand   :", car1.brand)
print("Model   :", car1.model)
print("Speed   :", car1.speed)

car1.accelerate()
car1.brake()

# -------------------------------------------------------------------------------------------------------
# 9.2 - Create a BankAccount class with deposit and withdraw methods.

class BankAccount:


    def __init__(self, balance):
        self.balance = balance

    def deposit(self):
        amount = float(input("deposit amount : "))
        if amount <= 0:
            print("deposit amount must be greterthen ZERO..")
        else:
            self.balance+=amount
            print("deposit succsessfully")
            print("total balance : ",self.balance)

    def withdraw(self):
        amount = float(input("\nwithdrawal amount : "))
        if amount <= 0:
            print("withdrawal amount must be greterthen ZERO..")
        elif amount>self.balance:
            print("insuffient balance")
        else:
            self.balance-=amount
            print("withdraw succsessfully")
            print("total balance : ",self.balance)

p1=BankAccount(1000)
p1.deposit()
p1.withdraw()

# -------------------------------------------------------------------------------------------------------
# 9.3 - Create a Student class with a method to calculate average marks.

class Student:
    def __init__(self, che, phy, math):
        self.che = che
        self.phy = phy
        self.math = math

    def average(self):
        if self.che <= 0 or self.phy <= 0 or self.math <= 0:
            print("invalid input.....")
        else:
            avg = (self.che+self.phy+self.math)/3
            print("total average is : ", avg)


che = float(input("\nchemistry        : "))
phy = float(input("physics          : "))
math = float(input("math             : "))
p1 = Student(che, phy, math)

p1.average()

# -------------------------------------------------------------------------------------------------------
# 9.4 - Create a Rectangle class with methods to find area and perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        if self.length <= 0 or self.width <= 0:
            print("Length and width must be greater than zero.")
        else:
            area = self.length * self.width
            print("Rectangle area      : ", area)

    def perimeter(self):
        if self.length <= 0 or self.width <= 0:
            print("Length and width must be greater than zero.")
        else:
            perimeter = 2 * (self.length + self.width)
            print("Rectangle perimeter : ", perimeter)


length = int(input("\nlength  : "))
width = int(input("width   : "))
p1 = Rectangle(length, width)

p1.area()
p1.perimeter()

# -------------------------------------------------------------------------------------------------------
# 9.5 - Create an Employee class that displays salary details.

class Employee:

    def __init__(self, name, salary, hra, bonus):
        self.name = name
        self.salary = salary
        self.hra = hra
        self.bonus = bonus

    def display(self):
        print("\nname   : ", self.name)
        print("salary : ", self.salary)
        print("HRA    : ", self.hra)
        print("bonus  : ", self.bonus)
        data = self.salary+self.hra+self.bonus
        print("-----------------------")
        print("total salary : ", data)


name = input("name   : ")
salary = float(input("salary : "))
hra = float(input("HRA    : "))
bonus = float(input("bonus  : "))
p1 = Employee(name, salary, hra, bonus)

p1.display()

# -------------------------------------------------------------------------------------------------------
# # 9.6 - Create a Book class to store title, author, and price, and display details.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("\n----------details----------")
        print("book title  : ", self.title)
        print("author name : ", self.author)
        print("book price  : ", self.price)


title = input("\nbook name   : ")
author = input("author name : ")
price = float(input("book price  : "))
p1 = Book(title, author, price)

p1.display()

# -------------------------------------------------------------------------------------------------------
# # 9.7 - Create a Circle class to find area and circumference.

class Circle:

    def __init__(self,  r):

        self.r = r

    def area(self):
        if self.r <= 0:
            print("radius must be greater than ZERO")
        else:
            self.pi = 3.14
            area = self.pi * self.r * self.r
            print("\nCircle area          : ", area)

    def circumference(self):
        if self.r <= 0:
            print("radius must be greater than ZERO")
        else:
            self.pi = 3.14
            circumference = 2 * self.pi * self.r
            print("Circle circumference : ", circumference)


r = int(input("\nCircle radius        : "))
p1 = Circle(r)

p1.area()
p1.circumference()

# -------------------------------------------------------------------------------------------------------
# # 9.8 - Create a Laptop class with a method to apply discounts on price.

class Laptop:
    def __init__(self, price, coupons):
        self.price = price
        self.coupons = coupons

    def discounts(self):
        if self.price <= 0 or self.coupons < 0 or self.coupons > self.price:
            print("current price number must be greater than ZERO")
        else:
            print("\ncurrent price   : ", self.price)
            print("discounts price : ", self.coupons)
            disc = self.price - self.coupons
            print("-------------------------")
            print("total price is  : ", disc)


price = float(input("\ncurrent price   : "))
coupons = float(input("discounts price : "))

p1 = Laptop(price, coupons)
p1.discounts()

# -------------------------------------------------------------------------------------------------------
# 9.9 - Create a Flight class with seat booking functionality.

class Flight:

    def __init__(self, seats):
        self.seats = seats

    def book_seat(self, booked_seats):

        if booked_seats <= 0:
            print("seats must be greater than ZERO")

        elif booked_seats > self.seats:
            print("not enough seats available")

        else:
            self.seats -= booked_seats
            print("seat booking successful")
            print("remaining seats :", self.seats)


seats = int(input("enter total seats : "))

p1 = Flight(seats)

booked_seats = int(input("how many seats do you want to book? : "))

p1.book_seat(booked_seats)

# -------------------------------------------------------------------------------------------------------
#  9.10 - Create a Shop class with a method to add and list products.

class shop:
    def __init__(self,add):
        self.add=add
        self.cart=[]

    def product(self):
        self.cart.append(self.add)
        print("product add succsessfully")
    def display(self):
        if len(self.cart)==0:
            print("product not add yet")
        else:
            for i in self.cart:
                print(i)    

add=input("enter the product : ")
p1=shop(add)

p1.product()
p1.display()

