print("Truple")
#Kajal runs a snacks center. her menu is constant and never changes
menu=("coffee","sandwich","soda","ice creams")
print("Item no 1:",menu[0]) #Item no 1: coffee
#looks like list but list is always written in [],truple is (), we cannot change it
#print("\nWe cannot change Truple.Example")
#menu[0]="chai" #error
print("\n\nSets")
visitors=["Kajal","Devansh","Gunjan","Vishal","Rishab","Harshika","Kajal","Rishab"]
uvis=set(visitors)
print(uvis)
print("\nAdding to sets")
uvis.add("Aarav")
print(uvis)

# Checking membership — FASTER than lists
print("\nChecking membership")
if "Kajal" in uvis:
    print("Kajal visited today!!")

#set operations
morning_costumers={"Kajal","Devansh","Gunjan","Vishal"}
evening_costumers={"Vishal","Rishab","Harshika","Kajal"}

Both_time=morning_costumers & evening_costumers
print(Both_time)

either_time= morning_costumers | evening_costumers
print(either_time)

only_morning=  morning_costumers - evening_costumers
print(only_morning)

print("\n\n Strings")
"  vada pav  "
"MISAL pav"
"chai,vada pav,misal"
#the above list is messy
order="  vada pav"
print(order.strip()) #strip() removes spaces
print(order.title())
order="MISAL pav"
print(order.lower()) #prints in lower case
print(order.upper()) #prints in upper case
print(order.title()) #prints it in title format with upper case for each word

orders="chai,wada pav,misal "
items=orders.split(",")
print(items[0])

order="vada pav is bad"
print(order.replace("bad","good"))

email = "kajal@gmail.com"
print(email.startswith("kajal"))
print(email.endswith(".com"))
print("y" in email)
print("a" in email)

print("\nExample 1")
#Create a tuple of 4 Indian cities
cities=("Pune","Kota","Gangapur","Indore")
#Try to change one value and see the error
#cities[1]="Jaipur"
#print(cities[1])
#Print it with a comment explaining why tuples exist= IT has items which cannot be changed. we use it for fixed itmes.
print("\nExample 2")
fruits=["apple", "banana", "apple", "mango", "banana", "apple"]
#Convert to set, print unique items and count
fruit=set(fruits)
print(fruit)
print(len(fruit))
#Add "grapes", check if "banana" exists
fruit.add("grapes")
print(fruit)
if "banana" in fruit:
    print("banana is present")
print("\nExample 3")

#Take this messy input: "  KAJAL SINGH  "
name=("  KAJAL SINGH " )
#Strip spaces, convert to lowercase, then title case
print(name.strip()) 
print(name.lower())
print(name.title())
#Split "python,fastapi,databases,deployment" into a list
language="python,fastapi,databases,deployment"
lang=language.split(",")
print(lang)
#Join it back with → between each item
print(" -> ".join(lang))

print("\nDay 6 completed successfully!")
print("I have understood truple,sets and string operations")
print("Tomorrow I will learn File Handling + JSON.")