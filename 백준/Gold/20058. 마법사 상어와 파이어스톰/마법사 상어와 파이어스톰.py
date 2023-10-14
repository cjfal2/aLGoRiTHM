def find_cube(W):
    '''
    격자의 시작점을 찾아야함
    W: 2**L 의 값

    주위에 visited가 0이라면 돌리기
    뛰는 범위는 W만큼으로 설정한다. (행 열 모두)
    '''
    if W == 1:
        return

    for n in range(0, N, W):
        for m in range(0, N, W):
                rotate(n, m, W)


def rotate(sx, sy, k):
    '''
    시작 지점에서
    2**k * 2 ** k 에 해당하는 격자만 회전
    k == W
    '''
    temp = []
    for j in range(sy, sy+k):
        for i in range(sx+k-1, sx-1, -1):
            temp.append(pan[i][j])

    idx = 0
    for i in range(sx, sx+k):
        for j in range(sy, sy+k):
            pan[i][j] = temp[idx]
            idx += 1


def melt():
    '''
    녹아야하는 얼음을 melt_ice에 넣고 마지막에 한번에 녹이기
    '''
    melt_ice = set()
    for n in range(N):
        for m in range(N):
            x, y = n, m
            if pan[n][m]:
                num = 0
                for dx, dy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                    if N > dx >= 0 and N > dy >= 0 and pan[dx][dy]:
                        num += 1
                if num < 3:
                    melt_ice.add((n, m))
    for x, y in melt_ice:
        pan[x][y] -= 1


# 첫째 줄에 남아있는 얼음 A[r][c]의 합을 출력하고
# 둘째 줄에 가장 큰 덩어리가 차지하는 칸의 개수를 출력한다
# 단, 덩어리가 없으면 0을 출력한다.
M, Q = map(int, input().split())  # M: 격자 크기 2의 M승, Q: 마법 시젼 수
N = 2 ** M  # 격자 크기
pan = [list(map(int, input().split())) for _ in range(N)]  # 판
for what in list(map(int, input().split())):
    # 시전 마법 종류 (len(L) == Q), M 이하의 수
    find_cube(2**what)  # 돌리고
    melt()  # 녹이기

answer = 0
big = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
for n in range(N):
    for m in range(N):
        if not visited[n][m] and pan[n][m]:
            num = 1
            q = [(n, m)]
            visited[n][m] = 1
            answer += pan[n][m]
            while q:
                x, y = q.pop(0)
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = x + dx, y + dy
                    if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny] and pan[nx][ny]:
                        answer += pan[nx][ny]
                        num += 1
                        q.append((nx, ny))
                        visited[nx][ny] = 1
            big = max(big, num)

print(answer)
print(big)
