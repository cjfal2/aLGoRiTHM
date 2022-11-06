N, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]

ans = 0
big = 0
for i in range(N):
    for j in range(M):
        if pan[i][j]:
            visited = [[0 for _ in range(M)] for _ in range(N)]
            visited[i][j] = 1
            nums = [(1, pan[i][j])]
            q = [(i, j)]
            huge = 0
            while q:
                x, y = q.pop(0)
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nx, ny = x + dx, y + dy
                    if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
                        huge = max(visited[nx][ny], huge)
                        nums.append((visited[nx][ny], pan[nx][ny]))
            # for v in visited:
            #     print(v)
            # print("------------")
            if big < huge:
                big = huge
                ans = nums[0][1]+nums[-1][1]
            elif big == huge:
                ans = max(ans, (nums[0][1]+nums[-1][1]))
print(ans)