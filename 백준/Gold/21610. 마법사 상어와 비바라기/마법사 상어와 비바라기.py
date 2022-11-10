from collections import deque
import sys
input = sys.stdin.readline

news = {
    1: (0, -1),
    2: (-1, -1),
    3: (-1, 0),
    4: (-1, 1),
    5: (0, 1),
    6: (1, 1),
    7: (1, 0),
    8: (1, -1),
}

N, M = map(int, input().strip().split())
pan = [list(map(int, input().strip().split())) for _ in range(N)]
cloud = deque()
c = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for aa in c:
    cloud.append(aa)

for _ in range(M):
    d, s = map(int, input().strip().split())
    dx, dy = news.get(d)
    zz = -1
    new_cloud = deque()
    for _ in range(len(cloud)):
        zz += 1
        x, y = cloud[zz]
        nx, ny = (x + s*dx)%N, (y + s*dy)%N
        pan[nx][ny] += 1
        new_cloud.append((nx, ny))
    for s, g in new_cloud:
        for ds, dg in [[-1, -1], [-1, 1], [1, 1], [1, -1]]:
            ns, ng = s+ds, g+dg
            if N > ns >= 0 and N > ng >= 0 and pan[ns][ng]:
                pan[s][g] += 1
    all_new_cloud = deque()
    for i in range(N):
        for j in range(N):
            if pan[i][j] >= 2 and (i, j) not in new_cloud:
                all_new_cloud.append((i, j))
                pan[i][j] -= 2
    cloud = all_new_cloud

print(sum(sum(pan,[])))
