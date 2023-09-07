from collections import defaultdict


N, M = map(int, input().split())
info = defaultdict(list)
for _ in range(M):
    a, b, c, d = map(lambda x: int(x) - 1, input().split())
    info[(a, b)].append((c, d))


visited = [[[0, 0] for _ in range(N)] for _ in range(N)]
visited[0][0][0] = 1
visited[0][0][1] = 1

light = set()
light.add((0, 0))
q = [(0, 0)]
# answer = 1
while q:
    x, y = q.pop(0)
    temp = info.get((x, y))

    if temp:
        for i, j in temp:

            if not visited[i][j][1]:
                visited[i][j][1] = 1
                # answer += 1
                if (i, j) in light:
                    visited[i][j][0] = 1
                    # light.remove((i, j))
                    q.append((i, j))

    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny][0]:
            if visited[nx][ny][1]:
                visited[nx][ny][0] = 1
                q.append((nx, ny))
            else:
                light.add((nx, ny))
# print(answer)
# print(light)
answer = 0
for v in visited:
    for k in v:
        if k[1]:
            answer += 1
print(answer)