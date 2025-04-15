class parent():
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("hello, my name is "+self.name)


class child(parent):

    def greet(self):                   # method overloading
        print(self.name + " is playing")

c1 = child("babu")
# p1 = parent("ram")

c1.greet()
# p1.greet()