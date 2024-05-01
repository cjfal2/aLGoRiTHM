def bfs():
    N = int(input())
    pan = [input() for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[0][0] = 1
    q = [(0, 0)]
    while q:
        x, y = q.pop(0)
        if x == y == N-1:
            return "Yes"
        for dx, dy in (1, 0), (0, 1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and N > ny >= 0 and pan[nx][ny] == "." and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
    return "No"
print(bfs())