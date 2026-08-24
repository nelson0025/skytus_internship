#---------------------------------------------------------------------------------------
#3.1 - Take a string input and print its length.

name=input("enter text : ")
print(len(name))

#---------------------------------------------------------------------------------------
#3.2 - Convert a sentence to lowercase.

txt=input("enter text : ")

print(txt.lower())

#---------------------------------------------------------------------------------------
#3.3 - Replace spaces with underscores in a string.

txt=input("enter text : ")

print(txt.replace(" ","_"))

#---------------------------------------------------------------------------------------
#3.4 - Extract the first and last character of a string.

txt=input("enter text : ")

frist=txt[0]
last=txt[-1]

print("frist character : ",frist)
print("last character  : ",last)

#---------------------------------------------------------------------------------------
#3.5 - Reverse a string using slicing.

txt=input("enter text : ")
rev=txt[::-1]
print(rev)

#---------------------------------------------------------------------------------------
# 3.6 - Count how many times a letter appears in a string.

txt=input("enter text      : ")
letter=input("enter letter : ")
count=txt.count(letter)
print(count)

#---------------------------------------------------------------------------------------
# 3.7 - Check if a word is present in a sentence.

txt=input("enter text      : ")
word=input("search the word : ")

if word in txt:
    print("word is present")

else:
    print("word is not present")

#---------------------------------------------------------------------------------------
# 3.8 - Take name & age and print using f-string formatting.

name=input("enter your name : ")
age=int(input("enter your age  : "))

print(f"Hello,my name is {name} and i am {age} year old")

#---------------------------------------------------------------------------------------
# 3.9 - Remove extra spaces from the start and end of a string.

txt=input("enter text      : ")
rem=txt.strip()
print(rem)

#---------------------------------------------------------------------------------------
# 3.10 - Join a list of words into a single string with - between them.

food=["mango ","apple","banana","kiwi"]

list="-".join(food)
print(list)

#---------------------------------------------------------------------------------------
# 3.11 - Create a list of your 5 favorite movies.

movies=["bettleship","spidermen","pacific RIM","Top Gun","interstellar"]

print(movies)

#---------------------------------------------------------------------------------------
# 3.12 - Add a new movie to the list.


movies=["bettleship","spidermen","pacific RIM","Top Gun","interstellar"]
add=input("add movies : ")
movies.append(add)

print("\nmovies add successfully")
print(movies)

#---------------------------------------------------------------------------------------
# 3.13 - Remove the first movie from the list.

movies=["bettleship","spidermen","pacific RIM","Top Gun","interstellar"]

movies.pop(0)

print("\nmovies remove successfully")
print(movies)

#---------------------------------------------------------------------------------------
# 3.14 - Sort a list of numbers in ascending order.

num=[10,12,20,1,2,3,4,5,89,79,6,32,21,0]

num.sort()
print("\n---number sorted in ascending order---")

print(num)

#---------------------------------------------------------------------------------------
# 3.15 - Reverse a list.

movies=["bettleship","spidermen","pacific RIM","Top Gun","interstellar"]

movies.reverse()
print("list reverse successfully")

print(movies)

#---------------------------------------------------------------------------------------
# 3.16 - Find the largest number in a list.

num=[10,12,20,1,2,3,4,5,89,79,6,32,21,0]

number=max(num)
print(number)

#---------------------------------------------------------------------------------------
# 3.17 - Merge two lists into one.

movies=["bettleship","spidermen","pacific RIM","Top Gun","interstellar"]
food=["mango ","apple","banana","kiwi"]

movies.extend(food)
print(movies)

#---------------------------------------------------------------------------------------
# 3.18 - Access the last element of a list without using index number.

num=[10,12,20,1,2,3,4,5,89,79,6,32,21,0]
for i in num:
    last = i

print(last)

#---------------------------------------------------------------------------------------
# 3.19 - Create a nested list and access a specific inner element.

numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(numbers[0][2])

#---------------------------------------------------------------------------------------
# 3.20 - Count how many times an element appears in a list.

num=[1,1,12,2,2,3,3,3]
how_many=int(input("enter number to check : "))
data=num.count(how_many)
print(f"{how_many} is appears in a list {data} time")
