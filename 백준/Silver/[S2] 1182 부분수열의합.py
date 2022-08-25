from itertools import combinations


N,target = map(int,input().split())
L = list(map(int,input().split()))

co = 0
for i in range(1,N+1):
    x = combinations(L,i)
    for y in x:
        if sum(y) == target:
            co+=1
print(co)