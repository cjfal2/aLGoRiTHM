def back(cnt, x, y, percent):
    global answer

    if cnt == K:
        answer += percent
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < (2*K+1) and 0 <= ny < (2*K+1) and (nx, ny) not in visited:
            visited.add((nx, ny))
            back(cnt+1, nx, ny, percent * choice[i])
            visited.remove((nx, ny))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

K, E, W, S, N = map(int, input().split())
choice = [E/100, W/100, S/100, N/100]
visited = set()
visited.add((K, K))
answer = 0
back(0, K, K, 1)
print(answer)
