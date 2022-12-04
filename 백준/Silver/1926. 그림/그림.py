from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
pictures = [list(map(int, input().strip().split())) for _ in range(N)]

total = 0
big_picture = 0
for n in range(N):
    for m in range(M):
        if pictures[n][m]:
            total += 1
            co = 1
            pictures[n][m] = 0
            q = deque()
            q.append((n, m))
            while q:
                x, y = q.popleft()
                for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    nx, ny = x + dx, y + dy
                    if N > nx >= 0 and M > ny >= 0 and pictures[nx][ny]:
                        pictures[nx][ny] = 0
                        co += 1
                        q.append((nx, ny))
            big_picture = max(big_picture, co)

print(total)
print(big_picture)
