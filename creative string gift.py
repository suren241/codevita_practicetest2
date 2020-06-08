from collections import Counter
a,b=[int(x) for x in input().split()]
l=[]
s=''
for i in range(a):
    l.append(input())
for i in range(b):
    l2=[]
    [l2.append(j[i])for j in l]    
    count=Counter(l2)
    val=count.values()
    ky=count.keys()
    b=max(val)
    h=chr(133)
    for j in ky:
        if count[j]==b:
            h=min(j,h)
    s=s+h
print(s)
