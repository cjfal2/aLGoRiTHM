import sys
input = sys.stdin.readline


def find(x):
    if rep[x] != x:
        rep[x] = find(rep[x])
        
    return rep[x]


def union(x, y):
    a = find(x)
    b = find(y)
    rep[a] = b
    c = min(L[a], L[b])
    L[a], L[b] = c, c

N, M, money = map(int, input().strip().split())
L = list(map(int, input().strip().split()))
rep = [i for i in range(N)]


for i in range(M):
    a, b = map(lambda x : int(x)-1, input().strip().split())
    if find(a) != find(b):
        union(a, b)

ans = 0
for v in range(N):
    if v == rep[v]:
        ans += L[v]
        if ans > money:
            print("Oh no")
            quit()
print(ans)
