marks = [45, 78, 32, 89, 55, 91, 23, 67]
passed=[]
for p in marks:
    if p>=40:
      passed.append(p)
print(passed)

score=[mark for mark in marks if mark >=40]
print(score)

#Example 1 — Attendance Alert 
print("\nExample 1")
attendance = [82, 65, 91, 70, 55, 88, 73]
attend=[a for a in attendance if a<75]
print(attend)

print("\nExample 2 - Transform Every Item")
marks_50 = [23, 45, 38, 50, 29]
marks_100= [m*2 for m in marks_50]
print(marks_100)

print("\nExample 3 — Strings")
names= ["rohAn ","NaINA","GAyaTri","AadItiYA"]
name= [n.strip().title() for n in names]
print(name)

print("\nExample 4 — Both Transform AND Filter")
students = [("Sneha", 78), ("Rohan", 35), ("Priya", 82), ("Arjun", 29)]
passed_stud = [name.upper() for name,marks in students if marks >40 ]
print(passed_stud)

print("\n\nPRACTICE EXAMPLES")
print("Example 1")
subjects = ["mathematics", "physics", "chemistry", "english", "computer science"]
#Use list comprehension to get a new list where every subject name is in uppercase.
sub=[sub.upper() for sub in subjects]
print(sub)

print("\nExample 2")
cgpa = [6.5, 8.2, 7.1, 9.0, 5.8, 8.8, 6.9]
#The club only allows students with CGPA above 7.5. Get that filtered list.
result=[r for r in cgpa if r>=7.5]
print(result)

print("\nExample 3")
student = [("Aditya", 8.9), ("Meera", 6.2), ("Kabir", 7.8), ("Riya", 5.5)]
#Get only the names (not CGPA) of students who have CGPA above 7.0. Names should be in title case.
stud=[s.title() for s, cgpa in student if cgpa >=7.0]
print(stud)

print("Day 10 completed successfully!")
print("I have understood List Comprehensions .")
print("Tomorrow I will learn Lambda, Map, Filter.")