def solution(tickets):
    answer = []
    check = [0 for _ in range(len(tickets))]
    
    def dfs(t):
        if len(t) == len(tickets) + 1:
            answer.append(t[:])
            return
        
        for x in range(len(tickets)):
            if not check[x]:
                if not t:
                    if tickets[x][0] == "ICN":
                        t.append(tickets[x][0])
                        t.append(tickets[x][1])
                        check[x] = 1
                        dfs(t)
                        check[x] = 0
                        t.pop()
                        t.pop()
                elif tickets[x][0] == t[-1]:
                    t.append(tickets[x][1])
                    check[x] = 1
                    dfs(t)
                    check[x] = 0
                    t.pop()
                
                    
    dfs([])
                
                
    return sorted(answer)[0]