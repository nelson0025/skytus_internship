# -----------------------------------------------------------------------------------------------------------------------------
# 1 - To-Do List CLI

task={}
#----------------------------------------------------------------------------
def add_task_id_validation(task_id):
    if len(str(task_id))!=3 or not task_id.isdigit():
          print("task id must be 3 digits...") 
          return False
    if task_id  in task:
         print("task id alrady exists..") 
         return False
    return True 
#----------------------------------------------------------------------------
def add_task():
    while True:
        task_id = input("enter task id : ")

        if add_task_id_validation(task_id):
            task[task_id] = {"task name": []}
            break

    while True:
        task_name = input("enter task or(type done to stop) : ")

        if task_name == "":
            print("task can not be empty..")

        elif task_name.lower() == "done":
            break

        else:
            task[task_id]["task name"].append({
                "name": task_name,
                "completed": False
            })

    print("tasks added successfully..")

def view_task():
    if len(task) == 0:
        print("task not added yet..")
    else:
        for task_id, data in task.items():

            print(f"\nID : {task_id}")
            print("----------------")

            for i, task_data in enumerate(data["task name"], start=1):

                if task_data["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(f"{i}. {task_data['name']} [{status}]")

            print("----------------")

def mark_complete():


    while True:
        task_id = input("enter task id to mark : ")

        if len(task_id) != 3 or not task_id.isdigit():
            print("task id must be 3 digits...")
            continue

        if task_id not in task:
            print("task not found..")
            continue

        break

    print("\n---------- TASKS ----------")

    for i, task_data in enumerate(task[task_id]["task name"], start=1):
        if task_data["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(f"{i}. {task_data['name']} [{status}]")

    while True:
        print("\n---------------------------")
        choice = input("enter task number to complete : ")

        if not choice.isdigit():
            print("enter a valid number...")
            continue

        choice = int(choice)

        if choice < 1 or choice > len(task[task_id]["task name"]):
            print("task number not found...")
            continue

        break

    task[task_id]["task name"][choice - 1]["completed"] = True

    print("task marked as completed successfully..")

def update_task():
    while True:
        task_id = input("enter task id that you want to update : ")

        if len(task_id) != 3 or not task_id.isdigit():
            print("task id must be 3 digits...")
            continue

        if task_id not in task:
            print("task not found..")
            continue

        break

    print("\n---------- TASKS ----------")

    for i, task_data in enumerate(task[task_id]["task name"], start=1):
        print(f"{i}. {task_data['name']}")

    while True:
        print("\n---------------------------")
        choice = input("enter task number to update : ")

        if not choice.isdigit():
            print("enter a valid number...")
            continue

        choice = int(choice)

        if choice < 1 or choice > len(task[task_id]["task name"]):
            print("task number not found...")
            continue

        break
 
    while True:
        new_task = input("enter new task : ")

        if new_task == "":
            print("task can not be empty..")
            continue

        break
    while True:
             update_mark=input("update mark(complete/pending) : ")
             if update_mark=="complete":
                  task[task_id]["task name"][choice - 1]["completed"] = True
                  break
    
             elif update_mark=="pending":
                task[task_id]["task name"][choice - 1]["completed"] = False
                break
             else:
                 print("invalid choice..")
                

    task[task_id]["task name"][choice - 1]["name"] = new_task


    print("task updated successfully..")

def delete_task():
        while True:
               task_id = input("enter task id  for delete : ")

               if len(task_id) != 3 or not task_id.isdigit():
                        print("task id must be 3 digits...")
                        continue

               if task_id not in task:
                      print("task not found..")
                      continue

               break
        for task_id, data in task.items():

            print(f"\nID : {task_id}")
            print("----------------")
        
            for i, task_data in enumerate(data["task name"], start=1):

                if task_data["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(f"{i}. {task_data['name']} [{status}]")

            print("----------------")
        while True:
               choice=input("selact the option (yes/no) : ").lower()
               if choice=="yes":
                      del task[task_id]
                      print("delete successfully..")
                      break
               elif choice=="no":  
                      print("so you don't want to delete this task..")
                      break
               else:
                      print("invalid choice")  

while True: 
   print("\n|---|---------------------------------------|")
   print("|---|--------------TO-DO-LIST --------------|")
   print("|---|---------------------------------------|")
   print("|1. |            .add task..                |")
   print("|---|---------------------------------------|")
   print("|2. |          ..update task..              |")      
   print("|---|---------------------------------------|")
   print("|3. |          ..delete task..              |")
   print("|---|---------------------------------------|")
   print("|4. |        ..mark complete..              |")
   print("|---|---------------------------------------|")
   print("|5. |          ..view task..                |")  
   print("|---|---------------------------------------|")
   print("|6. |           .. EXIT..                   |")  
   print("|---|---------------------------------------|")
   choice=int(input("make a choice :  "))
   if choice==1:
         add_task()
   elif choice==2:    
         update_task()
   elif choice==3:       
         delete_task()
   elif choice==4:
         mark_complete()
   elif choice==5:
        view_task()      
   elif choice==6:                
        print("you are exit from to do list....")
        break
   else:
       print("invalid choise..")

# -----------------------------------------------------------------------------------------------------------------------------
# 2 - Bank Management System

bank={}
def create_account():
 account_number=int(input("enter account number :- "))
 if len(str(account_number))!=8:
          print("account number must be 8 digits....")
          return
 if account_number in bank:
      print("-----------------------------------------------------")
      print ("alrady exists..")
 else: 
     name=input("enter name :- ")
     if not valid_name(name):
          print("name shoud contain only letters..")
          return
     initial_balance=float(input("enter initial balance :- "))
     pin=int(input("enter the PIN : "))
     
     if len(str(pin))!=4:
          print("PIN must be 4 digits....")
          return
     age_no=input(" enter age : ")

     if len(str(age_no))>18 :
          print("age must be in greterthen 18 ")
          return
     if  not age_no.isdigit() :
         print("room must be in digits")  
         return
     phone_no  =input("enter phone number : ")
     if len(str(phone_no))!=10 or not phone_no.isdigit():
         print("phone number must have 10 digits")

     Email =input("enter the email : ")
     if Email in bank.values():
         print ("email alrady exists..")
         return
     address=input("enter the addresss : ")

     account_type=input("enter ccount type (savings/current): ")
     if account_type=="saving":
        print("accounttype is saving")
        return
     elif account_type=="current":
         print("account type is current")
     bank[account_number]={"name":name,"balance":initial_balance,"PIN":pin,"age":age_no,"phone number":phone_no,"Email":Email,"address":address,"account type":account_type,"history":[]}
     print("-----------------------------------------------------")
     print("account create succsessfully...!")

def deposit():
     
     account_number=int(input("enter the account number : "))
     if len(str(account_number))!=8:
          print("enter valid account number....")
          return
     pin=int(input("enter PIN :- "))
     print("-----------------------------------------------------")
     if len(str(pin))!=4:
          print("PIN must be 4 digits....")
          return
     if pin!=bank[account_number]["PIN"]:
         print("wrong PIN...")
         return
     else: 
         deposit=float(input("enter deposit amount : "))
         if account_number in bank:
             bank[account_number]["balance"]+=deposit
             print("-----------------------------------------------------")
             print(f"₹{deposit} deposit succsessfully..")
             print(f"total balance ₹ {bank[account_number]["balance"]}")
             bank[account_number]["history"].append(f"deposit: ₹{deposit}")
                  
         else:
             print("unable to deposit..!")

def show_bank():
     if len(bank)==0:
          print("account not found..!")
     else:
          
          print("\n-------------------ALL ACCOUNT----------------------")
          print("\n")
          for account_number,data in bank.items():
                print (f"account number : {account_number}")
                print (f"name           : {data["name"]}")                  
                print (f"balance        : ₹ {data["balance"]}")
                print (f"PIN            : {data["PIN"]}")
                print( f"age            : {data["age"]}")
                print( f"phone number   : {data["phone number"]}")
                print( f"Email          : {data["Email"]}")
                print( f"address        : {data["address"]}")
                print( f"account type   : {data["account type"]}")
               

                print("--------------------------------------")
def withdraw():
     account_number=int(input("enter the account number : "))
     if len(str(account_number))!=8:
          print("enter valid account number....")
          return
     pin=int(input("enter PIN :- "))
     print("-----------------------------------------------------")
     if len(str(pin))!=4:
          print("PIN must be 4 digits....")
          return
     if pin!=bank[account_number]["PIN"]:
         print("wrong PIN...")
         return
     else:
         withdraw=float(input("enter withdrawal amount : "))
         if account_number in bank:
          if withdraw<=bank[account_number]["balance"]:
              bank[account_number]["balance"]-=withdraw
              print("-----------------------------------------------------")
              print(f"₹{withdraw} withdrawal succsessfully..")
              print(f"total balance ₹{bank[account_number]["balance"]}")
              bank[account_number]["history"].append(f"withdraw: ₹{withdraw}")
          else:
              print("insufficent balance..!")

def check_balance():
     account_number=int(input("account Number :- "))
     pin=int(input("enter PIN :- "))
     print("-----------------------------------------------------")
     if len(str(pin))!=4:
          print("PIN must be 4 digits....")
          return
     if pin != bank[account_number]["PIN"]:
         print("wrong PIN...")
         return
     else :
      print(f"total balance : ₹ {bank[account_number]["balance"]}")

def transfer_amount():
     from_account=int(input("amount send from :- "))
     if len(str(from_account))!=8:
          print("account number must be 8 digits....")
          return
     print("-----------------------------------------------------")
     to_account=int(input(" amount recive in to :- "))
     if len(str(to_account))!=8:
          print("account number must be 8 digits....")
          return
     print("-----------------------------------------------------")
     amount=float(input("enter amount :- "))
     
     if from_account not in bank:
      print("transfer account not found....")
      return
     if to_account not in bank:
      print("reciver account not found..") 
      return
     if amount>bank[from_account]["balance"]:
         print("insufficient balance")
         return

     bank[from_account]["balance"]-=amount
     bank[to_account]["balance"]+=amount
     print("-----------------------------------------------------")
     print("mony transfer succsessfully..!")
     print("sender balance= ",bank[from_account]["balance"])
     print("reciver balance= ",bank[to_account]["balance"])
     bank[from_account]["history"].append(f"transfer: ₹{amount}")
     bank[to_account]["history"].append(f"recive: ₹{amount}")
     print("-----------------------------------------------------")

def valid_name(name):
     return name.replace(" ","").isalpha()          

def transation_history():
     account_number=int(input("enter account number :-  "))
     if account_number in bank:
          history=bank[account_number]["history"]
          if len(history)==0:
             print("transation not found..!") 
          else:
    
             print("\n----------------TRANSATION HISTORY-----------------")
             for transation in history:
               print(transation)
     else:
         print("account not found...")

def delete_account():
    account_number=int(input("enter account number to delete :- "))
    if account_number in bank:
        del bank[account_number]
        print("-----------------------------------------------------")
        print("account deleted successfully..!")
    else:
        print("account not found...")

def total_account():
    print("-----------------------------------------------------")
    print("total account in bank : ",len(bank))

def search_account():
    account_number=int(input("enter account number to search :- "))
    print("-----------------------------------------------------")
    if account_number in bank:
        data=bank[account_number]
        print(f"account number : {account_number}")
        print(f"name           : {data["name"]}")                  
        print(f"balance        : ₹ {data["balance"]}")
        print(f"PIN            : {data["PIN"]}")
        print( f"age            : {data["age"]}")
        print( f"phone number   : {data["phone number"]}")
        print( f"Email          : {data["Email"]}")
        print( f"address        : {data["address"]}")
        print( f"account type   : {data["account type"]}")       
    else:
        print("account not found...")

while True:
     print("\n|---|-----------------------------------------------|")
     print("|---|-----welcome to bank management system---------|")
     print("|---|-----------------------------------------------|")
     print("|1. |         ..create account..                    |")
     print("|---|-----------------------------------------------|")
     print("|2. |            ..deposit..                        |")
     print("|---|-----------------------------------------------|")
     print("|3. |           ..withdraw..                        |")
     print("|---|-----------------------------------------------|")
     print("|4. |         ..check balance..                     |")   
     print("|---|-----------------------------------------------|")
     print("|5. |         ..transfer amount..                   |")
     print("|---|-----------------------------------------------|")
     print("|6. |        ..transation history..                 |")
     print("|---|-----------------------------------------------|")     
     print("|7. |          ..delete_account..                   |")
     print("|---|-----------------------------------------------|") 
     print("|8. |          ..total_account..                    |")
     print("|---|-----------------------------------------------|") 
     print("|9. |           ..show_bank..                       |")
     print("|---|-----------------------------------------------|") 
     print("|10.|        ..search_account..                     |")
     print("|---|-----------------------------------------------|")  
     print("|11.|             ..EXIT..                          |")
     print("|---|-----------------------------------------------|") 

     choice=int(input("\n           make your choice : "))       
     print("-----------------------------------------------------")
     if choice==1:
         create_account()
     elif choice==2:
         deposit()
     elif choice==3:   
         withdraw()
     elif choice==4:
         check_balance()
     elif choice==5:
         transfer_amount()
     elif choice==6:
         transation_history()
     elif choice==7:
         delete_account()
     elif choice==8:
         total_account()       
     elif choice==9:
         show_bank()
     elif choice==10:
         search_account()
     elif choice==11:
         print("---LOG---OUT---")  
         break  
     else:
        print("---awww poor guy you are not make any decision---🤦‍♂️" ) 

# -----------------------------------------------------------------------------------------------------------------------------
# 3 - Quiz Game      

category={"football":{1:{"question":"\nHow many players are there in one football team on the field?","option":{"A":"9","B":"10","C":"11","D":"12"},"ans":"C"},
                      2:{"question":"\nWhich country won the FIFA World Cup in 2022?","option":{"A":"France","B":"Argentina","C":"Brazil","D":"Germany"},"ans":"B"},
                      3:{"question":"How long is a standard football match, excluding extra time?","option":{"A":"60 minutes","B":"80 minutes","C":"90 minutes","D":"120 minutes"},"ans":"C"},
                      4:{"question":"Which player is allowed to use their hands inside their own penalty area?","option":{"A":"Defender","B":"Goalkeeper","C":"Midfielder","D":"Striker"},"ans":"B"},
                      5:{"question":"How many halves are there in a standard football match?","option":{"A":"2","B":"3","C":"4","D":"5"},"ans":"A"}},

           "GTA 6":{  1:{"question":"What is the name of the female protagonist in GTA 6?","option":{"A":"Lara","B":"Lucia","C":"Maria","D":"Sophia"},"ans":"B"},
                      2:{"question":"What is the name of the male protagonist who is shown alongside Lucia?","option":{"A":"Jason","B":"Michael","C":"Franklin","D":"Trevor"},"ans":"A"},
                      3:{"question":"In which fictional state is GTA 6 primarily set?","option":{"A":"San Andreas","B":"Liberty State","C":"Leonida","D":"North Yankton"},"ans":"C"},
                      4:{"question":"Which fictional city returns in GTA 6?","option":{"A":"Vice Cit","B":"Los Santos","C":"Liberty City","D":"Las Venturas"},"ans":"A"},
                      5:{"question":"ich company is developing GTA 6?","option":{"A":"Ubisoft","B":"Rockstar Games","C":"Electronic Arts","D":"Activision"},"ans":"B"}}}

print("\n===== QUIZ GAME =====\n")

print("Available Categories:")

categories = list(category.keys())

for i, name in enumerate(categories, 1):
    print(f"{i}. {name}")


while True:

    try:
        choice = int(input("\nSelect category: "))

        if 1 <= choice <= len(categories):
            selected_category = categories[choice - 1]
            break
        else:
            print("Please select a valid category.")

    except ValueError:
        print("Please enter a number.")


print(f"\nYou selected: {selected_category.upper()}")
print("-" * 40)



questions = category[selected_category]

score = 0


for number, data in questions.items():

    print(f"\nQuestion {number}:")
    print(data["question"])

    print()



    for option, value in data["option"].items():
        print(f"{option}. {value}")

    while True:

        answer = input("\nYour answer (A/B/C/D): ").upper()

        if answer in data["option"]:
            break
        else:
            print("Please enter A, B, C or D.")


    if answer == data["ans"]:

        print("Correct!")
        score += 1

    else:

        correct_answer = data["ans"]

        print("Wrong!")
        print(
            f"Correct answer: "
            f"{correct_answer}. "
            f"{data['option'][correct_answer]}"
        )

total_questions = len(questions)

print("\n" + "=" * 40)
print("QUIZ COMPLETED")
print("=" * 40)

print(f"Your Score: {score}/{total_questions}")

percentage = (score / total_questions) * 100

print(f"Percentage: {percentage:.2f}%")

if percentage == 100:
    print("Excellent!")

elif percentage >= 60:
    print("Good job!")

else:
    print("Keep practicing!")

# -----------------------------------------------------------------------------------------------------------------------------
# 4 -       Weather App (API)

import requests

api_key= "cf0b8c727bc2d005bacfbdbe8dbbe87e"
base_url="https://api.openweathermap.org/data/2.5/weather"

while True:
    print("\n=====weather app menu=====\n")
    print("1. single city weather")
    print("2. multiple city weather")
    print("3. Exit")
    print("==========================")
    choice=int(input("\nselact option : "))

    weather={}
    citys=set()
    if choice==3:
          print("exiting weather app..")
          break
    elif choice==1:
        city=input("enter city name : ")
        params={"q":city ,"appid":api_key ,"units":"metric"}
        print("fetching weather data...")
        response =requests.get(base_url,params=params)
        if response.status_code==200:
            data=response.json()
            print("\n====== WEATHER SUMMARY ======")
            print(f"\ncity : {city}")
            print("-"*30)
            print(f"temperature : {data["main"]["temp"]} °C")
            print(f"weather     : {data["weather"][0]["description"]}")
            print(f"humidity    : {data["main"]["humidity"]}")
            print(f"wind speed  : {data["wind"]["speed"]}")
            print("-"*30)
            break
        else:
            print("can not found !")
            continue
    elif choice==2:
     while True:
              try : 
                  num_citys=int(input("\n how many city to check (1-4) : "))
                  if num_citys<1 or num_citys>4:
                      print ("invalid input ! please enter number between 1 to 4 ")
                      continue
                  break
              except ValueError:
                      print("invalid input ! please enter number valid input")
                      continue
                      
     for num in range(num_citys):
              while True:
                   city=input(f"enter the city name {num+1} : ")      
                   if not city.strip():
                        print("city name can not be empty")
                        continue   
                   params={"q":city ,"appid":api_key ,"units":"metric"}
                   print("fetching weather data...")
                   response =requests.get(base_url,params=params)
                   if response.status_code==200:
                         citys.add(city.strip())
                         data=response.json()
                         weather[city]=data
                         break
                   else:
                         print("can not found !")
                         continue
     citys=sorted(citys)            
     print("\n============================ WEATHER SUMMARY ============================")
     print(f"{'\nNo. ':<5}{'city':15}{'temperature':13}{'weather':20}{'humidity':10}{'wind speed':10}")
     print("-"*73)
     for city in citys:
            print(f"{list(citys).index(city)+1:<5}",end="")
            print(f"{city:15}",end="")
            print(f"{str(data["main"]["temp"]) + "°C":<13}",end="")
            print(f"{data["weather"][0]["description"]:<20}",end="")
            print(f"{data["main"]["humidity"]:<10}",end="")
            print(f"{data["wind"]["speed"]:<10}")
            print("-"*73)
    else:
            print("invalid choice! please selact a vaild option (1-3)..")
            continue


