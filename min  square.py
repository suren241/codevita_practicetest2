

for _ in range(int(input())):
    x=[]
    y=[]
    for _ in range(int(input())):
        a,b=map(int,input().split())
        x.append(a)
        y.append(b)
    s=max(x)-min(x)
    s1=max(y)-min(y)
    u=max(s,s1)**2
    print(u)
