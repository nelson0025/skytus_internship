# -------------------------------------------------------------------------------------------------------
# 10.1 - Create a base class Animal and subclasses Dog and Cat.

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):
    def bark(self):
        print(self.name, "say woof!")


class Cat(Animal):
    def bark(self):
        print(self.name, "say meow!")


dog1 = Dog("spider")
cat1 = Cat("lemon")

dog1.eat()
dog1.bark()
cat1.eat()
cat1.bark()

# -------------------------------------------------------------------------------------------------------
# 10.2 - Create a class hierarchy for Vehicle → Car → ElectricCar.


class Vehicle:
    def __init__(self, name, brand, car_type):
        self.name = name
        self.brand = brand
        self.car_type = car_type

    def company(self):
        print("\n--------------------------")
        print("car name  is : ", self.name)
        print("car brand is : ", self.brand)


class Car(Vehicle):
    def types(self):
        if self.car_type == "petrol":
             print(f"{self.brand} brand {self.name} car is petrol")
        elif self.car_type == "diesel":
             print(f"{self.brand} brand {self.name} car is diesel")
        elif self.car_type == "CNG":
             print(f"{self.brand} brand {self.name} car is CNG")
        elif self.car_type == "electric":
             print(f"{self.brand} brand {self.name} car is electric")
            
        else:
             print("invalid car type it must be petrol , diesel , CNG , Electric")

class  ElectricCar(Car):
        def Electric_Car(self):
            if self.car_type =="electric":
                print(f"{self.brand} brand {self.name} car is electric")
            else:
                 print("this not an Electric car")    

name=input("car name     : ")
brand=input("car brand    : ")
car_type=input("car type     : ")
p1=ElectricCar(name,brand,car_type)


p1.company()
p1.types()
p1.Electric_Car()

# -------------------------------------------------------------------------------------------------------
# 10.3 - Implement method overriding in a base and derived class.

class Sutdent : 
    def __init__(self ,name,number,mark1,mark2):
         self.name=name
         self.number=number
         self.mark1=mark1
         self.mark2=mark2
    def view (self):
         print(f"\nstudent name     : {self.name}")
         print(f"student number     : {self.number}")
         print(f"sudent frist mark  : {self.mark1}")
         print(f"sudent second mark : {self.mark2}")
         print(f"total mark         : {self.mark1 + self.mark2}")

class register(Sutdent):
     def __init__(self, name, number, mark1, mark2):
          super().__init__(name, number, mark1, mark2)

     def view (self):
         print("\n----------student register----------")
         print(f"student name       : {self.name}")
         print(f"student number     : {self.number}")
         print(f"sudent frist mark  : {self.mark1}")
         print(f"sudent second mark : {self.mark2}")
         print("------------------------------------")
         print(f"total mark         : {self.mark1 + self.mark2}")     

name=input("enter student name : ")
number=int(input("enter the number   : "))
mark1=float(input("enter frist mark   : "))
mark2=float(input("enter second mark  : "))
p1=register(name,number, mark1, mark2)      

p1.view()

# -------------------------------------------------------------------------------------------------------
# 10.4 - Demonstrate multiple inheritance with two parent classes.

class CustomerInfo:
    def __init__(self,name,number,age,address,Email):
        self.name=name        
        self.number=number
        self.age=age
        self.address=address
        self.Email=Email
  

class AccountInfo:
    def __init__(self,account_number,account_type,balance,branch_name):
        self.account_number=account_number
        self.account_type=account_type
        self.balance=balance
        self.branch_name=branch_name

                
class Bank(CustomerInfo,AccountInfo):    

    def __init__(self, name, number, age, address, Email,account_number,account_type,balance,branch_name):
          CustomerInfo.__init__(self,name, number, age, address, Email)
          AccountInfo.__init__(self,account_number,account_type,balance,branch_name)
    def customer(self):
         print("\n--------customer info--------")
         print("customer name    : ",self.name)
         print("customer number  : ",self.number)
         print("customer age     : ",self.age)
         print("customer address : ",self.address)
         print("customer Email   : ",self.Email)
    def account(self):
         print("\n--------Account info--------")
         print("account number  : ",self.account_number)
         print("account type  : ",self.account_type)
         print("current balance  : ",self.balance)
         print("bank branch  : ",self.branch_name)

print("----to-create-customer----")
name=input("\nname : ")
number=int(input("number : "))
age=int(input("age : "))
address=input("address : ")
Email=input("Email : ")

