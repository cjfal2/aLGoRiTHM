def solution(maps):
    answer = []
    N = len(maps)
    M = len(maps[0])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for n in range(N):
        for m in range(M):
            if not visited[n][m] and maps[n][m] != 'X':
                q = [(n, m)]
                visited[n][m] = 1
                cnt = int(maps[n][m])
                while q:
                    x, y = q.pop(0)
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        nx, ny = x + dx, y + dy
                        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and maps[nx][ny] in '123456789':
                            q.append((nx, ny))
                            visited[nx][ny] = 1
                            cnt += int(maps[nx][ny])
                answer.append(cnt)
    return sorted(answer) if answer else [-1]