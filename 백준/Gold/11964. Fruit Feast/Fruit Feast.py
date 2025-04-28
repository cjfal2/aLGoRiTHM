import sys
from collections import deque

input = sys.stdin.readline

t, a, b = map(int, input().split())

v = [[0]*2 for _ in range(t+1)]  # v[x][0]: 물 안마심, v[x][1]: 물 마심
q = deque()
q.append((0,0))  # (현재 배부름, 물 마셨는지)

while q:
    x, w = q.popleft()
    
    # 오렌지 먹기
    if x+a <= t and not v[x+a][w]:
        v[x+a][w] = 1
        q.append((x+a, w))
    # 레몬 먹기
    if x+b <= t and not v[x+b][w]:
        v[x+b][w] = 1
        q.append((x+b, w))
    # 물 마시기
    if w == 0:
        nx = x//2
        if not v[nx][1]:
            v[nx][1] = 1
            q.append((nx,1))

ans = 0
for i in range(t+1):
    if v[i][0] or v[i][1]:
        ans = max(ans, i)

print(ans)
