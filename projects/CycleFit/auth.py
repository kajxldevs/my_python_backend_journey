import json
import os
import hashlib

def HashPassword(Password):
    return hashlib.sha256(Password.encode()).hexdigest()

def Signup(Username, Password):
    
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            Users = json.load(f)
    else:
        Users = []

    
    for User in Users:
        if User["username"] == Username:
            return "Username already exists!"

    
    NewUser = {"username": Username, "password": HashPassword(Password)}
    Users.append(NewUser)
    with open("users.json", "w") as f:
        json.dump(Users, f)
    return "Signup successful!"

def Login(Username, Password):
    
    if not os.path.exists("users.json"):
        return "No users found. Please signup first."

    with open("users.json", "r") as f:
        Users = json.load(f)

    
    for User in Users:
        if User["username"] == Username:
            if User["password"] == HashPassword(Password):
                return "Login successful!"
            else:
                return "Wrong password!"

    return "Username not found!"

if __name__ == "__main__":
    print(Signup("Kajal", "kajal123"))
    print(Login("Kajal", "kajal123"))
    print(Login("Kajal", "wrongpassword"))