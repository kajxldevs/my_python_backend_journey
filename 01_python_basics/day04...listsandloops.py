#A list is one variable that holds multiple values.
print("\nBasic example") #Basic example
friends= ["Naina","Aaditiya","Tanvi","Aayush","Gayatri"]   
print(friends[0]) #Naina
print(friends[-2]) #just in case i want last item (name of last friend here), but i dont know the last number
#Aayush


#Adding
print("\nAdding new item- 1.append")
friends.append("Kajal")
print(friends) #always adds to the end  

#deleting
print("\nAdding new item- 2. insert")
friends.insert(2,"Dev")
print(friends) #can insert in middle

print("\nDelete- 1.remove")
friends.remove("Gayatri")
print(friends)

print("\nDelete- 2.pop")
friends.pop(3) #pop when we know index number
print(friends)
print()
friends.pop() # no value= last item gets delete
print(friends)

#number of items in list
print("/nNumber of items in list")
print(len(friends)) #to know number of items in list

#loops 
print("\nFor loop")
for friend in friends:
    print(friend)

print("\nEnumerate") #when we want index number too
for index,friend in enumerate(friends):
 print(index, friend,)

print("\nEXAMPLE 1")
languages = ["Python", "C", "C++", "JavaScript", "Java"]
"""Print the first language
Print the last language using negative index
Add "Rust" to the end
Print the total count of languages
Loop through and print all languages
Loop through and print with rank starting from 1 using enumerate
Print the length after adding Rust"""

print(languages[0]) #Python
print(languages[-1]) #Java
print(len(languages)) #5
languages.append("Rust")
print(languages[-1]) #Rust
for lang in languages:
   print(lang) #python,C,C++,Javascript,Java,Rust
for index, Language in enumerate(languages):
    print(index,Language) #0.python,1.C,2.C++,3.Javascript,4.Java,5.Rust
print(len(languages)) #6

print("\nDay 4 completed successfully!")
print("I have understood lists")
print("Tomorrow I will learn dictionaries.")