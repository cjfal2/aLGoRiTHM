import sys
sys.setrecursionlimit(1000000)


N = int(input())
pan = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)] # 방문 배열, 해당 칸에는 x, y에서 시작했을 때 얼마나 멀리갈 수 있는지 저장되어 있음


def dfs(x, y):
    if visited[x][y]: # 이미 방문한 곳
        return visited[x][y]

    visited[x][y] = 1 # 방문 처리
    for nx, ny in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
        if N > nx >= 0 and N > ny >= 0 and pan[x][y] < pan[nx][ny]: # 문제 이동 조건
            visited[x][y] = max(visited[x][y], dfs(nx, ny)+1) # 방문 재처리

    return visited[x][y]


answer = 0 # 정답
for n in range(N):
    for m in range(N):
        answer = max(answer, dfs(n, m))
print(answer)
