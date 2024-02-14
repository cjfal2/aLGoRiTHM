def solution(k, m, score):
    answer = 0
    score.sort()
    while 1:
        if len(score) < m:
            break
            
        box = 999
        for _ in range(m):
            box = min(box, score.pop())
        answer += box * m
    return answer