import sys
sys.setrecursionlimit(10**6)

N = int(input())
pan = [input() for _ in range(N)]

## 갈수있는지 없는지 판단
visited = [[0 for _ in range(N)] for _ in range(N)]
visited[0][0] = 1
q = [(0, 0)]
flag = True
while q:
    x, y = q.pop()
    if x == y == N-1:
        flag = False
        break

    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != "#":
            visited[nx][ny] = 1
            q.append((nx, ny))

if flag:
    print("INCONCEIVABLE")
    quit()

## 우, 하 만 탐색
# 방문한 위치를 추적하는 2차원 리스트를 생성 초기값은 -1
visited = [[-1 for _ in range(N)] for _ in range(N)]

def dfs(x, y):  # 깊이 우선 탐색 함수를 정의,
    # x와 y는 현재 위치
    if x == y == N-1:  # 만약 현재 위치가 끝점이라면,
        return 1  # 1을 반환 이는 유효한 경로를 찾았음을 의미

    if visited[x][y] != -1:  # 만약 이미 방문했다면,
        return visited[x][y]  # 방문한 위치의 값을 반환

    roads = 0  # 현 위치에서 이동할 수 있는 경로의 수를 저장하는 변수
    for dx, dy in (1, 0), (0, 1):
        nx, ny = x + dx, y + dy
        # 만약 다음 위치가 판 내에 있고, 다음 위치가 벽이 아니라면,
        if N > nx >= 0 and N > ny >= 0 and pan[nx][ny] != "#":
            roads += dfs(nx, ny)  # 다음 위치로 이동하고, 그 위치에서 이동할 수 있는 경로의 수를 재귀로 탐색

    visited[x][y] = roads % 2147483647  # 현재 위치에서 이동할 수 있는 경로의 수를 저장

    return visited[x][y]  # 현재 위치에서 이동할 수 있는 경로의 수를 반환


dfs(0, 0)  # 시작점에서 DFS를 시작



# 시작점에서 이동할 수 있는 경로의 수를 출력
print(visited[0][0] if visited[0][0] else "THE GAME IS A LIE")
