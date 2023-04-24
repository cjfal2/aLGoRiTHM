from collections import deque
import sys
input = sys.stdin.readline

tc = 1
while 1:
    N = int(input().strip())
    if not N:
        break
    L = [list(map(int, input().strip().split())) for _ in range(N)]
    visited = [[999999999 for _ in range(N)] for _ in range(N)]
    q = deque([(0, 0)])
    visited[0][0] = L[0][0]
    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and N > ny >= 0:
                coin = L[nx][ny]
                if visited[nx][ny] > visited[x][y] + coin:
                    visited[nx][ny] = visited[x][y] + coin
                    q.append((nx, ny))

    print(f'Problem {tc}: {visited[N-1][N-1]}')
    tc += 1
