# ------------------------------------------------------------------------------------
# 7.1 - Write a program to read a file and display its contents.

with open("File_Handling.txt","r") as file:
 data=file.read()
 print("\n",data)
 
# ------------------------------------------------------------------------------------
# 7.2 - Write a program to count the number of lines in a file.

with open("File_Handling.txt","r") as file:
 data=file.readlines()
 print("\ntotal number of line : ",len(data))

# ------------------------------------------------------------------------------------
# 7.3 - Write a program to count how many times each word appears in a file.

with open("File_Handling.txt","r") as file:
 data=file.read()
 x=data.split()
 word={}

 for i in x:
   if i in word:
      word[i]+=1
   else:  
      word[i]=1
print(word)      

# ------------------------------------------------------------------------------------
# 7.4 - Write a program to write 5 user-entered sentences to a file.

with open("File_Handling.txt", "w") as file:
    for i in range(5):
        user = input("Enter text : ")
        file.write(user + "\n")

# ------------------------------------------------------------------------------------
# 7.5 - Write a program to append a list of strings to an existing file.

user = ["mango","banana","apple","kiwi"]
with open("File_Handling.txt", "a") as file:

 for text in user:
    file.write(text+ "\n")

# ------------------------------------------------------------------------------------
# 7.6 - Write a program to read a file and print only lines containing a specific word.

word = input("Enter word: ")

with open("File_Handling.txt", "r") as file:
    for line in file:
        if word in line:
            print(line)

# ------------------------------------------------------------------------------------
# 7.7 - Write a program to replace a specific word in a file and save changes.


with open("File_Handling.txt", "r") as file:
    data = file.read()

data = data.replace("Python", "Java")

with open("File_Handling.txt", "w") as file:
    file.write(data)

# ------------------------------------------------------------------------------------
# 7.8 - Write a program to merge the contents of two text files into a third file.

with open("file_1.txt","r") as file:
      data=file.read()

with open("file-handling.txt","r") as file:
      data1=file.read()

with open("handling.txt","w") as file:
       file.write(data + data1)

# ------------------------------------------------------------------------------------
# 7.9 - Write a program to read a CSV file and display its content in a formatted way.

import csv

with open("student_1.csv", "r") as file:
    data = csv.reader(file)

    for row in data:
        print(row)

# ------------------------------------------------------------------------------------
# 7.10 - Write a program to back up a file by copying its contents into another file.

with open("file-handling.txt", "r") as file:
    data = file.read()

with open("handling.txt", "w") as file:
    file.write(data)