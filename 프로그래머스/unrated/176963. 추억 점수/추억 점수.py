def solution(name, yearning, photo):
    answer = []
    temp = {}
    for i in range(len(name)):
        temp[name[i]] = yearning[i]
        
    for pho in photo:
        a = 0
        for p in pho:
            if temp.get(p):
                a += temp.get(p)
            
        answer.append(a)
        
    return answer