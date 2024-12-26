N, M = map(int, input().split())
pan = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

section = 0
section_number = []
for n in range(N):
    for m in range(M):
        if pan[n][m] and not visited[n][m]:
            section += 1
            visited[n][m] = 1
            q = [(n, m)]
            cnt = 1
            while q:
                x, y = q.pop(0)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and pan[nx][ny]:
                        q.append((nx, ny))
                        cnt += 1
                        visited[nx][ny] = 1
            section_number.append(cnt)

section_number.sort()
print(section)
print(*section_number)