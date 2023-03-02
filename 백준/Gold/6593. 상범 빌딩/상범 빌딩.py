import sys
from collections import deque
input = sys.stdin.readline
delta = ((0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0))

def bfs(sero1, garo1):
    visited = []
    for _ in range(high):
        visited1 = [[0 for _ in range(sero1)] for _ in range(garo1)]
        visited.append(visited1)
    hh, gg, ss = start
    q = deque()
    visited[hh][gg][ss] = 1
    q.append((hh, gg, ss))
    while q:
        v, x, y = q.popleft()
        for dh, dx, dy in delta:
            nh = v + dh
            nx = x + dx
            ny = y + dy
            if high > nh >= 0 and garo1 > nx >= 0 and sero1 > ny >= 0 and visited[nh][nx][ny] == 0:
                if building[nh][nx][ny] == ".":
                    visited[nh][nx][ny]=visited[v][x][y] + 1
                    q.append((nh, nx, ny))
                elif building[nh][nx][ny] == "E":
                    print(f"Escaped in {visited[v][x][y]} minute(s).")
                    return
    print("Trapped!")


while 1:
    high, g, s = map(int, input().strip().split())
    if high == g == s == 0:
        break
    building = [[] for _ in range(high)]
    start = []
    flag = True
    for u in range(high):
        for k in range(g+1):
            a = list(input().strip())
            if not a:
                break
            if flag:
                for aa in range(len(a)):
                    if a[aa] == "S":
                        start = (u, k, aa)
                        flag = False
            building[u].append(a)
    bfs(s, g)
