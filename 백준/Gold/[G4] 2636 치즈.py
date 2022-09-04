from collections import deque
import sys


def bfs(sero1, garo1):
    visited = [[0 for _ in range(garo1)] for _ in range(sero1)]
    q = deque()
    for x, y in [[0, 0], [0, garo1-1], [sero1-1, 0], [sero1-1, garo1-1]]:
        q.append([x, y])
    c = 0
    while q:
        s1, g1 = q.popleft()
        for ds1, dg1 in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ns1, ng1 = s1 + ds1, g1 + dg1
            if sero1 > ns1 >= 0 and garo1 > ng1 >= 0:
                if visited[ns1][ng1] == 0 and cheese[ns1][ng1] == 0:
                    q.append([ns1, ng1])
                    visited[ns1][ng1] = 1

                elif cheese[ns1][ng1] == 1:
                    cheese[ns1][ng1] = 0
                    c += 1
                    visited[ns1][ng1] = 1
    return c


input = sys.stdin.readline
sero, garo = map(int, input().strip().split())
cheese = [list(map(int, input().strip().split())) for _ in range(sero)]
t = 0
ans = deque()
while 1:
    cz = bfs(sero, garo)
    if cz == 0:
        break
    ans.append(cz)
    t += 1
print(t)
print(ans[-1])
