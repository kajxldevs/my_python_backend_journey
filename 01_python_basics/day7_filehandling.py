f=open("orders.txt","w")
f.write("\nSandwich")
f.write("\nCoffee")
f.write("\nsoda")
f.close()
print("Order saved")

f=open("orders.txt","r")
contents=f.read()
f.close()
print(contents)

with open ("orders.txt","r") as f:
    contents=f.read()
    print(contents)

import json
student={
 "name":"kajal",
 "roll no":17,
 "marks":"9.36 spga",
 "branch":"Computer Science"
}
with open ("student.json","w") as f:
    json.dump(student,f)   
print("\n\nStudent data saved")

with open ("student.json","r") as f:
    student=json.load(f)
print ("Name:",student["name"])