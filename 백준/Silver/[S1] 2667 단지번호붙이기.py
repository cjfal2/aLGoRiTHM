N = int(input())
L = [list(map(int, input())) for _ in range(N)]

total = 0 # 전체 단지의 수
danji = [] # 각 단지의 1의 수
for i in range(N):
    for j in range(N):   # 이중 뽀문 도는데 1찾으면 bfs
        if L[i][j] == 1:
            total += 1
            q = [(i, j)]
            cost = 1     # 제일 처음거를 찾았으니 1부터 시작
            L[i][j] = 0  # 찾았으니 처음거를 0으로 바꿔줌
            while q:     # bfs
                x, y = q.pop(0)
                for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                    nx, ny = x+dx, y+dy
                    if N > nx >= 0 and N > ny >= 0 and L[nx][ny] == 1:
                        L[nx][ny] = 0       # 0으로 덮어버려서 다시는 못찾게 함
                        cost += 1           # cost도 1개 늘려줌
                        q.append((nx, ny))  # bfs 돌 수 있게함
            danji.append(cost) # 다 돌았으면 danji에 append

danji.sort() # 출력을 위해 단지를 소트
# 출력
print(total)
for z in danji:
    print(z)
