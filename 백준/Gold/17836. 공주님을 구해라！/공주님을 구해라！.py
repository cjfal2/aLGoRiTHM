def bfs(target):
    global answer

    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    q = [(0, 0, 0)]
    while q:
        x, y, c = q.pop(0)

        if target == "direct":
            if x == N-1 and y == M-1:
                answer.append(c)
                return

        elif target == "sword":
            if pan[x][y] == 2:
                answer.append(N+M-2-x-y+c)
                return
            
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != 1 and c+1 <= T:
                visited[nx][ny] = 1
                q.append((nx, ny, c+1))



N, M, T = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]

answer = []

bfs("direct")
bfs("sword")
if answer:
    answer = min(answer)
    print(answer) if answer <= T else print("Fail")
else:
    print("Fail")