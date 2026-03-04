"""
a=input("enter a number:")
print(type(a))
#.....
"""
"""
a=3
b=4
a=a+b
b=a-b
a=a-b
print("a:",a,"b:",b)
#...........


name = input("Enter name of the student: ")
subjects = int(input("Enter the number of subjects: "))

marks = [] 
subject_grades = [] 

def get_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 75:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 35:
        return "D"
    else:
        return "Fail"


for i in range(subjects):
    m = int(input(f"Enter marks for subject {i+1} (out of 100): "))
    if m < 0 or m > 100:
        print("Invalid marks! Please enter a value between 0 and 100.")
        exit()
    marks.append(m)
    subject_grades.append(get_grade(m))


total = sum(marks)
average = total / subjects
overall_grade = get_grade(average)


if all(m >= 35 for m in marks):
    result = "PASS"
else:
    result = "FAIL"
print("\n--- Student Report ---")
print("Name:", name)
print("\nSubject-wise Details:")
for i in range(subjects):
    print(f"Subject {i+1}: Marks = {marks[i]}, Grade = {subject_grades[i]}")

print("\nTotal Marks:", total)
print("Average Marks:", round(average, 2))
print("Overall Grade:", overall_grade)
print("Result:", result)
#.....................

print("convert celcius to farenheit and vice versa")
a=float(input("enter temperature in celcius:"))
b=float(input("enter temperature in farenheit:"))
f=(a*9/5)+32
c=(b-32)*5/9
print(f)
print(c)
#.....................

print("area of rectangle")
l,b,h=map(int,input("enter length,breath and height of a rectangle").split())
R=l*b*h
print("area of the rectangle is:",R)
#.....................

print("check if a number is even or odd")
a=int(input("enter a number"))
if(a%2==0):
    print("even")
else:
    print("odd")
#.....................

print("remainder and quotient of two numbers")
a,b=map(int,input("enter two numbers:").split())
c=a/b
d=a%b
print("quotient:",c)
print("remainder:",d)
#.....................

while True:
    try:
        a, b = map(int, input("Enter two numbers separated by space: ").split())
        break
    except ValueError:
        print(" Please enter valid numbers only.")
try:
    print("Quotient:", a // b)
    print("Remainder:", a % b)
except ZeroDivisionError:
    print(" Division by zero is not allowed.")
#.....................

print("largest among three numbers")
a,b,c=map(int,input("enter three number:").split())
if(a>b and a>c):
    print("a is largest:",a)
elif(b>c):
    print("b is largest:",b)    
else:
    print("c is largest:",c)    
#.....................
print("check if a number is positive,negative or zero")
a=int(input("enter a number:")) 
if(a>0):
    print("positive")
elif(a<0):
    print("negative")
else:
    print("zero")   
#.....................

print("check leap year")
a=int(input("enter a year:"))
if(a%4==0 and a%100!=0)or(a%400==0):
    print("leap year")
else:
    print("not a leap year")
#.....................
print("pattern")
r=5
c=r-1
for i in range(r):
    for j in range(c-i):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    print()
#.................

print("Create a Student class with attributes like name, roll number, and marks. Add a method to display student details")
class Student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def display_details(self):
        print(self.name,self.roll_number,self.marks)
s1=Student("pavani",68,958)
s1.display_details()
#.....................


print("to create a Rectangle class and calculate its area and perimeter.")
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
r1=Rectangle(5,10)
print("Area:",r1.area())
print("Perimeter:",r1.perimeter())
#.....................
"""
print("to create a Circle class and calculate its area and circumference.")
import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    def circumference(self):
        return 2*math.pi*self.radius
c1=Circle(7)
print("Area:",c1.area())
print("Circumference:",c1.circumference())
#.....................
