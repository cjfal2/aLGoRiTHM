A=list(map(int,input().split()))
x,y,r=map(int,input().split())
i=0
for a in A:
    i+=1
    if a==x:
        print(i)
        break
else:
    print(0)