def bfs():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[sn][sm] = 1
    q = [(sn, sm)]
    while q:
        x, y = q.pop(0)
        if pan[x][y] == 'G':
            print('Shortest Path:', visited[x][y]-1)
            return
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != 'X':
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    print('No Exit')
    return

    
for _ in range(int(input())):
    N, M = map(int, input().split())
    pan = []
    for i in range(N):
        a = list(input())
        for j in range(M):
            if a[j] == 'S':
                sn, sm = i, j
        pan.append(a)
    bfs()