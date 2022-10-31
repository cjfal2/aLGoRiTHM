from copy import deepcopy


news = [[],[-1, 0],[-1, -1],[0, -1],[1, -1],[1, 0],[1, 1],[0, 1],[-1, 1]]
# 델타 리스트인데, 인덱스를 맞추려고 0번을 빈 칸으로 선언

def find(t, pan):
    """
    물괴기 찾는 함수
    4x4라서 다행
    없는 번호가 있어도 빠르게 돌기가능
    없는 번호면 False False False
    있는 번호면 x좌표 y좌표 True
    t : 찾을 물고기 번호
    pan : 물고기 들어있는 리스트
    """
    for x in range(4):
        for y in range(4):
            if pan[x][y][0] == t:
                return x, y, True
    return False, False, False


def dfs(xx, yy, su, ocean):
    """
    전체적으로 기본 베이스인 판은 [물고기번호, 방향] 이 들어있는데
    물고기가 먹히면 [0, 방향] 으로 판에 남아있음
    """
    global co
    co = max(co, su) # co랑 su랑 비교해서
    shark_d = ocean[xx][yy][1] # 상어의 방향 저장
    ocean[xx][yy][0] = "S" 

    # 돌려돌려 물괴기
    for target in range(1, 17):
        fish_x, fish_y, flag = find(target, ocean) # find함수로 찾고
        if flag: # 물고기가 아직 살아있다면
            dix = ocean[fish_x][fish_y][1] - 1 # 방향을 그 물고기의 방향의 -1 로 일단 저장
            # 왜냐하면 바로 +1 을 해줄것이기 때문
            while 1:
                dix += 1 # 물고기 방향을 돌리는 수식임
                if dix > 8: # dix가 8을 넘어가면 1로 저장해줌
                    dix = 1
                nx = fish_x + news[dix][0] # 현재 방향에서 조건에 맞는지 확인하기위해 한걸음 나아가봄
                ny = fish_y + news[dix][1]
                if 0 <= nx < 4 and 0 <= ny < 4 and ocean[nx][ny][0] != "S": # 바다 안쪽이며, 상어의 위치가 아니면
                    # 0인 자리는 상관없음, 상어자리만 아니면 됨
                    ocean[fish_x][fish_y][1] = dix # 그 물괴기 방향을 새롭게 저장해주고
                    ocean[fish_x][fish_y], ocean[nx][ny] = ocean[nx][ny], ocean[fish_x][fish_y] # 자리 바꿈
                    break # 바로 끝내줘야함 한 번만 바꾸면 됨
                # if에서 튕겼다면 while 초기로 돌아가서 방향이 바뀜

    ocean[xx][yy][0] = 0 # 상어 자리를 0으로 바꿔줘서 물고기를 소화까지시킴

    # 잡아먹기
    dx, dy = news[shark_d][0], news[shark_d][1] # 델타에서 상어 방향에 대한 델타 x,y를 뽑아옴
    nx, ny = xx, yy
    for _ in range(3):
        # 델타 방향으로 최대 3번 이동 가능하니까 range(3)
        # dx,dy를 계속 더해줌
        nx += dx
        ny += dy
        if 0 <= nx < 4 and 0 <= ny < 4 and ocean[nx][ny][0]: # sea 안쪽이고, 물고기가 아직 안잡아먹혔다면 
            dfs(nx, ny, su+ocean[nx][ny][0], deepcopy(ocean))
            # nx,ny는 잡아먹을 물고기의 좌표이고
            # 수를 바로 세주면서 들어감


sea = [[] for _ in range(4)]
for i in range(4):
    a,aa,b,bb,c,cc,d,dd = map(int, input().split())
    for A, B in [(a,aa),(b,bb),(c,cc),(d,dd)]:
        sea[i].append([A, B]) # 물고기 번호랑 방향은 계속 바뀌니까 리스트로 넣어줌

co = 0 # 번호 더하는 변수
dfs(0, 0, sea[0][0][0], sea) # 시작은 0, 0 이고 , 0, 0 에 있는 물고기 번호를 바로 넣어줌
print(co)