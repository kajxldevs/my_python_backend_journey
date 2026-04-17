import json
import os
from datetime import datetime

def load_members():
 if os.path.exists("members.json"):
  with open ("members.json","r") as f:
   return json.load(f)
 return{}

def save_members(members):
 with open ("members.json","w") as f:
  json.dump(members, f) 
 
def add_members(members):
  no=input("Enter member no. =")
  if no in members:
    print("Member with this number already exists!")
    return
  name=input("Enter name= ")
  jdate = datetime.now().strftime("%d-%m-%Y")
  phone=input("Enter phone number=")
  members[no] = {"name": name,"phone": phone}
  save_members(members)
  print("New member added sucesfully!")

def view_members(members):
  no=input("Enter member number")
  if no in members:
    print(f"Name= {members[no]['name']}\nPhone= {members[no]['phone']}")
  else:
    print("Member not found!")

def update_members(members):
 no=input("Enter member number: ")
 if no not in members:
  print("Member not found!")
  return
 phone = input("New phone (press enter to skip): ")
 if phone:
    members[no]["phone"] = phone
    save_members(members)
    print("Updated!")
 
def delete_members(members):
    no = input("Enter member number: ")
    if no in members:
        del members[no]
        save_members(members)
        print("Member deleted!")
    else:
        print("Member not found!")

def main():
  mem=load_members()
  while True:
    print("GYM MEMBERSHIP RECORD SYSTEM")
    print("\n1.Add Member")
    print("2.View member")
    print("3.Update Member")
    print("4.Delete Member")
    print("5.Exit")
    choice= input("Enter here: ")
    if choice=="1": 
     add_members(mem)
    elif choice=="2":
     view_members(mem)
    elif choice=="3": 
     update_members(mem)
    elif choice=="4": 
     delete_members(mem)
    elif choice=="5": 
       break 
main()