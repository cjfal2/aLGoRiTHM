N, M = map(int, input().split())
pan = [input().strip() for _ in range(N)]
min_cost = float('inf')

for i in range(1, N-1):  # 흰색
    for j in range(i+1, N):  # 파란색
        cost = 0
        # 0부터 i-1까지는 흰색
        for x in range(i):
            cost += sum(1 for y in range(M) if pan[x][y] != 'W')

        # i부터 j-1까지는 파란색
        for x in range(i, j):
            cost += sum(1 for y in range(M) if pan[x][y] != 'B')

        # j부터 N-1까지는 빨간색
        for x in range(j, N):
            cost += sum(1 for y in range(M) if pan[x][y] != 'R')

        # 최소 비용 업데이트
        min_cost = min(min_cost, cost)

print(min_cost)
