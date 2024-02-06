from collections import deque

N, k = map(int, input().split())

lines = [list(map(int, list(input()))) for _ in range(2)]
visited = [[0 for _ in range(N)] for _ in range(2)]

q = deque()
q.append((0, 0, 1))

answer = 0

while q:
    x, y, t = q.popleft()

    if y >= N:
        answer = 1
        break

    if y < t - 1:
        continue

    if lines[x][y] == 0:
        continue

    if visited[x][y] != 0:
        continue

    visited[x][y] = 1

    q.append((x, y - 1, t + 1))
    q.append((x, y + 1, t + 1))
    q.append(((x + 1) % 2, y + k, t + 1))

print(answer)
