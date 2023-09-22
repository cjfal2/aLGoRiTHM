def solution(word):
    answer = set()
    s = []
    def dfs(length):
        if len(s) > length:
            return
        answer.add("".join(s))
        
        for i in "AEIOU":
            s.append(i)
            dfs(length)
            s.pop()
            
    for k in range(1, 6):
        dfs(k)
        
    answer = list(answer)
    answer.sort()
    a = answer.index(word)
    return a