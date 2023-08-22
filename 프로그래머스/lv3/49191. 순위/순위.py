def solution(n, results):
    answer = 0
    G = [[] for _ in range(n+1)]
    for a, b in results:
        G[a].append(b)
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if k in G[i] and j in G[k]:
                    G[i].append(j)
                    
    temp = [0 for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j in G[i]:
                temp[i] += 1
                temp[j] += 1
    
    for i in range(1, n+1):
        if temp[i] == n-1:
            answer += 1
    
    return answer