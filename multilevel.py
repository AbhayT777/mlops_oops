class gparent():
    def __init__(self, name):
        self.name = name

    def g(self):
        print(self.name + " is telling a story")

class parent(gparent):
    
    def p(self):
        print(self.name + " is working")


class child(parent):

    def c(self):
        print(self.name + " is playing")

c1 = child("sonu")

c1.g()
c1.p()
c1.c()