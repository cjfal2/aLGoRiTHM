from copy import deepcopy

def check(a,b,c,d):
    if MAX >= abs(pan[a][b] - pan[c][d]) >= MIN:
        return True
    return False


N, MIN, MAX = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]

turn = -1
for tt in range(2000):
    if tt > 0 and panbac == pan:
        break
    turn += 1
    visited = [[0 for _ in range(N)] for _ in range(N)]
    panbac = deepcopy(pan)
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                flag = False
                temp = [pan[i][j]]
                deca = [(i, j)]
                visited[i][j] = 1
                q = [(i, j)]
                while q:
                    x, y = q.pop(0)
                    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        nx, ny = x + dx, y + dy
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
