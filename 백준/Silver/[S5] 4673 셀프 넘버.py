def sn(N):
    for i in range(N):
        A = 0
        for z in str(i):
            A += int(z)
        B = A+i
        if B==N:
            return -1
    return N

for i in [1,3,5,7,9]:
    print(i)
for i in range(20,10001):
    Z = sn(i)
    if Z!=-1:
        print(Z)