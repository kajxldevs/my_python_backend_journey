#When using lists we write something as
print("Using lists")
User= ["Kajal", 19,"kajal435@gmail.com",True]
print("Name-",User[0])
print("Age-",User[1])
print("e-mail id-",User[2])
print("Is active-",User[3])

#But what if list is big, so we use dictionaries
print("\nUsing Dictionaries")
User= {
    "name":"Kajal",
    "age": 19,
    "e-mail":"kajal435@gmail.com",
    "is_active": True
}
print("\nAccess")  #Access
print(User["name"]) #Kajal
print(User["age"])  #19

print("\nAdd and Update") 
User["city"]="Pune" #Adding
print(User["city"]) 
User["age"]=20 #updating
print(User["age"]) 

print("\n Delete")
del User["is_active"]

print("\nCheck if key exists")
print("checking if name exists")
if "name" in User:
    print("User found")
else:
    print("User not found!")
print("\nchecking if user is active")
if User["age"]>18:
    print("User is Adult!")
else:
    print("User is minor")
print()
for key,value in User.items():
    print(key,"-",value)

print("\n\n Example 1")
#Create a student dictionary with keys: name, age, cgpa, city
Student={
    "name":"Kajal",
    "age": 19,
    "cgpa": 9.36,
    "city":"Kota"
}
#Print only the cgpa
print(Student["cgpa"]) #9.36
#Update the city to "Pune"
Student["city"]="Pune"
print(Student["city"]) #Pune
#Loop through and print every key → value pair
for key, value in Student.items():
    print(key,"->",value)

User["skills"]=["C","C++","Python","Django"]
print(User["skills"][1]) #c++

print("\nDay 5 completed successfully!")
print("I have understood dictionaries")
print("Tomorrow I will learn Tuples and Sets.")