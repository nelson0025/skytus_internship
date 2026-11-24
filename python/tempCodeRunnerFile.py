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


