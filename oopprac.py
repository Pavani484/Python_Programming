
class Computer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def com(self,name,age):
        print("Computer")
        print(self.name,self.age)
        print(name,age)
comp1=Computer("lalli",20)
comp1.com("lalli",16)
#........................
class Computer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # method defined inside constructor
        def com():
            print("Inside constructor method")
            print(self.name, self.age)

        # call it immediately
        com()

comp1 = Computer("lalli", 20)
#...................
class Computer:
    def __init__(self):
        self.name="pavani"
        self.age=18
    def update(self):
        self.age=23
        print(self.name,self.age)
    def compare(self,other):
        if self.name==other.name:
            return True
        else:
            return False
c1=Computer()
c2=Computer()
if c1.compare(c2):
    print("they are the same")
c1.name="lalli"
c1.age="20"
c1.update()
print(c1.name)
print(c2.name)
#.....................


