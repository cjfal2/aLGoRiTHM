def find(want):
    Q = []
    for i in range(N):
        for j in range(N):
            if shark[i][j] == want:
                a = abs(pong[0]-i)+abs(pong[1]-j)
                Q.append([i, j, a])
    Q.sort(key = lambda x: x[1])
    Q.sort(key = lambda x: x[0])
    Q.sort(key = lambda x: x[2])
    return Q


def ppp():
    for i in range(N):
        for j in range(N):
            if shark[i][j] == 9:
                return [i, j]


N = int(input())
shark = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
pong = ppp()
visited[pong[0]][pong[1]] = 1
size = 2
q = [pong]
while 1:
    x, y = q.pop(0)
    for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
        nx = x + dx
        ny = y + dy
        if N > nx >= 0 and N > ny >= 0 and shark[nx][ny] <= size:
            








