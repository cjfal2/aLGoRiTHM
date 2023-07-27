def solution(k, score):
    answer = []
    temp = []
    for s in score:
        temp.append(s)
        temp.sort()
        
        if len(temp) == k+1: temp = temp[1:]
        answer.append(temp[0]) if temp else answer.append(s)

    return answer