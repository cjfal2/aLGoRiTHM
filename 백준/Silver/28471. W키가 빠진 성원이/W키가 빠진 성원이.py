import sys
input = sys.stdin.readline

from collections import deque

N = int(input().strip())

pan = []
flag = True
for i in range(N):
    temp = list(input().strip())
    if flag:
        for j in range(N):
            if temp[j] == "F":
                p, q, flag = i, j, False
                break
    pan.append(temp)

answer = 0
q = deque([(p, q)])
while q:
    x, y = q.popleft()
    for dx, dy in (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1):
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and N > ny >= 0 and pan[nx][ny] == ".":
            answer += 1
            q.append((nx, ny))
            pan[nx][ny] = "#"

print(answer)