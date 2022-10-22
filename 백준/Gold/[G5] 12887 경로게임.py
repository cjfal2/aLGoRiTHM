N = int(input())
pan = list()
w = 0
for _ in range(2):
    a = list(input())
    pan.append(a)
    w += a.count('.')
if N == 1:
    if w == 1:
        print(0)
        quit()
    else:
        print(1)
        quit(0)
counts = [0]
for i in range(2):
    if pan[i][0] == '.':
        visited = [[0 for _ in range(N)] for _ in range(2)]
        visited[i][0] = 1
        q = [(i, 0)]
        while q:
            x, y = q.pop(0)
            for dx, dy in [[1, 0], [-1, 0], [0, 1]]:
                nx, ny = x + dx, y + dy
                if 2 > nx >= 0 and N > ny >= 0 and not visited[nx][ny] and pan[nx][ny] == '.':
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
        for v in visited:
            print(v)
        co = []
        for j in range(2):
            if visited[j][N-1]:
                co.append(visited[j][N-1])
        counts.append(w-min(co))
print(max(counts))