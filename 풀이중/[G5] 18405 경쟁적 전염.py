N, K = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

q = []
for i in range(N):
    for j in range(N):
        if L[i][j] != 0:
            q.append((L[i][j], i, j))
q.sort()

for _ in range(S):
    for _ in range(len(q)):
        virus, x, y = q.pop(0)
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if N > nx >= 0 and N > ny >= 0 and L[nx][ny] == 0 :
                L[nx][ny] = virus
                q.append((virus, nx, ny))

print(L[X-1][Y-1])