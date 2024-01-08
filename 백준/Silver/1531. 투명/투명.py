pan = [[0 for _ in range(100)] for _ in range(100)]
N, M = map(int, input().split())
for _ in range(N):
    sx, sy, ex, ey = map(lambda u: int(u) - 1, input().split())
    for x in range(sx, ex+1):
        for y in range(sy, ey+1):
            pan[x][y] += 1
answer = 0
for n in range(100):
    for m in range(100):
        if pan[n][m] > M:
            answer += 1
print(answer)