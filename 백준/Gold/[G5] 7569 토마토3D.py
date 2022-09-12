from collections import deque
import sys


def where(num):
    """
    :param num -> 1:싱싱 -1:썩은
    :return: 원하는 토마토의 리스트
    """
    w = list()
    for a in range(high):
        for b in range(sero):
            for c in range(garo):
                if tmt[a][b][c] == num:
                    w.append([a, b, c])
    return w


def cal():
    """
    결과를 계산하여 출력하는 함수
    :return: NONE
    """
    ans = 0
    for h in range(high):
        for s in range(sero):
            for g in range(garo):
                if visited[h][s][g] == 0:
                    print(-1)
                    return
                else:
                    if visited[h][s][g] > ans:
                        ans = visited[h][s][g]
    print(ans-1)


def bfs(start_list, garo1, sero1):
    global visited
    q = deque()
    for h, s, g in start_list:
        q.append((h, s, g))
        visited[h][s][g] = 1
    while q:
        v, x, y = q.popleft()
        # print(x, y)
        h0 = v
        h1 = v + 1
        h2 = v - 1
        if h1 < high and visited[h1][x][y] == 0 and tmt[h1][x][y] == 0:
            q.append((h1, x, y))
            visited[h1][x][y] = visited[h0][x][y] + 1
        if h2 >= 0 and visited[h2][x][y] == 0 and tmt[h2][x][y] == 0:
            q.append((h2, x, y))
            visited[h2][x][y] = visited[h0][x][y] + 1
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx = x + dx
            ny = y + dy
            if sero1 > nx >= 0 and garo1 > ny >= 0 and visited[h0][nx][ny] == 0 and tmt[h0][nx][ny] == 0:
                q.append((h0, nx, ny))
                visited[h0][nx][ny] = visited[h0][x][y] + 1


input = sys.stdin.readline
garo, sero, high = map(int, input().strip().split())
# 토마토 인풋 받기(3D)
tmt = []
for _ in range(high):
    tmt1 = [list(map(int, input().strip().split())) for _ in range(sero)]
    tmt.append(tmt1)
# 토마토 visited 만들기
visited = []
for _ in range(high):
    visited1 = [[0 for _ in range(garo)] for _ in range(sero)]
    visited.append(visited1)
# 썩은 토마토와 싱싱 토마토의 위치 찾기(높이, 세로, 가로)
where_ss = where(-1)
where_tmt = where(1)
for h, s, g in where_ss:
    visited[h][s][g] = -1

bfs(where_tmt, garo, sero)
cal()
