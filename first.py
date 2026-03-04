"""print("second largest element in an array")
a=list(map(int,input().split()))
l=len(a)
rmax1=rmax2=float('-inf')
for i in range(l):
    if(a[i]>rmax1):
        rmax2=rmax1
        rmax1=a[i]
       # print(rmax1)
    elif(a[i]>rmax2 and a[i]!=rmax1):
        rmax2=a[i]
        #print(rmax2)
if(rmax2==float('-inf')):
    print(-1)
else:
    print(rmax2)
    """
"""
print("move all zero's to the end of the array")
arr=[2,3,0]
n = len(arr)
j = 0 
for i in range(n):
    if arr[i] != 0:
        arr[j] = arr[i]
        j += 1
    #print(j)
for i in range(j, n):
    arr[i] = 0
print(arr)
print("reversing of an array")
a=[1,2,3,4]
n=len(a)
b=[]
for i in range(n-1,-1,-1):
    b.append(a[i])
print(b)
"""
"""
print("majority")
li=[1,1,2,2,2,1,1,1,2]
n=len(li)//2
dici={}
for i in li:
    if i not in dici:
        dici[i]=1
    else:
        dici[i]+=1
for i in dici:
    val=dici[i]
    if(val>n):
        ans=i
        break
print(ans)
#.....
li=[1,1,1,1,3,3,3,3,3]
n=len(li)//2
li.sort()
print(li[n])
#.............
print("good pairs in broot froce way")
li=[1,2,3,1,1,3]
n=len(li)
ans=0
for i in range(n):
    for j in range(n):
        if(li[i]==li[j] and i<j):
            print(i,j)
            ans=ans+1
print(ans)
#...........
li=[1,1,1,1,1,1]
n=len(li)
ans=0
k=n-1
ans=k*(k+1)//2
print(ans)
#.......
print("good pairs in optimal way")
a=[1,2,3,1,1,2]
dici={}
for i in a:
    if i in dici:
        dici[i]+=1
    else:
        dici[i]=1
ans=0
for i in dici:
    #print(dici[i])
    n=dici[i]
    ans=ans+n*(n-1)//2
print(ans)
#.....
"""
"""
jewels="aA"
stones="aAAbbbb"
dici={}
for i in stones:
    if i in dici:
        dici[i]+=1
    else:
        dici[i]=1
ans=0
for i in range(len(jewels)):
    ch=jewels[i]
    if ch in dici:
        ans+=dici[ch]
print(ans)
#timecomplexity is o(n)+o(k)
#................
"""
"""
print("decode the message")
key="the quick brown fox jumps over the lazy dog"
dici={}
temp=97
for i in key:
    if i!=" " and i not in dici:
        dici[i]=chr(temp)
        temp+=1
print(dici)
message="vkbs bs t suepuv" 
ans=" "
for i in message:
    if i==" ":
        ans+=" "
    else:
        ans+=dici[i]
print(ans)
#.............
key="zyxwuvtsqrponmlkjihgfedcba"
dici={}
temp=97
for i in key:
    if i!=" " and i not in dici:
        dici[i]=chr(temp)
        temp+=1
print(dici)
message="when you come home"
ans=" "
for i in message:
    if i==" ":
        ans+=" "
    else:
        ans+=dici[i]
print(ans)
#...........
"""
"""
print("isomorphic")
s="egf"
t="add"
dici={}
rev={}
iso=True
for i in range(len(s)):
    ch1=s[i]
    ch2=t[i]
    if ch1 not in dici and ch2 not in rev:
        dici[ch1]=ch2
        rev[ch2]=ch1
    elif ch1 in dici and dici[ch1]!=ch2:
        iso=False
        break
    elif ch2 in rev and rev[ch2]!=ch1:
        iso=False
        break
print(iso)
#.............
"""
"""
print("move all zeros to end")
arr=[2,4,0,6,8,0,9]
count=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[i],arr[count]=arr[count],arr[i]
        count+=1
print(arr) 
#.............
 """
