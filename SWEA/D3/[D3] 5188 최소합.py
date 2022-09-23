def dfs(x, y):
    global counts, ans, move

    if ans < counts:
        return

    if move == 2*(N-2)+3:
        ans = counts
        return

    for dx, dy in [[0, 1], [1, 0]]:
        nx = x + dx
        ny = y + dy
        if N > nx >= 0 and N > ny >= 0:
            move += 1
            s.append([nx, ny])
            counts += pan[nx][ny]
            dfs(nx, ny)
            move -= 1
            counts -= pan[nx][ny]
            s.pop()


for tc in range(int(input())):
    N = int(input())
    pan = [list(map(int, input().split())) for _ in range(N)]
    move = 1
    counts = pan[0][0]
    ans = 1111111111111111
    s = []
    dfs(0, 0)
    print(f'#{tc+1} {ans}')
