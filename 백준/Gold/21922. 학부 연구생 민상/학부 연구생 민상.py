import sys
input = sys.stdin.readline

wall = {
    1: [(0, -1), (0, 1)], # 막음
    2: [(1, 0), (-1, 0)], # 막음
    3: [
        [(1, 0), (0, -1)],
        [(-1, 0), (0, 1)],
        [(0, 1), (-1, 0)],
        [(0, -1), (1, 0)],
    ],  # 반사
    4: [
        [(1, 0), (0, 1)],
        [(-1, 0), (0, -1)],
        [(0, 1), (1, 0)],
        [(0, -1), (-1, 0)],
    ],  # 반사
}

'''
1. 방향 전환
2. 멈추기
3. 계속가기

'''


N, M = map(int, input().strip().split())

pan = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
num = 0
for n in range(N):
    for m in range(M):
        if pan[n][m] == 9:
            visited[n][m] = 1
            num += 1
            x, y = n, m
            for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
                dx, dy = di, dj
                nx, ny = x, y
                while 1:
                    nx += dx
                    ny += dy
                    if N > nx >= 0 and M > ny >= 0:
                        if pan[nx][ny] == 0:
                            if not visited[nx][ny]:
                                visited[nx][ny] = 1
                                num += 1
                        elif pan[nx][ny] == 9:
                            continue
                        else:
                            if pan[nx][ny] == 1:
                                if (dx, dy) in [(0, -1), (0, 1)]:
                                    if not visited[nx][ny]:
                                        num += 1
                                        visited[nx][ny] = 1
                                    break
                                else:
                                    if not visited[nx][ny]:
                                        num += 1
                                        visited[nx][ny] = 1
                            elif pan[nx][ny] == 2:
                                if (dx, dy) in [(1, 0), (-1, 0)]:
                                    if not visited[nx][ny]:
                                        num += 1
                                        visited[nx][ny] = 1
                                    break
                                else:
                                    if not visited[nx][ny]:
                                        visited[nx][ny] = 1
                                        num += 1
                            elif pan[nx][ny] == 3:
                                for a, b in wall.get(3):
                                    if a == (dx, dy):
                                        dx, dy = b
                                        if not visited[nx][ny]:
                                            num += 1
                                            visited[nx][ny] = 1
                                        break
                            elif pan[nx][ny] == 4:
                                for a, b in wall.get(4):
                                    if a == (dx, dy):
                                        dx, dy = b
                                        if not visited[nx][ny]:
                                            num += 1    
                                            visited[nx][ny] = 1
                                        break
                    else:
                        break
# num = 0
# for b in visited:
#     num += sum(b)
print(num)