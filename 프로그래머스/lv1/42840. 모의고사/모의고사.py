def solution(answers):
    answer = []
    answers = list(map(str, answers))
    a=b=c=0
    
    a1 = "12345"
    b1 = "21232425"
    c1 = "3311224455"
    
    for idx in range(len(answers)):
        if answers[idx] == a1[idx%5]:
            a += 1
        if answers[idx] == b1[idx%8]:
            b += 1
        if answers[idx] == c1[idx%10]:
            c += 1
    
    temp = [a,b,c]
    MAX = max(temp)
    for k in range(3):
        if temp[k] == MAX:
            answer.append(k+1)
    
    return answer