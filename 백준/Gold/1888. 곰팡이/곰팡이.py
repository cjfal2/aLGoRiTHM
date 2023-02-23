# 곰팡이가 피어있는 곳은 그 곰팡이의 자라는 속도
# 어느 곰팡이의 자라는 속도가 k라면, 하루가 지났을 때 그 곰팡이가 피어있던 자리를 중심으로 2k+1행 2k+1열의 격자에 같은 종의 곰팡이가 번진다는 의미이다.
# 만약 서로 다른 종의 곰팡이가 같은 칸에 번져 오면, 자라는 속도가 빠른 곰팡이가 그 칸을 차지한다.
# 곰팡이가 한 덩어리가 되기까지 걸리는 시간을 하루 단위로 출력한다.
from collections import deque

N, M = map(int, input().split())
pan = [list(map(int, input())) for _ in range(N)]

def check():
    '''
    덩어리를 확인할 함수
    '''
    number = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for n in range(N):
        for m in range(M):
            if not visited[n][m] and pan[n][m]:
                number += 1
                if number > 1: # 군집이 한 개가 넘어가면 바로 끊어줌

                    return False
                q = deque([(n, m)])
                visited[n][m] = 1
                while q:
                    x, y = q.popleft()
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        nx, ny = x + dx, y + dy
                        if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and pan[nx][ny]:
                            visited[nx][ny] = 1
                            q.append((nx, ny))
    return True # 군집이 한 개 이하라면 여기까지 옴

def bfs(i, j, velo):
    '''
    속도로 퍼트릴 함수
    속도 이하라면 잡아먹는다.
    '''
    for n in range(i-velo, i+velo+1):
        for m in range(j-velo, j+velo+1):
            # print(n, m)
            if N > n >= 0 and M > m >= 0 and pan[n][m] < velo:
                pan[n][m] = velo
                visit[n][m] = 1

ans = 0
while 1:
    if not ans and check():
        print(ans)
        break
    ans += 1
    visit = [[0 for _ in range(M)] for _ in range(N)]
    for p in range(N):
        for q in range(M):
            if pan[p][q] and not visit[p][q]:
                visit[p][q] = 1
                bfs(p, q, pan[p][q])

    if check():
        print(ans)
        break