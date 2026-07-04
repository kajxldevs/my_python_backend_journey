from user_profile import user
from bmi import CalculateBMI
from Cycle import Phase as GetCyclePhase
from Workout import GetPlan
from mood import GetTodayMood, SaveMood
from auth import Login, Signup

def main():
    print("\nWelcome to CycleFit \n")
    Choice = input("1. Login  2. Signup: ")
    
    if Choice == "2":
        Username = input("Enter username: ")
        Password = input("Enter password: ")
        print(Signup(Username, Password))
    
    Username = input("Enter username: ")
    Password = input("Enter password: ")
    Result = Login(Username, Password)
    print(Result)
    
    if Result != "Login successful!":
        return

    # Load profile
    UserData = user("Kajal", 19, 68.8, 157, "moderate-4x a week", "28/03/2026", "Pure veg")
    Data = UserData.LoadUser()

    # BMI
    BMI, Category = CalculateBMI(Data["Weight"], Data["Height"])
    CycleDay, Phase = GetCyclePhase(Data["RecentPeriod"])

    # Mood
    print("\nLet's check in on how you're feeling today!")
    Mood, Energy = GetTodayMood()
    SaveMood(Mood, Energy)
   

    # Workout
    print("\nWorkout preference:")
    Equipment = input("Gym or Home?: ").capitalize()
    BodyPart = input("Upper or Lower?: ").capitalize()
    Plan = GetPlan(Phase, Equipment, BodyPart)

    print(f"\n Your {Phase} Phase — {Equipment} {BodyPart} Workout:\n")
    for Exercise in Plan:
        print(f"  ✅ {Exercise}")

    if Energy <= 4:
        print("\n Energy is low today — consider lighter weights and listen to your body!")

if __name__ == "__main__":
    main()