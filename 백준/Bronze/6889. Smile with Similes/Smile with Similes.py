n = int(input())
m = int(input())
N = [input() for _ in range(n)]
M = [input() for _ in range(m)]
for a in N:
    for b in M:
        print(a, "as", b)