UserData={
    "name":"Kajal",
    "age":19,
    "weight": 68.8,
    "height": 157,
    "activity_level":"moderate-4x a week",
    "recent_period":"28/03/2026",
    "diet":"Pure veg"
}

#For each variable i am writing 'em as title format, first letter in uppercase 
import json
import os
from datetime import datetime

def LoadUser():
    if os.path.exists("data.json"):
        with open("data.json","r") as f:
            return json.load(f)
    return{}

def SaveUser(User):
    with open("data.json","w") as f:
         json.dump(User,f)
SaveUser(UserData)
Data=LoadUser()
print(Data)
