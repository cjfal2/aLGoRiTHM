from collections import deque

def solution(maps):
    
    def find_lever(n, m):
        q = deque([(n, m)])
        visited = [[0 for _ in range(M)] for _ in range(N)]
        visited[n][m] = 1
        while q:
            x, y = q.popleft()
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nx, ny = x + dx, y + dy
                if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and maps[nx][ny] != "X":
                    if maps[nx][ny] == 'L':
                        return nx, ny, visited[x][y]
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
        return -1, -1, -1



    def find_exit(n, m, dist):
        q = deque([(n, m)])
        visited = [[0 for _ in range(M)] for _ in range(N)]
        visited[n][m] = dist
        while q:
            x, y = q.popleft()
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nx, ny = x + dx, y + dy
                if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and maps[nx][ny] != "X":
                    if maps[nx][ny] == 'E':
                        return visited[x][y] + 1
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
        return -1
        

    N = len(maps)
    M = len(maps[0])
        
    for n in range(N):
        for m in range(M):
            if maps[n][m] == 'S':
                i, j, distance = find_lever(n, m)
                if i == j == distance == -1:
                    return -1
                return find_exit(i, j, distance)