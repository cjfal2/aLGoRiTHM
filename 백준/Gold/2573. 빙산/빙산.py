from copy import deepcopy

N, M = map(int, input().split())
bingsan = [list(map(int, input().split())) for _ in range(N)]

def divide():
    '''
    빙산이 찢어졌나 확인
    '''
    visited = [[False for _ in range(M)] for _ in range(N)]
    total = 0
    for n in range(1, N-1):
        for m in range(1, M-1):
            if not visited[n][m] and bingsan[n][m]:
                total += 1
                if total >= 2:
                    print(year)
                    quit()
                visited[n][m] = True
                q = [(n, m)]
                while q:
                    x, y = q.pop(0)
                    for dx, dy in [[1,0],[-1,0],[0,-1],[0,1]]:
                        nx, ny = x + dx, y + dy
                        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and bingsan[nx][ny]:
                            q.append((nx, ny))
                            visited[nx][ny] = True
    return total

def melt():
    '''
    지구온난화 시키기
    '''
    before_bingsan = deepcopy(bingsan)
    for n in range(1, N-1):
        for m in range(1, M-1):
            if bingsan[n][m]:
                zero = 0
                for dx, dy in [[1,0],[-1,0],[0,-1],[0,1]]:
                    nx, ny = n + dx, m + dy
                    if N > nx >= 0 and M > ny >= 0 and before_bingsan[nx][ny] == 0:
                        zero += 1
                bingsan[n][m] -= zero
                if bingsan[n][m] <= 0:
                    bingsan[n][m] = 0
                

year = 0
a = 1
while a:
    a = divide()
    year += 1
    melt()
print(0)