c = 0
while 1:
    M, N = map(int, input().split())
    if N == M == 0:
        break
    c += 1
    pan = [input() for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    answer = []
    for n in range(N):
        for m in range(M):
            if pan[n][m] == "*" and not visited[n][m]:
                visited[n][m] = 1
                eyes = []
                q = [(n, m)]
                eye_cnt = 0
                while q:
                    x, y = q.pop(0)
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        nx, ny = x + dx, y + dy
                        if N > nx >= 0 and M > ny >= 0 and pan[nx][ny] != "." and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            q.append((nx, ny))
                            if pan[nx][ny] == "X":
                                eyes.append((nx, ny))

                visit = set()
                for i, j in eyes:
                    if (i, j) not in visit:
                        eye_cnt += 1
                        visit.add((i, j))
                        q = [(i, j)]
                        while q:
                            x, y = q.pop(0)
                            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                                nx, ny = x + dx, y + dy
                                if N > nx >= 0 and M > ny >= 0 and pan[nx][ny] == "X" and (nx, ny) not in visit:
                                    visit.add((nx, ny))
                                    q.append((nx, ny))
                answer.append(eye_cnt)
    print("Throw", c)
    print(*sorted(answer))
    print()
