def omakase(shark_x, shark_y, size):
    road = [[False for _ in range(N)] for _ in range(N)] # 계속 road를 초기화 해주어야함
    road[shark_x][shark_y] = True # 시작점을 True 로

    now_fish = fish_total

    q = [(shark_x, shark_y, 0)]
    fishs = [] # 먹는 물고기 임시저장 리스트, 여기서 가장 가까운 물고기랑 조건에 맞는 물고기를 1개만 고를거임

    while q and now_fish: # q에 들어있는 만큼만 순회하고, 물고기가 있어야 순회
        x, y, move = q.pop(0)
        for dx, dy in [[-1, 0],[0, -1], [1, 0], [0, 1]]:
            nx, ny = x + dx, y +dy
            if N > nx >= 0 and N > ny >= 0 and not road[nx][ny]:
                road[nx][ny] = True # 일단 방문 길로 표시, 표시 안하면 되돌아가서 무한루프도는 불상사발생

                # 먹을 수 있는 물고기일 경우 일단 임시 저장, 뛰어넘어서 더 지나가지는 않음
                if 0 < sea[nx][ny] < size:
                    now_fish -= 1
                    fishs.append((nx, ny, move+1))

                # 같은 사이즈의 물고기이거나 0일 경우 지나갑니다~
                elif sea[nx][ny] <= size:
                    q.append((nx, ny, move+1))
    
    if fishs: # 후보 물고기 오마카세
        fishs.sort(key=lambda x:x[1]) # 3. 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기
        fishs.sort(key=lambda x:x[0]) # 2. 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기
        fishs.sort(key=lambda x:x[2]) # 1. 거리가 가까운 물고기
        a, b, c = fishs[0]
        return [a, b, c]
    else: # 아무것도 없어??.... 그러면 그냥 끝내..
        return



N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

fish_total = 0
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark = [i, j] # 처음 아기상어의 위치
            sea[i][j] = 0 # 처음 위치를 지나갈 수 있는 상태로 변경

        elif sea[i][j]: # 9가 아닌 숫자일 경우에는 물고기이므로 전체 물고기 수를 늘려줌
            fish_total += 1
size = 2 # 크기
exp = 0 # 경험치
total = 0 # 전체 이동 수

while fish_total: # 물고기가 있을 때만 돌거에요
    pinkpong = omakase(shark[0], shark[1], size) # bfs 시작~
    if pinkpong: # 오마카세가 나왔으면
        r_x, r_y, r_move = pinkpong
        
        fish_total -= 1 # 전체 물고기중에 하나 냠냠

        shark = [r_x, r_y] # 상어 위치 갱신
        
        sea[r_x][r_y] = 0 # 먹었으니 지나갈 수 있는 상태로 변경

        total += r_move # 해당 이동 수 만큼 토탈에 추가

        exp += 1 # 경험치 get
        if exp == size and size < 8: # 9보다 커질 경우 자기 자신을 잡아먹을? 가능성이 있어서..
            exp = 0 # 조건에 맞다면 경험치 초기화하고 레벨업
            size += 1
    else: # 이제 아무것도 못먹네.. 
        break

print(total)