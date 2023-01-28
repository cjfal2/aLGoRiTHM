import sys
input = sys.stdin.readline
from itertools import combinations


M, N = map(int, input().strip().split())
pan = [list(map(int, input().strip().split())) for _ in range(N)]

nums = list(range(0, 10)) * 3
# print(sorted(set(combinations(nums, 3))))
for comb in sorted(set(combinations(nums, 3))):
    for m in range(M):
        if pan[0][m] in comb:
            # print("comb:", comb)
            visited = [[0 for _ in range(M)] for _ in range(N)]
            visited[0][m] = 1
            q = [(0, m)]
            while q:
                x, y = q.pop(0)
                if pan[x][y] not in comb:
                    continue
                # print("x, y:", x, y, pan[x][y])
                if x == N-1:
                    print(*sorted(comb))
                    quit()
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = x + dx, y + dy
                    if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny] in comb:
                        q.append((nx, ny))
                        visited[nx][ny] = 1
            # print("===================")
print(*[-1,-1,-1])