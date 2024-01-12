def dfs(x, y):
    global answer 

    if x == N+1 and y == 1: # 종료 조건: 마지막 꼭지점에서 놔야 하므로 한칸 더 넘어갔을 경우에 종료를 해줌
        # print("========")
        # for j in pan:
        #     print(*j)
        # print("--------")
        answer += 1
        return

    # 이동 방향: 기본적으로 오른쪽, 끝에 닿으면 한 칸 아래로 
    if y == M:
        nx, ny = x+1, 1
    else:
        nx, ny = x, y+1
    
    # 네모 안놓기
    dfs(nx, ny)

    # 네모 놓기: 놓은 부분이 터지지않게 확인
    if pan[x-1][y] == 0 or pan[x][y-1] == 0 or pan[x-1][y-1] == 0:
        pan[x][y] = 1
        dfs(nx, ny) # 다음 놓을 곳 이동은 이동 방향으로
        pan[x][y] = 0


N, M = map(int, input().split())
pan = [[0 for _ in range(M+1)] for _ in range(N+1)] # 왼쪽 대각선을 확인하기 때문에 0,0 이 아닌 1,1 부터 시작
answer = 0
dfs(1, 1)
print(answer)
