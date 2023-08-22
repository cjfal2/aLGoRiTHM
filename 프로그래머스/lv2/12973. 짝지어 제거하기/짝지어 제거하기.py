def solution(s):
    
    if len(s) % 2:
        return 0
    
    temp = []
    for i in range(len(s)):
        if not temp:
            temp.append(s[i])
        elif temp[-1] == s[i]:
            temp.pop()
        else:
            temp.append(s[i])

     
    return 0 if temp else 1