'''
8 4
 0 1 0 1 0 1 1 1
0 1 1 0 0 1 0 0
 1 0 1 0 1 1 1 1
0 1 1 0 1 0 1 0

8 4
2 2 2 2 2 2 2 2 2 2
 2 0 1 0 1 0 1 1 1 2   홀
2 0 1 1 0 0 1 0 0 2    짝
 2 1 0 1 0 1 1 1 1 2
2 0 1 1 0 1 0 1 0 2
 2 2 2 2 2 2 2 2 2
아이디어:
0 이면 주변 1들을 찾음 ( 벽면 찾기 )
-> 가운데 쪽 0은 찾을 필요가 없음 -> n=0,N과 m=0,M에서 bfs로 찾은 뒤 주위 1의 수를 센다.

1 이면 외부를 찾음
-> 가운데 쪽 벽에 안붙은 1은 찾을 필요가 없음
->  n=0,N과 m=0,M에서 bfs로 찾은 뒤 메모 어펜드는 가장자리에 있는 부분만 주고 확인

- 확인법: 6방향체크 (패딩 때문에 홀짝 바뀜)
    - 짝수행 자리 : 위: (x-1, y-1), (x-1, y)  좌우 : (x, y+1), (x, y-1)  아래 : (x+1, y-1), (x+1, y)
    - 홀수행 자리 : 위: (x-1, y+1), (x-1, y)  좌우 : (x, y+1), (x, y-1)  아래 : (x+1, y+1), (x+1, y)

특이사항
    - M, N 으로 가야함
    - 이미 센 주위 것들을 체크해야함
    - 패딩을 줘야 편하지 않을까
'''
oddeven = {
    0: [(-1, -1), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 0)], # 짝
    1: [(-1, 1), (-1, 0), (0, 1), (0, -1), (1, 1), (1, 0)], # 홀
}


def bfs_zero(i, j):

    def check_around(p, q):
        global ans
        for dp, dq in oddeven.get(p%2):
            np, nq = p + dp, q + dq
            if pan[np][nq] == 1:
                ans += 1

    q = [(i, j)]
    visited[i][j] = 1
    check_around(i, j)
    while q:
        x, y = q.pop(0)
        for dx, dy in oddeven.get(x%2):
            nx, ny = x + dx, y + dy
            if not visited[nx][ny] and pan[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
                check_around(nx, ny)


def bfs_one(i, j):
    global ans
    q = [(i, j)]
    visited[i][j] = 1
    while q:
        x, y = q.pop(0)
        for dx, dy in oddeven.get(x%2):
            nx, ny = x + dx, y + dy
            if not visited[nx][ny]:
                if pan[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                elif pan[nx][ny] == 2:
                    ans += 1


M, N = map(int, input().split())
pan = [[2 for _ in range(M+2)]] +  [[2] + list(map(int, input().split())) + [2] for _ in range(N)] + [[2 for _ in range(M+2)]]
visited = [[0 for _ in range(M+2)]] + [[0] + [0 for _ in range(M)] + [0] for _ in range(N)] + [[0 for _ in range(M+2)]]

ans = 0

for n in (1, N): # 맨위 맨아래만 체크
    for m in range(1, M+1):
        if not visited[n][m]:
            if pan[n][m]:
                bfs_one(n, m)
            else:
                bfs_zero(n, m)

for m in (1, M): # 맨왼, 맨오른만 체크
    for n in range(1, N+1):
        if not visited[n][m]:
            if pan[n][m]:
                bfs_one(n, m)
            else:
                bfs_zero(n, m)

print(ans)