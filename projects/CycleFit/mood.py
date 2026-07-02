import json
import os
from datetime import datetime

def GetTodayMood():
    Mood = input("How are you feeling today? (Low/Okay/Good/Great): ")
    Energy = int(input("Rate your energy 1-10: "))
    return Mood, Energy

def SaveMood(Mood, Energy):
    Today = datetime.today().strftime("%d/%m/%Y")
    Entry = {"date": Today, "mood": Mood, "energy": Energy}
    
    if os.path.exists("mood_log.json"):
        with open("mood_log.json", "r") as f:
            Log = json.load(f)
    else:
        Log = []
    
    Log.append(Entry)
    
    with open("mood_log.json", "w") as f:
        json.dump(Log, f)

def LoadMoods():
    if os.path.exists("mood_log.json"):
        with open("mood_log.json", "r") as f:
            return json.load(f)
    return []

if __name__ == "__main__":
    Mood, Energy = GetTodayMood()
    SaveMood(Mood, Energy)
    print(LoadMoods())