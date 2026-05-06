class User:
    def __init__(self,name,age,cycle_day):
        self.name=name
        self.age=age
        self.cycle_day=cycle_day

    def greet(self):
      print("Hello i am "+ self.name + " and I am on cycle day " + str(self.cycle_day))

User1=User("kajal",19,2)
print(User1.name)
print(User1.age)
print(User1.cycle_day)
User1.greet()

User2=User("Priya", 21, 5)
print(User2.name)
print(User2.age)
print(User2.cycle_day)
User2.greet()

print("INHERITANCE")
class AdminUser(User):
    def delete_account(self, target_name):
        print(self.name + " deleted " + target_name + "'s account")
    def greet(self):
        print(f"Hello! i am {self.name} And i am admin on {self.cycle_day}")
admin = AdminUser("Kajal", 19, 2)
admin.greet()  # inherited from User
admin.delete_account("Priya")  # her own method
admin.greet()