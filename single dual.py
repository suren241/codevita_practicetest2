for _ in range(int(input())):
   
    s=input()
    l=list(s)
    x=set(l)
    if(len(l)>len(x)):
        print("Yes")
    else:
        print("No")
