import json
import os
from datetime import datetime

class user:
    def __init__(self, Name, Age, Weight, Height, ActivityLevel, RecentPeriod, Diet):
        self.Name = Name
        self.Age = Age
        self.Weight = Weight
        self.Height = Height
        self.ActivityLevel = ActivityLevel
        self.RecentPeriod = RecentPeriod
        self.Diet = Diet

    def SaveUser(self):
        with open("data.json", "w") as f:
            json.dump(self.__dict__, f)
            
    def LoadUser(self):
        with open("data.json","r") as f:
             return json.load(f)

Kajal = user("Kajal", 19, 68.8, 157, "moderate-4x a week", "28/03/2026", "Pure veg")
Kajal.SaveUser()
Kajal.LoadUser()
print(Kajal.LoadUser())