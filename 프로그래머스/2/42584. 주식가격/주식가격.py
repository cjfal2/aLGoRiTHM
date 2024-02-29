def solution(prices):
    N = len(prices)
    
    answer = []
    for i in range(N):
        a = prices[i]
        cnt = 0
        for j in range(i+1, N):
            b = prices[j]
            cnt += 1
            if a > b:
                break
          
        answer.append(cnt)
    return answer