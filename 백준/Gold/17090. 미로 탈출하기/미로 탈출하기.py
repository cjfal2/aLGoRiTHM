import sys
sys.setrecursionlimit(10000000)


N, M = map(int, input().split())
pan = [input() for _ in range(N)]

visited = [[-1 for _ in range(M)] for _ in range(N)]

dxrections = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1)
}


def dfs(x, y):
    if N > x >= 0 and M > y >= 0:
        if visited[x][y] != -1:
            return visited[x][y]            # 그곳의 탈출 가능 여부에 따라 탈출 가능

        visited[x][y] = 0                   # 방문처리
        dx, dy = dxrections.get(pan[x][y])  # 진행 방향
        visited[x][y] = dfs(x + dx, y + dy) # 재귀

        return visited[x][y]

    else:
        return 1  # 탈출 가능


answer = 0
for n in range(N):
    for m in range(M):
        answer += dfs(n, m) # dfs의 return값 탈출 가능 여부에 따라 0 또는 1이 더해짐
print(answer)
