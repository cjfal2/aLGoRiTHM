def bfs(x, y):
    num = L[x][y] - 1
    co = 0
    q = list()
    q.append([x, y])
    while q:
        a, b = q.pop(0)
        co += 1
        num += 1
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]: # 우 하 좌 상
            nx, ny = a + dx, b + dy
            if N>nx>=0 and N>ny>=0 and L[nx][ny] == num+1:
                q.append([nx, ny])

    return co


for tc in range(int(input())):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    ans = [0 , 0]
    res = 0
    for x in range(N):
        for y in range(N):
            counts = bfs(x, y)
            if counts > res:
                ans = [L[x][y], counts]
                res = counts
            elif counts == ans[1]:
                MIN = min(ans[0], L[x][y])
                ans = [MIN, counts]
    print(f'#{tc+1}', *ans)
