N, M = map(int, input().split())
pan = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1
q = [(0, 0, pan[0][0], 0)]
answer = 0
while q:
    x, y, number, jump = q.pop(0)
    if (x, y) == (N-1, M-1):
        answer = jump
        break
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx * number, y + dy * number
        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny]:
            visited[nx][ny] = 1
            q.append((nx, ny, pan[nx][ny], jump+1))
            
print(answer if answer else "IMPOSSIBLE")