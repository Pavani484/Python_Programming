"""
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
#..................

class Pavani:
    wheels=16
    def __init__(self,name,age):
        self.name=name
        self.age=age
c1=Pavani("lalli",20)
print(c1.name,c1.age)
print(c1.name,c1.wheels)
#..................


class Student:
    school='ZPHS'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def display(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def display2(cls):
        return cls.school
    @staticmethod
    def display3():
        print("hello pavani")
        print(Student.school)
s1=Student(1,2,3)
s2=Student(4,5,6)
print(s1.display())
print(s2.display())
print(s1.display2())
Student.display3()
#..................


class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        #self.lap=self.Laptop(8,"hp")
        ram, brand = input("Enter laptop RAM and brand: ").split()
        ram = int(ram)
        self.lap = self.Laptop(ram, brand)
    def show(self):
        print(self.name, self.roll)
        self.lap.show()
    class Laptop:
        def __init__(self,ram,brand):
            self.ram=ram
            self.brand=brand
        def show(self) :
            print(self.ram,self.brand)
s1=Student("lalli",20)
s1.show()
#.................
class A:
    def feat1(self):
        print("feat1")
    def feat2(self):
        print("feat2")
class B(A):
    def feat3(self):
        print("feat3")
    def feat4(self):
        print("feat4")
class C(A):
    def feat5(self):
        print("feat5")
a1=B()
a1.feat3()
a1.feat4()
a1.feat1()
#..................
"""
"""
a=25
b=23
print(a+b)
print(int.__add__(a,b))
print(int.__sub__(a,b))
#..................

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+self.m2
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3
    def __gt__(self,other):
        s1=self.m1+self.m1
        s2=other.m2+other.m2
        if s1>s2:
            return True
        else:
            return False
s1=Student(10,40)
s2=Student(30,20)
s3=s1+s2
print(s3.m1,s3.m2)
if s1>s2:
    print(" s1 wins")
else:
    print(" s2 wins")
#............
"""


