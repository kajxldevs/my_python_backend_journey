"""Problem — The CycleFit Logger
In CycleFit, every time a user's data is saved, you want to log it — print when saving started and when it's done.
You have this function —
pythondef save_user_data():
    print("Saving Kajal's cycle data...")
Your job —
Write a decorator called logger that prints —

"Log: Starting process..." — before
"Log: Process complete! ✅" — after

Then decorate save_user_data with it and call it.
Expected output —
Log: Starting process...
Saving Kajal's cycle data...
Log: Process complete! ✅""" 

def decorator(func):
    def wrap():
        print("Starting process...")
        func()
        print("Process complete!")
    return wrap

@decorator    
def save_user_data():
    print("Saving Kajal's cycle data...")

#save_user_data=decorator(save_user_data)
save_user_data()
