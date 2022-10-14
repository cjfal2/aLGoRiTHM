from copy import deepcopy

# 조건에 맞는 위치인지 확인
def check(a,b,c,d):
    if MAX >= abs(pan[a][b] - pan[c][d]) >= MIN:
        return True
    return False


N, MIN, MAX = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]

# 바로 올려줄거라 -1 부터 시작
turn = -1
for tt in range(2000):
    # 이전과 달라진게 없으면 종료
    if tt > 0 and panbac == pan:
        break
    turn += 1
    visited = [[0 for _ in range(N)] for _ in range(N)]
    panbac = deepcopy(pan)
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                flag = False # 주위에 조건에 해당하는게 없을 수도 있어서
                temp = [pan[i][j]] # 인구수 담기
                deca = [(i, j)] # 인구수를 바꿀 좌표를 담기
                visited[i][j] = 1
                q = [(i, j)]
                while q:
                    x, y = q.popleft()
                    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        nx, ny = x + dx, y + dy
                        # 범위 안쪽이고 방문을 안했으며, deca에 좌표가 없으면서 동시에 check를 만족하면
                        if N > nx >= 0 and N > ny >= 0 and not visited[nx][ny] and (nx, ny) not in deca and check(x,y,nx,ny):
                            visited[nx][ny] = 1
                            q.append((nx, ny))
                            deca.append((nx, ny))
                            temp.append(pan[nx][ny])
                            flag = True
                if flag:
                    ts = sum(temp)//len(temp)
                    for n, m in deca:
                        pan[n][m] = ts
print(turn)