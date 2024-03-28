import sys
input = sys.stdin.readline


n = int(input())

A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab = dict()
for a in A:
    for b in B:
        v = a + b
        if v not in ab:
            ab[v] = 1
        else:
            ab[v] += 1


answer = 0
for c in C:
    for d in D:
        v = -(c + d)
        if v in ab:
            answer += ab[v]

print(answer)
