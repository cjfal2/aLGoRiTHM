from collections import deque

def solution(maps):
    
    def find(n, m, dist, what):
        q = deque([(n, m)])
        visited = [[0 for _ in range(M)] for _ in range(N)]
        visited[n][m] = dist
        while q:
            x, y = q.popleft()
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nx, ny = x + dx, y + dy
                if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and maps[nx][ny] != "X":
                    if maps[nx][ny] == what:
                        return nx, ny, visited[x][y]
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
        return -1, -1, -1
        

    N = len(maps)
    M = len(maps[0])
    for n in range(N):
        for m in range(M):
            if maps[n][m] == 'S':
                i, j, distance = find(n, m, 1, 'L')
                if i == j == distance == -1:
                    return -1
                i, j, distance = find(i, j, distance, 'E')
                return distance + 1 if i != -1 else -1