sero, garo = map(int, input().split())
L = [list(input()) for _ in range(sero)]

distance = []
for s in range(sero):
    for g in range(garo):
        if L[s][g] == 'L':
            visited = [[-1 for _ in range(garo)] for _ in range(sero)]
            visited[s][g] = 0
            q = [(s, g)]
            while q:
                x, y = q.pop(0)
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nx, ny = x + dx, y + dy
                    if sero > nx >= 0 and garo > ny >= 0 and visited[nx][ny] == -1 and L[nx][ny] == "L":
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
            MAX = 0
            for i in range(sero):
                for j in range(garo):
                    if visited[i][j] > MAX:
                        MAX = visited[i][j]
            distance.append(MAX)
print(max(distance))
