def solution(citations):
    answer = 0
    for a in range(len(citations)+1):
        x = 0
        for b in citations:
            if b >= a:
                x += 1
        if x >= a:
            answer = max(answer, a)
    
    return answer