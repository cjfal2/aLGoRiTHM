def pang():
    f = False
    memo = []
    visited = [[0 for _ in range(10)] for _ in range(N)]
    for i in range(N):
        for j in range(10):
            if not visited[i][j] and pan[i][j]:
                q = [(i, j)]
                visited[i][j] = 1
                what = pan[i][j]
                temp = [(i, j)]
                while q:
                    x, y = q.pop(0)
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        nx, ny = x + dx, y + dy
                        if N > nx >= 0 and 10 > ny >= 0 and not visited[nx][ny] and pan[nx][ny] == what:
                            visited[nx][ny] = 1
                            q.append((nx, ny))
                            temp.append((nx, ny))
                if len(temp) >= K:
                    memo.extend(temp)
                    f = True
    return memo, f


def gravity():
    for h in range(N, -1, -1):
        for w in range(10):
            x, y = h, w
            while 1:
                if N > x >= 0 and 10 > y >= 0 and N > x+1 >= 0 and pan[x][y] and not pan[x+1][y]:
                    pan[x+1][y] = pan[x][y]
                    pan[x][y] = 0
                    x += 1
                else:
                    break


N, K = map(int, input().split())
pan = [list(map(int, list(input()))) for _ in range(N)]

while 1:
    mem, flag = pang()
    if not flag:
        break
    for x, y in mem:
        pan[x][y] = 0
    gravity()

for p in pan:
    print(*p, sep="")
