from datetime import datetime

def  Phase(Perioddate):
    Start=datetime.strptime(Perioddate,"%d/%m/%Y")
    Today=datetime.today()
    DaysPassed= (Today- Start).days
    Current=(DaysPassed%28)

    if (Current<=5):
        Phase=("Menstrual")
    elif (Current<=13):
        Phase=("Follicular")
    elif (Current<=16):
        Phase=("Ovulatory")
    else:
        Phase=("Luteal") 

    return(Current,Phase)

if __name__ == "__main__":
    CycleDay, Phase = Phase("28/03/2026")
    print(f"Cycle Day: {CycleDay} — Phase: {Phase}")