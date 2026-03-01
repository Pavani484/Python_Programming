
'''import matplotlib.pyplot as plt
height=[10,20,30,40]
weight=[30,50,80,30]
plt.scatter(height,weight)
plt.xlabel(height)
plt.ylabel(weight)
plt.title("scatter diagram")
plt.show()
'''
''' 
import matplotlib.pyplot as plt
a=[10,20,30,40]
b=["A","B","C","D"]
plt.pie(a,labels=b)
plt.xlabel(a)
plt.ylabel(b)
plt.title("piechart")
plt.show()
''' 
''' 

import matplotlib.pyplot as plt
import numpy as np
a=np.random.randint(10,90,40)
bins=[10,30,50,70,80]
plt.xlabel("class interval")
plt.ylabel("age")
plt.title("histogram")
plt.hist(a,bins=bins)
plt.show()
''' 
''' 
import matplotlib.pyplot as plt
import numpy as np
#a = np.random.randint(10, 90, 40)
a=[10,20,36,45,40,50]
plt.plot(a)
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Line Chart")
plt.show()
''' 
#import pandas as pd
#df = pd.read_excel("D:/MPCE_Urban_1999_Exact.xlsx")
#print(df)
"""
#broot force way
colors=[1,1,1,6,1,1,1]
l=len(colors)
ans=0
for i in range(l):
    for j in range(l):
        if(colors[i]!=colors[j]):
            b=abs(i-j)
            ans=max(ans,b)
print(ans)
"""
"""#optimal way
colors=[2,4,5,6,8,2]
a=len(colors)
b=0
for i in range(a-1,-1,-1):
    if(colors[i]!=colors[0]):
        temp=i
        b=max(temp,b)
        break
#print(b)
"""
"""
colors=[2,4,5,6,8,2]
a=len(colors)
b=0
for i in range(a-1,-1,-1):
    if(colors[i]!=colors[0]):
        temp=i
        b=max(temp,b)
        break
    for i in range(a):
        if(colors[i]!=colors[a-1]):
            temp=a-1-i
            b=max(b,temp)
            break
print(b)
"""
