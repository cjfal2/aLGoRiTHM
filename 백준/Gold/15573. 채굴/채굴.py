from collections import deque
import sys
input = sys.stdin.readline


def bfs(hard, s, t):
    global cnt
    visited[s][t] = 1
    q = deque([(s, t)])
    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if N+1 > nx >= 0 and M+2 > ny >= 0 and not visited[nx][ny] and 0 < pan[nx][ny] <= hard:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1


N, M, K = map(int, input().split())
pan = [[0 for _ in range(M+2)]] + [[0] +
                                   list(map(int, input().split())) + [0] for _ in range(N)]

D = 1000001
start = 1
end = 1000000
while start <= end:
    mid = (start+end)//2

    cnt = 0
    visited = [[0 for _ in range(M+2)] for _ in range(N+1)]
    for n in range(N+1):
        for m in range(M+2):
            if not pan[n][m] and not visited[n][m]:
                bfs(mid, n, m)

    # print(D, mid, start, end, cnt)
    target = D
    if cnt >= K:
        # D = min(D, mid)
        D = mid
        end = mid - 1
    else:
        start = mid + 1

    # print(target, mid)
    # if target > mid:
    #     end = mid - 1
    # elif target < mid:
    #     start = mid + 1
    # else:
    #     break
print(D)
