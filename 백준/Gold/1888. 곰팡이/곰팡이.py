from collections import defaultdict

N, M = map(int, input().split())
wall = [list(map(int, input())) for _ in range(N)]
total = N * M
mold = defaultdict(list)

def bfs(_i, _j):
    global mold
    q = [(_i, _j)]
    while q:
        _r, _c = q.pop(0)
        for _dr, _dc in (-1, 0), (1, 0), (0, 1), (0, -1):
            nr, nc = _r + _dr, _c + _dc
            if -1 < nr < N and -1 < nc < M and wall[nr][nc]:
                if visit[nr][nc] < day:
                    visit[nr][nc] = day
                    q.append((nr, nc))

def isLump():
    global mold
    cnt = 0
    for i in range(N):
        for j in range(M):
            if wall[i][j] and visit[i][j] != day:
                if cnt:
                    return False
                cnt += 1
                visit[i][j] = day
                bfs(i, j)
    return True

day = 0
visit = [[-1] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if wall[i][j]:
            mold[wall[i][j]].append((i, j))

while not isLump():

    mold = dict(sorted(mold.items(), reverse=1))

    for v, q in mold.items():
        new_q = []
        while q:
            r, c = q.pop(0)
            for nr in range(0 if (-1)*v+r <= 0 else (-1)*v+r, N if v+r >= N else v+r+1):
                for nc in range(0 if (-1)*v+c <= 0 else (-1)*v+c, M if v+c >= M else v+c+1):
                    if wall[nr][nc] < v:
                        wall[nr][nc] = v
                        new_q.append((nr, nc))
        mold[v] = new_q[:]
    day += 1


print(day)