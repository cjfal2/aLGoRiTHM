import sys, heapq
input = sys.stdin.readline

M, N = map(int, input().strip().split())
pan = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1

q = []
heapq.heappush(q, (0, 0, 0))

answer = 0
while q:
    cnt, x, y = heapq.heappop(q)
    if x == N-1 and y == M-1:
        answer = cnt
        break
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny]:
            visited[nx][ny] = 1
            heapq.heappush(q, (cnt+1, nx, ny)) if pan[nx][ny] else heapq.heappush(q, (cnt, nx, ny))
print(answer)
