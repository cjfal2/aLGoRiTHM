import sys
input = sys.stdin.readline

durl = {
    'D': (1,  0),
    'U': (-1,  0),
    'R': (0,  1),
    'L': (0, -1)
}


def dfs(x, y, uni):
    global ans
    if visited[x][y]:
        if visited[x][y] == uni:
            ans += 1
        return

    visited[x][y] = uni
    dx, dy = durl.get(pan[x][y])
    dfs(x + dx, y + dy, uni)


N, M = map(int, input().split())
pan = [input() for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

ans = uni = 0
for n in range(N):
    for m in range(M):
        uni += 1
        dfs(n, m, uni)

print(ans)

