'''
공기청정기는 항상 1번 열, 크기는 두 행

1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
(r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
확산되는 양은 Ar,c/5이고 소수점은 버린다.
(r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.

# 1. 확산 시키기 => 동시에 일어나므로 새로운 배열을 만들어주면 어떨까
확산된 미세먼지들을 겹치면 다 더해줘야함
* 새로운 배열은 숫자가 아니라 배열이어야할 듯??..
공기청정기에 닿으면 없어짐


2. 공기청정기가 작동한다.
공기청정기에서는 바람이 나온다.
위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

# 2. 공기청정기 작동하기.
시계방향, 반시계방향 탐색 구현 + 미세먼지 이동 + 공기청정기(-1) 이랑 닿으면 없어짐
'''

R, C, T = map(int, input().split()) # RxC 방 T번 확산

pan = [] # 방
aircon = [] # 공기청정기 위치 [위, 아래]
for r in range(R):
    inp = list(map(int, input().split()))
    if not aircon:
        if inp[0] == -1:
            aircon.append((r, 0))
            aircon.append((r+1, 0))
    pan.append(inp)

#print("======")
# 동작하기
for _ in range(T):
    new_pan = [[0 for _ in range(C)] for _ in range(R)]
    new_pan[aircon[0][0]][aircon[0][1]] = -1
    new_pan[aircon[1][0]][aircon[1][1]] = -1

    ############# 확산 
    for r in range(R):
        for c in range(C):
            if pan[r][c] > 0:
                temp, cost = [], pan[r][c]//5 # temp: 이동할 좌표들, cost: 얼마나 이동하는지
                
                # 이동 가능한거 찾기
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = r + dx, c + dy
                    if R > nx >= 0 and C > ny >= 0 and pan[nx][ny] != -1:
                        temp.append((nx, ny))

                # 진짜 이동시키기, 새로운판에다가는 새로운판에 있는 값에 얹어서 더해줘야함
                new_pan[r][c] += (pan[r][c] - cost * len(temp))
                for x, y in temp:
                    new_pan[x][y] += cost
    ############

    ########### 공기청정기 발동, 밀어야하므로 발사 방향 반대로 접근
    # 위쪽 청정기
    x, y = aircon[0]
    # [위, 오른, 아래, 왼]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dix = 0 # 현재 방향
    while 1:
        nx, ny = x + dx[dix], y + dy[dix]
        # 벽에 박는 경우 방향 전환, 근데 벽이 nx가 아님
        if aircon[0][0] < nx or 0 > nx or C <= ny or 0 > ny:
            dix = (dix+1)%4
            continue
        # 공기청정기에 박는 경우 끝
        if nx == aircon[0][0] and ny == 0:
            break
        # 먼지인 경우 진행 반대 방향으로 땡겨옴
        if new_pan[nx][ny]:
            if x == aircon[0][0] and y == 0:
                new_pan[nx][ny] = 0
            else:
                new_pan[x][y] = new_pan[nx][ny]
                new_pan[nx][ny] = 0

        # 0이나 먼지일 경우
        x, y = nx, ny
            
    # 아래쪽 청정기
    x, y = aircon[1]
    # [아래, 오른, 위, 왼]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dix = 0 # 현재 방향
    while 1:
        nx, ny = x + dx[dix], y + dy[dix]
        # 벽에 박는 경우 방향 전환, 근데 벽이 0이 아님
        if R <= nx or aircon[1][0] > nx or C <= ny or 0 > ny:
            dix = (dix+1)%4
            continue
        # 공기청정기에 박는 경우 끝
        if nx == aircon[1][0] and ny == 0:
            break

        # 먼지인 경우 진행 반대 방향으로 땡겨옴
        if new_pan[nx][ny]:
            if x == aircon[1][0] and y == 0:
                new_pan[nx][ny] = 0
            else: 
                new_pan[x][y] = new_pan[nx][ny]
                new_pan[nx][ny] = 0

        # 0이나 먼지일 경우
        x, y = nx, ny

    ###########
    # 끝났으면 판 저장
    pan = new_pan
                
# 출력 확인
answer = 2 # -1 두개도 셀거기 때문
for v in pan:
    answer += sum(v)
print(answer)