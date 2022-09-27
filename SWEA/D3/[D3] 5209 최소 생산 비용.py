def joongso(idx, co):
    global ans
    if co >= ans:
        return

    if idx == N:
        ans = co
        return
    for z in range(N):
        if visited[z] == 1:
            continue
        visited[z] = 1
        joongso(idx+1, co+L[idx][z])
        visited[z] = 0


for tc in range(int(input())):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    s = []
    ans = 1627834687132847
    visited = [0] * (N+1)
    joongso(0, 0)
    print(f'#{tc+1} {ans}')

