print ("LEARNING LOOPS-for loop")
print ("Example 1")
colors=["Red","Green","White","Purple","Black","Indigo","pink","silver"]
for i in colors :
    print(i)

print() 
print ("Example 2")
colors=["Red","Green","White","Purple","Black","Indigo","pink","silver"]
for i in range(len(colors)):
     print(f"Color: {i+1}:{colors[i]}")

print("LEARNING LOOPS - while loop")
print("Example 1")

i = 1
while i <= 5:
    print(f"number is {i}")
    i += 1

print("\nExample 2 - Countdown")

count = 8
while count > 0:
    print(f"Number is: {count}")
    count -= 1          # This line MUST be indented with 4 spaces