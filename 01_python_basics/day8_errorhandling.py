#num= int(input("Number :")) #hello
#print("double:",num*2) #invalid literal for int() with base 10: 'hello'

print("try and Except")
try:
 num=int(input("Number:"))
 print=("double=",num*2)
except ValueError:
 print("That's not a number!")

try:
 num=int(input("Number:"))
 print=("double=",num*2)
except Exception as e:
 print("That's not a number!", e)

print("\nelse and finally")
try:
 num=int(input("Number:"))
except ValueError:
 print("That's not a number!")
else:
 print("Double is:", num*2)
finally:
 print("Program completed")