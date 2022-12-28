from collections import deque

N, M = map(int, input().split())
pan = []
flag = 0
for b in range(N):
    a = list(input())
    pan.append(a)
    for aa in range(M):
        if a[aa] == "I":
            s, e = b, aa
            pan[s][e] = "X"
visited = [[False for _ in range(M)] for _ in range(N)]
visited[s][e] = True
q = deque()
q.append((s, e))
ans = 0
while q:
    x, y = q.popleft()
    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny]:
            if pan[nx][ny] != "X":
                visited[nx][ny] = True
                q.append((nx, ny))
                if pan[nx][ny] == "P":
                    ans += 1
if ans:
    print(ans)
else:
    print("TT")