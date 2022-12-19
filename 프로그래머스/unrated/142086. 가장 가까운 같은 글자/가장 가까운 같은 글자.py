def solution(s):
    check = []
    answer = []
    for i in s:
        if i not in check:
            answer.append(-1)
        else:
            answer.append(check[::-1].index(i)+1)
        check.append(i)    
    return answer