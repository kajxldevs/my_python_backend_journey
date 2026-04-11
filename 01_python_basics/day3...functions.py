def greet(name="stranger"):
    print("Hello," + name)
greet("Kajal")
greet ()

def add (a,b):
 return a+b
result= add (5,3)
print(result)

def mp(a,b,c):
   return a*b*c
result=mp(3,5,2)
print(result)

#Addition and substraction
def calculator (a,b,op="add"):
   if op=="add":
      return a+b
   elif op == "sub":
      return a-b
   else:
    return ("Unknown operation")
result= calculator (10,5)
print(result)
result= calculator (10,5,"sub")
print(result)

print("Day 3 completed successfully!")
print("I have understood functions")
print("Tomorrow I will learn list and Loops .")