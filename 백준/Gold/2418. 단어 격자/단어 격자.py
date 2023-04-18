dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def dfs(x, y, nxt):
    global memo, arr, target, H, W, L
    if nxt == L:
        return 1
    if memo[x][y][nxt] != -1:
        return memo[x][y][nxt]

    temp = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < H and 0 <= ny < W and arr[nx][ny] == target[nxt]:
            temp += dfs(nx, ny, nxt + 1)
    memo[x][y][nxt] = temp
    return temp


H, W, L = map(int, input().split())
arr = [input() for _ in range(H)]
target = input()
memo = [[[-1 for _ in range(101)] for _ in range(200)] for _ in range(200)]
ans = 0
for i in range(H):
    for j in range(W):
        if arr[i][j] == target[0]:
            ans += dfs(i, j, 1)
print(ans)
