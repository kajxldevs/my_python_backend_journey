#normally we write
def square(x):
    return x*x

#In Lamda we write it as
square=lambda x: x*x  #lambda <input> : <what to return>

print("Syntax: \nlambda <input> : <what to return>")
print("\n\nExample")
square = lambda x: x * x
print(square(5))

print("\n\nExample with two numbers:")
sum = lambda x,y:x+y
print(sum(3,4))

#Problem 1
print("\n\nPROBLEM 1")
#Write a lambda that takes a number and returns True if it's even, False if it's odd.
is_even= lambda x: x%2==0
print(is_even(4))
print(is_even(7))

print("\n\n\nMAP")
scores = [3, 7, 2, 8, 5]
result=list(map(lambda x:x*2,scores))
print(result)

print("\n\nPROBLEM 2")
"""These are raw scores. 
But you want to show the user a boosted score — 
multiply every mood score by 1.5 to show a "potential mood" 
if they follow their cycle recommendations."""
mood_scores = [6, 4, 8, 3, 7]
potential_mood=list(map(lambda x: x*1.5,mood_scores))
print(potential_mood)

print("\n\n\nMAP")
numbers = [1, 6, 3, 8, 2, 7]
num=list(filter(lambda x:x>4,numbers))
print(num)
print("\n\nPROBLEM 3")
#Users who have a mood score less than 5 need extra care — CycleFit wants to flag them.
low= list(filter(lambda x:x<5,mood_scores))
print(low)

print("\n\nPROBLEM 4")
energy_scores = [8, 3, 6, 2, 7, 4, 5]
low_energy=list(filter(lambda a:a<5,energy_scores))
print(low_energy)
recovery=list(map(lambda a:a*2,low_energy))
print(recovery)