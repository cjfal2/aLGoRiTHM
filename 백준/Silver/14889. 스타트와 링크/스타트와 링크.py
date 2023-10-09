def dfs(q):
    global answer

    if len(start) == N//2:
        link = []
        for x in range(N):
            if x not in start:
                link.append(x)

        t, k = 0, 0
        for i in range(N//2 - 1):
            for j in range(i+1, N//2):
                t += pan[start[i]][start[j]] + pan[start[j]][start[i]]
                k += pan[link[i]][link[j]] + pan[link[j]][link[i]]
        answer = min(answer, abs(t-k))
        return

    for i in range(q, N):
        if i not in start:
            start.append(i)
            dfs(i)
            start.pop()


N = int(input())
pan = [list(map(int, input().split())) for _ in range(N)]
start = []
answer = float("INF")
dfs(0)
print(answer)
