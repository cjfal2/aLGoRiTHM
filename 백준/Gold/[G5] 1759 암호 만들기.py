from itertools import combinations

L, C = map(int, input().split())
M = sorted(list(input().split()))
X = list(combinations(M, L))
Q = []
U = ['a', 'i', 'u', 'e', 'o']
for i in X:
    a = 0
    z = 0
    for j in i:
        if j in U:
            a += 1
        else:
            z += 1
    if a >= 1 and z >= 2:
        Q.append(i)
for k in Q:
    print(*k, sep="")