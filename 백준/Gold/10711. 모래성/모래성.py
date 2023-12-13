from collections import deque

direc = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

N, M = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]
q = deque()

for n in range(N):
    temp = input()
    for m in range(M):
        if temp[m] == '.':
            q.append((n, m))
            arr[n][m] = 0
        else:
            arr[n][m] = int(temp[m])

answer = 0

while q:
    for _ in range(len(q)):
        x, y = q.popleft()
        for dx, dy in direc:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and arr[nx][ny] > 0:
                arr[nx][ny] -= 1
                if arr[nx][ny] == 0:
                    q.append((nx, ny))
    if not q:
        break

    answer += 1

print(answer)
