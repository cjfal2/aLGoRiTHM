co = 0
for i in range(1,int(input())+1):
    if i < 100:
        co+=1
    else:
        A = list(map(int,str(i)))
        Q = []
        for k in range(1,len(A)):
            Q.append(A[k]-A[k-1])
        if len(list(set(Q)))==1:
            co+=1
print(co)