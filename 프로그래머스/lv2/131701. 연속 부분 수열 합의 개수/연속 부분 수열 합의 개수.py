def solution(elements):
    answer = set()
    N = len(elements)
    elements *= 2
    for length in range(1, N+1):
        for i in range(N):
            answer.add(sum(elements[i:i+length]))
    
    return len(answer)