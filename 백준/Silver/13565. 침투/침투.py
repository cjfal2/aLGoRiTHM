import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
pan = [list(map(int, list(input().strip()))) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]
flag = False
for i in range(N):
    for j in range(M):
        if not i and not visited[i][j]:
            visited[i][j] = True
            q = [(i, j)]
            while q:
                x, y = q.pop(0)
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nx, ny = x + dx, y + dy
                    if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and not pan[nx][ny]:
                        if nx == N-1:
                            print("YES")
                            quit()
                        visited[nx][ny] = True
                        q.append((nx, ny))
print("NO")
