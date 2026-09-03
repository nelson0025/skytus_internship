#---------------------------------------------------------------------------------------
# 4.1 - Create a tuple with 5 numbers.

number=(1,2,3,4,5)
print(number)

#---------------------------------------------------------------------------------------
# 4.2 - Access the third element in a tuple.

food=("apple","mango","kiwi","banana")
print("third element is : ",food[2])

#---------------------------------------------------------------------------------------
# 4.3 - Unpack a tuple into separate variables.

fruits=("apple","banana","kiwi","orange",)
(red,yellow,green,orange)=fruits

print(red)
print(yellow)
print(green)
print(orange)

#---------------------------------------------------------------------------------------
# 4.4 - Create a set of 5 fruits.

fruits={"apple","mango","kiwi","banana","cherry"}
print(fruits)

#---------------------------------------------------------------------------------------
# 4.5 - Add a new fruit to the set.

fruits={"apple","mango","kiwi","banana","orange"}
fruits.add("cherry")

print(fruits)

#---------------------------------------------------------------------------------------
# 4.6 - Remove an element from a set.

fruits={"apple","mango","kiwi","banana","orange"}
fruits.remove("orange")
print(fruits)

#---------------------------------------------------------------------------------------
# 4.7 - Find union of two sets.

num1={1,2,3,4,5,6,7,8,9,10}
num2={11,12,13,14,15,16,17,18,19,20}

num3=num1.union(num2)
print(num3)

#------------------------------------------------------------------------------------
# 4.8 - Find intersection of two sets.

num1={1,2,3,4,5,6,7,8,9,10}
num2={11,2,3,42,53,4,57,8,69,10}

num3=num1.intersection(num2)
print(num3)

#------------------------------------------------------------------------------------
# 4.9 - Check if one set is subset of another.

num1={1,2,3,4}
num2={1,2,3,4,5,6,7,8,9,10}

num3=num1.issubset(num2)
print(num3)

#------------------------------------------------------------------------------------
# 4.10 - Convert a list with duplicate values into a set to remove duplicates.

list=[1,1,2,2,3,34,5,6,78,8,8]
set1=set(list)
print(set1)

#------------------------------------------------------------------------------------
# 4.11 - Create a dictionary storing student names and marks.

school={}
name=input("enter student name : ")
mark=float(input("enter student mark : "))

school={"name":name,"mark":mark}
print("------------------------")
print("student name and mark store successfully..")
print(f"\nname : {school["name"]}")
print(f"mark : {school["mark"]}")

#------------------------------------------------------------------------------------
# 4.12 - Add a new key-value pair to an existing dictionary.

school={}
name=input("enter student name : ")
mark=float(input("enter student mark : "))
en_no=int(input("enter roll number : "))


school={"name":name,"mark":mark}
school.update({"roll_no":en_no})
print("------------------------")
print("student name and mark store successfully..")
print(f"\nname  : {school["name"]}")
print(f"mark    : {school["mark"]}")
print(f"roll no : {school["roll_no"]}")

#------------------------------------------------------------------------------------
# 4.13 - Delete a key-value pair from a dictionary.

school={}
name=input("enter student name : ")
mark=float(input("enter student mark : "))

school={"name":name,"mark":mark}
school.pop("mark")
print("------------------------")
print("in student dictionary mark key-value delete successfully..")
for i in school.items():
    print(i)

#------------------------------------------------------------------------------------
# 4.14 - Merge two dictionaries into one.

a={1,2,3,4,5,6}
b={7,8,9,10,11}

a.update(b)
print(a)

#------------------------------------------------------------------------------------
# 4.15 - Check if a key exists in a dictionary.


school={"name":"nelson","mark":65}

if "mark" in school:
    print("mark key exists..")
else:
    print("key not found..")

#------------------------------------------------------------------------------------
# 4.16 - Count word frequency in a given string using a dictionary.

wo_rd={}

txt=input("enter the string : ")
word =txt.split()
for letter  in word:
   if letter in wo_rd:
      wo_rd[letter]+=1
   else:
      wo_rd[letter]=1

print(wo_rd)
         
#------------------------------------------------------------------------------------
# 4.17 - Find the key with the maximum value in a dictionary.
         
number={}

a=int(input("enter the frist  number  : "))
b=int(input("enter the second number  : "))
c=int(input("enter the third  number  : "))

number={"A":a,"b":b,"C":c}

value=max(number.values())
for key in number:
   if number[key]==value:
      print("-----------------------")
      print("mex value with key ",key)

#------------------------------------------------------------------------------------
# 4.18 - Reverse keys and values in a dictionary.

number={}
reverse={}
a=int(input("enter the frist  number  : "))
b=int(input("enter the second number  : "))
c=int(input("enter the third  number  : "))

number={"A":a,"b":b,"C":c}

for key,value in number.items():
    reverse[value]=key
print(reverse)

#------------------------------------------------------------------------------------
# 4.19 - Update the value for a specific key.

register={"name":"nelson","age":23,"address":"maliyadhara","mark":95}

update_mark=float(input("update the  mark : "))

print(register)

register["mark"]=update_mark
print("------------------------------------------------------------------")
print(register)

#------------------------------------------------------------------------------------
# 4.20 - Convert a list of tuples into a dictionary.

tup1=("mango","banana","apple","kiwi")
tup2=(120,130,140,150)

result=dict(zip(tup1,tup2)) 
print(result)