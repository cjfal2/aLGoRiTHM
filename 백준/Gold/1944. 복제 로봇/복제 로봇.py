from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline


def find(a):
    if rep[a] != a:
        rep[a] = find(rep[a])
    return rep[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        rep[a] = b
    else:
        rep[b] = a


def bfs(start, end):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[start[0]][start[1]] = 1
    q = deque([start])
    while q:
        x, y = q.popleft()
        if (x, y) == end:
            return visited[x][y] - 1
        for dx, dy in dix:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != "1":
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    print(-1)
    quit()


dix = ((1, 0), (-1, 0), (0, 1), (0, -1))
N, M = map(int, input().strip().split())
rep = [i for i in range(M + 2)]
# 판을 받아주고 S랑 K 찾기
sk = []
pan = []
sk_dict = dict()
number = 1
for n in range(N):
    temp = input().strip()
    for m in range(N):
        if temp[m] in "SK":
            sk.append((n, m))
            sk_dict[(n, m)] = number
            number += 1
    pan.append(temp)
# print(sk)
# sk 에 있는 애들을 돌리면서 (최단거리찾기) edge에 넣기
edge = []
for combi in combinations(sk, 2):
    d = bfs(*combi)
    edge.append([d, sk_dict[combi[0]], sk_dict[combi[1]]])
edge.sort()

# print(edge)
total = 0
for d, u, v in edge:
    root_u, root_v = find(u), find(v)
    if root_u != root_v:
        union(u, v)
        total += d
print(total)
