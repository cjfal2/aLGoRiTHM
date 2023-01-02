from collections import deque


while 1:
    M, N = map(int, input().split())
    if N == M == 0:
        break
    pan = []
    flag = True
    for n in range(N):
        p = input()
        pan.append(p)
        if flag:
            for m in range(M):
                if p[m] == '@':
                    sn, sm = n, m
                    flag = False
    cost = 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[sn][sm] = 1
    q = deque()
    q.append((sn, sm))
    while q:
        x, y = q.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != '#':
                visited[nx][ny] = 1
                cost += 1
                q.append((nx, ny))
    print(cost)