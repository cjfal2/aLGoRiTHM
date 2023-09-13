def solution(triangle):
    N = len(triangle)
    temp = [[0 for _ in range(N)] for _ in range(N)]
    temp[-1] = triangle[-1]
    
    for t in range(N-2, -1, -1):
        for i in range(t+1):
            temp[t][i] = triangle[t][i] + max(temp[t+1][i], temp[t+1][i+1])

    return temp[0][0]