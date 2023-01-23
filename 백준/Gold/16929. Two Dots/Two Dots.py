def dfs(what, x, y, dot_num):
    # print(f'x:{x}, y:{y}')

    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        # print(f'x:{x}, y:{y}, nx:{nx}, ny:{ny}')
        # print()
        if N > nx >= 0 and M > ny >= 0:
            if not visited[nx][ny] and pan[nx][ny] == what:
                visited[nx][ny] = 1
                dfs(what, nx, ny, dot_num+1)
                visited[nx][ny] = 0
            elif dot_num >= 3 and n == nx and m == ny:
                print("Yes")
                quit()


N, M = map(int, input().split())
pan = [list(input()) for _ in range(N)]

for n in range(N):
    for m in range(M):
        visited = [[0 for _ in range(M)] for _ in range(N)]
        # print('what:', pan[n][m])
        visited[n][m] = 1
        dfs(pan[n][m], n, m, 0)
        
print('No')
