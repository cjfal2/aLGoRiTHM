from collections import deque
import sys


def bfs(start_list, garo1, sero1):
    global visited
    q = deque()
    for s, g in start_list:
        q.append((s, g))
        visited[s][g] = 1
    # print(q)
    while q:
        s1, g1 = q.popleft()
        # print(s1, g1)
        for ds1, dg1 in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ns1, ng1 = s1 + ds1, g1 + dg1
            if sero1 > ns1 >= 0 and garo1 > ng1 >= 0 and visited[ns1][ng1] == 0 and tmt[ns1][ng1] == 0:
                q.append((ns1, ng1))
                visited[ns1][ng1] = visited[s1][g1] + 1


input = sys.stdin.readline
garo, sero = map(int, input().strip().split())
tmt = [list(map(int, input().strip().split())) for _ in range(sero)]

visited = [[0 for _ in range(garo)] for _ in range(sero)]
where_ss = list()
for k in range(sero):
    for u in range(garo):
        if tmt[k][u] == -1:
            where_ss.append([k, u])

for m, n in where_ss:
    visited[m][n] = -1

where_tmt = list()
for k in range(sero):
    for u in range(garo):
        if tmt[k][u] == 1:
            where_tmt.append([k, u])

bfs(where_tmt, garo, sero)

# for h in visited:
#     print(h)

C = 0
co = 0
for k in range(sero):
    if not C:
        for u in range(garo):
            if visited[k][u] == 0:
                C = 1
                print(-1)
                if C:
                    break
            else:
                if visited[k][u] > co:
                    co = visited[k][u]
    if C:
        break
if not C:
    print(co-1)
