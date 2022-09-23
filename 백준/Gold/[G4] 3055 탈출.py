def find_want(w):
    """
    목표물 w의 좌표를 찾아내는 함수
    :param w: 목표물
    :return: 좌표들( ex [x, y] )이 있는 리스트
    """
    H = []
    for i in range(R):
        for j in range(C):
            if justin[i][j] == w:
                H.append([i, j])
    return H


def water_bfs():
    """
    홍수를 내는 함수
    :return: 없어용
    """
    for _ in range(len(q)):
        x, y = q.pop(0)
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if R > nx >= 0 and C > ny >= 0:
                if justin[nx][ny] == '.':
                    justin[nx][ny] = '*'
                    q.append([nx, ny])


def sonic_bfs():
    """
    고슴 도치의 여행
    p : 도치의 위치 큐
    q : 물의 위치 큐
    :return: 선인장 or 이동거리
    """
    water_bfs()     # 시작하면 먼저 홍수를 한번 내줘야 한다.
    p = [sonic[0]]
    while p:
        for _ in range(len(p)):     # 소닉의 이동
            x, y = p.pop(0)
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx = x + dx
                ny = y + dy
                if R > nx >= 0 and C > ny >= 0:
                    if justin[nx][ny] == '.' and visited[nx][ny] == 0:      # 갈수 있고 아직 안갔으면
                        visited[nx][ny] = visited[x][y] + 1
                        p.append([nx, ny])
                    elif justin[nx][ny] == 'D':     # 비버의 동굴일 경우!
                        return visited[x][y]

        if q:       # q에 요소가 있으면 홍수 재발생
            water_bfs()
    return 'KAKTUS'     # 도착을 못하면 선인장 리턴!


R, C = map(int, input().split())
justin = [list(input()) for _ in range(R)]      # 비버의 굴이 있는 띠떱숲의 지도

water = find_want('*')      # 물은 시작점이 많을 수 있음
sonic = find_want('S')      # 고슴도치 위치
wall = find_want('X')       # 벽은 시작점이 많을 수 있음

visited = [[0 for _ in range(C)] for _ in range(R)]
visited[sonic[0][0]][sonic[0][1]] = 1
for x, y in wall:       # visited에 벽 표시
    visited[x][y] = 'X'

justin[sonic[0][0]][sonic[0][1]] = "."      # justin에서 고슴도치 위치를 홍수가 갈 수 있는 곳으로 설정
q = []      # 물의 시작점이 많은 케이스를 고려하여 for문을 돌려준다 그렇지 않으면 에러가 난다.
for qq in water:
    q.append(qq)

print(sonic_bfs())
