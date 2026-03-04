"""a="hello"
b=len(a)
sum=0
for i in range(b-1):
    s=(abs(ord(a[i])-ord(a[i+1])))
    sum=sum+s
print(sum)

a=["X++","++X","--X","X--"]

x=0
for i in a:
    if (i == "--X" or i=="X--"):
        x=x-1
    if(i=="X++" or  i == "++X"):
        x=x+1

print(x)




a="1.1.1.1"
l=len(a)
s=""
for i in range(l):
    if(a[i]=="."):
        s=s+"[.]"
    else:
        s=s+a[i]
print(s)

r=4
c=5
for i in range(r):
    for j in range(c):
        if(i==0 or j==0 or i==r-1 or j==c-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")




j="diii"
s="diaidi"
m=""
for i in j:
    #print(i)
    m=j[i]
    for k in s:
        print(k)
a=[111,2,34,4,5,10,2,3,4,9,]
b=len(a)
l=0
for i in range(b):
    l=a[0]
for i in range(b):
    if(a[i]>l):
        l=a[i]
print(l)
jewels="aA"
stones="aAAvvv"
c=0
for i in jewels:
    for j in stones:
        if(i==j):
            c=c+1
print(c)

jewels="aA"
stones="aAbjhb"
a=0
for i in range(len(jewels)):
    for j in range(len(stones)):
        if(i==j):
            a=a+1
            break
print(a)

stones="abcABC"
jewels="abbaAB"
a=0
for i in range(len(jewels)):
    for j in range(len(stones)):
        print(jewels[i],stones[j])
        if(i==j):
            a=a+1
            break
print(a)

a=[1,2,3]
b=[4,5,6]
c=(a+b)
d=len(c)
print(d)
if(d%2==0):
    e=c//2
print(e)

a=[5,6,47,8,9,5]
b=len(a)
s=0
for i in range(b):
    c=a[i]
    s=max(c,s)
print(s)

a=["Iam pavani","Iam from BCA-AI","one of the system is not there"]
ans=0
for j in range(len(a)):
    ch=a[j]
   # print(ch)
    b = 1
    for i in range(len(ch)):
        s=ch[i]
        if(s==" "):
            b=b+1
    ans=max(ans,b)
print(b)

li=["pavani is a good girl"," she is studing in sgdc in mpl","pavani"]
ans=0
for j in range(len(li)):
    s=li[j]
    a=0
    for i in range(len(s)):
        ch=s[i]
        if(ch==" "):
            a=a+1
    ans=max(ans,a)
print(ans)

a=[[1,2,3,4],[4,5,6,7]]
b=len(a)
c=len(a[0])
for i in range(b):
    for j in range(1):
        print(a[i][3])

for i in range(3):
    for j in range(3):
        print("*",end="")
        if(j!=3-1):
            print("_",end="")
    print(" ")


r=8
c=3
for i in range(r):
    for j in range(c):
        print("*",end="")
        if(j!=c-1):
            print("_",end="")
    print(" ")

r=0
c=5
for i in range(r,6):
   # print("*",end=" ")
    for j in range(0,i):
        print("#",end=" ")
    print(" ")



rows = 5
cols = 10

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
a=[1,2,3,4,5,6]
b=len(a)
print(a)

r=4
c=30
for i in range(r):
    for j in range(c):
        if(i==0 or i==r-1  or j==0  or j==c-1):
            print("*",end="")
        else:
            print("",end=" ")
    print(" ")

r=4
c=8
for i in range(r):
    for j in range(c):
        if(i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
...
r=3
c=5
for i in range(r):
    for j in range(c):
        if(i==0 and j!=0 and j!=1 or i == 1 and j != 0 and j !=c-1 or i==2 and j!=c-2 and j!=c-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")

rows = 5  # Number of rows

for i in range(rows):
    spaces = " " * (2 * (rows - i - 1))  # Adding spaces for alignment
    stars = "* " * 3  # Printing three stars per row
    print(spaces + stars)



r=5

for i in range(r):
    for j in range(r-i):
        print("#",end=" ")
    print(" ")
r=6
c=4
c1=r-1
for i in range(r):
    for j in range(c1-i):
        print(" ",end=" ")
    for k in range(c):
        print("*",end="")
    print(" ")

r=10
c1=r-1
for i in range(r+1):
    for j in range(i):
        print(" ",end="")
    for k in range(c1):
        print("*",end="")
    print(" ")

r=8
c=r-1
c1=1
for i in range(r):
    for j in range(c-i):
        print(" ",end=" ")
    for k in range(c1+i):
        print("*",end=" ")
    for l in range(c1+i-1):
        print("*",end=" ")
    print(" ")
    --------
r=8
c=0
c1=r
for i in range(r+1):
    for j in range(c+i):
        print("*",end=" ")
    for k in range(c1-i):
        print(" ",end=" ")
    for l in range(c1-i):
        print(" ",end=" ")
    for m in range(c+i):
        print("*",end=" ")
    print(" ")
..............
r=6
c1=1
for i in range(r):
    for j in range(r-i):
        print("*",end=" ")
    for k in range(c1+i-1):
        print(" ",end=" ")
    for l in range(c1+i-1):
        print(" ",end=" ")
    for m in range(r-i):
        print("*",end=" ")
    print(" ")
"""
"""
a=[17,18,5,6,1]
l=len(a)
ans=[]
for i in range(l-1):
    temp=float("-inf")
    for j in range(i+1,l):
        temp=max(temp,a[j])
    ans.append(temp)
ans.append(-1)
print(ans)
"""
"""
print("optimal way")
li=[5,4,3,2,1]
l=len(li)
rmax=-1
for i in range(l-1,-1,-1):
    temp=li[i]
    li[i]=rmax
    rmax=max(rmax,temp)
print(li)
#........
"""

# print("swapping")
# a=2
# b=5
# t=a
# a=b
# b=t
# print(a,b)
# print("sorting in decending order")
# c=[0,1,4,6,3,2]
# c.sort(reverse=True)
# print(c)
print("bubble sort")
p=[0,7,2,5,6]
l=len(p)
for i in range(0,l-1):
    swapped=False
    for j in range(0,l-i-1):
        if(p[j]>p[j+1]):
            p[j],p[j+1]=p[j+1],p[j]
            swapped=True
    if(swapped==False):
        break
print(p)


print("dictionary")
li=[8,5,6,0,1,8,1,5,1]
n=len(li)
dici={}
for i in range(n):
    val=li[i]
    if val not in dici:
        dici[val]=1
    else:
        temp=dici[val]
        dici[val]=temp+1
print(dici)
       
# print("problems on dictionary")
# li=["apple","banana","carrot"]
# dici={}
# for i in li:
#     if i not in dici:
#         dici[i]=1
#     else:
#         dici[i]+=1
# for i in dici:
#     print(i,"->",dici[i])







