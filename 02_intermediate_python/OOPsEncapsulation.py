#PRIVATE
print("PRIVATE")  #--->Can be only accessed within a class
class person:
    #constructor
    def __init__(self,name,age):
        self.__name=name  #for private variable
        self.__age=age
    
    def display(self):
        print(f"The name is {self.__name} and the age is {self.__age}")


p=person("Kajal",19) 
#print(person.__name)----------->This will show error saying'person' object has no attribute '__name'
print("To access it")
p.display()

dir(person)
#print(person._Person__name)
#not a good practice