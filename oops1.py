# initializing a class
class Employee:
    # __init__ is a special method/magic method/dunder method , also called as constructor
    def __init__(self):
        print("atributes are called by itself when an object is created")
        self.id = 123
        self.sal = 500000
        self.design = "sde"
        print("atributes are called")
    # initializing a method
    def travel(self, dest):
        print("methods are called manually")
        print("employee have to go "+ dest)

sam = Employee() #creating an object
print(sam.id)
sam.travel("pune") #calling the method
