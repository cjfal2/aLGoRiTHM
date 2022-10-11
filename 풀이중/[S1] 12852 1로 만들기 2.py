n=int(input())
d=[0]*(n+1)

for i in range(2,n+1):
    i2 = int(i/2)
    i3 = int(i/3)

    if (not i%2) and (not i%3):
        d[i]=min(d[i-1]+1,d[i2]+1,d[i3]+1)

    elif not i%2:
        d[i]=min(d[i-1]+1,d[i2]+1)

    elif not i%3:
        d[i]=min(d[i-1]+1,d[i3]+1)

    else:
        d[i]=d[i-1]+1
    print(i)
# print(d)
print(d[n])