print("----to-create-account----")
account_number=int(input("\naccount number : "))
account_type=input("account type : ")
balance=int(input("current balance : "))
branch_name=input("branch name : ")

p1=Bank( name, number, age, address, Email,account_number,account_type,balance,branch_name)

p1.customer()
p1.account()

# -------------------------------------------------------------------------------------------------------
# 10.5 - Create a polymorphic function that works with different shapes.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height



def calculate_area(shape):
    print("Area:", shape.area())


circle = Circle(5)
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 6)


calculate_area(circle)
calculate_area(rectangle)
calculate_area(triangle)
        
# -------------------------------------------------------------------------------------------------------
# 10.6 - Create a Bank system with SavingsAccount and CurrentAccount classes.

class BankAccount:

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Insufficient Balance")


class SavingsAccount(BankAccount):

    def __init__(self, account_holder, account_number, balance, interest_rate):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print("Interest:", interest)


class CurrentAccount(BankAccount):

    def __init__(self, account_holder, account_number, balance, overdraft_limit):
        super().__init__(account_holder, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Overdraft limit exceeded")


saving = SavingsAccount("nelson", 101, 10000, 5)

saving.deposit(2000)
saving.withdraw(3000)
saving.calculate_interest()

print("\n-------------------\n")



current = CurrentAccount("nelson", 102, 5000, 2000)

current.deposit(1000)
current.withdraw(7000)

# -------------------------------------------------------------------------------------------------------
# 10.7 - Create a class with private attributes and getter/setter methods.

class Fruits:
    def __init__(self,name,price):
        self.__name=name
        self.__price=price

    def get_name(self):
         return self.__name
 
    def get_price(self):
         return self.__price  

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price can't be negative")

name=input("Fruits name       : ")             
price=float(input("Fruits price      : "))
new_price=float(input("new Fruits price  : "))
p1=Fruits(name,price)                

print("\nFruits name : ",p1.get_name())
print("old price   : ",p1.get_price())
p1.set_price(new_price)
print("New Price   : ", p1.get_price())    


# -------------------------------------------------------------------------------------------------------
# 10.8 - Create a Teacher and Student class to show inheritance.

class Teacher:
      def __init__(self,name,subject):
            self.name=name
            self.subject=subject

      def display(self):
            print("\nTeacher name : ",self.name)
            print("subject name : ",self.subject)
            
class  Student(Teacher):
      def __init__(self,student_name,roll_no,name,subject):
            super().__init__(name,subject)
            self.student_name=student_name
            self.roll_no=roll_no

      def view(self):
            print("student name    : ",self.student_name )
            print("student roll no : ",self.roll_no)


name=input("Teacher name   : ")
subject=input("subject name : ")
student_name=input("student name : ")
roll_no=int(input("student roll no : "))
p1=Student(student_name,roll_no,name,subject)

p1.display()
p1.view()

# -------------------------------------------------------------------------------------------------------
# 10.9 - Create a MusicPlayer class and subclass Spotify to override the play method.

class MusicPlayer:
     
      def __init__(self,name,song_type):
            self.name=name
            self.song_type=song_type

      def play(self):
            print("song name : ",self.name)
            print("song type : ",self.song_type)

class Spotify(MusicPlayer):

            def __init__(self,new_type,price,song_type,name):
                 super(). __init__(name,song_type)
                 self.new_type=new_type
                 self.price=price
            def play(self)  :
                 
                 print("new song type : ",self.new_type)  
                 print("membership price : ",self.price)


name=input("song name   : ")
song_type=input("song type : ")
new_type=input("song new type : ")
price=float(input("membership price : "))

inner=Spotify(new_type,price,song_type,name)

inner.play()

# -------------------------------------------------------------------------------------------------------
# 10.10 - Demonstrate the use of super() in inheritance.

class Fruits:
    def __init__(self,name,price,new_price):
        self.name=name
        self.price=price
        self.new_price=new_price

    def display(self):

        print("\nfruits name : ",self.name)    
        print("fruits price : ",self.price)
        print("fruits new price : ",self.new_price)  
class Shop(Fruits):

        def __init__(self,name,price,new_price):
             super().__init__(name,price,new_price)
           
                

             
name=input("Fruits name       : ")             
price=float(input("Fruits price      : ")) 
new_price=float(input("Fruits new price      : "))
p1=Shop(name,price,new_price)


p1.display()