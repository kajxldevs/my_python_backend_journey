import os
import json

def LoadWorkout():
    if os.path.exists("Workout.json"):
        with open ("Workout.json","r") as f:
            return json.load(f)
    return{}

def GetPlan(Phase,Equipment,BodyPart):
    Data=LoadWorkout()
    PhaseData=Data[Phase]
    EqiPlan=PhaseData[Equipment]
    Target=EqiPlan[BodyPart]
    return Target

if __name__ == "__main__":
    Plan = GetPlan("Menstrual", "Gym", "Upper")
    for exercise in Plan:
        print(exercise)