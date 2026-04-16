import random
print(random.randint(1,20))
print(random.choice(["sandwich","coffee","tea"]))

print("\nImport math")
import math
print(math.sqrt(100))
print(math.ceil(3.1))
print(math.floor(2.62))
print(math.pi)

print("\os")
import os
if os.path.exists("student.json"):
    print("File found!")
else:
    print("File not found!")

print("\ndate time")
from datetime import datetime
now = datetime.now()
print(now)
