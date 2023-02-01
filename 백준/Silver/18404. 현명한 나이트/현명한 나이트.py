import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in (-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny]:
                if (nx,ny) in memo:
                    ans[memo_dict.get((nx,ny))] = visited[x][y]
                    memo.remove((nx,ny))
                    if not memo:
                        return
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1


N, M = map(int, input().strip().split())
ans = dict()
sx, sy = map(int, input().strip().split())
memo = set()
memo_dict = dict()
for i in range(M):
    ex, ey = map(int, input().strip().split())
    memo.add((ex-1, ey-1))
    memo_dict[(ex-1, ey-1)] = i

q = deque([(sx-1, sy-1)])
visited = [[0 for _ in range(N)] for _ in range(N)]
visited[sx-1][sy-1] = 1
bfs()
answer = []
for i, j in sorted(ans.items()):
    answer.append(j)
print(*answer)
