def solution(maps):
    answer = 0
    N, M = len(maps), len(maps[0])
    q = [(0, 0)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    while q:
        x, y = q.pop(0)
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and maps[nx][ny]:
                if nx == N-1 and ny == M-1:
                    return visited[x][y] + 1
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return -1