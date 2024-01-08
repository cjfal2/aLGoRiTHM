pan = [[0 for _ in range(5)] for _ in range(5)]
K = int(input())
answer = 0
total = 25 - K
for _ in range(K):
    a, b = map(lambda x: int(x) - 1, input().split())
    pan[a][b] = 1


def back(x, y, g):
    global answer
    if x == 4 and y == 4:
        if total == g:
            answer += 1
        return

    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        if 5 > nx >= 0 and 5 > ny >= 0 and pan[nx][ny] == 0:
            pan[nx][ny] = 1
            back(nx, ny, g+1)
            pan[nx][ny] = 0


pan[0][0] = 1
back(0, 0, 1)
print(answer)
