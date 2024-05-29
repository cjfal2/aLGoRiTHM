N, M = map(int, input().split())
a = 0
for _ in range(N):
    if 0 not in set(list(map(int, input().split()))):
        a += 1
print(a)