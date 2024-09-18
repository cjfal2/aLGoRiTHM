A = int(input())
V, W = map(int, input().split())
M = V // W
if A <= M:
    print(1)
else:
    print(0)