"""
print("finding error number")
li=[1,2,2,4]
dup=-1
mis=-1
s=set()
for i in range(len(li)):
    val=li[i]
    if val not in s:
        s.add(val)
    else:
        dup=val
for i in range(1,len(li)+1):
    if i not in li:
        mis=i
print(dup,mis)
 #.............

print("subsarrays")
a=[1,2,3]
n=len(a)
ans=[]
for i in range(3):
    for j in range(i,n):
        temp=[]
        for k in range(i,j+1):
            temp.append(a[k])
        ans.append(temp)
print(ans)
#..........
s="pavani"
n=len(s)
ans=[]
for i in range(n):
    for j in range(i,n):
        temp=" "
        for k in range(i,j+1):
            temp+=s[k]
        ans.append(temp)
print(ans)
#..........
li=[5,9,1,8,7]   
n=len(li)
ans=0
for i in range(n):
    for j in range(i,n):
        temp=[]
        tsum=0
        for k in range(i,j+1):
            temp.append(li[k])
            tsum+=li[k]
        if(len(temp)==3):
            #print(temp,tsum)
            ans=max(ans,tsum)
print(ans)
#.........

print("sliding window")
li=[5,9,1,8,7]
n=len(li)
l=0
temp=0
ans=0
for r in range(n):
    temp+=li[r]
    if(r-l==3):
        temp-=li[l]
        l+=1
    if(r-l+1==3):
        ans=max(ans,temp)
print(ans)
#.........


print("slibing window")
li=[5,9,1,8,7]
n=len(li)
ans=0
l=0
temp=0
for r in range(n):
    temp+=li[r]
    if(r-l==3):
        temp-=li[l]
        l+=1
    if(r-l+1==3):
        ans=max(ans,temp)
print(ans)   
#...................
print('broot froce way')
s="xyzzaz"
n=len(s)
ans=0
for i in range(n):
    for j in range(i,n):
        temp=[]
        for k in range(i,j+1):
            temp.append(s[k])
        if(len(temp)==3 and len(set(temp))==3):
            print(temp)
            ans+=1
print(ans)
#...........
print("optimal way")
s="xyzzaz"
n=len(s)
l=0
ans=0
temp=[]
for i in range(n):
    temp.append(s[i])
    if(i-l==3):
        temp.pop(0)
        l+=1
    if(i-l+1==3 and len(set(temp))==3):
        print(temp)  
        ans+=1
print(ans)

#.......
print("using hash map")
s="xyzzaz"
n=len(s)
l=0
ans=0
k=3
dici={}
for r in range(n):
    if s[r] in dici:
        dici[s[r]]+=1
    else:
        dici[s[r]]=1
    if(r-l==k):
        dici[s[l]]-=1
        if(dici[s[l]]==0):
            dici.pop(s[l])
        l+=1
    if(len(dici)==k):
        ans+=1
print(ans)
#...........

print("minimum difference")
nums=[3,4,8,1,5]
n=len(nums)
nums.sort()
k=3
ans=float('inf')
for i in range(n):
    for j in range(i,n):
        temp=[]
        for m in range(i,j+1):
            temp.append(nums[m])
        if(len(temp)==k):
            last=temp[-1]
            first=temp[0]
            ans=min(ans,last-first)
print(ans)
#............
print("optimal way")
nums=[3,4,8,1,5]
nums.sort()
n=len(nums)
k=3
l=0
ans=float('inf')
for r in range(n):
    if(r-l==k):
        l+=1
    if(r-l+1==k):
        print(nums[l:r+1])
        ans=min(ans,nums[r]-nums[l])
print(ans)
#..........
print("array parition")
nums=[6,2,6,5,1,2]
n=len(nums)
nums.sort()
ans=0
for i in range(0,n,2):
    ans+=nums[i]
print(ans)
#.....
print("minimum cost of buying candies with discount")
cost=[6,5,7,9,2,2]
cost.sort()
ans=0
t=0
for i in range(len(cost)-1,-1,-1):
    if(t==2):
        t=0
    else:
        ans+=cost[i]
        t+=1
print(ans)
#..........
print("Minimum absolute difference pairs:")
arr = [1, 3, 6, 10, 15]
arr.sort()
ans = float('inf')
for i in range(1, len(arr)):
    #print(arr[i],arr[i-1])
    ans= min(ans, arr[i] - arr[i - 1])
for i in range(1, len(arr)):
    if arr[i] - arr[i - 1] == ans:
        print([arr[i - 1], arr[i]])
#............
print("two sum")
num=[2,4,11,3]
n=len(num)
target=6
ans=0
for i in range(n):
    for j in range(n):
        print(i,j)
        if(num[i]+num[j]==target):
            ans = [i, j]
            found = True
            break
    if found:
        break

print(ans)
#.........

print('''number of subarrays of size k and average greater 
than  or equal to threshold  in broot froce way''')
arr=[2,2,2,2,5,5,5,8]
n=len(arr)
ans=0
k=3
threshold=4
for i in range(n):
    for j in range(i,n):
        temp=[]
        tsum=0
        for m in range(i,j+1):
            temp.append(arr[m])
            tsum+=arr[m]
        if(len(temp)==k and (tsum/k)>=threshold):
            #print(temp,tsum)
            ans+=1
print(ans)
#............
print("optimal way")
arr=[2,2,2,2,5,5,5,8]
n=len(arr)
l=0
temp=0
k=3
threshold=4
ans=0
for r in range(n):
    temp+=arr[r]
    if(r-l==k):
        temp-=arr[l]
        l+=1
    if(r-l+1==k and (temp/k)>=threshold):
        #print(temp)
        #print(l,r,temp)
        ans+=1
print(ans)
#.............
print("variable slidiong window")
arr=[9,3,4,8,1]
n=len(arr)
l=0
temp=0
ans=0
k=10
for r in range(n):
    temp+=arr[r]
    while temp>k:
        temp-=arr[l]
        l+=1
    ans=max(ans,r-l+1)
print(ans)
#...........
arr=[0,1,3,1,1,6,7,1,0,1]
n=len(arr)
l=0
temp=0
ans=0
k=2
for r in range(n):
    if(arr[r]==1):
        temp+=1
    while temp> k:
        if(arr[l]==1):
            temp-=1
        l+=1
    ans=max(ans,r-l+1)
print(ans)
#.........

arr=[12,1,3,1,1,6,7,1,8,1]
n=len(arr)
l=0
temp=0
ans=0
k=2
for r in range(n):
    if(arr[r]%2!=0):
        temp+=1
    while temp> k:
        if(arr[l]%2!=0):
            temp-=1
        l+=1
    ans=max(ans,r-l+1)
print(ans)

#............
arr=[1,1,1,0,0,0,1,1,1,1,0]
n=len(arr)
ans=0
l=0
temp=0
k=2
for r in range(n):
    if(arr[r]==0):
        temp+=1
    while(temp>k):
        if(arr[l]==0):
            temp-=1
        l+=1
    ans=max(ans,r-l+1)
print(ans)

#.......
arr=[1,1,1,0,0,0,1,1,1,1,0]
n=len(arr)
l=0
cnt0=0
cnt1=0
ans=0
k=2
for r in range(n):
    if(arr[r]==1):
        cnt1+=1
    else:
        cnt0+=1
    while min(cnt0,cnt1)>k:
        if(arr[l]==1):
            cnt1-=1
        else:
            cnt0-=1
        l+=1
    ans=max(ans,r-l+1)
print(ans)
#.............

s="abcabcbb"
n=len(s)
ss=set()
l=0
ans=0
for r in range(n):
    val=s[r]
    if val not in ss:
        ss.add(val)
    else:
        while val in ss:
            ss.remove(s[l])
            l+=1
        ss.add(val)
    ans=max(ans,r-l+1)
print(ans)
#.........
arr=[0,1,2,2]
n=len(arr)
l=0
ans=0
dici={}
for r in range(n):
    if arr[r] not in dici:
        dici[arr[r]]=1
    else:
        dici[arr[r]]+=1
    while(len(dici)>2):
        dici[arr[l]]-=1
        if(dici[arr[l]]==0):
            dici.pop(arr[l])
        l+=1
    ans=max(ans,r-l+1)
print(ans)
#..........
"""
"""
print("functions")
def fun(s1,s2):
    for i in range(len(s1)):
        if(s1!=s2):
            return False
    return True
ans=fun("abc","aby")
print(ans)
#...........
def fun1(dicia,dicib):
    if len(dicia)!=len(dicib):
        return False
    for i in  dicia:
        if i not in dicib or dicia[i]!=dicib[i]:
            return False
    return True 
dicia={1:2,3:4}
dicib={1:2,3:6}
ans=fun1(dicia,dicib)
print(ans)
#.................
def fun(dicia,dicib):
    for i in range(len(s1)):
        if i not in dicia:
            dicia[i]=1
        else:
            dicia[i]+=1
    for i in range(len(s2)):
        if i not in dicib:
            dicib[i]=1
        else:
            dicib[i]+=1
    if(len(dicia)!=len(dicib)):
        return False
    for i in  dicia:
        if i not in dicib or dicia[i]!=dicib[i]:
            return False
    return True 
dicia={}
dicib={}
s1="abcab"
s2="abbca"
ans=fun(dicia,dicib)
print(ans)
#.................
print("number of anagrams")
def funa(dicia,dicib):
    if(len(dicia)!=len(dicib)):
        return False
    for i in  dicia:
        if i not in dicib or dicia[i]!=dicib[i]:
            return False
    return True
dicia={}
dicib={}
s="abcab"
p="abbca"
l=0
ans=[]
for i in p:
    if i not in dicib:
        dicib[i]=1
    else:
        dicib[i]+=1
for r in range(len(s)):
    if s[r] in dicia:
        dicia[s[r]]+=1
    else:
        dicia[s[r]]=1
    if(r-l==len(p)):
        dicia[s[l]]-=1
        if(dicia[s[l]]==0):
            dicia.pop(s[l])
        l+=1
    if(r-l+1==len(p)):
        if funa(dicia,dicib):
            ans.append(l)
print(ans)
#...........
nums=[2,3,1,2,4,3]
n=len(nums)
l=0
temp=0
ans=float('inf')
target=7
for r in range(n):
    temp+=nums[r]
    while(temp>=target):
      ans=min(ans,r-l+1)
      temp-=nums[l]
      l+=1
if(ans==float('inf')):
   print(0)
print(ans)
#................
def atmostk(nums,k):
    n=len(nums)
    l=0
    temp=0
    ans=0
    for r in  range(n):
        if(nums[r]%2==1):
          temp+=1
        while temp>k:
           if(nums[l]%2==1):
              temp-=1
           l+=1
        ans+=(r-l+1)
    return ans
nums=[6,1,2,1]
k=2
print(atmostk(nums,k)-atmostk(nums,k-1))
#print(atmostk(nums,k-1))

#..........
def atmostk1(nums,k):
    n=len(nums)
    l=0
    temp=0
    ans=0
    for r in  range(n):
        if(nums[r]==1):
          temp+=1
        while temp>k:
           if(nums[l]==1):
              temp-=1
           l+=1
        ans+=(r-l+1)
    return ans
nums=[1,0,1,0,1]
k=2
print(atmostk1(nums,k)-atmostk1(nums,k-1))




print("subarrays with k different integers ")
def atmostk(nums,k):
    l=0
    ans=0
    dici={}
    n=len(nums)
    for r in range(n):
        val=nums[r]
        if val not in dici:
            dici[val]=1
        else:
            dici[val]+=1
        while(len(dici)>k):
            lval=nums[l]
            dici[lval]-=1
            if(dici[lval]==0):
                dici.pop(lval)
            l+=1
        ans+=(r-l+1)
    return ans
nums=[1,2,1,2,3]
k=2
print(atmostk(nums,k)-atmostk(nums,k-1))

#.....................
"""
"""
nums = -123
r = 0
original = nums  
nums = abs(nums)  

count = len(str(abs(original)))
print(type(original))
print("Number of digits:", count)

while nums > 0:
    t = nums % 10
    r = r * 10 + t
    nums = nums // 10  

if original < 0:
    r = -r

print("Reversed number:", r)
#..........
"""
nums=[1,3,5,7]
l=len(nums)
sum=0
sum1=0
for i in range (l):
    if(i%2==0):
        sum+=nums[i]
    else:
        sum1+=nums[i]
s=sum-sum1
print(s)
#................
n=3
c=0
for a in range(1,n):
    b=n-a
    if '0' not in str(a) and '0' not in str(b):
        c+=1
print(c)
#.........................

