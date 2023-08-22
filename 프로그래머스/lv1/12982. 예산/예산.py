def solution(d, budget):
    answer = 0
    for a in sorted(d):
        budget -= a
        if budget < 0:
            break
        answer += 1
        
    return answer