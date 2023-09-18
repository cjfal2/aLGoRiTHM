def solution(land):
    answer = 0
    N = len(land)
    
    temp = [[0 for _ in range(4)] for _ in range(N)]
    temp[0] = land[0]
    
    for i in range(1, N):
        for j in range(4):
            MAX = 0
            for k in range(4):
                if j == k:
                    continue
                MAX = max(MAX, temp[i-1][k])
            temp[i][j] = land[i][j] + MAX
    

    return max(temp[-1])