import sys
input = sys.stdin.readline
from collections import deque


def fire_move():
    for _ in range(len(fire)):
        x, y = fire.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx = x + dx
            ny = y + dy
            if N > nx >= 0 and M > ny >= 0:
                if pan[nx][ny] == '.' or pan[nx][ny] == 'J':
                    pan[nx][ny] = 'F'
                    fire.append((nx, ny))


def run():
    fire_move()     
    p = deque()
    p.append(jihoon)
    while p:
        for _ in range(len(p)):   
            x, y = p.popleft()
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nx = x + dx
                ny = y + dy
                if N > nx >= 0 and M > ny >= 0:
                    if pan[nx][ny] == '.' and visited[nx][ny] == 0:    
                        visited[nx][ny] = visited[x][y] + 1
                        p.append((nx, ny))
                else:
                    print(visited[x][y])
                    return
        if fire:      
            fire_move()
    print("IMPOSSIBLE")
    return




N, M = map(int, input().strip().split())
pan = []
fire = deque()
for n in range(N):
    p = list(input().strip())
    for m in range(M):
        if p[m] == 'F':
            fire.append((n, m))
        elif p[m] == 'J':
            jihoon = (n, m)
    pan.append(p)
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[jihoon[0]][jihoon[1]] = 1

run()
